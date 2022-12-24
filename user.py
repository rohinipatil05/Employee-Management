
from Employee import *
from Management import Management
def user():
    found= False
    user = input("Are you the Employee of Company(Y/N):").lower()
        
    if(user=='y' or user=='yes'):
        id =int(input("Enter your Id:"))
        mb = int(input("Enter your Mobile No:"))
        
        Management.searchAcc(mb)

        if(Management.found2 == True):
            print('''
                                        =======================================================
                                                Welcome to Employee Management System
                                        =======================================================
                        ''')
            ch=0
            while(ch!=4):            
                print('''
                        1.View my Salary.
                        2.View my Department and Designation.
                        3.View all my Details.
                        4.MAIN MENU
                    ''')
                ch = int(input("Enter your choice : "))
                if(ch == 1):
                   Management.viewsal(mb)
                    
                elif(ch == 2):
                    Management.viewdpt(mb)

                elif(ch==3):
                    Management.alldetails(mb)
                    
                elif(ch == 4):
                    print("Thank You ....!")
                    break
                else:
                    print("INVALID Choice")
