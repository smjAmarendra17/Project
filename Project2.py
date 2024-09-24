#Generate and printsimple number patterns.
def generate_pyramid_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n, i, -1):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end=" ")
        print()  # Newline

# Generate pyramid pattern with 5 rows
generate_pyramid_pattern(5)