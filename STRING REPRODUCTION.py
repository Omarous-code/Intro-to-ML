import string
from random import randint, choice
from time import sleep

letters = string.ascii_letters + " " + string.digits + string.punctuation
def random_string(length):
    letters = string.ascii_letters + " " + string.digits + string.punctuation
    return ''.join(choice(letters) for i in range(length))
target_string = input("Enter a string: ")
len_string = len(target_string)
pop = [random_string(len_string) for j in range (20)]
found_sol = False
generation = 0
max_generation = 100000


def evaluate(population):
    scores = []
    for string in population:
        score = 0
        for i in range(len_string):
            if string[i] == target_string[i]:
                score += 1
            finalscore = (score / len_string) * 100
        scores.append((string, finalscore))
    return scores


def sort(scores):
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return sorted_scores
def mate(sorted_scores):
    sortarr = []
    children = []
    for item in sorted_scores:
        sortarr.append(item[0])
    for i in range(20):
        child = ""
        Hindividual = sortarr[randint(0, 4)]
        Lindividual = sortarr[randint(10, 15)]
        for f in range(len_string):
            child += choice(Hindividual[f] + Lindividual[f])
        children.append(child)
    return children





def mutate(population):
    for i in range(20):
        if randint(0, 100) > 90:
            listed_string = list(population[i])
            listed_string[randint(0, len_string -1)] = choice(letters)
            population[i] = ''.join(listed_string)
    return population

def check_score(sorted_scores):
    global found_sol
    if sorted_scores[0][1] == 100:
        found_sol = True






while found_sol == False and generation < max_generation:
    sorted_population = (sort(evaluate(pop)))
    check_score(sorted_population)
    print(sorted_population)
    if sorted_population[0][1] != 100:
        mated_population = mate(sorted_population)
        print(mated_population)
        mutated_population = mutate(mated_population)
        print(mutated_population)
        pop.clear()
        pop = mutated_population
        print(pop)
        print("this is pop")
        generation += 1
        print("generation " + str(generation))



