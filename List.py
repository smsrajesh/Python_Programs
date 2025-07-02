
"""
    Exercise : Nested list
    WAP to insert a value in the specified location with specified value

"""

row_1=['😊','😊','😊']
row_2=['😊','😊','😊']
row_3=['😊','😊','😊']

matrix=[row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

position=input("Enter a value of two digit in the range of 33: ")
row_number=int(position[0])
column_number=int(position[1])

matrix[row_number-1][column_number-1]=input("Enter the value to store : ")
print(f"{row_1}\n{row_2}\n{row_3}\n")
print(matrix)

