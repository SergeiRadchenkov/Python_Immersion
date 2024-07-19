
import os
import json
import csv
import pickle

def get_dir_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)

    return total_size

def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results

def save_results_to_json(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file)

def save_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(results, file)
