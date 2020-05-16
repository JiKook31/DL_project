from keras.models import load_model
import pickle
import numpy as np

with open('x_set', 'rb') as fp:
    X = pickle.load(fp)

with open('y_set', 'rb') as fp:
    y = pickle.load(fp)

model = load_model("model_file/model.pt")

score = model.evaluate(X, np.array(y), verbose=0)

if score[1] < 0.75:
	print("\033[1;31;40m Accuracy of the model is lower than required. It should be more than 75.\n")
	exit(1)
else:
	print("\033[1;32;40m Test on accuracy of the model is passed  \n")