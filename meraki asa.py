import pandas as pd

# Load the uploaded dataset
file_path = '/mnt/data/mental_health_diagnosis_treatment_.csv'
data = pd.read_csv(file_path)

# Display the first few rows and basic info of the dataset
data_info = data.info()
data_head = data.head()

data_info, data_head
