import data_scrapper as ds

driver_path = "./chromedriver"

df = ds.get_jobs('data scientist', 1000, driver_path, 15, False)
df.to_csv('glassdoor_jobs.csv', index=False)
