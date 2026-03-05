from pyspark.sql.functions import col

# Read raw data
df = spark.read.option("header", True).csv("s3://your-raw-bucket/sales.csv")

# Convert amount to integer
df = df.withColumn("amount", col("amount").cast("int"))

# Validation - remove negative values
df_clean = df.filter(col("amount") > 0)

# Add tax column
df_final = df_clean.withColumn("amount_with_tax", col("amount") * 1.18)

# Write to Delta
df_final.write.format("delta") \
    .mode("overwrite") \
    .save("s3://your-processed-bucket/sales_delta")

print("ETL Job Completed Successfully")
