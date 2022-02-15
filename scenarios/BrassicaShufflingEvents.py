from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Brassica in evolution history. 
result in outdutdata/Brassica
"""
## please use your path
path = 'G:/IAGS'

outfile = path + '/IAGS/outputdata/Brassica/shufflingEvents.txt'
outfile = open(outfile,'w')

"""
Ancestor Brassica -> B. rapa
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Brassica/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Brassica/'

descendant_file = species_block_sequence_dir + 'Brapa.final.block'
ancestor_file = ancestor_block_sequence_dir + 'Brassica.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('Ancestor Brassica -> B. rapa\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor Brassica -> B. oleracea
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Brassica/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Brassica/'

descendant_file = species_block_sequence_dir + 'Boleracea.final.block'
ancestor_file = ancestor_block_sequence_dir + 'Brassica.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)

outfile.write('Ancestor Brassica -> B. oleracea\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor Brassica -> B. nigra
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Brassica/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Brassica/'

descendant_file = species_block_sequence_dir + 'Bnigra.final.block'
ancestor_file = ancestor_block_sequence_dir + 'Brassica.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('Ancestor Brassica -> B. nigra\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

outfile.close()
