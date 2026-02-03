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

# --- IDIOMS & PHRASES ---
idioms = [
    ("piece of cake", "/piːs əv keɪk/", "dễ như ăn bánh", "Testing this is a piece of cake.", "B2"),
    ("break the ice", "/breɪk ðə aɪs/", "phá vỡ sự ngại ngùng", "Play a game to break the ice.", "C1"),
    ("hit the nail on the head", "", "nói chính xác vấn đề", "You hit the nail on the head.", "C1"),
    ("cost an arm and a leg", "", "rất đắt đỏ", "This laptop costs an arm and a leg.", "C1"),
    ("let the cat out of the bag", "", "tiết lộ bí mật", "Who let the cat out of the bag?", "C1"),
    ("kill two birds with one stone", "", "một mũi tên trúng 2 đích", "Learn English while commuting.", "C1"),
    ("cutting corners", "", "làm tắt / làm ẩu", "Don't cut corners on security.", "C1"),
    ("miss the boat", "", "bỏ lỡ cơ hội", "Buy now or miss the boat.", "C1"),
    ("call it a day", "", "ngừng làm việc (trong ngày)", "Let's call it a day.", "B2"),
    ("hang in there", "", "kiên trì nhé", "Hang in there, almost done.", "B2"),
    ("better late than never", "", "thà muộn còn hơn không", "Late submission? Better late than never.", "B2"),
    ("so far so good", "", "mọi thứ vẫn ổn", "How is the project? So far so good.", "B2"),
    ("under the weather", "", "không khỏe", "I'm feeling under the weather.", "C1"),
    ("speak of the devil", "", "vừa nhắc đã tới", "Speak of the devil, here represents John.", "C1"),
    ("time flies", "", "thời gian trôi nhanh", "Time flies when coding.", "B2"),
    ("on the ball", "", "nhanh nhạy / hiểu việc", "She is really on the ball.", "C1"),
    ("burn the midnight oil", "", "thức khuya làm việc", "We burned the midnight oil for the release.", "C1"),
    ("once in a blue moon", "", "rất hiếm khi", "It happens once in a blue moon.", "C1"),
    ("the best of both worlds", "", "vẹn cả đôi đường", "Remote work offers the best of both worlds.", "C1"),
    ("see eye to eye", "", "đồng quan điểm", "We don't see eye to eye on this.", "C1"),
    ("rule of thumb", "", "quy tắc ngón tay cái / kinh nghiệm", "A good rule of thumb is to test early.", "C1"),
    ("out of the blue", "", "bất ngờ", "The error appeared out of the blue.", "B2"),
    ("get something off your chest", "", "nói ra cho nhẹ lòng", "Tell me, get it off your chest.", "C1"),
    ("go the extra mile", "", "nỗ lực hơn mong đợi", "We go the extra mile for clients.", "C1"),
    ("play it by ear", "", "tùy cơ ứng biến", "We don't have a plan, let's play it by ear.", "C1"),
    ("bite the bullet", "", "ngậm đắng nuốt cay / chấp nhận làm", "I have to bite the bullet and fix it.", "C1"),
    ("climb the ladder", "", "thăng tiến", "Climb the corporate ladder.", "C1"),
    ("keep an eye on", "", "để mắt tới", "Keep an eye on the server logs.", "B2"),
    ("give me a hand", "", "giúp tôi một tay", "Can you give me a hand?", "A2"),
    ("in the same boat", "", "cùng hội cùng thuyền", "We are all in the same boat.", "B2"),
]
for w, ipa, meaning, example, level in idioms:
    new_items.append({"type": "word", "term": w, "ipa": ipa or "N/A", "meaning": meaning, "example": example, "level": level})

# --- ADVANCED TECH & DATA VOCAB ---
tech_vocab = [
    ("artificial intelligence", "", "trí tuệ nhân tạo", "AI is changing the world.", "B2"),
    ("machine learning", "", "học máy", "Train the model with machine learning.", "C1"),
    ("neural network", "", "mạng nơ-ron", "Deep neural networks.", "C1"),
    ("blockchain", "", "công nghệ chuỗi khối", "Bitcoin uses blockchain.", "C1"),
    ("cryptocurrency", "", "tiền điện tử", "Invest in cryptocurrency.", "C1"),
    ("virtual reality", "", "thực tế ảo", "VR headset.", "B2"),
    ("augmented reality", "", "thực tế tăng cường", "AR app.", "C1"),
    ("internet of things", "", "vạn vật kết nối", "IoT devices.", "C1"),
    ("big data", "", "dữ liệu lớn", "Analyze big data.", "B2"),
    ("cloud computing", "", "điện toán đám mây", "Move to cloud computing.", "B2"),
    ("cybersecurity", "", "an ninh mạng", "Enhance cybersecurity.", "B2"),
    ("biometrics", "", "sinh trắc học", "Biometric authentication.", "C1"),
    ("automation", "", "tự động hóa", "Process automation.", "B2"),
    ("robotics", "", "người máy học", "Advances in robotics.", "C1"),
    ("quantum computing", "", "điện toán lượng tử", "Quantum computing speed.", "C1"),
    ("ethics", "", "đạo đức", "AI ethics.", "C1"),
    ("privacy", "", "quyền riêng tư", "Data privacy.", "B2"),
    ("surveillance", "", "giám sát", "Mass surveillance.", "C1"),
    ("bandwidth", "", "băng thông", "High bandwidth.", "B2"),
    ("latency", "", "độ trễ", "Low latency.", "C1"),
    ("redundancy", "", "dự phòng", "System redundancy.", "C1"),
    ("infrastructure", "", "cơ sở hạ tầng", "IT infrastructure.", "C1"),
    ("microservices", "", "vi dịch vụ", "Microservices architecture.", "C1"),
    ("monolith", "", "nguyên khối", "Monolithic app.", "C1"),
    ("containerization", "", "ảo hóa container", "Docker containerization.", "C1"),
    ("orchestration", "", "điều phối", "Kubernetes orchestration.", "C1"),
    ("serverless", "", "không máy chủ", "Serverless functions.", "C1"),
    ("devops", "", "phát triển vận hành", "DevOps culture.", "B2"),
    ("continuous integration", "", "tích hợp liên tục", "CI/CD pipeline.", "C1"),
    ("continuous deployment", "", "triển khai liên tục", "Deployed daily.", "C1"),
     ("legacy system", "", "hệ thống cũ", "Replace the legacy system.", "C1"),
    ("refactoring", "", "tái cấu trúc code", "Need refactoring.", "C1"),
    ("technical debt", "", "nợ kỹ thuật", "Pay down technical debt.", "C1"),
    ("scalability", "", "khả năng mở rộng", "Test scalability.", "C1"),
    ("bottleneck", "", "nút thắt cổ chai", "Identify bottlenecks.", "C1"),
    ("throughput", "", "lưu lượng xử lý", "Maximize throughput.", "C1"),
    ("load balancing", "", "cân bằng tải", "Use a load balancer.", "C1"),
    ("failover", "", "chuyển đổi dự phòng", "Automatic failover.", "C1"),
    ("uptime", "", "thời gian hoạt động", "99.9% uptime.", "B2"),
    ("downtime", "", "thời gian chết", "Minimize downtime.", "B2"),
]
for w, ipa, meaning, example, level in tech_vocab:
    new_items.append({"type": "word", "term": w, "ipa": ipa or "N/A", "meaning": meaning, "example": example, "level": level})

# --- GENERAL ADVANCED ---
gen_adv = [
    ("ambitious", "", "tham vọng", "Ambitious project.", "B2"),
    ("authentic", "", "xác thực / chân thật", "Authentic experience.", "C1"),
    ("comprehensive", "", "toàn diện", "Comprehensive guide.", "C1"),
    ("confidential", "", "bảo mật", "Confidential info.", "C1"),
    ("crucial", "", "cốt yếu", "Crucial component.", "B2"),
    ("deliberate", "", "cố ý / thận trọng", "Deliberate action.", "C1"),
    ("elaborate", "", "kỹ lưỡng / phức tạp", "Elaborate design.", "C1"),
    ("fragile", "", "mỏng manh", "Fragile ecosystem.", "B2"),
    ("genuine", "", "thật / chân thành", "Genuine interest.", "B2"),
    ("inevitable", "", "không thể tránh khỏi", "Change is inevitable.", "C1"),
    ("innovative", "", "đổi mới", "Innovative solution.", "B2"),
    ("mandatory", "", "bắt buộc", "Mandatory training.", "C1"),
    ("meticulous", "", "tỉ mỉ", "Meticulous planning.", "C1"),
    ("obsolete", "", "lỗi thời", "Obsolete technology.", "C1"),
    ("pragmatic", "", "thực tế", "Pragmatic approach.", "C1"),
    ("prominent", "", "nổi bật", "Prominent figure.", "C1"),
    ("resilient", "", "kiên cường / đàn hồi", "Resilient system.", "C1"),
    ("rigorous", "", "nghiêm ngặt", "Rigorous testing.", "C1"),
    ("simultaneous", "", "đồng thời", "Simultaneous requests.", "C1"),
    ("subtle", "", "tinh tế / nhỏ", "Subtle difference.", "C1"),
    ("sustainable", "", "bền vững", "Sustainable growth.", "B2"),
    ("tedious", "", "nhàm chán / tẻ nhạt", "Tedious task.", "C1"),
    ("temporary", "", "tạm thời", "Temporary fix.", "B1"),
    ("permanent", "", "vĩnh viễn", "Permanent storage.", "B1"),
    ("transparent", "", "minh bạch", "Transparent process.", "B2"),
    ("unanimous", "", "nhất trí", "Unanimous decision.", "C1"),
    ("unprecedented", "", "chưa từng có", "Unprecedented traffic.", "C1"),
    ("versatile", "", "đa năng", "Versatile tool.", "C1"),
    ("vulnerable", "", "dễ bị tổn thương", "Vulnerable to attacks.", "C1"),
     ("accumulate", "", "tích lũy", "Accumulate data.", "C1"),
    ("allocate", "", "phân bổ", "Allocate resources.", "C1"),
    ("anticipate", "", "dự đoán", "Anticipate problems.", "C1"),
    ("compensate", "", "đền bù", "Compensate for lag.", "C1"),
    ("consolidate", "", "hợp nhất / củng cố", "Consolidate servers.", "C1"),
    ("contradict", "", "mâu thuẫn", "Contradict the specs.", "C1"),
    ("deviate", "", "chệch hướng", "Deviate from plan.", "C1"),
    ("diminish", "", "giảm bớt", "Diminish risk.", "C1"),
    ("eliminate", "", "loại bỏ", "Eliminate waste.", "B2"),
    ("emphasize", "", "nhấn mạnh", "Emphasize security.", "B2"),
    ("enhance", "", "nâng cao", "Enhance performance.", "B2"),
    ("establishing", "", "thành lập", "Establishing connection.", "B2"),
    ("evaluate", "", "đánh giá", "Evaluate the code.", "C1"),
    ("exaggerate", "", "phóng đại", "Don't exaggerate.", "B2"),
    ("facilitate", "", "tạo điều kiện", "Facilitate meetings.", "C1"),
    ("fluctuate", "", "biến động", "Speed fluctuates.", "C1"),
    ("generate", "", "tạo ra", "Generate output.", "B1"),
    ("ignore", "", "phớt lờ", "Ignore warnings.", "A2"),
    ("imply", "", "ngụ ý", "Imply consent.", "C1"),
    ("initiate", "", "khởi xướng", "Initiate scan.", "C1"),
]
for w, ipa, meaning, example, level in gen_adv:
    new_items.append({"type": "word", "term": w, "ipa": ipa or "N/A", "meaning": meaning, "example": example, "level": level})

# --- MORE QUIZZES ---
quizzes = [
    ("What does 'break the ice' mean?", ["Destroy ice", "Start conversation", "End meeting", "Freeze"], 1, "Break the ice means to start a conversation to reduce tension."),
    ("If something implies 'mandatory', it is:", ["Optional", "Required", "Suggested", "Forbidden"], 1, "Mandatory means required."),
    ("Synonym for 'obsolete':", ["New", "Modern", "Outdated", "Funny"], 2, "Obsolete means outdated."),
    ("Antonym for 'permanent':", ["Forever", "Temporary", "Lasting", "Stable"], 1, "Temporary is opposite to permanent."),
    ("What is 'redundancy' in IT?", ["Unnecessary repetition for backup", "Deleting files", "Writing code", "Selling products"], 0, "Redundancy provides backup."),
    ("To 'allocate' resources means to:", ["Throw away", "Assign/Distribute", "Eat", "Hide"], 1, "Allocate means to assign/distribute."),
    ("If a system is 'resilient', it:", ["Breaks easily", "Recovers quickly", "Is slow", "Is expensive"], 1, "Resilient means recovers quickly."),
    ("What implies 'prioritizing'?", ["Ignoring everything", "Doing important things first", "Sleeping", "Eating"], 1, "Prioritizing means ranking by importance."),
    ("A 'bottleneck' causes:", ["Speed", "Slowdown", "Success", "Money"], 1, "A bottleneck slows things down."),
    ("To 'mitigate' risk means to:", ["Increase it", "Reduce it", "Ignore it", "Buy it"], 1, "Mitigate means to reduce severity."),
    ("Which is a 'soft skill'?", ["Python", "Communication", "SQL", "Linux"], 1, "Communication is a soft skill."),
    ("What does 'scalability' measure?", ["Weight", "Ability to grow/handle load", "Price", "Color"], 1, "Scalability is ability to grow."),
    ("Idiom 'Cost an arm and a leg' means:", ["Cheap", "Expensive", "Free", "Painful"], 1, "It means very expensive."),
    ("What is a 'milestone'?", ["A rock", "A significant event/goal", "A mistake", "A lunch break"], 1, "Milestone is a significant point/achievement."),
    ("To 'brainstorm' means to:", ["Generate ideas", "Have a headache", "Wash brain", "Sleep"], 0, "Brainstorming is generating ideas."),
    ("Which word describes 'doing many things at once'?", ["Singular", "Multitasking", "Focusing", "Sleeping"], 1, "Multitasking."),
    ("To 'verify' is to:", ["Guess", "Check correctness", "Delete", "Ignore"], 1, "Verify means to check correctness."),
    ("A 'bug' in a plan is:", ["An insect", "A flaw/problem", "A feature", "A bonus"], 1, "In this context, a bug is a flaw."),
    ("If you are 'proactive', you:", ["Wait for orders", "Act in advance", "Sleep late", "Complain"], 1, "Proactive means acting in advance."),
    ("What is 'feedback'?", ["Food", "Comments/Evaluation", "Back button", "Music"], 1, "Feedback is comments or evaluation."),
]
for q, opts, ans, exp in quizzes:
    new_items.append({"type": "quiz", "question": q, "options": opts, "answer": ans, "explain": exp})
    
current_content = get_current_content()
current_content.extend(new_items)
save_content(current_content)

print(f"Added {len(new_items)} items. Total items: {len(current_content)}")
