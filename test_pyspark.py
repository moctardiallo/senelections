from pyspark.sql import SparkSession

if __name__ == "__main__":
    logFile = "./test_text_file.md"
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    logData = spark.read.text(logFile).cache()
    numAs = logData.filter(logData.value.contains("a")).count()
    numBs = logData.filter(logData.value.contains("b")).count()
    print("numRows:", logData.count())
    print("numAs:", numAs)
    print("numBs:", numBs)
