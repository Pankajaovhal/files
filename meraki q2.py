a=open("people1-exercise.txt","w")
a.write("rishabh - meerut\nimtiyaz - delhi\nnilima - cochin\nrati - shimla\nayishah - delhi\nraghu - shimla\nnaseer - kanpurkarthikeyan - delhi")
a.write("salma - jaipur\npankaj - delhi\nbrijesh - delhi\ngovind - delhi\npuneet - shimla\nsiddhi - delhi\nsuman - jaipur\nrajeev - shimla")
a.write("mohinder - delhi\nrajendra - jaipur\npriyanka - shimla\nneela - delhi\nsashi - jaipur\nsarika - delhi\ndeepti - shimla\nharshad - delhi")
a.write("trishna - raipur\npradeep - jaipur\nsekhar - delhi\nnand - delhi\nanoop - delhi\nbalwinder - toky")
a.close()

a=open("people1-exercise.txt","r")
print(a.read())

# a=open("people-exercise.txt","r")
# i=a.read()
# print(i)

# file=open("people1-exercise.txt","r")
# c=0
# for i in file:
#     c=c+1
# print(c)