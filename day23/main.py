from math import factorial

def pascal_triangle(n):
   for i in range(n):
       # run 'j' from 0 to 'n-i' (inclusive) to add leading spaces 
       # before each row to create a right-aligned triangle.
       for j in range(n-i+1):
           print(end=' ')

       for j in range(i+1):
           
           # The binomial coefficient C(i, j) is calculated 
           # using the formula: C(i, j) = i! / (j! * (i-j)!).
           print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')

       print()

# print the Pascal's Triangle with 5 rows.
if __name__ == '__main__':
   pascal_triangle(5)