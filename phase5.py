import random
import time
from datetime import datetime
import csv

# Expected ranges
WEIGHT_RANGE = (95, 105)        # grams
TEMP_RANGE = (18, 22)           # °C

# Logs
product_log = []
defect_log = []

# Simulate weight and temperature reading
def get_weight():
    return round(random.uniform(90, 110), 2)

def get_temperature():
    return round(random.uniform(15, 25), 2)

# Inspection function
def inspect_products(n=8):
    for i in range(n):
        weight = get_weight()
        temp = get_temperature()
        status = "PASS"

        if not (WEIGHT_RANGE[0] <= weight <= WEIGHT_RANGE[1]):
            status = "FAIL (Weight)"
        if not (TEMP_RANGE[0] <= temp <= TEMP_RANGE[1]):
            status = "FAIL (Temp)" if status == "PASS" else "FAIL (Weight & Temp)"

        product_log.append({
            'Time': datetime.now().strftime("%H:%M:%S"),
            'Product': i + 1,
            'Weight (g)': weight,
            'Temperature (°C)': temp,
            'Status': status
        })

        if "FAIL" in status:
            defect_log.append(product_log[-1])

        print(f"Product {i+1}: Weight = {weight}g, Temp = {temp}°C => {status}")
        time.sleep(0.2)

    # Save to CSV
    with open('inspection_log.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=product_log[0].keys())
        writer.writeheader()
        writer.writerows(product_log)

    # Display summary
    print(f"\nTotal Products Checked: {len(product_log)}")
    print(f"Defective Products: {len(defect_log)}")

# Run inspection
if __name__ == "__main__":
    inspect_products()
