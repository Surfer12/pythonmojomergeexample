# main.py

import mojo_compute

def main():
    data = [i for i in range(1_000_000)]
    result = mojo_compute.sum_large_list(data)
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()
