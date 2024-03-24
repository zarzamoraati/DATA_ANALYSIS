
# #Funciiones#

# def is_prime(number):
#     if number < 2 :
#             return False    
#     for i in range(2,number):
#         if number % i == 0:
#                 return False
#     return True


# print(is_prime(10))
# print(is_prime(7))
# print(is_prime(22))


# def liters_100km_to_miles_gallon(liters):
#     millas=(100*1000)/1609.344
#     galones=liters/3.78541
#     return millas/galones
#     #1km =1000m 
#     #1 milla = 1609.344 metros.
#     #1galon=3.78541L
    

# print(float(liters_100km_to_miles_gallon(3.9)))

# ##alcance local

# def scope_test():
#    my_var=777
#    print(my_var)


# my_var=200
# scope_test()
# print(my_var)


# ##Alcance global

# # def scope_test():
# #    global my_var
# #    my_var=777
# #    print(my_var)


# # my_var=200
# # scope_test()
# # print(my_var)


# ##IMC=Indice de Masa Corporal

# def bmi(weight,height):
#         mci=weight/height ** 2
#         return mci

# print(bmi(70,1.7))

# ###Es un traingulo?
# def is_triangle(a,b,c):
#         if  a+b <= c:
#             return False
#         elif a+c <= b:
#             return False
#         elif b+c <= a:
#             return False
#         else:
#             return True

# print(is_triangle(1, 1, 1))
# print(is_triangle(1, 1, 3))
