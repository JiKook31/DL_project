from keras.models import load_model
import pickle
import numpy as np

with open('x_set', 'rb') as fp:
    X = pickle.load(fp)

with open('y_set', 'rb') as fp:
    y = pickle.load(fp)

try:
    model = load_model("model_file/model.pt")
except:
    model = None
    print("Error with model file. Model could not be loaded")
    exit(1)

score = model.evaluate(X, np.array(y), verbose=0)

if score[1] < 0.75:
    print("Accuracy of the model is lower than required")
    exit(1)
else:
    print("Test on accuracy of the model is passed")