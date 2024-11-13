import random
class software_engineer:
    def __init__ (self,name,age,hours_worked_in_week,hourly_pay,duration_no_of_performance_bugs,duration_no_of_non_performance_bugs):
        self.name=name
        self.age=age
        self.hours_worked_in_week=hours_worked_in_week
        self.hourly_pay=hourly_pay
        self.no_of_performance_bugs = 0
        self.no_of_non_performance_bugs = 0
        self.duration_no_of_performance_bugs=duration_no_of_performance_bugs
        self.duration_no_of_non_performance_bugs=duration_no_of_non_performance_bugs
        self.salary =None


    def get_duration_no_of_performance_bugs(self):
        return self.duration_no_of_performance_bugs

    def get_duration_no_of_non_performance_bugs(self):
        return self.duration_no_of_non_performance_bugs

    def  get_p_bugs(self):
        return self.no_of_performance_bugs

    def set_p_bugs(self,value_p):
        self.no_of_performance_bugs=self.calculate_p_bugs(value_p)# because dont have "def calculate.." they just put "self" infront of "calculate..." and it recieved the instanec from "self" in "def set_bugs..." like it would if had "def calculate.." above the calculate function call here.

    def calculate_p_bugs(self,value_p):
        random_number=random.randrange(value_p)
        return random_number

    def get_bugs_non_p(self):
        return self.no_of_non_performance_bugs

    def set_bugs_non_p(self,value_non_p):
        self.no_of_non_performance_bugs=self.calculate_non_p_bugs(value_non_p)

    def calculate_non_p_bugs(self,value_non_p):
        random_number2=random.randrange(value_non_p)
        return random_number2

    def get_salary(self):
        return f"employee salary with bonuses: ${self.salary}"

    def set_salary(self,base_value):
         self.salary=self.calculate_salary(base_value)#salary which is a attribute is now set to whatever instance you used, it will show up if you use "instance.__dict__" with a value if you use this method and use a base value

    def calculate_salary(self,base_value):
        if self.no_of_performance_bugs<10 and self.no_of_non_performance_bugs<10:
            return base_value
        if 10<=self.no_of_performance_bugs<20 and self.no_of_non_performance_bugs<10:
            return base_value+50
        if self.no_of_performance_bugs < 10 and 10<=self.no_of_non_performance_bugs < 20:
            return base_value+50
        if 10<=self.no_of_performance_bugs < 20 and 10<=self.no_of_non_performance_bugs < 20:
            return base_value + 100
        return base_value+200

class bug_duration:
    def __init__(self):
        self.dur_perf_bugs_list= []
        self.dur_non_perf_bugs_list = []


    def duration_perf_bugs(self,employee):
        self.dur_perf_bugs_list.append(employee)

    def calculate_avg_perf_bugs(self):
        count=0
        value=0
        for emp in self.dur_perf_bugs_list:
            count+=1
            value+=emp.get_duration_no_of_performance_bugs()#the "get_duration... this part here is the calling part which will be a value thats why it has the "()" part. this is the
        return value/count#same as "tech with tim oop" where get_age() part which is a number as well


    def duration_non_perf_bugs(self,employee):#Note:would have to pass employee as a parameter, how else would you append the instances s1 to s4 to a list. And in oop you can pass instances as paramteres which you cant do in normal functions
        self.dur_non_perf_bugs_list.append(employee)

    def calculate_avg_non_perf_bugs(self):
        count2=0
        value2=0
        for emp in self.dur_non_perf_bugs_list:
            count2+=1
            value2+=emp.get_duration_no_of_non_performance_bugs()
        return value2/count2

    def perf_bugs_ratio(self):
        x=bd.calculate_avg_perf_bugs()
        y=bd2.calculate_avg_non_perf_bugs()
        z= x+y
        return (x/z)*100


    def non_perf_bugs_ratio(self):
        x=bd.calculate_avg_perf_bugs()
        y=bd2.calculate_avg_non_perf_bugs()
        z= x+y
        return (y/z)*100

    def standard_deviation_of_perf_bugs(self):
        total=0
        count=0
        for emp in self.dur_perf_bugs_list: #remember this list is in one of the instances which is "bd" thats why we have "self"
            count+=1
            total=total+(self.calculate_avg_perf_bugs()-emp.get_duration_no_of_performance_bugs())**2
        return (total/count)**.5




s1=software_engineer("richy",31,35,20,58,211)
s2=software_engineer("tim",38,28,17,112,189)
s3=software_engineer("tony",42,43,22,49,172)
s4=software_engineer("louise",22,36,15,162,310)
s5=software_engineer("john",41,33,28,70,289)

s1.set_p_bugs(49)
s2.set_p_bugs(28)
s3.set_p_bugs(36)
s4.set_p_bugs(35)
s5.set_p_bugs(37)

s1.set_bugs_non_p(20)
s2.set_bugs_non_p(39)
s3.set_bugs_non_p(49)
s4.set_bugs_non_p(20)
s5.set_bugs_non_p(20)

s1.set_salary(4000)
s2.set_salary(4000)
s3.set_salary(4800)
s4.set_salary(3900)
s5.set_salary(3400)
print(s1.__dict__)
print()
print(s1.get_salary())
print(s2.get_salary())
print(s3.get_salary())
print(s4.get_salary())
print(s5.get_salary())
print()
bd=bug_duration()
bd.duration_perf_bugs(s1)
bd.duration_perf_bugs(s2)
bd.duration_perf_bugs(s3)
bd.duration_perf_bugs(s4)
bd.duration_perf_bugs(s5)
print()
bd2=bug_duration()
bd2.duration_non_perf_bugs(s1)
bd2.duration_non_perf_bugs(s2)
bd2.duration_non_perf_bugs(s3)
bd2.duration_non_perf_bugs(s4)
bd2.duration_non_perf_bugs(s5)
print()
print(bd.calculate_avg_perf_bugs())
print(bd2.calculate_avg_non_perf_bugs())

print()
print(bd.perf_bugs_ratio())
print(bd2.non_perf_bugs_ratio())


print()
print(bd.standard_deviation_of_perf_bugs())
