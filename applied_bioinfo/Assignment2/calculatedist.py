import argparse

def loop_over_files():
    for f in args.file:
        print f
        read_sequence()

def read_sequence(f):
    print 'Here I read in the sequence.'
    open(f)
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
    parser.add_argument('file', type=argparse.FileType('r'), nargs='+', help='Pass files to calculate their distance.')
    args = parser.parse_args()
    parser.print_help()

    loop_over_files()
