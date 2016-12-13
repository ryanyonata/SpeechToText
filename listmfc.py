import os

def listfiles(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

if __name__ == '__main__':
    lf = listfiles("train\\")
    for files in lf:
        print files
