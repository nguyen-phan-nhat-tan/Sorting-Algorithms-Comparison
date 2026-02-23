# Thực nghiệm các giải thuật sắp xếp nội

# 

# phân tích thực nghiệm về hiệu năng của các thuật toán Sorting khác nhau được triển khai bằng Python, so sánh giữa các bản tự cài đặt và các thư viện tiêu chuẩn công nghiệp.

# 

# \## 📋 Project Overview

# The goal of this project is to test the efficiency of $O(n \\log n)$ algorithms when handling large-scale datasets (1,000,000 elements) with varying initial orders (sorted, reverse-sorted, and random).

# 

# \### Algorithms Tested:

# \* \*\*Quicksort\*\*: Implemented with Median-of-Three pivot selection to prevent $O(n^2)$ degradation on sorted data.

# \* \*\*Heapsort\*\*: A standard max-heap implementation.

# \* \*\*Mergesort\*\*: A recursive divide-and-conquer approach.

# \* \*\*NumPy Sort\*\*: The highly optimized `numpy.sort()` (typically using Quicksort or Timsort in C).

# 

# \## 📊 Methodology

# The benchmark utilizes 10 distinct datasets, each containing 1 million elements:

# 1\.  \*\*Dataset 1\*\*: Sorted Floats (Ascending)

# 2\.  \*\*Dataset 2\*\*: Reverse Sorted Floats (Descending)

# 3\.  \*\*Datasets 3-5\*\*: Random Floats

# 4\.  \*\*Datasets 6-10\*\*: Random Integers

# 

# \### Security \& Precision

# \* \*\*Timing\*\*: Uses `time.perf\_counter()` for high-precision measurement.

# \* \*\*Data Integrity\*\*: Each algorithm receives a fresh copy of the data to ensure previous sorts do not influence subsequent tests.

# 

# \## 🚀 Getting Started

# 

# \### Prerequisites

# \* Python 3.8+

# \* NumPy

# \* Pandas (for CSV generation)

# 

# \### Installation

# ```bash

# git clone \[https://github.com/](https://github.com/)\[Your-Username]/sorting-benchmark.git

# cd sorting-benchmark

# pip install numpy pandas

