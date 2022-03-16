import os
from shutil import move

folder = r"C:\Users\viana\\Downloads"

xlsx = (".xlsx", ".XLSX")
csv = (".csv", ".CSV")
json = (".json", ".JSON")
pdf = (".pdf", ".PDF")

reportes = [
    "Datastore Performance", "Cluster Performance", "Oversized VMs", "Host Configuration", "Host Performance", "Backups on Repository",
    "Protected VMs", "Capacity Planning", "Latest Job Status", "Backup Inventory", "VMs Growth"
    ]

files = [ f.path for f in os.scandir(folder) if f.is_file() ]

for file in files:
    for chequeo in reportes:
        if chequeo in file:
            move(file, r"C:\Users\viana\Documents\infrastructure\Reports")
            files.remove(file)
            break
    if file.endswith(xlsx):
        move(file, r"C:\Users\viana\Downloads\xlsx")
    elif file.endswith(csv):
        move(file, r"C:\Users\viana\Downloads\csv")
    elif file.endswith(json):
        move(file, r"C:\Users\viana\Downloads\json")
    elif file.endswith(pdf):
        move(file, r"C:\Users\viana\Downloads\pdf")