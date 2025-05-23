#dictionaries 
marks = {
    "harry" : 100 ,
    "suvam" : 90 ,
    "jaya" : 70,
     "tanu" : 80
}

print(marks , type(marks))

person = {
    'First_name' : 'ana',
    'last_name' : 'hathway',
    'age' : 21,
    'country' : 'turkey',
    'skills' : ['Js' , 'Python', 'cpp'],
    'address' :{
        'street' : 'moon',
        'pin' : 8065
    }
}
print(person)
print(len(person))

#acess values of dictionary :
print(person['First_name'], person['age'])
print(person['age'])

#acess dict values using .get()
print(person.get('skills'))
print(person.get('address'))

#adding new key & value pair to person
person['job_title'] = 'developer' #add new key
person['skills'].append('HTML') #append 
person['age'] = 42
#update
person.update({'job_title': 'tester'})
person['First_name'] = 'anna'
print(person)

#use in operator to check in dictionary
print('First_name' in person)
print('turkey' in person)

#methods in dictionary
#keys()
keys= person.keys()
print(keys)

#values()
values = person.values()
print(values)

person_copy = person.copy()
print(person_copy)

#deleting in dictionary
person.pop('First_name')
print(person)

person.popitem()
print(person)

del person['age']
print(person)