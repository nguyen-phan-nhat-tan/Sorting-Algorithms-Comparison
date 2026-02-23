# Thực nghiệm các giải thuật sắp xếp nội

# Tổng quan Dự án

Mục tiêu của dự án là nghiên cứu và so sánh hiệu suất thực tế của các thuật toán sắp xếp có độ phức tạp lý thuyết O(nlogn) trên quy mô dữ liệu lớn (1.000.000 phần tử). Bài thử nghiệm đối chiếu giữa các thuật toán tự cài đặt và các hàm sắp xếp tiêu chuẩn.

- **Quicksort:** Được triển khai với kỹ thuật chọn Pivot là Median-of-Three nhằm ngăn chặn tình trạng suy biến độ phức tạp thành O(n*n) trên dữ liệu đã sắp xếp.
- **Heapsort:** Triển khai dựa trên cấu trúc Max-heap tiêu chuẩn.
- **Mergesort:** Tiếp cận theo phương pháp chia để trị đệ quy.
- **Python Sort (Timsort):** Hàm sorted() mặc định của Python, được viết bằng C.
- **NumPy Sort:** Hàm numpy.sort() sử dụng thư viện C-API.

# Phương pháp thực nghiệm

Quá trình Benchmark sử dụng 10 tập dữ liệu riêng biệt, mỗi tập chứa 1 triệu phần tử:

- **Dataset 1:** Số thực đã sắp xếp tăng dần.
- **Dataset 2:** Số thực đã sắp xếp giảm dần.
- **Datasets 3-5:** Số thực ngẫu nhiên.
- **Datasets 6-10:** Số nguyên ngẫu nhiên.

## Độ chính xác và Tính toàn vẹn

- **Đo lường thời gian:** Sử dụng time.perf_counter() để đảm bảo độ chính xác cao trong phép đo.
- **Độc lập dữ liệu:** Mỗi thuật toán làm việc trên một bản sao độc lập (.copy()) để đảm bảo tính khách quan.
- **Giới hạn hệ thống:** Tăng sys.setrecursionlimit để xử lý an toàn 1 triệu đệ quy mà không gây lỗi Stack Overflow.

## Yêu cầu

- Python 3.8+
- Thư viện: numpy, pandas, matplotlib

## Cài đặt

```bash
git clone https://github.com/nguyen-phan-nhat-tan/Sorting-Algorithms-Comparison
pip install -r requirements.txt
python src/benchmark.py
```
