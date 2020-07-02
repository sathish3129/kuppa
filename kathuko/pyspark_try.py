from pyspark import SparkContext

textFile = sc.textFile("/user/hive/interview/EmployeeInfo.csv").map(lambda line: line.split(","))
# df