""" Testing Tuple"""

companies = ('Microsoft', 'Google', 'Amazon')

mine = companies

companies = ()
print (companies)
print("mine", id(mine), id(companies))