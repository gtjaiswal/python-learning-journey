# 1️⃣ Ask user to enter student names and marks until they type 'done'.
# 2️⃣ Store data in a dictionary {student_name: [marks]}.
# 3️⃣ Compute and display:
#     - Average marks per student
#     - Class topper(s)
#     - Class average
#not_done = True
dict_marks = {}
str_student_marks = input("Enter Student Name followed by comma sepertaed marks for 5 subjects. Enter \"done\' to end input. ")
while str_student_marks != "done":
    name, marks_str = str_student_marks.split(":")
    marks_int = [int(num) for num in marks_str.split(",")]
    print(f" Name : {name}, Marks : {marks_int} ")
    #marks_int.append(sum(marks_int)/len(marks_int))
    dict_marks[name]= marks_int
    print(dict_marks)
    str_student_marks = input("Enter next Student Name followed by comma sepertaed marks for 5 subjects. Enter \"done\' to end input. ")
print(f"Individual Report : \n {dict_marks}",dict_marks)
print("all done!")