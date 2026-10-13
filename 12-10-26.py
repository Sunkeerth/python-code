#  Loggers for info for storing in the log file of pgm execution.

# def sum_eve(lst):
#     sum_cal=0
#     for i in lst:
#         if i%2==0:
#             sum_cal+=i
#     return sum_cal

# def main():
#     inp=map(int ,input("enter the list numerical values for me .").split())
#     res=sum_eve(inp)
#     print(res)

# main()


import logging
# def sum_eve(lst):
#     print("sum_even function started ")
#     sum_cal=0
#     for i in lst:
#         if i%2==0:
#             sum_cal+=i
#     print("it will return an value .")
#     return sum_cal

# def main():
#     print("main function started : ")
#     print("user need enter the input : ")
#     inp=map(int ,input("enter the list numerical values for me .").split())
    
#     res=sum_eve(inp)
#     print(res)

# main()

# from pathlib import Path
# log_dir=Path(__file__).parent/'logs'
# log_dir.mkdir(exist_ok=True)

# logging.basicConfig(filename=log_dir/'app.log',level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s',encoding='utf-8',force=True)


# def sum_eve(lst):
#     logging.info("sum_eve started execution .")
#     sum_cal=0
#     for i in lst:
#         if i%2==0:
#             sum_cal+=i
#     logging.info("sum_eve completed execution .")
#     return sum_cal

# def main1():
#     logging.info("main started exec : ")
#     inp=map(int ,input("enter the list numerical values for me .").split())
#     res=sum_eve(inp)
#     print(res)
#     logging.info("main completed exec : ")

# # main()


        
"""
ways of logging. 
1. debug
2. info
3.warning
4.error
5.critical

"""


class logg:
    def add1(self,a,b):
        return a+b
    def sub2(self,a,b):
        return a-b
    def mul1(self,a,b):
        return a*b
#  waring related logging info in the log file 
    def warn(self,a,b):
        out=0
        if b==0:
            print('invalid the denimoter number : ')
            # logging.basicConfig(filename='app.log',level=logging.warning)
        else :
            out=a/b
        return out
    def ExecptionalErrorHandling(self):
        try:
            num=int(input("enter the numeritator : "))
            dem=int(input("enter the denominator : "))
            res=num/dem
            print(f'result of num by den is : {res}')
        except :
            logging.error(f" user entered the wrong denominator  :num : {num } dem : {dem }",exc_info=True)
            
            
            
def main():
        logging.basicConfig(filename='app.log',level=logging.DEBUG)
        logging.basicConfig(filename='app.log',level=logging.warning)
        logging.basicConfig(filename='app.log',level=logging.error)
        a=int(input("enter the a number :"))
        b=int(input("enter the b value : "))
        logging.debug(f'a=>{a}')
        logging.debug(f'b=>{b}')
        if b==0:
            logging.warning(f'the denimoter of b must non zero : => {b}')
        obj=logg()
        res1=obj.add1(a,b)
        print(res1)
        logging.debug(f'result 1 add   is => {res1}')
        res2=obj.mul1(a,b)
        print(res2)
        logging.debug(f'result 2 mul1 is => {res2}')
        res3=obj.sub2(a,b)
        print(res3)
        logging.debug(f'result 3 sub  is => {res3}')
        res4=obj.warn(a,b)
        print(res4)
        res5=obj.ExecptionalErrorHandling()
main()
        
        
        
        
        