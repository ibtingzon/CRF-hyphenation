import random

def convertToCRFFormat(data_set, filename):
	outputfile = open(filename,'w')

	for word in data_set:
		for ind in range(len(word)):			
			if ind == len(word) - 1: 
				outputfile.write(word[ind] + '\t' + str(0) + '\n')
			
			elif word[ind + 1] == '-':
				outputfile.write(word[ind] + '\t' + str(1) + '\n')
			
			elif word[ind] != '-' :
				outputfile.write(word[ind] + '\t' + str(0) + '\n')

		outputfile.write('\n')
	outputfile.close()

def splitDataset(data_orig):
	test_data = []
	train_data = []

	random.shuffle(data_orig)
	length = len(data_orig)/2
	
	for i in range(length):
		word = random.choice(data_orig)
		train_data.append(word)
		data_orig.remove(word)

	test_data = data_orig
	return train_data, test_data

def parseDataset(filename):
	data_orig = []
	inputfile = open(filename)
	line = inputfile.readline().strip()

	while line:
		line = inputfile.readline().strip()
		data_orig.append(line)

	inputfile.close()
	return data_orig

def main(): 
	filename = 'Englishdataset.txt'
	
	print "Reading data set..."
	data_orig = parseDataset(filename)
	
	print "Splitting the dataset (random)..."
	train_data, test_data = splitDataset(data_orig)

	print "Converting to CRF++ readable format..."
	convertToCRFFormat(train_data, 'EngHyphen_train.txt')
	convertToCRFFormat(test_data, 'EngHyphen_test.txt')

	print 'Done.'	

if __name__ == '__main__':
    main()