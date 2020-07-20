'''
Created on 20 Jul 2020

@author: Alicia

'''

'''
Study Unit 1 Activity 14:
'''
def main():
    print("Calculate your future worth through compound interest:")
    
    
    principal = int(input("Enter the amount of money in dollars: $"))
    apr = float(input("Enter bank annual interest rate as decimal number: "))
    n = int(input("Enter the number of years: "))
    
    for i in range(n):
        principal = principal * (1 + apr)
        
    print("The compounded interest for" , n , "years is $" , principal)
        
main()
    
    