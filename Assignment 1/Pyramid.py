print("Enter the number of rows:")
z = int(input())

for i in range(1, z + 1):
    print(" " * (z - i) + "*" * (2 * i - 1))



"""Output:
Enter the number of rows :
5
 Output:    
            *
           ***
          *****
         *******
        *********   """