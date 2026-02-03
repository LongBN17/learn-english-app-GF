# Learn English - Web Version

Web application version của Learn English extension, được tạo tương tự như Learn Chinese web app.

## Tính năng

### 📖 Tab Learn (Học)
- Hiển thị từ vựng, ngữ pháp, và quiz một cách ngẫu nhiên
- Chỉ đọc thông tin, không có SRS
- Nút **Speak** để nghe phát âm
- Nút **Next** để chuyển sang item tiếp theo

### 🎯 Tab Practice (Luyện tập)
- Hệ thống SRS (Spaced Repetition System) giống Learn Chinese
- Theo dõi tiến độ học tập với progress bar
- Nút **Known** để đánh dấu đã biết
- Nút **Again** để đánh dấu cần học lại
- Nút **Hint** để xem gợi ý (cho quiz)
- Nút **Speak** để nghe phát âm
- Stats bar hiển thị: Today, Streak, Known, Due

### ⚙️ Settings
- **Auto speak on next**: Tự động phát âm khi chuyển sang item mới
- **Review only**: Chỉ hiển thị các card đã đến hạn review
- **Daily goal**: Mục tiêu học mỗi ngày
- **Content type**: Lọc theo loại nội dung (All, Vocabulary, Grammar, Quiz)

## Các loại nội dung

### 1. Word (Từ vựng)
- Hiển thị từ tiếng Anh
- IPA (International Phonetic Alphabet) phát âm
- Nghĩa tiếng Việt
- Ví dụ sử dụng
- Level badge (A1, A2, B1, B2, C1, C2)

### 2. Grammar (Ngữ pháp)
- Topic (chủ đề)
- Formula (công thức)
- Usage (cách sử dụng)
- Signal words (từ tín hiệu)
- Example (ví dụ)

### 3. Quiz (Câu hỏi trắc nghiệm)
- Câu hỏi
- 4 lựa chọn
- Click vào đáp án để xem kết quả
- Giải thích đáp án

## Cách sử dụng

### 1. Chạy local server

Do CORS policy, bạn cần chạy local web server:

**Python:**
```bash
cd c:\Users\Tester\python\new\learn_english
python -m http.server 8000
```

**Node.js (nếu có):**
```bash
cd c:\Users\Tester\python\new\learn_english
npx http-server -p 8000
```

### 2. Mở trình duyệt

Mở trình duyệt và truy cập:
```
http://localhost:8000/app.html
```

hoặc

```
http://localhost:8000/index.html
```

## Keyboard Shortcuts

### Tab Learn:
- **N**: Next item
- **S**: Speak (phát âm)

### Tab Practice:
- **N**: Next item
- **Space**: Hint
- **Enter**: Mark as Known
- **Backspace**: Mark as Again
- **S**: Speak (phát âm)

## So sánh với Extension

### Giống nhau:
- ✅ Sử dụng cùng file `data/content.json`
- ✅ Hỗ trợ 3 loại: word, grammar, quiz
- ✅ Settings: content type filter
- ✅ Random selection

### Khác biệt:
- ✅ Web version có SRS system (như Learn Chinese)
- ✅ Web version có stats tracking (Today, Streak, Known, Due)
- ✅ Web version có 2 tabs: Learn và Practice
- ✅ Extension có notification alarm (web không có)
- ✅ Extension có popup nhỏ gọn (web có UI đầy đủ)

## Files

- `index.html`: Redirect đến app.html
- `app.html`: Main application
- `data/content.json`: Dữ liệu nội dung (dùng chung với extension)

## Lưu ý

- Dữ liệu được lưu trong `localStorage` của trình duyệt
- Progress và settings sẽ được lưu tự động
- Cần chạy local server để load `content.json` (do CORS)
