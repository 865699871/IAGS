import random
import copy
import pandas as pd
import numpy as np

def changeAdj(adj_list):
    change = copy.deepcopy(adj_list)
    endpoints = []
    for j in change:
        for k in j:
            endpoints.append(k)
    random.shuffle(endpoints)
    change_part = []
    for j in range(int(len(endpoints) / 2)):
        change_part.append([endpoints[j * 2], endpoints[2 * j + 1]])
    return change_part

def reverse(item):
    if item[-1] == 'a':
        return item[:-1] + 'b'
    else:
        return item[:-1] + 'a'

def assemble(adjacency_list):
    ## assemble adjacencies to sequence
    matrix_items = []
    for i in adjacency_list:
        for j in i:
            if j not in matrix_items:
                matrix_items.append(j)
    matrix_items = sorted(matrix_items)
    adjacency_matrix = {}
    for i in matrix_items:
        adjacency_matrix[i] = {}
        for j in matrix_items:
            adjacency_matrix[i][j] = 0
    for i in adjacency_list:
        adjacency_matrix[i[0]][i[1]] = 1
        adjacency_matrix[i[1]][i[0]] = 1
    adjacency_matrix = pd.DataFrame(adjacency_matrix)
    index = adjacency_matrix.index.tolist()
    columns = adjacency_matrix.columns.tolist()
    np_adjacency_matrix = np.asarray(adjacency_matrix)
    adjacencies = {}
    for i in range(len(index)):
        for j in range(len(index)):
            if int(np_adjacency_matrix[i][j]) == 1:
                if '$' == index[i] or '$' == index[j]:
                    continue
                pair = sorted([index[i], index[j]])
                key = pair[0] + '@' + pair[1]
                if key not in adjacencies.keys():
                    adjacencies[key] = 1
                else:
                    adjacencies[key] += 1
    adjs = {}
    for i in adjacencies.keys():
        itemset = i.split('@')
        if itemset[0] not in adjs.keys():
            adjs[itemset[0]] = itemset[1]
        if itemset[1] not in adjs.keys():
            adjs[itemset[1]] = itemset[0]
    startpoint = []

    for j in range(len(columns)):
        if np_adjacency_matrix[0][j] == 1:
            startpoint.append(columns[j])
    markerstartpoint = []
    chr = []
    for i in startpoint:
        if i not in markerstartpoint:
            path = []
            if i[-1] == 'a':
                path.append(i[:-1])
            else:
                path.append('-' + i[:-1])
            start = reverse(i)
            if start in startpoint:
                markerstartpoint.append(start)
                chr.append(path)
            else:
                while True:
                    next = adjs[start]
                    if next[-1] == 'a':
                       path.append(next[:-1])
                    else:
                        path.append('-' + next[:-1])
                    start = reverse(next)
                    if start in startpoint:
                        markerstartpoint.append(start)
                        break
                chr.append(path)
    vector = []
    for i in chr:
        for j in i:
            if j.startswith('-'):
                vector.append(j[1:])
            else:
                vector.append(j)
    cyclepoint = []
    for i in adjs.keys():
        if i[:-1] not in vector:
            cyclepoint.append(i)

    cyclechr = []
    markercycle = []
    for i in cyclepoint:
        if i not in markercycle:
            startpoint = i
            cycle = []
            markercycle.append(i)
            start = i
            while True:
                next = adjs[start]
                if next[-1] == 'a':
                    cycle.append(next[:-1])
                else:
                    cycle.append('-' + next[:-1])
                markercycle.append(start)
                markercycle.append(next)
                start = reverse(next)
                if start == startpoint:
                    break
            cyclechr.append(cycle)
    return chr,cyclechr


def outSequence(sequence,outfile):
    outfile = open(outfile,'w')
    for i in sequence:
        for j in i:
            outfile.write(j+' ')
        outfile.write('\n')
    outfile.close()

def buildSimulatedGMP_CRBs(adjacencises, save_final_species_adjacencies, change_adjacency_number, divergence_level, current_level):
    random.shuffle(adjacencises)
    sp1 = copy.deepcopy(adjacencises)
    sp1_change = copy.deepcopy(sp1[:change_adjacency_number])
    sp1_change = changeAdj(sp1_change)

    sp1_unchange =  copy.deepcopy(sp1[change_adjacency_number:])
    new_sp1 = copy.deepcopy(sp1_change + sp1_unchange)
    save_final_species_adjacencies.append(new_sp1)
    listadj = []
    for i in adjacencises:
        listadj.append(i[0]+'@'+i[1])
    sp1list = []
    for i in new_sp1:
        sp1list.append(i[0]+'@'+i[1])
    changeadj = []
    unchangeadj = []
    count = 0
    for i in sp1list:
        if i not in listadj:
            changeadj.append(i)
            count += 1
        else:
            unchangeadj.append(i)

    random.shuffle(adjacencises)
    sp2 = copy.deepcopy(adjacencises)
    sp2_change =  copy.deepcopy(sp2[:change_adjacency_number])
    sp2_change = changeAdj(sp2_change)

    sp2_unchange = copy.deepcopy(sp2[change_adjacency_number:])
    new_sp2 = copy.deepcopy(sp2_change + sp2_unchange)
    sp2list = []
    for i in new_sp2:
        sp2list.append(i[0] + '@' + i[1])
    count = 0
    changeadj = []
    for i in sp2list:
        if i not in listadj:
            changeadj.append(i)
            count += 1

    if current_level == divergence_level:
        save_final_species_adjacencies.append(new_sp2)
    else:
        save_final_species_adjacencies.append(new_sp2)
        buildSimulatedGMP_CRBs(new_sp2, save_final_species_adjacencies, change_adjacency_number,
                               divergence_level, current_level + 1)

def sequence2adjacency(sequence):
    adjacency = []
    for i in sequence:
        block = i[0]
        if block.startswith('-'):
            adjacency.append(['$',block[1:] + 'b'])
            start = block[1:] + 'a'
        else:
            adjacency.append(['$', block + 'a'])
            start = block + 'b'
        for j in range(len(i)-1):
            block = i[j+1]
            if block.startswith('-'):
                adjacency.append([start, block[1:] + 'b'])
                start = block[1:] + 'a'
            else:
                adjacency.append([start, block + 'a'])
                start = block + 'b'
        adjacency.append([start,'$'])
    return adjacency


# simulate with some changed adjacencies in each species
def simulateGMP_CRBs(outdir, change_adjacency_number):
    ancestor_sequence_file = outdir + '/ancestor.sequence'
    chromosome_number = 5
    block_number = 100
    ancestor_sequence = []
    one_chromosome = int(block_number / chromosome_number)
    block = 100
    for i in range(chromosome_number):
        sequence = []
        for j in range(one_chromosome):
            if block % 2 == 0:
                sequence.append('-' + str(block))
            else:
                sequence.append(str(block))
            block += 1
        ancestor_sequence.append(sequence)
    outSequence(ancestor_sequence, ancestor_sequence_file)
    ancestor_adjacency = sequence2adjacency(ancestor_sequence)
    random.shuffle(ancestor_adjacency)

    divergence_level = 1
    # change some adjacencies in each divergence
    save_final_species_adjacencies = []
    buildSimulatedGMP_CRBs(ancestor_adjacency, save_final_species_adjacencies, change_adjacency_number, divergence_level, current_level=0)

    species_count = 1
    for i in save_final_species_adjacencies:
        copy_count = 1
        outfile = outdir + '/species.sequence.' + str(species_count)
        outfile = open(outfile,'w')
        filter_tel2tel = []
        for j in i:
            # filter ($,$)
            if j[0] == '$' and j[1] == '$':
                continue
            else:
                if j[0] != '$':
                    newendpoint1 = j[0][:-1]+'_'+str(copy_count)+j[0][-1]
                else:
                    newendpoint1 = '$'
                if j[1] != '$':
                    newendpoint2 = j[1][:-1]+'_'+str(copy_count)+j[1][-1]
                else:
                    newendpoint2 = '$'
                filter_tel2tel.append([newendpoint1, newendpoint2])
        chrs,cycles = assemble(filter_tel2tel)
        for j in chrs:
            outfile.write('s ')
            for k in j:
                outfile.write(k+' ')
            outfile.write('\n')
        for j in cycles:
            outfile.write('c ')
            min_index = -1
            min_value = 1000000
            for k in range(len(j)):
                if j[k].startswith('-'):
                    item = j[k][1:].split('_')
                    block = int(item[0])
                else:
                    item = j[k].split('_')
                    block = int(item[0])
                if block < min_value:
                    min_index = k
                    min_value = block
            if j[min_index].startswith('-'):
                half1 = j[min_index + 1:]
                half2 = j[:min_index + 1]
                new_string = half1 + half2
            else:
                half1 = j[min_index:]
                half2 = j[:min_index]
                new_string = half1 + half2
            for k in new_string:
                outfile.write(k+' ')
            outfile.write('\n')
        outfile.close()
        species_count += 1


