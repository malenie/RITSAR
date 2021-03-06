##############################################################################
#                                                                            #
#  This is a demonstration of the ritsar toolset using AFRL Gotcha data.     #
#  Algorithms can be switched in and out by commenting/uncommenting          #
#  the lines of code below.                                                  #
#                                                                            #
##############################################################################

#Add include directories to default path list
from sys import path
path.append('../')

#Include standard library dependencies
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
cmap = cm.Greys_r

#Include SARIT toolset
from ritsar import phsRead
from ritsar import imgTools

#Define top level directory containing *.mat file
#and choose polarization and starting azimuth
pol = 'HH'
directory = './data/AFRL/pass1'
start_az = 1

#Import phase history and create platform dictionary
[phs, platform] = phsRead.AFRL(directory, pol, start_az, n_az = 3)

#Create image plane dictionary
img_plane = imgTools.img_plane_dict(platform, res_factor = 1.5, upsample = True, aspect = 1.0)

#Apply algorithm of choice to phase history data
img_bp = imgTools.backprojection(phs, platform, img_plane, taylor = 43, upsample = 6)
#img_pf = imgTools.polar_format(phs, platform, img_plane, taylor = 43)

#Output image
plt.imshow(np.abs(img_bp)**0.5, cmap = cm.Greys_r)
plt.title('Backprojection')

#Autofocus image
print('autofocusing')
#img_af, af_ph = imgTools.autoFocus(img_bp, win = 0, win_params = [300,0.8])
img_af, af_ph = imgTools.autoFocus(img_bp, win = 0, win_params = [300,0.8])

#Output autofocused image
plt.figure()
plt.imshow(np.abs(img_af)**0.5, cmap = cm.Greys_r)
plt.title('Autofocused Polar Format')
