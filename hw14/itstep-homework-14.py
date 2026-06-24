# # შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:
# #
# # id,name,age,grade,subject_name,mark
# # 1,string,0,string,string,0
# # 2,string,0,string,string,0
# #
# #
#
# import os, csv
# path = "files"
# filename = "data1.csv"
#
# os.makedirs(path, exist_ok=True)
# filename = os.path.join(path, filename)
#
# head = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
# data = [
#     ['1', 'name1', 21, 'E', 'subj_2', 51],
#     ['2', 'name2', 22, 'D', 'subj_2', 61],
#     ['33', 'name3', 23, 'C', 'subj_1', 71],
#     ['4', 'name4', 24, 'B', 'subj_1', 81],
#     ['55', 'name5', 25, 'A', 'subj_3', 91],
# ]
#
# with open(filename, mode='w', encoding='utf-8') as file:
#   writer = csv.writer(file)
#
#   writer.writerow(head)
#   writer.writerows(data)

# # 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი სტუდენტს დაამატებს csv ფაილში.
# #    დაასორტირეთ მონაცემები id-ის მიხედვით.
# #
# #
#
# new_student = ['6', 'name_new', 20, 'B', 'subj_2', 85]
#
# def add_student(filename, new_student):
#     data.append(new_student)
#
#     data.sort(key=lambda x: int(x[0]))
#
#     with open(filename, mode='w', encoding='utf-8') as file:
#         writer = csv.writer(file)
#
#         writer.writerow(head)
#         writer.writerows(data)
#     print("მონაცემები წარმატებით განახლდა ფაილში!")
#
# add_student(filename, new_student)


# # 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა,
# #    ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.
# #
# #
#
# user_input = input("insert student ID or type 'all' to print all students data")
#
# def one_or_all(user_input):
#     with open(filename, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#
#         if user_input == 'all':
#               for row in reader:
#                 print(row)
#         else:
#             for row in reader:
#                 if user_input == row[0]:
#                     print(row)
#
#
# one_or_all(user_input)


# # 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.
# #
# #
#
# def average_mark_by_subject(filename):
#     subject_stats = {}
#     with open(filename, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         next(reader)
#
#         for row in reader:
#             subject = row[4]
#             mark = int(row[5])
#
#             if row[4] in subject_stats:
#                 subject_stats[subject][0] += mark
#                 subject_stats[subject][1] += 1
#             else:
#                 subject_stats[subject] = [mark, 1]
#
#     for subject, stats in subject_stats.items():
#         total_mark = stats[0]
#         count = stats[1]
#         average = total_mark / count
#
#         print(f"{subject:<15} | {average:<12.2f}")
#
#
# average_mark_by_subject(filename)

# # 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება
# #    სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის `id`,
# #    საგანს და განახლებულ ქულას.
# #
# #
# user_input = input("insert student ID: ")
# user_input2 = input("insert student mark: ")
#
# def change(user_input, user_input2):
#     updated_rows = []
#
#     with open(filename, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#
#         for row in reader:
#             if user_input == row[0]:
#                 row[5] = int(user_input2)
#             updated_rows.append(row)
#
#     with open(filename, mode='w', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(updated_rows)
#
# change(user_input, user_input2)


# # 5. დაამატეთ ახალი სტუდენტი და ჩაწერეთ ფაილში.
# #
# #
# import os, csv
# path = "files"
# filename = "data3.csv"
#
# os.makedirs(path, exist_ok=True)
# filename = os.path.join(path, filename)
#
# head = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
# students = [
#   {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
#   {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
#   {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
#   {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
#   {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
#   {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
#   {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
# ]
#
# with open(filename, mode='w', encoding='utf-8') as file:
#
#     writer = csv.DictWriter(file, fieldnames=head)
#
#     writer.writeheader()
#     writer.writerows(students)
#
#
# new_student = {
#   'id': 5,
#   'name': 'Demetre',
#   'age': 18,
#   'grade': 'A',
#   'subject_name': 'Informatic',
#   'mark': 94
# }
#
#
# with open(filename, mode='a', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=head)
#
#     writer.writerow(new_student)


