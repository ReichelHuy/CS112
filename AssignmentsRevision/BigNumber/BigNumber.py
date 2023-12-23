def f(new, j):
    global mas
    global n
    global k
    summ = 0
    mas_2 = mas.copy()
    # Thay vì search trong khoảng rộng ta nên seach trong khoảng max a[i]
    # nếu tồn tại j <= n-1 và giá trị kq đang lớn hơn giá trị của a[j] và giá trị này có thể vượt được kq
    # lượng chênh lệch sẽ được cộng vào sum 
    # tăng j lên 1
    # vì khi tăng j lên 1 chúng ta bây giờ chỉ cần giảm kq đi 1 đơn vị 
    # và khi nó đạt được trả về true 
    """
    Lấy ví dụ 
    n=5, k=6
    [1 3 4 5 1] với output= 7, ans sẽ luôn là số lớn nhất trong mảng . 
    ta sẽ tìm kiếm với ans+1=5, trả về true nếu có thể tăng lên 1 đơn vị 
    ta thấy để "1" lên đươc ans="5" cần 4 hành động  (ans-1 =4) , 
    ta lưu số hành động vào sum=4,
    Gọi new chính là giá trị tối thiểu của mỗi phần tử phải đạt được 
    giải thích : để 1->5 thì 3->4 (thoả a[i] <= a[i+1]):[1,3]->[2,3]->[3,3]->[3,4]->[4,4]->[5,4]. new = ans - 1 = 5-1 =4 . 
    có nghĩa là để thoả điều kiện đó thì "3" phải lên được 4, cần 1 hành động (new - a[i] = 1 ), cộng cho sum thì 5 hành động 
    tới đây phải chú ý tổng hành động không được vượt quá k, lúc này (tổng=5) <= (k=7) 
    => 4 -> 5, cần thêm 1 hành động, cộng với sum trước đó là 6 
    => 5 -> 5, 5<=5 ta cần 0 hành động để đạt 5,  dừng vòng lợp vì a[i] đã đạt tới giá trị new , trả về 0
    Complexity :
    Duyệt qua n phần tử là n 
    kiểm tra từng phần tử có đạt tới giá trị max : n 
    tăng k đơn vị. Độ phức tạp (n^2 * k)
    Other solution: 
    
    """
    while j < n and new > mas_2[j] and summ + new - mas_2[j] <= k:
        summ += new - mas_2[j]
        j += 1
        new -= 1
    if j < n and new <= mas_2[j]:
        return True
    return False
 
 
t = int(input())
mas_ans = []
for q in range(t):
    n, k = map(int, input().split())
    mas = [int(el) for el in input().split()]
    ans = max(mas)
    for i in range(n):
        while f(ans + 1, i):
            ans += 1
    mas_ans.append(ans)
for i in range(t):
    print(mas_ans[i])