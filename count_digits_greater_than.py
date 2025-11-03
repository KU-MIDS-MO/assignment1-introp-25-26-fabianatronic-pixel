def count_digits_greater_than(n,t):
    if n<0 or  type(t)!=int or not (0<=t <=9):
        return -1
    
    count=0
    while n>0:
        digit=n%10
        if digit>t:
           count += 1
        n//=10
    return count
   