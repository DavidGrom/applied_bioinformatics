import argparse

def readfastq(InFile):
    filename = InFile
    names = []
    count = 0
    for line in open(filename):
        if line[0] == '@':
            count += 1
            names.append(line[1:])
    return print_seq(names, count)

def print_seq(sequences, numbers):
    print 'The total number of sequences is: ', numbers
    for name in sequences:
        print name

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--filename', help='Input fastq file.')
    args = parser.parse_args()
    #FileName = raw_input('Which fasta file do you want to check for sequences? >')
    readfastq(args.filename)
