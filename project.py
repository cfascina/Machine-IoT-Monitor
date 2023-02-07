# %%
import findspark
import os

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.sql.functions import col, from_json

# %%
findspark.init()

# %%
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 pyspark-shell'

# %%
spark = SparkSession.builder.appName('MachineSensorsMonitor').getOrCreate()

# %%
df = spark \
    .readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', 'localhost:9092') \
    .option('subscribe', 'sensors-data') \
    .load()

# %%
sensor_data = \
    StructType([
        StructField('temperature', DoubleType(), True),
        StructField('rpm', IntegerType(), True)
    ])

# %%
message_schema = \
    StructType([ 
        StructField('timestamp', StringType(), True), 
        StructField('id_machine', StringType(), True), 
        StructField('sensor-data', sensor_data, True)
    ])

# %%
df = df.selectExpr('CAST(value AS STRING)')

# %%
df = df.withColumn('jsonData', from_json(col('value'), message_schema)).select('jsonData.*')

# %%
df.printSchema()