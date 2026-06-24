# # 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip
# # ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
# #
# # params: [1, 2, 3], ['a', 'b', 'c']
# # outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]
# #
# #
# params = [1, 2, 3], ['a', 'b', 'c']
#
# def func(lst1, lst2):
#     return list(zip(lst1,lst2))
#
# print(func(*params))


# # 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების
# # ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის
# # პარამეტრს (TypeError).
# # ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.
# #
# # params:[1, 2, 3, 4, 5]
# # output: 120
#
#
# from functools import reduce
# params=[1, 2, 3, 4, 5]
#
# def func(lst):
#     try:
#         result = reduce(lambda x, y: x * y, lst)
#         return result
#     except TypeError:
#         return TypeError
#
# print(func(params))


# # 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის
# # კენტ ელემენტებს.
# #
# # params: [1, 2, 3, 4, 5, 6, 7]
# # outputs: [1, 3, 5, 7]
# #
# #
# params = [1, 2, 3, 4, 5, 6, 7]
# new_params = []
#
# def func(lst):
#     for item in lst:
#         if item % 2 == 1:
#             new_params.append(item)
#     return new_params
#
# print(func(params))


# # 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
# # დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
# # გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა
# # გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
# #
# # მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას,
# # რომელიც მთავრდება რაღაც სიმბოლოებით...
# #
# # params: ['hello', 'world', 'coding', 'nod'], 'ing'
# # outputs: ['coding']
#
#
# params = ['hello', 'world', 'coding', 'nod'], 'ing'
#
# def func(par1, par2):
#     word = list(filter(lambda x: x.endswith(par2), par1))
#     return word
#
# print(func(*params))
