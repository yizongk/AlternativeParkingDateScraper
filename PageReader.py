import pandas as grabber

url = "https://www1.nyc.gov/html/dot/html/motorist/alternate-side-parking.shtml"
tables = grabber.read_html(url)

print(tables)
