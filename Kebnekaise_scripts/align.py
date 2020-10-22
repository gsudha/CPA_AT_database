import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
import parse_fasta
import parse_pdb


P1_fasta = sys.argv[1]
P2_fasta = sys.argv[2]
chain = sys.argv[3]
out = sys.argv[4]


P1 = parse_fasta.read_fasta(open(sys.argv[1], 'r')).values()[0][0]
P2 = parse_pdb.get_atom_seq(open(sys.argv[2], 'r'), chain)

with open(P1_fasta) as f:
    P1_header = f.readline()


with open(P2_fasta) as f:
    P2_header = f.readline()

alignments = pairwise2.align.localms(P1, P2, 2, -1, -0.5, -0.001)
#print alignments
#print P1_header
#print(alignments[0][0])
#print P2_header
#print(alignments[0][1])
with open(out,"w") as r:
    r.write(P2_header+ alignments[0][0]+ "\n" + ">P2_header"+"\n"+ alignments[0][1])                                                                                        
