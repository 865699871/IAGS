from models.MultiGMPmodel import MultiCopyGMPmodel
from models.MultiGGHPmodel import MultiCopyGGHPmodel
from models.GGHPmodel import GGHPmodel
from util.calculatedCRBrateAndEstimationAccuracy import calculatedCRBrateAndEstimationAccuracy

"""
Inferring ancestor species for Papaver species. 
Ancestor 3: Multi-copy GGHP model, result in outdutdata/Papaver/Ancestor3
Ancestor 1: GGHP model, result in outdutdata/Papaver/Ancestor1
Ancestor 2: Multi-copy GMP model, Ancestor1 should be doubled,result in outdutdata/Papaver/Ancestor2
"""


def doubled(infile,outfile):
    """
    Used for doubled species block sequence.

    :param infile: block sequence file
    :param outfile: block sequence file
    """
    outfile = open(outfile,'w')
    sequence = []
    with open(infile,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            sequence.append(line)
    for i in sequence:
        outfile.write(i)
    for i in sequence:
        outfile.write(i)

## please use your path
path = 'G:/IAGS'

workdir = path + '/IAGS/inputdata/Papaver/'

"""
Inferring ancestor species for Papaver species. 
Ancestor 3 using Multi-copy GGHP model
"""
dup_child_file = workdir + 'Psetigerum.final.block'
outgroup_file = workdir + 'Psomniferum.final.block'
outAncestor3dir = path + '/IAGS/outputdata/Papaver/Ancestor3/'
dup_copy_number = 4
out_copy_number = 2
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor3'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor3dir,
                   ancestor_name, dup_copy_number, out_copy_number,
                   ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Psomniferum.final.block'
matching_target_copy_number = out_copy_number
matching_target_name = 'P.somniferum'
speciesAndCopyList = [
    [workdir + 'Psetigerum.final.block',dup_copy_number,'P.setigerum'],
    [workdir + 'Psomniferum.final.block',out_copy_number,'P.somniferum']
]

model_type = 'MultiCopyGGHP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor3dir, model_type)

"""
Inferring ancestor species for Papaver species. 
Ancestor 1 using GGHP model
"""
dup_child_file = workdir + 'Psomniferum.final.block'
outgroup_file = workdir + 'Prhoeas.final.block'
outAncestor1dir = path + '/IAGS/outputdata/Papaver/Ancestor1/'
dup_copy_number = 2
out_copy_number = 1
ancestor_name = 'Ancestor1'
GGHPmodel(dup_child_file=dup_child_file,
          outgroup_file=outgroup_file,
          outdir=outAncestor1dir,
          ancestor_name=ancestor_name,
          dup_copy_number=dup_copy_number,
          out_copy_number=out_copy_number)

# Evaluation
matching_target_file = workdir + 'Prhoeas.final.block'
matching_target_copy_number = out_copy_number
matching_target_name = 'P.rhoeas'
ancestor_copy_number = 1
speciesAndCopyList = [
    [workdir + 'Psomniferum.final.block',dup_copy_number,'P.somniferum'],
    [workdir + 'Prhoeas.final.block',out_copy_number,'P.rhoeas']
]
model_type = 'GGHP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor1dir, model_type)

"""
Inferring ancestor species for Papaver species. 
Ancestor 2 using Multi-copy GMP model
"""
doubled(outAncestor1dir + 'Ancestor1.block',outAncestor1dir + 'Ancestor1.doubled.block')
species_file_list = [workdir + 'Psomniferum.final.block',
                     outAncestor3dir + 'Ancestor3.block',
                     outAncestor1dir + 'Ancestor1.doubled.block']
guided_species_for_matching = workdir + 'Psomniferum.final.block'
outAncestor2dir = path + '/IAGS/outputdata/Papaver/Ancestor2/'
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor2'
MultiCopyGMPmodel(species_file_list, outAncestor2dir, guided_species_for_matching,
                  ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Psomniferum.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'P.somniferum'
speciesAndCopyList = [
    [workdir + 'Psomniferum.final.block',ancestor_target_copy_number,'P.somniferum'],
    [outAncestor3dir + 'Ancestor3.block',ancestor_target_copy_number,'Ancestor3'],
    [outAncestor1dir + 'Ancestor1.doubled.block',ancestor_target_copy_number,'Ancestor1.doubled']
]
model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor2dir, model_type)



