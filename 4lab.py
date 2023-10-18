input = input("Enter is: ")  
input = input.lower()  
list = input.split()  
print("Created list is:", list)


from collections import Counter
symbol = Counter("".join(list))
symbol_list = [(symbol, count) for symbol, count in symbol.items()]
symbol_list.sort()
print("List of symbol counts:", symbol_list)


def is_vowel(char):
    return char in "aeiou"
list_vow = []
list_cons = []
list_symb = []
for symbol, count in symbol_list:
    if symbol.isalpha():
        if is_vowel(symbol):
            list_vow.append((symbol, count))
        else:
            list_cons.append((symbol, count))
    else:
        list_symb.append((symbol, count))
print("List of vowels:", list_vow)
print("List of consonants:", list_cons)
print("List of symbols:", list_symb)



list_A = [12, 5, 8, 19, 27, 14, 3, 7, 21, 9]
list_A.sort()
q1, q2, q3, q4 = [], [], [], []
n = len(list_A)
q1_end = n // 4
q2_end = 2 * q1_end
q3_end = 3 * q1_end
q1 = list_A[:q1_end]
q2 = list_A[q1_end:q2_end]
q3 = list_A[q2_end:q3_end]
q4 = list_A[q3_end:]
if n % 4 != 0:
    q1.append(0)
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)


student_data = {
    "Name": "John Doe",
    "Assignments": [90, 85, 92, 78],  
    "Labs": [95, 88, 75, 82],  
    "Tests": [88, 92, 79, 95] 
}
print("Student Information:")
print("Name:", student_data["Name"])
print("Assignments:", student_data["Assignments"])
print("Labs:", student_data["Labs"])
print("Tests:", student_data["Tests"])


student_data = {
    "Name": "John Doe",
    "Assignments": [90, 85, 92, 78],
    "Labs": [95, 88],
    "Tests": [88, 92],
}
submission_check = {}
name = student_data["Name"]
submitted_activities = 0
if len(student_data.get("Assignments", [])) == 4:
    submitted_activities += 4
if len(student_data.get("Labs", [])) == 2:
    submitted_activities += 2
if len(student_data.get("Tests", [])) == 2:
    submitted_activities += 2
submission_check[name] = submitted_activities
print("Submission Check:")
print(submission_check)


student_data = {
    "Name": "John Doe",
    "Assignments": [90, 85, 92, 78],
    "Labs": [95, 88],
    "Tests": [88, 92],
}
submission_check = {
    "John Doe": 4 
}
if submission_check.get(student_data["Name"], 0) >= 4:
    assignments_avg = sum(student_data.get("Assignments", [0])) / 4
    labs_avg = sum(student_data.get("Labs", [0])) / 2
    tests_avg = sum(student_data.get("Tests", [0])) / 2

    final_grade = 0.3 * assignments_avg + 0.5 * labs_avg + 0.2 * tests_avg
    student_data["Final Grade"] = final_grade
else:
    student_data["Final Grade"] = 0
print("Updated Student Data:")
print(student_data)


student_data_1 = {
    "Name": "John Doe",
    "Assignments": [90, 85, 92, 78],
    "Labs": [95, 88],
    "Tests": [88, 92],
    "Final Grade": 0.0,
}
student_data_2 = {
    "Name": "Jane Smith",
    "Assignments": [82, 76, 89, 94],
    "Labs": [91, 85],
    "Tests": [78, 85],
    "Final Grade": 0.0,
}
students_scores = {}
student_data_list = [student_data_1, student_data_2]
for student_data in student_data_list:
    student_name = student_data["Name"]
    student_scores = {
        "Assignments": student_data["Assignments"],
        "Labs": student_data["Labs"],
        "Tests": student_data["Tests"],
        "Final Grade": student_data["Final Grade"],
    }
    students_scores[student_name] = student_scores
print("Students' Scores:")
print(students_scores)


user_transactions = [
    (1,2,3),
    (2,1,2),
    (3,3),
    (4,1,2),
    (5,1,2,3),
]
user_statistics ={}
for transaction_set in user_transactions:
    user_id =transaction_set[0]
    transactions = transaction_set[1:]
    if user_id  not in user_statistics:
        user_statistics[user_id] = {"comment":0,"like":0,"share":0,"mft": None,"lft": None}
for transaction in transactions:
    if transaction ==1:
        user_statistics[user_id]["comment"]+=1
    elif transaction==2:
        user_statistics[user_id]["like"]+=1
    elif transaction ==3:
        user_statistics[user_id]["share"]+=1
        mft=max(user_statistics[user_id], key=lambda key: user_statistics[user_id][key])
        lft= min(user_statistics[user_id], key=lambda key: user_statistics[user_id][key])
        user_statistics[user_id]["mft"]=mft
        user_statistics[user_id]["lft"]=lft
        for user_id, stats in user_statistics.items():
            print(f"User {user_id}-comment:{stats['comment']}, like: {stats['like']}, share: {stats['share']}, MFT: {stats['mft']}, LFT: {stats['lft']}")
