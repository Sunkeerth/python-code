# USER DEFINED FUNCTION

import mymodule
mymodule.add(12,13)
mymodule.sub(13,14)
mymodule.mul(22,23)
#Instead of calling a module by its name every single time we want to 
#use a function from that module, we can rename it and this is called 
#as aliasing. This can be done by using keyword called as as.

import mymodule as mm
mm.add(1,13)
mm.sub(1,14)
mm.mul(2,23)

# by using the * we will impote the all functions in the file or module

from mymodule import *
add(1,2)
sub(2,3)
mul(4,5)


#If the module contains huge number of functions and we want to use 
#only a couple of functions from it then instead of using * and 
#importing all functions we can just mentions the function which we 
#want to use and import them selectively as shown below


from mymodule import add,sub,mul
add(2,3)
sub(3,4)
mul(5,6)

# BUILT IN FUNCTION

"""import mymodule
help(mymodule)
mymodule.add(1,2)
mymodule.sub(1,2)
mymodule.mul(1,2)"""

#__doc__(double underscore doc double underscore)/dunder doc

#print(mymodule.add,__doc__)


# 

import mymodule

def fun_eve_od(a,b):
    c=a*b
    print(c," fun")
if __name__=='__main__':
    fun_eve_od(10,8)
    
    
    





