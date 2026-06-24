
# # 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
# #
# my_set = set(input("Enter a set of numbers: "))
# print(my_set)


# # 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე,
# # რომლის შეცვლაც შეუძლებელი იქნება (frozenset).
#
# my_set = frozenset(input("Enter a set of numbers: "))
# print(my_set)


# # 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები
# # კორტეჟის სახით (tuple).
#
# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
#
# my_tuple = tuple(set1 | set2)
# print(my_tuple)


# # 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური
# # ელემენტები სიის სახით (list).
#
# my_tuple = tuple(input("enter a tuple "))
# my_set = list(set(my_tuple))
# print(my_set)


# # 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# #[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# #
# # დაბეჭდეთ შემდეგი ფორმატით:
# #
# # Name: Gega, Age: 24
# # Name: Gaga, Age: 21
# # Name: Goga, Age: 19
# # Name: Giga, Age: 27
# # Name: Gagi, Age: 11
#
# my_tuple = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# for item in my_tuple:
#     print(f"Name: {item[0]}, age: {item[1]}")


#
# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# დავბეჭდოთ თანხვედრა.

# customer1 = ["Irakli", "Giorgi", "Nona", "Oto"]
# customer2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
#
# my_intersection = set(customer1) & set(customer2)
# print(my_intersection)