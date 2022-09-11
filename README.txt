Requirements: Python 3.7.12
              pandas 1.3.5
	      matplotlib 3.5.1

TECH-ASSESSMENT for EonLabs - Data Representation


The following script data_rep.py utilizes monthly_data.csv, weekly_data.csv, and hourly_data.csv to produce hourly_df_2017_to_present.csv
    containing hourly data normalized under min-max normalization between values 0 and 100 in the the time window from 
    2017 to present (Sept. 1, 2022). A plot of the results is also generated as hourly_df_plot.png. The output files are saved under the folder
    /output.


Notes:  monthly_data appears to be normalized according to min-max normalization with min=6 and max=100, from 2017 til present
        weekly_data appears to be normalized according to min-max normalization with min=7 and max=100, for each month
        hourly_data appears to be normalized according to min-max normalization with min=0 and max=100, for each week


To make our data consistent, we simply multiply the value of each hour by the value of the week that it is in, 
    multiplied by the value of the month that it is in. Finally we can normalize this data to be within the 
    range of 0 and 100. The output csv is saved in the same format as hourly_data, the only difference being that
    it is normalized between 2017 and present, instead of weekly.