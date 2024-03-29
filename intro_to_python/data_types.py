# Operators
print(3 + 5)
print(5 - 10)
print(10 * 9)
print(12 / 5)
print(12 % 5)
print(2**3)
print(7 // 2) # ROUNDS DOWN

mean = (23 + 32 + 64) / 3
print(mean)

tilesNeeded = (9 * 7) + (5 * 7)
print(tilesNeeded)

leftOver = (17 * 6) - tilesNeeded
print(leftOver)

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decreas the rainfall variable by 10% to account for runoff
rainfall = rainfall + (rainfall *.10)

# add the rainfall variable to the reservoir_volume variable
reservoir_volume = reservoir_volume + rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume + (reservoir_volume *.05)

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume - (reservoir_volume *.05)

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)