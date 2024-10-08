# Coding Challenges

#### Hello! In this repository I upload programs and coding challenges that I find useful to improve my Python skills and programming logic.

- **array_leaders:** Given an array, this function prints all the Leaders in the array. An element is a Leader if it is greater than all the elements to its right side. The rightmost element is always a leader.
  
  Example: Input -> [16, 17, 4, 3, 5, 2], Output -> [17, 5, 2]

- **kadanes_algorithm:** Given an array of intergers, this function finds the contigous subarray (containing at least one number) which 
    has the maximum sum and return its sum.

  Example: Input -> [2, 3, -8, 7, -1, 2, 3], Output -> 11

- **text_predictor:** This function returns a maximun of three suggested words (from a given repository) after each character is typed by the costumer in the "search field". If there are more than three aceptable keywords, the functions returns the words that are first in alphabetical order. Furthermore, 
    the function starts suggesting keywords after the costumer has entered at least two characters.

  Example: Input -> repository=[mobile, mouse, mousepad, motor] keyword=motor, Output -> [[mobile, motor, mouse], [motor], [motor], [motor]]

- **prime_numbers_calculator:** This function calculates all prime numbers up to and including a given number n.

  Example: Input -> 18, Output -> [2, 3, 5, 7, 11, 13, 17]

- **rings_of_power:** Given a positive integer representing the rings of power from LOTR, this function distributes all the rings among the races 
    of Middle-Earth. Elves will receive an odd number of rings, dwarfs a prime number, men an even number and Sauron will receive only one ring.
    The function returns the total number of fair distributions, if there are any, and one of those distributions.

  Example: Input -> 17,    Output -> One of 23 fair distributions of the 17 rings of power is: Elves 11 rings, Dwarfs 3 rings, Men 2 rings, Sauron 1 ring.
 
