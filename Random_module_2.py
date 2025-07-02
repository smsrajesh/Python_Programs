import random

# Type - 1 :

names=input("Enter the names separated by comma : ")
individual_names=names.split(",")
pay_person=individual_names[random.randrange(0,len(individual_names))]
print(f"{pay_person} pays\'s the Bill")


# Type - 2 :

names=input("Enter the names separated by comma : ")
individual_names=names.split(",")
choice_person=random.choice(individual_names)
print(f"{choice_person} pays\'s the Bill")

