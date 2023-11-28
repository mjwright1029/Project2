import csv

villager_name = input('Enter the name of the villager')


def get_info():
    species = ''
    gender = ''
    personality = ''
    hobby = ''
    birthday = ''
    with open('villagers.csv', 'r', newline='') as csvfile:
        content = csv.reader(csvfile, delimiter=',')

        for row in content:
            if row and row[0] == villager_name:
                species = row[4]
                gender = row[5]
                personality = row[6]
                hobby = row[8]
                birthday = row[9]
                return row, species, gender, personality, hobby, birthday


def main():
    info, species, gender, personality, hobby, birthday = get_info()
    print(f'Species: {species}, Gender: {gender}, Personality: {personality}, Hobby: {hobby}, Birthday: {birthday}')


if __name__ == '__main__':
    main()
