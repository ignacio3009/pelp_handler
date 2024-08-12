import os

def get_file_list(input_dir):
    file_list = []
    for file in os.listdir(input_dir):
        if file.endswith('.csv'):
            file_list.append(file)
    return file_list