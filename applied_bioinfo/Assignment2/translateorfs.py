#!/usr/bin/env python

def getsequence(InFileName):
    """Reads in a fasta file into a list"""
    InFile = open(InFileName, 'r')
    LineNumber = -1
    sequences = []
    print 'The file is searched for sequences...'
    for line in InFile:
        line = line.strip('\n')
        if line[0] =='>': #checks if the current line is the beginning of a new seq
            name = line[1:] # if yes, saves the name by chopping off '>'
            sequences.append([name, '']) # saves the name to a list and creates a string entry to it
            LineNumber += 1 # increases the line number to start the record
        else: # we are on a line containg sequence
            if LineNumber > -1: # checks if we passed a name line
                line = line.upper()
                sequences[LineNumber][1] += line # adds the line to the corresponding name entry
    #for seq in sequences: run for debugging
        #print seq[0],':',seq[1]
    #print sequences
    return sequences

def reversecomplementsequence(sequences):
    print 'The sequence is now reversed and the complementary strand created...'
    revsequences = [] # create a list to store all reversed complementary sequences
    complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'} # create a dictionary as basis for base switch
    for seq in sequences: # loop through all the entries in sequences
        # for entry 1 in seq (the actual sequence not the name) replace each base according to complement
        complementseq = [complement[base] if base in complement else '*' for base in seq[1]]
        # recombine the entries of the created complementseq list to a string
        complement_str = ''.join(complementseq)
        # reverse the obtained complementary string for reading 5' - 3'
        revsequences.append([seq[0], complement_str[::-1]])
    return revsequences

def sequence_to_codon(sequences):
    print 'The sequence is partitioned into codons...'
    for seq in sequences:
        codons = [seq[1][i:i+3] for i in range(0, len(seq[1]), 3)]
        seq[1] = codons
    return sequences

def translate(codonsfor):

    translation = ""
    codemap = {
    'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GGT': 'G', 'GAG': 'E', 'GAA': 'E', 'GAC': 'D',
    'GAT': 'D', 'GCG': 'A', 'GCA': 'A', 'GCC': 'A', 'GCT': 'A', 'GTG': 'V', 'GTA': 'V',
    'GTC': 'V', 'GTT': 'V', 'AGG': 'R', 'AGA': 'R', 'AGC': 'S', 'AGT': 'S', 'AAG': 'K',
    'AAA': 'K', 'AAC': 'N', 'AAT': 'N', 'ACG': 'T', 'ACA': 'T', 'ACC': 'T', 'ACT': 'T',
    'ATG': 'M', 'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'CGG': 'R', 'CGA': 'R', 'CGC': 'R',
    'CGT': 'R', 'CAG': 'Q', 'CAA': 'Q', 'CAC': 'H', 'CAT': 'H', 'CCG': 'P', 'CCA': 'P',
    'CCC': 'P', 'CCT': 'P', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CTT': 'L', 'TGG': 'W',
    'TGA': 'X', 'TGC': 'C', 'TGT': 'C', 'TAG': 'X', 'TAA': 'X', 'TAC': 'T', 'TAT': 'T',
    'TCG': 'S', 'TCA': 'S', 'TCC': 'S', 'TCT': 'S', 'TTG': 'L', 'TTA': 'L', 'TTC': 'F',
    'TTT': 'F'
    }
    print 'Your sequence is now translated into aminoacid code...'
    #print codonsfor
    for seq in codonsfor:
        #print 'all codons for name', seq[0]
        #print seq[1]
        for triplet in seq[1]:
            #print triplet
            if triplet in codemap:
                #print triplet
                #print codemap[triplet]
                translation += codemap[triplet]
                #print translation
            else:
                translation += 'Z'
        seq[1] = translation
        translation = ''
    #print seq[1]
    return codonsfor

def splitsequence(sequences):

    num = 0
    orflist = []
    finalorf = []

    print 'The sequences are split to look for the longest ORF...'
    num = 0
    orflist.append([''])
    for seq in sequences:
        #print seq[1]
        for aa in seq[1]:
            if not aa == "X":
                orflist[num] += aa
                #print num
            else:
                num += 1
                orflist.append([''])
    for orf in orflist:
        orfseq = ''.join(orf)
        finalorf.append(orfseq)
        seq[1] = sorted(finalorf)[-1]
    print finalorf
    print seq[1], 'for ', seq[0]
        #r aa in seq[1]:
            #while aa != 'X':
            #    aaseq += aa
        #orflist.append(aaseq)
            #if aa == 'X': # checks if current aa is not stop to add to string
            #    onum += 1
            #    orfs.append([onum, ''])
            #else:
            #    print '+aa'
            #    orfs.append()[onum][1] += aa
        #print orfs


        #sequence = ''.join(seq[1])
        #split = sequence.split('stop') # split the sequence into ORFs
        #print 'And the longest ORF returned'
        #seq[1] = sorted(split)[-1] # safe the longest ORF as new entry
        #print seq[1], 'is entry for', seq[0]
    return sequences



def main():
    InFileName = raw_input('Which file should be searched for the longest ORF?\n >')
    #OutFileName = 'testruns_' + InFileName
    #OutFile = open(OutFileName, 'w')

    sequences = getsequence(InFileName)
    print sequences
    #reverseseq = reversecomplementsequence(sequences)
    #print reverseseq
    codonsfor = sequence_to_codon(sequences)
    print codonsfor
    #codonsrev = sequence_to_codon(reverseseq)
    #print codonsrev
    translatedfor = translate(codonsfor)
    print translatedfor
    #translatedrev = translate(codonsrev)
    #print translatedrev
    sequencesplit = splitsequence(translatedfor)
    print sequencesplit
    #reversesplit = splitsequence(translatedrev)
    #print reversesplit
    #OutFile.close()

main()
