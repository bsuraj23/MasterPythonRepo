# Example 1: Write sample DB rows to file
data = [("Alice", 25), ("Bob", 30)]
with open("db_dump.txt", "w") as f:
    for name, age in data:
        f.write(f"{name},{age}\n")

# Example 2: Convert SQL result to CSV
result = [("ID", "Name"), (1, "Tom"), (2, "Jerry")]
with open("result.csv", "w") as f:
    for row in result:
        f.write(",".join(map(str, row)) + "\n")

# Example 3: Dumping DB rows in JSON format
import json
data = [{"name": "Alice"}, {"name": "Bob"}]
with open("db.json", "w") as f:
    json.dump(data, f)

# Example 4: Saving SQL rows as text
rows = [("ProductA", 100), ("ProductB", 200)]
with open("products.txt", "w") as f:
    for prod, price in rows:
        f.write(f"{prod} - {price}\n")

# Example 5: Logging DB actions to file
with open("db_log.txt", "a") as f:
    f.write("Database connection established\n")
