# Databricks notebook source
print("hey")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC Paragraphs:
# MAGIC <p><b>This is a simple html paragraph </b> </p>
# MAGIC
# MAGIC Tables:
# MAGIC | Column 1 | Column 2 | Column 3 |
# MAGIC |----------|----------|----------|
# MAGIC | Value 1  | Value 2  | Value 3  |
# MAGIC | Value 4  | Value 5  | Value 6  |
# MAGIC | Value 7  | Value 8  | Value 9  |
# MAGIC
# MAGIC Lists:
# MAGIC 1. Furkhan shaikh
# MAGIC 2. Rehan shaikh
# MAGIC 3. Misbah shaikh
# MAGIC 4. Faisal shaikh
# MAGIC
# MAGIC * Faisal shaikh
# MAGIC * Furkhan shaikh
# MAGIC
# MAGIC Images:
# MAGIC ![Tajmahal](https://th.bing.com/th/id/R.346f7e430f383ab85353bd8677c7ab3a?rik=OMN1B2EtGNVe8Q&riu=http%3a%2f%2fwww.transindiatravels.com%2fwp-content%2fuploads%2fthe-taj-mahal-agra.jpg&ehk=To420bIyh5Hzdgl6NHAuPQXLx5OGWSHKbqDvIeEimYw%3d&risl=&pid=ImgRaw&r=0)
# MAGIC

# COMMAND ----------

# MAGIC %run ./demo_notebook_target

# COMMAND ----------

# Confirm if the variable from target notebook is configured.
print(msg)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

list_of_files = dbutils.fs.ls("databricks-datasets")
# This display() function prints output in a pretty format.
display(list_of_files)

# COMMAND ----------


