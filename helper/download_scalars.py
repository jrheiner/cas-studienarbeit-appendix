import os
import requests
from concurrent.futures import ThreadPoolExecutor


TAGS_TO_DOWNLOAD = [
    'train/loss',
    'train/accuracy',
    'train/f1',
    'test/loss',
    'test/accuracy',
    'test/f1',
    'validation/loss',
    'validation/accuracy',
    'validation/f1',
]


def download_csv_file(tag, run, base_url='http://localhost:6006/data/plugin/scalars/scalars', download_dir='.'):
    params = {
        'tag': tag,
        'run': run,
        'format': 'csv'
    }
    url = f"{base_url}?tag={params['tag']}&run={params['run']}&format={params['format']}"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    file_name = os.path.join(download_dir, f"{tag.replace('/', '_')}${run.replace('\\', '_').replace('_custom-metrics', '')}.csv")

    try:
        response = requests.get(url)
        response.raise_for_status() 
        with open(file_name, 'wb') as csv_file:
            csv_file.write(response.content)
        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {file_name}: {e}")

def download_csv_files(tags, runs, base_url='http://localhost:6006/data/plugin/scalars/scalars', download_dir='.'):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_csv_file, tag, run, base_url, download_dir) for tag in tags for run in runs]

        for future in futures:
            future.result()



if __name__ == "__main__":
    tags_to_download = [
        'train/loss',
        'train/accuracy',
        'train/f1',
        'test/loss',
        'test/accuracy',
        'test/f1',
        'validation/loss',
        'validation/accuracy',
        'validation/f1',
    ]

    runs_to_download = [
        's424242-cl1-cf16-dm-bn0\\custom-metrics',
        's424242-cl1-cf16-dm-bn1\\custom-metrics',
        's424242-cl1-cf16-dn-bn0\\custom-metrics',
        's424242-cl1-cf16-dn-bn1\\custom-metrics',
        's424242-cl1-cf16-ds-bn0\\custom-metrics',
        's424242-cl1-cf16-ds-bn1\\custom-metrics',
        's424242-cl1-cf32-dm-bn0\\custom-metrics',
        's424242-cl1-cf32-dm-bn1\\custom-metrics',
        's424242-cl1-cf32-dn-bn0\\custom-metrics',
        's424242-cl1-cf32-dn-bn1\\custom-metrics',
        's424242-cl1-cf32-ds-bn0\\custom-metrics',
        's424242-cl1-cf32-ds-bn1\\custom-metrics',
        's424242-cl1-cf64-dm-bn0\\custom-metrics',
        's424242-cl1-cf64-dm-bn1\\custom-metrics',
        's424242-cl1-cf64-dn-bn0\\custom-metrics',
        's424242-cl1-cf64-dn-bn1\\custom-metrics',
        's424242-cl1-cf64-ds-bn0\\custom-metrics',
        's424242-cl1-cf64-ds-bn1\\custom-metrics',
        's424242-cl1-cf128-dm-bn0\\custom-metrics',
        's424242-cl1-cf128-dm-bn1\\custom-metrics',
        's424242-cl1-cf128-dn-bn0\\custom-metrics',
        's424242-cl1-cf128-dn-bn1\\custom-metrics',
        's424242-cl1-cf128-ds-bn0\\custom-metrics',
        's424242-cl1-cf128-ds-bn1\\custom-metrics',
        's424242-cl2-cf16-dm-bn0\\custom-metrics',
        's424242-cl2-cf16-dm-bn1\\custom-metrics',
        's424242-cl2-cf16-dn-bn0\\custom-metrics',
        's424242-cl2-cf16-dn-bn1\\custom-metrics',
        's424242-cl2-cf16-ds-bn0\\custom-metrics',
        's424242-cl2-cf16-ds-bn1\\custom-metrics',
        's424242-cl2-cf32-dm-bn0\\custom-metrics',
        's424242-cl2-cf32-dm-bn1\\custom-metrics',
        's424242-cl2-cf32-dn-bn0\\custom-metrics',
        's424242-cl2-cf32-dn-bn1\\custom-metrics',
        's424242-cl2-cf32-ds-bn0\\custom-metrics',
        's424242-cl2-cf32-ds-bn1\\custom-metrics',
        's424242-cl2-cf64-dm-bn0\\custom-metrics',
        's424242-cl2-cf64-dm-bn1\\custom-metrics',
        's424242-cl2-cf64-dn-bn0\\custom-metrics',
        's424242-cl2-cf64-dn-bn1\\custom-metrics',
        's424242-cl2-cf64-ds-bn0\\custom-metrics',
        's424242-cl2-cf64-ds-bn1\\custom-metrics',
        's424242-cl2-cf128-dm-bn0\\custom-metrics',
        's424242-cl2-cf128-dm-bn1\\custom-metrics',
        's424242-cl2-cf128-dn-bn0\\custom-metrics',
        's424242-cl2-cf128-dn-bn1\\custom-metrics',
        's424242-cl2-cf128-ds-bn0\\custom-metrics',
        's424242-cl2-cf128-ds-bn1\\custom-metrics',
        's424242-cl3-cf16-dm-bn0\\custom-metrics',
        's424242-cl3-cf16-dm-bn1\\custom-metrics',
        's424242-cl3-cf16-dn-bn0\\custom-metrics',
        's424242-cl3-cf16-dn-bn1\\custom-metrics',
        's424242-cl3-cf16-ds-bn0\\custom-metrics',
        's424242-cl3-cf16-ds-bn1\\custom-metrics',
        's424242-cl3-cf32-dm-bn0\\custom-metrics',
        's424242-cl3-cf32-dm-bn1\\custom-metrics',
        's424242-cl3-cf32-dn-bn0\\custom-metrics',
        's424242-cl3-cf32-dn-bn1\\custom-metrics',
        's424242-cl3-cf32-ds-bn0\\custom-metrics',
        's424242-cl3-cf32-ds-bn1\\custom-metrics',
        's424242-cl3-cf64-dm-bn0\\custom-metrics',
        's424242-cl3-cf64-dm-bn1\\custom-metrics',
        's424242-cl3-cf64-dn-bn0\\custom-metrics',
        's424242-cl3-cf64-dn-bn1\\custom-metrics',
        's424242-cl3-cf64-ds-bn0\\custom-metrics',
        's424242-cl3-cf64-ds-bn1\\custom-metrics',
        's424242-cl3-cf128-dm-bn0\\custom-metrics',
        's424242-cl3-cf128-dm-bn1\\custom-metrics',
        's424242-cl3-cf128-dn-bn0\\custom-metrics',
        's424242-cl3-cf128-dn-bn1\\custom-metrics',
        's424242-cl3-cf128-ds-bn0\\custom-metrics',
        's424242-cl3-cf128-ds-bn1\\custom-metrics',
        's424242-cl4-cf16-dm-bn0\\custom-metrics',
        's424242-cl4-cf16-dm-bn1\\custom-metrics',
        's424242-cl4-cf16-dn-bn0\\custom-metrics',
        's424242-cl4-cf16-dn-bn1\\custom-metrics',
        's424242-cl4-cf16-ds-bn0\\custom-metrics',
        's424242-cl4-cf16-ds-bn1\\custom-metrics',
        's424242-cl4-cf32-dm-bn0\\custom-metrics',
        's424242-cl4-cf32-dm-bn1\\custom-metrics',
        's424242-cl4-cf32-dn-bn0\\custom-metrics',
        's424242-cl4-cf32-dn-bn1\\custom-metrics',
        's424242-cl4-cf32-ds-bn0\\custom-metrics',
        's424242-cl4-cf32-ds-bn1\\custom-metrics',
        's424242-cl4-cf64-dm-bn0\\custom-metrics',
        's424242-cl4-cf64-dm-bn1\\custom-metrics',
        's424242-cl4-cf64-dn-bn0\\custom-metrics',
        's424242-cl4-cf64-dn-bn1\\custom-metrics',
        's424242-cl4-cf64-ds-bn0\\custom-metrics',
        's424242-cl4-cf64-ds-bn1\\custom-metrics',
        's424242-cl4-cf128-dm-bn0\\custom-metrics',
        's424242-cl4-cf128-dm-bn1\\custom-metrics',
        's424242-cl4-cf128-dn-bn0\\custom-metrics',
        's424242-cl4-cf128-dn-bn1\\custom-metrics',
        's424242-cl4-cf128-ds-bn0\\custom-metrics',
        's424242-cl4-cf128-ds-bn1\\custom-metrics',
        's424242-cl5-cf16-dm-bn0\\custom-metrics',
        's424242-cl5-cf16-dm-bn1\\custom-metrics',
        's424242-cl5-cf16-dn-bn0\\custom-metrics',
        's424242-cl5-cf16-dn-bn1\\custom-metrics',
        's424242-cl5-cf16-ds-bn0\\custom-metrics',
        's424242-cl5-cf16-ds-bn1\\custom-metrics',
        's424242-cl5-cf32-dm-bn0\\custom-metrics',
        's424242-cl5-cf32-dm-bn1\\custom-metrics',
        's424242-cl5-cf32-dn-bn0\\custom-metrics',
        's424242-cl5-cf32-dn-bn1\\custom-metrics',
        's424242-cl5-cf32-ds-bn0\\custom-metrics',
        's424242-cl5-cf32-ds-bn1\\custom-metrics',
        's424242-cl5-cf64-dm-bn0\\custom-metrics',
        's424242-cl5-cf64-dm-bn1\\custom-metrics',
        's424242-cl5-cf64-dn-bn0\\custom-metrics',
        's424242-cl5-cf64-dn-bn1\\custom-metrics',
        's424242-cl5-cf64-ds-bn0\\custom-metrics',
        's424242-cl5-cf64-ds-bn1\\custom-metrics',
        's424242-cl5-cf128-dm-bn0\\custom-metrics',
        's424242-cl5-cf128-dm-bn1\\custom-metrics',
        's424242-cl5-cf128-dn-bn0\\custom-metrics',
        's424242-cl5-cf128-dn-bn1\\custom-metrics',
        's424242-cl5-cf128-ds-bn0\\custom-metrics',
        's424242-cl5-cf128-ds-bn1\\custom-metrics',       
    ]

    download_csv_files(TAGS_TO_DOWNLOAD, runs_to_download_seed2,
                       download_dir='tb-data-first-full-run')
