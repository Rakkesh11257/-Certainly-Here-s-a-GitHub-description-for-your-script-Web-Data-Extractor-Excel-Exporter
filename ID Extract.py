import re
from openpyxl import Workbook

# Sample data from the web page
web_data = """

Pass your string copied from web
Example
ID: value1_value2_value3

"""

# Define the pattern to match "ID: value_1_value_2_value_3"
pattern = r"ID:\s([\w\d]+)_([\w\d]+)_([\w\d]+)"

# Find all matches in the web data
matches = re.findall(pattern, web_data)

# Concatenate values with underscores and put them into an Excel sheet
wb = Workbook()
ws = wb.active
ws.title = "Extracted Values"

# Set headers
ws.append(["ID"])

# Add extracted values to the Excel sheet
for match in matches:
    id_value = "_".join(match)
    ws.append([id_value])

# Save the workbook
wb.save("extracted_values.xlsx")