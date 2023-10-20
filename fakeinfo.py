#Create a program to generate fake data like name, email, or detailed fake profile with all the information about a person.

from faker import Faker
fake = Faker()
print(fake.name())
print(fake.email())
print(fake.country())

print(fake.profile())                                                        
