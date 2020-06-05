from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pprint


scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
#sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1p0vKYQW5iaw0VVGWK1AYtypUBigpTrBcwDFDP_V-AIo/edit#gid=0")
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1fZWmkOpeB3WZxwC1ejKEcStWRPMftR9aEuhIbVkmRl8/edit#gid=1996831855")

#worksheet = sheet.get_worksheet(0) #Get By ID
worksheet = sheet.worksheet("Parts board") #Get By Title
#worksheet.update('B5', [["ABCD", "ฟหกด"], ["FF", "GG"]])
#worksheet.update('B5', [["ABCD", "ฟหกด"]])

# worksheet.format('B5', {'textFormat': {'bold': True}})

#results = worksheet.get_all_records()
results = worksheet.acell('D6').value
pp = pprint.PrettyPrinter()
pp.pprint(results)
