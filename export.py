import shutil
from pathlib import Path

# Define the base directories
datapacks_dir = Path("./datapacks")
resourcepacks_dir = Path("./resourcepacks")
out_dir = Path("./out")

# Ensure the output directory exists
out_dir.mkdir(parents=True, exist_ok=True)

def zip_subfolders(base_dir, output_subdir):
    """
    Zips subfolders of the given base directory into the specified output subdirectory.
    """
    for folder in base_dir.iterdir():
        if folder.is_dir():
            # Get the name of the folder
            folder_name = folder.name
            # Define the subfolder to zip (e.g., ./datapacks/<name>/<name>)
            subfolder_to_zip = folder / folder_name
            if subfolder_to_zip.exists() and subfolder_to_zip.is_dir():
                # Define the output zip file path
                output_zip = out_dir / output_subdir / f"{folder_name}.zip"
                # Ensure the output subdirectory exists
                output_zip.parent.mkdir(parents=True, exist_ok=True)
                # Zip the subfolder
                shutil.make_archive(str(output_zip.with_suffix('')), 'zip', subfolder_to_zip)
                print(f"Zipped: {folder} -> {output_zip}")
            else:
                print(f"Skipping {folder}: Subfolder {folder_name} does not exist or is not a directory.")

# Process datapacks
zip_subfolders(datapacks_dir, "datapacks")

# Process resourcepacks
zip_subfolders(resourcepacks_dir, "resourcepacks")

print("All folders processed.")