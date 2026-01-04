import csv
from collections import defaultdict

#CSV
def read_csv(file_path):
    data=[]
    with open (file_path, 'r', encoding='utf-8') as file: 
        reader=csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data 
#age
def  calculate_average_age(data):
    total_age = 0
    count = 0
    for person in data:
        age = person.get('age')
        if age and age.isdigit():
            total_age += int (age)
            count += 1
    return total_age / count if count else 0
#age_max_min
def min_max_age(data):
    ages = [int(person['age']) for person in data if person.get('get') and person['age'].isdigit()]
    return(min(ages),max(ages)) if ages else (0, 0)
#city
def count_per_city(data):
    city_count=defaultdict(int)
    for person in data:
        city = person.get('city')
        if city:
            city_count[city] += 1
    return city_count
#function
def main():
    people =read_csv('data/people.csv')

    print("Total people:", len(people))
    print("Average age:", calculate_average_age(people))

    min_age, max_age =min_max_age(people)
    print("Min age:",min_age)
    print("Max age:",max_age)

    city_count=count_per_city(people)
    print("People per city:")
    for city, count in city_count.items():
        print(f"{city}:{count}")

if __name__ == "__main__":
    main()
