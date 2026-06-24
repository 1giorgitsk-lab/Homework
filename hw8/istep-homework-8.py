# # 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n
# # რაოდენობის მიმდევრობას.
# #
#
# def fibonacci(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b,a+b
#     return a
#
# print(fibonacci(10))
#
#
# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა
# სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან
# შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.
#
# str1 = input("Enter a string")
# str2 = input("Enter a string")
#
# def anagram(str1, str2):
#     if  sorted(str1) == sorted(str2):
#         return "Anagram"
#     else:
#         return "Not Anagram"
#
# print(anagram(str1, str2))
#


# # 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
# #
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
#
# print(factorial(5))
#
#
# #
# # 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს.
# # ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს
# # მისი რაოდენობა.
#
# str = input("Enter a string")
# chr = input("Enter a character")
# def check(str,chr):
#     sum = 0
#     for i in str:
#         if chr == i:
#             sum +=1
#     return sum
#
# print(check(str,chr))


