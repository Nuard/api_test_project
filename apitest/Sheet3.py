import openpyxl


# Location of the file
path = 'C:/Users/melikyan.tatevik/Documents/Megafeed/Soccer-old.xlsx'

# To open the workbook
wb = openpyxl.load_workbook(path)

# Get workbook active sheet
sheet = wb.active

wb.title = "Sheet3"

# Rows to lists
row_list2 = [row for row in sheet.values]
#print(row_list2)

list_of_lists2 = [list(elem) for elem in row_list2]
print(list_of_lists2)

for item in list_of_lists2:
    if item[3] == None:
        item[3] = ''

for item in list_of_lists2:
    if item[4] == None:
        item[4] = ''