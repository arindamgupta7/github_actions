import json

with open('configs/config_old.json') as f:
    old_data = json.load(f)

with open('configs/config_new.json') as f:
    new_data = json.load(f)

old_dict = {item["key"]: item for item in old_data}
new_dict = {item["key"]: item for item in new_data}

diff_keys = [
    key for key in old_dict
    if key in new_dict and str(old_dict[key].get("value")) != str(new_dict[key].get("value"))
]

print(f"Number of settings with different values: {len(diff_keys)}")
print("Keys with different values:", diff_keys)
