
# coding: utf-8

# In[1]:

##use image shrinker to shrink by 94%
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as mpatches
import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


fig = plt.figure()

ax = fig.add_subplot(1,1,1)

data = np.transpose(np.loadtxt('spec'))

ax.plot(data[0], data[1], c='#000000', linewidth=0.5)
ax.yaxis.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.get_yaxis().tick_left()
ax.get_xaxis().set_tick_params(which='both',direction='out')
ax.set_ylim(0, 115)
ax.set_xlim(600, 2000)

ax.xaxis.set_major_locator(MultipleLocator(200))
ax.xaxis.set_minor_locator(MultipleLocator(50))

for label in ax.get_xticklabels(): 
        label.set_fontsize(10)

ax.set_xlabel('M/Z', fontweight='bold', fontsize = 10)


#pic = imread('A55_dimer_95.jpg')
#ab = AnnotationBbox(im, (1042, 95), frameon=False)
#ax.add_artist(ab)

pic = np.array(Image.open('A55_dimer_95.jpg'))
d = OffsetImage(pic, zoom=1)

donly = np.transpose(np.loadtxt('dimer_only_labels'))
dpos = np.transpose(np.loadtxt('dimerpicpos'))

##dimer only labels
##pic labels are 7 higher than the txt y position

for i in range(len(donly[0])):
    
    ax.annotate(str(int(donly[0][i]))+'+', xy=(donly[1][i], donly[2][i]), color='#4AB825', fontweight='bold', ha='center', fontsize=10)

ax.annotate('17+', xy=(749.27, 21), xytext=(693, 30), color='#4AB825', fontweight='bold', ha='center', fontsize=10, arrowprops=(dict(arrowstyle="->")))
ax.annotate('15+', xy=(847.11, 37), xytext=(804, 53), color='#4AB825', fontweight='bold', ha='center', fontsize=10, arrowprops=(dict(arrowstyle="->")))
ax.annotate('11+', xy=(1143.37, 96), xytext=(1187, 103), color='#4AB825', fontweight='bold', ha='center', fontsize=10, arrowprops=(dict(arrowstyle="->")))

    
for i in range(len(dpos[0])):
    temp = AnnotationBbox(d, (dpos[0][i], dpos[1][i]), frameon=False)
    ax.add_artist(temp)
    
##monomer and dimer only labels

monly = np.transpose(np.loadtxt('monomer_only_labels'))
mpos = np.transpose(np.loadtxt('monomerpicpos'))

for i in range(len(monly[0])):
        
    ax.annotate(str(int(monly[0][i]))+'+', xy=(monly[2][i]-41, monly[3][i]), color='#4AB825', fontweight='bold', ha='center', fontsize=10)
    ax.annotate('&', xy=(monly[2][i], monly[3][i]), fontweight='bold', ha='center', fontsize=10)
    
    if len(str(int(monly[1][i]))) == 2:
        ax.annotate(str(int(monly[1][i]))+'+', xy=(monly[2][i]+45, monly[3][i]), color='#B2B200', fontweight='bold', ha='center', fontsize=10)

    if len(str(int(monly[1][i]))) == 1:
        ax.annotate(str(int(monly[1][i]))+'+', xy=(monly[2][i]+35, monly[3][i]), color='#B2B200', fontweight='bold', ha='center', fontsize=10)

ax.annotate('16+', xy=(700-41, 51), color='#4AB825', fontweight='bold', ha='center', fontsize=10)
ax.annotate('&', xy=(783, 39), xytext=(700, 51), fontweight='bold', ha='center', fontsize=10, arrowprops=(dict(arrowstyle="->")))
ax.annotate('8+', xy=(700+35, 51), color='#B2B200', fontweight='bold', ha='center', fontsize=10)

ax.annotate('14+', xy=(855-41, 74), color='#4AB825', fontweight='bold', ha='center', fontsize=10)
ax.annotate('&', xy=(897, 44), xytext=(855, 74), fontweight='bold', ha='center', fontsize=10, arrowprops=(dict(arrowstyle="->")))
ax.annotate('7+', xy=(855+35, 74), color='#B2B200', fontweight='bold', ha='center', fontsize=10)


#ax.annotate('14+', xy=(847.11, 37), xytext=(804, 53), color='#4AB825', fontweight='bold', ha='center', fontsize=10, arrowprops=(dict(arrowstyle="->")))
        
for i in range(len(mpos[0])):
    temp = AnnotationBbox(d, (mpos[0][i], mpos[1][i]), frameon=False)
    ax.add_artist(temp)

####
green_patch = mpatches.Patch(color='#4AB825', alpha=.8)
yellow_patch = mpatches.Patch(color='#B2B200', alpha=.8)

ax.legend([yellow_patch,green_patch], ['TerS DBD Monomer Ions','TerS DBD Dimer Ions'], fontsize=10)

plt.figtext(0,0.94,'B', fontsize=20)
        
fig.patch.set_facecolor('white')
plt.tight_layout()

plt.show()


# In[58]:

plt.close("all")


# In[ ]:



