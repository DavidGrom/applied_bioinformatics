import argparse

def loop_over_files():


    print args.file
    for in_file in args.file:
        read_sequence(in_file)

def read_sequence(filename):
    print 'Here I read in the sequence.'
    sequences = []
    names = []
    sequence = ''
    line_num = -1
    for line in open(str(filename), 'r'):
        line = line.strip('\n')
        if line[0] == '>':
            name = line[1:]
            names.append(name)
            line_num += 1
            #print line_num
        else:
            if line_num > -1:
                line = line.upper()
                sequence += line
    sequences.append(sequence)
    #return names
    #return sequences
    print names
    #print_names(names)

def print_names(names):
    print names
    print 'Ja hoffe es klappt.'
    for i in names:
        print 'Hallo'
        print i

def calculate_nucfreq():
    print 'Pass in the sequence and calculate the nucleotide frequency.'

def calculate_matrix():
    print 'Calculate distance matrix.'

def create_matrix():
    print 'Create the distance matrix.'


if __name__ == '__main__':
    # type.argparse.FileType('r') tries to open each argument as a file and generated an error if not possible
    # Doing this it checks if every input is a valid and readable file
    parser = argparse.ArgumentParser(description='Process some files.', epilog='Input fasta files to generate a distance matrix.')
    parser.add_argument('file', nargs='+', help='Pass files to calculate their distance.')
    args = parser.parse_args()
    parser.print_help()

    loop_over_files()
