# Comandos para instalar la paqueteria necesaria:
#    pip install numpy
#    pip install scipy
#    python -mpip install -U matplotlib
#    python -mpip install -U sklearn

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np

#import some data to play with
iris = datasets.load_iris()



especies = iris.target_names
caracteristicas = iris.data


plt.figure(1)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,2])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,2])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,2])
plt.ylabel('Longitud de Pétalo (cm)')
plt.show()

plt.figure(2)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,3])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,3])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,3])
plt.ylabel('Anchura de Pétalo (cm)')
plt.show()

plt.figure(3)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,0])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,0])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,0])
plt.ylabel('Longitud de Sépalo (cm)')
plt.show()

plt.figure(4)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,1])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,1])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,1])
plt.ylabel('Anchura de Sépalo (cm)')
plt.show()
#En esta version de la base de datos de iris las dos primeras columnas
#corresponden a las medidas de Sépalo y las otras dos columnas a las
#medidas del Pétalo, contrario a la version que se maneja en el curso de
#IA de Iran Roman
#0:Longitud de Sepalo 1:Anchura de Sepalo
#2:Longitud de Petalo 3:Anchura de Petalo


#Al parecer, las dos caracteristicas que mejor separan los tres tipos de flores fueron
#La longitud de Petalo y la Anchura de Pétalo. La siguiente figura muestra como estas dos caracteriticas
#diferencian los tres tipos de flores.
plt.figure(5)
plt.scatter(caracteristicas[0:49,2],caracteristicas[0:49,3])
plt.scatter(caracteristicas[50:99,2],caracteristicas[50:99,3])
plt.scatter(caracteristicas[100:149,2],caracteristicas[100:149,3])
plt.xlabel('Longitud de Pétalo (cm)')
plt.ylabel('Anchura de Pétalo (cm)')
plt.show()

#Experimenta generando otras figuras donde grafiquesotras caracteristicas en los ejesx,y.
#Determina si alguna otra pareja de caracteristicas sirve para diferenciar las tres especies de
#flores.Después procede a responder las siguientes preguntas.

plt.figure(6)
plt.scatter(caracteristicas[0:49,0],caracteristicas[0:49,1])
plt.scatter(caracteristicas[50:99,0],caracteristicas[50:99,1])
plt.scatter(caracteristicas[100:149,0],caracteristicas[100:149,1])
plt.xlabel('Longitud de Sépalo (cm)')
plt.ylabel('Anchura de Sépalo (cm)')
plt.show()

plt.figure(7)
plt.scatter(caracteristicas[0:49,2],caracteristicas[0:49,0])
plt.scatter(caracteristicas[50:99,2],caracteristicas[50:99,0])
plt.scatter(caracteristicas[100:149,2],caracteristicas[100:149,0])
plt.xlabel('Longitud de Pétalo (cm)')
plt.ylabel('Longitud de Sépalo (cm)')
plt.show()

plt.figure(8)
plt.scatter(caracteristicas[0:49,3],caracteristicas[0:49,1])
plt.scatter(caracteristicas[50:99,3],caracteristicas[50:99,1])
plt.scatter(caracteristicas[100:149,3],caracteristicas[100:149,1])
plt.xlabel('Anchura de Pétalo (cm)')
plt.ylabel('Anchura de Sépalo (cm)')
plt.show()



