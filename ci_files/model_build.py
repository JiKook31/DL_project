import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Model, Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional


with open ('ci_files/x_set', 'rb') as fp:
    X = pickle.load(fp)

with open ('ci_files/y_set', 'rb') as fp:
    y = pickle.load(fp)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

input_layer = Input(shape=(56,))
model = Embedding(input_dim=26302, output_dim=56, input_length=56)(input_layer)
model = Dropout(0.1)(model)
model = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(model)
out = TimeDistributed(Dense(17, activation="softmax"))(model)

model = Model(input_layer, out)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train, np.array(y_train), batch_size=32, epochs=1, validation_split=0.2, verbose=1)

model.save("model.pt")