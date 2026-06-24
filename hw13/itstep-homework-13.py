

# # 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის სახელს და
# # დააბრუნებს ფაილის სრულ გზას.
#
#
#
# import os
#
# folder = "my_files"
# file = "/file1.txt"
#
# os.makedirs(folder, exist_ok=True)
#
# with open(folder + file, mode='a', encoding='utf-8') as file:
#     print(os.listdir())

# # 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.
# #
# #
# folder = "my_files"
# file = "/file1.txt"
#
#
# with open(folder + file, mode='r', encoding='utf-8') as file:
#     data = file.read()
#
# print(data)

# # 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და დაამატებს ფაილის კონტენტს.
# #
# # [
# #   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
# #   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# # ]
# #
# # ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.
# #
# #
# import json
#
# folder = "my_files"
# file = "/file1.txt"
#
# user_info = [
#    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
#
# with open(folder + file, mode='a', encoding='utf-8') as file:
#     for user in user_info:
#         json.dump(user, file)
#
#

# # 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.
#
# import json
# import os
#
# folder = "my_files"
# file = "/file2.json"
#
# new_data = {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56}
#
# with open(folder + file, mode='w', encoding='utf-8') as file:
#     json.dump(new_data, file)

