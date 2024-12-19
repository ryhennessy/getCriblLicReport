# getCriblLicReport

A script to pull the Cribl usage metrics from the leader node and store the daily values in a csv file. The script is written to only leverage the standard python libraries that should be available with any system with python installed.

## Inputs
The script expects three inputs: leader url, local user name, and password.These values can be provided via prompts from running the script or can be added at the top of the script. You will need to uncomment the lines that set the values.

## Outputs
The script will output the historical daily ingest metrics. This data will be stored in a file called usage.csv. 
