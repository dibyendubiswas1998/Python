stu = {'fname':'Dibyendu',
       'lname':'Biswas',
       'age':22,
       'ph':9476289669,
       'course':['python', 'django', 'javascript', 'ML', 'DL']
        }
#-----------------------------------------------------

print(stu['lname'])
print(stu['age'])
print(stu['ph'])
#-----------------------------------------------------

stu['age'] = 23
print(stu)
#-----------------------------------------------------

stu.pop('age')
print(stu)
#-----------------------------------------------------

stu['fname'] = 'Deb'
stu['lname'] = 'Roy'
print(stu)
#-----------------------------------------------------

print(stu.get('course'))
print(stu.get('course1', 'Not Found'))
#-----------------------------------------------------

print(stu.keys())
print(stu.items())
#-----------------------------------------------------

for key, value in stu.items():
    print(f"{key} : {value}")
#-----------------------------------------------------

fname = ['Arko', 'Dibyendu', 'Ram', 'Shyam']
lname = ['Biswas', 'Paul', 'Roy', 'Sen']
#-----------------------------------------------------

print(list(zip(fname, lname)))
#-----------------------------------------------------

dct = dict()
for fname, lname in zip(fname, lname):
    dct[fname] = lname
print(dct)
#-----------------------------------------------------

myDct = {fname:lname for fname,lname in zip(fname, lname)}
print(myDct)

#-----------------------------------------------------
myDct = {fname:lname for fname,lname in zip(fname, lname) if fname != 'Dibyendu'}
print(myDct)

