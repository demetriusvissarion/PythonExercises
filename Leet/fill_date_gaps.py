import json
from datetime import datetime, timedelta

# Function to parse the dates and return the date part only


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ").date()

# Function to find missing dates and fill gaps


def fill_missing_dates(json_response):
    # Parse the JSON response into a list of dictionaries
    data = json.loads(json_response)

    # Sort the data by date
    data.sort(key=lambda x: parse_date(x['date']))

    # Extract only the dates from the data
    dates = [parse_date(item['date']) for item in data]

    # Find the range of dates
    start_date = dates[0]
    end_date = dates[-1]

    # Create a set of all dates in the range
    all_dates = {start_date + timedelta(days=i)
                 for i in range((end_date - start_date).days + 1)}

    # Create a set of existing dates
    existing_dates = set(dates)

    # Find the missing dates
    missing_dates = all_dates - existing_dates

    # Create the missing entries with value = 0
    missing_entries = [{"date": date.isoformat() + "T00:00:00.000Z", "value": 0}
                       for date in missing_dates]

    # Combine the existing data with the missing entries
    full_data = data + missing_entries

    # Sort the full data by date
    full_data.sort(key=lambda x: parse_date(x['date']))

    return full_data


# Example usage
json_response = '''
[
    {"date":"2012-04-23T18:25:43.511Z", "value":25},
    {"date":"2012-04-25T18:25:43.511Z", "value":30}
]
'''

# Fill missing dates
result = fill_missing_dates(json_response)
print(json.dumps(result, indent=4))
