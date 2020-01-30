# Page 24, programming tasks for HL 13th Oct 2019
                                                                          
import statistics


def show_logo():
    print('''____    __    ____  _______  __        ______   ______   ___  ___
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______| \n \n''')



def get_marks_name():
                global x
                global student_name
                global teacher_name
                student_name = input("Please enter your name : ")
                teacher_name = input("Please enter your computer science teacher's name : ")
                h_1 = int(input("Please enter your mark out of 10 for Homework 1 : "))
                h_2 = int(input("Please enter your mark out of 10 for Homework 2 : "))
                h_3 = int(input("Please enter your mark out of 10 for Homework 3 : "))
                h_4 = int(input("Please enter your mark out of 10 for Homework 4 : "))
                data = [h_1,h_2,h_3,h_4]
                x = statistics.mean(data)
                return x, student_name, teacher_name
show_logo()

get_marks_name()

if int(x) >= 8 :
                print("Well done", student_name, ",", teacher_name, "is very pleased with your efforts.")
elif int(x) >= 6 :
                print("A good effort,", student_name, ".", teacher_name, "thinks you should check your work carefully.")
elif int(x) >= 5 :
                print(student_name,"this is very poor",",", teacher_name, "has asked you to try harder.")
else:
                print("\n ERROR IN VALUES. ABORTING \n")


































































































































                
