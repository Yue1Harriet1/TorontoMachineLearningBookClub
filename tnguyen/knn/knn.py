from operator import itemgetter
import numpy as np
import math

# The KNN algorithm
def predict(testVector, trainingSet, k):
	# calculate distances
	predictions = []
	for trainingVector in trainingSet:
		distance = math.sqrt(((trainingVector[:-1] - testVector[:-1])**2).sum())
		prediction = trainingVector[-1]
		predictions.append([distance, prediction])

	# sort by distance
	predictions = sorted(predictions, key=itemgetter(0))

	# take top k
	predictions = np.array(predictions)[:,1]
	predictions = predictions[:k]

	# tally votes
	votes = {}
	for vote in predictions:
		if vote in votes:
			votes[vote] = votes[vote] + 1
		else:
			votes[vote] = 1

	# find max vote
	maxVote = -1
	prediction = ""
	for vote in votes:
		if votes[vote] > maxVote:
			maxVote = votes[vote]
			prediction = vote

	return prediction

def test(testSet, trainingSet, k):
	predictions = []
	expectations = []

	for testVector in testSet:
		prediction = predict(testVector, trainingSet, k)
		expected = testVector[-1]

		predictions.append(prediction)
		expectations.append(expected)

	predictions = np.array(predictions)
	expectations = np.array(expectations)

	diff = predictions - expectations
	diff = np.absolute(diff)

	correct = 0
	for i in range(len(predictions)):
		if expectations[i] == predictions[i]:
			correct += 1
		#print "expectation: {0}, prediction: {1}".format(expectations[i], predictions[i])

	print "K: {0}, percent correct: {1:.2f}".format(k, float(correct)/len(testSet))

# import data
SUBSET = True
execfile("import.py")

for k in range(1, 20):
	test(testSet, trainingSet, k)
