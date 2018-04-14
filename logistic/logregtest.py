import numpy as np
import math
import sys
import csv

#Functions
def loadCSV(fileName,nFeat):
	xload = []
	yload = []
	temp = []
	with open(fileName) as f:
		string = f.read().replace('\n',',')
		lines = string.split(',')									#lines = list of every data point
	lines = lines[:-1]
	for count in range (0,len(lines)):
		if (count+1) % (nFeat+1) == 0:								#if position is 14(y value) append to y
			yload.append([float(lines[count])])
		else:														#else (if first position append a dummy '1') append to temp
			temp.append(float(lines[count]))
	xload = [temp[i:i+nFeat] for i in range(0,len(temp),nFeat)]		#splitting x into a list of lists separated by each instance
	x1 = np.matrix(xload)											#converting x from list of lists to matrices
	y1 = np.matrix(yload)											#converting y from list of lists to matrices
	x1 = x1 * (1.0/255.0)											#converts x values into percentages
	return x1,y1
	
def testAccuracy(weight,feats,results,nEx):
	correct = 0.0
	wrong = 0
	for i in range(nEx):
		powert = float(-1*(weight * feats[i].T))
		if (powert >= maxpow):
			ytest = 0.0
		elif (powert <= minpow):
			ytest = 1.0
		else:
			ytest = 1/(1+(e**powert))
			
		if (round(ytest,1) == results[i,0]):
			correct += 1.0
		else:
			wrong += 1
			print " "
			print ytest
			print results[i,0]
	print "Percentage"
	print (float(correct/float(nEx)))*100
	print "Number of errors"
	print wrong


#Constants
e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250996181881593041690351598888519345807273866738589422879228499892086805825749279610484198444363463244968487560233624827041978623209002160990235304369941849146314093431738143640546253152096183690888707016768396424378140592714563549061303107208510383750510115747704171898610687396965521267154688957035035402123407849819334321068170121005627880235193033224745015853904730419957777093503660416997329725088687696640355570716226844716256079882651787134195124665201030592123667719432527867539855894489697096409754591856956380236370162112047742722836489613422516445078182442352948636372141740238893441247963574370263755294448337998016125492278509257782562092622648326277933386566481627725164019105900491644998289315056604725802778631864155195653244258698294695930801915298721172556347546396447910145904090586298496791287406870504895858671747985466775757320568128845920541334053922000113786300945560688166740016984205580403363795376452030402432256613527836951177883863874439662532249850654995886234281899707733276171783928034946501434558897071942586398772755
numEx = 1400		#number of examples in training data
testEx = 800		#number of examples in testing data
numFeat = 256		#number of features
eta = 0.01			#learning rate
itr = 600.0			#number of iterations
emptyArray = []
for f in range(numFeat):
	emptyArray.append(0.0)					#A vector of 0s
maxpow = (math.log(sys.float_info.max))-0.1 #maximum power that e can be put to and not overflow
minpow = (math.log(sys.float_info.min))+0.1 #minimum power that e can be put to and not overflow



#Logistic regression w/o regulation
x,y = loadCSV("usps-4-9-train.csv",numFeat)
w = np.matrix(emptyArray)
gradient = np.matrix(emptyArray)
for f in range(itr):
	gradient = np.matrix(emptyArray)
	for i in range(0,numEx):
		power = float(-1*(w * x[i].T))
		if (power >= maxpow):
			ytarget = 0.0
		elif (power <= minpow):
			ytarget = 1.0
		else:
			ytarget = 1/(1+(e**power))

		gradient = gradient + ((ytarget - y[i])*x[i])
	w = w - (eta*gradient)

x,y = loadCSV("usps-4-9-test.csv",numFeat)
print "Without regulation"
testAccuracy(w,x,y,testEx)


#logistic regression with regulation
x,y = loadCSV("usps-4-9-train.csv",numFeat)
w = np.matrix(emptyArray)
gradient = np.matrix(emptyArray)
lamb = e**1.2 #regularization strength
for f in range(itr):
	gradient = np.matrix(emptyArray)
	for i in range(0,numEx):
		power = float(-1*(w * x[i].T))
		if (power >= maxpow):
			ytarget = 0.0
		elif (power <= minpow):
			ytarget = 1.0
		else:
			ytarget = 1/(1+(e**power))

		gradient = gradient + ((ytarget - y[i])*x[i])
	w = w - (eta*(gradient + (lamb*w)))

x,y = loadCSV("usps-4-9-test.csv",numFeat)
print "\nWith Regulation"
testAccuracy(w,x,y,testEx)