def myfunc(a,b, *args):

    # print(a)
    # print(b)
    # print("---------- C --------------")
    # print(c)
    #
    # print("---------- D --------------")
    # print(d)

    for ar in args:
        if ar == c:
            print(c)

        # elif ar == d:
        #     print(d)
        else:
            print(d)

    print("No args passed")



a="hello"
b="ball"
c="hihg"
d="omg"

#myfunc(a,b,c,d)

myfunc(a,b)