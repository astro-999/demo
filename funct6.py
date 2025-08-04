try:
    def add(*args):
        print(args)
        #args = args[0]
        print(args)
        sum = 0
        for i in args :
            sum= sum + i
        return sum
    '''num = int(input('Enter the numbers to be summed '))
    g =[]
    for i in range(1, num+1):
        i = int(input(f'Enter the {i} number '))
        g.append(i)
    total =  add(g)
    print(total)'''
    total1 = add(2,3,4,4,6)
    print(total1)

except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)