import os


all_models = ['cl1-cf128-dm-bn0', 'cl1-cf128-dm-bn1', 'cl1-cf128-dn-bn0', 'cl1-cf128-dn-bn1', 'cl1-cf128-ds-bn0', 'cl1-cf128-ds-bn1', 'cl1-cf16-dm-bn0', 'cl1-cf16-dm-bn1', 'cl1-cf16-dn-bn0', 'cl1-cf16-dn-bn1', 'cl1-cf16-ds-bn0', 'cl1-cf16-ds-bn1', 'cl1-cf32-dm-bn0', 'cl1-cf32-dm-bn1', 'cl1-cf32-dn-bn0', 'cl1-cf32-dn-bn1', 'cl1-cf32-ds-bn0', 'cl1-cf32-ds-bn1', 'cl1-cf64-dm-bn0', 'cl1-cf64-dm-bn1', 'cl1-cf64-dn-bn0', 'cl1-cf64-dn-bn1', 'cl1-cf64-ds-bn0', 'cl1-cf64-ds-bn1', 'cl2-cf128-dm-bn0', 'cl2-cf128-dm-bn1', 'cl2-cf128-dn-bn0', 'cl2-cf128-dn-bn1', 'cl2-cf128-ds-bn0', 'cl2-cf128-ds-bn1', 'cl2-cf16-dm-bn0', 'cl2-cf16-dm-bn1', 'cl2-cf16-dn-bn0', 'cl2-cf16-dn-bn1', 'cl2-cf16-ds-bn0', 'cl2-cf16-ds-bn1', 'cl2-cf32-dm-bn0', 'cl2-cf32-dm-bn1', 'cl2-cf32-dn-bn0', 'cl2-cf32-dn-bn1', 'cl2-cf32-ds-bn0', 'cl2-cf32-ds-bn1', 'cl2-cf64-dm-bn0', 'cl2-cf64-dm-bn1', 'cl2-cf64-dn-bn0', 'cl2-cf64-dn-bn1', 'cl2-cf64-ds-bn0', 'cl2-cf64-ds-bn1', 'cl3-cf128-dm-bn0', 'cl3-cf128-dm-bn1', 'cl3-cf128-dn-bn0', 'cl3-cf128-dn-bn1', 'cl3-cf128-ds-bn0', 'cl3-cf128-ds-bn1', 'cl3-cf16-dm-bn0', 'cl3-cf16-dm-bn1', 'cl3-cf16-dn-bn0', 'cl3-cf16-dn-bn1', 'cl3-cf16-ds-bn0', 'cl3-cf16-ds-bn1', 'cl3-cf32-dm-bn0', 'cl3-cf32-dm-bn1', 'cl3-cf32-dn-bn0', 'cl3-cf32-dn-bn1', 'cl3-cf32-ds-bn0', 'cl3-cf32-ds-bn1', 'cl3-cf64-dm-bn0', 'cl3-cf64-dm-bn1', 'cl3-cf64-dn-bn0', 'cl3-cf64-dn-bn1', 'cl3-cf64-ds-bn0', 'cl3-cf64-ds-bn1', 'cl4-cf128-dm-bn0', 'cl4-cf128-dm-bn1', 'cl4-cf128-dn-bn0', 'cl4-cf128-dn-bn1', 'cl4-cf128-ds-bn0', 'cl4-cf128-ds-bn1', 'cl4-cf16-dm-bn0', 'cl4-cf16-dm-bn1', 'cl4-cf16-dn-bn0', 'cl4-cf16-dn-bn1', 'cl4-cf16-ds-bn0', 'cl4-cf16-ds-bn1', 'cl4-cf32-dm-bn0', 'cl4-cf32-dm-bn1', 'cl4-cf32-dn-bn0', 'cl4-cf32-dn-bn1', 'cl4-cf32-ds-bn0', 'cl4-cf32-ds-bn1', 'cl4-cf64-dm-bn0', 'cl4-cf64-dm-bn1', 'cl4-cf64-dn-bn0', 'cl4-cf64-dn-bn1', 'cl4-cf64-ds-bn0', 'cl4-cf64-ds-bn1', 'cl5-cf128-dm-bn0', 'cl5-cf128-dm-bn1', 'cl5-cf128-dn-bn0', 'cl5-cf128-dn-bn1', 'cl5-cf128-ds-bn0', 'cl5-cf128-ds-bn1', 'cl5-cf16-dm-bn0', 'cl5-cf16-dm-bn1', 'cl5-cf16-dn-bn0', 'cl5-cf16-dn-bn1', 'cl5-cf16-ds-bn0', 'cl5-cf16-ds-bn1', 'cl5-cf32-dm-bn0', 'cl5-cf32-dm-bn1', 'cl5-cf32-dn-bn0', 'cl5-cf32-dn-bn1', 'cl5-cf32-ds-bn0', 'cl5-cf32-ds-bn1', 'cl5-cf64-dm-bn0', 'cl5-cf64-dm-bn1', 'cl5-cf64-dn-bn0', 'cl5-cf64-dn-bn1', 'cl5-cf64-ds-bn0', 'cl5-cf64-ds-bn1']


def check_count(directory):
    data_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            metric, run = parse_filename(filename)
            seed, model = parse_run(run)

            if seed not in data_dict.keys():
                data_dict[seed] = {}
            if metric not in data_dict[seed].keys():
                data_dict[seed][metric] = []
            data_dict[seed][metric].append(model)

    total_seeds = data_dict.keys()
    print(f'got {len(total_seeds)} seeds: {list(total_seeds)}')
    for s in data_dict.keys():
        print(f'# {s}: {len(data_dict[seed].keys())} metrics: {list(data_dict[seed].keys())}')
    print('---')
    for s in data_dict.keys():
        for loopmetric in data_dict[seed]:
            print(f'# {s} # {loopmetric}: {len(data_dict[s][loopmetric])} models')
            missing_models = [missingmodel for missingmodel in all_models if missingmodel not in data_dict[s][loopmetric]]
            if missing_models:
                print(f"! # {s}: {len(missing_models)} missing: {missing_models}")
                break
        print('-')


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
    result_dict = checkcount(directory_path)

