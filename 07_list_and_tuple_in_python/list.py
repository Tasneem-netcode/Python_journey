l = ["python" , "java" , 3 , 0.78, "WLGYT" , "code"]
        # 0         1      2     3      4         5
print(l[0])
print(l[1])
print(l[3])
print(l[4])
print(len(l))

l[2] = True #unlike strings , list are mutable i.e can be changed
print(l[2])

#empty list
lst = list()
empty_list = []
print(len(empty_list))

countries =['finland' , 'ireland' , 'saudi' , 'switzerland']
skills = ['HTML' , 'css' , 'c++', 'python' , 'git' ]

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
fruits =[ "avocado" , 'berry' ,'banana' , 'kiwi' , 'WM' , 'orangess']

first_fruit = fruits[0]
print(first_fruit)

last_index =len(fruits) - 1
last_fruit = fruits[last_index] 
print(last_fruit)

#check items in list
skills = ['HTML' , 'css' , 'c++', 'python' , 'git' ]
does_exist = 'git' in skills
print(does_exist) #true
does_exist = 'java' in skills
print(does_exist) #false

#list functions :
# 1. len(list)
print(len(skills))

# 2.list.append()
skills.append('sql')
print(skills)

# 3.list.insert(index , ele)
skills.insert(2 , 'c')
print(skills)

# 4. list.extend(iterable)
skills.extend(['java' , 'github'])
print(skills)

# 5. list.remove(x)
skills.remove('java' )
print(skills)

# 6.pop()
last_item = skills.pop()
print(last_item)
print(skills)

# 7.index(x)
print(skills.index('git'))

# 8.count(x)
print(skills.count('python'))
nums = [10 ,20 ,30 ,10 ,50 ,10 ]
print(nums.count(10))

# 9 . Sort()
nums.sort()
print(nums)



nums.sort(reverse=True)
print(nums)

# 10. reverse()
nums.reverse()
print(nums)
skills.reverse()
print(skills)

# 11.copy()
newskills= skills.copy()
print(newskills)

# 12. clear()
newskills.clear()


#joining list :
positive =[1 ,2,3,4,5]
zero =[ 0]
negative = [-1 ,-2, -3, -4, -5]
int = positive + zero +negative
print(int)

positive.extend(negative)
print(positive)




