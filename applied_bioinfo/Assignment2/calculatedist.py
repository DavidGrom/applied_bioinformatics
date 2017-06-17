import argparse

def loop_over_files():
    names = []
    sequences = []
    sequence = ''
    line_num = -1
    print args.file
    for in_file in args.file:
        #read_sequence(in_file)
        print 'Read in sequence and its name and save to a list.'
        for line in open(in_file, 'r'):
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
        sequence = ''
    #print names
    #print sequences



#def read_sequence(filename):
    #print 'Here I read in the sequence.'
    #sequences = []
    #names = []
    #sequence = ''
    #line_num = -1
    #for line in open(str(filename), 'r'):
        #line = line.strip('\n')
        #if line[0] == '>':
            #name = line[1:]
            #names.append(name)
            #line_num += 1
            #print line_num
        #else:
            #if line_num > -1:
                #line = line.upper()
                #sequence += line
    #sequences.append(sequence)
    #return names
    #return sequences
    #save_names(name)
    #print sequences

#def save_names(name):
    #names = []
    #print 'Ja hoffe es klappt.'
    #names.append(names)
    #print names

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
