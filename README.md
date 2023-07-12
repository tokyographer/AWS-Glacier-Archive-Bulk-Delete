# AWS Glacier Bulk Delete
This Python script runs on your terminal and bulk deletes AWS Glacier archives in bulk by iterating through your vault Archive IDs. This Python script executes multithreading delete tasks using the concurrent.futures module which provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.. The app will reduce delete time of large archive lists in Glacier reducing delete times.

# About this script
Deleting a Glacier Vault can be a cumbersome process that involves a series of steps on CLI that are required in order to retreive the Vault details and archive IDs. In order for the script to work properly you must follow the next steps.

# Retreiving your Archive IDs requirements.

In order to retreive your Achive IDs you must follow a number of aws cli commands. These are the commands:

1. aws glacier list-vaults --account-id 123456789012
2. aws configure list
3. aws glacier initiate-job --vault-name awsexamplevault --account-id 111122223333 --job-parameters "{\"Type\":\"inventory-retrieval\"}"
4. aws glacier describe-job --vault-name awsexamplevault --account-id 111122223333 --job-id *** jobid ***
5. aws glacier get-job-output --vault-name awsexamplevault --account-id 111122223333 --job-id *** jobid *** output.json

From the obtained output.json file from step 5 you must parse the "ArchiveId" keys and list them in a txt file. The archivedelete.py script will iterate the ids deleting each one by one. The process can last several hours.

You must not close your terminal session otherwise the process will be interrupted.

