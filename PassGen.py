from random import randint

password = ""
for i in range(10):
    i = chr(randint(65,90))
    password = str(password) + i
print(password)

password = ""
for i in range(4):
    i = chr(randint(65, 90))
    for j in range (4):
        j = chr(randint(65, 90)).lower()
    for k in range (2):
        k = chr(randint(50, 64))
    password = str(password) + i + j + k
print(password)

