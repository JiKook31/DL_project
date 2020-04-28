from model.paraphrase.predict import Predict
import torch

def paraphrase(sent, paraphraser, num):
    para_list = [paraphraser.infer(sent)]
    for i in range(1,num):
        new_para = paraphraser.infer(para_list[i-1])
        para_list.append(new_para)
    return para_list

def translate(sent, translator):
    return translator(sent)

def para_translate(sentence, num_paras=3):
    translator = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.ru-en.single_model', tokenizer='moses', bpe='fastbpe')
    paraphraser = Predict(checkpoint='checkpoint_coco', directory='paraphrase/coco')

    sent_trans = translate(sentence, translator)
    sent_paras = [sent_trans]
    sent_paras.extend(paraphrase(sent_trans, paraphraser, num_paras))

    return sent_paras