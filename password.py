import random
import string
length = int(input('enter the length of password'))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
all = lower + upper + num
temp = random.sample(all,length)
password = "".join(temp)
all = string.ascii_letters + string.digits 
password = "".join(random.sample(all,length))
print(password)
