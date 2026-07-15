class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print("name : {} , age: {}".format(self.name,self.age))
  
class Employee(Person):
    def __init__(self, name, age,employee_id):
        Person.__init__(self,name, age)
        self.employee_id = employee_id
    
    def show_details(self):
        print("name : {} , age: {} , employee_id {}".format(self.name,self.age,self.employee_id))
        
class PartTime(Person):
    def __init__(self, name, age,working_hours):
        Person.__init__(self,name, age)
        self.working_hours = working_hours
        
    def show_details(self):
        print("name : {} , age: {} , working_hours {}".format(self.name,self.age,self.working_hours))      
        
class Consultant(Employee,PartTime):
    def __init__(self, name, age, employee_id,working_hours,project_name):
        Employee.__init__(self,name, age, employee_id)
        PartTime.__init__(self,name,age,working_hours)
        self.project_name =project_name
        
    def show_details(self):
        print("name :{} ,age :{} ,employee_id :{} ,working_hours :{} ,project_name :{}".format(self.name,self.age,self.employee_id,self.working_hours,self.project_name)) 

Person_obj = Person("Greg",30)
Person_obj.show_details()

Employee_obj = Employee("Greg",30,110,)
Employee_obj.show_details()

PartTime_obj = PartTime("Greg",30,40)
PartTime_obj.show_details()

Consultant_obj = Consultant("Greg",30,110,40,"XYZ")
Consultant_obj.show_details()

