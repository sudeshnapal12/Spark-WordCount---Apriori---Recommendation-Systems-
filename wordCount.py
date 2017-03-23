###########################################
# Author: Sudeshna Pal
# SBU ID: 110938222
###########################################

from pyspark import SparkContext
from operator import add

# Creating Spark Context
sc = SparkContext(appName="Word Count")
text_file = sc.textFile("README.md")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print 'Word count', counts.collect()