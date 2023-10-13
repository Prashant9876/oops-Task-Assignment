#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1+2


# In[2]:


type(a)


# In[3]:


0 and 0


# In[4]:


e = 3+4j


# In[5]:


e.real


# In[6]:


e.imag


# In[7]:


a= 10
if a <=10:
    print ("yes no is equal to or greater than a ")


# In[8]:


n=5
i=1
while i<5:
    print(i)
    i+=1
    if i==3:
        break
        ## in while Else is not executed when we use break function because while can complete its loop`
else:
    print("this is default")


# In[9]:


S="Prashant"
for i in S:
    print(i)


# In[10]:


l = [1,2,3,4,5,"Ravan",(3+4j),34.5]
for i in l:
    print(type(i))
else:
    print("Devil is done ")


# ## In for and  while loop "Else" is not executed when we use break function because while can complete its loop
# 

# In[11]:


range(10)


# In[12]:


list(range(10))


# Slicing in string
#   
# x[a:b:c] is slicing 
# but x[a] is indexing when we pass only one value
# here ; a is lower bound
# b is upper bound (b's is excluded)
# c is the jump(if we put 2 the it will print 0 index and then print valoue of 2nd index and continue till end .by default it is one it can't be zero)
# 

# In[13]:


s = "Prashant"
#when we put only last value i.e -1 it will automatically start reverse indexing
s[::-1]


# In[14]:


s[::2]


# In[15]:


s[7:2:-1]


# In[16]:


s[6:2:-1]


# In[17]:


s[2:7:-1]


# In[18]:


s[-2:-8:-1]


# In[19]:


s[-2::-1]


# In[20]:


s[-90:-1]


# In[21]:


s[:-90:]


# In[22]:


s[:-90:-1]


# In[23]:


c = 200
d = str(c)
d[1]
# if we have to performing slicing into int then we have to typcast its value to string


# In[24]:


s1 = "Devil is here"
len(s1)


# In[25]:


#  s.find() = Return the lowest index in value  where substring sub is found
s1.find("s")


# In[26]:


s1.find("e")


# In[27]:


s1.find("is")


# In[28]:


#Return the number of non-overlapping occurrences of substring sub in string
s1.count("s")


# In[29]:


s1.count("z")


# In[30]:


s2= s1.upper()


# In[31]:


s2.lower()


# In[32]:


s2.title()


# In[33]:


s1.capitalize()


# In[34]:


s+"1"


# In[35]:


s*3


# In[ ]:





# # List, Tuple, set

# In[2]:


#List
l =[1,2,3,4,3+2j,"ed",2.34,True]


# In[37]:


type(l)


# In[38]:


l[::2]


# In[39]:


l[1]


# In[40]:


l[90]


# In[ ]:


l[:3]


# In[ ]:


l[-1]


# In[ ]:


l1 = l[::-1]


# In[ ]:


l[::2]


# In[ ]:


len(l[::2])


# In[ ]:


l+l1


# In[ ]:


l


# In[ ]:


#if we have to get e from  string ed 
l[5][0]


# In[7]:


l2 = [5,6,7]


# In[ ]:


l2*3


# In[ ]:


len(l)


# In[ ]:


l


# In[ ]:


l.append(5)


# In[43]:


l.append(l2)


# In[3]:


l


# In[4]:


l.extend(5)


# In[5]:


l.extend("sudh")


# In[6]:


l


# In[11]:


l.extend([9,8,7])


# In[12]:


l


# In[14]:


l.insert(1,"Prashant")


# In[15]:


l


# In[17]:


l.insert(3,[1,2,3,4,5])


# In[18]:


l


# In[19]:


l.insert(-1,45)


# In[20]:


l


# In[22]:


l.pop()


# In[23]:


l


# In[24]:


l.pop(2)


# In[25]:


l


# In[30]:


l.remove(5)


# In[31]:


l


# In[34]:


l[2].remove(4)


# In[35]:


l


# In[41]:


l.sort()


# In[1]:


import numpy as np
import pandas as pd
l3 = [7,4,6,3,7,2,8,4,6,6]


# In[2]:


l3.sort()


# In[3]:


A = "Prashant"


# In[5]:


# we can replace the char of string temporarly
A.replace("a","d")


# In[6]:


A


# # tuple
# 

# In[7]:


t = (2,3,4,5,"sudh",True,24.3,True)


# In[9]:


t.count(2)


# In[11]:


t.index(5)


# # set
# 

# In[12]:


s2 = {234,235,756,"ssv",True,23.521}


# In[13]:


# we can't put a list into set .we can only put primitive data into it
s3  = {534,3,356,44.4.[4,"wc",43],90}


# In[14]:


#it will remove the duplicate element 
s4 = {2,3,23,4,2,3,23,"sac","sac","Sac"}


# In[15]:


s4


# # Dictionary

# In[1]:


d ={}



# In[2]:


type(d)


# In[3]:


d1 = {"key":"sunh" }


# In[4]:


d1


# In[5]:


d2 = {"name": "Prashant","email":"prashant74887","phone":"8349333"}


# In[6]:


d2


# In[7]:


d3={2313:"dkfm"}


# In[8]:


d3


# In[9]:


d4 = {@ :"QDC"}


# In[11]:


d2["name"]


# In[12]:


d6={"Company":"pwskills","Course":["web dev","data science","java with system design"]}


# In[13]:


d6


# In[15]:


d6["Course"][1]


# In[18]:


d7 = {"number":[1,2,3,4,543],"assignment":(1,2,3,4,5),"launchdate":{12,4,4,25,6},"class_time":{"web dev":8,"java":9}}


# In[19]:


d7


# In[20]:


d7["class_time"]["java"]


# In[21]:


d7["mentor" ]= ["krish","sudhanshu","hayder"] 


# In[22]:


d7


# In[24]:


del d7["number"]


# In[25]:


d7


# In[28]:


list(d7.keys())


# In[30]:


list(d7.items())


# In[32]:


d7.pop("assignment")


# In[33]:


d7


# # Conditional statement
# 

# In[44]:


Marks = int(input())
print("marks: ", Marks)
if Marks >100:
    print("Enter valid Marks")
elif Marks >=80:
    print("you will be a part A0 batch")
elif 60<=Marks<80:
    print("you will be a part of a1 batch")
elif  40<=Marks<60:
    print("you will be a part of a2 batch")
else:
    print("you will be a part of A3 batch")


# In[49]:


price= int(input())
if price> 1000:
    print("i will not purchase")
    if price>5000:
        print("it is too much")
    elif price <2000:
        print("it's ok")
else:
    print("i will purchase")


# # loop
# 

# In[59]:


l1=[]
l=[1,2,3,4,5,6,7,8]
for i in l:
     print(i+1)
     l1.append(i+1)
    
    


# In[60]:


l1



# In[63]:


l2=[]
l = ["sudh","kumar","pwskills","course"]
for i in l:
    print(i)
    l2.append(i.upper())
l2


# In[69]:


l5=[]
l6=[]

l4 = [1,2,3,4,"subh","kumar",324,34.456,"abc"]
for i in l4:
    print(i)
    if type(i) == int or type(i) == float:
        l5.append(i)
    else:
        l6.append(i)

l5


# In[67]:


l6


# # Function

# In[4]:


def text():
    print("This is my very very first function")


# In[5]:


text()


# In[6]:


text() + "cmcm"


# In[7]:


def test2():
       return "this is my 2nd function"


# In[9]:


test2() +"cmlmvl"


# In[11]:


def test3():
    return "sudh" , 133, True, [1,2,3,4,5]


# In[12]:


test3()


# In[15]:


a,b,c,d = test3()


# In[16]:


a,b,c,d


# In[17]:


def test4():
    a= 5+6/7
    return a


# In[18]:


test4()


# In[19]:


def test5(a,b,c):
    d= a +b/c
    return d


# In[21]:


test5(2,3,5)


# In[23]:


def test6(a,b):
    return a+b


# In[25]:


test6(3,5)


# In[27]:


test6("sfnn","jwofjof")


# In[28]:


test6([1,2,3,4], [9,8,7,6,5])


# In[19]:


l = [1,2,3,4,"sudg", "kumar", [1,2,3,4,5,6]]
def test7(l):
    l1 = []
    for i in l:
        if type(i)== int or type(i)==float:
            l1.append(i)
    return l1


# In[20]:


test7(l)


# In[21]:


l


# In[22]:


l3=[]
def test8(a):
    """This is my function to extract num data from list""" 
    for i in a:
        if type(a)== list:
            for j in i:
                l3.append(j)
        else:
            if type(i)== int or type (i)== float:
                l3.append(i)
    return l3


# In[23]:


test8(l)


# In[24]:


def test9(a,b):
    return a+b


# In[25]:


def test10(*args):
    return args


# In[26]:


type(test10())


# In[27]:


test10(1,2,3,4,5,"wei", True, 33.4)


# In[29]:


def test11(*args,a):
    return args,a


# In[30]:


test11(1,2,3,4,a = "wkh")


# In[41]:


def test13(c,d,a=12, b=39):
    return a,b,c,d


# In[42]:


test13(22,54)


# In[36]:


def test14(**kwargs):
    return kwargs


# In[38]:


test14()


# In[39]:


test14(a = [1,2,3,4,5], b= "sudh", c = 21.44)


# # Generater function
# 

# In[1]:


def fibo(n):
    a,b = 0,1
    for i in  range(n):
        yield a
        a,b = b,a+b


# In[2]:


fibo(10)


# In[3]:


for i in fibo(10):
       print(i)


# In[17]:


def fibo1():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b


# In[18]:


fibz = fibo1()


# In[19]:


for i in range(10):
    print(next(fibz))


# In[23]:


s = "sudh"


# In[24]:


for i in s:
    print(i)


# In[25]:


s1 = iter(s) # next function doesnt work with string we have to use iter() function for this

type(s1)
# In[72]:


next(s1)


# In[74]:


next(s1)


# In[75]:


next(s1)


# In[77]:


next(s1)


# In[28]:


next(s1)


# In[30]:


iter(s1)


# In[84]:


def count(n):
    count = 1
    while count < n:
        yield count
        count = count+1


# In[85]:


c = count(5)


# In[86]:


for i in c:
    print(i)


# In[87]:


type(c)


# # Lambda Function
# 

# In[88]:


def test111(n,p):
    return n**p


# In[89]:


test111(3,2)


# In[92]:


a = lambda n,p: n**p


# In[93]:


a(3,2)


# In[94]:


add = lambda x,y: x+y


# In[96]:


add(3,5)


# In[97]:


c_to_f = lambda c: (9/5)*c +32


# In[98]:


c_to_f(45)


# In[100]:


find_max = lambda x,y: x if x>y else y


# In[102]:


find_max(10,34)


# In[103]:


s = "pwskills"
find_len = lambda s :len(s)


# In[104]:


find_len(s)


# # Map,reduced and filter
# 

# In[105]:


l = [1,2,3,4,5]


# In[106]:


def test(l):
    l1 = []
    for i in l:
        l1.append(i**2)
    return l1


# In[107]:


test(l)


# In[ ]:


#map   map(func,*iterables )


# In[109]:


def sq(x):
    return x**2


# In[110]:


list(map(sq,l))


# In[112]:


list(map(lambda x:x**2, [9,8,7,6]))


# In[114]:


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
list(map(lambda x,y: x+y,l1,l2))


# In[115]:


def add(x,y):
    return x+y


# In[116]:


list(map(add,l1,l2))


# In[118]:


s = "pwskillist"
list(map(lambda s : s.upper(), s))


# In[34]:


from functools import reduce ## in reduce function we have to pass only two agrument only in function


# In[35]:


l = [1,2,3,4,5,6]


# In[36]:


reduce(lambda x,y :x+y,l)


# In[124]:


reduce(lambda x,y:x+y,l)


# In[126]:


reduce(lambda x,y :x+y,[1])


# In[128]:


reduce(lambda x,y : x*y,l)


# In[130]:


list(filter(lambda x: x %2 ==0, l))


# In[ ]:


list(filter(lambda x: x %2 !=0, l))


# In[132]:


l1 = [-3,4,5,6,-1,-5]


# In[135]:


list(filter(lambda x: x<0,l1))


# In[137]:


l2 = ['sudh', "pwskills","kimarsim", "bihat","hajipur"]


# In[142]:


list(filter(lambda x: len(x)<6,l2))


# OOPS concept in python
# 

# In[38]:


a = 1 
print(type (a))


# In[39]:


class test:
    pass


# In[40]:


a= test()


# In[41]:


type(a)


# In[42]:


print(type (a))


# In[1]:


class pwskills:
    def welcome_msg(self):
        print("welcome to pw skills")


# In[2]:


piyush = pwskills()


# In[3]:


print(type(piyush))


# In[4]:


piyush.welcome_msg()


# In[5]:


ami = pwskills()


# In[6]:


ami.welcome_msg()


# In[38]:


class pwskills1 :
    def __init__(self ,phone_no, email_id, student_id):
        self.phone_no = phone_no
        self.email_id = email_id
        self.student_id = student_id
    def return_student_detail(self):
        return self.phone_no,self.email_id, self.student_id


# In[39]:


rohan = pwskills1(8340291901,"prashantkumar74887@gmail.com",2101331550060)


# In[40]:


rohan.return_student_detail()


# In[43]:


rohan.phone_no


# In[44]:


rohan.email_id


# In[49]:


class pwskills2 :
    def __init__(self ,phone_no, email_id, student_id):
        self.phone_no1 = phone_no
        self.email_id1 = email_id
        self.student_id1 = student_id
    def return_student_detail(self):
        return self.phone_no1,self.email_id1, self.student_id1


# In[50]:


sudh = pwskills2(12131213,"ansxkcdwk",1213)


# In[51]:


sudh.return_student_detail()


# In[54]:


sudh.phone_no


# In[55]:


sudh.phone_no1


# In[59]:


class pwskills2 :
    def __init__(sudh ,phone_no, email_id, student_id):
        sudh.phone_no1 = phone_no
        sudh.email_id1 = email_id
        sudh.student_id1 = student_id
    def return_student_detail(self):
        return sudh.phone_no1,sudh.email_id1, sudh.student_id1


# In[60]:


rohan = pwskills2(13344,"1421",131434)


# In[62]:


rohan.phone_no1


# Polymorphism
# 

# In[63]:


def test(a,b):
    return a+b


# In[65]:


test("sudh"," kumar")


# In[66]:


test([1,2,44,4],[123,44,32,])


# In[12]:


class data_science:
    def syllabus(self):
        print("this is my sllybus for data science batch")


# In[13]:


class web_dev:
    def syllabus(self):
        print("this is my web dev")


# In[14]:


def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()


# In[16]:


data_science = data_science()


# In[17]:


web_dev = web_dev()


# In[18]:


class_obj = [data_science,web_dev]


# In[19]:


class_parcer(class_obj)


# Encapsulation

# In[1]:


class car():
    def __init__(self , year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0
        
        ## we have to write "__" for Encapsualation in python withon this we cant call this function
        
    def set_speed(self,speed):
        self.__speed = 0 if speed<0 else speed
    def get_speed(self):
        return self.__speed


# In[2]:


c = car(2022,"toyata","innova",220)


# In[3]:


c._car__year


# In[5]:


c.set_speed(-333)


# In[7]:


c.get_speed()


# In[ ]:


c


# In[93]:


class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    def withdraw(self, amount):
        if self.__balance >= amount &  amount < 20000:
            self.__balance = self.__balance - amount
        elif amount > 20000:
            print(" Limit Excced")
            
        else:
          return False
    def get_balance(self):
        return self.__balance
    


# In[94]:


piyush = bank_account(1000000)


# In[95]:


piyush.get_balance()


# In[96]:


piyush.deposit(20070)


# In[97]:


piyush.get_balance()


# In[99]:


piyush.withdraw(145)


# In[100]:


piyush.get_balance()


# In[101]:


piyush.withdraw(1000000000)


# Inheristance

# In[106]:


class test:
    def test_meth(self):
        return "this is my first class"


# In[107]:


class child_test(test):
    pass


# In[108]:


child_test_obj = child_test()


# In[109]:


child_test_obj.test_meth()


# In[147]:


class class1:
    def test_classes(self):
        return "this is method of first class"


# In[148]:


class class2(class1):
    def test_classes2(self):
        return "this is method of second class"


# In[149]:


class class3(class2):
    def test_classes3(self):
        return "this is method of  third class"


# In[150]:


class_obj.test_classes2()


# In[151]:


class3 = class3()


# In[153]:


class3.test_classes()


# In[154]:


class3.test_classes2()


# In[155]:


class3.test_classes3()


# In[156]:


class class5:
    def test1(self):
        return "this is my fie=rst class"


# In[157]:


class class6:
    def test2(self):
        return "this is my second class"


# In[158]:


class class7(class5 , class6):
    pass


# In[159]:


class_obj = class7()


# In[161]:


class_obj.test1()


# In[162]:


class_obj.test2()


# abstract = use for making skeleton /blueprint of any code
# 

# In[2]:


import abc
class pwskills:
    @abc.abstractmethod
    def students_details(self):
        pass
    @abc.abstractmethod
    def students_assignment(self):
        pass
    @abc.abstractmethod
    def students_marks(self):
        pass
    


# In[3]:


class student_detail(pwskills):
    def students_details(self):
        return "this is a method for taking students details"
    def students_assignment(self):
        return "assignment detail for each student "
    


# In[4]:


class data_science_master(pwskills):
    def students_details(self):
        return "this will return a student details for data sciencwe masters"
    def students_assignment(self):
        return "this will give you a sudent assignment details for data science masters"


# In[5]:


dsm = data_science_master()


# In[6]:


dsm.students_details()


# In[7]:


dsm.students_assignment()


# In[9]:


stu_detail = student_detail()


# In[11]:


stu_detail.students_details()


# In[25]:


#Ques 5
# method Overriding :- Method overriding, in simple words, is when a child class provides its own version of a method that is already defined in its parent class. This allows the child class to change or extend the behavior of the method while keeping the same method name.

class shape:
    def earea(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius*self.radius
    
class rect(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth


# In[26]:


cir= circle(5)


# In[27]:


rec = rect(4,5)


# In[28]:


print(f"area of circle is", cir.area())


# In[29]:


print(f"area of rectangle is ",rec.area())


# In[ ]:




