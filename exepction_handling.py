"""class handling_error:
    def __init__(self,a,b):"""
a=int(input(" enter the value of A "))
b=int(input(" enter the value of B "))

def operation1(a,b):
    try:
        c = a / b
        print(" result is {}".format(c))
    except ZeroDivisionError:
        print(" you can not divide any no. by 0 ")
    except ValueError:
        print("  .. ")
    except TypeError:
        print("entered values are not in integer format ")
    finally:
        print(" successfully done with operation")


operation1(a,b)