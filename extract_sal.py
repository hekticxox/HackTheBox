import zipfile

# Path to the .sal file
sal_file = "hw_debug.sal"

# Attempt to extract the file if it's a ZIP archive
try:
    with zipfile.ZipFile(sal_file, 'r') as zip_ref:
        zip_ref.extractall("extracted_sal")
        print("Extraction successful! Files are in 'extracted_sal' directory.")
except zipfile.BadZipFile:
    print("The .sal file is not a valid ZIP archive.")