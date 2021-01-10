import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# Salary parsing
df['hourly'] = df['Salary Estimate'].apply(
    lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(
    lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != "-1"]
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

minus_hr = minus_kd.apply(lambda x: x.lower().replace(
    'per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

# Company name parsing
df['company_text'] = df.apply(
    lambda x: x['Company Name'][:-3] if x['Rating'] > 0 else x['Company Name'], axis=1)

# Parse the state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])

# Is job at headquarters?
df['same_state'] = df.apply(
    lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

# Parse company age
df['age'] = df.Founded.apply(lambda x: 2020 - x if x > 1 else x)

# Parse Job Description
df['python_yn'] = df['Job Description'].apply(
    lambda x: 1 if 'python' in x.lower() else 0)
df['r_studio_yn'] = df['Job Description'].apply(
    lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(
    lambda x: 1 if 'spark' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(
    lambda x: 1 if 'aws' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(
    lambda x: 1 if 'excel' in x.lower() else 0)

df = df.drop(df.columns[0], axis=1)
df.to_csv('salary_data_cleaned.csv', index=False)
