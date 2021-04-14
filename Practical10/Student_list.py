#Student list
#Creat a new class
class student():
    def __init__(self):      #creat a function to set init data
        self.first_name= None
        self.last_name = None
        self.undergraduate_programme= None
    def firstname(self,firstname):  #creat a function to set firstname
        self.first_name = firstname
    def lastname(self,lastname):     #creat a function to set lastname
        self.last_name = lastname
    def undergraduate_programe(self,programme):     #creat a function to set undergraduate programe
        list=['BMI','BMS']
        if programme in list:
            self.undergraduate_programme=programme
    def print(self):     #creat a function to output data
        a = "The student's name is "
        b = self.first_name
        c =' '
        d = self.last_name
        e = ", his/her undergraduate programme is "
        f = self.undergraduate_programme
        g = '.'
        result=a+b+c+d+e+f+g

        return result


#set a example to run this programme
student1 =student()
student1.firstname('Andy')
student1.lastname('Bob')
student1.undergraduate_programe('BMI')
print(student1.print())






