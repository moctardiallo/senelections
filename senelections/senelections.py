from pyspark.sql import SparkSession

if __name__ == "__main__":

    spark = SparkSession.builder.appName("SenElections").getOrCreate()

    sample = "csv/SAMPLE.csv"

    df = spark.read.csv(sample, sep=";", header=True)

    df.show()

    print(df.count())
