import data_scrapper as ds
import pandas as pd

driver_path = "./chromedriver"

df = ds.get_jobs('data scientist', 1000, driver_path, 10, False)
df.to_csv('glassdoor_jobs.csv', index=False)
