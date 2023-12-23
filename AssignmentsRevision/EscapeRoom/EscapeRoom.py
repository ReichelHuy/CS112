#Readme: Nếu giải bài toán bằng cách thêm vào, sẽ rất khó, ta tổng quát cho việc xoá 1 phần tử 
# Nếu n=1, trả ngay về phần tử đó
# Ví dụ N=3 và mảng đã được sắp xếp [1 2 3 5 6 ]
# Nếu ta xoá phần tử đầu thì giá trị mỗi cặp là 8 , chính là phần tử thứ 2 + cuói cùng ,kí hiệu K3= 8
# Nếu ta xoá phần tử cuối thì giá trị mỗi cặp là 6, chính là phần tử thứ 1 + kế cuối , kí hiệu k1=6
# Nếu ta xoá bất cứ cái nào ở giữa, rõ ràng giá trị mỗi cặp là 7, chính là đầu + cuối , kí hiệu k2=7
# ta sẽ duyệt lại mảng 2n-1 ban đầu cho 3 trường hợp, lưu giá trị skips, dùng kĩ thuật 2 còn trỏ để duyệt 2 đầu 
# skips chỉ cho phép bỏ qua duy nhất 1 phần tử, và phần tử bị bỏ qua chính là phần tử bị xoá !
# Kết quả của bài toán chỉ là (K-phần tử bị đánh dấu bỏ qua) 
#  Bài toán đi tìm password có thể tóm tắt thành 3 trường hợp như trên
#  

def find_password(N, nums):
    if (N==1):
        return 1
    nums.sort()
    K_candidates = set()
    # Case 1: Remove the first element
    K1 = nums[0] + nums[-2]
    K_candidates.add(K1)
    # Case 2: Remove the last element
    K2 = nums[-1] + nums[1]
    K_candidates.add(K2)
    # Case 3: Remove an element in the middle
    K3 = nums[0] + nums[-1]
    K_candidates.add(K3)

    #Sort Answer
    for K in sorted(K_candidates):
        i = 0
        j = N - 1
        skips = 0
        mark = 0
        while i < j:
            if nums[i] + nums[j] < K:
                mark = i
                skips += 1
                i += 1
            elif nums[i] + nums[j] > K:
                mark = j
                skips += 1
                j -= 1
            else:
                i += 1
                j -= 1
        
        if (skips <= 1 ):
            if (skips == 0 and K-nums[i]>0):
                return(K-nums[i])
            if (K-nums[mark]>0):
                return(K-nums[mark])
     
    return -1


# Đọc số lượng test case
K = int(input())

for case in range(1, K + 1):
    # Đọc số N
    N = int(input())

    # Đọc dãy số
    nums = list(map(int, input().split()))

    # Tìm mật khẩu
    password = find_password(2*N-1, nums)

    # In kết quả
    print(f"Case #{case}: {password}")