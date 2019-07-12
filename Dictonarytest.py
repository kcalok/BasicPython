from collections import  Counter


def genrate_dictonary(num):
    mydic ={}
    for i in range(1,num+1):
        mydic[i] = i*i
    return mydic

dic1 = genrate_dictonary(10)

print(dic1)


def remove_dic_key(dic1, num):
    if num in dic1:
        del dic1[num]
    return dic1



dic1 = remove_dic_key(dic1,9)
print(dic1)

list1 = ['red', 'green', 'blue']
list2 = ['#FF0000','#008000', '#0000FF']
ar = {1,2,3}
ar2 = {'one','two','three'}

col_dict = dict(zip(list1,list2))
num_dict = dict(zip(ar,ar2))
print(col_dict)
print(num_dict)

for k in sorted(col_dict):
    print("The key is %s , The value is %s" % (k,col_dict[k]))
    #print("The key is {} and value is {}" .format(k,col_dict[k]))

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],

    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}


result = {}

if not bool(result):
    print("aaaa")
else:
    print ("bbb")



for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print (result )



d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result = {}
result = Counter(d1) + Counter(d2)

print(result)



