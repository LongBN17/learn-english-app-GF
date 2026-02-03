import json
import random

def get_current_content():
    try:
        with open('data/content.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_content(content):
    with open('data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

new_items = []

# --- VOCABULARY (IT & Business) ---
vocab_list = [
    ("backend", "/ˈbækend/", "phần xử lý phía server", "Backend handles logic.", "B1"),
    ("frontend", "/ˈfrʌntend/", "giao diện người dùng", "Frontend is built with React.", "B1"),
    ("fullstack", "/ˈfʊlstæk/", "lập trình toàn diện", "He is a fullstack dev.", "B2"),
    ("server", "/ˈsɜːvə/", "máy chủ", "Restart the server.", "A2"),
    ("client", "/ˈklaɪənt/", "máy khách / khách hàng", "Client sends request.", "B1"),
    ("request", "/rɪˈkwest/", "yêu cầu", "HTTP request failed.", "B1"),
    ("response", "/rɪˈspɒns/", "phản hồi", "Check the API response.", "B1"),
    ("header", "/ˈhedə/", "phần đầu thông tin", "Add auth token in header.", "B2"),
    ("body", "/ˈbɒdi/", "phần nội dung", "Send data in body.", "B1"),
    ("status code", "/ˈsteɪtəs kəʊd/", "mã trạng thái", "Status code 404.", "B1"),
    ("query parameter", "/ˈkwɪəri pəˈræmɪtə/", "tham số truy vấn", "Filter by query parameter.", "B2"),
    ("path variable", "/pɑːθ ˈveəriəbl/", "biến đường dẫn", "Use path variable for ID.", "B2"),
    ("cookie", "/ˈkʊki/", "cookie trình duyệt", "Store session in cookie.", "B1"),
    ("session", "/ˈseʃn/", "phiên làm việc", "Session expired.", "B1"),
    ("cache", "/kæʃ/", "bộ nhớ đệm", "Clear the cache.", "B2"),
    ("proxy", "/ˈprɒksi/", "máy chủ trung gian", "Connect via proxy.", "B2"),
    ("dns", "/ˌdiː en ˈes/", "hệ thống tên miền", "DNS resolution error.", "B2"),
    ("ip address", "/ˌaɪ ˈpiː əˈdres/", "địa chỉ IP", "Whitelist this IP.", "B1"),
    ("firewall", "/ˈfaɪəwɔːl/", "tường lửa", "Firewall blocked connection.", "B2"),
    ("encryption", "/ɪnˈkrɪpʃn/", "mã hóa", "Use AES encryption.", "B2"),
    ("decryption", "/diːˈkrɪpʃn/", "giải mã", "Decryption failed.", "B2"),
    ("hashing", "/ˈhæʃɪŋ/", "băm dữ liệu", "Password hashing.", "B2"),
    ("token", "/ˈtəʊkən/", "mã xác thực", "Refresh the token.", "B1"),
    ("jwt", "/ˌdʒeɪ dʌbljuː ˈtiː/", "JSON Web Token", "Decode the JWT.", "B2"),
    ("oauth", "/ˈəʊɔːθ/", "giao thức ủy quyền", "Login with OAuth.", "B2"),
    ("git", "/ɡɪt/", "hệ thống quản lý phiên bản", "Commit to git.", "B1"),
    ("branch", "/brɑːntʃ/", "nhánh", "Create a new branch.", "B1"),
    ("commit", "/kəˈmɪt/", "lưu thay đổi", "Commit message.", "B1"),
    ("merge", "/mɜːdʒ/", "gộp nhánh", "Merge pull request.", "B1"),
    ("conflict", "/ˈkɒnflɪkt/", "xung đột code", "Resolve merge conflicts.", "B2"),
    ("pull request", "/pʊl rɪˈkwest/", "yêu cầu gộp code", "Review the PR.", "B1"),
    ("clone", "/kləʊn/", "sao chép repo", "Clone the project.", "B1"),
    ("push", "/pʊʃ/", "đẩy code lên", "Push to origin.", "B1"),
    ("pull", "/pʊl/", "kéo code về", "Pull latest changes.", "B1"),
    ("fork", "/fɔːk/", "tách nhánh dự án", "Fork the repo.", "B2"),
    ("issue", "/ˈɪʃuː/", "vấn đề", "Report an issue.", "B1"),
    ("scrum", "/skrʌm/", "khung làm việc Agile", "Daily scrum meeting.", "B2"),
    ("agile", "/ˈædʒaɪl/", "phương pháp linh hoạt", "Agile development.", "B2"),
    ("sprint", "/sprɪnt/", "giai đoạn phát triển ngắn", "Two-week sprint.", "B1"),
    ("kanban", "/ˈkænbæn/", "bảng quản lý công việc", "Move card on Kanban.", "B2"),
    ("standup", "/ˈstændʌp/", "họp đứng hàng ngày", "Update in standup.", "B1"),
    ("backlog", "/ˈbæklɒɡ/", "danh sách công việc tồn", "Add to backlog.", "B1"),
    ("user story", "/ˈjuːzə ˈstɔːri/", "câu chuyện người dùng", "Write user stories.", "B1"),
    ("epic", "/ˈepɪk/", "công việc lớn", "Break down the epic.", "B2"),
    ("feature", "/ˈfiːtʃə/", "tính năng", "New feature request.", "A2"),
    ("specification", "/ˌspesɪfɪˈkeɪʃn/", "đặc tả", "Read specs carefully.", "B2"),
    ("prototype", "/ˈprəʊtətaɪp/", "nguyên mẫu", "Design a prototype.", "B2"),
    ("wireframe", "/ˈwaɪəfreɪm/", "khung xương giao diện", "Draw wireframes.", "B2"),
    ("mockup", "/ˈmɒkʌp/", "mô hình thiết kế", "Approve the mockup.", "B2"),
    ("responsive", "/rɪˈspɒnsɪv/", "tương thích thiết bị", "Responsive design.", "B1"),
    ("loop", "/luːp/", "vòng lặp", "Infinite loop error.", "A2"),
    ("condition", "/kənˈdɪʃn/", "điều kiện", "Check condition.", "A2"),
    ("class", "/klɑːs/", "lớp", "Define a class.", "B1"),
    ("object", "/ˈɒbdʒɪkt/", "đối tượng", "Create an object.", "B1"),
    ("inheritance", "/ɪnˈherɪtəns/", "kế thừa", "Class inheritance.", "B2"),
    ("polymorphism", "/ˌpɒliˈmɔːfɪzm/", "đa hình", "Support polymorphism.", "C1"),
    ("encapsulation", "/ɪnˌkæpsjuˈleɪʃn/", "đóng gói", "Data encapsulation.", "C1"),
    ("abstraction", "/æbˈstrækʃn/", "trừu tượng hóa", "Level of abstraction.", "C1"),
    ("constructor", "/kənˈstrʌktə/", "hàm khởi tạo", "Call constructor.", "B2"),
    ("destructor", "/dɪˈstrʌktə/", "hàm hủy", "Resource destructor.", "B2"),
    ("interface", "/ˈɪntəfeɪs/", "giao diện", "Implement interface.", "B1"),
    ("namespace", "/ˈneɪmspeɪs/", "không gian tên", "Avoid namespace pollution.", "B2"),
    ("module", "/ˈmɒdjuːl/", "mô-đun", "Import module.", "B1"),
    ("package", "/ˈpækɪdʒ/", "gói phần mềm", "Install package.", "B1"),
    ("library", "/ˈlaɪbri/", "thư viện", "Use standard library.", "B1"),
    ("framework", "/ˈfreɪmwɜːk/", "khung phần mềm", "Web framework.", "B1"),
    ("dependency", "/dɪˈpendənsi/", "phụ thuộc", "Manage dependencies.", "B2"),
    ("compiler", "/kəmˈpaɪlə/", "trình biên dịch", "Compiler error.", "B2"),
    ("interpreter", "/ɪnˈtɜːprɪtə/", "trình thông dịch", "Python interpreter.", "B2"),
    ("runtime", "/ˈrʌntaɪm/", "thời gian chạy", "Runtime error.", "B2"),
    ("exception", "/ɪkˈsepʃn/", "ngoại lệ", "Handle exception.", "B2"),
    ("stack trace", "/stæk treɪs/", "vết ngăn xếp", "Read stack trace.", "B2"),
    ("log", "/lɒɡ/", "nhật ký", "Check error logs.", "A2"),
    ("console", "/kənˈsəʊl/", "bảng điều khiển", "Print to console.", "A2"),
    ("terminal", "/ˈtɜːmɪnl/", "cửa sổ lệnh", "Open terminal.", "B1"),
    ("shell", "/ʃel/", "trình bao", "Shell script.", "B2"),
    ("script", "/skrɪpt/", "kịch bản", "Run build script.", "B1"),
    ("argument", "/ˈɑːɡjumənt/", "đối số", "Invalid argument.", "B1"),
    ("return", "/rɪˈtɜːn/", "trả về", "Return value.", "A1"),
    ("null", "/nʌl/", "rỗng", "Value is null.", "B1"),
    ("undefined", "/ˌʌndɪˈfaɪnd/", "chưa định nghĩa", "Variable is undefined.", "B1"),
    ("string", "/strɪŋ/", "chuỗi ký tự", "Parse string.", "B1"),
    ("integer", "/ˈɪntɪdʒə/", "số nguyên", "Convert to integer.", "B1"),
    ("boolean", "/ˈbuːliən/", "kiểu đúng sai", "Boolean flag.", "B1"),
    ("array", "/əˈreɪ/", "mảng", "Loop through array.", "B1"),
    ("list", "/lɪst/", "danh sách", "Add to list.", "A1"),
    ("dictionary", "/ˈdɪkʃənri/", "từ điển (cấu trúc dữ liệu)", "Key-value dictionary.", "B1"),
    ("queue", "/kjuː/", "hàng đợi", "Message queue.", "B2"),
    ("stack", "/stæk/", "ngăn xếp", "Stack overflow.", "B2"),
    ("linked list", "/lɪŋkt lɪst/", "danh sách liên kết", "Traverse linked list.", "B2"),
    ("tree", "/triː/", "cây (cấu trúc)", "Binary tree.", "B1"),
    ("graph", "/ɡrɑːf/", "đồ thị", "Graph algorithm.", "B2"),
    ("sort", "/sɔːt/", "sắp xếp", "Sort ascending.", "B1"),
    ("search", "/sɜːtʃ/", "tìm kiếm", "Binary search.", "B1"),
    ("recursion", "/rɪˈkɜːʃn/", "đệ quy", "Infinite recursion.", "C1"),
    ("iteration", "/ˌɪtəˈreɪʃn/", "lặp lại", "Next iteration.", "B2"),
    ("complexity", "/kəmˈpleksəti/", "độ phức tạp", "Time complexity.", "C1"),
    ("optimization", "/ˌɒptɪmaɪˈzeɪʃn/", "tối ưu hóa", "Memory optimization.", "C1"),
    ("performance", "/pəˈfɔːməns/", "hiệu năng", "High performance.", "B1"),
    ("scalability", "/ˌskeɪləˈbɪləti/", "khả năng mở rộng", "Horizontal scalability.", "C1"),
    ("reliability", "/rɪˌlaɪəˈbɪləti/", "độ tin cậy", "System reliability.", "B2"),
    ("maintainability", "/meɪnˌteɪnəˈbɪləti/", "khả năng bảo trì", "Code maintainability.", "B2"),
    ("usability", "/ˌjuːzəˈbɪləti/", "khả năng sử dụng", "Improve usability.", "B2"),
    ("accessibility", "/əkˌsesəˈbɪləti/", "khả năng truy cập", "Web accessibility.", "B2"),
]

for w, ipa, meaning, example, level in vocab_list:
    new_items.append({"type": "word", "term": w, "ipa": ipa, "meaning": meaning, "example": example, "level": level})

# --- QUIZZES ---
quizzes = [
    ("What does '404' usually mean?", ["Success", "Not Found", "Server Error", "Unauthorized"], 1, "404 Not Found is a standard HTTP status code."),
    ("Which is NOT a programming language?", ["Python", "HTML", "Java", "C++"], 1, "HTML is a markup language, not a programming language."),
    ("What does 'API' stand for?", ["App Process Info", "Application Programming Interface", "Apple Phone Inc", "Auto Path Integra"], 1, "API = Application Programming Interface."),
    ("What is a 'bug'?", ["A feature", "An error", "A virus", "A user"], 1, "A bug is an error or flaw in software."),
    ("What does 'Frontend' generally refer to?", ["Server database", "User Interface", "Operating System", "Network cables"], 1, "Frontend deals with the client-side/user interface."),
    ("To 'merge' code means to:", ["Delete it", "Combine it", "Hide it", "Print it"], 1, "Merging combines changes from branches."),
    ("Which data structure uses LIFO (Last In First Out)?", ["Queue", "Stack", "Array", "Tree"], 1, "Stack is LIFO."),
    ("What is 'Git' used for?", ["Photo editing", "Version control", "Listening to music", "Writing emails"], 1, "Git is a version control system."),
    ("What is 'SQL' used for?", ["Designing logos", "Databases", "Web styling", "Video games"], 1, "SQL is for database management."),
    ("What typically runs on port 80?", ["SSH", "HTTP", "FTP", "SMTP"], 1, "Port 80 is standard for HTTP web traffic."),
    ("What does 'GUI' stand for?", ["Global User Info", "Graphical User Interface", "General Unit Index", "Green UI"], 1, "GUI = Graphical User Interface."),
    ("Which is an Agile framework?", ["Waterfall", "Scrum", "Concrete", "Stone"], 1, "Scrum is an Agile framework."),
    ("What is a 'variable'?", ["A constant value", "A storage location with a name", "A hardware part", "A web page"], 1, "A variable stores data."),
    ("What does 'SSD' stand for?", ["Super Speed Disk", "Solid State Drive", "System Storage Device", "Slow Save Drive"], 1, "SSD = Solid State Drive."),
    ("In Python, what is used to define a block of code?", ["Brackets {}", "Indentation", "Semicolons ;", "Parentheses ()"], 1, "Python uses indentation."),
    ("What does 'HTML' check for?", ["Logic", "Structure", "Style", "Database"], 1, "HTML provides the structure of web pages."),
    ("What does 'CSS' stand for?", ["Computer Style Sheet", "Cascading Style Sheets", "Creative Style System", "Colorful Sheet Style"], 1, "CSS = Cascading Style Sheets."),
    ("A 'loop' is used to:", ["Stop a program", "Repeat code", "Delete files", "Network computers"], 1, "Loops repeat code blocks."),
    ("What represents 'True' or 'False'?", ["Integer", "Boolean", "String", "Float"], 1, "Boolean represents truth values."),
    ("What is 'Open Source'?", ["Free to modify code", "Closed software", "Paid software", "Virus"], 0, "Open source code is available for modification."),
]

for q, opts, ans, exp in quizzes:
    new_items.append({"type": "quiz", "question": q, "options": opts, "answer": ans, "explain": exp})

# --- GRAMMAR ---
grammar_points = [
    ("Conditional Type 0", "If + S + V(present), S + V(present)", "Sự thật hiển nhiên", "If you heat ice, it melts.", "if, when"),
    ("Conditional Type 1", "If + S + V(present), S + will + V", "Có thể xảy ra ở hiện tại/tương lai", "If it rains, I will stay home.", "if"),
    ("Conditional Type 2", "If + S + V(past), S + would + V", "Không có thật ở hiện tại", "If I were you, I would study harder.", "if"),
    ("Conditional Type 3", "If + S + had + V3, S + would + have + V3", "Không có thật ở quá khứ", "If I had known, I would have come.", "if"),
    ("Passive Voice (Present)", "S + am/is/are + V3", "Bị động hiện tại", "The report is written by him.", "by"),
    ("Passive Voice (Past)", "S + was/were + V3", "Bị động quá khứ", "The bug was fixed yesterday.", "by"),
    ("Passive Voice (Future)", "S + will be + V3", "Bị động tương lai", "The project will be finished soon.", "by"),
    ("Relative Clause (Who)", "N(person) + who + V...", "Mệnh đề quan hệ chỉ người", "The dev who wrote this is a genius.", "who"),
    ("Relative Clause (Which)", "N(thing) + which + V...", "Mệnh đề quan hệ chỉ vật", "The app which crashes often is bad.", "which"),
    ("Relative Clause (That)", "N + that + ...", "Thay cho Who/Which", "The tool that I use is free.", "that"),
    ("Modal Verbs (Can)", "S + can + V", "Khả năng", "I can code in Python.", "can"),
    ("Modal Verbs (Should)", "S + should + V", "Lời khuyên", "You should back up data.", "should"),
    ("Modal Verbs (Must)", "S + must + V", "Bắt buộc", "You must meet the deadline.", "must"),
    ("Modal Verbs (May/Might)", "S + may/might + V", "Khả năng thấp", "It might rain today.", "might"),
    ("Comparatives (Short adj)", "S + V + adj-er + than + N", "So sánh hơn tính từ ngắn", "This code is faster than yours.", "than"),
    ("Comparatives (Long adj)", "S + V + more + adj + than + N", "So sánh hơn tính từ dài", "Python is more popular than C.", "than"),
    ("Superlatives (Short adj)", "S + V + the + adj-est", "So sánh nhất tính từ ngắn", "It is the fastest server.", "the"),
    ("Superlatives (Long adj)", "S + V + the + most + adj", "So sánh nhất tính từ dài", "It is the most complex system.", "the most"),
    ("Gerunds (Verb as Noun)", "V-ing behaves like a noun", "Danh động từ", "Coding is fun.", "ing"),
    ("Infinitives (Purpose)", "To + V", "Chỉ mục đích", "I study to learn.", "to"),
    ("Reported Speech (Statement)", "S + said (that) + S + V(backshift)", "Câu tường thuật", "He said he was busy.", "said"),
    ("Reported Speech (Question)", "S + asked + if/wh- + S + V(backshift)", "Câu hỏi tường thuật", "She asked where I worked.", "asked"),
    ("Phrasal Verbs (Get up)", "get up", "thức dậy", "I get up at 6.", "up"),
    ("Phrasal Verbs (Turn on)", "turn on", "bật", "Turn on the computer.", "on"),
    ("Phrasal Verbs (Give up)", "give up", "từ bỏ", "Don't give up.", "up"),
    ("Phrasal Verbs (Look for)", "look for", "tìm kiếm", "I'm looking for a job.", "for"),
    ("Phrasal Verbs (Run out of)", "run out of", "hết", "We ran out of memory.", "out of"),
]

for t, f, u, e, s in grammar_points:
    new_items.append({"type": "grammar", "topic": t, "formula": f, "use": u, "signal": s, "example": e})

current_content = get_current_content()
current_content.extend(new_items)
save_content(current_content)

print(f"Added {len(new_items)} items. Total items: {len(current_content)}")
