import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

def main():
    app_name = os.getenv("SPARK_APP_NAME", "lab8-batch-infer")
    spark = (SparkSession.builder.appName(app_name).getOrCreate())

    df = spark.range(0, 10).withColumn("note", lit("hello lab8"))
    df.show(truncate=False)

    out = os.getenv("OUTPUT_PATH", "/tmp/lab8_out")
    df.coalesce(1).write.mode("overwrite").json(out)
    print(f"Saved output to: {out}")

    spark.stop()

if __name__ == "__main__":
    main()

