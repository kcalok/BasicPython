class Person(object):
    def __init__(self,name,profession):
        self.name = name
        self.profession = profession

_profession = {}




people = [Person("Nick", "Programmer"), Person("Alice","Engineer"),Person("Alok","Software")]



for p in people:
    _profession[p.name] = p.profession


_profession["Gaurav"] = "Software tester"



name = ["maiku","Natan","Abhay","Shailender"]
prof = ["Performance Eng","Technical Analyst","B.A","C++ coding"]

for i in range(len(name)):
    _profession[name[i]] = prof[i]

print(_profession)


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {}

for d in (dic1,dic2,dic3):
    dic4.update(d)

for d_keys,d_values in dic4.items():
    print(d_keys , "=>" , d_values)

def is_key_exists(keyval):
    if keyval in _profession.values():
        print("Key already exists: " +keyval )
    else:
        print("Key does not exists "+ keyval)

is_key_exists("B.A")




def genrate_dic(number):
    dec5 ={}
    for i in range(1, number+1):
        dec5[i] = i*i
    return dec5

def genrate_dic2(number):
    dec5 ={}
    for i in range(number+2, number+9):
        dec5[i] = i*i
    return dec5

dic = genrate_dic(5)
print("<<<dic>>>")
print(dic)
dic2 = genrate_dic2(10)
print("<<<dic2>>>")
print(dic2)
newdic = dic.copy()
print("<<<new dic without merge >>>")
print(newdic)
newdic.update(dic2)
print("<<<merged dic>>>")
print(newdic)

for k,val in newdic.items():
    if (18 in newdic):
        del newdic[18]
    print("The Key is :" , k ,"and" , "value is : " , val)


result = 1
for k in newdic:
    result = 1 * newdic[k]

print( result,"is the product")
print( sum(newdic.keys()), "is the sum ")

