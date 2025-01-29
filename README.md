# getCriblLicReport

A script to pull the Cribl usage metrics from the leader node and store the daily values in a CSV file. The script is written to leverage only the libraries available in a standard Python installation. 

## Inputs
The script expects three inputs: leader URL, local user name, and password. You can provide these values via prompts when running the script or by adding them at the top of the script. If you provide the values at the top of the script, you must uncomment the lines that set the variables.

## Outputs
The script will output the historical daily ingest metrics, which will be stored in a file called usage.csv.
