import csv
import time

st = time.time()


# import texts from csv
texts = []
with open('test.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		texts.append(row[2])
		line_count += 1

# tokenize words
words = []
for t in texts:
	word = t.split()
	for w in word:
		words.append(w)

# count word frequency
freq = {}
for w in words:
	if w in list(freq.keys()):
		freq[w] += 1
	else:
		freq[w] = 1
#print(freq)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
