# getCriblLicReport

A script to pull the Cribl usage metrics from the leader node and store the daily values in a CSV file. The script is written to leverage only the libraries available in a standard Python installation. 

## Inputs
The script expects four inputs: leader URL, username, password, and timezone. You can provide these values via prompts when running the script or by hardcoding them at the top of the script. If you hardcode them, uncomment the corresponding lines and set the values.

| Variable | Description | Example |
|---|---|---|
| `criblUrl` | Full URL to the Cribl leader node | `https://leader.example.com:9000` |
| `loginData['username']` | Cribl username | `admin` |
| `loginData['password']` | Cribl password | `thepassword` |
| `reportTimezone` | IANA timezone name for report dates. Leave blank at the prompt to use the system local timezone. | `America/Chicago` |

Common timezone values: `America/New_York`, `America/Chicago`, `America/Denver`, `America/Los_Angeles`, `UTC`.

## Outputs
The script will output the historical daily ingest metrics, which will be stored in a file called leaderhostname-usage.csv.

| Column | Description |
|---|---|
| Date | The date of the usage period (formatted MM-DD-YY) |
| Gigabytes In | Total GB ingested for the day |
| Gigabytes Out | Total GB sent out for the day |
| Cribl2Cribl GB | GB of data exchanged between Cribl instances (exempt from licensing) |
| GB In (C2C Removed) | Licensable GB In — total GB ingested minus the Cribl-to-Cribl exempt bytes |
| Events In | Total number of events ingested for the day |
| Events Out | Total number of events sent out for the day |
