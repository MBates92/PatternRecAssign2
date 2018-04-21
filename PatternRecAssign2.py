import numpy as np
import matplotlib.pyplot as plt

###############################################################################
'''Functions'''
###############################################################################

def gradient_ascent(x,f,steps):

    df = np.gradient(f,x)
    
    initial_idx = np.random.randint(0,steps)
    next_idx = initial_idx
    
    conv = []
    
    for i in range(0,steps):
        
        if next_idx == steps:
            return np.nan
    
        grad = float(df[next_idx])
        
        if grad>0:
            step = 1
        elif grad<0:
            step = -1
        
        next_idx += step
        
        if i == steps-2:
            conv.append(next_idx)
        if i == steps-1:
            conv.append(next_idx)
            
    conv = np.asarray(conv)    
    guess = []
    guess.append(x[conv[0]])
    guess.append(x[conv[1]])
    
    final_guess = np.mean(guess)
    
    return final_guess

###############################################################################
'''Implementation'''
###############################################################################

x = np.linspace(-6*np.pi,6*np.pi,1000)
f = np.sin(x)
steps = 1000

guesses = []

iterations = 1000

for k in range(0,iterations):
    guesses.append(gradient_ascent(x,f,steps))

guesses = np.asarray(guesses)
a,axarr = plt.subplots(2,sharex=True)
axarr[0].plot(x, f,c='g')
axarr[0].scatter(guesses,np.sin(guesses),c='r')
axarr[0].set_title('1000 tries')
axarr[0].set_ylabel('f(x)=sin(x)')
axarr[1].hist(x,bins = 6,rwidth = 0.5,edgecolor="k")
axarr[1].set_xlabel('x')
axarr[1].set_ylabel('N')