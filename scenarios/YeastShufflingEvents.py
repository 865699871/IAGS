from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Yeast in evolution history. 
result in outdutdata/Yeast
"""
## please use your path
path = 'G:/IAGS'

outfile = path + '/IAGS/outputdata/Yeast/shufflingEvents.txt'
outfile = open(outfile,'w')

"""
preWGD yeast -> N. castellii
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Ncastellii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 2
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> N. castellii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> S. cerevisiae
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Scerevisiae.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 2
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)

outfile.write('preWGD yeast -> S. cerevisiae\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
preWGD yeast -> K. naganishii
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Knaganishii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 2
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)

outfile.write('preWGD yeast -> K. naganishii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> Z. rouxii
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Zrouxii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> Z. rouxii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
preWGD yeast -> L. kluyveri
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Lkluyveri.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> L. kluyveri\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> L. waltii
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Lwaltii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)

outfile.write('preWGD yeast -> L. waltii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
preWGD yeast -> L. thermotolerans
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Lthermotolerans.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> L. thermotolerans\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> E. gossypii
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Egossypii.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> E. gossypii\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
preWGD yeast -> K. lactis
"""
species_block_sequence_dir = path + '/IAGS/inputdata/Yeast/'
ancestor_block_sequence_dir = path + '/IAGS/outputdata/Yeast/'

descendant_file = species_block_sequence_dir + 'Klactis.final.block'
ancestor_file = ancestor_block_sequence_dir + 'preWGD_yeast.block'

descendant_copy_number = 1
ancestor_copy_number = 1

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor_block_sequence_dir)
outfile.write('preWGD yeast -> K. lactis\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

outfile.close()
