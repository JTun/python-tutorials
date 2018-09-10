
def myfunction(arg1, arg2,arg3):
    print "My Very first python function with Arguments"
    print "{},{},{}".format(arg1, arg2, arg3)
    sum = arg1 + arg2 + arg3

    #return sum

    if arg3 == "chicago":
        second_func(arg1,arg2)
    else:
        second_func(arg1,arg2,arg3)


# Polymorphism in Funtion names
def second_func(arg1,arg2,arg3=None):
    print("Testing optional argument")
    print (arg1,arg2,arg3)

    print third_func(arg1)

def third_func(arg1):
    return "My arg is: " + arg1


if __name__ == "__main__":
   # myfunction(1,2,3)
    myreturn = myfunction(1,2,3)      
    print my_return
