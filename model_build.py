import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Model, Input
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional

def preprocess_conll_file(filename, output_filename):
  '''
  refactors the conll dataset file from the 'filename' path
  gets rid of unnecessary colums, changes the structure and format of the file
  and writes the result to 'output_filename', the final structure is:
  sentence_index,word,ner_tag
  '''
  with open(filename) as conll_file:
      lines = conll_file.readlines()

  sentence_idx = 0
  result = 'sentence_idx,word,tag\n'
  for line in lines:
      splitted = line.split()
      if len(splitted) > 1:
          word = splitted[0]
          tag = splitted[2]
          if not word.__contains__(',') and not word.__contains__('"'):
              result += f'{sentence_idx},{word},{tag}\n'
      else:
          sentence_idx += 1

  f = open(output_filename, "w+")
  f.write(result)


preprocess_conll_file("conll.txt", "dataset.csv")
dataset = pd.read_csv("dataset.csv", error_bad_lines=False)


class SentenceGetter(object):
    '''
    this class converts text representation of sentences in the dataset
    to the list representation
    list of tuples is a sentence
    tuple is (word,tag)
    '''

    def __init__(self, dataset):
        self.dataset = dataset
        self.empty = False
        self.n_sent = 1
        aggregation_function = lambda s: [(w, t) for w, t in zip(s["word"].values.tolist(), s["tag"].values.tolist())]
        self.grouped = self.dataset.groupby("sentence_idx").apply(aggregation_function)
        self.sentences = [s for s in self.grouped]

    def get_next(self):
        try:
            s = self.grouped["Sentence: {}".format(self.n_sent)]
            self.n_sent += 1
            return s
        except:
            return None

getting_sents = SentenceGetter(dataset)
sentences = getting_sents.sentences

# getting list and count of words
words = list(set(dataset["word"].values))
words.append("END")
n_words = len(words)

# getting list and count of tags
tags = list(set(dataset["tag"].values))
n_tags = len(tags)

# getting max length of a sentence for future padding
maxlen = max([len(s) for s in sentences])

# assigning an index to each word and tag and generating dictionary
word2idx = {w: i for i, w in enumerate(words)}
tag2idx = {t: i for i, t in enumerate(tags)}

# converting words into indexes
X = [[word2idx[w[0]] for w in s] for s in sentences]
X = pad_sequences(maxlen=maxlen, sequences=X, padding="post",value=n_words-1)

# converting tags into indexes
y = [[tag2idx[w[1]] for w in s] for s in sentences]
y = pad_sequences(maxlen=maxlen, sequences=y, padding="post", value=tag2idx["O"])
y = [to_categorical(i, num_classes=n_tags) for i in y]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

input_layer = Input(shape=(maxlen,))
model = Embedding(input_dim=n_words, output_dim=maxlen, input_length=maxlen)(input_layer)
model = Dropout(0.1)(model)
model = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(model)
out = TimeDistributed(Dense(n_tags, activation="softmax"))(model)

model = Model(input_layer, out)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train, np.array(y_train), batch_size=32, epochs=1, validation_split=0.2, verbose=1)

model.save("model.pt")

import os
print(os.path.abspath("model.pt"))