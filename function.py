''' def fun1(num1, num2):
        print(num1,num2)

    num1 = 20
    num2 = 10
    fun1(num1, num2 )'''
try:
   def fun2( name):
       print(name.upper())
       
   name = input('enter your name :')
   fun2(name)
   
except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)