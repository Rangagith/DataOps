from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    ("ProductA", 100),
    ("ProductB", 200),
    ("ProductC", 300)
]

df = spark.createDataFrame(data, ["product", "sales"])

df.show()

df.write.mode("overwrite").format("delta").save("/tmp/sales_data")

print("ETL Job Completed Successfully")
