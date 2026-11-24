# Databricks notebook source
data = [
    (1, "Dubai", "UAE"),
    (2, "Abu Dhabi", "UAE"),
    (3, "Mumbai", "India"),
    (4, "Bengaluru", "India"),
    (5, "Hyderabad", "India"),
]

df = spark.createDataFrame(data, ["id", "city", "country"])
display(df)

# COMMAND ----------

from pyspark.sql import functions as F

result = (
    df.groupBy("country")
      .agg(F.count("*").alias("total_cities"))
      .orderBy(F.desc("total_cities"))
)

display(result)

# COMMAND ----------

df.createOrReplaceTempView("cities")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT country, COUNT(*) AS total_cities
# MAGIC FROM cities
# MAGIC GROUP BY country
# MAGIC ORDER BY total_cities DESC

# COMMAND ----------

result_sql = spark.sql("""
    SELECT country, COUNT(*) AS total_cities
    FROM cities
    GROUP BY country
    ORDER BY total_cities DESC
""")
display(result_sql)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.default
# MAGIC

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("workspace.default.cities")

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO workspace.default.cities VALUES
# MAGIC   (6, 'Sharjah', 'UAE'),
# MAGIC   (7, 'Chennai', 'India')

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM workspace.default.cities WHERE city = 'Mumbai'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.cities ORDER BY id

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY workspace.default.cities

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.cities VERSION AS OF 0 ORDER BY id

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.cities VERSION AS OF 1 ORDER BY id

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.cities ORDER BY id

# COMMAND ----------

# MAGIC %sql
# MAGIC RESTORE TABLE workspace.default.cities TO VERSION AS OF 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.cities ORDER BY id

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY workspace.default.cities