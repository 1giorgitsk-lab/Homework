# 1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს
# 1-დან "n"-მდე რიცხვების ჯამს.


# n = int(input("Enter number: "))
# sum = 0
# for i in range(n):
#     sum += i
#     print(sum)


# 2. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while"
# ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1


# num = int(input("Enter number: "))
#
# while True:
#     print(num)
#     num -= 1
#     if num == 0:
#         break


# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ
# განსაზღვრული რიცხვი. როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.


# import random
#
# guess = random.randrange(1, 10)
# attempt = 3
#
# while attempt > 0:
#     num = int(input("guess the number, from 1 to 10: "))
#     if num == guess:
#         print("you Win!")
#         break
#     attempt -= 1
# else:
#     print("you Lose!")



# 4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი
# total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს
# პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება
# შეყვანილი დადებითი რიცხვების ჯამი.

# total_sum = 0
#
# while True:
#     num = input("Enter a number or 'sum' to stop: ")
#     if num == "sum":
#         break
#     elif int(num) > 0:
#         total_sum += int(num)
# print(total_sum)



