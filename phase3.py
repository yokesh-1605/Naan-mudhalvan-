
# quality_control.py

def check_product(width, height, weight):
    if 9.5 <= width <= 10.5 and 19.5 <= height <= 20.5 and 95 <= weight <= 105:
        return "PASS"
    else:
        return "FAIL"

products = [
    {"id": 1, "width": 10.0, "height": 20.0, "weight": 100},
    {"id": 2, "width": 9.2, "height": 20.1, "weight": 96},
    {"id": 3, "width": 10.3, "height": 21.0, "weight": 99}
]

for p in products:
    result = check_product(p["width"], p["height"], p["weight"])
    print(f"Product {p['id']} - {result}")
