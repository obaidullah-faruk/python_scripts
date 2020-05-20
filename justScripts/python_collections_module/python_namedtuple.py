from collections import namedtuple

Person = namedtuple("Person", 'name,age')    # Similar like struct
person = Person("Faruk", 25)
print(person)
print(f"{person.name}, {person.age}")