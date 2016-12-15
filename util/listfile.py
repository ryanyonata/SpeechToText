import os

def listfiles(directory):
    file_paths = []
    output_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
            output_paths.append("train\\" + root.split("\\")[-1] + "\\" + filename.split(".")[0] + ".mfc")

    return file_paths, output_paths

if __name__ == '__main__':
    lf, of = listfiles("D:\set_5-20161205T084921Z\set_5")
    for i in xrange(len(lf)):
        print lf[i] + " " + of[i]
