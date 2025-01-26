import csv
import gspread
from google.oauth2.service_account import Credentials
import time

MONTH = 'dec'

file = f'stmt_{MONTH}.csv'

transactions = []

def stmtFin(file):
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[1]
            amount = float(row[2])
            total = float(row[3])
            transaction = ((date, name, amount, total))
            transactions.append(transaction)
        return transactions

def total(file):
    sum = 0
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            amount = float(row[2])
            sum += amount
        return sum


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("Credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1wxPpxoBYeu5sriM7L_B6s6kWJl1Vj-wvbOMCrMrAwsY"
sheet = client.open_by_key(sheet_id)

wks = sheet.worksheet("Dec")

rows = stmtFin(file)
sum = total(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[2], row[3]],2)
    time.sleep(2)


wks.insert_row([f'Over/Under this month: {float(sum)}'],30)