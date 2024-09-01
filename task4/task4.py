import sys


def read_file(file_path):
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]
    return nums


def solve(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    res =0
    for num in nums:
        res += abs(num - median)
    return res


def main():
    if len(sys.argv) != 2:
        print("Use,please: taks4.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    nums = read_file(file_path)
    result = solve(nums)
    print(result)


if __name__ == "__main__":
    main()
