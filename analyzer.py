import csv
from os import name

def read_csv(file_path):
    people = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            people.append(row)
    return people

def calculate_average_age(data):
    total_age = 0
    count = 0

    for person in data:
        age = person.get('age')
        if age and age.isdigit():
            total_age += int(age)
            count += 1

    if count == 0:
        return 0

    return total_age / count

def main():
    people = read_csv('data/people.csv')
    print("Total people:", len(people))
    print("Average age:", calculate_average_age(people))

if __name__== "__main__":
    main()