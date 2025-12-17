import csv

gold_rate = float(input("Enter today's gold rate per gram: "))
gold_weight = float(input("Enter gold weight in grams: "))

wastage = 0
making_charges = 0

file = open("gold_slabs.csv", "r")
reader = csv.DictReader(file)

for row in reader:
    start = float(row["Weight_From"])
    end = float(row["Weight_To"])

    
    if gold_weight >= start and gold_weight <= end:
        wastage = float(row["Wastage"])
        making_charges = float(row["Making_Charges"])
        break

file.close()

total_price = ((gold_weight + wastage) * gold_rate) + making_charges

print("\n----- GOLD BILL -----")
print("Gold Weight:", gold_weight, "g")
print("Wastage:", wastage, "g")
print("Making Charges: ₹", making_charges)
print("Total Price: ₹", total_price)
