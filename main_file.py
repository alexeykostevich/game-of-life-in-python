from life import Cell, Life, WrappedUniverse


# Create a random wrapped universe of 10 x 10
universe = WrappedUniverse.random(10, 10, Cell.likely)
# Get a universe iterator (actually, generator) from life
life = Life.originate_from(universe, Cell)

# Iterate through life and print the universe on each step
for universe in life:
    print(universe)
    input('Press Enter to continue...')