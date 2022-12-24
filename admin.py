import datetime
from Employee import Emp
from Management import Management
def admin():
    
    user = input("Enter your Username: ")
    pwd =input("Enter your Password: ")

    user_id = "ADMIN"
    password = "admin!"

    if (user == user_id or pwd == password ):
        if(user == user_id):
            if(pwd == password):
                print("Your Login is Successful")

                choice=0 
                while(choice != 7):
                    print('''
                                        =======================================================
                                                Welcome ADMIN to Employee Management System
                                        =======================================================
                        ''')
                    
                    print('''
                                    1.Insert Employe Records
                                    2.Display all Employee Records 
                                    3.Search Employee Records as per ID
                                    4.Search Employee Records as per Name
                                    5.Update Record
                                    6.Delete Record
                                    7.Gross Salary
                                    8.Exit
                            ''')
                    choice = int(input("Enter your choice : "))
                    if (choice == 1):
                        nm = input("Enter the Name : ")
                        mb =int(input("Enter Mobile No"))
                        Em = (input("Enter the EMAIL : "))
                        DeptID = input("Enter the DEPARTMENT : ")
                        Designation = (input("Enter the Designation : "))
                        Salary= int(input("Enter salary"))
                        Dat = datetime.datetime.now()
                        Dat=Dat.date()
                        DateofJoining=Dat
                        p1 = Emp(nm,mb,Em,DeptID,Designation,Salary,DateofJoining)
                        Management.Insert(p1)
                    elif (choice == 2):
                            Management.show_emp()
                    elif(choice ==3):
                        ID = int(input("Enter the Id to be serched : "))
                        Management.searchempid(ID)
                    elif(choice == 4):
                        NAME=(input("Enter the NAME to be serched : "))
                        Management.searchempnm(NAME)
                    elif (choice == 5):
                        ID = int(input("Enter the Id : "))
                        Management.editemp(ID)
                    elif(choice == 6):
                        id=int(input("Enter the Id to be removed"))
                        Management.removeemp(id)
                    elif(choice==7):
                        #ID= int(input("Enter id:"))
                        Management.TOTSal()
                    elif(choice==8):
                        break
                    else:
                            print("INVALID INPUT ")
    else:
        
        print("Inavlid Details")
#admin()