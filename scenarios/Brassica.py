from models.GMPmodel import GMPmodel
from util.calculatedCRBrateAndEstimationAccuracy import calculatedCRBrateAndEstimationAccuracy
"""
Inferring ancestor species for Brassica using GMP model
result in outdutdata/Brassica
"""
## please use your path
path = 'G:/IAGS'

workdir = path + '/IAGS/inputdata/Brassica/'
species_block_filelist = [workdir + 'Boleracea.final.block',
                          workdir + 'Brapa.final.block',
                          workdir + 'Bnigra.final.block']
ancestor_name = 'Brassica'
outdir = path + '/IAGS/outputdata/Brassica/'

GMPmodel(species_file_list=species_block_filelist,
         outdir=outdir,
         ancestor_name=ancestor_name)

# Evaluation
matching_target_file = workdir + 'Boleracea.final.block'
matching_target_copy_number = 1
matching_target_name = 'B.oleracea'

speciesAndCopyList = [[workdir + 'Boleracea.final.block',1,'B.oleracea'],
                      [workdir + 'Brapa.final.block',1,'B.rapa'],
                      [workdir + 'Bnigra.final.block',1,'B.nigra']]

model_type = 'GMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outdir, model_type)
