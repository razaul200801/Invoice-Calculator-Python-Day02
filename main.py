
service = input("Enter Service Name: ")
hours = float(input("Enter Number of Hours: "))
hourly_rate = float(input("Enter Hourly Rate: "))
discount_percent = float(input("Enter Discount Percent (%): "))

sub_total = round(hours*hourly_rate, 2)
discount = round(sub_total*(discount_percent)/100, 2)
tax = round((sub_total-discount)*0.10,2) # 10% Tax
total_cost = round((sub_total-discount) + tax, 2)

print()
print("========== Invoice ==========")
print(f"Service Name: {service}")
print(f"Hours: {hours}")
print(f"Hourly Rate: ${hourly_rate}")
print("-----------------------------")
print(f"Sub Total: ${sub_total}")
print(f"Discount: ${discount}")
print(f"Tax (10%): ${tax}")
print("-----------------------------")
print(f"Final Total: ${total_cost}")
print("=============================")

