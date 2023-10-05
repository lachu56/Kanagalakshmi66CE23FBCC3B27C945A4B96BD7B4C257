def fact_rec(n):
 if n==0 or n==1:
  return 1
 else:
  return n*fact_.rec(n-1)
number=int(input("Enter value:"))
res=fact_rec(number)
print("The factorial of {} is {}:".format(number,res))