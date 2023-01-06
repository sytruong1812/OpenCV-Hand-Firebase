# opencv_hand_firebase
1. Tổng quan:
- Viết code Python để nhận diện bàn tay và đếm số ngón tay, sau đó sẽ gửi dữ liệu lên Firebase.
- Viết code cho ESP32 nhận dữ liệu từ Firebase qua Wifi sau đó điều khiển Led.
2. Tạo Firebase để truyền, nhận dữ liệu:
- Đầu tiên, ta cần tạo tài khoản Google để sử dụng Firebase. Các bước hướng dẫn chi tiết tham khảo tại: https://khuenguyencreator.com/giao-tiep-voi-realtime-database-firebase-su-dung-esp32-va-app/ .
3. Code cho ESP32 để nhận dữ liệu từ Firebase:
- Đầu tiên, ta tải phần mềm Arduino IDE về máy.
- Tiếp theo, ta cài thư viện ESP32 cho Arduino IDE, chọn board ESP32 để lập trình và nạp code, tham khảo chi tiết tại: https://ohtech.vn/all-courses/lap-trinh-esp32-voi-arduino-ide/lessons/cai-dat-arduino-ide-va-upload-code-cho-esp32/.
- Sau đó, ta tiến hành cài thư viện Wifi, thư viện Firebase của Mobizt cho ESP32, tham khảo chi tiết tại: https://khuenguyencreator.com/giao-tiep-voi-realtime-database-firebase-su-dung-esp32-va-app/ .
- Cuối cùng, ta viết chương trình nhận dữ liệu từ Firebase và điều khiển Led cho ESP32, tham khảo hướng dẫn tại: https://khuenguyencreator.com/giao-tiep-voi-realtime-database-firebase-su-dung-esp32-va-app/ .
4. Code Python để đếm số ngón tay và truyền dữ liệu lên Firebase:
- Đầu tiên, người thực hiện đề tài sử dụng phầm mềm PyCharm, phiên bản PyCharm Community Edition 2021.3.3 để lập trình python. Ngoài ra phiên bản Python sử dụng là Python 3.9 (64-bit).
- Tiếp theo, ta tiến hành viết code python để nhận diện bàn tay và đếm số ngón tay, tham khảo video hướng dẫn chi tiết tại: https://www.youtube.com/watch?v=UaPDbJsJ63Q .
- Sau đó, ta tiến hành viết python để truyền nhận dữ liệu giữa project python với Firebase, tham khảo video hướng dẫn chi tiết tại đây: https://www.youtube.com/watch?v=EiddkXBK0-o . 
- Cuối cùng, ta kết hợp 2 code chương trình đếm số ngón tay và truyền nhận dữ liệu qua Firebase với nhau để hoàn thành đề tài.

Link: https://youtu.be/5VoAAqBmKJU
