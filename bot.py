import random
import string

print('CONGRATS FOR REACHING THIS STAGE')
A = input('ENTER THE NO. YOU FOUND IN THE PREVIOUS IMAGE' ":" " ")
N = 25
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
b = str(res)
if A == "277":
    print('OKAY GOOD. TAKE THIS TOKEN AND DM IT US ON OUR OFFICIAL INSTAGRAM ACCOUNT:', b)
else:
    print('ughh ohh! wrong code')
