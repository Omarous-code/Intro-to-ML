import string
from ftplib import print_line
from random import randint, choice

def random_string(length):
    letters = string.ascii_letters + " " + string.digits + string.punctuation
    return ''.join(choice(letters) for i in range(length))
target_string = input("Enter a string: ")
len_string = len(target_string)
scores = []
pop = [random_string(len_string) for j in range (20)]
found_sol = False

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
        if finalscore == 100.0:
            global found_sol = True
            break
        else:
            scores.append((string, finalscore))
            return scores


def sort(scores):
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return sorted_scores
def mate(sorted_scores):
    for item in sorted_scores:
        sortarr = [item[0]]
    return sortarr
print(mate(sort(evaluate(pop))))
print("this is the mating")
#
#def mutate(population):
#    for string in population:
#        if randint(0, 100) >= 90:
#            string[randint(0, (len_string -1))] = string.join(choice(string.ascii_letters + " " + string.digits + string.punctuation))

#print(mutate(scores))

print(target_string)