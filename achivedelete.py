import subprocess
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def delete_archive(vault_name, account_id, archive_id):
    command = f"aws glacier delete-archive --vault-name {vault_name} --account-id {account_id} --archive-id {archive_id}"
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def delete_archives(vault_name, account_id, archive_file):
    with open(archive_file, 'r') as file:
        archive_ids = [line.strip() for line in file]

    total_archives = len(archive_ids)
    print(f"Deleting {total_archives} archives")

    with ThreadPoolExecutor() as executor:
        futures = []
        for archive_id in archive_ids:
            futures.append(executor.submit(delete_archive, vault_name, account_id, archive_id))

        for future in tqdm(futures, total=total_archives):
            future.result()

    print("Deletion complete!")

# Set the vault name, account ID, and archive file path
vault_name = "Replace with your GLACIER VAULT NAME"
account_id = "Replace with your AWS ACCOUNT ID"
archive_file = "Replace with the .txt file that contains list of Archive IDs"

# Check if the archive file exists
if not os.path.isfile(archive_file):
    print(f"Error: The file '{archive_file}' does not exist.")
else:
    delete_archives(vault_name, account_id, archive_file)
