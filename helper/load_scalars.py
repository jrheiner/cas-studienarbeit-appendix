import os
import csv

def read_csv_files(directory):
    data_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            metric, run = parse_filename(filename)
            seed, model = parse_run(run)

            if metric not in data_dict.keys():
                data_dict[metric] = {}
            if model not in data_dict[metric].keys():
                data_dict[metric][model] = []


            with open(filepath, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                x_values = []
                x_rel_values = []
                y_values = []

                print(filename)

                for row in csv_reader:
                    x_values.append(int(row['Step']))
                    y_values.append(float(row['Value']))

                data_dict[metric][model].append({
                    'seed': seed,
                    'model': model,
                    'x': x_values,
                    'y': y_values
                })

    return data_dict

def parse_filename(filename):
    parts = filename.split('$')
    if len(parts) == 2:
        metric, run = parts
        return metric, run[:-4]
    else:
        return None, None

def parse_run(run):
    seed, model = run.split('-', 1)
    return seed, model


if __name__ == "__main__":
    directory_path = "tb-data-runs"
    result_dict = read_csv_files(directory_path)

    # print(result_dict)
