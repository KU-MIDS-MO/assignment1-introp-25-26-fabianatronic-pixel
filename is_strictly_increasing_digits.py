def is_strictly_increasing_digits(n):
       if n<0  or type(n)!=int:
           return -1
       if n<10:
           return True
       
       prev=10
       while n>0:
           digit=n%10
           n//=10
           if digit >=prev:
               return False
           prev=digit
       return True
