# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE EMPLOYEES
# MAGIC   (id int, name string, salary double)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- NOTE: With latest Databricks Runtimes, inserting few records in single transaction is optimized into single data file.
# MAGIC -- For this demo, we will insert the records in multiple transactions in order to create 4 data files.
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES 
# MAGIC   (1, "Adam", 3500.0),
# MAGIC   (2, "Sarah", 4020.5);
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES
# MAGIC   (3, "John", 2999.3),
# MAGIC   (4, "Thomas", 4000.3);
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES
# MAGIC   (5, "Anna", 2500.0);
# MAGIC
# MAGIC INSERT INTO employees
# MAGIC VALUES
# MAGIC   (6, "Kim", 6200.3)
# MAGIC
# MAGIC -- NOTE: When executing multiple SQL statements in the same cell, only the last statement's result will be displayed in the cell output.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees;

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail employees;
# MAGIC

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees'

# COMMAND ----------

# MAGIC %sql
# MAGIC Update employees set salary = salary * 0.1 where name like 'A%'

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees'

# COMMAND ----------

# MAGIC %sql
# MAGIC -- You can still see numFiles = 4
# MAGIC DESCRIBE detail employees

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees;

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employees;

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees/_delta_log'

# COMMAND ----------

# MAGIC %fs head 'dbfs:/user/hive/warehouse/employees/_delta_log/00000000000000000005.json'
