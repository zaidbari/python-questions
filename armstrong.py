'''
Armstrong number in python
A 3 digit armstrong number is a number that is equal to the sum of cubes of its digits and a 4 digit armstrong number is a number that consists of four such digits whose fourth powers when added together give the number itself
'''

num = int(input("Enter a number: "))
sum = 0

temp = num

if ( num <= 999):
   while temp > 0:
      digit = temp % 10
      sum  += digit ** 3
      temp //= 10
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")

elif ( (num > 999) and (num < 10000)):
   while temp > 0:
      digit = temp % 10
      sum += digit ** 4
      temp //= 10
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")

else:
   print(num,"is not an Armstrong number")

