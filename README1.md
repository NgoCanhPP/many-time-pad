# Many Time Pad

Ý tưởng:

- Với khoá $k$ , xét các kí tự $x_1, x_2$ được mã hoá thành các kí tự $y_1, y_2$
    
    $y_1 = x_1\oplus k,\ y_2 = x_2\oplus k$
    
    Ta có, 
    
    $y_1\oplus y_2= (x_1\oplus k)\oplus (x_2\oplus k) = (x_1\oplus k)\oplus (k\oplus x_2) = x_1\oplus (k\oplus k)\oplus x_2) =x_1 \oplus x_2$
    
- Ngoài ra việc XOR một kí tự ASCII với space sẽ đổi chỗ kí tự các cột 1-2, 3-4 tương ứng trong bảng sau
    
    <img width="800" alt="Untitled" src="https://github.com/NgoCanhPP/many-time-pad/assets/88614136/dd554659-1733-41bc-a55a-a9bf74f67df6">

    
    Nguồn: wikipedia.org
    
    Ví dụ: ‘A’ XOR ‘ ‘ = ‘a’
    

Bước 1:

Với mỗi ciphertext ta sử dụng phép XOR ciphertext đó với tất cả các ciphertext còn lại thu được danh sách list_xored bao gồm các xored là kết quả của phép XOR ở trên

Với mỗi từ thứ i có các khả năng:

- trong các xored[i] nếu tồn tại 1 xored[i] có giá trị hex nằm trong đoạn [20, 3F] hoặc lớn hơn hoặn bằng 7F thì vị trí của i chắc chắn không phải dấu cách vì các ciphertext chỉ luôn chứa các kí tự thường
- sau khi loại trừ trường hợp trên thì khả năng ciphertext[i] là 1 dấu cách ‘ \s’ phụ thuộc vào giới hạn b < n với số lượng giá trị hex của mỗi xored[i] nói trên nằm trong đoạn [01, 1F] là b.
    
    Với tập mã này thì em nhận thấy với n = 2 thì sẽ cho ra mã kết quả đẹp nhất có thể dự đoạn được nội dung
    

Sau khi duyệt hết các từ thứ i thì thu được 1 chuỗi là dạng khung của chuỗi cần tìm với kí hiệu ‘__’ là kí tự chưa xác định chắc chắn không phải dấu cách. Còn lại ‘\s’ là kí tự có xác suất cao là dấu cách (nhưng vẫn có thể là dấu khác)

Minh hoạ nằm trong 12 dòng đầu file ‘result.txt’ là kết quả khi sử dụng mã cần giải mã (mã số 11) XOR với tất cả các mã còn lại

Bước 2:

Xác định dạng khung của tất cả các chuỗi kí tự khác (kết quả nằm trong file ‘over_view.txt’)

Bước 3: Giải mã

Với kí tự thứ i của mã cần giải, xem xét xem kí tự thứ i của tất các các ciphertext còn lại có cái nào có khả năng là dấu cách không, nếu có XOR kí tự này với kí tự thứ i của mã cần giải ta thu được 1 khả năng của kí tự thứ i của mã cần giải. Xét trên tất cả các kí tự thứ i của các ciphertext còn lại ta được bộ các khả năng của kí tự thứ i của mã cần giải cho nó vào kết quả.

Xét trên tất các các kí tự của mã cần giảir và in kết quả ra file result.txt. 

Bước 4: Dự đoán kết quả và kết luận

Sau khi có được kết quả từ bước 3. Dự đoán được mã cần giải là

‘The secret message is: When using a string cipher, never use the key more than once’

Các kí tự dấu ‘:’ và dấu ‘,’ được dự đoán bởi kết quả từ bước 2 khi mà ở vị trí của dấu ‘:’, ciphertext thứ 5 sau khi XOR với vị trí này của mã cần giải được hex là ‘1A’ - là kết quả của việc XOR dấu ‘:’ và dấu cách, tương tự cho dấu ‘,’
