# Apache Spark

### 1. WordCount from local file "SampleFileWordCount.txt" </br>
Set PATH to spark-submit.</br>
Open location of your project in cmd and enter 
``` 
>> spark-submit wordCount.py
```
### 2. Contextual Word Count in Spark (using AWS EMR)</br>
* Objective: Create Spark program to count what people “feel”</br>
  * Input: First 5,000 1,000 “WET” files from the Common Crawl September 2016</br>
  * Output: Count of words that appear after the string  “I feel”</br>
    * your code should be case insensitive (convert strings to lowercase)
    * “I feel” can appear anywhere and you should only count the one single word appearing after it (this will mean many common words that aren’t “feelings” will also be included; i.e. “that”, “the”, etc…).
* Create spark code to achieve output from above
   * The wet-paths.gz file linked to above lists the path to files containing just the text of web-page (i.e. ready for directly reading in for distributed IO). 
  * (optional) Test on your own system with a local Spark on approximately 5 downloaded wet files (no need to download more; you will use the remaining files directly through aws).  
* Launch an EMR Spark Instance:
  * Step 1. Make sure you’re feeling good about your Spark code because once you launch the EMR instance (as per next steps) you will start losing credits. 
  * Step 2. Login to: https://console.aws.amazon.com
  * Step 3. Navigate to EMR Service Page</br>
Click on “Services” at the top, then EMR
  * Step 4. Configure your cluster</br>
Use Default settings, except:
    * Under “Applications”, choose “Spark: ...”
    * Under “Number of Instances”, choose at least 7
    (consult pricing if choosing more)
    * Under EC2 Key pair add a pair a that you plan to use 
    (follow “learn how to create EC2 key pair”)
  * Step 5.  Create a screen shot of the EMR console page showing that you have a cluster running. 
* Migrate your code to your EMR Spark Cluster
    * Connect to your master node via ssh. 
    * Test your code in your respective language on limited sample
(consider the spark or pyspark shell)
    * Access the data through S3 
(e.g. s3://commoncrawl/crawl-data/CC-MAIN-2016-40/wet.paths.gz)
    * Run your code on the full sample: first 5,000 1,000 wet files
      * Running on the first 5,000 is worth 5 points extra credit. 
(make sure to note this clearly in your output file submission)
    * Filter your results to just those words occurring at least 30 times
(this can be done inside or outside Spark) 
      * Save these as a list of tuples: (word, count)
  * Once completed, make sure you have saved the code to your local machine and terminate the cluster instance from the  EMR console page so you stop losing credits. 
