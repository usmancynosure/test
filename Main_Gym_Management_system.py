print("NOte: 'Admin'is the pasward to access admin page")
print("*" * 50)
print("--------------Welcome to Lyalpur Fitness Gym----------------")
print("*" * 50)
members_details = []
new_machine=[]

#selection for admin and member
def show_options():
    print("select")
    options = int(input("Enter\n1-for Admin\n2-for members\n3-for exit\nenter your choice: "))
    return options

#function for create member
def create_member():
    Name = input("Name: \n")
    Age = input("Age: \n")
    Reg_No = input("Reg_no: \n")

    Gender = input("Gender(male/female): \n").lower()
    Bodymass = input("BMI: \n")
    Month_duration= input("Duration in months: \n")
    information = [Name, Age, Reg_No, Gender, Bodymass, Month_duration]

    members_details.append(information)

    print("Information saved successfully", members_details)


def view_member():
    print("********Viewing Member*********")
    print("[Name,  Age, Reg_No, Gender, BMI, Duration]")
    for member in members_details:
        print(member)


#function for search member 
def search_member():
    print("********Search Member*********")
    Reg_No_search = input("Enter your Reg_No:\n")
    for member in members_details:
        if Reg_No_search == member[2]:
            # print(f"The details of member is {member}")
            print(f'Name: {member[0]}')
            print(f'Age: {member[1]}')
            print(f'Reg_No: {member[2]}')
            print(f'Gender: {member[3]}')
            print(f'BMI: {member[4]}')
            print(f'Duration(in month): {member[5]}')


#function for delete member
def delete_member():
    Reg_No_search = input("Enter reg_no:\n")
    for member in members_details:
        if Reg_No_search == member[2]:
            members_details.remove(member)
            print("****Current member list is******")
            print(members_details)

#function for update member
def update_member():
    Reg_No_search = input("Enter your reg no:\n")
    for member in members_details:
        if Reg_No_search == member[2]:
            print("----------Member found succesfully----------------")
            member[4] = input("Your updated BMI")
            member[5] = input("Update Duration+'months'")
            print("********Updated Member information is**********")

            print(member)

#function for add equipments
def Add_equipment():
    for_tricep=input("Enter machine for tricep: ")          #Cable machine
    for_leg= input("Enter machine for leg Exercise:")       #leg extension
    for_wingz= input("Enter machine for Back exercise:" )    #lat pulldown
    for_bicep=input("Enter machine for biceps exercise")   #incline_curl machine
    for_Cardio=input("enter machine for cardio exercise:")  #cycling machine
    for_Chest=input("enter machine for chest exercise:")    #pec desk
    
 
    machines=[for_tricep,for_leg,for_wingz,for_bicep,for_Cardio,for_Chest]
    new_machine.append(machines)
    print(new_machine)

#function for exercise plan
#first calculate BMI
def Excercise_Plan():
    print("---------customize exercise plan according to to your BMI----------")
    weight = int(input("Enter your weight in kilogram:\n"))
    feet, inch = eval(input("Enter your height in feet and inches seperated by comma:\n"))
    feet1 = (inch / 12)
    height_in_feet = feet + feet1
    height_in_meter = (height_in_feet * 0.3048)                   
    Body_Mass_index = weight / (height_in_meter * height_in_meter)
    print("Your BMI is ",Body_Mass_index)
    if Body_Mass_index < 18.5:
        print("*********Excercise Plan for Too Slim people is***********")
        print('''
        Monday: Chest,
        Tuesday:Biceps
        Wednesday:Rest
        Thursday:Wings
        Friday:Triceps
        Saturday:Rest
        Sunday:Rest''')
    elif Body_Mass_index > 18.5 and Body_Mass_index < 25:
        print("*******Excercise Plan for Normal Person is*********")
        print('''
        Monday: Chest,
        Tuesday:Biceps
        Wednesday:Cardio
        Thursday:Back
        Friday:Triceps
        Saturday:Legs
        Sunday:Rest''')
    elif Body_Mass_index > 25 and Body_Mass_index < 30:
        print("*****Excercise plan for obessed persons*******")
        print('''
        Monday: Chest,
        Tuesday:Biceps
        Wednesday:Cardio
        Thursday:Back
        Friday:Rest
        Saturday:Legs
        Sunday:Cardio''')

    
#function for pakage category

def package_category():
    print("select category\n1.Simple package\n2.Premium package")
    option = int(input())
    if option == 1:
        print("-------------You selected Simple Package------------")
        print("1.with_trainer_charges=45000\n2.without_trainer_charges=25000")
        select = int(input('>'))
        if select == 1:
            charges=45000
            print(f"your membership per yearly charges[with_trainer] is={charges}/yr")
        else:
            charges=25000
            print(f"yours membership per yearly charges[without_trainer] is={charges}/yr")
    elif option == 2:
        print("----------You selected Premium package------------")
        print('''select package\n1.with_trainer_charges = 1500000\n 2.without_trainer_charges=100000''')
        select=int(input('>'))
        if select==1:
            charges=150000
            print(f"your membership charge per year[with trainer] is:{charges}/yr")
        elif select==2:
            charges=100000
            print(f"your membership charge per year[with out trainer] is:{charges}/yr")
        else:
            print("invalid option")
#function for view equipment
def view_equipment():
    print("*********Viewing Machnes*******")
    print("[for_triceps, for legs,  for wingz, for biceps, for cardio,  for chest]")
    for machines in new_machine:
        print(machines)
#calling the function made by admin
while True:
    n = show_options()
    if (n == 1):
        print("welcome to Admin login")
        print("Enter the passward to login")
        
        password = input("Enter Your passward").lower()
        if (password == "admin"):
            print("********Hello Admin********")
            while True:
                admin_options = eval(input("Enter\n1-create member\n2-view member\n3-search member\n4-delete member\n5-update member\n6-Add equipment\n7-to go to menu \nenter your option: "))
                if (admin_options == 1):
                    print("Create member ")
                    create_member()
                elif (admin_options == 2):
                    view_member()
                elif (admin_options == 3):
                    search_member()
                elif admin_options == 4:
                    delete_member()
                elif (admin_options == 5):
                    update_member()
                elif (admin_options==6):
                    Add_equipment()
                elif (admin_options == 7):
                   break

        else:
            print("Wrong passward press 1 to retry")
#callling function made by member
    elif (n == 2):
        while True:
            print("HELLO MEMBER")
            member_options = int(
                input("Enter\n1-for Excercise Plan\n2-for view details,\n3-for view packages category\n4.view equipments\n5-to go to menu\n Enter your option: "))
            if (member_options == 1):
                Excercise_Plan()
                print("------your exercise plane succesfully created--------")
            elif (member_options == 2):
                search_member()
                # break
            elif (member_options==3):
                package_category()
            elif (member_options==4):
                view_equipment()
            elif (member_options==5):
                break


    elif (n == 3):
        break







