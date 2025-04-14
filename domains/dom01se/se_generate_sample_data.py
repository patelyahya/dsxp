import pandas as pd
import random
import datetime

def generate_code_changes_data():
    data = {
        'commit_id': [f'c_{i+1}' for i in range(100)],
        'lines_added': [random.randint(10, 500) for _ in range(100)],
        'lines_removed': [random.randint(5, 300) for _ in range(100)],
        'files_changed': [random.randint(1, 10) for _ in range(100)],
        'timestamp': [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 100)) for _ in range(100)]
    }
    return pd.DataFrame(data)

def generate_issues_data():
    severity_levels = ['Critical', 'High', 'Medium', 'Low']
    data = {
        'issue_id': [f'i_{i+1}' for i in range(50)],
        'severity': [random.choice(severity_levels) for _ in range(50)],
        'time_to_resolve': [random.randint(1, 30) for _ in range(50)],
        'opened_date': [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 100)) for _ in range(50)],
        'closed': [random.choice([True, False]) for _ in range(50)]
    }
    return pd.DataFrame(data)

def generate_code_reviews_data():
    data = {
        'pr_id': [f'pr_{i+1}' for i in range(40)],
        'review_comments': [random.randint(0, 20) for _ in range(40)],
        'time_to_merge': [random.randint(1, 10) for _ in range(40)],
        'reviewed_by': [f'user_{random.randint(1, 10)}' for _ in range(40)],
        'merged': [random.choice([True, False]) for _ in range(40)]
    }
    return pd.DataFrame(data)

def generate_testing_data():
    data = {
        'test_id': [f't_{i+1}' for i in range(30)],
        'pass_rate': [random.uniform(60.0, 100.0) for _ in range(30)],
        'execution_time': [random.uniform(0.5, 5.0) for _ in range(30)],
        'coverage': [random.uniform(50.0, 100.0) for _ in range(30)]
    }
    return pd.DataFrame(data)

def generate_deployment_data():
    data = {
        'deployment_id': [f'd_{i+1}' for i in range(20)],
        'successful': [random.choice([True, False]) for _ in range(20)],
        'time_taken': [random.randint(5, 60) for _ in range(20)],
        'rollback': [random.choice([True, False]) for _ in range(20)],
        'deployed_at': [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 50)) for _ in range(20)]
    }
    return pd.DataFrame(data)

# Generate and save data
if __name__ == "__main__":
    code_changes_df = generate_code_changes_data()
    code_changes_df.to_csv('sample_data/code_changes.csv', index=False)

    issues_df = generate_issues_data()
    issues_df.to_csv('sample_data/issues.csv', index=False)

    code_reviews_df = generate_code_reviews_data()
    code_reviews_df.to_csv('sample_data/code_reviews.csv', index=False)

    testing_df = generate_testing_data()
    testing_df.to_csv('sample_data/testing.csv', index=False)

    deployment_df = generate_deployment_data()
    deployment_df.to_csv('sample_data/deployment.csv', index=False)

    print("Sample data generated and saved to 'sample_data/' directory.")
