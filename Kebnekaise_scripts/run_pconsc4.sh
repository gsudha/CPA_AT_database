#!/bin/bash
#SBATCH -A SNIC2019-3-319
#SBATCH --job-name=Jackhmmer_01
#SBATCH -c 6
#SBATCH -t 6:00:00
#SBATCH --output=%J.slurm.$i.out
#SBATCH --error=%Jslurm.$i.error

#export PYTHON_EGG_CACHE=~/pfs/python35/lib/python3.6/site-packages


i=$1
#if [ ! -f $i.rr ]; then
python3.6 ~/pfs/Repeats/run_pconsc4.py fasta MSA. a3m output.rr contact_map.pdf
#fi
