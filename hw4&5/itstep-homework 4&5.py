# # 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.
#
# str = input("enter some text").encode("utf-8")
# print(str)
#
# # 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# # ჩამოაშორეთ ზედმეტი ინტერვალები.
# # ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# # დაუმატეთ ქვესტრიქონი 'Python'.
# # თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
# #
# # მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip().
# #
# # მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"
#
#
# str = input("enter some text").strip().lower()
# str2 = "Python"
# print(str.replace("python",str2))

# # 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# # პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# # რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.
# 
# str = input("enter a word")
# rng = int(len(str)/2)
# print(str[0:rng])

# # 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# # string მოდულის გამოყენებით დაწერეთ შემოწმება.
# # სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# # მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.
#
# from string import ascii_lowercase, ascii_uppercase, digits, punctuation
#
# str = input("enter some text that contains letters, numbers and dont contains symbols")
#
# strc = 0
# dgtc = 0
#
# for i in str:
#     if i in ascii_lowercase or i in ascii_uppercase:
#         strc += 1
#     if i in digits:
#         dgtc += 1
#     if i in punctuation:
#         print("symbols arent allowed")
#         break
# else:
#     if strc > 0 and dgtc > 0:
#         print("everything is OK")

# # 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# # სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# # გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.
#
# str = input("enter some text")
#
# bytes_str = str.encode("utf-8")
# print(bytes_str)
#
# original_str = bytes_str.decode("utf-8")
# print(original_str)




# # 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს
# # სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი;
# # 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
# #
# # a – append
# #
# # r – remove
# #
# # e – exit
# #
# # გამოიყენეთ მხოლოდ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.
#
# lst = []
#
# while True:
#     option = input("choose option: 'a'-to append, enter 'r'-to remove and enter 'e'-to exit")
#     if option == 'e':
#         break
#
#     num = input("enter a number")
#
#     if option == 'a':
#         lst.append(num)
#     elif option == 'r':
#         lst.remove(num)
#
# print(lst)




# # 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list_1 = [43, '22', 12, 66, 210,
# # ["hi"]], და შეასრულებს შემდეგ ნაბიჯებს:
# #
# # a. დაბეჭდავს 210-ის ინდექსს;
# #
# # b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
# #
# # c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
# #
# # d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის მნიშვნელობა, გაასუფთავეთ
# # my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.
# #
# # მინიშნება: სიის გასუფთავება – arr.clear()
#
# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]
#
# print(my_list_1.index(210))
# my_list_1.append("hello")
# my_list_1.remove(my_list_1[2])
# print(my_list_1, "\n")
#
# my_list_2 = my_list_1.copy()
# my_list_2.clear()
# print(my_list_1)
# print(my_list_2)

# # 3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი
# # ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი,
# # წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.
# #
# # მინიშნება: სრული დამთხვევისთვის გამოიყენეთ .fullmatch() მეთოდი re მოდულიდან.
#
# import re
#
# number = input("enter phone number: (xxx) xxx-xxx")
#
# pattern = r"\(\d{3}\)\s\d{3}[\-]\d{3}"
#
#
# if re.fullmatch(pattern, number):
#     print(number)
# else:
#     print("Invalid Number")