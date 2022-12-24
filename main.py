from admin import admin
from user import user

ch = 0
while(ch != 4):

        print('''

                    1.ADMIN
                    2.USER
                    3.EXIT
        ''')
        ch = int(input("Enter your choice : "))
        if(ch == 1):
            
            admin()
        elif(ch == 2):
            
            user()
        elif(ch == 3):
            print("Thank You ....!")
            break
        else:
            print("INVALID Choice")
        