from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer
import pyspark.sql.functions as f
import time

st = time.time()


# import texts from csv
spark = SparkSession\
  .builder \
  .appName("PythonWordCount") \
  .getOrCreate()

df = spark.read.csv("test.csv")

# tokenize words
tokenizer = Tokenizer(inputCol='_c2', outputCol='words_token')
df_words_token = tokenizer.transform(df)

# count word frequency
result = df_words_token.withColumn('word', f.explode(f.col('words_token'))) \
  .groupBy('word') \
  .count().sort('count', ascending=False) \

spark.stop()


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
