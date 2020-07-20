'''
Created on 20 Jul 2020

@author: Alicia

'''

# def main():
#     print("This program illustrates a chaotic function")
#     x = float(input("Enter a number between 0 and 1: "))
#     for i in range(10):
#         x = 3.9 * x * (1-x)
#         print(x)
#         
# main()

'''
Study Unit 1 Activity 10: Modify chaos.py so that the user can input the number of times for the loop to be repeated. 
The number of times the loop is repeated determines the number of times a new value is computer for x when then gets printed.
'''
def main():
    print("This program illustrates a chaotic function")
    
    r = int(input("Enter the number of times for the loop to be repeated: "))
    x = float(input("Enter a number between 0 and 1: "))
     
    for i in range(r):
        x = 3.9 * x * (1-x)
        print(x)

