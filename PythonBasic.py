import sys
import datetime
from math import  pi
import calendar
from datetime import date

def get_system_version():
    sys.version


def get_sys_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_sys_date():
    return datetime.datetime.now().strftime("%d/%m/%Y")

def calc_area_of_circle():
    radius = float(input("Enter the radius of the circle:"))
    area = pi*(radius**2)
    print("The area of the circle  is %f:" %area)

def welcome_user_reverse():
    firstname = input("Enter the first name:\n")
    lastname = input("Enter the last name:\n")
    print("First name entered is %s and last name entered is %s" %(firstname,lastname))
    print("Hello %s %s to python"%(lastname,firstname))

def construct_list_tuple_dict_from_input():
    vals = input("Enter the digits as comma separated values :\n")
    l = vals.split(",")
    t = tuple(l)
    d = dict(zip(l, t))
    print(l)
    print(t)
    print(d)

def display_extention_of_filename():
    filename = input("Enter the file name with extension : \n")
    if filename == "":
        filename = __file__
        ext = filename.split(".")
        print("The extension of the default file is %s:" % ext[-1])
    else:
        ext = filename.split(".")
        print("The extension of the file name enterd is %s:" % ext[-1])

def display_first_last_item_in_list():
    color_list = ["Red", "Green", "White", "Black"]
    print("The First item in the list is %s " % color_list[0])
    print("The Last item in the list is %s " % color_list[-1])


def print_exam_schedule():
        date = get_sys_date()
        d = (10,12,2019)
        print("Examination starts from %s" % date)
        print("Examination ends on %i/%i/%i" % d)



def compute_value():
    i = int(input("Enter the number for computation :\n"))
    result = i*1+i**2+i**3
    n1 = int("%s"%i)
    n2 = int("%s%s" %(i,i))
    n3 = int("%s%s%s" % (i, i,i))
    result2 = n1+n2+n3
    print("The number in n+n*2+n*3 format is : %i" % result)
    print("The number in n+nn+nnn format is : %i" % result2)

'''A docstring is a string literal that occurs as the first statement 
in a module, function, class, or method definition. Such a docstring
becomes the __doc__ special attribute of that object.
All modules should normally have docstrings, and all functions and classes exported by a module 
should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings.'''

def print_info_abt_method(method):
    print(method.__doc__)


'''method to print the calander of the year and month '''

def print_calender_of_month(y,m):
    # y = int(input("Enter the year : \n"))
    # m = int(input("Enter the month : \n "))
    print(calendar.month(y,m,6,2))

def calculate_date_diff():
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    delta = l_date - f_date
    print(delta)

def number_diff():
    num1 = int(input("Enter the number :\n"))
    num2 = int(input("Enter the second number :\n"))

    if num1 >= num2:
        diff = num1 - num2
        print("Double of diff amount is %i"% (diff*2))
    else:
        diff = num1 - num2
        print("The absolute diff amount is %i" % abs(diff))



def string_creation():
    str = input("Enter the string :\n")
    #print(str[0:3])   slice the string
    if len(str) >= 2 and str[0:2] == "Is":
        print(str)
    else:
        print("Is "+ str)


def copy_string_given_number_of_times(str,num):
    print(str*num)


def even_or_odd():
    num = int(input("enter the number : \n"))
    if num % 2 ==0:
        print("The number is even ")
    else:
        print("The number is odd ")


def num_exist_in_list(num):
    val =input("enter the comma seprated values  of the list :\n")
    l = val.split(",")


    count = 0
    for n in l:
        if n == str(num):
            count = count+1

    print("The number is present %i times  "%count)

def copy_of_char(str,num):
    if len(str) > 2:
        print(str[0:2]*num)
    else:
        print(str*num)

#copy_of_char("mi" ,5)


def return_even_char_in_string(str,num):
    for i in range(0,len(str)-1,2):
        print(str[i])

    print(str[num:])


def compare_list_items():
    l = [1,2,3,4,5,9,15,60,20,55,89]
    if l[0] == l[len(l)-1]:
        print("True")
    else:
        print("False")

    for i in l:
        if i%5==0:
            print(i)

def finds_no_of_times_substring_repeated_in_string(substr, str ):
    #str = "Emma is a good developer. Emma is also a writer"
    strl =  str.split(" ")
    count = 0
    for s in strl:
        if s == substr:
            count=count+1
    print("%s is repeated in the given '%s' %i times "%(substr,str, count))


#finds_no_of_times_substring_repeated_in_string("Emma", "Emma is a good developer. Emma is also a writer")


def print_pattern(num):
    for num in range(10):
        for i in range(num):
            print(num, end = " ")
        print("\n")





def create_list_from_lists():
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 =[9,8,5,6,7,4,55,22]
    new = []
    for i in l1:
        if i % 2 ==0:
            new.append(i)
    for i in l2:
        if i % 2 !=0:
            new.append(i)
    print(new)





def getMiddleThreeCharsoddlenghtstring(str):
    l = len(str)
    print(str)
    print(l)
    mid = int(l/2)
    print(mid)
    s = str[mid-1:mid+2]
    print(s)

def appendMiddle(str1 , str2):
    mid = int(len(str1)/2)
    newstr = str1[:mid]+str2+str1[mid:]
    print(newstr)

def mixString(s1,s2):
    mids1 = int(len(s1)/2)
    mids2 = int(len(s2) / 2)
    newstring = s1[0:1]+s2[0:1]+ s1[mids1:mids1+1] +s2[mids2:mids2+1]+s1[-1]+s2[-1]
    print(newstring)


def lowercaseFirst():
    str = input("Enter string in lower and uppercase \n")
    lower =[]
    upper= []
   # li = str.split()
    for i in str:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    newstring = ''.join(lower+upper)

    print(newstring)

def test_distinct_list_methods(data):
    d = data
    d.append(126)
    a=list((set(data)))
    print(a)
    if len(data) == len(set(data)):
        print(True)
    else:
        print(False)
    #fetch data from list in starting from 0 index and skipping 3 index
    print(data[0::3])
    print(max(data))
    print(min(data))
    # counts the number of times object is available in the list
    print("Number of times object is avialable in the list is :", d.count(5))
    #add list items of extended list on the first list
    d.extend(a)
    print("Extected list  :",d)
    #pops\gets  the last elemnet form the list [-1]
    print("pop the item from the list : ",d.pop())
    print("pop the item from the given index in the list : ",d.pop(0))
    #remove items from the list
    d.remove(126)
    print("remove the item from the list:" ,d )
    #reverse the items in the list
    d.reverse()
    print("Reverse the list items : ",d )

    #sort the list items in the given order
    d.sort(reverse=False)
    print("Sorted list is :",d )
    d.sort(reverse=True)
    print("Sorted list is :", d)


#test_distinct_list_methods([1,5,7,9,5,4,6,5,6,5,8,9,5,4,89,22])



def string_basic_methods():
    # concatenate string at the end
    str = "Hello World of"
    newstr = "Python"
    updated_string = str[:len(str)]+" "+newstr
    print("Updated string is :%s" %updated_string)
    print("Slice the string and give value at the index : ",str[0])
    print("Slice the string and give value in the range : ", str[0:6])

string_basic_methods()
