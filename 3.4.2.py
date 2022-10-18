#import matplotlib.pyplot as plt
#https://pythonbaba.com/online-python-code-editor-and-ide-for-data-science/

tau0 = 6.9092
k = 24 * 10 ** (-3)

taus = [7.982, 7.967, 7.949, 7.929, 7.908, 7.880, 7.848, 7.818, 7.782, 7.735, 7.687, 7.634, 7.583, 7.512, 7.478, 7.423, 7.318, 7.266, 7.177, 7.136, 7.109, 7.092] 
T = [14.2, 15.05, 15.51, 16.03, 16.52, 17.03, 17.54, 18.03, 18.52, 19.04, 19.53, 20.04, 20.53, 21.05, 21.51, 22.04, 23.02, 24.03, 26.09, 28.09, 30.1, 32.04]
delta_u = [-6, -16, -16, -16, -16, -14, -14, -15, -15, -14, -14, -13, -14, -9, -11, -14, -12, -20, -15, -15, -12, -13]

y = [1 / (tau ** 2 - tau0 ** 2) for tau in taus]

for i in range(len(T)):
    T[i] += k * delta_u[i]
    #print(T[i], 100*y[i])

#plt.scatter(T,y)

#plt.show()


t = [T[15], T[16], T[17], T[18]] #x

s = [y[15], y[16], y[17], y[18]] #y


def sr(a):
    s=0
    for x in a:
        s=s+x
    return s/4
def srp(a,b):
    s=0
    for i in range(4):
        s=s+a[i]*b[i]
    return s/4
b=(srp(t,s)-sr(t)*sr(s))/(srp(t,t)-(sr(t))**2)
print(b)
a=sr(s)-b*sr(t)
print(a)
print()
gb=((srp(s,s)-(sr(s))**2)/(srp(t,t)-(sr(t))**2)-b**2)**0.5
gb=gb/(4**0.5)
print(gb)
ga=gb*((srp(t,t)-(sr(t))**2)**0.5)
print(ga)
print()
print(-a/b)
print()
#print(((ga/a)**2+(gb/b)**2)**0.5)
def f(x):
    return -0.5548104014158303 + 0.03190261941623221 * x
'''
print(f(15))
print(f(30))
'''
print('='*25)
print()
gasis=4*((10**-6)/7.266)**2+(0.1**2+(24**2)*(0.02**2))/((24.03+24*0.02)**2)
print(((ga/a)**2+(gb/b)**2+2*gasis)**0.5)
