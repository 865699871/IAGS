from models.MultiGMPmodel import MultiCopyGMPmodel
from models.MultiGGHPmodel import MultiCopyGGHPmodel
from util.calculatedCRBrateAndEstimationAccuracy import calculatedCRBrateAndEstimationAccuracy
from util.cutCircularChromosomes import cutCircularChromosomes

"""
Inferring ancestor species for Gramineae species. 
Ancestor 4: Multi-copy GGHP model, result in outdutdata/Gramineae/Ancestor4
Ancestor 3: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor3
Ancestor 2: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor2
Ancestor 1: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor1

"""
## please use your path
path = 'G:/IAGS'

workdir = path + '/IAGS/inputdata/Gramineae/'

"""
Inferring ancestor species for Gramineae species. 
Ancestor 4 using Multi-copy GGHP model
"""
dup_child_file = workdir + 'Zmays.final.block'
outgroup_file = workdir + 'Sbicolor.final.block'
outAncestor4dir = path + '/IAGS/outputdata/Gramineae/Ancestor4/'
dup_copy_number = 4
out_copy_number = 2
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor4'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor4dir,
                   ancestor_name, dup_copy_number, out_copy_number, ancestor_target_copy_number)

# speciesAndCopyList = [
#     [workdir + 'Zmays.final.block',dup_copy_number,'Z.mays'],
#     [workdir + 'Sbicolor.final.block',out_copy_number,'S.bicolor']
# ]
# cutCircularChromosomes(outAncestor4dir + 'Ancestor4.block',
#                        ancestor_target_copy_number,
#                        ancestor_name,speciesAndCopyList,outAncestor4dir)

# Evaluation
matching_target_file = workdir + 'Sbicolor.final.block'
matching_target_copy_number = out_copy_number
matching_target_name = 'S.bicolor'

speciesAndCopyList = [
    [workdir + 'Zmays.final.block',dup_copy_number,'Z.mays'],
    [workdir + 'Sbicolor.final.block',out_copy_number,'S.bicolor']
]

model_type = 'MultiCopyGGHP'

calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor4dir, model_type)

"""
Inferring ancestor species for Gramineae species. 
Ancestor 3 using Multi-copy GMP model
"""
species_file_list = [workdir + 'Sbicolor.final.block',
                     outAncestor4dir + 'Ancestor4.block',
                     workdir + 'Osativa.final.block']
guided_species_for_matching = workdir + 'Sbicolor.final.block'
ancestor_target_copy_number = 2
outAncestor3dir = path + '/IAGS/outputdata/Gramineae/Ancestor3/'
ancestor_name = 'Ancestor3'
MultiCopyGMPmodel(species_file_list, outAncestor3dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Sbicolor.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'S.bicolor'
speciesAndCopyList = [
    [workdir + 'Sbicolor.final.block',ancestor_target_copy_number,'S.bicolor'],
    [outAncestor4dir + 'Ancestor4.block',ancestor_target_copy_number,'Ancestor4'],
    [workdir + 'Osativa.final.block',ancestor_target_copy_number,'O.sativa']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor3dir, model_type)

"""
Inferring ancestor species for Gramineae species. 
Ancestor 2 using Multi-copy GMP model
"""
species_file_list = [workdir + 'Bdistachyon.final.block',
                     workdir + 'Telongatum.final.block',
                     workdir + 'Osativa.final.block']
guided_species_for_matching = workdir + 'Bdistachyon.final.block'
ancestor_target_copy_number = 2
outAncestor2dir = path + '/IAGS/outputdata/Gramineae/Ancestor2/'
ancestor_name = 'Ancestor2'
MultiCopyGMPmodel(species_file_list, outAncestor2dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Bdistachyon.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'B.distachyon'
speciesAndCopyList = [
    [workdir + 'Bdistachyon.final.block',ancestor_target_copy_number,'B.distachyon'],
    [workdir + 'Telongatum.final.block',ancestor_target_copy_number,'T.elongatum'],
    [workdir + 'Osativa.final.block',ancestor_target_copy_number,'O.sativa']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor2dir, model_type)

"""
Inferring ancestor species for Gramineae species. 
Ancestor 1 using Multi-copy GMP model
"""
species_file_list = [workdir + 'Osativa.final.block',
                     outAncestor2dir + 'Ancestor2.block',
                     outAncestor3dir + 'Ancestor3.block']
guided_species_for_matching = workdir + 'Osativa.final.block'
ancestor_target_copy_number = 2
outAncestor1dir = path + '/IAGS/outputdata/Gramineae/Ancestor1/'
ancestor_name = 'Ancestor1'
MultiCopyGMPmodel(species_file_list, outAncestor1dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Osativa.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'O.sativa'
speciesAndCopyList = [
    [workdir + 'Osativa.final.block',ancestor_target_copy_number,'O.sativa'],
    [outAncestor2dir + 'Ancestor2.block',ancestor_target_copy_number,'Ancestor2'],
    [outAncestor3dir + 'Ancestor3.block',ancestor_target_copy_number,'Ancestor3']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor1dir, model_type)
