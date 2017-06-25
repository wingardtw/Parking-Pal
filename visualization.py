import mysql.connector
import numpy as np
import matplotlib
import matplotlib.pyplot as plt, matplotlib.dates as mdates
from sklearn.neural_network import MLPRegressor 
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
import xml.etree.ElementTree as ET
from datetime import datetime

# Set up element trees for parsing
tree1 = ET.parse('garage1data.xml')
tree3 = ET.parse('garage3data.xml')
tree4 = ET.parse('garage4data.xml')
root1 = tree1.getroot()
root3 = tree3.getroot()
root4 = tree4.getroot()
y1 = []
X1 = []
y3 = []
X3 = []
y4 = []
X4 = []
hours = []
Xtick = []

# Collect data for garages
for child in root1:
	y1.append(child[2].text)
	X1.append(child[3].text)

for child in root3:
	y3.append(child[2].text)
	X3.append(child[3].text)

for child in root4:
	y4.append(child[2].text)
	X4.append(child[3].text)

# Shape data for sklearn
X1 = mdates.datestr2num(X1)
X1 = X1.reshape(-1,1)

X3 = mdates.datestr2num(X3)
X3 = X3.reshape(-1,1)

X4 = mdates.datestr2num(X4)
X4 = X4.reshape(-1,1)

# Test data set
Xtest = np.arange(736504.84722222,736505.6962963, .01).reshape(-1,1)



y1 = np.asarray(y1,dtype=float)
y3 = np.asarray(y3,dtype=float)
y4 = np.asarray(y4,dtype=float)


reg1 = MLPRegressor()
reg1.fit(X1, y1)

reg3 = MLPRegressor()
reg3.fit(X3, y3)

reg4 = MLPRegressor(activation = 'logistic',
					solver = 'sgd',
					alpha = .001,
					hidden_layer_sizes = 2,
					max_iter = 3000)
reg4.fit(X4, y4)

kr1 = KernelRidge(kernel = 'rbf')
kr1.fit(X1,y1)

kr3 = KernelRidge(kernel = 'rbf')
kr3.fit(X3,y3)

kr4 = KernelRidge(kernel = 'rbf')
kr4.fit(X4,y4)

svr_rbf1 = SVR(kernel='rbf', C = 1e4,gamma = 0.1, epsilon = 0.001)
y_rbf1 = svr_rbf1.fit(X1,y1).predict(Xtest)

svr_rbf3 = SVR(kernel='rbf', C = 1e5,gamma = 0.1, epsilon = 0.001)
y_rbf3 = svr_rbf3.fit(X3,y3).predict(Xtest)

svr_rbf4 = SVR(kernel='rbf', C = 1e5,gamma = 0.1, epsilon = 0.001)
y_rbf4 = svr_rbf4.fit(X4,y4).predict(Xtest)

#print(svr_rbf4.get_params())

#test_x = np.arange(736504.84722222,736505.48074074,.001).reshape(-1,1)
#print(reg.predict(736505.26962963))
#print(reg.score(X,y))


fig, ax =plt.subplots()
#plt.plot_date(X1, y1,label= "Garage 1 Occupancy")
plt.plot_date(X3, y3, label= "Garage 3 Occupancy")
#plt.plot_date(X4, y4, label = "Garage 4 Occupancy")
#plt.plot_date(Xtest,y_rbf1, label= "Garage 1 Model_SVR")
plt.plot_date(Xtest,y_rbf3, label= "Garage 3 Model_SVR")
#plt.plot_date(Xtest,y_rbf4, label = "Garage 4 Model_SVR")
#plt.plot_date(X1,kr1.predict(X1), label = "Garage 1 Model_KR")
#plt.plot_date(X3,kr3.predict(X3), label = "Garage 3 Model_KR")
#plt.plot_date(X4,kr4.predict(X4), label = "Garage 4 Model_KR")
#plt.plot_date(X1,reg1.predict(X1), label= "Garage 1 Model_MLPReg")
#plt.plot_date(X3,reg3.predict(X3), label= "Garage 3 Model_MLPReg")
#plt.plot_date(X4,reg4.predict(X4), label= "Garage 4 Model_MLPReg")

print("Score 1: " + str(svr_rbf1.score(X1,y1)))
print("Score 3: " + str(svr_rbf3.score(X3,y3)))
print("Score 4: " + str(svr_rbf4.score(X4,y4)))

legend = plt.legend(loc = 'upper center', shadow = True)
plt.ylabel('Number of spots occupied')
plt.title('SF Parking Occupancy')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
#plt.plot_date(test_x, kr1.predict(test_x))
#plt.plot_date(test_x, kr3.predict(test_x))
#plt.plot_date(test_x, kr4.predict(test_x))
plt.show()

"""
db = mysql.connector.connect(host = "localhost",
					 		 user = "root",
					 		 passwd = "",
					 		 db = "parking_pad"
							)

cur = db.cursor()
dt = []
num_taken = []
cur.execute('SELECT datetime, availability FROM availability WHERE availability != 0 AND garage_id = 1')
for tup in cur:
	dt.append(tup[0])
	num_taken.append(tup[1])

dates = mdates.date2num(dt)
plt.plot_date(dates, num_taken)
plt.show()
"""

