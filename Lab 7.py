import numpy as np
import random
from datetime import datetime

cities = 4
population = 10
mutation_rate = 0.3

nameslist = np.array(['Sirsa', 'Bhiwani', 'Hisar', 'Chandigarh'])
graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]


cities_dict = { x:y for x,y in zip(nameslist,range(cities))}
print(cities_dict)

for i in graph:
	print(i)
def distance(a,b):
	return graph[a][b]

def distance_names(city_a, city_b, cities_dict):
    return distance(cities_dict[city_a], cities_dict[city_b])




# create population set 
def gene(city_list, population):

    population_set = []
    for i in range(population):

        temp = city_list[np.random.choice(list(range(cities)), cities, replace=False)]
        population_set.append(temp)
    return np.array(population_set)

population_set = gene(nameslist, population)
print(population_set)

print()
print()



# finding solutions fitness 
def fitness_eval(city_list, cities_dict):
	total = 0
	for i in range(cities):
		a = city_list[i]
		b = city_list[((i+1)%cities)]
		total += distance_names(a,b, cities_dict)
	return total


def fitnes(population_set, cities_dict):
    fitnes_list = np.zeros(population)
    for i in  range(population):
        fitnes_list[i] = fitness_eval(population_set[i], cities_dict)
    return fitnes_list

fitnes_list = fitnes(population_set,cities_dict)
print(fitnes_list)


print()
print()



# Roulette Wheel Selection

def selection(population_set,fitnes_list):
	total_fit = fitnes_list.sum()
	prob_list = fitnes_list/total_fit
	
	list_a = np.random.choice(list(range(len(population_set))), len(population_set),p=prob_list, replace=True)
	list_b = np.random.choice(list(range(len(population_set))), len(population_set),p=prob_list, replace=True)

	list_a = population_set[list_a]
	list_b = population_set[list_b]
	
	return np.array([list_a,list_b])

progenitor_list = selection(population_set,fitnes_list)
print(progenitor_list)

print()
print()



# mating 
def mate(a, b):

	offspring = list(a[0:5])
	for city in b:
		if not city in offspring:
			offspring = np.concatenate((offspring,[city]))
	return offspring
		
def mate_population(progenitor_list):
	new_population_set = []
	for i in range(len(progenitor_list[0])):
		prog_a, prog_b = progenitor_list[0][i], progenitor_list[1][i]
		offspring = mate(prog_a, prog_b)
		new_population_set.append(offspring)     
	return new_population_set

new_population_set = mate_population(progenitor_list)
print(new_population_set)


print()
print()


# mutation 
def mutate_offspring(offspring):
	for q in range(int(cities*mutation_rate)):
		a = np.random.randint(0,cities)
		b = np.random.randint(0,cities)
		offspring[a], offspring[b] = offspring[b], offspring[a]
	return offspring
    
    
def mutate_population(new_population_set):
    mutated_pop = []
    for offspring in new_population_set:
        mutated_pop.append(mutate_offspring(offspring))
    return mutated_pop

mutated_popu = mutate_population(new_population_set)
print(mutated_popu)


# stopping 

best_solution = [-1,np.inf,np.array([])]

for i in range(10000):
	if i%100==0: 
		print(i, fitnes_list.min(), fitnes_list.mean(), datetime.now().strftime("%d/%m/%y %H:%M"))
	fitnes_list = fitnes(mutated_popu,cities_dict)
	
	#Saving the best solution
	if fitnes_list.min() < best_solution[1]:
		best_solution[0] = i
		best_solution[1] = fitnes_list.min()
		best_solution[2] = np.array(mutated_popu)[fitnes_list.min() == fitnes_list]
	

	progenitor_list = selection(population_set,fitnes_list)
	new_population_set = mate_population(progenitor_list)
	mutated_popu = mutate_population(new_population_set)



