# CONDITIONAL STATEMENTS ARE TYPE OF STATMENTS IN WHICH CONDITION IS
# SPECIFIED THROUGH WHICH THE CONTROL FLOW OF THE PROGRAM IS CONTROLLED
# SO WHENEVER THE CONDITIONAL STATEMENTS BECOMES FULFILLED THE BLOCK OF CODE RUNS
# INSIDE OF IT



# IF STATEMENTS

student_marks = [98, 79, 30] # each subject has total of 100 marks
total_marks = 300
obtained_marks = sum(student_marks)
student_percentage = obtained_marks / total_marks * 100
print("Student Obtained ", end="")
if student_percentage >= 50 and student_percentage < 70 :
    print("Grade C", end="")
print(" with ", obtained_marks, "/" , total_marks," marks ", sep="")


# SHORT HAND IF OR TERNARY OPERATORS
name = "cat is a dog"
result = True if name.__len__() == 0 else False
print("is str \"name\" empty? ",result)

# IF-ELSE STATEMENT WHERE OF THE CONDITION IS NOT TRUE THAN RUN AUTOMATICALLY THE OTHER PART
i = 3
if i % 2 == 0:
    print(i, "is Even Number")
else:
    print(i, "is Odd Number")

num = 5
if not num < 5:
    print("Number", num, "is greater than", 5)



# IF-ELSE-IF PROGRAM WITH COMPLETE GRADING
# modifying previously decalred student result data
student_marks = [60, 100 , 60]
obtained_marks = sum(student_marks)
student_percentage = obtained_marks / total_marks * 100

print("Student Obtained ", end="")
if student_percentage >= 90:
    print("Grade A", end="")
elif student_percentage >= 70 and student_percentage < 90:
    print("Grade B", end="")
elif student_percentage >= 50 and student_percentage < 70:
    print("Grade C", end="")
elif student_percentage < 50:
    print("Grade D", end="")
print(" with ", obtained_marks, "/" , total_marks," marks ", sep="")


