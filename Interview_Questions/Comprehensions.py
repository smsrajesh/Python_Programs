
# create a collection (list/set/dictionary) 
# in a single line using loop + optional condition 
# is called comprehension.
# we can say as "short form of for loop".

# List_Comprehension = [] 

# Q1.Create a list of squares of numbers from 1 to 10 using list comprehension.

squares_list=[ i**2 for i in range(1,11)]
print(squares_list)


# Q2.Create a list of even numbers from 1 to 20 using list comprehension.

even_num_list=[i for i in range(1,21) if i %2==0]
print(even_num_list)



# Set_Comprehension = {} 

# n=[1,2,2,3,4,5,5,6,7,8,9,10]
# de_dup={ i for i in n}
# print(de_dup)

# Q1.Create a set of squares of numbers from 1 to 10 using set comprehension.

# square_set={i**2 for i in range(1,11)}
# print(square_set)

# Q2.Create a set of even numbers from 1 to 20 using set comprehension.

# even_num_set={i for i in range(1,21) if i%2==0}
# print(even_num_set)



# Dictionary_Comprehension = {k:v}

# n=[1,2,2,3,4,5,5,6,7,7,8,9,10]
# de_dup={ i:i*i for i in n}
# print(de_dup)


# Q1.Create a dictionary of numbers from 1 to 10 and their squares using dictionary comprehension.

# square_dict={i:i**2 for i in range(1,11)}
# print(square_dict)

# Q2.Create a dictionary of even numbers from 1 to 20 and their squares using dictionary comprehension.

# even_square_dict={i:i**2 for i in range(1,21) if i%2==0}
# print(even_square_dict)


# There is no tuple comprehension in python but we can create a generator expression 
# which is similar to tuple comprehension.

t=(i for i in range(1,11))
print(type(t)) # It returns <class 'generator'>

# If you want it to be a tuple then you can convert it to a tuple using the tuple() function.
n=[1,2,3,3,4,5,5,6,2,4]
t1=tuple(i for i in n)
print(t1)
print(type(t1)) # It returns <class 'tuple'>

