###########################################
# Author: Aviral Nigam
# SBU ID: 110849584
###########################################

import itertools
from pyspark import SparkContext
from operator import add
import sys

# Initialize the spark context
sc = SparkContext(appName="Frequent Itemset")

# Take filename from command line arguments
# filename = str(sys.argv[1])

# Load file into spark
file = sc.textFile("ratings_Video_Games.csv")
print '*******************************', file.take(2)

# Extract the data and take only unique values
# extract_data = file.map(lambda p : p.split(",")).map(lambda p : (p[1],p[0])).distinct()
