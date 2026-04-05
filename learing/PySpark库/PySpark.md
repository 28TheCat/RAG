1. 什么是 Spark 和 PySpark？Spark (Apache Spark)Spark 是一个开源的分布式计算框架。它的核心特点是基于内存计算，比传统的 MapReduce 快得多。它主要用于大规模数据的并行处理。PySparkPySpark 是 Spark 提供的 Python 语言 API。为什么用 PySpark？ Spark 本身是用 Scala 编写的，运行在 JVM（Java 虚拟机）上。PySpark 允许 Python 开发者利用 Python 简洁的语法，调用 Spark 的分布式计算能力。Python on Spark: 实际上是 Python 进程通过 Py4J 库与 JVM 通信，从而驱动集群中的 Executor 进行计算。2. 环境安装在 Python 虚拟环境（如你的 .venv）中，通过 pip 即可安装：Bashpip install pyspark
注：由于 Spark 依赖 Java，请确保你的电脑已安装 JDK 8 或 11。3. 构建执行环境入口对象在 PySpark 中，一切计算的起点都是 SparkContext（基础 RDD 编程）或 SparkSession（现代 SQL/DataFrame 编程）。Pythonfrom pyspark import SparkConf, SparkContext

# 1. 创建配置对象
conf = SparkConf().setAppName("My_Spark_App").setMaster("local[*]")

# 2. 构建入口对象 SparkContext
sc = SparkContext(conf=conf)

# ... 进行计算 ...

# 3. 停止运行
sc.stop()
4. PySpark 编程模型：RDD什么是 RDD (Resilient Distributed Dataset)？RDD（弹性分布式数据集）是 Spark 的基本抽象。你可以把它理解为一个存储在集群多个节点上的大型 List。核心流程：数据输入：将物理数据（文件、List）转成 RDD。数据计算：对 RDD 进行各种转换操作，返回的依然是 RDD。数据输出：将 RDD 转回 Python 对象或保存到文件。5. 数据输入：容器转 RDD你可以将 Python 的内置容器（List, Tuple, Set, Dict）转换成 Spark 能够处理的 RDD 对象。原始数据类型转换方法示例Listsc.parallelize(list)sc.parallelize([1, 2, 3])Tuplesc.parallelize(tuple)sc.parallelize((1, 2, 3))Setsc.parallelize(set)sc.parallelize({1, 2, 3})Dictsc.parallelize(dict)默认转换 Key：sc.parallelize({"a":1}).collect() -> ['a']6. 数据计算方法 (算子)RDD 的计算分为两类：Transformation（转换算子） 和 Action（动作算子）。A. 转换算子 (Transformation)这些方法返回的依旧是 RDD 对象。它们是“惰性”的，只有遇到 Action 时才会真正执行。map(func): 对每一条数据进行处理。flatMap(func): 解嵌套处理（如：一行句子切分成多个单词）。filter(func): 过滤数据。distinct(): 去重。B. 动作算子 (Action)这些方法执行计算并返回非 RDD 对象（如 List、数值或保存文件）。collect(): 将 RDD 变成 Python 的 List。reduce(func): 聚合计算（如求和）。count(): 统计元素个数。saveAsTextFile(path): 保存为文本文件。7. 完整代码示例Pythonfrom pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("PikachuCounter")
sc = SparkContext(conf=conf)

# 1. 源数据 (List) -> RDD
data_list = ["pikaqiu pikaqiu spark", "hello python pikaqiu"]
rdd = sc.parallelize(data_list)

# 2. RDD 迭代计算 (链式调用)
result_rdd = rdd.flatMap(lambda x: x.split(" ")) \
                .filter(lambda x: x == "pikaqiu") \
                .map(lambda x: (x, 1))

# 3. 结果输出 -> 转成 List
final_list = result_rdd.collect()
print(f"计算结果: {final_list}")

sc.stop()