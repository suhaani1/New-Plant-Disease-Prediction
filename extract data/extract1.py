import os
import zipfile
import logging

# Setup logging
log_file = "extraction_errors.log"
logging.basicConfig(
    filename=log_file,
    filemode='w',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Path to your ZIP file (Update as needed)
zip_path = r'D:\SHIVANI\INTERNSHIP\EDUNET\10\datasets\New_Plant _Diseases_Dataset.zip'

# Set a shorter extraction path to avoid path length issues
extract_to = "C:/tmp/plant_disease_dataset"
os.makedirs(extract_to, exist_ok=True)

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        print(f"Extracting {len(zip_ref.infolist())} files to '{extract_to}'...")

        for member in zip_ref.infolist():
            try:
                zip_ref.extract(member, extract_to)
            except Exception as e:
                logging.error(f"Failed to extract: {member.filename} - Error: {e}")
                print(f"Skipped: {member.filename}")

        print("✅ Extraction completed (check log for any skipped files).")

except FileNotFoundError:
    logging.error(f"Zip file not found: {zip_path}")
    print(f"❌ ERROR: The zip file '{zip_path}' was not found.")
except zipfile.BadZipFile:
    logging.error("Invalid or corrupted ZIP file.")
    print("❌ ERROR: The ZIP file is corrupted or invalid.")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    print(f"❌ Unexpected error: {e}")
