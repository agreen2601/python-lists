planet_list = ["Mercury", "Mars"]

# 1
planet_list.append("Jupiter")
planet_list.append("Saturn")

# 2
planet_list.extend(["Uranus", "Neptune"])

# 3
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

# 4
planet_list.append("Pluto")

# 5
rocky_planets = planet_list[0:4]

# 6
del(planet_list[8])