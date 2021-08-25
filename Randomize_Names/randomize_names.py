import random, os
alpha = list ("qwertyuiop[]asdfghjkl;'zxcvbnm,.1234567890QWERTYUIOP[]ASDFGHJKLZXCVBNM!@#$%^&()_+-=")
cycle = random.randint(6,50)
i=0
name = ''
while i < cycle:
        get_name = random.randint(0,len(alpha)-1)
        name += alpha[get_name]
        i += 1
old_folder = os.getcwd() + name
if old_folder == True:
        print ('There is same folder, start creating new name...')
        i=0
        while i < cycle:
                name =''
                get_name = random.randint(1,len(alpha)-1)
                name += alpha[get_name]
                i += 1
else:
        os.mkdir(name)
print ('Rdy')



