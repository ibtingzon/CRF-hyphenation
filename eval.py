from __future__ import division


def evaluateSeriousWordLevel(true_output, predicted_output):
	swe, total = 0, 0
	size = len(true_output)

	for i in range(size):
		for j in range(len(true_output[i])):
			true = int(true_output[i][j])
			predicted = int(predicted_output[i][j])
			if true == 0 and predicted == 1:
				swe = swe + 1
				break
		total = total + 1

	return swe, total

def evaluateOverallWordLevel(true_output, predicted_output):
	owe, total = 0, 0
	size = len(true_output)

	for i in range(size):
		if true_output[i] != predicted_output[i]:
			owe = owe + 1
		total = total + 1

	return owe, total

def evaluateLetterLevel(true_output, predicted_output):
	TN, TP, FN, FP = 0, 0, 0, 0
	total = 0
	size = len(true_output)

	for i in range(size):
		for j in range(len(true_output[i])):
			true = int(true_output[i][j])
			predicted = int(predicted_output[i][j])

			if true == predicted:
				TP = TP + 1
			elif true == 1 and predicted == 0:
				FN = FN + 1
			elif true == 0 and predicted == 1:
				FP = FP + 1
			elif true == 0 and predicted == 0:
				TN = TN + 1
			total = total + 1

	return TP, TN, FP, FN, total

def readResults(filename):
	file = open(filename)
	line = file.readline()

	true_output = []
	predicted_output = []
	true_output_set = []
	predicted_output_set = []
	
	while line:
		if not line.strip():
			true_output = []
			predicted_output = []
			true_output_set.append(true_output)
			predicted_output_set.append(predicted_output)
		else:
			line = line.split()
			true_output.append(line[-2])
			predicted_output.append(line[-1])

		line = file.readline()	

	file.close()
	return true_output_set, predicted_output_set

def main():
	filename = 'EngHyphen_results.txt'
	true_output, predicted_output = readResults(filename)
	TP, TN, FP, FN, total = evaluateLetterLevel(true_output, predicted_output)
	precision = (TP + TN)
	print 'n = ', total
	print "TP = ", TP, " (", TP/total, ")"
	print "TN = ", TN, " (", TN/total, ")"
	print "FP = ", FP, " (", FP/total, ")"
	print "FN = ", FN, " (", FN/total, ")"
	print "oler: (FP + FN)/ (TP + TN + FP +FN) = ", (FP + FN)/ (TP + TN + FP + FN)
	print "sler: (FP)/ (TP + TN + FP +FN) = ", (FP)/ (TP + TN + FP + FN)
	print "accuracy: (TP + TN)/ (TP + TN + FP +FN) = ", (TP + TN)/ (TP + TN + FP + FN)
	owe, total = evaluateOverallWordLevel(true_output, predicted_output)
	print "total no. of words = ", total
	print "owe =", owe
	print "ower =", owe/total
	swe, total = evaluateSeriousWordLevel(true_output, predicted_output)
	print "swe = ", swe
	print "swer =", swe/total


if __name__ == '__main__':
    main()