from sympy.abc import lamda

numbers = [1, 2, 3, 4, 5, 6]

def maximum(numbers):
    return max(numbers)

maxi = maximum(numbers)

print(maxi)


for i in numbers :
    print(i)

def sum_even(numbers):
    somme = 0
    for i in numbers:
        if i % 2 == 0:
            somme = somme + i
    return somme
som = sum_even(numbers)
print(som)

text = "Python est un excellent langage"

def count_words(text):
    words = text.split()
    mot_lon = max(words, key=len)
    return mot_lon

print(count_words(text))

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count_vo = 0
    for i in text:
        if i in vowels :
            count_vo = count_vo + 1

    return count_vo
print(count_vowels("Ferdinand"))

employees = [
    {"name": "Alice", "salary": 2500},
    {"name": "Bob", "salary": 3000},
    {"name": "John", "salary": 2800},
]

def tri_salaire(employees):
    salary_salay = []
    for employee in employees:
        if employee["salary"] >2700:
            salary_salay.append(employee["name"])
    return salary_salay
print(tri_salaire(employees))

numbers_m = [5, 2, 8, 1, 9, 4]

def deux_max(numbers):
    numbers.sort()

    return  numbers[-3]
print(deux_max(numbers_m))

a = {"name": "Ferdinand"}
b = {"age": 24}

def fusion(dict1:dict, dict2:dict):
    result = dict1 | dict2
    result.update(dict1)
    return result

print(fusion(a, b))

sales = [
    ("Apple", 10),
    ("Orange", 20),
    ("Apple", 30),
    ("Orange", 10),
]

def somme_fruit(fruit):
    result = {}
    for fruit, quantity in sales:

        result[fruit] = result.get(fruit, 0) + quantity

    return result

print(somme_fruit(sales))

def nbre_caractere(mots):
    frequence =  {}

    for c in mots:
        frequence[c] = frequence.get(c, 0) + 1

    caractere = max(frequence, key=frequence.get)
    return caractere, frequence[caractere]
print(nbre_caractere("programmingg"))

students = [
    {"name": "Alice", "grade": 15},
    {"name": "Bob", "grade": 8},
    {"name": "John", "grade": 12},
    {"name": "Emma", "grade": 18},
]

def tri_note(notes):
    resutts = []
    for note in notes:
        if note["grade"] >= 10:
            resutts.append(note)

    resutts.sort(
        key=lambda x : x["grade"],
        reverse=True
    )
    return resutts
print(tri_note(students))

print(max(students, key=lambda x : x["grade"]))