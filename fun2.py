from oper1 import opert 
try:
    num1 = int(input('Enter the first number : '))
    num2  = int(input('Enter the second number : '))
    oper = input('Enter the opertaion : ')
    result = opert(num1,num2,oper)
    print(f'(The result is :{result})')
except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)