import time
import os
import pandas as pd
import numpy as np
import sys
from algorithms import quicksort, heapsort, mergesort

sys.setrecursionlimit(2000000)

def setup_directories():
    for folder in ['data', 'results']:
        if not os.path.exists(folder):
            os.makedirs(folder)

def save_as_txt(filename, data):
    path = os.path.join('data', filename)
    np.savetxt(path, data, fmt='%g', header=f"Dataset size: {len(data)}")

def generate_and_save_data():
    size = 1_000_000
    # 1. Sorted (Float)
    d1 = np.sort(np.random.rand(size))
    save_as_txt('dataset_1_sorted.txt', d1)
    
    # 2. Reverse (Float)
    save_as_txt('dataset_2_reverse.txt', d1[::-1])
    
    # 3-5. Random (Float)
    for i in range(3, 6):
        save_as_txt(f'dataset_{i}_random_float.txt', np.random.rand(size))
        
    # 6-10. Random (Int)
    for i in range(6, 11):
        data = np.random.randint(0, 10**9, size=size)
        save_as_txt(f'dataset_{i}_random_int.txt', data)

def run_benchmark():
    setup_directories()
    
    if not any(fname.endswith('.txt') for fname in os.listdir('data')):
        generate_and_save_data()

    results = []
    print(f"\nStarting benchmark")
    print("-" * 85)

    data_files = sorted([f for f in os.listdir('data') if f.endswith('.txt')], 
                        key=lambda x: int(x.split('_')[1]))

    for i, file_name in enumerate(data_files, 1):
        d = np.loadtxt(os.path.join('data', file_name))
        
        row = {'Data': i}
        print(f"Processing Dataset {i}/10: {file_name}")

        methods = [
            ("Quicksort", quicksort), 
            ("Heapsort", heapsort), 
            ("Mergesort", mergesort), 
            ("sort (python)", sorted),
            ("sort (numpy)", np.sort)
        ]

        for name, func in methods:
            print(f"  > Running {name}...", end="", flush=True)
            arr_copy = d.copy() if name == "sort (numpy)" else list(d)
            
            start = time.perf_counter()
            func(arr_copy)
            end = time.perf_counter()
            
            duration = round((end - start) * 1000, 2)
            row[name] = duration
            print(f" {duration} ms")
        
        results.append(row)
        print("-" * 85)

    # Export CSV
    df = pd.DataFrame(results)
    avg_row = df.mean(numeric_only=True).to_dict()
    avg_row['Data'] = 'Average'
    df = pd.concat([df, pd.DataFrame([avg_row])], ignore_index=True)

    output_path = os.path.join("results", "results.csv")
    df.to_csv(output_path, index=False)
    print(f"\nBenchmark complete. CSV saved to: {output_path}")

if __name__ == "__main__":
    run_benchmark()