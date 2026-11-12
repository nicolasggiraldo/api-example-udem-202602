import pickle

def load_model(input_file):
    with open(input_file, 'rb') as file:
        model = pickle.load(file)
    return model