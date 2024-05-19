# Split and joining lists
transportation = "train, car, motorcycle, bus, airplane, boat, taxi, uber"
SNHU_email = "ryan.hopkins2@snhu.edu"
UMA_email = "ryan.hopkins@maine.edu"
candy = "snickers bar, baby ruth, gummy worms, skittles candy"

transportation = transportation.split(",")
SNHU_email = SNHU_email.split("@")
UMA_email = UMA_email.split(".")
candy = candy.split(" ")

print(transportation)
print(SNHU_email) 
print(UMA_email)
print(candy)

toys = ["bike", "cars", "dolls", "computer", "tablet"]
print("".join(toys))
print("-".join(toys))
print("****".join(toys))
print(" AND ".join(toys))