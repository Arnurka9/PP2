import json 

with open("sample-data.json", "r") as file:
    data = json.load(file)

main_data = data["imdata"]


print()
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 50, "-" * 19, "" , "-" * 6, "-" * 6 )

for item in main_data:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    description = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
        
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
        