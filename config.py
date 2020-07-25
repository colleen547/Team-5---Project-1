import os

# output csv path
cleaned_csv = "US_Accidents_Cleaned.csv"
# output zip path
destination_zip = os.path.join("Resources", "US_Accidents.zip")

# column names and data types
col_types = {'ID': 'str', 
             'Severity': 'int8', 
             'Start_Time': 'str', 
             'Start_Lat': 'float32', 
             'Start_Lng': 'float32', 
             'City': 'str', 
             'County': 'str', 
             'State': 'category', 
             'Zipcode': 'str', 
             'Sunrise_Sunset': 'category'}