list_of_students=[
    {"Roll_Number":1,
    "Name":"Upneet",
    "Class":12,
    "Subject":["Maths","Physics","Chemistry"]},
    
    {"Roll_Number":2,
    "Name":"Banipreet",
    "Class":12,
    "Subject":["Maths","Physics","Chemistry"]},

     {"Roll_Number":3,
    "Name":"Arshdeep",
    "Class":12,
    "Subject":["Maths","Physics","Chemistry"]},

     {"Roll_Number":4,
    "Name":"Punarpratap",
    "Class":12,
    "Subject":["Maths","Physics","Chemistry"]}
    ]
def update_name():
    update_list=int(input("Enter the roll number you want to update :"))
    updated_name=input("enter a name you want to update")
    if update_list==1:
        list_of_students[0]['Name']=updated_name
        print(list_of_students) 

    elif update_list==2:
        list_of_students[1]['Name']=updated_name
        print(list_of_students)

    elif update_list==3:
        list_of_students[2]['Name']=updated_name
        print(list_of_students)  

    elif update_list==4:
        list_of_students[3]['Name']=updated_name
        print(list_of_students)

    else:
        print("wrong info provided")          


    



print("1.List Students\n""2.Search Student\n""3.Update Student\n""4.Delete student\n""5.Add a student\n""6.Exit")
option=int(input("please Choose an option : "))

if option==1:

    print(list_of_students)

elif option==2:
    roll_number=int(input("Enter a roll number(1-4) :"))
    if roll_number==1:
        print(list_of_students[0])

    elif roll_number==2:
        print(list_of_students[1])

    elif roll_number==3:
        print(list_of_students[2])

    else :
        print(list_of_students[3])



elif option==3:
    update_name()
    # update_list=int(input("Enter the roll number you want to update :"))
    # updated_name=input("enter a name you want to update")
    # if update_list==1:
    #     list_of_students[0]['Name']=updated_name
    #     print(list_of_students)


elif option==4:
    delete_name=int(input("enter the roll number to delete its info"))
    del list_of_students[delete_name]
    print(list_of_students)

elif option==5:
    def add_a_student():
        new_student = {
                    "roll number":0,
                    "name":"",
                    "class":"",
                    "subjects":[]
                    }
        
        new_roll_number=int(input("enter new roll number\n"))
        new_name=input("enter new name\n")
        new_class=input("enter new class")
        for i in range(3):
            new_subjects=input("enter subject name")
            new_student["subjects"].append(new_subjects)
        new_student.update({"roll number":new_roll_number, "name":new_name, "class":new_class,"subjects":new_subjects})
        list_of_students.append(new_student)
        print(list_of_students)

add_a_student()
    
    





    



