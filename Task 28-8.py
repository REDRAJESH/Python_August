#!/usr/bin/env python
# coding: utf-8

# In[227]:


a="computer science"
b=a.split()
c=b[0]
d=b[-1]

#1st Word
e=c[len(c)//2]
f=c.split(c[len(c)//2])
g=f[0]
q=f[-1]
h=g.capitalize()
i=h[0:-1]+h[-1].upper()
j=i+e+q

#Second Word
x=d[len(d)//2]
m=d.split(d[len(d)//2])
n=m[0]
o=m[1]
p=(m[len(m)//2])
r=x.upper()
s=n+r+o+x

#4th 
t=j+s
u=(t[len(t)//2]).upper()
w=t.split(t[len(t)//2])
aa=w[0]
bb=w[-1]
cc=aa+u+bb

print(cc)




# In[ ]:





# In[ ]:




