#It needs two files "first" and "second" to run
a=open("first")
b=open("second")
s=a.read()
t=b.read()
s=s.split()
t=t.split()
slen=len(s)
tlen=len(t)
count=0
for i in range(slen):
	if s[i] in t:
		count+=1
va=count/slen
print(str(int(va*100))+"%")
print(s)
