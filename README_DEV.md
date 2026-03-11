# Learn English App - Development Guide

## 🚀 Cách push code lên GitHub

Chỉ cần chạy:
```bash
push_to_github.bat
```

## 🔧 Công cụ sinh content mới

### Sinh content tự động:
```bash
python generate_new_content.py
```

Chọn loại content và số lượng, script sẽ tự động:
- ✓ Thêm vào `data/content.json`
- ✓ Đầy đủ dịch tiếng Việt
- ✓ Đầy đủ giải thích

### Các loại content:
1. **Word** - Từ vựng (term, meaning, example, IPA)
2. **Grammar** - Ngữ pháp (công thức, cách dùng, ví dụ)
3. **Quiz** - Câu hỏi trắc nghiệm 4 đáp án
4. **Fillblank** - Điền từ chọn đáp án (có hint)
5. **Typeblank** - Điền từ gõ đáp án (có hint)
6. **Reorder** - Sắp xếp từ thành câu

## 📊 Thống kê hiện tại

- Tổng: **5,952 items**
- Từ vựng: 1,450
- Ngữ pháp: 615
- Quiz: 1,620
- Fillblank: 723
- Typeblank: 739
- Reorder: 805

## 🌐 Chạy local

```bash
cd learn_english
python -m http.server 8000
```

Mở: http://localhost:8000/app.html
