
from secrets import choice
from Employee import Emp
import datetime
class Management:
    found2=False
    def Insert(e):
        fp =open("Emp.txt","a")
        data =str(e)
        fp.write(data)
        fp.write("\n")
        fp.close()
        
    def show_emp():
        try:
            fp = open("Emp.txt","r")
            print("="*127)
            F="%15s %15s %15s %15s %15s %15s %15s %15s "    
            print(F % ("ID","NAME", "MOBILE","EMAIL ADDRESS","Department","Designation","Salary","Date of Joining"))
            
            print("="*127)
        except FileNotFoundError:
            print("File not found...!")
        else:  
            for data in fp:
                data= data.strip()
                data=data.split(",")
                print("%15s %15s %15s %15s %15s %15s %15s %15s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            fp.close()

    def searchempid(ID):
            try:
                fp = open("Emp.txt","r")
                print("="*127)
                F="%15s %15s %15s %15s %15s %15s %15s %15s " 
                print(F % ("ID","NAME", "MOBILE","EMAIL ADDRESS","Department","Designation","Salary","Date of Joining"))
                print("="*127)
            except FileNotFoundError:
                print("File not found...!")
            else:  
                
                for line in fp:
                    line= line.strip()
                    line =line.split(",")
                    if (int(line[0]) == ID):
                        print("%15s %15s %15s %15s %15s %15s %15s %15s"%(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
                        break
                    
                else:
                    print("ID not found")    

    def searchempnm(NAME)  :
        try:
            fp = open("Emp.txt","r")
            print("="*127)
            F="%15s %15s %15s %15s %15s %15s %15s %15s " 
            print(F % ("ID","NAME", "MOBILE","EMAIL ADDRESS","Department","Designation","Salary","Date of Joining"))
            print("="*127)
        except FileNotFoundError:
            print("File not found...!")
        else:  
            
            for line in fp:
                line= line.strip()
                line =line.split(",")
                if (str(line[1]) == NAME):
                    print("%15s %15s %15s %15s %15s %15s %15s %15s"%(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
                    break
                
            else:
                print("Name not found")    

    def searchAcc(mb):
        try:
            fp = open("Emp.txt","r")
        except FileNotFoundError:
            print("File not found...!")
        else:
            #found= False
            for i in fp:
                i= i.strip()
                i=i.split(",")
                
                if( mb== int(i[2])):
                    print("Account Found")
                    Management.found2= True
                    break
                    
            else:
                print("Account Not Found")
    def viewsal(mb):
        try:
            fp = open("Emp.txt","r")
            print("="*140)
            F="%60s    "    
            print(F % ("Salary"))
            print("="*140)
        except FileNotFoundError:
            print("File not found...!")
        else:
            #found= False
            for i in fp:
                i= i.strip()
                i=i.split(",")
                
                if( mb== int(i[2])):
                    print(" %60s"%(i[6]))
                    Management.found2= True
                    break
                    
            else:
                print("Account Not Found")                

    def viewdpt(mb):
        try:
            fp = open("Emp.txt","r")
            print("="*140)
            F="%40s    %40s  "    
            print(F % ("Department","Designation"))
            
            print("="*140)
        except FileNotFoundError:
            print("File not found...!")
        else:
            #found= False
            for i in fp:
                i= i.strip()
                i=i.split(",")
                
                if( mb== int(i[2])):
                    print("%40s    %40s  "%(i[4],i[5]))
                    Management.found2= True
                    break
                    
            else:
                print("Account Not Found") 

    def alldetails(mb):
        try:
            fp = open("Emp.txt","r")
            print("="*127)
            F="%15s %15s %15s %15s %15s %15s %15s %15s "    
            print(F % ("ID","NAME", "MOBILE","EMAIL ADDRESS","Department","Designation","Salary","Date of Joining"))
            print("="*127)
        except FileNotFoundError:
            print("File not found...!")
        else:
            #found= False
            for i in fp:
                i= i.strip()
                i=i.split(",")
                print("%15s %15s %15s %15s %15s %15s %15s %15s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                        
                if( mb== int(i[2])):
                    
                    Management.found2= True
                    break
                    
            else:
                print("Account Not Found") 
     



    def editemp(ID):
        choice2 = 0
        
        try:
            fp = open("Emp.txt","r")
        except FileNotFoundError:
            print("File not found...!")
        else:  
            found = False
            new = []
            for line in fp:
                line= line.strip()
                line =line.split(",")
                if (int(line[0]) == ID):
                    found = True
                    while(choice2 !=6):
                        print('''
                                1.Edit Employee by Name
                                2.Edit Employee by Mobile No
                                3.Edit Employee by Email
                                4.Edit Employee by Department
                                5.Edit Employee Designation
                                6.Edit Employee Salary
                                7.Edit the all details of product
                                8.Exit
                    
                        ''')
                        choice2 = int(input("Enter your choice : "))
                        if (choice2 == 1):
                            line[1] = input("Enter the name you have to be update : ")
                            break
                        elif (choice2 == 2):
                            line[2] = input("Enter the MOBILE you have to be update : ")
                            break
                        elif (choice2 == 3):
                            line[3] = input("Enter the EMAIL  you have to be update : ")
                            break
                        elif (choice2 == 4):
                            line[4] = input("Enter the DeptID  you have to be update : ")
                            break
                        elif(choice2 ==5):
                            line[5] = input("Enter the designation  you have to be update : ")
                            break
                        elif(choice2==6):
                            line[6] = input("Enter the Salary  you have to be update : ")
                            break
                        
                           
                            

                        elif (choice2 == 7):
                            line[1] = input("Enter the name you have to be update : ")
                            line[2] = input("Enter the MOBILE you have to be update : ")
                            line[3] = input("Enter the EMAIL  you have to be update : ")
                            line[4] = input("Enter the DeptID  you have to be update : ")
                            line[5] = input("Enter the designation  you have to be update : ")
                            line[6] = input("Enter the Salary  you have to be update : ")
                           
                            

                            break
                        elif (choice2 == 8):
                            break
            
                new.append(line)
                
         
            if(found):
                fp = open("Emp.txt","w")
                for i in new:
                    i = ",".join(i)
                    i += "\n"
                    fp.write(i)
                fp.close()
            else:
                print("Id not found....!")                       
                           
    def removeemp(id):
        try:
            fp = open("Emp.txt","r")
        except FileNotFoundError:
            print("File not found...!")
        else:  
            found = False
            new = []
            for line in fp:
                line= line.strip()
                line =line.split(",")
                if (int(line[0]) == id):
                    found = True
                else:
                    new.append(line)
            if(found):
                if(found):
                    fp = open("Emp.txt","w")
                    for i in new:
                        i = ",".join(i)
                        i += "\n"
                        fp.write(i)
                    fp.close()
            else:
                print("Id not found....!")


    def TOTSal():
        try:
            fp = open("Emp.txt","r")
        except FileNotFoundError:
            print("File not found...!")
        else:                   
            print("Please Note the Gross Salary is calculated on basis of following criteria")
            print("1. HRA is 30%  of Basic Salary")
            print("2. DA is 15%  of basic Salary")
            print("3. TAX deducted is 15%  of(Basic +HRA +DA)")
            print("4. Total Gross Salary is: Basic +HRA + DA - TAX")
            ch= input("Continue(Y/N)")

            if ch=='y' or ch=='Y':
                print("="*140)
                F="%15s %15s %15s %15s %15s %15s %15s  "     
                print(F % ("ID","NAME", "Basic Salary","HRA","DA","TAX","GROSS"))
                print("="*140)
                for i in fp:
                    i= i.strip()
                    i=i.split(",")                    
                    HRA =round(30*int(i[6])/100,0)
                    DA  =round(15*int(i[6])/100,0)
                    TAX = round(((int(i[6])+HRA+DA)*15/100),0)
                    GROSS =HRA+DA+(int(i[6])-TAX)
                    print(F % (i[0],i[1],i[6], HRA , DA ,TAX , GROSS))

                #print("%15s %15s %15s %15s %15s %15s %15s %15s"%(i[0],i[1],i[2],i[3],i[4],i[5],int(i[6]),i[7],HRA , DA ,TAX , GROSS))
            else:
                print("Go to Main menu")
        
            

      
