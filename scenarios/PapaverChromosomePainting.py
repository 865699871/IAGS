from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Papaver in evolution history. 
result in outdutdata/Papaver/plot
"""
## please use your path
path = 'G:/IAGS'

# colors for target species chromosomes, Ancestor 1
colorlist = ['#DF1159','#1E93C9','#26AF67','#D5A1C5','#EBCA6D','#94B51E']

block_length_file = path + '/IAGS/inputdata/Papaver/blockindex.genenumber'
target_species_block_file = path + '/IAGS/' \
                            'outputdata/Papaver/Ancestor1/Ancestor1.block'
target_species_name = 'Ancestor1'
target_species_copy_number = 1


"""
Ancestor 1 -> P. rhoeas
"""
rearranged_species_block_file = path + '/IAGS/' \
                                'inputdata/Papaver/Prhoeas.final.block'
rearranged_species_name = 'P.rhoeas'
rearranged_species_copy_number = 1

outdir = path + '/IAGS/outputdata/Papaver/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> Ancestor 2
"""
rearranged_species_block_file = path + '/IAGS/' \
                                'outputdata/Papaver/Ancestor2/Ancestor2.block'
rearranged_species_name = 'Ancestor2'
rearranged_species_copy_number = 2

outdir = path + '/IAGS/outputdata/Papaver/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> Ancestor 3
"""
rearranged_species_block_file = path + '/IAGS/' \
                                'outputdata/Papaver/Ancestor3/Ancestor3.block'
rearranged_species_name = 'Ancestor3'
rearranged_species_copy_number = 2

outdir = path + '/IAGS/outputdata/Papaver/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)


"""
Ancestor 1 -> P. somniferum
"""
rearranged_species_block_file = path + '/IAGS/' \
                                'inputdata/Papaver/Psomniferum.final.block'
rearranged_species_name = 'P.somniferum'
rearranged_species_copy_number = 2

outdir = path + '/IAGS/outputdata/Papaver/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

"""
Ancestor 1 -> P. setigerum
"""
rearranged_species_block_file = path + '/IAGS/' \
                                'inputdata/Papaver/Psetigerum.final.block'
rearranged_species_name = 'P.setigerum'
rearranged_species_copy_number = 4

outdir = path + '/IAGS/outputdata/Papaver/plot/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)
