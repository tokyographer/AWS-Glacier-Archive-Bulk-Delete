# aws-glacier-bulk-delete
Python app that runs on your terminal that bulk deletes AWS Glacier archives in bulk through a Python script that executes multithreading delete tasks. The app will reduce delete time of large archive lists in Glacier reducing delete times.

# About this script
Deleting a Glacier Vault can be a cumbersome process that involves a series of steps on CLI that are required in order to retreive the Vault details and archive IDs. In order for the script to work properly you must follow the next steps.

# Retreiving your Archive IDs requirements.

In order to retreive your Achive IDs you must parse before the IDs from the output.json file obtained after running: 

```aws glacier describe-job --vault-name awsexamplevault --account-id 111122223333 --job-id *** jobid ***```

The job takes several hours to complete. Once you have the output.json file you will have to parse the "ArchiveId" keys and list them in a txt file. The archivedelete.py script will iterate the ids deleting each one by one. The process can last several hours.

You must not close your terminal session otherwise the process will be interrupted.

