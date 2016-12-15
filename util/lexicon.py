import sys

def read_lexicon(input_file):
    lex = []
    with open(input_file, "r") as f:
        for line in f:
            arr = line.split(" ", 1)
            lex.append(arr)

    return lex

def write_new_lexicon(lexicon, output_file):
    with open(output_file, "w") as f:
        for lex in lexicon:
            f.write("%s\t[%s]\t%s" % (lex[0], lex[0], lex[1]))

def main(input_file, output_file):
    lex_list = read_lexicon(input_file)
    write_new_lexicon(lex_list, output_file)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
