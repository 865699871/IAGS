from models.GGHPmodel import GGHPmodel
from util.calculatedCRBrateAndEstimationAccuracy import calculatedCRBrateAndEstimationAccuracy

"""
Inferring ancestor species for Yeast species. GGHP model
block sequences and target copy number of nonWGD and WGD yeast should be merged, respectively.

result in outdutdata/Yeast
"""

def mergeblock(filelist,outfile):
    """
    merge multi-species file
    :param filelist: species block sequence file list
    :param outfile: output file
    """
    filelines = []
    for i in filelist:
        file = open(i,'r')
        for j in file:
            filelines.append(j)
        file.close()
    outfile = open(outfile,'w')
    for i in filelines:
        outfile.write(i)
    outfile.close()

## please use your path
path = 'G:/IAGS'

workdir = path + '/IAGS/inputdata/Yeast/'
nonWGD_yeast = [workdir + 'Egossypii.final.block',
                workdir + 'Lkluyveri.final.block',
                workdir + 'Klactis.final.block',
                workdir + 'Zrouxii.final.block',
                workdir + 'Lthermotolerans.final.block',
                workdir + 'Lwaltii.final.block']
merged_nonWGDspecies_file = workdir + 'merged_non_WGD_yeast.block'
# merged
mergeblock(nonWGD_yeast,merged_nonWGDspecies_file)

WGD_yeast = [workdir + 'Ncastellii.final.block',
             workdir + 'Knaganishii.final.block',
             workdir + 'Scerevisiae.final.block']
merged_WGDspecies_file = workdir + 'merged_WGD_yeast.block'
mergeblock(WGD_yeast,merged_WGDspecies_file)

outdir = path + '/IAGS/outputdata/Yeast/'
ancestor_name = 'preWGD_yeast'
# three duplicated yeasts and six non duplicated yeasts, target copy number are both 6.
GGHPmodel(dup_child_file=merged_WGDspecies_file,
          outgroup_file=merged_nonWGDspecies_file,
          outdir=outdir,
          ancestor_name=ancestor_name,
          dup_copy_number=2*3,
          out_copy_number=1*6)
# Evaluation
matching_target_file = workdir + 'Lwaltii.final.block'
matching_target_copy_number = 1
matching_target_name = 'Lwaltii'

speciesAndCopyList = [
    [workdir + 'Ncastellii.final.block',2,'Ncastellii'],
    [workdir + 'Knaganishii.final.block',2,'Knaganishii'],
    [workdir + 'Scerevisiae.final.block',2,'Scerevisiae'],
    [workdir + 'Egossypii.final.block',1,'Egossypii'],
    [workdir + 'Lkluyveri.final.block',1,'Lkluyveri'],
     [workdir + 'Klactis.final.block', 1, 'Klactis'],
     [workdir + 'Zrouxii.final.block', 1, 'Zrouxii'],
     [workdir + 'Lthermotolerans.final.block', 1, 'Lthermotolerans'],
     [workdir + 'Lwaltii.final.block', 1, 'Lwaltii']
]

model_type = 'GGHP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outdir, model_type)
