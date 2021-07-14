import random
import string
N = 23
a = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
print(a)
b = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
print(b)