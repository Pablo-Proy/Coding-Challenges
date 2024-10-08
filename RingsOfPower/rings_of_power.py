
from prime_numbers import prime_numbers_calculator
from itertools import product
import random

def rings_of_power(total_rings):

    """
    Given a positive integer representing the rings of power from LOTR, this function distributes all the rings among the races 
    of Middle-Earth. Elves will receive an odd number of rings, dwarfs a prime number, men an even number and Sauron will receive only one ring.

    The function returns the total number of fair distributions, if there are any, and one of those distributions.
    """

    try: 

        if total_rings<0:

            print("Error -- The total number of rings (total_rings) must be a positive integer.")
        
        else:

            elves_rings=[2*n+1 for n in range(total_rings//2)] #Odd numbers up to and including total_rings
            dwarfs_rings=prime_numbers_calculator(total_rings) #Prime numbers up to and including total_rings
            men_rings=[2*n for n in range(total_rings//2+1)] #Even numbers up to and including total_rings
            sauron_rings=[1]

            #All possible distributions of the rings are calculated using cartesian product:
            ring_combinations=product(elves_rings,dwarfs_rings,men_rings,sauron_rings)
            fair_distribution=[]
            cont=0
                
            for ring_distribution in ring_combinations:

                if sum(ring_distribution)==total_rings:

                    fair_distribution.append(ring_distribution)
                    cont+=1

            if len(fair_distribution)!=0:

                aux=random.randint(0,len(fair_distribution)-1)

                print(f"One of {cont} fair distributions of the {total_rings} rings of power is:")
                print(f"\tElfs {fair_distribution[aux][0]} rings.")
                print(f"\tDwarfs {fair_distribution[aux][1]} rings.")
                print(f"\tMen {fair_distribution[aux][2]} rings.")
                print(f"\tSauron {fair_distribution[aux][3]} ring.")

            else:

                print("There is no fair distribution of the rings of power! Unfortunately Gollum keeps all of them.")
    
    except TypeError:

        print("TypeError -- The total number of rings (total_rings) must be a positive integer.")