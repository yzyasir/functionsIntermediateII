# 1) THIS IS THE FIRST QUESTION

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# 1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# 
# print(x[1])
# # This targets the part of the array
# 
# print(x[1][0])
# This targets the right one and the first value
 
# x[1][0] = 15
# print(x)
# This is the answer

# 2) Change the last_name of the first student from 'Jordan' to 'Bryant'

# students[0]['last_name'] = 'Bryant'
# Notes: This is to target the specific key in that dictionary

# students[0]['last_name'] = 'Bryant'
# Have to equate the name to the string 

# print(students)
# # This is the answer

# 3) In the sports_directory, change 'Messi' to 'Andres'

# print(sports_directory["soccer"][0])
# This targets the value we want to change, see how i targetted the string then the index

# sports_directory["soccer"][0] = "Andres"
# print(sports_directory)
# This is the answer

# Note: You cannot do print(sports_directory["soccer"][0] = "Andres"). Must print the var.

# 4) Change the value 20 in z to 30
# 
# print(z[0]['y'])
# Had to target the index then the string to get to where I wanted

# z[0]['y'] = 30
# print(z)
# This is the answer


# 2) THIS IS THE SECOND QUESTION
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(some_list):
    for student_dictionary in some_list:
        for key, val in student_dictionary.items():
            print(f'{key} - {val}')

# iterateDictionary(students)
# GO OVER THIS AGAIN YOU IDIOT!!!!

# 3) THIS IS THE THIRD QUESTION
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def interateDictionary2(key_name, some_list):
    # print(some_list)
    for student_dictionary in some_list:
        print(student_dictionary[key_name])

# iterateDictionary2("first_name", students)

# 4) THIS IS THE FORTH QUESTION
# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(someDictionary):
    # print(someDictionary)
    for key, val in someDictionary.items():
        # print(len(val))
        print(f'{len(val)} {key.upper()}')
        for item in val:
            print(item)
        print(" ")
        print(f"{len(someDictionary[key])} {key.upper()}")

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon






