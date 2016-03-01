#PyBS Accounting
A simple script for PBS log accounting.

### Usage

Specify either a combination of years, months, and days or a user, or use the --all flag.

### Flags

| Short 	| Long          	| Description                              	|
|-------	|---------------	|------------------------------------------	|
| -y    	| --year         	| list of years to analyze                	|
| -m    	| --month        	| list of months to analyze                	|
| -d    	| --day         	| list of days to analyze                 	|
| -A    	| --all         	| use all log files                       	|
| -u    	| --user         	| list of users to analyze                 	|
| -h    	| --help        	| help I need somebody                     	| 

### TODO

- ~~implement user cmd line argument parsing and validation~~
- ~~file name generation from cmd line args~~
- actually process logs
  - ~~number of unique users~~
    - per year/month/date
  - number of jobs by user
    - per year/month/date
  - number of jobs
    - per year/month/date
  - resource utilization
    - per year/month/date
- establish default level of log processing
- establish additional flags for varying degrees of processing
- visualization
