#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/14/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Function to find all prime numbers in a given range of 0 to n

def main():
    num = int(input("Enter the inclusive limit of the range of numbers to find primes: "))
    count_primes(num)

def count_primes(n):
    
    primes = []
    composites = []
    
    for i in range(n+1):
        
        # 0 is neither prime nor composite
        if i == 0:
            pass
        
        # 1 is composite since it has only one positive factor i.e. itself
        elif i == 1:
            composites.append(i)
        
        # 2 is composite since it has exactly two positive factors i.e. 1 and 2    
        elif i == 2:
            primes.append(i)
            
        elif i > 2 and i < 9 and i % 2 != 0:
            primes.append(i)
            
        else:
            # Even numbers besides 2 are always composite
            if i % 2 == 0:
                composites.append(i)
            
            # Odd numbers need to be checked for further divisibility
            else:
                if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
                    composites.append(i)
                else:
                    primes.append(i)
                
    print("Composites ", composites)            
    print("Primes ", primes)
    
if __name__ == "__main__":
    main()