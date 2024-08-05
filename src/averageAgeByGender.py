def get_avg_age_for_gender(persons, gender):
    gender_filtered_list = [person for person in persons if person['gender'] == gender]

    avg_age = 0

    for person in gender_filtered_list:
        avg_age += person['age']

    return round(avg_age / len(gender_filtered_list), 2)


def main():
    persons = [
        {'name': 'Petya', 'age': 30, 'gender': 'Male'},
        {'name': 'Lexa', 'age': 24, 'gender': 'Female'},
        {'name': 'Neo', 'age': 55, 'gender': 'Male'}
    ]

    gender = input('Enter gender to calculate avg age: ')
    print(f'Average age for {gender} is {get_avg_age_for_gender(persons, gender)}')


if __name__ == '__main__':
    main()
