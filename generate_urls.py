import datetime

# Define start and end dates
start_date = datetime.date(2000, 1, 4)
end_date = datetime.date(2023, 3, 14)

# Define the URL format string
url_template = 'https://droughtmonitor.unl.edu/data/png/{date}/{date}_usdm.png'

# Define the output file name
output_file = 'urls.txt'

# Open the file for writing
with open(output_file, 'w') as f:
    # Loop over dates in 7-day increments
    delta = datetime.timedelta(days=7)
    d = start_date
    while d <= end_date:
        # Format the URL for the current date
        url = url_template.format(date=d.strftime('%Y%m%d'))
        # Write the URL to the file
        f.write(url + '\n')
        # Increment the date
        d += delta
