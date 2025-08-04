try:
    def least(a):
        less = a[0]  
        # print(less)
        for i in a:
            if i<less :
                less = i 
        #print(less)
        return less
    l1 = [ 4, 7, 8, 10, 14, 9, 2]
    small =least(l1)
    print(f'the smallest no :{small}')
except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)
