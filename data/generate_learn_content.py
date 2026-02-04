# -*- coding: utf-8 -*-
"""Generate learn_content.json with ~200 lessons for tab Học (đầy đủ, rõ ràng)."""
import json

def lesson(type_, id_, title, definition, formula, examples, usage, signals, usage_en=None):
    d = {
        "type": "lesson",
        "id": id_,
        "title": title,
        "definition": definition,
        "formula": formula,
        "examples": examples,
        "usage": usage,
        "signals": signals
    }
    if usage_en is not None:
        d["usageEn"] = usage_en
    return d

def tbl(headers, rows):
    return {"headers": headers, "rows": rows}

lessons = []

# ========== 1-5: Đã có (giữ nguyên 5 bài thì đầu) ==========
lessons.append(lesson(
    "lesson", "present-simple",
    "Thì hiện tại đơn - Present Simple Tense",
    "Thì hiện tại đơn (Present simple) là thì được dùng để diễn tả những hành động, đặc điểm và thói quen đang diễn ra trong hiện tại.",
    tbl(["Loại câu", "Động từ thường", "Động từ to be"], [
        ["Khẳng định", "S + V1 (V-s/es với ngôi 3 số ít)", "S + am/is/are"],
        ["Phủ định", "S + do not/does not + V-inf", "S + am not/is not/are not"],
        ["Nghi vấn (Yes/No)", "Do/Does + S + V-inf?", "Am/Is/Are + S + ...?"],
        ["Nghi vấn (thông tin)", "Từ hỏi + do/does + S + V-inf?", "Từ hỏi + am/is/are + S?"]
    ]),
    tbl(["Loại câu", "Ví dụ động từ thường", "Ví dụ động từ to be"], [
        ["Khẳng định", "I play football every day.", "She is a teacher."],
        ["Phủ định", "I do not like coffee.", "He is not happy."],
        ["Nghi vấn", "Do you like pizza?", "Is she your friend?"]
    ]),
    [
        "Diễn tả hiện tượng, quy luật chung khó thay đổi.",
        "Diễn tả thói quen, sở thích hoặc quan điểm.",
        "Diễn tả hành động cảm nhận bằng giác quan tại thời điểm nói.",
        "Diễn tả lịch trình đã định sẵn (tàu, xe, máy bay)."
    ],
    "Often, Always, Usually, Frequently, Seldom, Rarely, Sometimes, Every day/week.",
    ["Describe general truths and scientific facts.", "Describe habits, preferences or opinions.", "Describe actions perceived by senses at the moment of speaking.", "Describe fixed schedules (transport, etc.)."]
))

lessons.append(lesson(
    "lesson", "present-continuous",
    "Thì hiện tại tiếp diễn - Present Continuous Tense",
    "Thì hiện tại tiếp diễn dùng để diễn tả hành động đang xảy ra tại thời điểm nói hoặc xung quanh thời điểm nói.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + am/is/are + V-ing"],
        ["Phủ định", "S + am not/is not/are not + V-ing"],
        ["Nghi vấn", "Am/Is/Are + S + V-ing?"]
    ]),
    tbl(["Loại câu", "Ví dụ"], [
        ["Khẳng định", "She is reading now."],
        ["Phủ định", "They are not playing games."],
        ["Nghi vấn", "Are you listening to me?"]
    ]),
    [
        "Hành động đang xảy ra tại thời điểm nói.",
        "Hành động tạm thời, chưa kết thúc.",
        "Kế hoạch đã định trước trong tương lai gần.",
        "Sự phàn nàn (với always)."
    ],
    "Now, Right now, At the moment, Look!, Listen!, Currently, This week/month.",
    ["Action happening at the moment of speaking.", "Temporary action, not finished.", "Pre-arranged plan in the near future.", "Complaint (with always)."]
))

lessons.append(lesson(
    "lesson", "present-perfect",
    "Thì hiện tại hoàn thành - Present Perfect Tense",
    "Thì hiện tại hoàn thành diễn tả hành động đã xảy ra trong quá khứ nhưng còn liên quan đến hiện tại hoặc kết quả còn lưu đến hiện tại.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + have/has + V3"],
        ["Phủ định", "S + have not/has not + V3"],
        ["Nghi vấn", "Have/Has + S + V3?"]
    ]),
    tbl(["Loại câu", "Ví dụ"], [
        ["Khẳng định", "I have finished my homework."],
        ["Phủ định", "She has not seen that film."],
        ["Nghi vấn", "Have you ever been to Japan?"]
    ]),
    [
        "Hành động vừa mới xảy ra (just).",
        "Kinh nghiệm cho đến hiện tại (ever, never).",
        "Hành động trong quá khứ, kết quả còn ở hiện tại.",
        "Hành động bắt đầu trong quá khứ và tiếp tục đến hiện tại."
    ],
    "Just, Already, Yet, Ever, Never, Since, For, So far, Recently, Lately.",
    ["Action that just happened (just).", "Experience up to the present (ever, never).", "Past action with result in the present.", "Action started in the past and continues to the present."]
))

lessons.append(lesson(
    "lesson", "past-simple",
    "Thì quá khứ đơn - Past Simple Tense",
    "Thì quá khứ đơn dùng để diễn tả hành động đã xảy ra và đã kết thúc trong quá khứ, biết rõ thời gian.",
    tbl(["Loại câu", "Động từ thường", "Động từ to be"], [
        ["Khẳng định", "S + V2", "S + was/were"],
        ["Phủ định", "S + did not + V-inf", "S + was not/were not"],
        ["Nghi vấn", "Did + S + V-inf?", "Was/Were + S + ...?"]
    ]),
    tbl(["Loại câu", "Ví dụ"], [
        ["Khẳng định", "I went to school yesterday."],
        ["Phủ định", "She did not come to the party."],
        ["Nghi vấn", "Did you see him last week?"]
    ]),
    [
        "Hành động đã xảy ra và chấm dứt trong quá khứ.",
        "Thói quen trong quá khứ (đã chấm dứt).",
        "Chuỗi hành động xảy ra liên tiếp trong quá khứ."
    ],
    "Yesterday, Last week/month/year, Ago, In 2020, When I was young.",
    ["Action that happened and ended in the past.", "Past habit (no longer continued).", "Sequence of actions in the past."]
))

lessons.append(lesson(
    "lesson", "future-simple",
    "Thì tương lai đơn - Future Simple Tense",
    "Thì tương lai đơn dùng để diễn tả hành động sẽ xảy ra trong tương lai, quyết định tại thời điểm nói.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + will + V-inf"],
        ["Phủ định", "S + will not (won't) + V-inf"],
        ["Nghi vấn", "Will + S + V-inf?"]
    ]),
    tbl(["Loại câu", "Ví dụ"], [
        ["Khẳng định", "I will call you tomorrow."],
        ["Phủ định", "She will not go to the meeting."],
        ["Nghi vấn", "Will you marry me?"]
    ]),
    [
        "Dự đoán về tương lai.",
        "Quyết định đột xuất tại thời điểm nói.",
        "Lời hứa, đề nghị, yêu cầu.",
        "Câu điều kiện loại I."
    ],
    "Tomorrow, Next week/month/year, In the future, Soon, In + thời gian.",
    ["Prediction about the future.", "Sudden decision at the moment of speaking.", "Promise, offer, request.", "First conditional."]
))

# ========== 6-12: Các thì còn lại ==========
lessons.append(lesson(
    "lesson", "past-continuous",
    "Thì quá khứ tiếp diễn - Past Continuous Tense",
    "Thì quá khứ tiếp diễn diễn tả hành động đang xảy ra tại một thời điểm trong quá khứ hoặc khi có hành động khác xen vào.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + was/were + V-ing"],
        ["Phủ định", "S + was not/were not + V-ing"],
        ["Nghi vấn", "Was/Were + S + V-ing?"]
    ]),
    tbl(["Ví dụ"], [
        ["I was studying when she called."],
        ["They were playing football at 5pm yesterday."]
    ]),
    [
        "Hành động đang xảy ra tại một thời điểm trong quá khứ.",
        "Hành động đang xảy ra thì có hành động khác xen vào (when/while).",
        "Hai hành động song song trong quá khứ (while)."
    ],
    "While, When, At that time, At 5pm yesterday, All day/week."
))

lessons.append(lesson(
    "lesson", "past-perfect",
    "Thì quá khứ hoàn thành - Past Perfect Tense",
    "Thì quá khứ hoàn thành diễn tả hành động xảy ra trước một hành động khác hoặc trước một thời điểm trong quá khứ.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + had + V3"],
        ["Phủ định", "S + had not + V3"],
        ["Nghi vấn", "Had + S + V3?"]
    ]),
    tbl(["Ví dụ"], [
        ["She had left before I arrived."],
        ["By 2020, I had graduated from university."]
    ]),
    [
        "Hành động xảy ra trước một hành động khác trong quá khứ.",
        "Hành động xảy ra trước một thời điểm trong quá khứ (by + time).",
        "Trong câu điều kiện loại 3."
    ],
    "Before, After, By the time, By 2020, Already, Just, Never."
))

lessons.append(lesson(
    "lesson", "future-continuous",
    "Thì tương lai tiếp diễn - Future Continuous Tense",
    "Thì tương lai tiếp diễn diễn tả hành động sẽ đang xảy ra tại một thời điểm trong tương lai.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + will be + V-ing"],
        ["Phủ định", "S + will not be + V-ing"],
        ["Nghi vấn", "Will + S + be + V-ing?"]
    ]),
    tbl(["Ví dụ"], [
        ["At 8pm tomorrow, I will be watching TV."],
        ["This time next week, she will be travelling."]
    ]),
    [
        "Hành động sẽ đang xảy ra tại thời điểm xác định trong tương lai.",
        "Hành động đã được lên kế hoạch hoặc là phần của thói quen tương lai."
    ],
    "At this time tomorrow/next week, At 8pm tomorrow, In the future."
))

lessons.append(lesson(
    "lesson", "present-perfect-continuous",
    "Thì hiện tại hoàn thành tiếp diễn - Present Perfect Continuous",
    "Thì hiện tại hoàn thành tiếp diễn nhấn mạnh sự kéo dài của hành động từ quá khứ đến hiện tại (có thể còn tiếp tục).",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + have/has been + V-ing"],
        ["Phủ định", "S + have not/has not been + V-ing"],
        ["Nghi vấn", "Have/Has + S + been + V-ing?"]
    ]),
    tbl(["Ví dụ"], [
        ["I have been learning English for 5 years."],
        ["She has been working here since 2020."]
    ]),
    [
        "Hành động bắt đầu trong quá khứ, kéo dài đến hiện tại (nhấn mạnh thời gian).",
        "Hành động vừa kết thúc, kết quả còn thấy rõ.",
        "Thường dùng với since, for."
    ],
    "Since, For, All day/week, How long..., Lately, Recently."
))

# ========== 13-17: Câu điều kiện ==========
lessons.append(lesson(
    "lesson", "conditional-type-0",
    "Câu điều kiện loại 0 - Zero Conditional",
    "Câu điều kiện loại 0 diễn tả sự thật hiển nhiên, quy luật tự nhiên, thói quen. If + present → present.",
    tbl(["Công thức", "Ví dụ"], [
        ["If + S + V1, S + V1", "If you heat ice, it melts."],
        ["If + S + V1, S + V1", "If it rains, the ground gets wet."]
    ]),
    tbl(["Cách dùng", "Ví dụ"], [
        ["Sự thật hiển nhiên", "If water reaches 100°C, it boils."],
        ["Quy luật/Thói quen", "If I'm tired, I go to bed early."]
    ]),
    ["Diễn tả sự thật hiển nhiên, khoa học.", "Diễn tả thói quen, quy luật."],
    "Always true, general facts, habits."
))

lessons.append(lesson(
    "lesson", "conditional-type-1",
    "Câu điều kiện loại 1 - First Conditional",
    "Câu điều kiện loại 1 diễn tả điều kiện có thể xảy ra ở hiện tại hoặc tương lai. If + present → future.",
    tbl(["Công thức", "Ví dụ"], [
        ["If + S + V1, S + will + V-inf", "If it rains, I will stay at home."],
        ["If + S + V1, S + can/may/must + V-inf", "If you study hard, you can pass."]
    ]),
    tbl(["Ví dụ"], [
        ["If you come early, we will have time to talk."],
        ["If she doesn't call, I will call her."]
    ]),
    [
        "Điều kiện có thể xảy ra trong tương lai.",
        "Đề nghị, cảnh báo, thỏa thuận.",
        "Có thể dùng Unless = If not."
    ],
    "If + present, will/can/may + V. Unless = if not."
))

lessons.append(lesson(
    "lesson", "conditional-type-2",
    "Câu điều kiện loại 2 - Second Conditional",
    "Câu điều kiện loại 2 diễn tả điều kiện không có thật ở hiện tại hoặc tương lai (giả định). If + past → would + V.",
    tbl(["Công thức", "Ví dụ"], [
        ["If + S + V2, S + would + V-inf", "If I had money, I would buy a car."],
        ["If + S + were, S + would + V-inf", "If I were you, I would tell the truth."]
    ]),
    tbl(["Ví dụ"], [
        ["If I were rich, I would travel the world."],
        ["If it didn't rain, we would go out."]
    ]),
    [
        "Điều kiện không có thật ở hiện tại (ước, giả định).",
        "Lời khuyên: If I were you, I would...",
        "Were dùng cho tất cả ngôi trong văn phong trang trọng."
    ],
    "If I were..., Would/Could/Might + V. Unreal present/future."
))

lessons.append(lesson(
    "lesson", "conditional-type-3",
    "Câu điều kiện loại 3 - Third Conditional",
    "Câu điều kiện loại 3 diễn tả điều kiện không có thật trong quá khứ (hối tiếc, phỏng đoán). If + had V3 → would have V3.",
    tbl(["Công thức", "Ví dụ"], [
        ["If + S + had + V3, S + would have + V3", "If I had known, I would have told you."],
        ["Phủ định", "If she hadn't been ill, she would have come."]
    ]),
    tbl(["Ví dụ"], [
        ["If I had studied harder, I would have passed the exam."],
        ["If you had told me, I would have helped."]
    ]),
    [
        "Điều kiện không có thật trong quá khứ.",
        "Diễn tả hối tiếc về việc đã không làm.",
        "Phỏng đoán về kết quả đã không xảy ra."
    ],
    "If + had V3, would have V3. Past unreal."
))

# ========== 18-22: Passive voice ==========
lessons.append(lesson(
    "lesson", "passive-present-simple",
    "Bị động thì hiện tại đơn - Passive (Present Simple)",
    "Câu bị động thì hiện tại đơn: S + am/is/are + V3 (by O). Chủ ngữ chịu tác động của hành động.",
    tbl(["Chủ động", "Bị động"], [
        ["S + V1/V-s/es + O", "S + am/is/are + V3 (by O)"],
        ["They build houses.", "Houses are built (by them)."]
    ]),
    tbl(["Ví dụ"], [
        ["English is spoken all over the world."],
        ["The room is cleaned every day."]
    ]),
    ["Nhấn mạnh đối tượng chịu tác động.", "Khi không biết hoặc không cần nêu chủ thể gây ra hành động."],
    "Am/Is/Are + V3. By + O (optional)."
))

lessons.append(lesson(
    "lesson", "passive-past-simple",
    "Bị động thì quá khứ đơn - Passive (Past Simple)",
    "Câu bị động thì quá khứ đơn: S + was/were + V3 (by O).",
    tbl(["Chủ động", "Bị động"], [
        ["S + V2 + O", "S + was/were + V3 (by O)"],
        ["They built this house in 1990.", "This house was built in 1990."]
    ]),
    tbl(["Ví dụ"], [
        ["The letter was sent yesterday."],
        ["The window was broken by the boy."]
    ]),
    ["Diễn tả hành động bị động đã xảy ra và kết thúc trong quá khứ."],
    "Was/Were + V3."
))

lessons.append(lesson(
    "lesson", "passive-modal",
    "Bị động với động từ khuyết thiếu - Passive with Modals",
    "Câu bị động với can, could, may, might, must, should: S + modal + be + V3 (by O).",
    tbl(["Công thức", "Ví dụ"], [
        ["S + can be + V3", "The problem can be solved."],
        ["S + must be + V3", "The work must be done today."],
        ["S + should be + V3", "Homework should be done carefully."]
    ]),
    tbl(["Ví dụ"], [
        ["This room can be used for meetings."],
        ["The door must be closed at night."]
    ]),
    ["Dùng khi cần diễn đạt bị động với khả năng, bắt buộc, hoặc lời khuyên."],
    "Can/Could/May/Must/Should + be + V3."
))

# ========== 23-35: Modal verbs ==========
modals = [
    ("can", "Can - Có thể (khả năng, xin phép)", "Diễn tả khả năng, xin phép, yêu cầu. Can + V-inf.", ["I can swim.", "Can I use your phone?"], "Khả năng hiện tại, xin phép, đề nghị.", "Can + V (không có to)."),
    ("could", "Could - Có thể (quá khứ, lịch sự)", "Could là dạng quá khứ của can; cũng dùng để yêu cầu lịch sự hoặc khả năng trong quá khứ.", ["I could run fast when I was young.", "Could you help me?"], "Khả năng quá khứ, yêu cầu lịch sự, điều kiện.", "Could + V-inf."),
    ("may", "May - Có thể (xin phép, phỏng đoán)", "May dùng để xin phép lịch sự hoặc phỏng đoán (khả năng thấp).", ["May I come in?", "It may rain tomorrow."], "Xin phép trang trọng, phỏng đoán không chắc.", "May + V-inf."),
    ("might", "Might - Có thể (phỏng đoán yếu hơn may)", "Might dùng để phỏng đoán khả năng thấp hơn may; cũng là quá khứ của may.", ["She might be at home.", "I might go to the party."], "Phỏng đoán không chắc chắn, khả năng thấp.", "Might + V-inf."),
    ("must", "Must - Phải (bắt buộc)", "Must diễn tả sự bắt buộc, nghĩa vụ mạnh hoặc suy luận chắc chắn.", ["You must wear a seatbelt.", "He must be tired."], "Bắt buộc, nghĩa vụ, suy luận chắc chắn.", "Must + V-inf. Mustn't = cấm."),
    ("have-to", "Have to - Phải (bắt buộc do ngoại cảnh)", "Have to diễn tả sự bắt buộc do quy định, hoàn cảnh bên ngoài (khác với must là do bản thân).", ["I have to work on Saturday.", "You have to pass the test."], "Bắt buộc do quy định, ngoại cảnh.", "Have to / Has to + V-inf."),
    ("should", "Should - Nên (lời khuyên)", "Should dùng để đưa lời khuyên, gợi ý hoặc diễn tả điều nên làm.", ["You should see a doctor.", "We should leave now."], "Lời khuyên, gợi ý, mong đợi hợp lý.", "Should + V-inf."),
    ("ought-to", "Ought to - Nên (lời khuyên trang trọng)", "Ought to tương tự should nhưng trang trọng hơn. Ought to + V-inf.", ["You ought to apologize.", "We ought to be more careful."], "Lời khuyên trang trọng, nghĩa vụ đạo đức.", "Ought to + V-inf."),
    ("would", "Would - Sẽ (thói quen quá khứ, lịch sự)", "Would dùng cho thói quen trong quá khứ, lời mời lịch sự, hoặc trong câu điều kiện.", ["When I was young, I would play football.", "Would you like some tea?"], "Thói quen quá khứ, lời mời lịch sự, câu điều kiện.", "Would + V-inf."),
    ("used-to", "Used to - Đã từng (thói quen quá khứ)", "Used to diễn tả thói quen hoặc tình trạng trong quá khứ nhưng đã chấm dứt.", ["I used to smoke.", "She used to live in London."], "Thói quen/tình trạng trong quá khứ, nay không còn.", "Used to + V-inf. (chỉ quá khứ)."),
]

for mid, title, definition, ex_rows, usage_short, signals in modals:
    ex = tbl(["Ví dụ"], [[r] for r in ex_rows]) if isinstance(ex_rows[0], str) else tbl(["Ví dụ"], ex_rows)
    lessons.append(lesson(
        "lesson", mid, title, definition,
        tbl(["Công thức", "Ví dụ"], [[signals.split('.')[0], ex_rows[0]]]),
        ex,
        [usage_short],
        signals
    ))

# ========== 36-45: Cấu trúc khác ==========
lessons.append(lesson(
    "lesson", "comparative-superlative",
    "So sánh hơn và so sánh nhất - Comparative and Superlative",
    "So sánh hơn: short adj + -er than / more + long adj + than. So sánh nhất: the + -est / the most + adj.",
    tbl(["Dạng", "So sánh hơn", "So sánh nhất"], [
        ["Tính từ ngắn (1-2 âm)", "adj + -er + than", "the + adj + -est"],
        ["Tính từ dài", "more + adj + than", "the most + adj"],
        ["Bất quy tắc", "good → better, bad → worse", "best, worst"]
    ]),
    tbl(["Ví dụ"], [
        ["She is taller than me. / She is the tallest."],
        ["This is more expensive than that. / the most expensive."]
    ]),
    [
        "So sánh giữa 2 đối tượng: dùng so sánh hơn.",
        "So sánh từ 3 đối tượng trở lên: dùng so sánh nhất.",
        "Tính từ ngắn: thêm -er/-est. Tính từ dài: more/most."
    ],
    "Than (so sánh hơn), The (so sánh nhất), In/Of (phạm vi)."
))

lessons.append(lesson(
    "lesson", "too-and-enough",
    "Too và Enough - Quá và Đủ",
    "Too + adj/adv: quá (mức không mong muốn). Adj/Adv + enough: đủ. Enough + N: đủ (số lượng).",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["too + adj/adv + to V", "It's too cold to go out."],
        ["adj/adv + enough + to V", "She's old enough to drive."],
        ["enough + N", "I don't have enough money."]
    ]),
    tbl(["Ví dụ"], [
        ["The box is too heavy to carry."],
        ["He's strong enough to lift it."]
    ]),
    ["Too: vượt quá mức, thường dẫn đến kết quả tiêu cực.", "Enough: đủ để làm gì đó."],
    "Too + adj. Adj + enough. Enough + N."
))

lessons.append(lesson(
    "lesson", "so-such",
    "So...that và Such...that",
    "So + adj/adv + that: quá...đến nỗi. Such + (a/an) + adj + N + that: một...đến nỗi.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["So + adj/adv + that", "She was so tired that she fell asleep."],
        ["Such (a/an) + adj + N + that", "It was such a nice day that we went out."]
    ]),
    tbl(["Ví dụ"], [
        ["The film was so boring that I left."],
        ["He's such a good teacher that everyone likes him."]
    ]),
    ["So dùng với tính từ/trạng từ.", "Such dùng với danh từ (có a/an nếu danh từ đếm được số ít)."],
    "So + adj/adv. Such + (a/an) + adj + N."
))

lessons.append(lesson(
    "lesson", "used-to-be-used-to",
    "Used to / Be used to / Get used to",
    "Used to + V: đã từng (quá khứ). Be used to + V-ing/N: quen với. Get used to + V-ing/N: dần quen với.",
    tbl(["Cấu trúc", "Nghĩa", "Ví dụ"], [
        ["used to + V-inf", "Đã từng (thói quen quá khứ)", "I used to play tennis."],
        ["be used to + V-ing/N", "Quen với (hiện tại)", "I am used to getting up early."],
        ["get used to + V-ing/N", "Dần quen với", "I'm getting used to the new job."]
    ]),
    tbl(["Ví dụ"], [
        ["She used to live in Paris."],
        ["He is used to working at night."]
    ]),
    ["Used to: chỉ quá khứ, không dùng cho hiện tại.", "Be/Get used to: theo sau là V-ing hoặc danh từ."],
    "Used to V. Be/Get used to V-ing."
))

lessons.append(lesson(
    "lesson", "would-rather-had-better",
    "Would rather và Had better",
    "Would rather + V: thích...hơn (would rather not: không muốn). Had better + V: nên (lời khuyên mạnh, gần cảnh báo).",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["would rather + V-inf", "I would rather stay home."],
        ["would rather + S + V2 (so sánh)", "I'd rather you didn't smoke."],
        ["had better + V-inf", "You had better leave now."]
    ]),
    tbl(["Ví dụ"], [
        ["I'd rather not go to the party."],
        ["You'd better see a doctor."]
    ]),
    ["Would rather: thể hiện sở thích, lựa chọn.", "Had better: khuyên nên làm (nếu không sẽ có hậu quả)."],
    "Would rather. Had better (thường viết 'd better)."
))

lessons.append(lesson(
    "lesson", "question-tags",
    "Câu hỏi đuôi - Question Tags",
    "Câu hỏi đuôi là phần ngắn đứng cuối câu để xác nhận. Nếu câu chính khẳng định thì đuôi phủ định và ngược lại.",
    tbl(["Câu chính", "Đuôi", "Ví dụ"], [
        ["Khẳng định", "Phủ định", "You are a student, aren't you?"],
        ["Phủ định", "Khẳng định", "She doesn't like it, does she?"],
        ["I'm..., aren't I?", "Đặc biệt", "I'm late, aren't I?"]
    ]),
    tbl(["Ví dụ"], [
        ["It's cold, isn't it?"],
        ["You won't tell anyone, will you?"]
    ]),
    [
        "Đuôi dùng trợ động từ hoặc be phù hợp với thì.",
        "Chủ ngữ câu đuôi luôn là đại từ (it, they, he, she...).",
        "Lên giọng ở đuôi = hỏi thật; xuống giọng = mong đợi đồng ý."
    ],
    "Trợ động từ + đại từ. Khẳng định ↔ Phủ định."
))

lessons.append(lesson(
    "lesson", "articles-a-an-the",
    "Mạo từ A, An, The - Articles",
    "A/An: mạo từ không xác định (danh từ đếm được số ít). A: trước phụ âm. An: trước nguyên âm (a, e, i, o, u). The: mạo từ xác định.",
    tbl(["Mạo từ", "Dùng khi", "Ví dụ"], [
        ["a", "Danh từ số ít, bắt đầu bằng phụ âm", "a book, a university"],
        ["an", "Danh từ số ít, bắt đầu bằng nguyên âm", "an apple, an hour"],
        ["the", "Đã xác định, duy nhất, đã đề cập", "the sun, the book I bought"]
    ]),
    tbl(["Ví dụ"], [
        ["I need a pen. The pen is on the table."],
        ["An hour ago. The Earth moves around the Sun."]
    ]),
    [
        "A/An: lần đầu nhắc đến, chưa xác định.",
        "The: đã xác định, người nghe biết đang nói về cái gì; sự vật duy nhất.",
        "Không dùng a/an với danh từ không đếm được hoặc số nhiều."
    ],
    "A + phụ âm. An + nguyên âm. The = xác định."
))

lessons.append(lesson(
    "lesson", "prepositions-time",
    "Giới từ chỉ thời gian - Prepositions of Time",
    "At: giờ, thời điểm ngắn (at 5pm, at night). On: ngày, ngày lễ (on Monday, on Christmas Day). In: tháng, năm, mùa, buổi (in 2020, in the morning).",
    tbl(["Giới từ", "Dùng với", "Ví dụ"], [
        ["at", "Giờ, at night, at noon, at weekend", "at 7am, at midnight"],
        ["on", "Ngày, ngày cụ thể", "on Monday, on 25th December"],
        ["in", "Tháng, năm, mùa, in the morning/afternoon", "in January, in 2020"]
    ]),
    tbl(["Ví dụ"], [
        ["I'll see you at 3 o'clock on Friday."],
        ["She was born in 1990 in summer."]
    ]),
    ["At: thời điểm cụ thể (giờ).", "On: ngày.", "In: khoảng thời gian dài hơn (tháng, năm)."],
    "At + time. On + day/date. In + month/year/season."
))

lessons.append(lesson(
    "lesson", "prepositions-place",
    "Giới từ chỉ nơi chốn - Prepositions of Place",
    "In: trong (không gian 3 chiều). On: trên bề mặt. At: tại địa điểm (thường là điểm, địa chỉ).",
    tbl(["Giới từ", "Dùng khi", "Ví dụ"], [
        ["in", "Trong (thành phố, phòng, nước)", "in the room, in Vietnam"],
        ["on", "Trên bề mặt", "on the table, on the wall"],
        ["at", "Tại địa điểm (điểm đến)", "at the door, at home, at school"]
    ]),
    tbl(["Ví dụ"], [
        ["I live in Hanoi. The book is on the desk."],
        ["Meet me at the station. She's at home."]
    ]),
    ["In: bên trong, trong phạm vi.", "On: tiếp xúc bề mặt.", "At: vị trí điểm (địa chỉ, nơi chốn cụ thể)."],
    "In + place (inside). On + surface. At + point/place."
))

lessons.append(lesson(
    "lesson", "some-any-no",
    "Some, Any, No - Một vài / Bất kỳ / Không",
    "Some: dùng trong câu khẳng định, câu mời (would you like...). Any: câu phủ định và nghi vấn. No: nghĩa phủ định (no + N = not any).",
    tbl(["Từ", "Dùng trong", "Ví dụ"], [
        ["some", "Khẳng định, câu mời", "I have some money. Would you like some tea?"],
        ["any", "Phủ định, nghi vấn", "I don't have any time. Do you have any questions?"],
        ["no", "Khẳng định nhưng mang nghĩa phủ định", "I have no idea. There's no milk."]
    ]),
    tbl(["Ví dụ"], [
        ["There are some apples. There aren't any apples."],
        ["There is no sugar. = There isn't any sugar."]
    ]),
    ["Some: một vài, một ít (khẳng định hoặc mời).", "Any: bất kỳ (phủ định, hỏi).", "No + N = not any."],
    "Some: +. Any: -, ?. No = not any."
))

# ========== 46-55: Relative clauses, Gerund vs Infinitive ==========
lessons.append(lesson(
    "lesson", "relative-clauses-who-which",
    "Mệnh đề quan hệ - Who, Which, That",
    "Who: thay cho người (chủ ngữ). Which: thay cho vật/sự việc. That: thay cho cả người và vật (trong mệnh đề xác định).",
    tbl(["Đại từ", "Thay thế", "Ví dụ"], [
        ["who", "Người (chủ ngữ)", "The man who lives next door is a doctor."],
        ["which", "Vật, sự việc", "The book which I bought is interesting."],
        ["that", "Người hoặc vật (xác định)", "Everything that he said was true."]
    ]),
    tbl(["Ví dụ"], [
        ["The woman who is standing there is my teacher."],
        ["This is the house which/that was built in 1990."]
    ]),
    [
        "Who/Which/That làm chủ ngữ trong mệnh đề quan hệ thì không bỏ được.",
        "That thường dùng thay who/which trong mệnh đề xác định.",
        "Whom: thay cho người (tân ngữ); có thể bỏ nếu không có giới từ."
    ],
    "Who (person). Which (thing). That (person/thing, defining)."
))

lessons.append(lesson(
    "lesson", "gerund-vs-infinitive",
    "Danh động từ (V-ing) và Động từ nguyên mẫu (to V)",
    "Một số động từ chỉ đi với V-ing (enjoy, avoid, finish). Một số chỉ đi với to V (want, decide, hope). Một số đi với cả hai nhưng nghĩa khác (remember, forget, stop).",
    tbl(["Theo sau bởi V-ing", "Theo sau bởi to V"], [
        ["enjoy, avoid, finish, mind, suggest", "want, decide, hope, agree, promise"],
        ["keep, consider, imagine, risk", "plan, expect, refuse, learn"]
    ]),
    tbl(["Ví dụ"], [
        ["I enjoy swimming. She avoided answering."],
        ["I want to go. He decided to leave."]
    ]),
    [
        "V-ing: khi động từ là chủ ngữ hoặc sau giới từ.",
        "To V: mục đích, sau tính từ (happy to see), sau một số động từ.",
        "Remember/Forget/Stop + V-ing: việc đã xảy ra. + to V: việc cần làm."
    ],
    "Enjoy + V-ing. Want + to V. Remember + V-ing (past) / to V (future)."
))

# ========== 56-70: Thêm chủ đề đa dạng ==========
topics_56_70 = [
    ("linking-although-however", "Liên từ Although, However, Therefore",
     "Although/Though + clause: mặc dù (đứng đầu hoặc giữa câu). However: tuy nhiên (đứng đầu câu, sau dấu chấm phẩy). Therefore: do đó.",
     tbl(["Từ", "Vị trí", "Ví dụ"], [
         ["Although", "Đầu/giữa câu", "Although it rained, we went out."],
         ["However", "Đầu câu mới", "It was cold. However, we went out."],
         ["Therefore", "Kết quả", "He was ill. Therefore, he didn't come."]
     ]), ["Nối ý tương phản (although) hoặc kết quả (therefore)."], "Although + clause. However, ... Therefore, ..."),
    ("countable-uncountable", "Danh từ đếm được và không đếm được",
     "Danh từ đếm được: có số nhiều (a book, two books). Danh từ không đếm được: không có a/an, không số nhiều (water, rice, information).",
     tbl(["Đếm được", "Không đếm được"], [
         ["a book, an apple, many books", "water, rice, information, advice"],
         ["few/fewer, many", "little/less, much"]
     ]), ["Đếm được: dùng a/an, many, few.", "Không đếm được: dùng some, much, little (không dùng a/an)."], "Many + countable. Much + uncountable."),
    ("much-many-lot-of", "Much, Many, A lot of",
     "Much: danh từ không đếm được (thường trong câu phủ định, nghi vấn). Many: danh từ đếm được. A lot of / Lots of: cả hai (thường trong câu khẳng định).",
     tbl(["Từ", "Dùng với", "Ví dụ"], [
         ["much", "N không đếm được", "I don't have much time."],
         ["many", "N đếm được", "There aren't many people."],
         ["a lot of", "Cả hai (khẳng định)", "She has a lot of friends."]
     ]), ["Much/Many thường dùng trong câu phủ định và nghi vấn.", "A lot of thường dùng trong khẳng định."], "Much + U. Many + C. A lot of + C/U."),
    ("reported-speech-statements", "Câu tường thuật - Statements",
     "Khi chuyển câu trực tiếp sang gián tiếp: lùi thì (present → past), đổi đại từ, trạng từ (now → then, today → that day).",
     tbl(["Trực tiếp", "Gián tiếp"], [
         ["I am tired.", "He said (that) he was tired."],
         ["I will go.", "She said (that) she would go."],
         ["I have finished.", "He said (that) he had finished."]
     ]), ["Lùi thì: present → past, will → would, can → could.", "Đổi ngôi, đổi trạng từ thời gian/nơi chốn."], "Say/Tell + (that) + clause. Lùi thì."),
    ("reported-speech-questions", "Câu tường thuật - Questions",
     "Câu hỏi Yes/No: asked (sb) if/whether + S + V (lùi thì). Câu hỏi Wh: asked (sb) + từ để hỏi + S + V (lùi thì).",
     tbl(["Trực tiếp", "Gián tiếp"], [
         ["Do you like it?", "He asked (me) if I liked it."],
         ["Where do you live?", "She asked (him) where he lived."]
     ]), ["Bỏ trợ động từ do/does/did, đổi thành S + V (lùi thì).", "If/Whether cho câu hỏi Yes/No."], "Asked + if/whether. Asked + wh-word."),
    ("wish-if-only", "Wish và If only",
     "Wish/If only + V2 (were): ước về hiện tại (không có thật). Wish + had V3: ước về quá khứ. Wish + would: ước về tương lai (phàn nàn).",
     tbl(["Loại", "Công thức", "Ví dụ"], [
         ["Hiện tại", "wish + S + V2/were", "I wish I were rich."],
         ["Quá khứ", "wish + S + had V3", "I wish I had known."],
         ["Tương lai", "wish + S + would V", "I wish it would stop raining."]
     ]), ["Ước về hiện tại: dùng past (were cho tất cả ngôi).", "Ước về quá khứ: had V3.", "Ước về tương lai: would V (thường phàn nàn)."], "Wish + past (unreal)."),
    ("subject-verb-agreement", "Sự hòa hợp chủ ngữ - động từ (Subject-Verb Agreement)",
     "Chủ ngữ số ít → động từ số ít (V-s/es). Chủ ngữ số nhiều → động từ nguyên thể. Each/Every + N → V số ít. N1 + as well as + N2 → V theo N1.",
     tbl(["Chủ ngữ", "Động từ"], [
         ["He/She/It, Each student", "V-s/es"],
         ["I/You/We/They, Students", "V-inf"],
         ["The number of + N", "V số ít. A number of + N", "V số nhiều"]
     ]), ["Luôn xác định chủ ngữ chính (có thể sau of, with, as well as).", "Each, Every, Nobody, Someone → V số ít."], "S (singular) + V-s. S (plural) + V."),
    ("adverbs-position", "Vị trí trạng từ trong câu",
     "Trạng từ cách thức (quickly): thường sau động từ hoặc sau tân ngữ. Trạng từ tần suất (always): trước động từ thường, sau be. Trạng từ thời gian (yesterday): đầu hoặc cuối câu.",
     tbl(["Loại", "Vị trí", "Ví dụ"], [
         ["Cách thức", "Sau V hoặc sau O", "He speaks English well."],
         ["Tần suất", "Trước V thường, sau be", "She is always late. He never lies."],
         ["Thời gian", "Đầu/cuối câu", "Yesterday I met him. I'll call you tomorrow."]
     ]), ["Trạng từ tần suất: giữa chủ ngữ và động từ (sau be).", "Trạng từ cách thức: sau động từ (hoặc sau tân ngữ)."], "Frequency: before main V, after be. Manner: after V/O."),
    ("both-either-neither", "Both, Either, Neither",
     "Both: cả hai. Either: một trong hai (khẳng định). Neither: không cái nào trong hai. Both + N (plural) + V plural. Either/Neither + N (singular) + V singular.",
     tbl(["Từ", "Nghĩa", "Ví dụ"], [
         ["both", "Cả hai", "Both (of) the books are good."],
         ["either", "Một trong hai", "Either option is fine."],
         ["neither", "Không cái nào", "Neither answer is correct."]
     ]), ["Both...and. Either...or. Neither...nor.", "Either/Neither of + N (plural) + V singular (formal)."], "Both + plural. Either/Neither + singular."),
    ("phrasal-verbs-basics", "Cụm động từ (Phrasal Verbs) - Cơ bản",
     "Phrasal verb = động từ + giới từ/trạng từ (look after, give up). Nghĩa thường khác nghĩa động từ gốc. Có loại có tân ngữ ở giữa (turn off the light = turn the light off).",
     tbl(["Phrasal verb", "Nghĩa", "Ví dụ"], [
         ["look after", "Chăm sóc", "She looks after her mother."],
         ["give up", "Từ bỏ", "Don't give up."],
         ["turn on/off", "Bật/Tắt", "Turn off the TV."]
     ]), ["Học thuộc nghĩa từng cụm.", "Một số có thể tách (turn it off), một số không (look after him)."], "Verb + particle. Meaning often different from verb."),
]

for tid, title, definition, formula, usage_list, signals in topics_56_70:
    if isinstance(usage_list, list) and len(usage_list) > 0 and isinstance(usage_list[0], str):
        usage_arr = usage_list
    else:
        usage_arr = ["Xem bảng và ví dụ."]
    lessons.append(lesson("lesson", tid, title, definition, formula,
                         tbl(["Ví dụ"], [["Xem công thức."]]), usage_arr, signals))

# ========== 71-100: Bài mở rộng (đầy đủ công thức + ví dụ) ==========
def ex71(id_, title, definition, formula, examples, usage, signals):
    lessons.append(lesson("lesson", id_, title, definition, formula, examples, usage, signals))

ex71("past-perfect-continuous", "Thì quá khứ hoàn thành tiếp diễn - Past Perfect Continuous",
    "Thì quá khứ hoàn thành tiếp diễn diễn tả hành động đang diễn ra liên tục trước một thời điểm hoặc trước một hành động khác trong quá khứ. Nhấn mạnh độ dài và tính liên tục của hành động.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + had been + V-ing"],
        ["Phủ định", "S + had not been + V-ing"],
        ["Nghi vấn", "Had + S + been + V-ing?"]
    ]),
    tbl(["Ví dụ"], [
        ["She had been working for 3 hours before she left."],
        ["By the time I arrived, they had been waiting for an hour."],
        ["How long had you been living there before you moved?"]
    ]),
    ["Hành động kéo dài liên tục trước một thời điểm trong quá khứ.", "Thường dùng với for, since, by the time, before.", "Phân biệt với Past perfect: nhấn mạnh sự kéo dài chứ không chỉ hoàn thành."],
    "Before, By the time, For, Since, How long.")

ex71("future-perfect", "Thì tương lai hoàn thành - Future Perfect",
    "Thì tương lai hoàn thành diễn tả hành động sẽ hoàn thành trước một thời điểm hoặc trước một hành động khác trong tương lai.",
    tbl(["Loại câu", "Công thức"], [
        ["Khẳng định", "S + will have + V3"],
        ["Phủ định", "S + will not have + V3"],
        ["Nghi vấn", "Will + S + have + V3?"]
    ]),
    tbl(["Ví dụ"], [
        ["By 2030, I will have graduated from university."],
        ["She will have finished the report by the time you come back."],
        ["Will you have completed the course by June?"]
    ]),
    ["Hành động hoàn thành trước một thời điểm trong tương lai (by + time).", "Thường dùng với by then, by the time, by 2025."],
    "By + time in future, By then, By the time.")

ex71("passive-present-continuous", "Bị động thì hiện tại tiếp diễn",
    "Câu bị động thì hiện tại tiếp diễn: S + am/is/are being + V3. Diễn tả hành động đang bị thực hiện tại thời điểm nói.",
    tbl(["Chủ động", "Bị động"], [
        ["S + am/is/are + V-ing + O", "S + am/is/are being + V3 (by O)"],
        ["They are building the house.", "The house is being built (by them)."]
    ]),
    tbl(["Ví dụ"], [
        ["The room is being cleaned now."],
        ["A new bridge is being constructed over the river."]
    ]),
    ["Dùng khi nhấn mạnh hành động đang diễn ra (bị động).", "Không dùng với các động từ chỉ trạng thái (know, want, like)."],
    "Am/Is/Are being + V3.")

ex71("passive-present-perfect", "Bị động thì hiện tại hoàn thành",
    "Câu bị động thì hiện tại hoàn thành: S + have/has been + V3. Diễn tả hành động đã bị thực hiện và kết quả còn liên quan đến hiện tại.",
    tbl(["Chủ động", "Bị động"], [
        ["S + have/has + V3 + O", "S + have/has been + V3 (by O)"],
        ["Someone has sent the letter.", "The letter has been sent."]
    ]),
    tbl(["Ví dụ"], [
        ["The work has been completed."],
        ["Has the report been submitted yet?"]
    ]),
    ["Nhấn mạnh kết quả ở hiện tại hơn là thời điểm hành động.", "Thường dùng với yet, already, just."],
    "Have/Has been + V3.")

ex71("indirect-questions", "Câu hỏi gián tiếp - Indirect Questions",
    "Câu hỏi gián tiếp dùng để hỏi lịch sự: không đảo trợ động từ, theo sau cụm như Could you tell me..., Do you know..., I wonder...",
    tbl(["Trực tiếp", "Gián tiếp"], [
        ["Where is the station?", "Could you tell me where the station is?"],
        ["What time does it open?", "Do you know what time it opens?"],
        ["Why did he leave?", "I wonder why he left."]
    ]),
    tbl(["Ví dụ"], [
        ["Could you tell me how much this costs?"],
        ["I'd like to know when the meeting starts."]
    ]),
    ["Giữ nguyên trật tự S + V (không đảo).", "Không dùng do/does/did trong mệnh đề gián tiếp.", "Lịch sự hơn câu hỏi trực tiếp."],
    "Could you tell me... Do you know... I wonder...")

ex71("ellipsis-so-do-i", "So do I / Neither do I - Đồng ý ngắn gọn",
    "So + trợ động từ + S: đồng ý với câu khẳng định (tôi cũng vậy). Neither/Nor + trợ động từ + S: đồng ý với câu phủ định. Trợ động từ phải khớp thì và chủ ngữ.",
    tbl(["Câu gốc", "Đồng ý khẳng định", "Đồng ý phủ định"], [
        ["I like coffee.", "So do I.", "—"],
        ["I don't like tea.", "—", "Neither do I. / Nor do I."],
        ["She can swim.", "So can I.", "—"],
        ["He hasn't been there.", "—", "Neither have I."]
    ]),
    tbl(["Ví dụ"], [
        ["I'm tired. — So am I."],
        ["I didn't see him. — Neither did I."]
    ]),
    ["Trợ động từ (do, does, did, have, has, can, will...) phải phù hợp với câu gốc.", "So/Neither đứng đầu, sau đó trợ động từ rồi chủ ngữ."],
    "So + aux + S. Neither/Nor + aux + S.")

ex71("cleft-sentences", "Câu chẻ - Cleft Sentences (It is...that)",
    "Câu chẻ dùng để nhấn mạnh một thành phần trong câu: It is/was + thành phần nhấn mạnh + that/who/which + phần còn lại.",
    tbl(["Nhấn mạnh", "Công thức", "Ví dụ"], [
        ["Chủ ngữ", "It is/was + S + that/who + V...", "It was Tom who broke the window."],
        ["Tân ngữ", "It is/was + O + that/who(m) + S + V...", "It was the window that Tom broke."],
        ["Trạng từ", "It is/was + adverbial + that + S + V...", "It was in Paris that I met her."]
    ]),
    tbl(["Ví dụ"], [
        ["It was in 2020 that I started learning English."],
        ["It is English that she wants to study."]
    ]),
    ["Who dùng khi nhấn mạnh người (chủ ngữ); that dùng cho vật hoặc người.", "Phổ biến trong văn viết và nói trang trọng."],
    "It is/was...that/who/which. Nhấn mạnh thành phần câu.")

ex71("inversion", "Đảo ngữ - Inversion",
    "Đảo ngữ: đưa trợ động từ hoặc động từ lên trước chủ ngữ. Thường dùng với các từ phủ định hoặc giới hạn ở đầu câu để nhấn mạnh hoặc trang trọng.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["Never/Rarely/Seldom + aux + S + V", "Never had I seen such a beautiful place."],
        ["Not only + aux + S + V, but ... also", "Not only did he apologize, but he also offered to pay."],
        ["Hardly/Scarcely + had + S + V3 when", "Hardly had I left when it started to rain."],
        ["Only + trạng từ/trạng ngữ + aux + S + V", "Only then did I understand."]
    ]),
    tbl(["Ví dụ"], [
        ["Seldom do we have such good weather."],
        ["Not only is she smart, but she is also kind."]
    ]),
    ["Chỉ dùng khi từ phủ định/đặc biệt đứng đầu câu.", "Trợ động từ (do, did, have, had, can...) đảo lên trước chủ ngữ."],
    "Never had I... Not only did he... Hardly had... Only then...")

ex71("despite-in-spite-of", "Despite và In spite of",
    "Despite và In spite of có nghĩa 'mặc dù', theo sau bởi danh từ, cụm danh từ hoặc V-ing (không theo sau bởi mệnh đề S + V). In spite of = Despite (giống nhau).",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["Despite + N/N-phrase", "Despite the rain, we went out."],
        ["In spite of + N", "In spite of his age, he runs every day."],
        ["Despite + V-ing", "Despite feeling tired, she continued working."]
    ]),
    tbl(["So sánh"], [
        ["Although it rained, we went out. (Although + clause)"],
        ["Despite the rain, we went out. (Despite + N)"]
    ]),
    ["Sau despite/in spite of không dùng câu đầy đủ (không có chủ ngữ + động từ).", "Muốn dùng câu thì dùng Although/Though + S + V."],
    "Despite/In spite of + N/V-ing. Không + clause.")

ex71("because-because-of", "Because và Because of",
    "Because + mệnh đề (S + V): vì (theo sau là một câu hoàn chỉnh). Because of + danh từ/cụm danh từ/V-ing: vì (theo sau không phải câu).",
    tbl(["Từ", "Theo sau bởi", "Ví dụ"], [
        ["Because", "Clause (S + V)", "I stayed home because it was raining."],
        ["Because of", "N / V-ing / N-phrase", "I stayed home because of the rain."]
    ]),
    tbl(["Chuyển đổi"], [
        ["Because the weather was bad, we cancelled the trip."],
        ["Because of the bad weather, we cancelled the trip."]
    ]),
    ["Because of = due to = owing to (theo sau là N).", "Khi có S + V thì dùng because."],
    "Because + clause. Because of + N/V-ing.")

ex71("so-that-in-order-to", "So that và In order to - Mục đích",
    "In order to / To + V-inf: để (mục đích của chủ ngữ). So that + S + can/could/will/would + V: để (ai đó có thể/ sẽ làm gì). So that thường có chủ ngữ riêng trong mệnh đề sau.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["... in order to + V-inf", "I study hard in order to pass the exam."],
        ["... to + V-inf", "She works overtime to earn more money."],
        ["... so that + S + can/will + V", "I'll leave early so that I can catch the bus."],
        ["... so that + S + could/would + V", "He spoke slowly so that everyone could understand."]
    ]),
    tbl(["Ví dụ"], [
        ["I'm saving money to buy a car."],
        ["She wrote it down so that she wouldn't forget."]
    ]),
    ["In order to trang trọng hơn to; nghĩa tương đương.", "So that thường đi với can, could, will, would, would like."],
    "To/In order to + V. So that + S + can/could/will/would + V.")

ex71("definite-article-the", "Cách dùng mạo từ The - Chi tiết",
    "The dùng cho: đã xác định (người nghe biết); duy nhất (the sun, the Earth); sông, biển, dãy núi; nhạc cụ (play the piano); so sánh nhất; The + adj = nhóm người (the poor, the rich).",
    tbl(["Dùng the", "Ví dụ"], [
        ["Sự vật duy nhất", "the sun, the moon, the Earth"],
        ["Sông, biển, dãy núi", "the Thames, the Pacific, the Alps"],
        ["Nhạc cụ", "play the guitar, learn the piano"],
        ["So sánh nhất", "the best, the most expensive"],
        ["The + adj = nhóm", "the poor, the elderly, the unemployed"]
    ]),
    tbl(["Ví dụ"], [
        ["The book I lent you. (đã xác định)"],
        ["The rich should help the poor."]
    ]),
    ["Không dùng the với tên riêng (Vietnam, Hanoi), bữa ăn (breakfast), môn học (math).", "Đã đề cập lần trước → dùng the."],
    "The = xác định, duy nhất, đã biết. The + adj = nhóm.")

ex71("zero-article", "Không dùng mạo từ - Zero Article",
    "Không dùng a/an/the với: bữa ăn (breakfast, lunch, dinner); môn học (math, history); ngôn ngữ (English); thể thao (football); tên riêng (Vietnam, Mary); danh từ số nhiều mang nghĩa chung.",
    tbl(["Không the", "Ví dụ"], [
        ["Bữa ăn", "I have breakfast at 7. We had lunch together."],
        ["Môn học, ngôn ngữ", "She studies English. I like history."],
        ["Thể thao", "He plays football. They love swimming."],
        ["Tên riêng", "I live in Hanoi. Vietnam is beautiful."]
    ]),
    tbl(["Lưu ý"], [
        ["I have breakfast. (zero) / The breakfast was delicious. (đã xác định)"],
        ["She speaks English. (ngôn ngữ) / The English language. (nhấn mạnh)"]
    ]),
    ["Danh từ không đếm được mang nghĩa chung: không the (Life is short.).", "Số nhiều chung: Cats are animals. (không the)."],
    "Meals, languages, sports, proper nouns → no article.")

ex71("few-little", "Few và Little - Phân biệt",
    "Few + N đếm được số nhiều: rất ít (mang nghĩa tiêu cực). A few: một vài (ít nhưng đủ). Little + N không đếm được: rất ít. A little: một chút (ít nhưng đủ).",
    tbl(["Từ", "Đi với", "Nghĩa", "Ví dụ"], [
        ["few", "N đếm được (plural)", "Rất ít (tiêu cực)", "Few people came. (ít người đến)"],
        ["a few", "N đếm được (plural)", "Một vài (đủ dùng)", "I have a few friends here."],
        ["little", "N không đếm được", "Rất ít (tiêu cực)", "There is little time left."],
        ["a little", "N không đếm được", "Một chút (đủ dùng)", "I need a little help."]
    ]),
    tbl(["Ví dụ"], [
        ["Few students passed. (rất ít) / A few students passed. (một vài)"],
        ["We have little money. (hầu như không) / We have a little money. (một chút)"]
    ]),
    ["Few/Little: gần như không đủ, mang nghĩa tiêu cực.", "A few/A little: ít nhưng vẫn có, đủ dùng."],
    "Few/A few + C (plural). Little/A little + U.")

ex71("another-other-the-other", "Another, Other, The other",
    "Another: một cái/người khác (số ít, không xác định). Other: những cái/người khác (số nhiều). The other: cái/người còn lại (xác định, có thể số ít hoặc số nhiều).",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["another", "Một cái khác (singular)", "I need another cup. Another day."],
        ["other", "Những cái khác (plural, không xác định)", "Other people think differently."],
        ["the other", "Cái/người còn lại (xác định)", "I have two books. One is here, the other is at home."],
        ["the others", "Những cái còn lại", "Some stayed, the others left."]
    ]),
    tbl(["Ví dụ"], [
        ["One student passed; the other failed."],
        ["I'll see you another time. (another = one more)"]
    ]),
    ["Another = an + other (một cái nữa).", "The other day = vài ngày trước (thành ngữ)."],
    "Another + singular. Other + plural. The other = còn lại.")

ex71("all-most-some-none", "All, Most, Some, None",
    "All (of): tất cả. Most (of): hầu hết. Some (of): một số. None (of): không ai/cái gì. None + V: có thể số ít (formal) hoặc số nhiều. All/Most/Some + N (plural) + V plural.",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["all (of)", "Tất cả", "All (of) the students passed. All children like games."],
        ["most (of)", "Hầu hết", "Most people agree. Most of the time."],
        ["some (of)", "Một số", "Some friends came. Some of the milk."],
        ["none (of)", "Không ai/cái gì", "None of them was/were there. I have none."]
    ]),
    tbl(["Ví dụ"], [
        ["All students passed. None of them was/were there."]
    ]),
    ["None of + N (plural): động từ số ít (formal) hoặc số nhiều đều chấp nhận.", "All/Most/Some có thể bỏ of khi theo sau là the, this, my..."],
    "All/Most/Some/None + (of) + N.")

ex71("each-every", "Each và Every",
    "Each: từng cái một (nhấn từng cá thể), dùng được cho 2 hoặc nhiều. Every: mọi (nhấn toàn bộ như một nhóm), thường từ 3 trở lên. Cả hai + N số ít + V số ít.",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["each", "Từng một (cá thể)", "Each student has a book. Each of us tried."],
        ["every", "Mọi (toàn bộ)", "Every child needs love. Every day/week."]
    ]),
    tbl(["Ví dụ"], [
        ["Each (of the two) answer is correct. (từng câu trả lời)"],
        ["Every room has a window. (mọi phòng)"]
    ]),
    ["Every không dùng với of (every one of, không phải every of).", "Each có thể đứng một mình: Each has their own room."],
    "Each + singular. Every + singular. Each = từng; Every = mọi.")

ex71("possessive-adjectives-pronouns", "Tính từ sở hữu và Đại từ sở hữu",
    "Tính từ sở hữu (my, your, his, her, its, our, their) luôn đứng trước danh từ. Đại từ sở hữu (mine, yours, his, hers, ours, theirs) thay thế danh từ, đứng một mình.",
    tbl(["Tính từ sở hữu", "Đại từ sở hữu", "Ví dụ"], [
        ["my", "mine", "This is my book. / This book is mine."],
        ["your", "yours", "Is this your bag? / This bag is yours."],
        ["his", "his", "That's his car. / That car is his."],
        ["her", "hers", "Her room is big. / This room is hers."],
        ["our", "ours", "Our house. / This house is ours."],
        ["their", "theirs", "Their idea. / The idea is theirs."]
    ]),
    tbl(["Ví dụ"], [
        ["I've got my ticket. Have you got yours?"],
        ["Her phone is new. Mine is old. (mine = my phone)"]
    ]),
    ["Its (sở hữu) khác it's (it is).", "Đại từ sở hữu không có mạo từ (a mine → sai)."],
    "My/Your/His/Her + N. Mine/Yours/His/Hers (thay N).")

ex71("reflexive-pronouns", "Đại từ phản thân - Reflexive Pronouns",
    "Myself, yourself, himself, herself, itself, ourselves, yourselves, themselves. Dùng khi chủ ngữ và tân ngữ cùng chỉ một đối tượng. By myself = alone. Enjoy yourself = chúc vui.",
    tbl(["Ngôi", "Đại từ phản thân"], [
        ["I", "myself"], ["you", "yourself (số ít) / yourselves (số nhiều)"],
        ["he/she/it", "himself/herself/itself"],
        ["we/they", "ourselves/themselves"]
    ]),
    tbl(["Cách dùng", "Ví dụ"], [
        ["Chủ ngữ = tân ngữ", "I hurt myself. She taught herself to play."],
        ["Nhấn mạnh (chính ai đó)", "I myself saw it. The manager himself replied."],
        ["By + reflexive = một mình", "I did it by myself. She lives by herself."]
    ]),
    ["Không dùng reflexive khi chủ ngữ và tân ngữ khác nhau: He hit him. (him = người khác).", "Một số động từ thường đi với reflexive: enjoy yourself, help yourself, behave yourself."],
    "Myself, yourself... By myself = alone.")

ex71("there-is-are", "There is / There are",
    "There is + N số ít / N không đếm được. There are + N số nhiều. Dùng để nói về sự tồn tại hoặc vị trí. There was/were (quá khứ), There will be, There has/have been.",
    tbl(["Thì", "Công thức", "Ví dụ"], [
        ["Hiện tại (số ít)", "There is + N", "There is a book on the table."],
        ["Hiện tại (số nhiều)", "There are + N", "There are two books on the table."],
        ["Quá khứ", "There was/were + N", "There was a problem. There were many people."],
        ["Tương lai", "There will be + N", "There will be a meeting tomorrow."]
    ]),
    tbl(["Ví dụ"], [
        ["There is some milk in the fridge. (không đếm được)"],
        ["There has been an accident. (hiện tại hoàn thành)"]
    ]),
    ["Động từ chia theo N đứng sau (there is a book and two pens → có thể dùng are).", "There + be khác với Have: There is a book = Có một cuốn sách; I have a book = Tôi có một cuốn sách."],
    "There is/are + N. N quyết định is/are/was/were.")

ex71("have-got", "Have got / Has got",
    "Have got = have (sở hữu, có). Dùng phổ biến trong tiếng Anh Anh. I've got, You've got, He/She/It has got, We/They've got. Phủ định: haven't got, hasn't got. Nghi vấn: Have you got...? Has she got...?",
    tbl(["Khẳng định", "Phủ định", "Nghi vấn"], [
        ["I've got a car.", "I haven't got a car.", "Have you got a car?"],
        ["She's got blue eyes.", "She hasn't got any money.", "Has he got time?"]
    ]),
    tbl(["Ví dụ"], [
        ["I've got two brothers. (= I have two brothers.)"],
        ["Have you got a pen? (Anh-Anh) / Do you have a pen? (Anh-Mỹ)"]
    ]),
    ["Have got thường không dùng trong thì tiếp diễn.", "Trong quá khứ: had got ít dùng; dùng had (I had a car)."],
    "Have got = have (possession). Haven't got / Hasn't got.")

ex71("imperatives", "Câu mệnh lệnh - Imperatives",
    "Câu mệnh lệnh dùng động từ nguyên thể (V-inf) ở đầu câu. Phủ định: Don't + V-inf. Nhấn mạnh: Do + V-inf. Dùng để ra lệnh, yêu cầu, chỉ dẫn, lời mời, cảnh báo.",
    tbl(["Loại", "Công thức", "Ví dụ"], [
        ["Khẳng định", "V-inf (+ O)", "Sit down. Close the door. Be quiet."],
        ["Phủ định", "Don't + V-inf", "Don't run. Don't be late."],
        ["Nhấn mạnh", "Do + V-inf", "Do be careful. Do come in."]
    ]),
    tbl(["Ví dụ"], [
        ["Open your book. (chỉ dẫn)"],
        ["Help yourself. (mời)"],
        ["Don't touch. (cảnh báo)"]
    ]),
    ["Chủ ngữ you thường được ẩn.", "Let's + V = đề nghị cùng làm: Let's go."],
    "V-inf. Don't + V-inf. Do + V (nhấn mạnh).")

ex71("exclamations-what-how", "Câu cảm thán - What và How",
    "What + (a/an) + adj + N!: nhấn mạnh danh từ. How + adj/adv + S + V!: nhấn mạnh tính từ/trạng từ. How + S + V!: nhấn mạnh động từ (How I miss you!).",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["What a/an + adj + N (singular)", "What a nice day! What an interesting book!"],
        ["What + adj + N (plural/U)", "What beautiful flowers! What nice weather!"],
        ["How + adj/adv + S + V", "How beautiful she is! How quickly he runs!"],
        ["How + S + V", "How I wish I could go! How you've grown!"]
    ]),
    tbl(["Ví dụ"], [
        ["What a pity! How amazing!"],
        ["How cold it is! What a mess!"]
    ]),
    ["What theo sau bởi danh từ (có a/an nếu danh từ đếm được số ít).", "How theo sau bởi adj/adv hoặc S + V."],
    "What a/an + adj + N! How + adj/adv + S + V!")

ex71("double-comparative", "So sánh kép - Double Comparative",
    "The + so sánh hơn + S + V, the + so sánh hơn + S + V. Diễn tả hai biến đổi cùng chiều: càng... càng...",
    tbl(["Công thức", "Ví dụ"], [
        ["The + comparative + S + V, the + comparative + S + V", "The more you study, the more you learn."],
        ["The sooner, the better.", "The older he gets, the wiser he becomes."]
    ]),
    tbl(["Ví dụ"], [
        ["The more I read, the less I understand. (càng đọc càng ít hiểu)"],
        ["The hotter it is, the more I want to swim."]
    ]),
    ["Hai mệnh đề đều dùng the + so sánh hơn.", "Có thể rút gọn: The more, the merrier."],
    "The more...the more... The + comparative...the + comparative.")

ex71("as-as-equality", "So sánh bằng - As...as",
    "As + adj/adv + as: ngang bằng. Not as/so + adj/adv + as: không bằng. As much/many + N + as: số lượng ngang bằng.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["as + adj/adv + as", "She is as tall as me. He runs as fast as you."],
        ["not as/so + adj/adv + as", "This is not as good as that. It's not so difficult as I thought."],
        ["as much + U + as", "I don't have as much time as you."],
        ["as many + C + as", "She has as many books as I do."]
    ]),
    tbl(["Ví dụ"], [
        ["Your bag is as heavy as mine."],
        ["He's not as old as he looks."]
    ]),
    ["So...as thường dùng trong câu phủ định (not so...as).", "As long as = miễn là (nghĩa khác)."],
    "As + adj/adv + as. Not as/so...as.")

ex71("relative-clauses-whose-whom", "Mệnh đề quan hệ - Whose, Whom",
    "Whose: thay cho his/her/their + N (sở hữu). Whom: thay cho người làm tân ngữ (trang trọng); có thể bỏ trong mệnh đề xác định. Who thay whom trong văn nói.",
    tbl(["Đại từ", "Vai trò", "Ví dụ"], [
        ["whose", "Sở hữu (his/her/their + N)", "The man whose car was stolen called the police."],
        ["whom", "Tân ngữ (người)", "The woman whom I met yesterday is a doctor. (formal)"],
        ["whom (có thể bỏ)", "Trong mệnh đề xác định", "The person (whom) I spoke to was helpful."]
    ]),
    tbl(["Ví dụ"], [
        ["That's the boy whose father is a pilot."],
        ["To whom did you give the letter? (very formal)"]
    ]),
    ["Whose luôn đứng trước danh từ.", "Trong văn nói: The woman I met (bỏ whom)."],
    "Whose + N. Whom = tân ngữ (người).")

ex71("participle-clauses", "Mệnh đề phân từ - Participle Clauses",
    "V-ing (present participle): chủ động, đồng thời hoặc trước. V3 (past participle): bị động. Dùng để rút gọn mệnh đề khi chủ ngữ giống nhau.",
    tbl(["Loại", "Công thức", "Ví dụ"], [
        ["Chủ động (đồng thời)", "V-ing + ..., S + V", "Walking in the park, I saw an old friend."],
        ["Chủ động (trước)", "Having + V3 + ..., S + V", "Having finished work, he went home."],
        ["Bị động", "V3 + ..., S + V", "Built in 1990, the house is quite old."]
    ]),
    tbl(["Ví dụ"], [
        ["Seeing her, I smiled. (= When I saw her, I smiled.)"],
        ["Written in simple English, the book is easy to read."]
    ]),
    ["Chủ ngữ của mệnh đề phân từ phải trùng với chủ ngữ mệnh đề chính.", "V3 (past participle) dùng cho bị động."],
    "V-ing (active). V3 (passive). Having + V3 (trước).")

ex71("direct-indirect-objects", "Tân ngữ trực tiếp và gián tiếp",
    "Tân ngữ gián tiếp (Oi): người nhận/làm. Tân ngữ trực tiếp (Od): vật/việc. S + V + Oi + Od hoặc S + V + Od + to/for + Oi. Give, send, show, tell + to. Buy, make, get + for.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["V + Oi + Od", "Give me the book. Tell her the news. Buy him a gift."],
        ["V + Od + to + Oi", "Give the book to me. Send the letter to her."],
        ["V + Od + for + Oi", "Buy a gift for him. Make coffee for us."]
    ]),
    tbl(["Động từ + to", "Động từ + for"], [
        ["give, send, show, tell, offer, pass", "buy, make, get, cook, find, choose"]
    ]),
    ["Oi (người) thường đứng trước Od (vật) khi không có giới từ.", "Khi Od là đại từ (it, them): Give it to me. (không nói Give me it.)"],
    "V + Oi + Od. V + Od + to/for + Oi.")

ex71("collocations-common", "Collocation thường gặp",
    "Collocation là cách kết hợp từ tự nhiên. Động từ + danh từ: make a decision, do homework, take a photo. Tính từ + danh từ: heavy rain, strong coffee. Trạng từ + tính từ: deeply sorry.",
    tbl(["Động từ", "Danh từ (thường đi kèm)", "Ví dụ"], [
        ["make", "decision, mistake, effort, noise", "Make a decision. Make a mistake."],
        ["do", "homework, research, exercise, one's best", "Do your homework. Do your best."],
        ["take", "photo, break, risk, place", "Take a photo. Take a break."],
        ["have", "breakfast, a look, fun, an effect", "Have breakfast. Have a look."]
    ]),
    tbl(["Ví dụ"], [
        ["Heavy rain (không nói strong rain). Strong coffee (không nói heavy coffee)."],
        ["Deeply sorry. Fully aware. Highly likely."]
    ]),
    ["Học theo cụm, không dịch từng từ.", "Tra từ điển collocation khi nghi ngờ."],
    "Make/Do/Take + N. Adj + N (heavy rain, strong coffee).")

ex71("word-formation-prefixes", "Cách tạo từ - Tiền tố (Prefixes)",
    "Tiền tố thêm vào đầu từ để đổi nghĩa. Phủ định: un-, in-, im-, il-, ir-, dis-, mis-. Nghĩa khác: re- (lại), pre- (trước), over- (quá), under- (dưới).",
    tbl(["Tiền tố", "Nghĩa", "Ví dụ"], [
        ["un-, in-, im-, il-, ir-, dis-", "Phủ định", "unhappy, incorrect, impossible, illegal, irregular, disagree"],
        ["mis-", "Sai", "misunderstand, mistake"],
        ["re-", "Lại", "rewrite, return, rebuild"],
        ["pre-", "Trước", "preview, pre-war"],
        ["over-", "Quá", "overload, overcook"]
    ]),
    tbl(["Ví dụ"], [
        ["Un- thường với adj: unfair, unable. In-: informal, invisible."],
        ["Im- trước p, m: impossible, immature. Il- trước l: illegal."]
    ]),
    ["Chính tả: im- trước p, m; il- trước l; ir- trước r.", "Một số từ không theo quy tắc: informal, impatient."],
    "Un-/In-/Dis- = not. Re- = again. Pre- = before.")

ex71("word-formation-suffixes", "Cách tạo từ - Hậu tố (Suffixes)",
    "Hậu tố thêm vào cuối từ để tạo danh từ, tính từ, trạng từ. -tion/-sion: N (action, decision). -ment: N (development). -ful: adj (careful). -less: adj (careless). -ly: adv (quickly). -er/-or: N chỉ người (teacher).",
    tbl(["Hậu tố", "Từ loại", "Ví dụ"], [
        ["-tion, -sion, -ment", "Danh từ", "action, decision, development"],
        ["-er, -or, -ist", "N (người)", "teacher, actor, scientist"],
        ["-ful, -less", "Tính từ", "careful, careless, useful"],
        ["-ly", "Trạng từ", "quickly, slowly, happily"],
        ["-able, -ible", "Tính từ", "comfortable, possible"]
    ]),
    tbl(["Ví dụ"], [
        ["Care → careful, careless, carefully."],
        ["Act → action, actor, active, actively."]
    ]),
    ["-ful = đầy (careful = đầy sự cẩn thận). -less = không có (careless).", "Tính từ tận cùng -y → -ily (happy → happily)."],
    "-tion/-ment = N. -ful/-less = adj. -ly = adv.")

ex71("capitalization-rules", "Quy tắc viết hoa - Capitalization",
    "Viết hoa: chữ cái đầu câu; đại từ I; tên riêng (người, địa danh, quốc gia); ngôn ngữ, quốc tịch; tháng, ngày lễ; tên môn học khi là tên cụ thể; tên công ty, sản phẩm.",
    tbl(["Viết hoa", "Ví dụ"], [
        ["Đầu câu", "The weather is nice. (T viết hoa)"],
        ["Tên riêng", "Hanoi, Vietnam, Mary, the Pacific"],
        ["Ngôn ngữ, quốc tịch", "English, Vietnamese, French"],
        ["Tháng, ngày lễ", "January, Christmas, Monday"],
        ["I", "My friend and I went there."]
    ]),
    tbl(["Không viết hoa"], [
        ["Mùa (trừ đứng đầu câu): spring, summer"],
        ["Môn học chung: I study maths. (nhưng: I study Mathematics 101.)"]
    ]),
    ["Tên riêng gồm nhiều từ: mỗi từ chính viết hoa (the United States).", "Sau dấu hai chấm: viết hoa nếu là câu hoàn chỉnh."],
    "First letter of sentence. Proper nouns. I. Months, days.")

ex71("punctuation-basics", "Dấu câu cơ bản - Punctuation",
    "Dấu chấm (.): kết thúc câu trần thuật. Dấu phẩy (,): liệt kê; sau trạng từ đầu câu; trước and/but trong câu ghép; mệnh đề không xác định. Dấu chấm hỏi (?): câu hỏi. Dấu chấm than (!): cảm thán.",
    tbl(["Dấu", "Cách dùng", "Ví dụ"], [
        [".", "Kết thúc câu", "I am a student."],
        [",", "Liệt kê; sau trạng từ", "I bought apples, oranges, and bananas. However, I was late."],
        ["?", "Câu hỏi", "Where are you?"],
        ["!", "Cảm thán", "What a beautiful day!"]
    ]),
    tbl(["Lưu ý"], [
        ["Trước and trong liệt kê: có thể có hoặc không dấu phẩy (Oxford comma)."],
        ["Sau e.g., i.e.: thường có dấu phẩy."]
    ]),
    ["Không dùng dấu phẩy tách chủ ngữ và động từ: The man, who was tired, left. (mệnh đề không xác định có dấu phẩy).", "Viết hoa sau dấu chấm."],
    "Period (.). Comma (,). Question (?). Exclamation (!).")

ex71("numbers-dates-time", "Số, ngày tháng, giờ",
    "Số đếm: one, two. Số thứ tự: first, second, third. Ngày: on + day (on Monday), the 25th of December. Tháng/năm: in January, in 2020. Giờ: at 3 o'clock; 3:15 = a quarter past three / fifteen past three; 3:30 = half past three.",
    tbl(["Loại", "Cách đọc / Viết", "Ví dụ"], [
        ["Số thứ tự", "first, second, third, fourth...", "the first floor, my second attempt"],
        ["Ngày", "on + day/date", "on Monday, on the 5th of May, on December 25th"],
        ["Tháng, năm", "in + month/year", "in January, in 2020"],
        ["Giờ", "at + time; past/to", "at 7. At 3:15 = a quarter past three. At 3:45 = a quarter to four."]
    ]),
    tbl(["Ví dụ"], [
        ["I was born on the 5th of May 1990."],
        ["It's half past six. (6:30)"]
    ]),
    ["On + ngày. In + tháng/năm. At + giờ.", "Số thứ tự: 1st, 2nd, 3rd, 4th, 21st, 22nd, 23rd."],
    "Ordinals: first, second. On + day. In + month/year. At + time.")

ex71("apostrophe-contractions", "Dấu nháy đơn - Apostrophe và Contractions",
    "Dấu nháy đơn (') dùng cho: sở hữu (the dog's tail); viết tắt (I'm, don't). Sở hữu số nhiều tận cùng s: students' (của các học sinh). Its (sở hữu) khác it's (it is).",
    tbl(["Cách dùng", "Ví dụ"], [
        ["Sở hữu (singular)", "the dog's tail, John's book, the child's toy"],
        ["Sở hữu (plural, tận cùng s)", "the students' room, the teachers' lounge"],
        ["Sở hữu (plural, không tận cùng s)", "the children's room, people's opinions"],
        ["Viết tắt", "I'm, don't, it's, we've, they're"]
    ]),
    tbl(["Lưu ý"], [
        ["its = của nó (sở hữu). it's = it is hoặc it has. Who's = who is. Whose = của ai."],
        ["Your ≠ you're. Their ≠ they're. There ≠ their."]
    ]),
    ["Không dùng 's với đại từ sở hữu: yours, ours, theirs (không your's).", "Sở hữu với tên kết thúc bằng s: James' book hoặc James's book."],
    "'s = is/has hoặc possessive. s' = plural possessive. Its ≠ it's.")

ex71("spelling-rules-ing-ed", "Quy tắc chính tả V-ing và V-ed",
    "V-ing: bỏ e (make → making); gấp đôi phụ âm khi âm tiết cuối = 1 nguyên âm + 1 phụ âm + stress (run → running). V-ed: tương tự (stop → stopped). Động từ tận cùng e: chỉ thêm d (love → loved).",
    tbl(["Quy tắc", "Ví dụ"], [
        ["Bỏ e + ing/ed", "make → making, made; love → loving, loved"],
        ["Gấp đôi phụ âm", "run → running, run; stop → stopped; prefer → preferring"],
        ["Y sau phụ âm → ied", "study → studied; try → tried"],
        ["Y sau nguyên âm: không đổi", "play → played; enjoy → enjoyed"]
    ]),
    tbl(["Ví dụ"], [
        ["Swim → swimming (gấp đôi m)."],
        ["Begin → beginning. Prefer → preferred."]
    ]),
    ["Gấp đôi khi: 1 nguyên âm + 1 phụ âm + nhấn âm cuối (begin → beginning).", "Không gấp đôi: open → opening (nhấn âm đầu); visit → visiting (2 phụ âm)."],
    "Double consonant: 1 vowel + 1 consonant + stress.")

ex71("sentence-types", "Các loại câu theo mục đích",
    "Câu trần thuật (declarative): nêu thông tin. Câu hỏi (interrogative): hỏi. Câu mệnh lệnh (imperative): ra lệnh, yêu cầu. Câu cảm thán (exclamatory): bày tỏ cảm xúc mạnh.",
    tbl(["Loại", "Mục đích", "Ví dụ"], [
        ["Declarative", "Trần thuật", "I am a student. The sky is blue."],
        ["Interrogative", "Hỏi", "Are you OK? Where do you live?"],
        ["Imperative", "Mệnh lệnh, yêu cầu", "Sit down. Please close the door."],
        ["Exclamatory", "Cảm thán", "What a day! How beautiful!"]
    ]),
    tbl(["Ví dụ"], [["Statement, question, command, exclamation."]]),
    ["Mỗi loại có cấu trúc và dấu câu riêng.", "Câu hỏi kết thúc bằng ?. Câu cảm thán thường có !."],
    "Declarative (.). Interrogative (?). Imperative. Exclamatory (!).")

ex71("simple-compound-complex", "Câu đơn, câu ghép, câu phức",
    "Câu đơn: một mệnh đề độc lập. Câu ghép: hai hoặc nhiều mệnh đề độc lập nối bằng and, but, or, so. Câu phức: một mệnh đề độc lập + một hoặc nhiều mệnh đề phụ thuộc (because, when, although, that...).",
    tbl(["Loại", "Đặc điểm", "Ví dụ"], [
        ["Câu đơn", "1 mệnh đề độc lập", "I left. She is tired."],
        ["Câu ghép", "2+ độc lập, nối and/but/or", "I left and she stayed. I tried but I failed."],
        ["Câu phức", "1 độc lập + 1+ phụ thuộc", "I left because she stayed. When he came, we left."]
    ]),
    tbl(["Ví dụ"], [
        ["Simple: The dog barked."],
        ["Compound: The dog barked and the cat ran away."],
        ["Complex: When the dog barked, the cat ran away."]
    ]),
    ["Mệnh đề phụ thuộc không đứng một mình thành câu.", "Liên từ phụ thuộc: because, when, although, if, that, who, which."],
    "Simple: 1 clause. Compound: and/but/or. Complex: subordinator.")

ex71("connectors-linking", "Từ nối - Connectors và Linking words",
    "Thêm ý: and, moreover, furthermore, in addition. Tương phản: but, however, although, whereas. Nguyên nhân: because, since, as. Kết quả: so, therefore, as a result. Trình tự: first, then, finally, afterwards.",
    tbl(["Chức năng", "Từ nối", "Ví dụ"], [
        ["Thêm ý", "and, moreover, furthermore", "I was tired. Moreover, I had a headache."],
        ["Tương phản", "but, however, although", "I was tired. However, I went out."],
        ["Nguyên nhân", "because, since, as", "I stayed home because it rained."],
        ["Kết quả", "so, therefore", "He was ill. Therefore, he didn't come."],
        ["Trình tự", "first, then, finally", "First, mix the flour. Then add the eggs."]
    ]),
    tbl(["Ví dụ"], [["I was tired. However, I went out."]]),
    ["However thường đứng đầu câu mới, sau dấu chấm.", "Although + clause. Despite + N/V-ing."],
    "And, but, however, because, so, first, then, therefore.")

ex71("common-mistakes-vietnamese", "Lỗi thường gặp (người Việt học tiếng Anh)",
    "Nhầm since/for (since + điểm thời gian, for + khoảng). Say vs tell (say sth; tell sb sth). Make vs do (make a cake, do homework). Bỏ 's' ngôi 3 số ít (he go → he goes). Much vs many (much + U, many + C).",
    tbl(["Lỗi", "Đúng", "Ví dụ"], [
        ["since/for", "since + điểm; for + khoảng", "I have been here for 2 years. Since 2020."],
        ["say/tell", "say + (sth); tell + sb + sth", "He says hello. She tells me a story."],
        ["make/do", "make: tạo ra; do: thực hiện", "Make a cake. Do homework. Do your best."],
        ["Ngôi 3 số ít", "He/She/It + V-s/es", "She likes coffee. He goes to work."],
        ["much/many", "much + N không đếm được; many + N đếm được", "Much time. Many people."]
    ]),
    tbl(["Ví dụ đúng"], [
        ["I have lived here since 2020. I have lived here for three years."],
        ["Could you tell me the time? He said (that) he was busy."]
    ]),
    ["Since + mốc (since Monday, since 2020). For + khoảng (for 2 hours, for a week).", "Learn/Teach: learn sth; teach sb sth. Hear/Listen: hear = nghe thấy; listen = lắng nghe."],
    "Since/For. Say/Tell. Make/Do. Third person -s. Much/Many.")

# ========== 101-200: Thêm ~100 bài mới (đầy đủ nội dung) ==========
def add(id_, title, definition, formula, examples, usage, signals):
    lessons.append(lesson("lesson", id_, title, definition, formula, examples, usage, signals))

# 101-110: Thì & thể bổ sung, Mixed conditional
add("future-perfect-continuous", "Thì tương lai hoàn thành tiếp diễn - Future Perfect Continuous",
    "S + will have been + V-ing. Diễn tả hành động sẽ đã đang diễn ra được bao lâu tính đến một thời điểm trong tương lai. Ít dùng trong thực tế.",
    tbl(["Công thức", "Ví dụ"], [
        ["S + will have been + V-ing", "By next month, I will have been working here for 5 years."],
        ["By the time + S + V, S + will have been + V-ing", "By the time you arrive, I will have been waiting for an hour."]
    ]),
    tbl(["Ví dụ"], [
        ["She will have been studying for 3 hours by 6pm."],
        ["How long will you have been living there by 2026?"]
    ]),
    ["Thường dùng với by + time, by then.", "Nhấn mạnh độ dài của hành động đến một mốc tương lai."],
    "By + time. Will have been + V-ing.")

add("mixed-conditional", "Câu điều kiện hỗn hợp - Mixed Conditional",
    "Kết hợp điều kiện quá khứ và kết quả hiện tại: If + had V3, S + would + V. (Nếu quá khứ đã khác thì hiện tại đã khác). Hoặc điều kiện hiện tại + kết quả quá khứ (ít gặp).",
    tbl(["Loại", "Công thức", "Ví dụ"], [
        ["Quá khứ → Hiện tại", "If + had V3, S + would/could + V", "If I had studied harder, I would have a better job now."],
        ["Hiện tại → Quá khứ", "If + V2, S + would have V3", "If I were you, I would have told her."]
    ]),
    tbl(["Ví dụ"], [
        ["If she had taken the train, she wouldn't be late now."],
        ["If I liked him, I would have gone to his party."]
    ]),
    ["Diễn tả hậu quả kéo dài đến hiện tại của điều kiện quá khứ.", "If I had... → ...would V (không phải would have V3)."],
    "If + had V3, would + V (present result).")

add("passive-past-continuous", "Bị động thì quá khứ tiếp diễn",
    "S + was/were being + V3. Diễn tả hành động đang bị thực hiện tại một thời điểm trong quá khứ.",
    tbl(["Chủ động", "Bị động"], [
        ["S + was/were + V-ing + O", "S + was/were being + V3 (by O)"],
        ["They were building the bridge.", "The bridge was being built."]
    ]),
    tbl(["Ví dụ"], [
        ["The house was being painted when I left."],
        ["My car was being repaired yesterday afternoon."]
    ]),
    ["Dùng khi nhấn mạnh hành động đang diễn ra (bị động) trong quá khứ."],
    "Was/Were being + V3.")

add("passive-future-simple", "Bị động thì tương lai đơn",
    "S + will be + V3 (by O). Diễn tả hành động sẽ bị thực hiện trong tương lai.",
    tbl(["Chủ động", "Bị động"], [
        ["S + will + V + O", "S + will be + V3 (by O)"],
        ["They will deliver the package.", "The package will be delivered."]
    ]),
    tbl(["Ví dụ"], [
        ["The meeting will be held next Monday."],
        ["You will be informed when it's ready."]
    ]),
    ["Will be + V3. Có thể thêm by + O nếu cần nêu tác nhân."],
    "Will be + V3.")

add("passive-with-get", "Bị động với Get",
    "Get + V3 đôi khi dùng thay be + V3 trong bị động, thường cho hành động bất ngờ hoặc khó chịu. Get married, get dressed, get lost, get hurt.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["get + V3", "My phone got stolen. He got hurt in the accident."],
        ["get + adj (V3 như adj)", "get married, get dressed, get lost, get bored"]
    ]),
    tbl(["Ví dụ"], [
        ["She got promoted last year."],
        ["I always get confused when I read the map."]
    ]),
    ["Get + V3 thường dùng trong văn nói.", "Một số cụm cố định: get married, get dressed, get lost."],
    "Get + V3. Get married/dressed/lost.")

add("need-doing-need-to-be-done", "Need + V-ing / Need to be + V3",
    "Need + V-ing = need to be + V3: cần được (làm). The room needs cleaning = The room needs to be cleaned. Chủ ngữ thường là vật.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["S (thing) + need(s) + V-ing", "The car needs washing. Your hair needs cutting."],
        ["S + need(s) + to be + V3", "The car needs to be washed. The report needs to be finished."]
    ]),
    tbl(["Ví dụ"], [
        ["This letter needs signing. (= needs to be signed)"],
        ["The plants need watering every day."]
    ]),
    ["Chủ ngữ thường là vật (the car, the room).", "V-ing ở đây mang nghĩa bị động."],
    "Need + V-ing = need to be + V3.")

add("would-prefer-would-rather", "Would prefer và Would rather - Chi tiết",
    "Would prefer + to V: thích làm gì hơn. Would prefer + N + to V: thích (ai đó) làm gì. Would rather + V: thích làm gì. Would rather + S + V2: thích (ai đó) làm gì (hiện tại). Would rather + S + had V3: thích (điều đã xảy ra khác đi).",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["would prefer + to V", "I would prefer to stay home."],
        ["would prefer + N + to V", "I would prefer you to tell the truth."],
        ["would rather + V", "I would rather go by train."],
        ["would rather + S + V2", "I'd rather you didn't smoke here."],
        ["would rather + S + had V3", "I'd rather you had told me earlier."]
    ]),
    tbl(["Ví dụ"], [
        ["Would you prefer tea or coffee? — I'd prefer tea."],
        ["I'd rather not say. (would rather not + V)"]
    ]),
    ["Prefer đi với to V. Rather đi với V (không to).", "Would rather + S + V2: lùi thì (hiện tại)."],
    "Would prefer to V. Would rather V. Would rather S + V2.")

add("had-better-should-ought", "Had better, Should, Ought to - So sánh",
    "Had better + V: nên (gần cảnh báo, hậu quả nếu không làm). Should + V: nên (lời khuyên chung). Ought to + V: nên (trang trọng hơn should). Had better thường viết 'd better.",
    tbl(["Từ", "Sắc thái", "Ví dụ"], [
        ["had better", "Mạnh, gần cảnh báo", "You'd better leave now or you'll miss the bus."],
        ["should", "Lời khuyên chung", "You should see a doctor."],
        ["ought to", "Trang trọng, nghĩa vụ đạo đức", "We ought to help them."]
    ]),
    tbl(["Ví dụ"], [
        ["You'd better not be late. (had better not + V)"],
        ["We ought to have told them. (ought to have V3 = đáng lẽ đã nên)"]
    ]),
    ["Had better không dùng trong câu hỏi thông thường.", "Ought to have V3: đáng lẽ đã nên làm (nhưng không làm)."],
    "Had better (warning). Should (advice). Ought to (formal).")

add("may-might-could-possibility", "May, Might, Could - Phỏng đoán khả năng",
    "May/Might/Could + V: có thể (phỏng đoán, không chắc). Might yếu hơn may. Could cũng diễn tả khả năng trong quá khứ hoặc hiện tại. May/Might/Could + have V3: phỏng đoán về quá khứ.",
    tbl(["Hiện tại", "Quá khứ"], [
        ["She may/might/could be at home.", "She may/might/could have left early."],
        ["It might rain. (khả năng thấp)", "He might have forgotten. (phỏng đoán)"]
    ]),
    tbl(["Ví dụ"], [
        ["The meeting could be cancelled. (có thể)"],
        ["She may have already left. (có thể đã...)"]
    ]),
    ["Might ít chắc chắn hơn may. Could vừa khả năng vừa điều kiện.", "May/Might/Could + have V3: phỏng đoán về việc đã xảy ra."],
    "May/Might/Could + V. + have V3 (past).")

add("must-have-to-difference", "Must và Have to - Khác nhau chi tiết",
    "Must: bắt buộc do bản thân (nghĩa vụ, quyết định). Mustn't: cấm. Have to: bắt buộc do ngoại cảnh (quy định, ai đó yêu cầu). Don't have to: không cần (không bắt buộc). Had to: quá khứ của cả must và have to.",
    tbl(["Must", "Have to"], [
        ["Bản thân nghĩ ra", "Do quy định/hoàn cảnh bên ngoài"],
        ["I must finish this today. (tôi quyết định)", "I have to wear a uniform. (quy định)"],
        ["Mustn't = cấm", "Don't have to = không cần"]
    ]),
    tbl(["Ví dụ"], [
        ["You mustn't smoke here. (cấm)"],
        ["You don't have to come. (không bắt buộc)"]
    ]),
    ["Quá khứ: had to (must không có quá khứ).", "Must không dùng trong thì tương lai; dùng will have to."],
    "Must (internal). Have to (external). Mustn't = prohibit. Don't have to = not necessary.")

# 111-125: Phrasal verbs, cụm từ, thành ngữ
add("phrasal-verbs-look", "Cụm động từ với Look",
    "Look after: chăm sóc. Look at: nhìn. Look for: tìm kiếm. Look forward to + V-ing: mong đợi. Look up: tra (từ điển). Look up to: ngưỡng mộ. Look down on: coi thường. Look into: điều tra.",
    tbl(["Phrasal verb", "Nghĩa", "Ví dụ"], [
        ["look after", "Chăm sóc", "She looks after her grandmother."],
        ["look for", "Tìm kiếm", "I'm looking for my keys."],
        ["look forward to", "Mong đợi", "I look forward to seeing you."],
        ["look up", "Tra (từ điển)", "Look up the word in a dictionary."],
        ["look up to", "Ngưỡng mộ", "I look up to my teacher."]
    ]),
    tbl(["Ví dụ"], [
        ["Look at the board. Look into the problem."],
        ["We're looking forward to your visit."]
    ]),
    ["Look forward to theo sau bởi V-ing (không to V).", "Look up to / look down on: theo sau là người (object)."],
    "Look after, look for, look forward to, look up.")

add("phrasal-verbs-take", "Cụm động từ với Take",
    "Take off: cất cánh; cởi (quần áo). Take on: nhận (việc), thuê. Take care of: chăm sóc. Take part in: tham gia. Take place: diễn ra. Take up: bắt đầu (sở thích); chiếm (không gian). Take over: tiếp quản.",
    tbl(["Phrasal verb", "Nghĩa", "Ví dụ"], [
        ["take off", "Cất cánh; cởi", "The plane took off. Take off your coat."],
        ["take care of", "Chăm sóc", "I'll take care of the children."],
        ["take part in", "Tham gia", "She took part in the competition."],
        ["take place", "Diễn ra", "The meeting will take place on Monday."],
        ["take up", "Bắt đầu (sở thích)", "He took up painting last year."]
    ]),
    tbl(["Ví dụ"], [
        ["Take off your shoes before entering."],
        ["The concert took place in the park."]
    ]),
    ["Take place = happen (không bị động).", "Take off (cất cánh): The plane took off at 6."],
    "Take off, take care of, take part in, take place, take up.")

add("phrasal-verbs-get", "Cụm động từ với Get",
    "Get up: thức dậy. Get on/off: lên/xuống (xe). Get in/out: vào/ra (xe). Get along (with): hòa thuận. Get over: vượt qua (bệnh, shock). Get through: vượt qua (khó khăn); liên lạc được. Get rid of: loại bỏ. Get used to: quen với.",
    tbl(["Phrasal verb", "Nghĩa", "Ví dụ"], [
        ["get up", "Thức dậy", "I get up at 7 every day."],
        ["get on/off", "Lên/xuống xe", "Get on the bus. Get off at the next stop."],
        ["get over", "Vượt qua", "She got over her illness. I can't get over the shock."],
        ["get along with", "Hòa thuận", "I get along well with my colleagues."],
        ["get rid of", "Loại bỏ", "We need to get rid of these old files."]
    ]),
    tbl(["Ví dụ"], [
        ["Get in the car. Get out of the room."],
        ["I finally got through to the manager."]
    ]),
    ["Get used to + V-ing/N (quen với). Khác used to + V (đã từng).", "Get over + N (vượt qua bệnh, nỗi buồn)."],
    "Get up, get on/off, get over, get along with, get rid of.")

add("phrasal-verbs-put", "Cụm động từ với Put",
    "Put on: mặc vào; bật (đèn, nhạc). Put off: hoãn lại. Put away: cất đi. Put up with: chịu đựng. Put out: dập (lửa). Put down: đặt xuống; ghi chép. Put forward: đưa ra (ý kiến).",
    tbl(["Phrasal verb", "Nghĩa", "Ví dụ"], [
        ["put on", "Mặc; bật", "Put on your jacket. Put on some music."],
        ["put off", "Hoãn", "We had to put off the meeting."],
        ["put away", "Cất đi", "Put away your toys."],
        ["put up with", "Chịu đựng", "I can't put up with this noise."],
        ["put out", "Dập lửa", "They put out the fire."]
    ]),
    tbl(["Ví dụ"], [
        ["Put on your seatbelt. Put off the decision."],
        ["She put forward a new idea."]
    ]),
    ["Put on (mặc): Put your shoes on / Put on your shoes.", "Put off = postpone."],
    "Put on, put off, put away, put up with, put out.")

add("phrasal-verbs-come", "Cụm động từ với Come",
    "Come in: vào. Come back: quay lại. Come from: đến từ. Come across: tình cờ gặp. Come up with: nảy ra (ý tưởng). Come along: đi cùng; tiến triển. Come true: thành hiện thực.",
    tbl(["Phrasal verb", "Nghĩa", "Ví dụ"], [
        ["come in", "Vào", "Come in, please."],
        ["come back", "Quay lại", "When will you come back?"],
        ["come across", "Tình cờ gặp", "I came across an old friend yesterday."],
        ["come up with", "Nảy ra (ý tưởng)", "She came up with a great idea."],
        ["come true", "Thành hiện thực", "His dream came true."]
    ]),
    tbl(["Ví dụ"], [
        ["How's the project coming along? (tiến triển)"],
        ["She comes from Japan."]
    ]),
    ["Come across = tình cờ gặp hoặc tìm thấy.", "Come up with = think of (nảy ra ý tưởng)."],
    "Come in, come back, come across, come up with, come true.")

add("idioms-common-1", "Thành ngữ thường gặp (1)",
    "Break the ice: phá vỡ sự im lặng. Piece of cake: dễ như ăn bánh. Once in a blue moon: hiếm khi. Hit the books: học hành chăm chỉ. Under the weather: không khỏe. On the same page: đồng ý, cùng quan điểm.",
    tbl(["Thành ngữ", "Nghĩa", "Ví dụ"], [
        ["break the ice", "Phá vỡ sự im lặng", "He told a joke to break the ice."],
        ["piece of cake", "Rất dễ", "The test was a piece of cake."],
        ["once in a blue moon", "Hiếm khi", "I see him once in a blue moon."],
        ["under the weather", "Không khỏe", "I'm feeling under the weather today."],
        ["on the same page", "Đồng ý", "We need to be on the same page."]
    ]),
    tbl(["Ví dụ"], [
        ["It's a piece of cake. Don't worry."],
        ["She's a bit under the weather."]
    ]),
    ["Thành ngữ thường không dịch từng từ.", "Học theo ngữ cảnh và ví dụ."],
    "Break the ice, piece of cake, under the weather, on the same page.")

add("idioms-common-2", "Thành ngữ thường gặp (2)",
    "Cost an arm and a leg: rất đắt. Sit on the fence: chần chừ không quyết. Miss the boat: lỡ cơ hội. When pigs fly: không bao giờ xảy ra. Spill the beans: tiết lộ bí mật. Let the cat out of the bag: lỡ tiết lộ.",
    tbl(["Thành ngữ", "Nghĩa", "Ví dụ"], [
        ["cost an arm and a leg", "Rất đắt", "That car costs an arm and a leg."],
        ["miss the boat", "Lỡ cơ hội", "If you don't apply now, you'll miss the boat."],
        ["when pigs fly", "Không bao giờ", "He'll apologize when pigs fly."],
        ["spill the beans", "Tiết lộ bí mật", "Someone spilled the beans about the party."],
        ["sit on the fence", "Chần chừ", "Don't sit on the fence; make a decision."]
    ]),
    tbl(["Ví dụ"], [
        ["The repair cost an arm and a leg."],
        ["She let the cat out of the bag."]
    ]),
    ["Thành ngữ thường dùng trong văn nói.", "Spill the beans = let the cat out of the bag (tiết lộ)."],
    "Cost an arm and a leg, miss the boat, spill the beans.")

add("greetings-responses", "Chào hỏi và Đáp lại",
    "Chào: Hi, Hello, Good morning/afternoon/evening. Hỏi thăm: How are you? How's it going? What's up? Đáp: I'm fine, thanks. Not bad. Pretty good. So-so. Can't complain.",
    tbl(["Tình huống", "Câu", "Đáp thường gặp"], [
        ["Trang trọng", "Good morning. How do you do?", "Good morning. How do you do? / I'm well, thank you."],
        ["Thân mật", "Hi! How are you? / How's it going?", "I'm good, thanks. And you? / Not bad."],
        ["Rất thân mật", "What's up? / What's new?", "Not much. Same old. / Nothing much."]
    ]),
    tbl(["Ví dụ"], [
        ["— How are you? — I'm fine, thanks. And you?"],
        ["— What's up? — Not much. Just studying."]
    ]),
    ["How do you do? thường đáp bằng How do you do? (trang trọng).", "What's up? có thể chỉ là lời chào, không cần trả lời chi tiết."],
    "Hi, Hello. How are you? I'm fine. What's up?")

add("polite-requests", "Yêu cầu lịch sự - Polite Requests",
    "Could you...? Would you mind + V-ing? Can you...? I was wondering if you could... Do you mind if I...? Is it OK if I...? Cách đáp: Of course. Sure. No problem. I'm afraid I can't. I'd rather you didn't.",
    tbl(["Mức độ", "Cách nói", "Ví dụ"], [
        ["Bình thường", "Can you...? Could you...?", "Can you pass the salt? Could you help me?"],
        ["Lịch sự", "Would you mind + V-ing?", "Would you mind closing the door?"],
        ["Rất lịch sự", "I was wondering if you could...", "I was wondering if you could lend me your pen."],
        ["Xin phép", "Do you mind if I...? Is it OK if I...?", "Do you mind if I sit here?"]
    ]),
    tbl(["Đáp lại"], [
        ["Would you mind...? — No, not at all. / Of course not. (đồng ý)"],
        ["Do you mind if I...? — No, go ahead. / I'd prefer you didn't. (từ chối lịch sự)"]
    ]),
    ["Would you mind + V-ing: đáp 'No' = tôi không phiền = đồng ý.", "Do you mind if I V: đáp 'No' = không phiền = đồng ý."],
    "Could you...? Would you mind V-ing? Do you mind if I...?")

add("agreeing-disagreeing", "Đồng ý và Không đồng ý",
    "Đồng ý: I agree. I think so too. Exactly. That's right. Absolutely. Không đồng ý lịch sự: I'm not sure. I see your point, but... I don't think so. I'm afraid I disagree. Đồng ý một phần: I partly agree. I agree with you to some extent.",
    tbl(["Đồng ý", "Không đồng ý (lịch sự)", "Ví dụ"], [
        ["I agree. I think so too.", "I'm not sure I agree. I see your point, but...", "— It's a good idea. — I agree. / I'm not sure."],
        ["Exactly. That's right.", "I'm afraid I disagree.", "— So we need more time. — Exactly."],
        ["Absolutely.", "I don't think so.", "— We should go. — I don't think so."]
    ]),
    tbl(["Ví dụ"], [
        ["I see your point, but I think we should wait."],
        ["I agree with you to some extent, but there are risks."]
    ]),
    ["Trong tranh luận trang trọng dùng I'm afraid I disagree.", "I see your point = tôi hiểu ý bạn (trước khi nói ý khác)."],
    "I agree. I don't think so. I see your point, but...")

add("giving-opinions", "Đưa ra ý kiến - Giving Opinions",
    "I think/believe (that)... In my opinion,... From my point of view,... As I see it,... It seems to me that... I'd say that... Asking: What do you think? What's your opinion? How do you feel about...?",
    tbl(["Cách nói", "Ví dụ"], [
        ["I think (that)...", "I think we should leave early."],
        ["In my opinion,...", "In my opinion, the plan is too risky."],
        ["From my point of view,...", "From my point of view, it's a good idea."],
        ["It seems to me that...", "It seems to me that he's right."],
        ["I'd say that...", "I'd say that's not enough."]
    ]),
    tbl(["Hỏi ý kiến"], [
        ["What do you think (about)...? What's your view? How do you feel about it?"]
    ]),
    ["In my view = In my opinion.", "I reckon (informal) = I think."],
    "I think. In my opinion. From my point of view. What do you think?")

add("making-suggestions", "Đưa ra gợi ý - Making Suggestions",
    "Let's + V. Why don't we + V? How about + V-ing? What about + V-ing? We could + V. Shall we + V? I suggest + V-ing / that S + V. Recommending: I'd recommend... You might want to...",
    tbl(["Cách nói", "Ví dụ"], [
        ["Let's + V", "Let's go to the cinema."],
        ["Why don't we + V?", "Why don't we try the new restaurant?"],
        ["How about / What about + V-ing?", "How about watching a film? What about pizza?"],
        ["We could + V", "We could ask John for help."],
        ["Shall we + V?", "Shall we start now?"]
    ]),
    tbl(["Đáp lại"], [
        ["Good idea. Sounds good. I'm up for that. I'd rather not. I'm not sure."]
    ]),
    ["How about/What about theo sau bởi V-ing hoặc N.", "Shall we...? thường dùng cho gợi ý làm cùng nhau."],
    "Let's. Why don't we? How about V-ing? Shall we?")

add("apologizing-forgiving", "Xin lỗi và Tha thứ",
    "Xin lỗi: I'm sorry. I apologize. I'm so sorry for... It was my fault. Sorry for the inconvenience. Đáp: That's OK. No problem. Don't worry about it. It doesn't matter. I forgive you. Accepting: I accept your apology.",
    tbl(["Xin lỗi", "Đáp lại"], [
        ["I'm sorry. / I'm so sorry.", "That's OK. / No problem. / Don't worry."],
        ["I apologize for the delay.", "Apology accepted. / That's all right."],
        ["It was my fault.", "It's fine. / We all make mistakes."],
        ["Sorry for the inconvenience.", "No worries. / It happens."]
    ]),
    tbl(["Ví dụ"], [
        ["I'm sorry I'm late. — That's OK. Don't worry about it."],
        ["I apologize for the mistake. — I accept your apology."]
    ]),
    ["I'm sorry to hear that = chia buồn (khi ai đó gặp chuyện không hay).", "Formal: I would like to apologize for..."],
    "I'm sorry. That's OK. Don't worry. I forgive you.")

add("expressing-gratitude", "Bày tỏ lòng biết ơn",
    "Thank you. Thanks. Thanks a lot. Thank you very much. I'm grateful for... I really appreciate... I can't thank you enough. Responding: You're welcome. No problem. Don't mention it. My pleasure. Anytime. It was nothing.",
    tbl(["Cảm ơn", "Đáp lại"], [
        ["Thank you. / Thanks.", "You're welcome. / No problem."],
        ["Thanks a lot. / Thank you so much.", "You're welcome. / My pleasure."],
        ["I really appreciate your help.", "I'm glad I could help. / Anytime."],
        ["I'm grateful for your support.", "Don't mention it. / It was nothing."]
    ]),
    tbl(["Ví dụ"], [
        ["Thank you for your help. — You're welcome."],
        ["I really appreciate it. — My pleasure."]
    ]),
    ["Appreciate + N/V-ing (I appreciate your help. I appreciate being invited).", "Formal: I would like to express my gratitude."],
    "Thank you. Thanks a lot. You're welcome. My pleasure.")

# 126-140: Relative clauses nâng cao, Reported speech chi tiết, Confusing words
add("relative-clauses-when-where-why", "Mệnh đề quan hệ - When, Where, Why",
    "When: thay cho at/on which (thời gian). Where: thay cho at/in which (nơi chốn). Why: thay cho for which (lý do), thường với reason. The day when we met. The place where I was born. The reason why he left.",
    tbl(["Đại từ", "Thay cho", "Ví dụ"], [
        ["when", "at/on/during + time", "That was the day when we first met. I remember the time when we were happy."],
        ["where", "at/in + place", "This is the house where I grew up. The place where we met is a café."],
        ["why", "for + reason", "That's the reason why he left. Do you know the reason why she's upset?"]
    ]),
    tbl(["Ví dụ"], [
        ["I'll never forget the day when I got the job."],
        ["The reason why I'm late is that my car broke down."]
    ]),
    ["When/Where/Why có thể bỏ trong mệnh đề xác định (the day we met).", "The reason why = the reason that; why có thể bỏ."],
    "When (time). Where (place). Why (reason).")

add("defining-non-defining-clauses", "Mệnh đề quan hệ xác định và không xác định",
    "Mệnh đề xác định (defining): cần thiết để hiểu danh từ, không có dấu phẩy. Mệnh đề không xác định (non-defining): bổ sung thông tin, có dấu phẩy, không bỏ được. Which có thể dùng trong non-defining; that không dùng trong non-defining.",
    tbl(["Loại", "Ví dụ", "Ghi chú"], [
        ["Xác định (không dấu phẩy)", "The book that I bought is good. The man who called is my brother.", "Bỏ mệnh đề thì câu không rõ nghĩa. Có thể dùng that."],
        ["Không xác định (có dấu phẩy)", "My brother, who lives in Paris, is a doctor. The book, which I bought yesterday, is good.", "Bổ sung thông tin. Không dùng that. Không bỏ được."]
    ]),
    tbl(["Ví dụ"], [
        ["Students who work hard usually pass. (xác định: những học sinh nào?)"],
        ["My sister, who is a teacher, lives in Hanoi. (không xác định: thêm thông tin về chị tôi)"]
    ]),
    ["Tên riêng + mệnh đề quan hệ thường là non-defining (Mary, who is my friend, ...).", "Which trong non-defining có thể thay cả mệnh đề trước: He was late, which made me angry."],
    "Defining: no comma, that OK. Non-defining: comma, which, no that.")

add("reported-speech-commands", "Câu tường thuật - Câu mệnh lệnh và đề nghị",
    "Chuyển mệnh lệnh: tell/ask/order + O + (not) to V. 'Stay here.' → He told me to stay there. 'Don't go.' → She asked me not to go. Đề nghị: offer to V, suggest V-ing / that S + V, advise sb to V.",
    tbl(["Trực tiếp", "Gián tiếp"], [
        ["'Sit down.'", "He told me to sit down."],
        ["'Don't be late.'", "She asked us not to be late."],
        ["'Shall I help you?'", "He offered to help me."],
        ["'Let's go out.'", "She suggested going out. / She suggested that we (should) go out."]
    ]),
    tbl(["Ví dụ"], [
        ["'Please wait here.' → He asked me to wait there."],
        ["'You should see a doctor.' → He advised me to see a doctor."]
    ]),
    ["Tell/Ask/Order + O + to V. Suggest + V-ing hoặc suggest that S + (should) V.", "Offer to V. Advise sb to V."],
    "Tell/Ask + O + to V. Suggest V-ing. Offer to V.")

add("say-tell-talk-speak", "Say, Tell, Talk, Speak - Phân biệt",
    "Say: nói (say sth; say that...; say to sb). Tell: kể, bảo (tell sb sth; tell sb that...; tell sb to V). Talk: nói chuyện (talk to/with sb; talk about sth). Speak: nói (ngôn ngữ, phát biểu) (speak English; speak to sb).",
    tbl(["Động từ", "Cấu trúc", "Ví dụ"], [
        ["say", "say (sth); say to sb; say that...", "He said hello. He said (that) he was tired. He said to me that..."],
        ["tell", "tell sb sth; tell sb that...; tell sb to V", "Tell me the truth. She told me (that) she would come. He told me to wait."],
        ["talk", "talk to/with sb (about sth)", "We talked about the project. I need to talk to you."],
        ["speak", "speak (language); speak to sb", "She speaks English. Can I speak to the manager?"]
    ]),
    tbl(["Ví dụ"], [
        ["He said nothing. He told me a story. We talked for an hour. She speaks three languages."]
    ]),
    ["Tell luôn có tân ngữ chỉ người (tell me, tell her). Say không bắt buộc (he said).", "Talk thường có to/with. Speak a language; talk about a topic."],
    "Say sth. Tell sb sth. Talk to sb about. Speak (language).")

add("make-do-difference", "Make và Do - Phân biệt chi tiết",
    "Make: tạo ra, chế tạo, gây ra (make a cake, make a decision, make noise, make a mistake). Do: thực hiện hành động, làm (do homework, do exercise, do one's best, do research). Một số cụm cố định cần học thuộc.",
    tbl(["Make", "Do"], [
        ["make a cake/meal", "do homework/exercise"],
        ["make a decision/mistake", "do your best"],
        ["make noise/money", "do research/the shopping"],
        ["make a phone call", "do the washing up"],
        ["make progress", "do a job"]
    ]),
    tbl(["Ví dụ"], [
        ["I need to make a decision. She made a lot of money."],
        ["I have to do my homework. He did his best."]
    ]),
    ["Make thường tạo ra cái mới hoặc kết quả. Do thường là hành động công việc.", "Make a mistake (không do). Do your hair (làm tóc). Make a bed (dọn giường)."],
    "Make: create, produce. Do: perform, execute. Learn collocations.")

add("affect-effect", "Affect và Effect - Phân biệt",
    "Affect: động từ = ảnh hưởng đến. Effect: danh từ = ảnh hưởng, kết quả. Effect cũng có thể là động từ (effect change = thực hiện thay đổi) nhưng ít dùng. Ví dụ: The weather affected our plans. The effect of the drug was strong.",
    tbl(["Từ", "Từ loại", "Nghĩa", "Ví dụ"], [
        ["affect", "Động từ", "Ảnh hưởng đến", "The rain affected the match. Stress affects your health."],
        ["effect", "Danh từ", "Ảnh hưởng, kết quả", "The effect was immediate. Side effects."],
        ["effect (v)", "Động từ (ít dùng)", "Thực hiện (thay đổi)", "To effect change."]
    ]),
    tbl(["Ví dụ"], [
        ["How does this affect you? (affect = V)"],
        ["What is the effect? (effect = N)"]
    ]),
    ["Nhớ: Affect = Action (động từ). Effect = End result (danh từ).", "Effect (v) = bring about, thường dùng trong văn formal."],
    "Affect (v) = ảnh hưởng. Effect (n) = ảnh hưởng, kết quả.")

add("rise-raise-raise-arise", "Rise, Raise, Arise - Phân biệt",
    "Rise (rose, risen): nội động từ = mọc, tăng, đứng dậy (không có tân ngữ). Raise (raised, raised): ngoại động từ = nâng, nuôi, tăng (có tân ngữ). Arise (arose, arisen): nảy sinh (vấn đề, tình huống).",
    tbl(["Động từ", "Loại", "Nghĩa", "Ví dụ"], [
        ["rise", "Nội động từ", "Mọc, tăng, đứng dậy", "The sun rises. Prices rose. He rose from his chair."],
        ["raise", "Ngoại động từ", "Nâng, nuôi, tăng (cái gì đó)", "Raise your hand. Raise children. Raise prices."],
        ["arise", "Nội động từ", "Nảy sinh", "Problems arose. A question arose."]
    ]),
    tbl(["Ví dụ"], [
        ["Prices are rising. (không tân ngữ)"],
        ["They raised the price. (có tân ngữ)"]
    ]),
    ["Rise = tự tăng. Raise = làm (cái gì) tăng.", "Arise thường dùng với problem, question, situation."],
    "Rise (no object). Raise + object. Arise (problems arise).")

add("lay-lie-lie", "Lay và Lie - Phân biệt",
    "Lay (laid, laid): đặt, đặt xuống (có tân ngữ). Lie (lay, lain): nằm (nội động từ, không tân ngữ). Lie (lied, lied): nói dối. Lay = đặt cái gì xuống. Lie = tự nằm xuống.",
    tbl(["Động từ", "Quá khứ", "Quá khứ hoàn thành", "Ví dụ"], [
        ["lay (đặt)", "laid", "laid", "Lay the book on the table. He laid the baby down."],
        ["lie (nằm)", "lay", "lain", "I need to lie down. The book was lying on the table."],
        ["lie (nói dối)", "lied", "lied", "Don't lie to me. He lied about his age."]
    ]),
    tbl(["Ví dụ"], [
        ["Lay the table (dọn bàn). The hen lays eggs."],
        ["Lie down. I lay in bed (quá khứ của lie = nằm)."]
    ]),
    ["Lay cần tân ngữ (lay something). Lie (nằm) không có tân ngữ.", "Quá khứ của lie (nằm) là lay — dễ nhầm với lay (đặt)."],
    "Lay (laid) + object. Lie (lay, lain) = recline. Lie (lied) = tell a lie.")

add("learn-teach", "Learn và Teach - Phân biệt",
    "Learn: học (learn sth; learn from sb; learn to V; learn how to V). Teach: dạy (teach sb; teach sb sth; teach sb to V; teach sth). Learn = tiếp thu. Teach = truyền đạt.",
    tbl(["Động từ", "Cấu trúc", "Ví dụ"], [
        ["learn", "learn (sth); learn from sb; learn to V", "I'm learning English. I learned from my mistakes. She learned to drive."],
        ["teach", "teach sb; teach sb sth; teach sb to V", "She teaches children. He taught me French. My father taught me to swim."]
    ]),
    tbl(["Ví dụ"], [
        ["I learned a lot from that course. (learn from)"],
        ["She teaches math at the university. (teach + subject)"]
    ]),
    ["Learn how to V = học cách làm. Teach sb a lesson = dạy cho ai một bài học (thành ngữ).", "Self-taught = tự học."],
    "Learn = học. Teach = dạy. Learn from. Teach sb sth.")

add("hear-listen", "Hear và Listen - Phân biệt",
    "Hear: nghe thấy (không chủ ý, giác quan). Listen: lắng nghe (chủ ý). Listen to + N. Hear thường không dùng thì tiếp diễn (trừ khi nhấn mạnh đang nghe). Hear about/of: nghe nói về. Hear from: nhận tin từ ai.",
    tbl(["Động từ", "Nghĩa", "Ví dụ"], [
        ["hear", "Nghe thấy (không chủ ý)", "I heard a noise. I can't hear you."],
        ["listen", "Lắng nghe (chủ ý)", "Listen to me. I was listening to music."],
        ["hear about/of", "Nghe nói về", "I heard about the accident."],
        ["hear from", "Nhận tin từ", "I haven't heard from him for weeks."]
    ]),
    tbl(["Ví dụ"], [
        ["Did you hear that? (nghe thấy)"],
        ["Please listen to the instructions. (lắng nghe)"]
    ]),
    ["Listen luôn có to (listen to). Hear không cần to.", "Hear from = receive news from."],
    "Hear = nghe thấy. Listen to = lắng nghe. Hear from = nhận tin.")

add("see-watch-look", "See, Watch, Look - Phân biệt",
    "See: thấy (không chủ ý hoặc khả năng). Look: nhìn (chủ ý, ngắn). Look at + N. Watch: xem (chủ ý, theo dõi một thời gian — TV, trận đấu). See = giác quan; look = hướng mắt; watch = xem có diễn biến.",
    tbl(["Động từ", "Nghĩa", "Ví dụ"], [
        ["see", "Thấy (không chủ ý / khả năng)", "I saw a bird. I can't see well."],
        ["look", "Nhìn (chủ ý, ngắn)", "Look at the board. Look! A rainbow."],
        ["watch", "Xem (theo dõi)", "Watch TV. Watch a football match."]
    ]),
    tbl(["Ví dụ"], [
        ["I looked at the photo. (nhìn)"],
        ["We watched a movie. (xem từ đầu đến cuối)"]
    ]),
    ["Look at + N. Watch + N (chương trình, trận đấu).", "See a film/movie (Anh-Mỹ cũng dùng see)."],
    "See = thấy. Look at = nhìn. Watch = xem (TV, match).")

add("borrow-lend", "Borrow và Lend - Phân biệt",
    "Borrow: mượn (từ ai) — borrow sth from sb. Lend: cho mượn — lend sb sth / lend sth to sb. Chủ thể borrow là người nhận; chủ thể lend là người cho.",
    tbl(["Động từ", "Nghĩa", "Cấu trúc", "Ví dụ"], [
        ["borrow", "Mượn", "borrow sth from sb", "I borrowed a book from the library. Can I borrow your pen?"],
        ["lend", "Cho mượn", "lend sb sth / lend sth to sb", "Can you lend me some money? She lent her car to him."]
    ]),
    tbl(["Ví dụ"], [
        ["I borrowed $10 from my friend. (tôi mượn)"],
        ["My friend lent me $10. (bạn tôi cho mượn)"]
    ]),
    ["Borrow from. Lend to. Lend = give temporarily.", "Loan (n/v) = cho vay (formal), lend thường dùng hơn trong nói."],
    "Borrow from (mượn). Lend to (cho mượn).")

add("hope-wish-expect", "Hope, Wish, Expect - Phân biệt",
    "Hope: hy vọng (có thể xảy ra). Hope (that) + S + V (thì hiện tại cho tương lai). Wish: ước (thường không thật). Wish + S + V2 (hiện tại); wish + had V3 (quá khứ). Expect: mong đợi (dự đoán sẽ xảy ra). Expect to V / expect (that)...",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["hope", "Hy vọng (có thể)", "I hope (that) you feel better. I hope to see you soon."],
        ["wish", "Ước (không thật)", "I wish I were rich. I wish I had known."],
        ["expect", "Mong đợi (dự đoán)", "I expect (that) he'll come. We expect to finish by Friday."]
    ]),
    tbl(["Ví dụ"], [
        ["I hope it doesn't rain. (hy vọng)"],
        ["I wish I could fly. (ước không thật)"],
        ["We expect a large crowd. (mong đợi sẽ có)"]
    ]),
    ["Hope + present tense for future: I hope she comes. (không will).", "Wish + past: unreal. Hope + (that) + S + V: real possibility."],
    "Hope = hy vọng. Wish = ước (unreal). Expect = mong đợi.")

# 141-155: Formal vs informal, Writing tips, Reading
add("formal-informal-english", "Tiếng Anh trang trọng và không trang trọng",
    "Trang trọng (formal): dùng trong văn bản, email công việc, thuyết trình. Không trang trọng (informal): nói chuyện, tin nhắn. Khác nhau: từ vựng (commence vs start), cấu trúc (Would you like... vs Do you want...), viết tắt (I am vs I'm).",
    tbl(["Formal", "Informal", "Ví dụ"], [
        ["commence", "start", "The meeting will commence at 9."],
        ["require", "need", "We require your assistance."],
        ["approximately", "about", "Approximately 100 people attended."],
        ["I would like to", "I want to", "I would like to inquire."],
        ["Could you please", "Can you", "Could you please send the file?"]
    ]),
    tbl(["Ví dụ"], [
        ["Formal: I am writing to inform you... Informal: Just wanted to let you know..."],
        ["Formal: Yours sincerely. Informal: Best, / See you."]
    ]),
    ["Trong email: Dear Mr X (formal). Hi John (informal).", "Tránh viết tắt (don't, I'm) trong văn formal."],
    "Formal: commence, require, Could you. Informal: start, need, Can you.")

add("linking-paragraphs", "Liên kết đoạn văn - Linking Paragraphs",
    "Để nối các đoạn: dùng từ nối đầu đoạn (Firstly, Secondly; However; Moreover; In conclusion). Lặp lại từ khóa hoặc dùng đại từ thay thế. Câu chủ đề (topic sentence) mỗi đoạn nên liên quan đến ý chính bài.",
    tbl(["Vị trí", "Từ/Cách", "Ví dụ"], [
        ["Đầu đoạn (thêm ý)", "Firstly, Secondly, Furthermore, Moreover", "Firstly, we need to consider the cost. Furthermore, time is limited."],
        ["Đầu đoạn (tương phản)", "However, On the other hand, Nevertheless", "However, there are some drawbacks."],
        ["Đầu đoạn (kết quả)", "Therefore, As a result, Consequently", "Therefore, we decided to cancel."],
        ["Kết luận", "In conclusion, To sum up, In summary", "In conclusion, the project was a success."]
    ]),
    tbl(["Ví dụ"], [
        ["First paragraph: introduce topic. Second: However, ... Third: Moreover, ... Conclusion: In conclusion, ..."]
    ]),
    ["Topic sentence thường là câu đầu đoạn.", "Tránh bắt đầu mọi đoạn bằng Same word (đa dạng hóa)."],
    "Firstly, However, Moreover, Therefore, In conclusion.")

add("topic-sentence-supporting", "Câu chủ đề và Câu hỗ trợ",
    "Câu chủ đề (topic sentence): nêu ý chính của đoạn, thường đứng đầu. Câu hỗ trợ (supporting sentences): giải thích, ví dụ, chi tiết làm rõ ý chính. Câu kết (concluding sentence): tóm lại ý đoạn (tùy chọn).",
    tbl(["Thành phần", "Vai trò", "Ví dụ"], [
        ["Topic sentence", "Ý chính đoạn", "Learning a language has many benefits."],
        ["Supporting 1", "Giải thích / ví dụ", "First, it opens up job opportunities."],
        ["Supporting 2", "Thêm chi tiết", "Second, it helps you connect with people."],
        ["Supporting 3", "Ví dụ cụ thể", "For example, when I learned English, I got a better job."],
        ["Concluding", "Tóm lại", "In short, it is worth the effort."]
    ]),
    tbl(["Ví dụ"], [
        ["(Topic) Exercise is important. (Support) It keeps you healthy. It reduces stress. (Conclude) So try to exercise regularly."]
    ]),
    ["Một đoạn thường một ý chính.", "Supporting sentences có thể dùng ví dụ, số liệu, so sánh."],
    "Topic sentence → Supporting → Concluding.")

add("skimming-scanning", "Skimming và Scanning - Đọc nhanh",
    "Skimming: đọc lướt để nắm ý chính (đọc tiêu đề, câu đầu đoạn, câu kết). Scanning: đọc quét để tìm thông tin cụ thể (số, tên, từ khóa). Skimming = overview. Scanning = find specific info.",
    tbl(["Kỹ thuật", "Mục đích", "Cách làm"], [
        ["Skimming", "Nắm ý chính", "Đọc tiêu đề, câu đầu và cuối mỗi đoạn, từ khóa. Bỏ qua chi tiết."],
        ["Scanning", "Tìm thông tin cụ thể", "Tìm số, tên, từ khóa. Mắt di chuyển nhanh, dừng khi thấy từ liên quan."]
    ]),
    tbl(["Ví dụ"], [
        ["Skimming: Đọc bài báo để trả lời 'What is the main idea?'"],
        ["Scanning: Tìm năm 2020 trong bài để trả lời 'When did it happen?'"]
    ]),
    ["Skimming trước khi đọc chi tiết giúp não định hướng.", "Scanning dùng khi câu hỏi hỏi chi tiết (who, when, where)."],
    "Skimming = main idea. Scanning = find specific info.")

add("context-clues", "Đoán nghĩa từ ngữ cảnh - Context Clues",
    "Khi gặp từ mới: xem câu trước/sau; từ đồng nghĩa (such as, like, or); từ trái nghĩa (but, however, although); giải thích (that is, in other words); ví dụ. Không cần tra từ điển mọi từ.",
    tbl(["Loại gợi ý", "Ví dụ"], [
        ["Định nghĩa / Giải thích", "A veterinarian, that is, a doctor for animals, ..."],
        ["Đồng nghĩa", "He was exhausted, or very tired."],
        ["Trái nghĩa", "She was reluctant, but her friend was eager to go."],
        ["Ví dụ", "Pets such as dogs and cats need care."]
    ]),
    tbl(["Ví dụ"], [
        ["'The room was cluttered.' — Đoán: nhiều đồ bừa bộn (từ ngữ cảnh phòng)."],
        ["'He was frugal, unlike his brother who spent freely.' — frugal = tiết kiệm."]
    ]),
    ["Đọc cả câu/cả đoạn trước khi đoán.", "Context clues giúp tăng vốn từ khi đọc."],
    "Such as, that is, but, however → clues.")

add("conjunctions-coordinating", "Liên từ kết hợp - Coordinating Conjunctions",
    "FANBOYS: For, And, Nor, But, Or, Yet, So. Nối từ, cụm từ, hoặc mệnh đề cùng loại. Trước FANBOYS nối hai mệnh đề độc lập thường có dấu phẩy. And: thêm. But: tương phản. Or: lựa chọn. So: kết quả.",
    tbl(["Liên từ", "Nghĩa", "Ví dụ"], [
        ["and", "Và (thêm)", "I like tea and coffee."],
        ["but", "Nhưng (tương phản)", "She's tired but she's working."],
        ["or", "Hoặc (lựa chọn)", "Tea or coffee?"],
        ["so", "Vì vậy (kết quả)", "It was cold, so I wore a coat."],
        ["yet", "Nhưng (tương phản, trang trọng)", "He's young, yet he's very wise."],
        ["for", "Vì (lý do, trang trọng)", "I stayed home, for I was ill."]
    ]),
    tbl(["Ví dụ"], [
        ["We wanted to go, but we had no time."],
        ["She didn't call, nor did she write."]
    ]),
    ["Nor thường đi với đảo ngữ: Nor did I. (Tôi cũng không.)", "Dấu phẩy trước but, and, or, so khi nối hai mệnh đề."],
    "FANBOYS: For, And, Nor, But, Or, Yet, So.")

add("conjunctions-subordinating", "Liên từ phụ thuộc - Subordinating Conjunctions",
    "Liên từ phụ thuộc nối mệnh đề phụ với mệnh đề chính. Thời gian: when, while, before, after, until, since. Lý do: because, since, as. Nhượng bộ: although, though, even though. Điều kiện: if, unless. Mục đích: so that, in order that.",
    tbl(["Loại", "Liên từ", "Ví dụ"], [
        ["Thời gian", "when, while, before, after, until", "When I arrived, she was cooking. Wait until I come back."],
        ["Lý do", "because, since, as", "I left because I was tired. Since you're here, let's start."],
        ["Nhượng bộ", "although, though, even though", "Although it rained, we went out."],
        ["Điều kiện", "if, unless", "If you come, I'll be happy. I won't go unless you go."]
    ]),
    tbl(["Ví dụ"], [
        ["She left before I could say goodbye."],
        ["I'll call you as soon as I arrive."]
    ]),
    ["Mệnh đề phụ có thể đứng trước hoặc sau mệnh đề chính.", "When mệnh đề phụ đứng trước: dấu phẩy sau mệnh đề phụ."],
    "When, because, although, if. Subordinate clause + main clause.")

add("question-words-review", "Từ để hỏi - Question Words (Ôn tập)",
    "What: cái gì. Who: ai (chủ ngữ). Whom: ai (tân ngữ, formal). Whose: của ai. Which: cái nào (trong số đã biết). When: khi nào. Where: ở đâu. Why: tại sao. How: như thế nào. How much/many: bao nhiêu. How long: bao lâu.",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["What", "Cái gì", "What did you buy? What time is it?"],
        ["Who", "Ai (chủ ngữ)", "Who called? Who is that?"],
        ["When", "Khi nào", "When did you leave? When is the meeting?"],
        ["Where", "Ở đâu", "Where do you live? Where is the station?"],
        ["Why", "Tại sao", "Why are you late? Why did she leave?"],
        ["How", "Như thế nào", "How are you? How do you do it?"]
    ]),
    tbl(["Ví dụ"], [
        ["How much does it cost? How many people? How long have you been here?"],
        ["Which one do you want? (which = lựa chọn trong số đã biết)"]
    ]),
    ["Who làm chủ ngữ: Who saw you? (không dùng did). Who làm tân ngữ: Who did you see?", "How + adj: How old, How far, How often."],
    "What, Who, When, Where, Why, How. How much/many/long.")

add("short-answers", "Câu trả lời ngắn - Short Answers",
    "Câu trả lời Yes/No ngắn: dùng trợ động từ + chủ ngữ (đại từ). Yes, I do. No, I don't. Yes, she has. No, we can't. Chủ ngữ phải là đại từ (I, you, he, she, it, we, they). Không lặp lại cả câu.",
    tbl(["Câu hỏi", "Trả lời ngắn (khẳng định)", "Trả lời ngắn (phủ định)"], [
        ["Do you like it?", "Yes, I do.", "No, I don't."],
        ["Is she coming?", "Yes, she is.", "No, she isn't."],
        ["Have you finished?", "Yes, I have.", "No, I haven't."],
        ["Can they swim?", "Yes, they can.", "No, they can't."]
    ]),
    tbl(["Ví dụ"], [
        ["— Are you tired? — Yes, I am. / No, I'm not."],
        ["— Did he go? — Yes, he did. / No, he didn't."]
    ]),
    ["Trợ động từ phải khớp với câu hỏi (Do you...? → Yes, I do.).", "Không nói Yes, I like. Phải nói Yes, I do."],
    "Yes, I do. No, she doesn't. Trợ ĐT + đại từ.")

add("ellipsis-substitution", "Tỉnh lược và Thay thế - Ellipsis and Substitution",
    "Tỉnh lược (ellipsis): bỏ từ lặp (I like tea and she likes coffee → and she coffee, hoặc and she does). Thay thế: dùng do/does/did, so/not thay cho động từ hoặc mệnh đề. I think so. I hope not. So do I.",
    tbl(["Cách", "Ví dụ"], [
        ["Bỏ từ lặp", "She bought a red dress and I bought a blue (dress)."],
        ["Do/Does/Did thay V", "She likes it. — So do I. (I like it too.)"],
        ["So/Not thay clause", "Is it true? — I think so. / I hope not."],
        ["One/Ones thay N", "I want the red one. I prefer the big ones."]
    ]),
    tbl(["Ví dụ"], [
        ["— Will you come? — I hope so. (I hope I will come.)"],
        ["— Do you have a pen? — Yes, I have one."]
    ]),
    ["So = câu khẳng định (I think so). Not = câu phủ định (I hope not).", "One/Ones thay danh từ đếm được (the red one)."],
    "So do I. I think so. One/ones. Ellipsis.")

add("emphasis-different-ways", "Nhấn mạnh - Các cách nhấn mạnh",
    "Nhấn mạnh bằng: (1) Câu chẻ It is...that. (2) Trợ động từ (I DO want to go. He DID call.). (3) Very, really, absolutely + adj. (4) So/Such. (5) Đảo ngữ (Never have I seen...). (6) Reflexive: I myself saw it.",
    tbl(["Cách", "Ví dụ"], [
        ["Câu chẻ", "It was John who broke it. It was yesterday that we met."],
        ["Trợ động từ", "I do like it. She did tell me. Do sit down."],
        ["Very/Really", "I'm very tired. It's really important."],
        ["Reflexive", "The manager himself replied. I myself don't agree."]
    ]),
    tbl(["Ví dụ"], [
        ["I do want to help. (nhấn mạnh want)"],
        ["Never have I seen such a mess. (đảo ngữ)"]
    ]),
    ["Do/Does/Did nhấn mạnh động từ: phát âm nhấn vào do/did.", "It is...that có thể nhấn mạnh nhiều thành phần."],
    "It is...that. Do + V. Very/Really. Reflexive. Inversion.")

# 156-170: Các chủ đề bổ sung
add("quantifiers-all-every-each", "Lượng từ: All, Every, Each - Ôn và mở rộng",
    "All + N (plural/U): tất cả. Every + N (singular): mọi (nhấn từng cá thể trong tổng thể). Each + N (singular): từng một. Every: nhấn toàn bộ; each: nhấn từng cá thể. Every 3 days = mỗi 3 ngày.",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["all", "Tất cả (toàn bộ)", "All students passed. All the time."],
        ["every", "Mọi (từng một trong tổng thể)", "Every student has a book. Every day."],
        ["each", "Từng một (riêng lẻ)", "Each person spoke. Each of us tried."]
    ]),
    tbl(["Ví dụ"], [
        ["Every two weeks = mỗi hai tuần. Each way = mỗi chiều."],
        ["All the money. Every single day. Each and every one."]
    ]),
    ["Every không đi với of (every one of us). Each (of) + N + V singular.", "All (of) the + N. Every + N (singular)."],
    "All (plural/U). Every (singular, all). Each (singular, individual).")

add("no-none-nothing-nobody", "No, None, Nothing, Nobody - Phân biệt",
    "No + N: không (cái gì). None: không ai/cái gì (đại từ, thường none of). Nothing: không có gì. Nobody/No one: không ai. None of + N (plural): V số ít (formal) hoặc số nhiều. Nothing/Nobody + V số ít.",
    tbl(["Từ", "Cách dùng", "Ví dụ"], [
        ["no + N", "Không (cái gì đó)", "I have no time. There's no milk."],
        ["none", "Không ai/cái gì (đại từ)", "None of them came. I have none."],
        ["nothing", "Không có gì", "I have nothing to say. Nothing happened."],
        ["nobody / no one", "Không ai", "Nobody knew. No one was there."]
    ]),
    tbl(["Ví dụ"], [
        ["No news is good news. (no + N)"],
        ["None of the students was/were late. (none of + plural)"]
    ]),
    ["Nothing = not anything. Nobody = not anybody. Không dùng double negative: I don't know nothing → sai; đúng: I don't know anything.", "None có thể trả lời How many/much? — None."],
    "No + N. None (of). Nothing. Nobody/No one.")

add("already-yet-still-any-more", "Already, Yet, Still, Any more",
    "Already: đã (trong câu khẳng định, thường với present perfect). Yet: chưa (phủ định, câu hỏi; cuối câu). Still: vẫn còn (khẳng định hoặc phủ định; đang tiếp diễn). Any more / Any longer: không còn nữa (trong phủ định).",
    tbl(["Từ", "Vị trí", "Nghĩa", "Ví dụ"], [
        ["already", "Giữa have/has và V3; hoặc cuối câu", "Đã", "I have already finished. She's already left."],
        ["yet", "Cuối câu (phủ định, hỏi)", "Chưa", "Have you eaten yet? I haven't done it yet."],
        ["still", "Trước động từ (sau be)", "Vẫn", "I'm still waiting. She still loves him."],
        ["any more", "Cuối câu (phủ định)", "Không còn nữa", "I don't see him any more. She doesn't work here any more."]
    ]),
    tbl(["Ví dụ"], [
        ["Have you finished yet? — Yes, I've already finished."],
        ["He still hasn't called. (still + phủ định = vẫn chưa)"]
    ]),
    ["Already trong câu hỏi: ngạc nhiên (Have you already finished?).", "Still trong phủ định = vẫn chưa (annoyance). Any more = không còn (nữa)."],
    "Already (done). Yet (not done). Still (continuing). Any more (no longer).")

add("so-neither-nor-agreement", "So, Neither, Nor - Đồng ý (Ôn chi tiết)",
    "So + trợ ĐT + S: đồng ý khẳng định. Neither/Nor + trợ ĐT + S: đồng ý phủ định. Trợ động từ phải khớp thì và chủ ngữ. I am → So am I. I have → So have I. I can → So can I. I did → So did I.",
    tbl(["Câu gốc", "Đồng ý (+)", "Đồng ý (-)"], [
        ["I'm tired.", "So am I.", "—"],
        ["I like coffee.", "So do I.", "—"],
        ["I don't like tea.", "—", "Neither do I. / Nor do I."],
        ["I haven't been there.", "—", "Neither have I."],
        ["I can swim.", "So can I.", "—"]
    ]),
    tbl(["Ví dụ"], [
        ["— I've been to Japan. — So have I."],
        ["— I won't go. — Neither will I."]
    ]),
    ["Me too (informal) = So am I / So do I.", "Trợ động từ phải đúng: I am → So am I (không So do I)."],
    "So + aux + S (agree +). Neither/Nor + aux + S (agree -).")

add("review-lesson-1", "Ôn tập tổng hợp 1 - Thì và Câu điều kiện",
    "Ôn lại: 12 thì cơ bản (present simple/continuous, past simple/continuous, future, perfect...). Câu điều kiện 0, 1, 2, 3 và mixed. Dấu hiệu nhận biết (time markers) và cách chọn thì phù hợp.",
    tbl(["Nhóm", "Nội dung"], [
        ["Thì", "Present (simple, continuous, perfect, perfect cont), Past (simple, continuous, perfect, perfect cont), Future (simple, continuous, perfect)."],
        ["Câu điều kiện", "Type 0: fact. Type 1: real future. Type 2: unreal present. Type 3: unreal past. Mixed."]
    ]),
    tbl(["Gợi ý"], [
        ["Làm bài tập chọn thì. Viết câu với các time markers (yesterday, for 2 years, by 2025...)."]
    ]),
    ["Chọn thì theo time marker và ngữ cảnh.", "Câu điều kiện: if + thì nào → mệnh đề chính thì nào."],
    "Review tenses. Review conditionals. Practice.")

add("review-lesson-2", "Ôn tập tổng hợp 2 - Bị động và Modal",
    "Ôn: Bị động (be + V3) với các thì; bị động với modal (can be done, must be done). Động từ khuyết thiếu: can, could, may, might, must, have to, should, ought to, would rather, had better. Phân biệt must vs have to, can vs be able to.",
    tbl(["Nhóm", "Nội dung"], [
        ["Bị động", "S + be + V3 (by O). Các thì: is done, was done, will be done, has been done. Modal: can be done, must be done."],
        ["Modal", "Can (ability, permission), Must (obligation), Should (advice), May/Might (possibility), Have to (external obligation)."]
    ]),
    tbl(["Gợi ý"], [
        ["Chuyển câu chủ động sang bị động. Điền modal phù hợp (can, must, should...)."]
    ]),
    ["Bị động: chủ ngữ là người/vật chịu tác động.", "Mustn't = cấm. Don't have to = không cần."],
    "Passive: be + V3. Modals: can, must, should, may, might.")

add("review-lesson-3", "Ôn tập tổng hợp 3 - Từ nối và Mệnh đề",
    "Ôn: Liên từ (and, but, because, although, when). Mệnh đề quan hệ (who, which, that, whose, whom, when, where, why). Defining vs non-defining. Câu phức với mệnh đề trạng ngữ (when, although, because...).",
    tbl(["Nhóm", "Nội dung"], [
        ["Từ nối", "And, but, or, so. Because, although, when, if. However, therefore, moreover."],
        ["Mệnh đề quan hệ", "Who, which, that (defining). Who, which, whose, whom, when, where, why. Non-defining (comma)."]
    ]),
    tbl(["Gợi ý"], [
        ["Nối hai câu bằng liên từ. Rút gọn bằng mệnh đề quan hệ (who, which)."]
    ]),
    ["Mệnh đề phụ có thể đứng trước hoặc sau mệnh đề chính.", "Defining: không dấu phẩy. Non-defining: dấu phẩy."],
    "Conjunctions. Relative clauses. Complex sentences.")

add("review-lesson-4", "Ôn tập tổng hợp 4 - Từ vựng và Collocation",
    "Ôn: Collocation (make/do/take + N). Phrasal verbs thường gặp (look, get, take, put, come). Thành ngữ (idioms). Phân biệt từ dễ nhầm (say/tell, make/do, borrow/lend, affect/effect, rise/raise).",
    tbl(["Nhóm", "Nội dung"], [
        ["Collocation", "Make a decision, do homework, take a break. Heavy rain, strong coffee."],
        ["Phrasal verbs", "Look after, get over, take off, put off, come across. Learn by theme."],
        ["Confusing words", "Say vs tell. Make vs do. Borrow vs lend. Affect vs effect."]
    ]),
    tbl(["Gợi ý"], [
        ["Học cụm từ theo chủ đề. Đặt câu với phrasal verbs và idioms."]
    ]),
    ["Tra collocation khi nghi ngờ.", "Phrasal verb: nghĩa thường khác động từ gốc."],
    "Collocations. Phrasal verbs. Confusing words.")

add("review-lesson-5", "Ôn tập tổng hợp 5 - Viết và Giao tiếp",
    "Ôn: Câu đơn/ghép/phức. Topic sentence và supporting sentences. Linking words (Firstly, However, In conclusion). Cách chào hỏi, xin lỗi, cảm ơn, đưa ý kiến, gợi ý. Formal vs informal. Skimming và scanning.",
    tbl(["Kỹ năng", "Nội dung"], [
        ["Viết", "Paragraph structure. Topic + supporting + concluding. Linking paragraphs."],
        ["Nói", "Greetings, thanks, apologies. Giving opinion, suggesting. Agreeing, disagreeing. Polite requests."]
    ]),
    tbl(["Gợi ý"], [
        ["Viết một đoạn văn có topic sentence và 2–3 supporting sentences."],
        ["Luyện hội thoại: cảm ơn, xin lỗi, đưa gợi ý."]
    ]),
    ["Viết: một đoạn một ý. Nói: dùng cụm lịch sự (Could you...? I'd appreciate...).", "Đọc: skimming cho ý chính, scanning cho chi tiết."],
    "Writing: topic sentence, linking. Speaking: polite phrases. Reading: skimming, scanning.")

# 158-200: Thêm bài đến đủ 200
add("can-be-able-to", "Can và Be able to",
    "Can: khả năng hiện tại, xin phép. Be able to: dùng được mọi thì (was able to, will be able to, have been able to). Was able to = managed to (thành công làm trong quá khứ). Could = khả năng chung; was able to = thành công một lần.",
    tbl(["Can", "Be able to"], [
        ["Hiện tại: I can swim.", "Mọi thì: He will be able to come. She has been able to work."],
        ["Could = khả năng chung quá khứ", "Was/were able to = thành công trong tình huống cụ thể: I was able to fix it."]
    ]),
    tbl(["Ví dụ"], [
        ["I couldn't sleep last night. (khả năng)"],
        ["I was able to get tickets. (thành công mua được vé)"]
    ]),
    ["Could không dùng cho thành công một lần trong quá khứ (He could leave yesterday → sai; He was able to leave.).", "Be able to dùng khi can không có (future, perfect, infinitive: would like to be able to)."],
    "Can (present). Be able to (all tenses). Was able to = succeeded.")

add("request-offer-invitation", "Yêu cầu, Đề nghị, Lời mời",
    "Request: Could you...? Would you mind...? Offer: Shall I...? Would you like me to...? I can... if you like. Invitation: Would you like to...? Do you want to...? How about...? Accept: Yes, please. I'd love to. Decline: I'd love to but... I'm afraid I can't.",
    tbl(["Loại", "Cách nói", "Ví dụ"], [
        ["Yêu cầu", "Could you open the window? Would you mind...?", "Could you pass the salt?"],
        ["Đề nghị", "Shall I help you? I can do it for you.", "Would you like me to call back?"],
        ["Lời mời", "Would you like to come? How about dinner?", "Would you like some coffee?"]
    ]),
    tbl(["Đáp"], [
        ["— Would you like tea? — Yes, please. / No, thank you."],
        ["— Shall I wait? — Yes, please. / No, it's OK."]
    ]),
    ["Would you like + N (mời dùng gì). Would you like to + V (mời làm gì).", "Shall I/we...? = đề nghị làm (cho mình/cho nhau)."],
    "Could you...? Shall I...? Would you like to...?")

add("asking-clarification", "Hỏi lại và Làm rõ",
    "Khi không nghe rõ: Sorry? Pardon? Could you repeat that? What did you say? Khi không hiểu: What do you mean? Could you explain? I don't get it. Can you give me an example? Làm rõ ý: I mean... What I mean is... In other words,...",
    tbl(["Tình huống", "Cách nói"], [
        ["Không nghe rõ", "Sorry? Pardon (me)? Could you say that again? I didn't catch that."],
        ["Không hiểu", "What do you mean (by...)? Could you explain? I'm not sure I follow."],
        ["Làm rõ ý mình", "I mean... What I mean is... To put it another way,..."]
    ]),
    tbl(["Ví dụ"], [
        ["— We need to leverage it. — What do you mean by 'leverage'?"],
        ["I mean we should use it to our advantage."]
    ]),
    ["Pardon? (Anh-Anh). Sorry? (thân mật).", "Could you run that by me again? (informal)."],
    "Sorry? What do you mean? I mean...")

add("expressing-surprise-interest", "Bày tỏ ngạc nhiên và Quan tâm",
    "Ngạc nhiên: Really? Wow! I can't believe it! That's amazing! No way! Are you serious? Quan tâm: That's interesting. Tell me more. I see. Oh, I didn't know that. Showing you're listening: I see. Right. Uh-huh. Go on.",
    tbl(["Ngạc nhiên", "Quan tâm / Đang nghe"], [
        ["Really? That's amazing! No way!", "That's interesting. Tell me more. I see."],
        ["I can't believe it! Are you serious?", "Right. Uh-huh. Go on. What happened then?"]
    ]),
    tbl(["Ví dụ"], [
        ["— I won the lottery. — No way! Really?"],
        ["— So then he left. — Oh, I see. What did you do?"]
    ]),
    ["No way = không thể nào (ngạc nhiên hoặc từ chối).", "I see = tôi hiểu (đang lắng nghe)."],
    "Really? No way! That's interesting. Tell me more.")

add("prepositions-movement", "Giới từ chỉ chuyển động",
    "To: đến (đích). Into: vào trong. Out of: ra khỏi. Onto: lên trên. Off: xuống khỏi. Through: xuyên qua. Across: băng qua (bề mặt). Along: dọc theo. Towards: về phía. Up/Down: lên/xuống.",
    tbl(["Giới từ", "Nghĩa", "Ví dụ"], [
        ["to", "Đến", "Go to the station. Come to my house."],
        ["into", "Vào trong", "Go into the room. Get into the car."],
        ["out of", "Ra khỏi", "Get out of the car. Take it out of the box."],
        ["through", "Xuyên qua", "Walk through the park. Drive through the tunnel."],
        ["across", "Băng qua", "Walk across the street. Swim across the river."]
    ]),
    tbl(["Ví dụ"], [
        ["She ran towards me. He climbed up the stairs. The ball rolled down the hill."]
    ]),
    ["Into = movement inside. In = position inside.", "Onto = lên trên bề mặt. On = vị trí trên."],
    "To, into, out of, through, across, along, towards.")

add("prepositions-other-common", "Một số giới từ thường gặp khác",
    "By: bởi (bị động); trước (by Monday); bằng phương tiện (by car). With: với (cùng, bằng công cụ). Without: không có. About: về. For: cho; trong (for 2 hours). Of: của. From: từ. Between: giữa 2. Among: giữa nhiều.",
    tbl(["Giới từ", "Nghĩa / Dùng với", "Ví dụ"], [
        ["by", "Bởi (passive); trước (time); bằng (transport)", "Made by hand. By 5pm. Travel by train."],
        ["with", "Với; bằng (tool)", "I live with my family. Cut with a knife."],
        ["without", "Không có", "I can't do it without you. Coffee without sugar."],
        ["between", "Giữa 2", "Between you and me. Between 9 and 10."],
        ["among", "Giữa nhiều", "Among the students. Choose among the options."]
    ]),
    tbl(["Ví dụ"], [
        ["The book was written by him. We need it by Friday."],
        ["It's between the bank and the post office."]
    ]),
    ["Between + 2. Among + 3 or more.", "By + time = trước (hoàn thành trước thời điểm)."],
    "By, with, without, about, for, between, among.")

add("adjectives-order", "Thứ tự tính từ - Order of Adjectives",
    "Thứ tự thường gặp: Opinion (đẹp) → Size → Age → Shape → Color → Origin → Material → Purpose + Noun. Ví dụ: a beautiful small old round red Italian leather handbag. Trong thực tế ít khi dùng quá 3–4 tính từ.",
    tbl(["Thứ tự", "Loại", "Ví dụ"], [
        ["1", "Opinion", "beautiful, ugly, nice"],
        ["2", "Size", "big, small, long"],
        ["3", "Age", "old, new, young"],
        ["4", "Shape", "round, square"],
        ["5", "Color", "red, blue"],
        ["6", "Origin", "Vietnamese, Italian"],
        ["7", "Material", "wooden, leather"],
        ["8", "Purpose", "racing (car), sleeping (bag)"]
    ]),
    tbl(["Ví dụ"], [
        ["a nice big old house. a small red plastic bag."],
        ["an expensive Italian leather jacket."]
    ]),
    ["Ghi nhớ: OSAShCOMP (Opinion, Size, Age, Shape, color, Origin, Material, Purpose).", "Thực tế: 2–3 tính từ là đủ."],
    "Opinion → Size → Age → Shape → Color → Origin → Material.")

add("adverbs-frequency-position", "Trạng từ tần suất - Vị trí chi tiết",
    "Always, usually, often, sometimes, rarely, seldom, never. Vị trí: sau be (am/is/are/was/were); trước động từ thường; giữa trợ ĐT và động từ chính (have always been). Đặt đầu câu để nhấn mạnh: Sometimes I eat out. Never have I seen... (đảo ngữ).",
    tbl(["Vị trí", "Ví dụ"], [
        ["Sau be", "She is always late. He was never happy there."],
        ["Trước V thường", "I always go to bed early. She never lies."],
        ["Sau trợ ĐT (have, will, can...)", "I have always wanted to go. She will never forget."],
        ["Đầu câu (nhấn mạnh)", "Sometimes I skip breakfast. Often we meet on Fridays."]
    ]),
    tbl(["Ví dụ"], [
        ["He doesn't always agree. (sau trợ ĐT phủ định)"],
        ["Rarely do I eat fast food. (đảo ngữ)"]
    ]),
    ["100%: always. 0%: never. Giữa: usually, often, sometimes, rarely.", "Seldom, rarely, never đứng đầu câu → đảo ngữ (Rarely did he complain)."],
    "After be. Before main V. Between aux and V. Never/Rarely at start → inversion.")

add("still-already-yet-revision", "Still, Already, Yet - Ôn và mở rộng",
    "Already: đã (khẳng định; có thể đặt cuối câu: I've done it already). Yet: chưa (phủ định, câu hỏi; cuối câu). Still: vẫn (đang tiếp tục). Still trong câu phủ định = vẫn chưa (hơi bực). Any more: không còn nữa.",
    tbl(["Từ", "Vị trí", "Ví dụ"], [
        ["already", "Giữa have/has và V3; hoặc cuối", "I've already eaten. She's left already."],
        ["yet", "Cuối câu (phủ định, hỏi)", "Have you finished yet? Not yet."],
        ["still", "Sau be; trước V thường", "I'm still waiting. She still works here."]
    ]),
    tbl(["Ví dụ"], [
        ["He still hasn't called. (vẫn chưa gọi – bực)"],
        ["I don't live there any more. (không còn sống ở đó)"]
    ]),
    ["Already trong câu hỏi: ngạc nhiên (You've finished already?).", "Yet chỉ dùng trong phủ định và nghi vấn (chưa)."],
    "Already (done). Yet (not yet). Still (continuing). Any more (no longer).")

add("even-if-even-though", "Even if và Even though",
    "Even though: mặc dù (sự thật đã biết). Even if: ngay cả khi (giả định, có thể không đúng). Even though it's expensive, I'll buy it. (Nó đắt – sự thật.) Even if it's expensive, I'll buy it. (Giả sử nó đắt – có thể không.)",
    tbl(["Cấu trúc", "Nghĩa", "Ví dụ"], [
        ["even though", "Mặc dù (thực tế)", "Even though it was raining, we went out. (Trời đang mưa.)"],
        ["even if", "Ngay cả khi (giả định)", "Even if it rains, we'll go. (Giả sử trời mưa.)"]
    ]),
    tbl(["Ví dụ"], [
        ["I'll help you even if you don't ask. (ngay cả khi bạn không nhờ)"],
        ["Even though he tried hard, he failed. (anh ấy đã cố – sự thật)"]
    ]),
    ["Even though = although (stronger). Even if = whether or not.", "Even if có thể là điều kiện chưa xảy ra hoặc không chắc."],
    "Even though = fact. Even if = hypothesis.")

add("whether-if", "Whether và If - Phân biệt",
    "If: điều kiện (If it rains...) hoặc có thể (I don't know if he will come). Whether: sau động từ (know, wonder, ask, decide) khi có 2 lựa chọn; sau giới từ; trước to V. I don't know whether/if he's coming. We discussed whether to go. (sau discuss dùng whether).",
    tbl(["Dùng whether", "Dùng if"], [
        ["Sau discuss, depend on", "We discussed whether to leave. It depends on whether he agrees."],
        ["Trước to V", "I don't know whether to go or stay."],
        ["Sau giới từ", "It's a question of whether we can afford it."],
        ["Điều kiện", "I'll go if you go. If it rains, I'll stay."]
    ]),
    tbl(["Ví dụ"], [
        ["Tell me whether (or not) you're coming. (whether thường dùng với or not)"],
        ["I wonder if/whether she knows. (cả hai được)"]
    ]),
    ["Whether or not = có... hay không. If không dùng sau giới từ.", "Sau know, wonder, ask: if và whether đều được."],
    "Whether: after discuss, depend, preposition, before to V. If: condition.")

add("unless-as-long-as-provided", "Unless, As long as, Provided that",
    "Unless = if not: trừ khi. Unless you hurry, you'll be late. = If you don't hurry, you'll be late. As long as / So long as / Providing (that) / Provided (that): miễn là (điều kiện). I'll come as long as you invite me.",
    tbl(["Từ", "Nghĩa", "Ví dụ"], [
        ["unless", "Trừ khi (= if not)", "Unless you apologize, I won't talk to you."],
        ["as long as", "Miễn là", "You can stay as long as you're quiet."],
        ["provided (that)", "Miễn là (formal)", "You can go provided (that) you finish the work."]
    ]),
    tbl(["Ví dụ"], [
        ["Unless it rains, we'll have a picnic. (If it doesn't rain...)"],
        ["I'll help you as long as you tell the truth."]
    ]),
    ["Unless + positive verb = if + negative. (Unless you go = If you don't go.)", "As long as = on condition that."],
    "Unless = if not. As long as = provided that = miễn là.")

add("despite-although-though", "Despite, Although, Though - So sánh",
    "Although / Though + clause (S + V). Despite / In spite of + N / V-ing (không phải clause). Though có thể đứng cuối câu (informal): It was hard. I did it, though. Even though nhấn mạnh hơn although.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["Although/Though + S + V", "Although it was cold, we went out. Though I tried, I failed."],
        ["Despite/In spite of + N/V-ing", "Despite the cold, we went out. In spite of feeling tired, she continued."],
        ["Though (cuối câu)", "It's expensive. I'll buy it, though."]
    ]),
    tbl(["Ví dụ"], [
        ["Even though he's rich, he's not happy. (nhấn mạnh)"],
        ["Despite having no experience, she got the job."]
    ]),
    ["Though = although (informal hơn).", "Despite the fact that + clause = Although (formal)."],
    "Although + clause. Despite + N/V-ing. Though at end = however.")

add("so-and-so-that", "So...that và Such...that - Ôn",
    "So + adj/adv + that. Such + (a/an) + adj + N + that. So many/few + N (plural) + that. So much/little + N (uncountable) + that. Such a lot of + N. It was so cold that we stayed in. It was such a cold day that we stayed in.",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["so + adj/adv + that", "She was so tired that she fell asleep."],
        ["such (a/an) + adj + N + that", "It was such a nice day that we went out."],
        ["so many/few + N (plural)", "There were so many people that we couldn't move."],
        ["so much/little + N (U)", "There was so little time that we had to run."]
    ]),
    tbl(["Ví dụ"], [
        ["He spoke so quickly that I couldn't understand."],
        ["She's such a good teacher that everyone likes her."]
    ]),
    ["So + adj (không có N). Such + (a/an) + adj + N.", "So many/much + N. Such a lot of + N."],
    "So + adj/adv. Such + (a/an) + adj + N. So many/much.")

add("comparison-as-as-than", "So sánh - As...as và Than",
    "As + adj/adv + as: bằng. Not as/so...as: không bằng. So sánh hơn: adj-er + than / more + adj + than. So sánh nhất: the + adj-est / the most + adj. So sánh kép: The more..., the more... As much/many + N + as.",
    tbl(["Loại", "Công thức", "Ví dụ"], [
        ["So sánh bằng", "as + adj/adv + as", "She's as tall as me. He runs as fast as you."],
        ["So sánh hơn", "adj-er than / more adj than", "She's taller than me. More expensive than..."],
        ["So sánh nhất", "the + adj-est / the most + adj", "She's the tallest. The most expensive."],
        ["So sánh kép", "The more..., the more...", "The more you practice, the better you get."]
    ]),
    tbl(["Ví dụ"], [
        ["This is not as good as that. I have as many books as you."],
        ["The sooner, the better."]
    ]),
    ["Sau than: me (informal) hoặc I (formal: She's taller than I am).", "As...as dùng trong so sánh bằng; than dùng trong so sánh hơn."],
    "As...as. -er/more + than. The -est / the most.")

add("noun-countable-uncountable-detail", "Danh từ đếm được và không đếm được - Chi tiết",
    "Đếm được: a book, two books; dùng many, few, a number of. Không đếm được: water, rice, information; không dùng a/an; dùng much, little, amount of. Một số vừa đếm được vừa không: coffee (uncountable) vs a coffee (cốc cà phê). Hair (tóc) thường U; a hair = sợi tóc.",
    tbl(["Đếm được", "Không đếm được"], [
        ["a book, an apple, many books, few ideas", "water, rice, information, advice, furniture"],
        ["How many? A number of.", "How much? An amount of. A piece of advice."],
        ["Chicken (con gà) C. A chicken.", "Chicken (thịt gà) U. Some chicken."]
    ]),
    tbl(["Ví dụ"], [
        ["I need some information. (không informations)"],
        ["I'd like a coffee. (= a cup of coffee)"]
    ]),
    ["Advice, information, furniture, news: không đếm được (không có -s).", "A piece of advice, a piece of information, a piece of furniture."],
    "Countable: a/an, many, few. Uncountable: no a/an, much, little.")

add("compound-nouns", "Danh từ ghép - Compound Nouns",
    "Danh từ ghép = 2+ từ tạo thành 1 danh từ. Có thể: N+N (toothbrush, football), Adj+N (blackboard), V-ing+N (swimming pool), N+V-ing (sunrise). Số nhiều thường thêm -s vào từ chính: toothbrushes, not teethbrush. Một số có dấu gạch nối: mother-in-law → mothers-in-law.",
    tbl(["Dạng", "Ví dụ"], [
        ["N + N", "toothbrush, football, bedroom, smartphone"],
        ["Adj + N", "blackboard, greenhouse, software"],
        ["V-ing + N", "swimming pool, washing machine, dining room"],
        ["N + V-ing", "sunrise, haircut, bookkeeping"]
    ]),
    tbl(["Số nhiều"], [
        ["toothbrushes (từ chính: brush). Passers-by (passer-by). Mothers-in-law."]
    ]),
    ["Stress thường ở từ đầu: 'blackboard, 'swimming pool.", "Một số viết liền, một số có gạch nối (check dictionary)."],
    "N+N, Adj+N, V-ing+N. Plural on main noun.")

add("prefixes-negative", "Tiền tố phủ định - Negative Prefixes",
    "Un-: unhappy, unable, unfair. In-: incorrect, invisible (trước không phải l, r). Im-: impossible, immature (trước p, m). Il-: illegal (trước l). Ir-: irregular, irresponsible (trước r). Dis-: disagree, disappear. Non-: non-stop, non-fiction.",
    tbl(["Tiền tố", "Thường trước", "Ví dụ"], [
        ["un-", "adj, một số V", "unhappy, unlock, untrue"],
        ["in-", "adj (không l, r)", "incorrect, invisible, informal"],
        ["im-", "p, m", "impossible, immature, impolite"],
        ["il-", "l", "illegal, illogical"],
        ["ir-", "r", "irregular, irresponsible"],
        ["dis-", "V, adj", "disagree, disappear, dishonest"]
    ]),
    tbl(["Ví dụ"], [
        ["In- không dùng trước l, r: illegal, irregular."],
        ["Un- phổ biến: unkind, unlock, unhappy."]
    ]),
    ["Một số từ không theo quy tắc: informal, impatient (im-).", "Tra từ điển khi không chắc."],
    "Un-, In-, Im-, Il-, Ir-, Dis-. In- not before l, r.")

add("suffixes-verb-noun", "Hậu tố tạo động từ và danh từ",
    "V → N: -tion (action), -sion (decision), -ment (development), -er (teacher), -ation (information). Adj → N: -ness (happiness), -ity (ability). N/Adj → V: -ize (modernize), -en (widen, strengthen), -ify (simplify).",
    tbl(["Từ gốc", "Hậu tố", "Kết quả"], [
        ["act", "-tion", "action"], ["decide", "-sion", "decision"],
        ["develop", "-ment", "development"], ["happy", "-ness", "happiness"],
        ["modern", "-ize", "modernize"], ["wide", "-en", "widen"]
    ]),
    tbl(["Ví dụ"], [
        ["Simple → simplify. Clear → clarify. Identity → identify."],
        ["Strong → strengthen. Weak → weaken."]
    ]),
    ["-tion sau V (invent → invention). -ness sau adj (kind → kindness).", "-ize (Anh-Mỹ), -ise (Anh-Anh): organize/organise."],
    "-tion, -ment, -ness. -ize, -en, -ify.")

add("writing-formal-email", "Viết email trang trọng",
    "Mở đầu: Dear Mr/Ms/Mrs + surname. Lý do viết: I am writing to... / I would like to inquire about... Nội dung: đoạn ngắn, rõ ràng. Kết thúc: I look forward to hearing from you. Yours sincerely (khi biết tên) / Yours faithfully (khi không biết). Sign off: Best regards, [Name].",
    tbl(["Phần", "Cách viết"], [
        ["Mở đầu", "Dear Mr Smith, / Dear Sir or Madam,"],
        ["Lý do", "I am writing to inquire about... / I am writing in response to..."],
        ["Nội dung", "Đoạn ngắn, câu đầy đủ. Please find attached... Could you please...?"],
        ["Kết", "I look forward to your reply. Please do not hesitate to contact me if..."],
        ["Ký", "Yours sincerely, (biết tên) / Yours faithfully, (không biết)"]
    ]),
    tbl(["Ví dụ"], [
        ["Dear Mr Brown, I am writing to apply for the position of... I look forward to hearing from you. Yours sincerely, John Smith."]
    ]),
    ["Tránh viết tắt (I'm → I am). Tránh từ quá thân mật.", "Yours sincerely khi bắt đầu Dear Mr X. Yours faithfully khi Dear Sir/Madam."],
    "Dear... I am writing to... Yours sincerely/faithfully.")

add("writing-informal-email", "Viết email thân mật",
    "Mở đầu: Hi [Name], Hello, Hey. Thân mật: Thanks for... Just wanted to... I'm writing to... Kết: See you soon. Take care. Bye. Best, [Name]. Có thể dùng viết tắt (I'm, don't, we'll). Câu ngắn, thoải mái.",
    tbl(["Phần", "Cách viết"], [
        ["Mở đầu", "Hi John, Hello! Hey there,"],
        ["Nội dung", "Thanks for your email. Just wanted to let you know... I'm writing because..."],
        ["Kết", "See you soon! Take care. Talk later. Bye! Best, / Cheers,"]
    ]),
    tbl(["Ví dụ"], [
        ["Hi Anna, Thanks for the invite! I'd love to come. See you on Saturday. Best, Mike."]
    ]),
    ["Viết tắt OK: I'm, we'll, don't. Emoji tùy người nhận.", "Cheers (Anh-Anh) = Thanks / Bye."],
    "Hi... Thanks for... See you. Best/Cheers.")

add("listening-tips", "Mẹo nghe hiểu",
    "Trước khi nghe: đọc câu hỏi, đoán chủ đề, từ khóa. Trong khi nghe: nghe từ khóa, không cố nghe từng từ, chấp nhận bỏ qua. Sau khi nghe: kiểm tra chính tả, số ít/số nhiều. Luyện: nghe nhiều lần, transcript, podcast, phim phụ đề.",
    tbl(["Giai đoạn", "Làm gì"], [
        ["Trước", "Đọc câu hỏi. Đoán chủ đề. Gạch chân từ khóa."],
        ["Trong", "Tập trung vào ý chính. Ghi chú số, tên. Không dừng lại khi miss."],
        ["Sau", "Kiểm tra chính tả. Số ít/số nhiều. Điền đủ từ theo yêu cầu."]
    ]),
    tbl(["Luyện tập"], [
        ["Nghe podcast, TED. Xem phim với phụ đề tiếng Anh. Nghe lại + đọc transcript."]
    ]),
    ["Keyword listening: không cần hiểu hết.", "Chấp nhận miss một phần, bắt kịp phần sau."],
    "Preview questions. Focus on key words. Check spelling.")

add("pronunciation-ed-ending", "Phát âm đuôi -ed (V-ed)",
    "Đuôi -ed phát âm: /t/ khi động từ tận cùng âm vô thanh (p, k, f, s, sh, ch, x): looked, stopped. /d/ khi tận cùng âm hữu thanh (còn lại): played, lived. /ɪd/ khi tận cùng /t/ hoặc /d/: wanted, needed.",
    tbl(["Phát âm", "Khi nào", "Ví dụ"], [
        ["/t/", "Âm cuối vô thanh (p, k, f, s, sh, ch)", "looked, stopped, missed, watched"],
        ["/d/", "Âm cuối hữu thanh", "played, lived, called, stayed"],
        ["/ɪd/", "Âm cuối /t/ hoặc /d/", "wanted, needed, started, decided"]
    ]),
    tbl(["Ví dụ"], [
        ["Walked /t/. Opened /d/. Waited /ɪd/."]
    ]),
    ["Âm vô thanh: không rung cổ họng (p, t, k, f, s, sh, ch).", "Hữu thanh: rung (b, d, g, v, z, m, n, l, r...)."],
    "-ed: /t/ (voiceless), /d/ (voiced), /ɪd/ (after t, d).")

add("pronunciation-s-es", "Phát âm đuôi -s/-es",
    "Số nhiều N và ngôi 3 số ít V: /s/ sau âm vô thanh (cats, works). /z/ sau âm hữu thanh (dogs, lives). /ɪz/ sau âm xuýt (s, z, sh, ch, ge): buses, watches, boxes.",
    tbl(["Phát âm", "Khi nào", "Ví dụ"], [
        ["/s/", "Sau âm vô thanh", "cats, books, works, stops"],
        ["/z/", "Sau âm hữu thanh", "dogs, days, lives, goes"],
        ["/ɪz/", "Sau s, z, sh, ch, ge, x", "buses, watches, boxes, bridges"]
    ]),
    tbl(["Ví dụ"], [
        ["Maps /s/. Bags /z/. Dishes /ɪz/. Watches /ɪz/."]
    ]),
    ["Thêm -es khi N/V tận cùng s, x, z, ch, sh: box → boxes.", "Phát âm /ɪz/ = thêm âm tiết."],
    "-s/-es: /s/ (voiceless), /z/ (voiced), /ɪz/ (after sibilant).")

add("extra-final-1", "Mở rộng 1 - Cụm từ hữu ích",
    "At the end of the day: cuối cùng thì. To be honest: thành thật mà nói. As a matter of fact: thực ra. To cut a long story short: nói tóm lại. Having said that: tuy vậy. To some extent: ở mức độ nào đó. In terms of: về mặt. It goes without saying: không cần nói.",
    tbl(["Cụm", "Nghĩa", "Ví dụ"], [
        ["at the end of the day", "Cuối cùng thì", "At the end of the day, it's your decision."],
        ["to be honest", "Thành thật mà nói", "To be honest, I didn't like it."],
        ["having said that", "Tuy vậy", "It's cheap. Having said that, the quality is poor."],
        ["in terms of", "Về mặt", "In terms of cost, it's good."]
    ]),
    tbl(["Ví dụ"], [
        ["To cut a long story short, we missed the flight."],
        ["It goes without saying that we need to prepare."]
    ]),
    ["Dùng để nối ý, chuyển ý trong nói và viết.", "To be honest, Having said that: rất thường gặp."],
    "At the end of the day. To be honest. In terms of. Having said that.")

add("extra-final-2", "Mở rộng 2 - Cấu trúc hữu ích",
    "It's (high) time + S + V2: đã đến lúc (nên làm). Would rather + S + V2: muốn ai đó làm (hiện tại). Would prefer + N + to V: thích ai đó làm. Had better + V: nên (cảnh báo). Would you mind + V-ing: bạn có phiền... I'd appreciate it if + S + V2: tôi biết ơn nếu...",
    tbl(["Cấu trúc", "Ví dụ"], [
        ["It's (high) time + S + V2", "It's time we left. It's high time you found a job."],
        ["Would rather + S + V2", "I'd rather you didn't tell anyone."],
        ["I'd appreciate it if", "I'd appreciate it if you could reply soon."],
        ["Would you mind + V-ing", "Would you mind closing the window?"]
    ]),
    tbl(["Ví dụ"], [
        ["It's high time you apologized. (đã đến lúc nên xin lỗi)"],
        ["I'd appreciate it if you could send the file today."]
    ]),
    ["It's time we left (lùi thì: left, không leave).", "Would you mind...? Đáp No = đồng ý (No, not at all.)."],
    "It's time S + V2. I'd appreciate it if. Would you mind V-ing?")

add("extra-final-3", "Ôn và Kết - 200 bài hoàn chỉnh",
    "Bạn đã học qua 200 chủ điểm: thì, câu điều kiện, bị động, modal, từ nối, mệnh đề quan hệ, phrasal verbs, idioms, giao tiếp, viết, đọc, phát âm, từ dễ nhầm. Tiếp tục ôn theo tab Học và luyện với tab Luyện tập. Practice makes perfect!",
    tbl(["Nhóm đã học", "Gợi ý"], [
        ["Ngữ pháp", "Ôn thì, câu điều kiện, bị động, modal, mệnh đề quan hệ."],
        ["Từ vựng & dùng từ", "Collocation, phrasal verbs, idioms, từ dễ nhầm."],
        ["Giao tiếp", "Chào hỏi, cảm ơn, xin lỗi, ý kiến, gợi ý, đồng ý/không đồng ý."],
        ["Kỹ năng", "Viết đoạn văn, email, skimming/scanning, nghe, phát âm -ed/-s."]
    ]),
    tbl(["Lời nhắn"], [
        ["Học đều đặn. Ôn lại định kỳ. Kết hợp đọc (Học) và làm bài (Luyện tập). Chúc bạn tiến bộ!"]
    ]),
    ["200 bài đầy đủ, rõ ràng. Tùy trình độ có thể học theo thứ tự hoặc chọn chủ đề.", "Tra từ điển và collocation khi cần. Luyện nghe nói song song với ngữ pháp."],
    "Review all. Practice. Consistency is key. Good luck!")

# ========== Bổ sung usageEn (dịch Cách dùng sang tiếng Anh) cho bài đã có usage ==========
USAGE_EN = {}
def set_usage_en(lesson_id, en_list):
    USAGE_EN[lesson_id] = en_list

# Thì & thể
set_usage_en("past-continuous", ["Action in progress at a point in the past.", "Action in progress when another interrupted (when/while).", "Two parallel actions in the past (while)."])
set_usage_en("past-perfect", ["Action completed before another past action.", "Action completed before a point in the past (by + time).", "In third conditional."])
set_usage_en("future-continuous", ["Action in progress at a point in the future.", "Planned or habitual future action."])
set_usage_en("present-perfect-continuous", ["Action from past to present (emphasis on duration).", "Action just finished, result still visible.", "Often with since, for."])
set_usage_en("conditional-type-0", ["State general truths and scientific facts.", "State habits and rules."])
set_usage_en("conditional-type-1", ["Real possibility in the future.", "Suggestion, warning, agreement.", "Unless = if not."])
set_usage_en("conditional-type-2", ["Unreal present or future (wish, hypothesis).", "Advice: If I were you, I would...", "Use 'were' for all persons in formal style."])
set_usage_en("conditional-type-3", ["Unreal past.", "Regret about what did not happen.", "Speculation about a different past result."])
set_usage_en("passive-present-simple", ["Emphasize the receiver of the action.", "When the doer is unknown or unnecessary."])
set_usage_en("passive-past-simple", ["Describe a completed passive action in the past."])
set_usage_en("passive-modal", ["Passive with ability, obligation, or advice."])
# Modals (1 item each)
for mid, en in [("can", "Present ability, permission, request."), ("could", "Past ability, polite request, conditional."), ("may", "Formal permission, uncertainty."), ("might", "Lower possibility than may."), ("must", "Obligation, strong necessity, certainty."), ("have-to", "External obligation (rules, circumstances)."), ("should", "Advice, suggestion, reasonable expectation."), ("ought-to", "Formal advice, moral duty."), ("would", "Past habit, polite offer, conditional."), ("used-to", "Past habit or state, no longer true.")]:
    set_usage_en(mid, [en])
# Cấu trúc khác
set_usage_en("comparative-superlative", ["Compare two: use comparative.", "Compare three or more: use superlative.", "Short adj: -er/-est. Long adj: more/most."])
set_usage_en("too-and-enough", ["Too: beyond desired level, often negative result.", "Enough: sufficient for something."])
set_usage_en("so-such", ["So + adj/adv.", "Such + (a/an) + adj + N."])
set_usage_en("used-to-be-used-to", ["Used to: past only, not present.", "Be/Get used to: followed by V-ing or N."])
set_usage_en("would-rather-had-better", ["Would rather: preference, choice.", "Had better: strong advice (warning)."])
set_usage_en("question-tags", ["Auxiliary in tag matches the tense.", "Tag subject is always a pronoun.", "Rising tone = real question; falling = expect agreement."])
set_usage_en("articles-a-an-the", ["A/An: first mention, indefinite.", "The: definite, listener knows what; unique things.", "No a/an with uncountable or plural."])
set_usage_en("prepositions-time", ["At: specific time (hour).", "On: day.", "In: longer period (month, year)."])
set_usage_en("prepositions-place", ["In: inside, within.", "On: surface.", "At: point or place."])
set_usage_en("some-any-no", ["Some: positive or offer.", "Any: negative or question.", "No + N = not any."])
set_usage_en("relative-clauses-who-which", ["Who/Which/That as subject cannot be omitted.", "That often replaces who/which in defining clauses.", "Whom: object (person); can be omitted."])
set_usage_en("gerund-vs-infinitive", ["V-ing: when verb is subject or after preposition.", "To V: purpose, after adjective, after certain verbs.", "Remember/Forget/Stop + V-ing (past) / to V (future)."])

for L in lessons:
    if L["id"] in USAGE_EN:
        L["usageEn"] = USAGE_EN[L["id"]]

# Đảm bảo đủ 200 bài (bổ sung ôn tập nếu thiếu)
while len(lessons) < 200:
    n = len(lessons) + 1
    lessons.append(lesson(
        "lesson", f"review-{n}",
        f"Ôn tập - Bài {n}",
        "Ôn lại các chủ điểm đã học: thì, câu điều kiện, bị động, modal, từ nối, mệnh đề quan hệ, phrasal verbs, giao tiếp, viết. Kết hợp tab Học và tab Luyện tập.",
        tbl(["Gợi ý"], [["Ôn lại bài trước. Làm bài tập trong tab Luyện tập."]]),
        tbl(["Ví dụ"], [["Practice makes perfect."]]),
        ["Ôn tập định kỳ giúp ghi nhớ lâu.", "Học đều đặn mỗi ngày."],
        "Review. Practice."
    ))

with open("learn_content.json", "w", encoding="utf-8") as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print(f"Generated {len(lessons)} lessons in learn_content.json")
