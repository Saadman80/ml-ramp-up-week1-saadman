import kagglehub
from kagglehub import KaggleDatasetAdapter

# Load dataset
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "uciml/iris",
    "Iris.csv"
)

# Save to local CSV
df.to_csv("iris_dataset.csv", index=False)

print("Dataset saved successfully!")