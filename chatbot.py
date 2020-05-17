import random
import string


print ("HELLO! WE ARE LOOKING FOR POTENTIAL INDIVIDUALS FOR OUR SECRET ENTITY")

a = input('enter the no. you found in the image:' ' ')
N = 25
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
b = str(res)
if a == "297":
    print('good, now dm us on @theacehorsemen on insta for further instructions with this token:', b)
else:
    print('ugh ohh! sorry its wrong')
