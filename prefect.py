from prefect import flow, task
import subprocess

@task(log_prints=True)
def create_fake_data():
    print("Executando o script...")
    result = subprocess.run(['python', 'fake_data_generator.py'], capture_output=True, text=True)
    print(result.stdout)

@flow(name="Fake Data Generator")
def fake_data_generator():
    create_fake_data()

# This is the entry point for the Prefect flow
if __name__ == "__main__":
    fake_data_generator.serve(name="first-deployment", cron=("* * * * *"))