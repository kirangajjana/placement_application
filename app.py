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
        if self.percentage>=90:
            print("Hi,Congrats you have an capability to select in placement drive based on the below provided data by you")
            print(f"Your gud name is: {self.name}")
            print(f"your branch : {self.branch}")    
