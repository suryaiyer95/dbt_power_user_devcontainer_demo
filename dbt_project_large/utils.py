import shutil
import os
import yaml

# Define the path of the original jaffle_shop folder
original_folder = 'jaffle_shop'

# Loop to create 50 copies
for i in range(51, 100):
    # Create new folder name
    new_folder = f'jaffle_shop_{i}'
    # Copy the original folder to the new folder
    shutil.copytree(original_folder, new_folder)

    # Path to the dbt_project.yml file in the new folder
    yaml_file_path = os.path.join(new_folder, 'dbt_project.yml')

    # Read the YAML file
    with open(yaml_file_path, 'r') as file:
        yaml_content = yaml.safe_load(file)

    # Update the name field
    yaml_content['name'] = f'jaffle_shop{i}'

    # Write the updated YAML back to the file
    with open(yaml_file_path, 'w') as file:
        yaml.dump(yaml_content, file)

    print(f'Updated folder {new_folder}')
