class Placement:
    ''' this class was developed by kiran gajjana'''
    '''by using this class the user can know wether they will be selected to the placement or not based on percentage'''

    def __init__(self,name,branch,city,percentage,college):
        self.name=name
        self.branch=branch
        self.city=city
        self.percentage=percentage
        self.college=college
    def Analysis(self):
        if self.percentage>=90: #checking wether the  person will get the placement or not based on the percentage
            print(f"Hi, {self.name} Congrats you have an capability to select in placement drive based on the below provided data by you")
            print(f"Your gud name is: {self.name}")
            print(f"your branch : {self.branch}")
            print(f"your city: {self.city}")
            print(f"your percentage : {self.percentage}")      
            print(f"your college : {self.college}") 
        else:
            print(f"Hi,{self.name} sorry you have  less chances on getting the placement based on capability to select in placement drive based on the below provided data by you")
            print(f"Your gud name is: {self.name}")
            print(f"your branch : {self.branch}")
            print(f"your city: {self.city}")
            print(f"your percentage : {self.percentage}")      
            print(f"your college : {self.college}") 
list_placements=[]
while True:
    name=input("please enter your name")
    branch=input("please enter your branch")
    city=input("please eneter your city")
    percentage=float(input("please enter your percentage"))
    college=input("please enter your college name")
    k=Placement(name,branch,city,percentage,college)   
    list_placements.append(k)
    print("your data has been added successfully")
    option=input("do you want to add nore data [Yes|NO]")
    if option.lower()=='no':
        break


print("All the placement data") # we 2will be displaying all the plcement data added here
print('#'*40)
for data in list_placements:
    data.Analysis()
    print("^"*30)


    

