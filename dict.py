# Dictionary is used to create key-value pairs

dict = {'Name':'Ganesh',
        'Age': 21,
        'Occupation':'Student'}
print(dict)

dict.keys() # Return the all keys
dict.values() # Return the all values

print(dict.items())

for key,value in dict.items():
    print(key,value)


# Different methods of dictionary

dict['new'] = 'New_Value' # Adding key value pair.
print(dict)

dict.pop('new') # Removes the key value pair from dict
print(dict)