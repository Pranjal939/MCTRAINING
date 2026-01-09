import time
with open('abc.txt','a') as file:
    age = 20
    marks = 55
    state = 'GJ'
    time =  time.ctime()
    file.write(f'\n{age},{marks},{state},{time}')
file.close()
