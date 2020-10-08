import matplotlib.pyplot as plt
import math 
import numpy as np 

#input variables for calculating gsd
focal_length = float(input("What is your focal length in millimeters?"))
primary_diameter = float(input("What is your primary diameter in millimeters?"))
central_wavelength = float(input("What is your central wavelength in nanometers?"))
lpmm = float(input("What spatial resolution are you wishing to find a value for (lp/mm)?"))
secondary_diameter = float(input("What is your secondary diameter in millimeters?"))
#converting variable to mm
central_wavelength = central_wavelength*1e-6

#equations/outputs
D = secondary_diameter/primary_diameter
cutoff = 1/(central_wavelength*(focal_length/primary_diameter))
X = lpmm/cutoff
Y = X/D
A = (2/math.pi)*(np.arccos(X)-(X*math.sqrt(1-X**2)))
alpha = np.arccos(((1+D**2)-(4*X**2))/(2*D))

if Y > 1:
    B = 0
else:
    B = ((2*(D**2))/math.pi)*(np.arccos(Y)-(Y*math.sqrt(1-Y**2)))
E = ((1+D**2)-(4*X**2))/(2*D)

if E > 1:
    C = -2*D**2
else:
    C = ((2*D/np.pi)*(np.sin(alpha)))+(((1+D**2)/np.pi)*(alpha))-(((2*(1-D**2))/np.pi)*np.arctan((1+D)/(1-D))*np.tan(alpha/2))-(2*(D**2))


MTF = (A+B+C)/(1-D**2)

lpmm = np.linspace(0,cutoff,500)
s = MTF

plt.plot(lpmm,s)


print('your cut-off frequency is', cutoff, 'lp/mm')
print('your primary/secondary ratio is', D)
print('Your X is', X) 
print('Your Y is', Y) 
print('Your Alpha is', alpha) 
print('Your A is', A) 
print('Your B is', B) 
print('Your C is', C) 
print('Your MTF is', MTF,'lp/mm')            
                 


#axis titles
plt.title('MTF (lp/mm)')
plt.xlabel('Spatial Resolution (lp/mm)')
plt.ylabel('MTF')
  
# function to show the plot 
plt.show() 


