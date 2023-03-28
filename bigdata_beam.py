import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import re
from apache_beam.io import WriteToText
from apache_beam.dataframe import convert
import pandas as pd
import time

st = time.time()



# create pipeline

input_file = 'test.csv'
output_path = 'counts.txt'

with beam.Pipeline() as p:
	# import texts from csv
	df = pd.read_csv(input_file, names=["type", "title", "text"])
	df = df.text

	# tokenize words
	# count word frequency
	counts = (
		convert.to_pcollection(df, pipeline=p) # converts dataframe into pcollection
		| 'ExtractWords' >> (
			beam.FlatMap(
				lambda x: re.findall(r'[A-Za-z\']+', x)).with_output_types(str))
		| 'PairWithOne' >> beam.Map(lambda x: (x, 1))
		| 'GroupAndSum' >> beam.CombinePerKey(sum))
	
	def format_result(word_count):
		# Format the counts into a PCollection of strings.
		(word, count) = word_count
		return '%s: %s' % (word, count)

	output = counts | 'Format' >> beam.Map(format_result)
	
	# output | WriteToText(output_path)



et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
	
