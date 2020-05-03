from keras.models import load_model

try:
    model = load_model("model_file/model.pt")
    print("\033[1;32;40m Model is succesfully loaded! \n")
except:
    print(f"\033[1;31;40m Error with model file. Model could not be loaded\n")
    exit(1)