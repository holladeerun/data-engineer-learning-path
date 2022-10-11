# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

lesson_config = LessonConfig(name = None,
                             create_schema = True,
                             create_catalog = False,
                             requires_uc = False,
                             installing_datasets = True,
                             enable_streaming_support = False)

DA = DBAcademyHelper(course_config=course_config,
                     lesson_config=lesson_config)
DA.reset_lesson()
DA.init()

DA.paths.kafka_events = f"{DA.paths.datasets}/ecommerce/raw/events-kafka"

spark.sql(f"""
CREATE TABLE IF NOT EXISTS events_json
  (key BINARY, offset BIGINT, partition INT, timestamp BIGINT, topic STRING, value BINARY)
USING JSON 
OPTIONS (path = "{DA.paths.kafka_events}")
""")

DA.conclude_setup()

