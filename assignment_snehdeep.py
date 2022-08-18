### TASK FOR TODAY #########
# Using functions
# Choose operation 1 - Enter data, 2 retrive data
# operation 1 -
# Take input from user, first name, last name, school name, class name, marks
# Store the data in JSON file with auto increment id
# operation 2 -
# Enter id of user to retrive.
# show data on screen for user whose id is retrived.
import json

student_id = 0
data_list = []

def what_you_want():
    print("Hey User")
    print("what you need to enter the new data or retrieve the old data\n")
    opt = int(input("press 1 for entering the new data and press 2 for retrieve old data\n"))
    if opt == 1:
        add_data()

    elif opt == 2:
        display_data()

    else:
        print(" invalid option\n")
        return 0

def add_data():
    globals()['student_id'] = globals()['student_id'] + 1
    std_id = globals()['student_id']
    first_name = input("please enter your first name\n")
    last_name = input("please enter your last name\n")
    school_name = input("Now please enter your school name\n")
    class_of_student = int(input("now please enter in which class you study\n"))
    total_marks = int(input("now enter your total marks\n"))
    obj_of_student = {"first_name": first_name, "last_name": last_name, "school_name": school_name,
                      "class_of_student": class_of_student, "total_marks": total_marks, "student_id": std_id}
    data_list.append(obj_of_student)

    x = json.dumps(data_list)
    file = open('data', 'w')
    file.write(x)
    print("your data is updated in our records\n")
    return 0

def display_data():
    file = open('data', 'r')
    data_base = json.loads(file.read())
    std_id = int(input("please enter the id\n"))
    flag = 0
    for data in data_base:
        if data['student_id'] == std_id:
            print(data)
            flag = 1
            break

    if flag == 0:
        print("No records available in the data base\n")
        return 0

while 1:
    option = int(input("1 for start the process and 0 to end the process"))
    if option == 1:
        what_you_want()

    elif option == 0:
        break
    else:
        print("invalid option try again")