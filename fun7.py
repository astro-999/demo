def add(*args):
    print(args)
    #args = args[0]
    print(args)
    sum = 0
    multi = 1
    for i in args :
        sum= sum + i
        multi = multi*i
    return sum,multi

