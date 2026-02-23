\# Thực nghiệm các giải thuật sắp xếp nội



\# Tổng quan Dự án



Mục tiêu của dự án là nghiên cứu và so sánh hiệu suất thực tế của các thuật toán sắp xếp có độ phức tạp lý thuyết O(nlogn) trên quy mô dữ liệu lớn (1.000.000 phần tử). Bài thử nghiệm đối chiếu giữa các thuật toán tự cài đặt và các hàm sắp xếp tiêu chuẩn.



&nbsp;   Quicksort: Được triển khai với kỹ thuật chọn Pivot là Median-of-Three nhằm ngăn chặn tình trạng suy biến độ phức tạp thành O(n\*n) trên dữ liệu đã sắp xếp.



&nbsp;   Heapsort: Triển khai dựa trên cấu trúc Max-heap tiêu chuẩn.



&nbsp;   Mergesort: Tiếp cận theo phương pháp chia để trị đệ quy.



&nbsp;   Python Sort (Timsort): Hàm sorted() mặc định của Python, được viết bằng C.



&nbsp;   NumPy Sort: Hàm numpy.sort() sử dụng thư viện C-API.



\# Phương pháp thực nghiệm



Quá trình Benchmark sử dụng 10 tập dữ liệu riêng biệt, mỗi tập chứa 1 triệu phần tử:



&nbsp;   Dataset 1: Số thực đã sắp xếp tăng dần.



&nbsp;   Dataset 2: Số thực đã sắp xếp giảm dần.



&nbsp;   Datasets 3-5: Số thực ngẫu nhiên.



&nbsp;   Datasets 6-10: Số nguyên ngẫu nhiên.



Độ chính xác và Tính toàn vẹn



&nbsp;   Đo lường thời gian: Sử dụng time.perf\_counter() để đảm bảo độ chính xác cao trong phép đo.

&nbsp;   

&nbsp;   Độc lập dữ liệu: Mỗi thuật toán làm việc trên một bản sao độc lập (.copy()) để đảm bảo tính khách quan.

&nbsp;   

&nbsp;   Giới hạn hệ thống: Tăng sys.setrecursionlimit để xử lý an toàn 1 triệu đệ quy mà không gây lỗi Stack Overflow.

&nbsp;   

Yêu cầu



&nbsp;   Python 3.8+



&nbsp;   Thư viện: numpy, pandas, matplotlib



Cài đặt



&nbsp;   git clone https://github.com/nguyen-phan-nhat-tan/Sorting-Algorithms-Comparison



&nbsp;   pip install requirements.txt

&nbsp;   

&nbsp;   python src/benchmark.py







