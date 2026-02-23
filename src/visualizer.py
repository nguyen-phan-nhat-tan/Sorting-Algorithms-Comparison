import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

def generate_chart():
    file_path = os.path.join("results", "results.csv")
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Run benchmark.py first.")
        return

    df = pd.read_csv(file_path)

    df_main = df[df['Data'] != 'Average'].copy()
    df_main['Data'] = df_main['Data'].astype(int)
    df_main.set_index('Data', inplace=True)

    plt.figure(figsize=(18, 9))
    
    colors = ['#3498db', '#e67e22', '#95a5a6', '#f1c40f', '#2c3e50']
    
    ax = df_main.plot(kind='bar', width=0.8, color=colors, edgecolor='white', linewidth=0.5)

    plt.yscale('log')
    ax.yaxis.set_minor_locator(ticker.NullLocator())
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.yaxis.get_major_formatter().set_scientific(False)
    ax.yaxis.get_major_formatter().set_useOffset(False)
    ax.set_yticks([1, 10, 100, 1000, 10000, 100000])
    plt.title('Kết quả thử nghiệm trên bộ dữ liệu', fontsize=16, pad=20)
    plt.xlabel('Bộ dữ liệu (1-5: Floats, 6-10: Integers)', fontsize=12)
    plt.ylabel('Thời gian thực hiện (ms) - Thang đo Log', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y', which='both', linestyle='--', alpha=0.4)
    plt.legend(title='Thuật toán', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()

    output_img = os.path.join("results", "sorting_performance_chart.png")
    plt.savefig(output_img, dpi=300)
    print(f"Chart saved to: {output_img}")

if __name__ == "__main__":
    generate_chart()