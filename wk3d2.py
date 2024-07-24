#Ripple Patel




def pyramid(text, repeat):
    for i in range(1, repeat + 1):
        print (text * i)

def absolute_difference(num1, num2):
    diff = abs(num1 - num2 )
    #return diff
    print (diff)

def main():
     print ("difference 5 10", absolute_difference(5,10) == 6)
    # print("difference 10 5", absolute_difference(10, 15) == 5)
    # print("difference 200 -200", absolute_difference(200, -200) == 400)

     absolute_difference(5, 10)
     absolute_difference(10, 15)
     absolute_difference(200, -200)

     print ()
     pyramid("*", 2)
     pyramid("+", 5)
     pyramid("X", 10)

main()

