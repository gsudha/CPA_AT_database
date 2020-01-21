#!/bin/bash
#SBATCH -A SNIC2019-3-319
#SBATCH --job-name=DeepMP_modelling
#SBATCH -c 8
#SBATCH -t 24:00:00
#SBATCH --output=%J.slurm.out 
#SBATCH --error=%J.slurm.error


id=$1  # ID fasta

#Run Deep Meta Psicov
if [ ! -s $id.fasta.2u.a3m.aln ]; then
	if [ ! -s $id.DMP ]; then
		~/cbass/DeepMetaPSICOV/run_DMP.sh -i $id.fasta -o $id.DMP
		echo "Run Deep Meta Psicov" 
	fi
fi

#Run Deep Meta Psicov with alredy calculate MSA
if [ ! -s $id.DMP ]; then 
	~/cbass/DeepMetaPSICOV/run_DMP.sh -i $id.fasta -a $id.fasta.2u.a3m.aln -o $id.DMP
	echo "Run Deep Meta Psicov with alredy calculate MSA"
fi

#Convert Secondary structure file in Confold format
if [ ! -s $id.ss3 ]; then
	echo ">target_secondary_structure" > $id.ss3 ; awk 'BEGIN { ORS = "" } { print $3 }' $id.ss >> $id.ss3
	echo "Convert Secondary structure file"
fi

# Use contact prediction and ss as constrains in confold 

confold=/pfs/nobackup/home/m/mircomic/confold/CONFOLD/confold.pl
l=1.5 # L fraction of contacts 

dir=ALL_models_DMP/$id

mkdir -p $dir
##### Reformat contacts output #####
awk '$2-$1 > 5' $id.DMP >  $id.DMP.rr
sort -k5 -r -o $id.DMP.rr $id.DMP.rr
S=$(tail -1 $id.fasta); sed -i '1s/^/'$S'\n/' $id.DMP.rr

#### ######################### #####

seq=${id}.fasta
rr=${id}.DMP.rr
ss=${id}.ss3
outdir=$dir/confold_$l

if [ ! -f $outdir/stage2/${id}_model1.pdb ]; then
    rm -r $outdir
    mkdir $outdir
    $confold -seq $seq -rr $rr -ss $ss -o $outdir -selectrr ${l}L -stage2 1 -mcount 50 &> $outdir/${id}.log
    echo $id
fi
#ls -l $outdir/stage2/${id2}.fa_model1.pdb

echo "Model ready!"
