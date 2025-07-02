var_year=int(input("Enter Value of Year = "))

# Output - 1:

# if (var_year%4==0):
#     if (var_year%100==0):
#         if (var_year%400==0):
#             print(f"{var_year} is a leap year")
#         else:
#             print(f"{var_year} is not a leap year")
#     else:
#         print(f"{var_year} is a leap year")
# else:
#     print(f"{var_year} is not a leap year")



# Output - 2:

if ((var_year%4==0 or var_year%100==0) and var_year%400==0):
    print(f"{var_year} is a leap year")
else:
    print(f"{var_year} is a  not leap year")   


