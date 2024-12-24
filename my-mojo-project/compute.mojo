// compute.mojo

@mojo.function
def sum_large_list(data: list[int]) -> int:
    total = 0
    for number in data:
        total += number
    return total
