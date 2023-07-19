# LOOPS USED IN PYTHON CONTAINS MANY UNIQUE THINGS AS COMPARED TO
# OTHER TRADITIONAL LANGUAGES
# LOOPS ARE USED TO DO SOME KIND OF TRAVERSAL OR PROCESS ITERATIVELY 
# WITHOUT CHANGING THE FLOW OF THE PROGRAM

# FOR LOOP
students = ["student 1" ,"student 2" ,"student 3"]
print(end="\nTraversing Objects Elements (list): \n")
for student in students:
    print(student)

# printing other collections data
student_Data = [
    ("studentName", "studentRollNo", "studentClass"),
    ("Muhammad", "20-Arid-507", "BSCS-5A"),
    ("Noor Ullah", "20-Arid-537", "BSCS-5A")
]

print(end="\n\t\t\tSTUDENTS RECORD")
print("\n\n", student_Data[0][0].upper(), student_Data[0][1].upper(), student_Data[0][2].upper(), sep="\t")
for student in student_Data[1:]:
    print("", student[0], student[1], student[2], sep="\t")



# printing pattern
print(end="\nPattern: \n")
for i in range(0, 5, 1): # also providing step as third argument as 1 to be increamented by the factor
    for j in range(i, 5, 1): 
        print(j,"", sep=" ", end="") # providng separator and ending string
    else:
        print("Inner Loop Finished".center(30), sep=" ", end="\n") # run when loop finishes executing
else:
    print("Outer Loop Finished") # run when loop finishes executing



# WHILE LOOP
# while loop executes till that the condition specified is metting

print("\n\nPrinting Numbers")
x = 0
while x in range(0, 5): # will run only 1 iteration as the next will increment the x to terminal '5'
    print(x)
    x+=1

print("\n\nStudent Roll Numbers: ")
student_roll_no = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
while student_roll_no[i] is not 5: # will print numbers till 4
    print(end=student_roll_no[i].__str__() + "\t")
    i+=1


print("\n\nStudent Marks".__str__().center(20), "Student Precentage".__str__().center(20))
student_marks = [507, 798, 350]

total_marks = 800
i = 0
while i < student_marks.__len__() :
    print(student_marks[i].__str__().center(20), (student_marks[i] / total_marks * 100).__str__().center(20))
    i += 1


