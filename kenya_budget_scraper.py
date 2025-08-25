import pandas as pd

def fetch_budget_data():
    url = (
        "https://open.africa/dataset/9a9c52b6-65f6-4483-890f-3a34bb164ce2/"
        "resource/217fae3d-6987-4c56-93a2-e11ae473e18e/download/"
        "county-governments-budget-allocation-fy-2017_18.csv"
    )
    df = pd.read_csv(url)
    df.to_csv("kenya_budget_2017_18.csv", index=False)
    print("Saved dataset to 'kenya_budget_2017_18.csv'.")
    return df

if __name__ == "__main__":
    df = fetch_budget_data()
    print(df.head())
