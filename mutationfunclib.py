import random

# The bitwise_mutation function flips the value of a gene at a specific index in a chromosome
def bitwise_mutation(chromosome, gene_index):
    chromosome[gene_index] = 1 - chromosome[gene_index]
    return chromosome


# The uniform_bitwise_mutation function applies bitwise mutation to each gene in the chromosome with a given mutation
# rate
def uniform_bitwise_mutation(chromosome, mutation_rate):
    for gene in range(len(chromosome)):
        if random.randrange(0, 1) < mutation_rate:
            chromosome[gene] = 1 - chromosome[gene]
    return chromosome


# The swap_mutation function swaps the values of two genes at specific indexes in a chromosome
# chomosome must be a list
def swap_mutation(chromosome, index1, index2):
    temp1 = chromosome[index1]
    temp2 = chromosome[index2]
    chromosome[index1] = temp2
    chromosome[index2] = temp1
    return chromosome


# The crossover_mutation function creates an offspring by randomly selecting genes from two parents
def crossover_mutation(parent1, parent2):
    offspring = ""
    for i in range(len(parent1)):
        random_number = random.randrange(0, 1)
        if random_number < 0.5:
            offspring += str(parent1[i])
        if random_number > 0.5:
            offspring += str(parent2[i])
    return offspring


# The inverse_mutation function inverses the value of a range of genes in a chromosome
def inverse_mutation(chromosome, start, end):
    for i in range(start, end):
        chromosome[i] = 1 - chromosome[i]
    return chromosome


# The multipoint_mutation function sets the value of a list of genes to a new value
# Chromosome must be a list
def multipoint_mutation(chromosome, gene_indexes, new_value):
    for gene in gene_indexes:
        chromosome[gene] = new_value
    return chromosome


# The creep_mutation function increments the value of a gene by a given (small)change
def creep_mutation(chromosome, gene, change):
    chromosome[gene] += change
    return chromosome


# The random_setting_mutation function sets the value of a gene to a random value within a given range.
# It takes a boolean value as an input to determine if the random value should be an integer or a float.
# It also asserts if the input for integer is boolean
def random_setting_mutation(chromosome, gene, lower_bound, upper_bound, integer):
    assert isinstance(integer, bool), f"Expected a boolean but got {type(integer)}"
    if integer:
        chromosome[gene] = random.randint(lower_bound, upper_bound)
    else:
        chromosome[gene] = random.uniform(lower_bound, upper_bound)


# This function performs a scramble mutation on the given chromosome. It selects a subsequence of the chromosome,
# defined by the start and end indices, and shuffles the elements within that subsequence. The shuffled subsequence
# is then replaced back into the original chromosome.
def scramble_mutation(chromosome, start, end):
    sub_seq = chromosome[start:end]
    random.shuffle(sub_seq)
    chromosome[start:end] = sub_seq
    return chromosome


# This function performs a reverse subsequence mutation on the given chromosome. It selects a subsequence of the
# chromosome, defined by the start and end indices, and reverses the order of the elements within that subsequence.
# The reversed subsequence is then replaced back into the original chromosome.
def reverse_subsequence_mutation(chromosome, start, end):
    sub_seq = chromosome[start:end]
    sub_seq = sub_seq[::-1]
    chromosome[start:end] = sub_seq
    return chromosome
