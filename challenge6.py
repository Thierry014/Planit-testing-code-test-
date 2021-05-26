# challenge 6
# Given a list of people (each person has attributes like name, DOB, nationality) 
# and in this world two people can’t have the exact same name then a user can:

# * Obtain a list of duplicates from the original list
# * Alter the original list and remove duplicates
# * Calculate the average age
# * Find all the people with age less than N
# * Obtain a list of unique countries

class Person:
    def __init__(self, name, dob, nationality):
        self.name = name
        self.dob = dob
        self.nationality = nationality
        # get birth year form the dob string
        year  = int(dob[-4:])
        self.age = 2021 - year


# Toolbox function to solve the problem 
def toolbox(people_list, N=0):
    duplicate_list = []
    list_remove_duplicate = []
    avg_age = 0 
    unique_country = []
    people_dic = {}

    for person in people_list:
        # 1. check duplicate person 
        if person.name in people_dic and person.name not in duplicate_list:
            duplicate_list.append(person)
        else:
            people_dic[person.name] = 1
            # 2. generate an unique people list => remove duplicate person 
            list_remove_duplicate.append(person)
    
    print(f'list of duplicate: {[x.name for x in duplicate_list]}')
    print(f'list after remove duplicate: {[x.name for x in list_remove_duplicate]}')

    # 3. calculate average
    total = 0 
    for person in list_remove_duplicate:
        total += person.age

        # check country as well (avoid another for loop)
        if person.nationality not in unique_country:
            unique_country.append(person.nationality)

    avg_age = total//len(list_remove_duplicate)
    print(f'Average age in people list is: {avg_age}')

    # 4. find people age < N
    print(f'People who younger than {N} is/are: {[x.name for x in list_remove_duplicate if x.age < N]}')
    
    # 5. obtain list of unique country
    print(f'Unique country list: {unique_country}')

    return 

# create person object and people_list
tom = Person('Tom','01/01/1990','Australia')
jack = Person('Jack','05/05/1943', 'Brazail')
henry = Person('Henry','24/06/1993', 'China')
tracy = Person('Tracy','05/05/1981', 'Australia')
allen = Person('Allen','05/03/2000', 'USA')

people_list = [tom,jack,henry,jack,tracy,tom,allen]

print(toolbox(people_list,40))

# Test result 
# list of duplicate: ['Jack', 'Tom']
# list after remove duplicate: ['Tom', 'Jack', 'Henry', 'Tracy', 'Allen']
# Average age in people list is: 39
# People who younger than 40 is/are: ['Tom', 'Henry', 'Allen']
# Unique country list: ['Australia', 'Brazail', 'China', 'USA']