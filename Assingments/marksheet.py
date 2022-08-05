from re import T
from tkinter import N
from turtle import title


print("\t \t ******* Marks Sheet *******")
print("\t Board of Intermediate & Secondary Education, Gujranwala")
# Take the name of student as a input from user 
name= input("Please enter your name: ")
# Take Father name as a input from user
father_name=input("please enter your father name:")
#Roll no
roll_no=int(input("Please enter your roll no"))

# Subjects Marks given by the user
english= int(input("Please enter the marks obtain in English: "))
urdu= int(input("Please enter the marks obtain in Urdu: "))
islamiyat= int(input("Please enter the marks obtain in Islamiyat: "))
pak_studies= int(input("Please enter the marks obtain in Pak Studies: "))
math= int(input("Please enter the marks obtain in Mathmatics: "))
physics= int(input("Please enter the marks obtain in Physics: "))
Chemistry= int(input("Please enter the marks obtain in Chemistry: "))
biology= int(input("Please enter the marks obtain in biology: "))

total_marks=800
total_subject=8
# Percantage marks obtain by the studens in different subjects
obtain_marks=english+urdu+islamiyat+pak_studies+math+physics+Chemistry+biology
print("Total marks obtain is: ", obtain_marks)
percantage_marks=(obtain_marks/total_marks)*100
print("Ypur percantage of marks is: ", percantage_marks)

# programe to get the Grade of students on  the bassis of percantage marks 
if percantage_marks >=90:
    print("Congrulation you have got A+ grade in Exam.")
elif percantage_marks>=80 and percantage_marks<=89:
    print("Congrulation you have got A grade in Exam.")  
elif percantage_marks>=70 and percantage_marks<=79:
    print("Congrulation you have got B grade in Exam.")
elif percantage_marks >= 60 and percantage_marks <= 69 :
    print("Congrulation you have got C grade in Exam.")
elif percantage_marks >= 50 and percantage_marks <= 59 :
    print("Congrulation you have got D grade in Exam.")
elif percantage_marks >= 40 and percantage_marks <= 49 :
    print("Congrulation you have got E grade in Exam.")
else:
    print("Unfortunately you are fail in this Exam try next time.")    
