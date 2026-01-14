import os

def get_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'names.txt')

    with open(file_path) as f:
        names = f.read()

    names = names.split()
    return names
