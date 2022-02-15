from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Papaver in evolution history. 
result in outdutdata/Papaver
"""
## please use your path
path = 'G:/IAGS'

outfile = path + '/IAGS/outputdata/Papaver/shufflingEvents.txt'
outfile = open(outfile,'w')


"""
Ancestor 1 -> P. rhoeas
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Papaver/'
ancestor1_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor1/'

descendant_file = species_block_sequence_dir + 'Prhoeas.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)

outfile.write('Ancestor 1 -> P. rhoeas\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 2
"""
ancestor2_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor2/'
ancestor1_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor1/'

descendant_file = ancestor2_block_sequence_dir + 'Ancestor2.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 2\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 2 -> Ancestor 3
"""
ancestor3_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor3/'
ancestor2_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor2/'

descendant_file = ancestor3_block_sequence_dir + 'Ancestor3.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> Ancestor 3\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 2 -> P. somniferum
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Papaver/'
ancestor2_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor2/'

descendant_file = species_block_sequence_dir + 'Psomniferum.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> P. somniferum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 3 -> P. setigerum
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Papaver/'
ancestor3_block_sequence_dir = path + '/IAGS/outputdata/Papaver/Ancestor3/'

descendant_file = species_block_sequence_dir + 'Psetigerum.final.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

descendant_copy_number = 4
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> P. setigerum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')
outfile.close()
