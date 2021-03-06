import flask
import telebot
import time
import logging
import os
import json
from model.para_trans import loadmodel, para_translate_preloaded


LOG_FORMAT = '%(levelname)s %(name)s:%(lineno)d:%(funcName)s: %(message)s'
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


API_TOKEN = os.getenv("TOKEN")

WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PORT = os.getenv('WEBHOOK_PORT')




WEBHOOK_SSL_CERT = './cert/cert.pem'
WEBHOOK_SSL_PRIV = './cert/key.pem'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)


bot = telebot.TeleBot(API_TOKEN)
server = flask.Flask(__name__)

LOGGER.info("Starting loading model")
translator, paraphraser = loadmodel()
LOGGER.info("Model Loaded")


@server.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        print(update)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    text = 'Hello!'
    bot.send_message(chat_id=message.chat.id, text=text)



@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    LOGGER.info(f"Requested translate for '{text}'")
    output = para_translate_preloaded(translator, paraphraser,text)
    LOGGER.info(f"Translate for '{text}' is '{output}'")
    bot.reply_to(message, text=output)


if __name__ == '__main__':

    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))

    server.run(host='0.0.0.0',
               port=WEBHOOK_PORT,
               ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
               debug=False)

    LOGGER.info("Bot started")
