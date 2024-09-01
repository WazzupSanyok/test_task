import json
import sys


def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def fill_values(data, values_dict):
    if isinstance(data, dict):
        if 'id' in data:
            test_id = data['id']
            if test_id in values_dict:
                data['value'] = values_dict[test_id]
        for key in data:
            if isinstance(data[key], (dict, list)):
                fill_values(data[key], values_dict)
    elif isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], (dict, list)):
                fill_values(data[i], values_dict)
    return data


def solve(tests_file, values_file, results_file):
    tests_data = read_file(tests_file)
    values_data = read_file(values_file)

    values_map = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data, values_map)

    with open(results_file, 'w') as file:
        json.dump(tests_data, file, indent=2)


def main():
    if len(sys.argv) != 4:
        print("Use,please: taks3.py <tests_file> <values_file> <results_file>")
        sys.exit(1)

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    results_file = sys.argv[3]
    solve(tests_file, values_file, results_file)


if __name__ == "__main__":
    main()
    