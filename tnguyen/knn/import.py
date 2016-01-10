import numpy as np
import random

PERCENT_TEST = 0.3

"""
LOAD DATA
"""
file = open("abalone.data", "r")

data = []

# transform input into something I can work with
for line in file:
	line = line.rstrip("\n")
	line = line.split(",")

	if line[0] == "M":	# male
		line[0] = 1
	elif line[0] == "F":	# female
		line[0] = 2
	elif line[0] == "I":	# infant, informative!
		line[0] = 5
	data.append(line)

random.shuffle(data)		# randomize

# make a copy
originalData = list(data)

data = np.array(data)		# type conversion
data = data.astype(np.float)

colMax = np.amax(data, axis=0) 	# largest values in each col
colMax[-1] = 1 			# leave the label alone
data = np.divide(data, colMax)	# scale to weight all dimensions equally

data = data + [[1, 1, 1, 1, 1, 1, 1, 1, 0]]*data.shape[0]

# print distribution
print "Original distribution"
print "_____________________"
histogram = np.histogram(data[:,8], bins=[x -0.5 for x in range(1, 31)])
for i in range(len(histogram[0])):
	print "{0}: {1}".format(i+1, histogram[0][i])

if SUBSET:
	"""
	From the histogram, I suspect the original data does not cluster.
	It wasn't lending itself to KNN, so I am harvesting two classes where labels are 6 and 12.
	"""
	# reshape date
	subset = []
	for vector in originalData:
		if vector[-1] == "6" or vector[-1] == "12":
			subset.append(vector)
	random.shuffle(subset)

	subset = np.array(subset)
	subset = subset.astype(np.float)
	data = subset

# print distribution
print "Subset"
print "______"
histogram = np.histogram(data[:,8], bins=[x -0.5 for x in range(1, 31)])
for i in range(len(histogram[0])):
	print "{0}: {1}".format(i+1, histogram[0][i])

# divide up the data set
numTestVectors = int(len(data) * PERCENT_TEST)
testSet = data[:numTestVectors]
trainingSet = data[numTestVectors:]
