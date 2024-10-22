import csv, datetime, time

with open("rows_300.csv", "w", encoding="utf-8", newline="") as f:
   writer = csv.writer(f)
   writer.writerow(["№", "Sec", "Microsec"])
   for line in range(1,301):
       writer.writerow([line, datetime.datetime.now().second,
                        datetime.datetime.now().microsecond])
       time.sleep(0.01)