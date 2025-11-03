def sum_of_cubes_even(n):
    if n>2000:
        print("warning")
    if n<0 or type(n) != int:
        return -1
    return float(sum(i**3 for i in range(0,n+1,2)))



    
    #%%
 #   2) sum_of_cubes_even(n)
  #     - Return the sum of cubes of all even numbers from 0 up to and including n, as a float
   #    - Return -1 if n is negative or not an integer
    #   - If n > 2000, print a warning but still compute
