my_dict = {"Nadya": 1981, 'Sahsa': 1970, 'Vlad': 1999}
print(my_dict)
print(my_dict['Vlad'])
my_dict['Toma'] = 1962
print(my_dict)
my_dict.update({'Garik': 2015, 'Balu': 2022})
print(my_dict)
del my_dict['Sahsa']
my_dict.pop('Nadya')
print(my_dict)
my_set_ = {3,3,3,3,7,7,7,7,9,9,9, 'str', int,}
print(my_set_)
print(my_set_.add(4))
print(my_set_.add('G'))
print(my_set_.discard(int))
print(my_set_)