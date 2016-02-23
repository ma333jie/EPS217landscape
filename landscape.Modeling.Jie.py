
# coding: utf-8

# 0. Let's Define the problem

# In[1]:

import numpy as np
import random
import math
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[2]:

xl = 100*1e3
yl = 100*1e3
nx = 101
ny = 101
dt = 1000 # years
nstep = 1000 


# In[3]:

k = 1e-4
n = 1
m = 0.4
u = 2.e-3


# ### boundary condition 
# c1: h = 0 and (U = 0) along all 4 boundaries /
# c2: h = 0 at y = 0, y = yl and cyclic boundary conditions between x = 0 and x = xl /
# c3: h = 0 at y = 0 and relfective boundary conditions at y = yl and cyclic boundary condition / 
# 
# initial condition h = 0, nut need to adding a 1m high random noise

# In[4]:

# convection, everything only have one index
nn = nx*ny
h =  np.random.rand(nn,1)


# #### Do not run this, 
# for j in range(ny): <br />
#     for i in range(nx):<br />
#         nn2 = i+j*nx

# In[5]:

# compute the steepest neighbor node, check the smallest neighbor
# teach solution 
# other note a = sum (a, 1, mask) 


# In[6]:

# 1.compare with 8 different number
recdists = [] # distance to the receiver
recInds = [] # which is the receiver 
dx = xl/(nx-1)
dy = yl/(ny-1)
ddia = math.sqrt(dx*dx+dy*dy)

for i in range(nn):
    hmin = h[i]
    hmin = hmin[0]
    rec = i # reciver is itself
    d = 0  # distance is zero
    
    # make the hmin at the edges as zero first than calculate the inside value, fixed boundary 
    if i < nx or i > nn-nx or i % nx == 0 or i % nx == nx-1:
        d = 0  
        rec = i
        
    # 4 diagonal, 2 left, 2 right  
    else:
        ulist = [i-1+nx, i+1+nx, i-1-nx, i+1-nx, i-1, i+1, i-nx, i+nx] 
        dd = [ddia, ddia, ddia, ddia, dx,dx, dy,dy]
        for j in range(8):
            u = int(ulist[j])
            a = h[u]
            
            if a < hmin:
                hmin = a[0]
                d = dd[j]
                rec = u
    
    recdists.append(d) # distancce to its receiver  
    recInds.append(rec) # index of the receiver 


# In[7]:

# loop through the receiver ray 
ndon = np.zeros(nn) # calculate how many donner each cell has
donors = np.empty((nn,8)) # which index is the donner cell
donors[:] = np.NAN
#a = numpy.empty((3,3,))
#>>> a[:] = numpy.NAN
for i in range(nn):
    current = recInds[i] #start from reading the receiver array 
    if i != current:
        num = int(ndon[current])
        donors[current,num]= i # tell the donor where current from 
        ndon[current] = ndon[current]+1 # tell donor how many donor it has


# In[8]:

ndon = [0]*nn
donors = [[]]*nn

for i in range(nn):
    current =recInds[i]
    if i !=current:
        donors[current] = donors[current]+[i]
        ndon[current] = ndon[current]+1


# In[9]:

def helper(old,roots):
    if len(roots) == 0: # check if roots is an empty array        
        return old
    else:
        node = roots[0]
        old = old+[node]
        
        if ndon[node] == 0:
            roots = roots[1:]
        else:
            roots = donors[node]+roots[1:]
        return helper(old, roots)


# In[10]:

#start from the boundary and find its roots until the roots is itself 
#process to the doner until the #nun doner is zero
stacks = []
colors = []
# loop through each local minimum 
for i in range(nn):
    if i == recInds[i]:
        starter = i
        old = []
        stacks = stacks+helper(old, [starter])
        nsameColor = len(helper(old,[starter]))
        colors = colors +[starter]*nsameColor
        


# In[11]:

print type(stacks)


# In[12]:

revstacks = stacks[::-1]
#calculate the drange area
a = 0
areas = []
for i in range(nn):
    # check if it is the edges 
    if ndon[revstacks[i]] == 0:
        cumarea = dx*dy
        
    else:
        cumarea = dx*dy+cumarea
        a = a+1
    areas.append(cumarea)


# In[13]:

#build a link list, add the area dxdy 


# In[14]:

# first creat a area with 


# In[ ]:




# In[ ]:



