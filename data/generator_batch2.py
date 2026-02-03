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

# --- VOCABULARY (Business & General) ---
vocab_list = [
    # Business
    ("agenda", "/əˈdʒendə/", "chương trình nghị sự", "Review the agenda.", "B1"),
    ("minutes", "/ˈmɪnɪts/", "biên bản cuộc họp", "Take the minutes.", "B2"),
    ("proposal", "/prəˈpəʊzl/", "đề xuất", "Submit a proposal.", "B1"),
    ("strategy", "/ˈstrætədʒi/", "chiến lược", "Marketing strategy.", "B2"),
    ("competitor", "/kəmˈpetɪtə/", "đối thủ cạnh tranh", "Analyze competitors.", "B1"),
    ("market share", "/ˈmɑːkɪt ʃeə/", "thị phần", "Increase market share.", "B2"),
    ("revenue", "/ˈrevənjuː/", "doanh thu", "Annual revenue.", "B2"),
    ("profit", "/ˈprɒfɪt/", "lợi nhuận", "Net profit.", "B1"),
    ("investment", "/ɪnˈvestmənt/", "đầu tư", "Return on investment.", "B2"),
    ("budget", "/ˈbʌdʒɪt/", "ngân sách", "Tight budget.", "B1"),
    ("negotiation", "/nɪˌɡəʊʃiˈeɪʃn/", "đàm phán", "Salary negotiation.", "B2"),
    ("contract", "/ˈkɒntrækt/", "hợp đồng", "Sign the contract.", "B1"),
    ("partner", "/ˈpɑːtnə/", "đối tác", "Business partner.", "A2"),
    ("collaboration", "/kəˌlæbəˈreɪʃn/", "hợp tác", "Team collaboration.", "B2"),
    ("deadline", "/ˈdedlaɪn/", "hạn chót", "Meet the deadline.", "B1"),
    ("schedule", "/ˈʃedjuːl/", "lịch trình", "On schedule.", "A2"),
    ("appointment", "/əˈpɔɪntmənt/", "cuộc hẹn", "Make an appointment.", "A2"),
    ("vacancy", "/ˈveɪkənsi/", "vị trí trống", "Job vacancy.", "B2"),
    ("recruit", "/rɪˈkruːt/", "tuyển dụng", "Recruit new staff.", "B2"),
    ("candidate", "/ˈkændɪdət/", "ứng viên", "Interview the candidate.", "B1"),
    ("resume", "/ˈrezjuːmeɪ/", "sơ yếu lý lịch", "Send your resume.", "B1"),
    ("salary", "/ˈsæləri/", "lương", "Monthly salary.", "A2"),
    ("bonus", "/ˈbəʊnəs/", "tiền thưởng", "Year-end bonus.", "A2"),
    ("promotion", "/prəˈməʊʃn/", "thăng chức / khuyến mãi", "Get a promotion.", "B1"),
    ("resign", "/rɪˈzaɪn/", "từ chức", "He resigned yesterday.", "B2"),
    ("retire", "/rɪˈtaɪə/", "nghỉ hưu", "Retire at 60.", "B1"),
    ("colleague", "/ˈkɒliːɡ/", "đồng nghiệp", "Ask a colleague.", "A2"),
    ("supervisor", "/ˈsuːpəvaɪzə/", "người giám sát", "Report to supervisor.", "B2"),
    ("executive", "/ɪɡˈzekjətɪv/", "điều hành", "Chief Executive Officer.", "C1"),
    ("entrepreneur", "/ˌɒntrəprəˈnɜː/", "doanh nhân", "Successful entrepreneur.", "C1"),
    
    # General / Daily
    ("commute", "/kəˈmjuːt/", "đi lại (đi làm)", "Long daily commute.", "B2"),
    ("traffic jam", "/ˈtræfɪk dʒæm/", "tắc đường", "Stuck in a traffic jam.", "A2"),
    ("vehicle", "/ˈviːəkl/", "xe cộ", "Electric vehicle.", "B1"),
    ("purchase", "/ˈpɜːtʃəs/", "mua", "Purchase online.", "B1"),
    ("affordable", "/əˈfɔːdəbl/", "giá cả phải chăng", "Affordable price.", "B1"),
    ("expensive", "/ɪkˈspensɪv/", "đắt", "Too expensive.", "A1"),
    ("bargain", "/ˈbɑːɡɪn/", "mặc cả / món hời", "A real bargain.", "B2"),
    ("refund", "/ˈriːfʌnd/", "hoàn tiền", "Ask for a refund.", "B1"),
    ("receipt", "/rɪˈsiːt/", "hóa đơn", "Keep the receipt.", "B1"),
    ("warranty", "/ˈwɒrənti/", "bảo hành", "Under warranty.", "B2"),
    ("complaint", "/kəmˈpleɪnt/", "phàn nàn", "Customer complaint.", "B1"),
    ("solution", "/səˈluːʃn/", "giải pháp", "Find a solution.", "A2"),
    ("suggestion", "/səˈdʒestʃən/", "gợi ý", "Make a suggestion.", "B1"),
    ("opinion", "/əˈpɪnjən/", "ý kiến", "In my opinion.", "A2"),
    ("feedback", "/ˈfiːdbæk/", "phản hồi", "Give feedback.", "B1"),
    ("inconvenience", "/ˌɪnkənˈviːniəns/", "sự bất tiện", "Sorry for the inconvenience.", "B2"),
    ("opportunity", "/ˌɒpəˈtjuːnəti/", "cơ hội", "Missed opportunity.", "B1"),
    ("advantage", "/ədˈvɑːntɪdʒ/", "lợi thế", "Competitive advantage.", "B1"),
    ("disadvantage", "/ˌdɪsədˈvɑːntɪdʒ/", "bất lợi", "Main disadvantage.", "B1"),
    ("benefit", "/ˈbenɪfɪt/", "lợi ích", "Health benefits.", "B1"),
    ("challenge", "/ˈtʃælɪndʒ/", "thử thách", "Face a challenge.", "B1"),
    ("success", "/səkˈses/", "thành công", "Huge success.", "A1"),
    ("failure", "/ˈfeɪljə/", "thất bại", "Learn from failure.", "B1"),
    ("progress", "/ˈprəʊɡres/", "tiến bộ", "Make progress.", "B1"),
    ("development", "/dɪˈveləpmənt/", "phát triển", "Software development.", "B1"),
    ("environment", "/ɪnˈvaɪrənmənt/", "môi trường", "Protect the environment.", "A2"),
    ("pollution", "/pəˈluːʃn/", "ô nhiễm", "Air pollution.", "B1"),
    ("climate", "/ˈklaɪmət/", "khí hậu", "Climate change.", "B1"),
    ("global", "/ˈɡləʊbl/", "toàn cầu", "Global warming.", "B1"),
    ("sustainable", "/səˈsteɪnəbl/", "bền vững", "Sustainable energy.", "B2"),
    ("culture", "/ˈkʌltʃə/", "văn hóa", "Corporate culture.", "A2"),
    ("tradition", "/trəˈdɪʃn/", "truyền thống", "Local tradition.", "B1"),
    ("habit", "/ˈhæbɪt/", "thói quen", "Good habit.", "A2"),
    ("routine", "/ruːˈtiːn/", "thói quen hàng ngày", "Daily routine.", "B1"),
    ("lifestyle", "/ˈlaɪfstaɪl/", "lối sống", "Healthy lifestyle.", "A2"),
    ("health", "/helθ/", "sức khỏe", "Mental health.", "A1"),
    ("disease", "/dɪˈziːz/", "bệnh tật", "Cure the disease.", "B1"),
    ("symptom", "/ˈsɪmptəm/", "triệu chứng", "Flu symptoms.", "B2"),
    ("medicine", "/ˈmedsn/", "thuốc", "Take medicine.", "A2"),
    ("treatment", "/ˈtriːtmənt/", "điều trị", "Medical treatment.", "B1"),
    ("exercise", "/ˈeksəsaɪz/", "tập thể dục", "Regular exercise.", "A1"),
    ("nutrition", "/njuˈtrɪʃn/", "dinh dưỡng", "Good nutrition.", "B2"),
    ("diet", "/ˈdaɪət/", "chế độ ăn", "Balanced diet.", "A2"),
    ("ingredient", "/ɪnˈɡriːdiənt/", "nguyên liệu", "Fresh ingredients.", "B1"),
    ("recipe", "/ˈresəpi/", "công thức nấu ăn", "Follow the recipe.", "A2"),
    ("delicious", "/dɪˈlɪʃəs/", "ngon", "Delicious food.", "A1"),
    ("reservation", "/ˌrezəˈveɪʃn/", "đặt chỗ", "Dinner reservation.", "B1"),
    ("accommodation", "/əˌkɒməˈdeɪʃn/", "chỗ ở", "Book accommodation.", "B2"),
    ("transportation", "/ˌtrænspɔːˈteɪʃn/", "giao thông", "Public transportation.", "B1"),
    ("destination", "/ˌdestɪˈneɪʃn/", "điểm đến", "Holiday destination.", "B1"),
    ("document", "/ˈdɒkjumənt/", "tài liệu", "Sign the document.", "A2"),
    ("announcement", "/əˈnaʊnsmənt/", "thông báo", "Make an announcement.", "B1"),
    ("permission", "/pəˈmɪʃn/", "sự cho phép", "Ask for permission.", "B1"),
    ("signature", "/ˈsɪɡnətʃə/", "chữ ký", "Digital signature.", "B1"),
    
    # 50 More words
    ("available", "/əˈveɪləbl/", "có sẵn", "Is it available?", "A2"),
    ("unavailable", "/ˌʌnəˈveɪləbl/", "không có sẵn", "Currently unavailable.", "B1"),
    ("necessary", "/ˈnesəsəri/", "cần thiết", "It is necessary.", "B1"),
    ("unnecessary", "/ʌnˈnesəsəri/", "không cần thiết", "Cut unnecessary costs.", "B1"),
    ("urgent", "/ˈɜːdʒənt/", "khẩn cấp", "Urgent matter.", "B1"),
    ("important", "/ɪmˈpɔːtnt/", "quan trọng", "Important meeting.", "A1"),
    ("significant", "/sɪɡˈnɪfɪkənt/", "đáng kể", "Significant change.", "B2"),
    ("minor", "/ˈmaɪnə/", "nhỏ", "Minor bug.", "B1"),
    ("major", "/ˈmeɪdʒə/", "lớn", "Major update.", "B1"),
    ("various", "/ˈveəriəs/", "đa dạng", "Various options.", "B1"),
    ("specific", "/spəˈsɪfɪk/", "cụ thể", "Be specific.", "B1"),
    ("general", "/ˈdʒenrəl/", "chung", "General idea.", "A2"),
    ("detail", "/ˈdiːteɪl/", "chi tiết", "In detail.", "A2"),
    ("summary", "/ˈsʌməri/", "tóm tắt", "Executive summary.", "B1"),
    ("conclusion", "/kənˈkluːʒn/", "kết luận", "Reach a conclusion.", "B1"),
    ("introduction", "/ˌɪntrəˈdʌkʃn/", "giới thiệu", "Brief introduction.", "A2"),
    ("background", "/ˈbækɡraʊnd/", "nền tảng", "Technical background.", "B1"),
    ("experience", "/ɪkˈspɪəriəns/", "kinh nghiệm", "User experience.", "A2"),
    ("knowledge", "/ˈnɒlɪdʒ/", "kiến thức", "Basic knowledge.", "B1"),
    ("skill", "/skɪl/", "kỹ năng", "Soft skills.", "A2"),
    ("ability", "/əˈbɪləti/", "khả năng", "Ability to learn.", "B1"),
    ("talent", "/ˈtælənt/", "tài năng", "Hidden talent.", "B1"),
    ("effort", "/ˈefət/", "nỗ lực", "Make an effort.", "B1"),
    ("attempt", "/əˈtempt/", "cố gắng (danh từ/động từ)", "First attempt.", "B2"),
    ("result", "/rɪˈzʌlt/", "kết quả", "Test results.", "A2"),
    ("outcome", "/ˈaʊtkʌm/", "hậu quả/kết quả", "Project outcome.", "C1"),
    ("impact", "/ˈɪmpækt/", "tác động", "High impact.", "B2"),
    ("influence", "/ˈɪnfluəns/", "ảnh hưởng", "Influence behavior.", "B2"),
    ("effect", "/ɪˈfekt/", "hiệu quả/tác dụng", "Side effects.", "B1"),
    ("cause", "/kɔːz/", "nguyên nhân", "Root cause.", "B1"),
    ("reason", "/ˈriːzn/", "lý do", "Main reason.", "A1"),
    ("purpose", "/ˈpɜːpəs/", "mục đích", "Purpose of visit.", "B1"),
    ("goal", "/ɡəʊl/", "mục tiêu", "Set a goal.", "A2"),
    ("target", "/ˈtɑːɡɪt/", "mục tiêu (số liệu)", "Sales target.", "B1"),
    ("objective", "/əbˈdʒektɪv/", "mục tiêu cụ thể", "Learning objectives.", "B2"),
    ("method", "/ˈmeθəd/", "phương pháp", "Payment method.", "B1"),
    ("technique", "/tekˈniːk/", "kỹ thuật", "Coding technique.", "B1"),
    ("approach", "/əˈprəʊtʃ/", "cách tiếp cận", "New approach.", "B2"),
    ("process", "/ˈprəʊses/", "quy trình", "Recruitment process.", "B1"),
    ("procedure", "/prəˈsiːdʒə/", "thủ tục", "Standard procedure.", "B2"),
    ("policy", "/ˈpɒləsi/", "chính sách", "Company policy.", "B1"),
    ("regulation", "/ˌreɡjuˈleɪʃn/", "quy định", "Safety regulations.", "B2"),
    ("rule", "/ruːl/", "quy tắc", "Follow the rules.", "A1"),
    ("law", "/lɔː/", "luật", "Against the law.", "B1"),
    ("standard", "/ˈstændəd/", "tiêu chuẩn", "Industry standard.", "B1"),
    ("quality", "/ˈkwɒləti/", "chất lượng", "High quality.", "A2"),
    ("quantity", "/ˈkwɒntəti/", "số lượng", "Large quantity.", "B1"),
    ("increase", "/ɪnˈkriːs/", "tăng", "Increase sales.", "A2"),
    ("decrease", "/dɪˈkriːs/", "giảm", "Decrease costs.", "A2"),
    ("reduce", "/rɪˈdjuːs/", "giảm bớt", "Reduce waste.", "B1"),
]

for w, ipa, meaning, example, level in vocab_list:
    new_items.append({"type": "word", "term": w, "ipa": ipa, "meaning": meaning, "example": example, "level": level})

# --- QUIZZES ---
quizzes = [
    ("Which word is a synonym for 'employee'?", ["Boss", "Manager", "Staff", "Director"], 2, "Staff usually refers to employees."),
    ("To 'resign' means to:", ["Start a job", "Quit a job", "Get fired", "Get promoted"], 1, "Resign means to voluntarily leave a job."),
    ("What is an 'agenda'?", ["A list of topics for a meeting", "A type of computer", "A salary bonus", "A holiday"], 0, "Agenda is a meeting plan."),
    ("A 'deadline' is:", ["A starting line", "A time limit", "A dead phone", "A long meeting"], 1, "Deadline is the time by which something must be done."),
    ("If something is 'urgent', it requires:", ["No time", "More money", "Immediate attention", "Less people"], 2, "Urgent means it needs immediate action."),
    ("He is my 'colleague'. He is my:", ["Father", "Son", "Coworker", "Enemy"], 2, "Colleague means coworker."),
    ("What does 'CEO' stand for?", ["Chief Entertainment Officer", "Chief Executive Officer", "Company Energy Output", "Central Entry Option"], 1, "CEO = Chief Executive Officer."),
    ("Which word means 'lack of jobs'?", ["Employment", "Unemployment", "Promotion", "Retirement"], 1, "Unemployment means lack of jobs."),
    ("To 'recruit' means to:", ["Fire people", "Hire new people", "Train people", "Pay people"], 1, "Recruit means to hire."),
    ("A 'resume' is used for:", ["Cooking", "Job application", "Travel", "Shopping"], 1, "A resume (CV) is for job applications."),
    ("The opposite of 'profit' is:", ["Revenue", "Loss", "Salary", "Bonus"], 1, "Loss is the opposite of profit."),
    ("What do you pay to the government?", ["Salary", "Tax", "Profit", "Loan"], 1, "You pay tax to the government."),
    ("Which is NOT a department?", ["HR", "Marketing", "Sales", "Laptop"], 3, "Laptop is a device, not a department."),
    ("To 'negotiate' means to:", ["Discuss to reach agreement", "Fight physically", "Run away", "Sleep"], 0, "Negotiate implies discussion for agreement."),
    ("A 'contract' is a:", ["Phone", "Vehicle", "Legal agreement", "Building"], 2, "Contract is a legal agreement."),
]

for q, opts, ans, exp in quizzes:
    new_items.append({"type": "quiz", "question": q, "options": opts, "answer": ans, "explain": exp})

# --- GRAMMAR ---
grammar_points = [
    ("Verb Patterns (Verb + to V)", "S + V + to V", "Động từ theo sau là to V", "I want to learn English.", "want, hope, decide"),
    ("Verb Patterns (Verb + V-ing)", "S + V + V-ing", "Động từ theo sau là V-ing", "I enjoy coding.", "enjoy, avoid, finish"),
    ("Would rather", "S + would rather + V", "Thích làm gì hơn", "I would rather stay home.", "than"),
    ("Had better", "S + had better + V", "Nên làm gì (cảnh báo)", "You had better hurry.", "not"),
    ("Enough (Adj)", "S + be + adj + enough + (to V)", "Đủ... để làm gì", "He is old enough to drive.", "enough"),
    ("Too (Adj)", "S + be + too + adj + (for O) + to V", "Quá... để làm gì", "It's too hot to work.", "too"),
    ("So... that", "S + be + so + adj + that + S + V", "Quá... đến nỗi mà", "He was so tired that he slept.", "so...that"),
    ("Such... that", "S + V + such + (a/an) + adj + N + that + S + V", "Quá... đến nỗi mà", "It was such a good book that I finished it.", "such...that"),
    ("Tag Questions (Positive)", "S + V(pos)..., aux(neg)?", "Câu hỏi đuôi", "You are a dev, aren't you?", "isn't it?"),
    ("Tag Questions (Negative)", "S + V(neg)..., aux(pos)?", "Câu hỏi đuôi", "He doesn't like bugs, does he?", "does he?"),
    ("Causative (Have)", "S + have + O + V(bare)", "Nhờ ai làm gì", "I execute the script.", "have someone do"),
    ("Causative (Have - Passive)", "S + have + O + V3", "Có cái gì được làm", "I had my car fixed.", "have something done"),
    ("Inversion (Never)", "Never + aux + S + V", "Đảo ngữ với Never", "Never have I seen such a bug.", "never"),
    ("Inversion (Not only)", "Not only + aux + S + ... but + S + also...", "Không những... mà còn", "Not only is he smart, but he is also kind.", "not only"),
]

for t, f, u, e, s in grammar_points:
    new_items.append({"type": "grammar", "topic": t, "formula": f, "use": u, "signal": s, "example": e})

current_content = get_current_content()
current_content.extend(new_items)
save_content(current_content)

print(f"Added {len(new_items)} items. Total items: {len(current_content)}")
