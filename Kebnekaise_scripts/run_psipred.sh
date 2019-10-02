#!/bin/bash
#SBATCH -A SNIC2019-3-319
#SBATCH --job-name=Jackhmmer_01
#SBATCH -c 1
#SBATCH -t 08:00:00
#SBATCH --output=PSIpred.out
#SBATCH --error=PSIpred.error

/pfs/nobackup/home/m/mircomic/psipred/runpsipred $1.fasta
#change format of the output
printf '>PSIpred_prediction \n' >  $1.ss3 | grep 'Pred:' $1.horiz | cut -c6- | tr -d '\n ' >> $1.ss3

                                                                                                
