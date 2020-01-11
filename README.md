# SF-Crime-Analysis Project report

## The screenshot of kafka-consumer-console output is following:

![kafka-consumer-console Output Screentshot](https://github.com/johirbuet/SF-Crime-Analysis/blob/master/consumerconsolescreentshot.png "kafka-consumer-console Output")


## The screenshot of Spark UI is given below:
![Spark UI Screentshot](https://github.com/johirbuet/SF-Crime-Analysis/blob/master/screenshotofui.png "Spark UI")

## The screenshot of Stages in Spark UI is given below:
![Spark UI Stages Screentshot](https://github.com/johirbuet/SF-Crime-Analysis/blob/master/sparkstages.png "Spark Stages UI")



## Question 1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

`processedRowsPerSecond` has impact on the throughput. The higher the value of of `processedRowsPerSecond` the higher is the number of rows processed per second increasing throughput. 

## Question 2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
The few important SparkSession proeprty that can help to enhance the `processedRowsPerSecond` are given below:
* `spark.default.parallelism`

* `spark.streaming.kafka.maxRatePerPartition`

* `spark.sql.shuffle.partitions`

To chose optimal value of these we can use some back of the envelope calculation given the resources we have and the target performance we want to achieve. Sometimes empricially observing with different values of these parameters can also help to decide the right values. We can tell whether these values are optimal are not by observing `processedRowsPerSecond`. 
