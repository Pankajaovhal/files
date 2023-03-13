# a=open("question3","w")
# a.write("rishabh -meerut,\nimtiyaz -delhi,\nnilima -cochin,\nrati -shimla,\nayishah -delhi,\nraghu -shimla,\nnaseer -kanpur,\nkarthikeyan -delhi,\nsalma -jaipur,\npankaj -delhi,\nbrijesh -delhi,\ngovind -delhi,\npuneet -shimla,\nsiddhi -delhi,\nsuman -jaipur,\nrajeev -shimla,\nmohinder - delhi,\nrajendra -jaipur,\npriyanka -shimla,\nneela -delhi,\nsashi -jaipur,\nsarika -delhi,\ndeepti -shimla,\nharshad -delhi,\ntrishna -raipur,\npradeep -jaipur,\nsekhar -delhi,\nnand -delhi,\nanoop -delhi,\nbalwinder - tokyo")
# a.close()

a=open("question3.txt","r")
for i in a: 
    if "delhi" in i:
        d=open("delhi.txt","a")
        d.write(i)
        d.close()
    elif "shimla" in i:
        s=open("shimla.txt","a")
        s.write(i)
        s.close()
    else:
        o=open("others.txt","a")
        o.write(i)
        o.close()




