# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("local[2]") \
      .appName("JOB DF") \
      .getOrCreate() 

from pyspark.sql.types import *
#df = spark.read.option("header", True).csv(r"C:\Users\ngoun\Documents\dev_ops_all\bigdata_env\nifi\datas\quincaillerie_20240320104912.csv")
df = spark.read.option("header", True).option("inferSchema" , "true").csv(r"C:\Users\ngoun\Documents\dev_ops_all\bigdata_env\nifi\datas\*.csv")
df.show()

# using spark sql
df.createOrReplaceTempView("VENTE_DATA")
groupDF = spark.sql("SELECT code_produit, sum(qte) as qte_vendu from VENTE_DATA group by code_produit")
groupDF.show()

# copy from a folder to another
import os
import shutil

# source and destination Folder
source_folder = r"C:\Users\ngoun\Documents\dev_ops_all\bigdata_env\nifi\datas"
destination_folder = r"C:\Users\ngoun\Documents\dev_ops_all\bigdata_env\nifi\archives"

# all files in source folder
files = os.listdir(source_folder)

# Iterate source file and copy one by one to destination_folder
for file in files:
    if file.endswith(".csv"):  # Check CSV file
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.copy(source_path, destination_path) # copy

# Move the file
# shutil.copy(source_path, destination_path)

# terminal
#spark-submit2 C:\Users\ngoun\Documents\dev_ops_all\hadoop\codes\first.py
#spark-submit2 --driver-memory 1g --executor-memory 1g --executor-cores 1 C:\Users\ngoun\Documents\dev_ops_all\hadoop\codes\first.py
# --py-files file1.py,file2.py,file3.zip, file4.egg \  
   
spark.stop()