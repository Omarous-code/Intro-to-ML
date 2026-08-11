import string
from random import randint, choice

def random_string(length):
    letters = string.ascii_letters + " " + string.digits + string.punctuation
    return ''.join(choice(letters) for i in range(length))
target_string = input("Enter a string: ")
len_string = len(target_string)
scores = []
pop = [random_string(len_string) for j in range (20)]
found_sol = False
sortarr = []
children = []

def v_tuple(tuple):
    for item in tuple:
        print(item)

def evaluate(population):
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
    for item in sorted_scores:
        sortarr.append(item[0])
    for i in range(20):
        child = ""
        Hindividual = sortarr[randint(0, 4)]
        Lindividual = sortarr[randint(15, 19)]
        for f in range(len_string):
            child += choice(Hindividual[f] + Lindividual[f])
        children.append(child)
    return children


print(sort(evaluate(pop)))
print(mate(sort(evaluate(pop))))

def mutate(population):
    for i in range(20):
        string = population[i]
        if randint(0, 100) >= 90:
            letters = string.ascii_letters + " " + string.digits + string.punctuation
            listed_string = list(string)



#print(mutate(scores))

print(target_string)