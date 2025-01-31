# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
    .appName("JOB DF READ HIVE") \
    .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
    .config("spark.sql.catalogImplementation", "hive") \
    .enableHiveSupport() \
    .getOrCreate()


# Read Hive table
#df = spark.sql("select * from test2.la_table")
df = spark.sql("select * from test.toto_data_load")
df.show()

# grouping data by groupe
groupDF = spark.sql("SELECT groupe, sum(qte) as qte_vendu from test.toto_data_load group by groupe")
groupDF.show()

# saving data in another tables
# Create Hive Internal table
groupDF.write.mode("append") \
     .saveAsTable("test.toto_group")

# terminal
#./spark-submit /partage/xml_spark/read_hive.py
#./spark-submit --driver-memory 1g --executor-memory 1g --executor-cores 1 /partage/xml_spark/read_hive.py
#./spark-submit --master yarn --driver-memory 1g --executor-memory 1g --executor-cores 1 /partage/xml_spark/read_hive.py
# --py-files file1.py,file2.py,file3.zip, file4.egg \  
   
spark.stop()