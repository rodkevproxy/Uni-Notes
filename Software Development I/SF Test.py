
# Variables
height_m = 3
radius_m = 2
pi = 3.142

# Volume in cubic metres
volume_m3 = (pi * radius_m**2 * height_m) / 3

# Convert to litres 
volume_litres = volume_m3 * 1000

# Output
print(f"The volume of the cone is {volume_m3:.3f} cubic metres or {volume_litres:.1f} ltrs.")
