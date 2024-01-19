import shutil
import os

# Define the source file path and the directory for the copies
source_file = 'jaffle_shop/models/customers.sql'  # Replace with your source file path
destination_dir = 'jaffle_shop/models'  # Replace with your desired destination directory

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Copy the file 50 times
for i in range(51, 101):
    # Define a new filename for each copy
    new_file = os.path.join(destination_dir, f'customers_{i+1}.sql')  # Replace 'ext'
    shutil.copy(source_file, new_file)
