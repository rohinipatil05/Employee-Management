
class Emp:
    count=100
    def __init__(self ,nm = "default",mb = 0,EM = "none",DeptID = 0,Designation="none",Salary=0,DateofJoining="none"):
        Emp.count +=1
        self.ID= Emp.count 
        self.enm = nm
        self.mb = mb
        self.EM = EM 
        self.DeptID = DeptID
        self.Designation=Designation
        self.Salary=Salary
        self.DateofJoining =DateofJoining


   # def showemp(self):
    #    print(self.ID,self.enm,self.mb,self.EM,self.DeptID,self.Designation,self.Salary,self.DateofJoining)
    
    def __str__(self):
        data = str(self.ID) + "," + str(self.enm)+ "," + str(self.mb) + "," + str(self.EM) + "," + str(self.DeptID)+"," + str(self.Designation) + "," + str(self.Salary) + "," + str(self.DateofJoining)  
        return data


    