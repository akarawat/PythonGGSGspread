from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pprint

'''
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1p0vKYQW5iaw0VVGWK1AYtypUBigpTrBcwDFDP_V-AIo/edit#gid=0")
worksheet = sheet.get_worksheet(0)
results = worksheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(results)
'''
import gspread

scope = ['https://www.googleapis.com/auth/spreadsheets']
gc = gspread.service_account('credentials.json', scope)

# Open a sheet from a spreadsheet in one go
#wks = gc.open("Where is the money Lebowski?").sheet1
wks = client.open_by_url("https://docs.google.com/spreadsheets/d/1p0vKYQW5iaw0VVGWK1AYtypUBigpTrBcwDFDP_V-AIo/edit#gid=0").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[1, 2], [3, 4]])

# Or update a single cell
wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})

'''
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("https://docs.google.com/spreadsheets/d/1p0vKYQW5iaw0VVGWK1AYtypUBigpTrBcwDFDP_V-AIo/edit#gid=0").sheet1  # Open the spreadhseet
#sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1p0vKYQW5iaw0VVGWK1AYtypUBigpTrBcwDFDP_V-AIo/edit#gid=0").sheet1

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

#insertRow = ["hello", 5, "red", "blue"]
#sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

sheet.update_cell(2,2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet
'''