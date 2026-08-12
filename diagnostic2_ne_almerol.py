starship = 50,000

satellite = 1,000
rover = 2,500
supplies = 500
weight = int(input("What cargo would you like to load?"))
count = 1
def calculate_fuel(cargo_weight):
    while count <= 3:
        if weight == "satellite":
            print("starship")
            return starship + satellite
        elif weight == "rover":
            print(starship)
            return starship + rover
        elif weight == "supplies":
            print(starship)
            return starship + supplies
        else: print("Data not approved for mission")
        if weight == "launch":
            break
    count += 1