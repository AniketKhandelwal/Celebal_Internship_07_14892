print("Enter the number of rows:")
z = int(input())

for i in range(z, 0, -1):
    print(" " * (z-i) + "*" * i)



"""Output:
Enter the number of rows :
5
 Output:    
        *****
         ****
          ***
           **
            *  """