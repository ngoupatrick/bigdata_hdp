# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("yarn") \
      .appName("JOB DF READ") \
      .getOrCreate() 

#from pyspark.sql.types import *
df = spark.read.text("hdfs://namenode:9000/test/toto.txt")
df.show()

# calcul sur le dataframe
# df....
# terminal
# cd /spark/bin
#./spark-submit /partage/xml_spark/read_text.py
#./spark-submit  --master yarn --driver-memory 1g --executor-memory 1g --executor-cores 1 /partage/xml_spark/read_text.py
#./spark-submit --master yarn --driver-memory 1g --executor-memory 1g --executor-cores 1 /partage/xml_spark/read_text.py
# --py-files file1.py,file2.py,file3.zip, file4.egg \  
   
spark.stop()