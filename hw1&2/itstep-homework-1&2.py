## დავალება 1 და დავალება 2



## დავალება 1



## 1. კონსოლიდან შეიტანეთ ორი რიცხვი და დაბეჭდეთ ყველა არითმეტიკული ოპერაცია (მიმატება, გამოკლება,
## გამრავლება, ჩვეულებრივი გაყოფა, მთელზე გაყოფა, ნაშთის აღება, ახარისხება).

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")
# print(f"{num1} // {num2} = {num1 // num2}")
# print(f"{num1} % {num2} = {num1 % num2}")
# print(f"{num1} ** {num2} = {num1 ** num2}")

## 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს
## ორი დიაგონალის სიგრძე.

# diag1 = int(input("Enter first diagonal: "))
# diag2 = int(input("Enter second diagonal: "))
#
# print(f"area: {diag1} * {diag2} * 1/2 = {diag1 * diag2 * 1/2}")

## 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში,
## დეციმეტრებში, მილიმეტრებში, მილში.

# meter = int(input("Enter number of meters: "))
#
# print(f"{meter} m = {meter * 100} cm ")
# print(f"{meter} m = {meter * 10} dm ")
# print(f"{meter} m = {meter * 1000} mm ")
# print(f"{meter} m = {meter / 1610} mile ")

## 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს
## სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

# სიმაღლე = int(input("შეიყვანეთ სამკუთხედის სიმაღლე: "))
# ფუძე = int(input("შეიყვანეთ სამკუთხედის ფუძე: "))
#
# print(f"სამკუთხედის ფართობი: {სიმაღლე} * {ფუძე} * 1/2 = {სიმაღლე * ფუძე / 2}")

## 5. კონსოლიდან შეიტანეთ ორნიშნა რიცხვი და დაბეჭდეთ ციფრთა ჯამი.

# number = input("შეიყვანეთ ორნიშნა რიცხვი: ")
#
# ჯამი = int(number[0]) + int(number[1])
# print(f"ჯამი: {number[0]} + {number[1]} = {int(number[0]) + int(number[1])}")



## დავალება 2



## 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა
## რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
#
# num = int(input("Enter a number"))
#
# if num in num_list:
#     print("The number in list")
# else:
#     print("The number not in list")


## 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას.
## თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

# num = int(input("Enter a integer:"))
#
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")



# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ
# ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

# st1 = input("Enter a string: ")
# st2 = input("Enter another string: ")
#
# if st1 is st2:
#     print("Same object")
# else:
#     print("Different object")


# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი
# პირობა:
#
# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ
# ტექსტი "More than list elements";
#
# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
#
# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
#
# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.
#
# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
#
# num = int(input("Enter a number: "))
#
# if num_list[2] < num < num_list[-1]:
#     print("More than list element")
# elif num == num_list[5]:
#     print("Equal")
# else:
#     print("None of the conditions were met")

