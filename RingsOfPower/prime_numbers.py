
def prime_numbers_calculator(n):

    """
    This function calculates all prime numbers up to and including a given number n.
    """
    prime_numbers=[]

    for i in range(2,n+1):

        isprime=True
        number=2

        while isprime and number<i:

            if i%number==0:

                isprime=False
            
            number+=1

        if isprime:

            prime_numbers.append(i)
    
    
    return prime_numbers    