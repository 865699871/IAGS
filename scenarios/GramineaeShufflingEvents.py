from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Gramineae in evolution history. 
result in outdutdata/Gramineae
"""
## please use your path
path = 'G:/IAGS'

outfile = path + '/IAGS/outputdata/Gramineae/shufflingEvents.txt'
outfile = open(outfile,'w')


"""
Ancestor 1 -> O. sativa
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Gramineae/'
ancestor1_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor1/'

descendant_file = species_block_sequence_dir + 'Osativa.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> O. sativa\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 2
"""
ancestor2_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor2/'
ancestor1_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor1/'

descendant_file = ancestor2_block_sequence_dir + 'Ancestor2.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 2\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 3
"""
ancestor3_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor3/'
ancestor1_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor1/'

descendant_file = ancestor3_block_sequence_dir + 'Ancestor3.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 3\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 2 -> T. elongatum
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Gramineae/'
ancestor2_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor2/'

descendant_file = species_block_sequence_dir + 'Telongatum.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> T. elongatum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 2 -> B. distachyon
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Gramineae/'
ancestor2_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor2/'

descendant_file = species_block_sequence_dir + 'Bdistachyon.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> B. distachyon\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 3 -> S. bicolor
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Gramineae/'
ancestor3_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor3/'

descendant_file = species_block_sequence_dir + 'Sbicolor.final.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> S. bicolorn\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 3 -> Ancestor 4
"""
ancestor4_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor4/'
ancestor3_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor3/'

descendant_file = ancestor4_block_sequence_dir + 'Ancestor4.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor3_block_sequence_dir)

outfile.write('Ancestor 3 -> Ancestor 4\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 4 -> Z. mays
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Gramineae/'
ancestor4_block_sequence_dir = path + '/IAGS/outputdata/Gramineae/Ancestor4/'

descendant_file = species_block_sequence_dir + 'Zmays.final.block'
ancestor_file = ancestor4_block_sequence_dir + 'Ancestor4.block'

descendant_copy_number = 4
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor4_block_sequence_dir)


outfile.write('Ancestor 4 -> Z. mays\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')
outfile.close()
