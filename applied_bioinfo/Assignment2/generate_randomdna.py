import random

def generate(x):
    '''The function generated a random DNA sequence depending on user input.'''
    #ask user for length of random sequence
    #create variable that is used to save the created string to
    assert x > 0, 'The input must be a greater than 0'
    #assert int(x), 'The input must be a number.'
    random_dna = ''
    #random.seed(1234)
    #Human GC content is around 40% so like this I try to account for the distribution
    weighted_choices = [('A', 3), ('T', 3), ('C', 2), ('G', 2)]
    distribution = [base for base, y in weighted_choices for i in range(y)]
    print distribution #to check if it worked
    #loop through random choices as often as the user wanted to
    for i in range(x):
        #here: think about a way that skews the random choice towards biological reality
        base = random.choice(distribution)
        random_dna += base
    return print_dna(random_dna)

def print_dna(random_dna):
    #output is supposed to be in valid fasta format
    print 'The following k-mer has been generated and is in fasta format:'
    print '>randomsequence \n', random_dna

#def generate_dna(x):
#    for i in range(x):
#   geht das wenn user input in main erfolgt
#   und ich generate_dna() dann in main() aufrufe?
#
#
if __name__ == '__main__':
    dna_length = int(raw_input('Please, state the length of the k-mer you want to generate: >'))
    generate(dna_length)
