try:
    def checck(a):
        odd = []
        even = []
        for i in a :
            if i%2==0 :
                even.append(i)
            else:
                odd.append(i)
        return even,odd
    l1 =[ 1, 3, 5, 4, 6, 36 ]
    result = checck(l1)
    print(result)
except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)
