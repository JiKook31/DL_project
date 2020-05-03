from keras.models import load_model

try:
    model = load_model("model_file/model.pt")
    print("Model is succesfully loaded!")
except:
    model = None
    print("Error with model file. Model could not be loaded")
    exit(1)