ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

print(f"{len(ice_cream)} flavors")

ice_cream["mint"] = 3

print(ice_cream["chocolate"])

ice_cream["vanilla"] += 10

ice_cream.pop("strawberry")

total_orders: int = 0

for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]

print(f"Total orders: {total_orders}")


print(ice_cream["pecan"])
