'''di = {'a':'45','a':54,'a':65,'name':'jagerna'} #last ko value 
print(di)
print(len(di))
di['a']= 61 #changing
print(di)
d1 = {'a1':54,'e1': 58}
d3 ={}
d3 = di.copy()

print(d3)
del di['a']
print(di)
d3.clear()
print(d3)
'''
#n = int(input('enter the item in dictionary'))
'''d1 = { }
for i in range(n):
    key =  input("Enter key : ")
    value = input('enter the item :')
    d1[key]= value
print(d1)'''
'''for i in range(1,n):
    print(i)'''
di = {'a':'45','a':55,'a':{'a':54,'e1': 58},'name':'jagerna'}
d1 = {'a':54,'e1': 58}
'''d3 = {**d1,**di}
print(d3)
print(di|d1) #merge of two dictionary'''

'''n = int(input('enter the number :'))
d5 = {i:i**2 for i in range(1,n+1)} #dictionaries comprehension
print(d5)
for key,value in d5.items():
    print(key,value)'''
d6 = {1: 1, 2: 4, 3: 9, 4: d1}
'''print(d6[4])
print(d6.get(10,'hhhh'))'''
d8 = {1:d6, 'f':d1,'g':di}
print(d8)
