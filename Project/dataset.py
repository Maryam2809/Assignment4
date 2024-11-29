import kagglehub
kagglehub.login()
# Download latest version
path = kagglehub.dataset_download("elvinrustam/books-dataset")

print("Path to dataset files:", path)
