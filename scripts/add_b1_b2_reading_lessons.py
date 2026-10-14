# -*- coding: utf-8 -*-
"""
Script to create 15 comprehensive B1 - B2 English lessons (Conversations & Reading Passages)
with bilingual translations, key vocabularies (with IPA), and 4 multiple-choice questions
with detailed pedagogical explanations.
Merges with existing 21 lessons to provide a total of 36 rich lessons.
"""

import json
from pathlib import Path

NEW_B1_B2_LESSONS = [
    # ---------------- MODULE 22 ----------------
    {
        "id": "read-22",
        "title": "Job Interview: Strengths, Weaknesses, and Career Goals",
        "type": "conversation",
        "topic": "Công sở & Nghề nghiệp",
        "level": "B1 - B2",
        "summary": "Buổi phỏng vấn xin việc vị trí Chuyên viên Tiếp thị Kỹ thuật số giữa Giám đốc tuyển dụng và ứng viên tiềm năng.",
        "content": [
            { "speaker": "Alex (Male / Hiring Manager)", "text": "Good afternoon, Linh. Welcome to our office. Did you have any trouble finding our building today?" },
            { "speaker": "Linh (Female / Candidate)", "text": "Good afternoon, Mr. Alex. Not at all. Your directions were very clear, and the commute was quite pleasant." },
            { "speaker": "Alex (Male / Hiring Manager)", "text": "Wonderful. To begin, could you tell me a little bit about yourself and why you applied for this Digital Marketing Specialist position?" },
            { "speaker": "Linh (Female / Candidate)", "text": "Certainly. I have worked in social media marketing for over three years. In my previous role, I managed organic campaigns that increased our website traffic by thirty-five percent. I applied here because your company produces educational technology that truly empowers students." },
            { "speaker": "Alex (Male / Hiring Manager)", "text": "That is impressive. How do you handle unexpected deadlines or shifting priorities when multiple campaigns run concurrently?" },
            { "speaker": "Linh (Female / Candidate)", "text": "I prioritize tasks using a project management board. If urgent revisions arise, I communicate promptly with my teammates so we can redistribute workloads without missing critical milestones." },
            { "speaker": "Alex (Male / Hiring Manager)", "text": "Every professional has areas to improve. What would you consider your greatest professional weakness?" },
            { "speaker": "Linh (Female / Candidate)", "text": "In the past, I sometimes hesitated to delegate tasks because I wanted every detail to be perfect. However, I have learned that trusting capable colleagues produces better outcomes and fosters team growth." },
            { "speaker": "Alex (Male / Hiring Manager)", "text": "That shows great self-awareness. Do you have any questions for me regarding our team culture or expectations?" },
            { "speaker": "Linh (Female / Candidate)", "text": "Yes, thank you. Could you share what qualities distinguish the most successful marketers within your organization?" }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Alex (Nam / Trưởng phòng tuyển dụng):** Chào buổi chiều, Linh. Chào mừng bạn đến văn phòng của chúng tôi. Hôm nay bạn tìm đường đến tòa nhà có thuận lợi không?\n
- **Linh (Nữ / Ứng viên):** Chào buổi chiều, anh Alex. Rất thuận lợi ạ. Hướng dẫn chỉ đường của công ty rất rõ ràng và việc đi lại khá thoải mái.\n
- **Alex (Nam / Trưởng phòng tuyển dụng):** Tuyệt vời. Để bắt đầu, bạn có thể giới thiệu một chút về bản thân và lý do bạn ứng tuyển vào vị trí Chuyên viên Tiếp thị Kỹ thuật số này không?\n
- **Linh (Nữ / Ứng viên):** Dạ chắc chắn rồi ạ. Tôi đã làm việc trong lĩnh vực tiếp thị truyền thông xã hội hơn ba năm. Ở vị trí trước đây, tôi quản lý các chiến dịch tự nhiên giúp tăng lưu lượng truy cập trang web lên 35%. Tôi ứng tuyển vào đây vì công ty tạo ra các sản phẩm công nghệ giáo dục thực sự trao quyền cho học sinh.\n
- **Alex (Nam / Trưởng phòng tuyển dụng):** Rất ấn tượng. Bạn xử lý thế nào trước các hạn chót bất ngờ hoặc các mức độ ưu tiên thay đổi khi nhiều chiến dịch chạy đồng thời?\n
- **Linh (Nữ / Ứng viên):** Tôi sắp xếp thứ tự ưu tiên cho công việc bằng bảng quản lý dự án. Nếu có yêu cầu chỉnh sửa khẩn cấp, tôi trao đổi ngay với đồng đội để có thể phân bổ lại khối lượng công việc mà không trễ các cột mốc quan trọng.\n
- **Alex (Nam / Trưởng phòng tuyển dụng):** Bất kỳ chuyên gia nào cũng có điểm cần hoàn thiện. Bạn coi điểm yếu lớn nhất trong công việc của mình là gì?\n
- **Linh (Nữ / Ứng viên):** Trước đây, tôi đôi khi ngần ngại giao việc cho người khác vì muốn mọi chi tiết đều phải hoàn hảo. Tuy nhiên, tôi đã học được rằng việc tin tưởng các đồng nghiệp có năng lực sẽ mang lại kết quả tốt hơn và thúc đẩy sự phát triển của cả nhóm.\n
- **Alex (Nam / Trưởng phòng tuyển dụng):** Điều đó cho thấy khả năng tự nhận thức rất tốt. Bạn có câu hỏi nào dành cho tôi về văn hóa đội ngũ hoặc các kỳ vọng không?\n
- **Linh (Nữ / Ứng viên):** Dạ có ạ, cảm ơn anh. Anh có thể chia sẻ những phẩm chất nào tạo nên sự khác biệt của những chuyên viên tiếp thị thành công nhất trong tổ chức của mình không ạ?""",
        "keyVocab": [
            { "word": "commute", "ipa": "/kəˈmjuːt/", "meaning": "quãng đường đi lại giữa nhà và nơi làm việc" },
            { "word": "concurrently", "ipa": "/kənˈkɝː.ənt.li/", "meaning": "đồng thời, cùng một lúc" },
            { "word": "prioritize", "ipa": "/praɪˈɔːr.ə.taɪz/", "meaning": "sắp xếp thứ tự ưu tiên" },
            { "word": "delegate", "ipa": "/ˈdel.ə.ɡeɪt/", "meaning": "ủy quyền, giao phó trách nhiệm" },
            { "word": "self-awareness", "ipa": "/ˌself.əˈwer.nəs/", "meaning": "sự tự nhận thức, hiểu rõ bản thân" }
        ],
        "questions": [
            {
                "id": "q-22-1",
                "question": "What notable achievement did Linh mention from her previous marketing role?",
                "options": [
                    "A. She reduced the advertising budget by fifty percent.",
                    "B. She increased website traffic by thirty-five percent through organic campaigns.",
                    "C. She authored a bestselling book about consumer psychology.",
                    "D. She completely redesigned the company's mobile application."
                ],
                "answerIndex": 1,
                "explanation": "Linh nêu rõ: 'I managed organic campaigns that increased our website traffic by thirty-five percent' (Tôi quản lý các chiến dịch tự nhiên giúp tăng lưu lượng truy cập web 35%)."
            },
            {
                "id": "q-22-2",
                "question": "How does Linh handle unexpected deadlines and shifting priorities?",
                "options": [
                    "A. By turning off her phone until all tasks are finished.",
                    "B. By requesting an immediate salary raise from management.",
                    "C. By prioritizing tasks on a project board and communicating promptly with teammates.",
                    "D. By postponing difficult tasks until the following month."
                ],
                "answerIndex": 2,
                "explanation": "Linh chia sẻ: 'I prioritize tasks using a project management board... communicate promptly with my teammates so we can redistribute workloads'."
            },
            {
                "id": "q-22-3",
                "question": "What weakness did Linh acknowledge, and what did she learn from it?",
                "options": [
                    "A. She struggled with speaking English in international meetings.",
                    "B. She was frequently late to client appointments.",
                    "C. She hesitated to delegate tasks, but learned that trusting colleagues yields better outcomes.",
                    "D. She refused to use modern computer software."
                ],
                "answerIndex": 2,
                "explanation": "Linh thừa nhận: 'I sometimes hesitated to delegate tasks... learned that trusting capable colleagues produces better outcomes'."
            },
            {
                "id": "q-22-4",
                "question": "What does Linh ask Alex at the end of the interview?",
                "options": [
                    "A. What qualities distinguish successful marketers in the company.",
                    "B. The exact date of the next annual company party.",
                    "C. How much bonus she will receive during the holidays.",
                    "D. Whether the office offers free parking for all employees."
                ],
                "answerIndex": 0,
                "explanation": "Linh hỏi: 'Could you share what qualities distinguish the most successful marketers within your organization?'"
            }
        ]
    },

    # ---------------- MODULE 23 ----------------
    {
        "id": "read-23",
        "title": "The Art of Mindful Eating and Healthy Habits",
        "type": "passage",
        "topic": "Sức khỏe & Lối sống",
        "level": "B1 - B2",
        "summary": "Bài đọc khám phá phương pháp ăn uống chánh niệm, tác hại của việc ăn vội trước màn hình và cách xây dựng mối quan hệ lành mạnh với thực phẩm.",
        "content": """In modern society, busy schedules and digital distractions have fundamentally changed the way we consume food. Many working adults eat their meals in front of computer monitors or while scrolling through social media notifications on their smartphones. Consequently, people frequently swallow large meals in less than ten minutes without truly tasting their food or paying attention to physiological signals of fullness. Nutritionists refer to this pattern as absent-minded consumption, which often leads to overeating and digestive discomfort.\n\nMindful eating offers a refreshing antidote to this chaotic habit. Rooted in mindfulness practices, it encourages individuals to engage all five senses during mealtime. When practicing mindful eating, you begin by observing the vivid colors and pleasant aromas of the ingredients before taking your first bite. Chewing slowly allows digestive enzymes in saliva to break down nutrients effectively, while giving the brain sufficient time—typically twenty minutes—to register satiety hormones released by the stomach.\n\nFurthermore, developing a mindful approach to eating helps people distinguish between emotional hunger and physical hunger. Emotional hunger strikes suddenly, demanding immediate satisfaction through high-sugar or ultra-processed comfort foods during moments of stress or boredom. In contrast, genuine physical hunger develops gradually and can be satisfied by a diverse variety of nourishing whole foods. Recognizing this difference prevents guilt and empowers individuals to cultivate a sustainable, positive relationship with nutrition.\n\nAdopting mindful eating does not require strict dietary restrictions or counting every calorie. Simple lifestyle adjustments, such as sitting down at a proper dining table, putting down utensils between mouthfuls, and savoring the unique flavors of home-cooked meals, can dramatically enhance digestion and emotional well-being. By treating each meal as an intentional pause rather than a chore, we reconnect with the nourishing power of wholesome food.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Trong xã hội hiện đại, lịch trình bận rộn và những xao nhãng kỹ thuật số đã thay đổi căn bản cách chúng ta ăn uống. Nhiều người trưởng thành đi làm thường ăn cơm trước màn hình máy tính hoặc trong khi lướt thông báo mạng xã hội trên điện thoại thông minh. Do đó, mọi người thường nuốt chửng những bữa ăn lớn chỉ trong chưa đầy mười phút mà không thực sự nếm trải hương vị thức ăn hay chú ý đến các tín hiệu sinh lý báo hiệu đã no. Các chuyên gia dinh dưỡng gọi kiểu ăn uống này là tiêu thụ thiếu chú tâm, điều thường dẫn đến việc ăn quá no và khó chịu về tiêu hóa.\n\nĂn uống chánh niệm mang lại một liều thuốc giải sảng khoái cho thói quen hỗn loạn này. Có nguồn gốc từ các bài thực hành chánh niệm, phương pháp này khuyến khích mỗi cá nhân vận dụng cả năm giác quan trong bữa ăn. Khi thực hành ăn uống chánh niệm, bạn bắt đầu bằng việc quan sát màu sắc sống động và mùi thơm dễ chịu của các nguyên liệu trước khi cắn miếng đầu tiên. Việc nhai chậm cho phép các enzyme tiêu hóa trong nước bọt phân giải chất dinh dưỡng hiệu quả, đồng thời cho não bộ đủ thời gian—thường là khoảng hai mươi phút—để tiếp nhận các hormone báo no do dạ dày giải phóng.\n\nHơn nữa, việc phát triển cách tiếp cận chánh niệm đối với ăn uống giúp con người phân biệt được giữa đói cảm xúc và đói thể chất. Cơn đói cảm xúc ập đến bất ngờ, đòi hỏi sự thỏa mãn tức thì thông qua các món ăn nhiều đường hoặc thực phẩm chế biến sẵn để giải tỏa trong những lúc căng thẳng hoặc buồn chán. Ngược lại, cơn đói thể chất thực sự phát triển dần dần và có thể được thỏa mãn bởi nhiều loại thực phẩm nguyên phần bổ dưỡng. Nhận biết được sự khác biệt này giúp ngăn ngừa cảm giác tội lỗi và trao quyền cho mỗi người xây dựng một mối quan hệ tích cực, bền vững với dinh dưỡng.\n\nÁp dụng ăn uống chánh niệm không đòi hỏi chế độ ăn kiêng nghiêm ngặt hay phải đếm từng calo. Những điều chỉnh lối sống đơn giản, chẳng hạn như ngồi vào bàn ăn đàng hoàng, đặt thìa dĩa xuống giữa các lần nhai và thưởng thức trọn vẹn hương vị độc đáo của những bữa cơm nhà nấu, có thể cải thiện đáng kể hệ tiêu hóa và sức khỏe tinh thần. Bằng cách coi mỗi bữa ăn như một khoảng dừng có chủ đích thay vì một việc vặt, chúng ta kết nối lại với sức mạnh nuôi dưỡng của thực phẩm lành mạnh.""",
        "keyVocab": [
            { "word": "distraction", "ipa": "/dɪˈstræk.ʃən/", "meaning": "sự xao nhãng, mất tập trung" },
            { "word": "antidote", "ipa": "/ˈæn.t̬i.doʊt/", "meaning": "liều thuốc giải, giải pháp khắc phục" },
            { "word": "satiety", "ipa": "/səˈtaɪ.ə.t̬i/", "meaning": "cảm giác no bụng, thỏa mãn" },
            { "word": "emotional hunger", "ipa": "/ɪˈmoʊ.ʃən.əl ˈhʌŋ.ɡɚ/", "meaning": "cơn đói do cảm xúc (buồn, stress) gây ra" },
            { "word": "sustainable", "ipa": "/səˈsteɪ.nə.bəl/", "meaning": "bền vững, duy trì lâu dài" }
        ],
        "questions": [
            {
                "id": "q-23-1",
                "question": "What common modern behavior often leads to absent-minded overeating?",
                "options": [
                    "A. Eating fresh fruits during morning workouts.",
                    "B. Consuming meals quickly in front of screens while scrolling on phones.",
                    "C. Cooking detailed family recipes every Sunday afternoon.",
                    "D. Drinking warm tea before going to bed."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu rõ: 'Many working adults eat their meals in front of computer monitors or while scrolling through social media notifications... leads to overeating'."
            },
            {
                "id": "q-23-2",
                "question": "Approximately how long does it take for the brain to register fullness hormones from the stomach?",
                "options": [
                    "A. Two minutes.",
                    "B. Twenty minutes.",
                    "C. One hour.",
                    "D. Five seconds."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 giải thích: 'giving the brain sufficient time—typically twenty minutes—to register satiety hormones released by the stomach'."
            },
            {
                "id": "q-23-3",
                "question": "How does emotional hunger differ from physical hunger according to the text?",
                "options": [
                    "A. Emotional hunger happens only late at night after heavy exercise.",
                    "B. Emotional hunger appears suddenly and craves sugary comfort foods, whereas physical hunger develops gradually.",
                    "C. Emotional hunger can only be cured by prescription medicine.",
                    "D. Physical hunger makes people crave fast food exclusively."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 phân tích: 'Emotional hunger strikes suddenly, demanding immediate satisfaction through high-sugar... physical hunger develops gradually'."
            },
            {
                "id": "q-23-4",
                "question": "What is one simple practical tip recommended for practicing mindful eating?",
                "options": [
                    "A. Skipping dinner twice a week.",
                    "B. Counting calories on a digital spreadsheet.",
                    "C. Putting down utensils between bites and sitting at a dining table without distractions.",
                    "D. Eating all meals standing up in the kitchen."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 4 gợi ý: 'sitting down at a proper dining table, putting down utensils between mouthfuls, and savoring the unique flavors'."
            }
        ]
    },

    # ---------------- MODULE 24 ----------------
    {
        "id": "read-24",
        "title": "Hotel Check-In & Requesting Room Amenities",
        "type": "conversation",
        "topic": "Du lịch & Khách sạn",
        "level": "B1 - B2",
        "summary": "Cuộc đối thoại tại quầy lễ tân khách sạn khi khách làm thủ tục nhận phòng, yêu cầu phòng tầng cao yên tĩnh và tìm hiểu dịch vụ xe đưa đón.",
        "content": [
            { "speaker": "Marcus (Male / Front Desk)", "text": "Good evening! Welcome to the Grand Horizon Hotel. How may I assist you this evening?" },
            { "speaker": "Emma (Female / Guest)", "text": "Good evening. I have a reservation under the name Emma Watson for three nights." },
            { "speaker": "Marcus (Male / Front Desk)", "text": "Thank you, Ms. Watson. Let me pull up your booking in our reservation system. Yes, here it is: a Deluxe King room with city views, including daily breakfast." },
            { "speaker": "Emma (Female / Guest)", "text": "That is correct. If possible, could I request a room on a higher floor away from the elevator? I am a light sleeper and have an early conference tomorrow." },
            { "speaker": "Marcus (Male / Front Desk)", "text": "Certainly! We have a quiet corner room available on the fourteenth floor that faces the internal courtyard. It should ensure an uninterrupted night of rest." },
            { "speaker": "Emma (Female / Guest)", "text": "That sounds perfect! What time is breakfast served in the morning, and where is the restaurant located?" },
            { "speaker": "Marcus (Male / Front Desk)", "text": "Breakfast is served from 6:30 AM to 10:30 AM in the Terrace Bistro on the second floor. We offer both a continental buffet and made-to-order omelets." },
            { "speaker": "Emma (Female / Guest)", "text": "Wonderful. Also, does the hotel provide a complimentary shuttle service to the international airport on Wednesday?" },
            { "speaker": "Marcus (Male / Front Desk)", "text": "Yes, our airport shuttle departs every hour on the hour. You can reserve your seat with the concierge desk at least three hours before departure." },
            { "speaker": "Emma (Female / Guest)", "text": "Thank you so much for your attentive help, Marcus. I really appreciate it." },
            { "speaker": "Marcus (Male / Front Desk)", "text": "It is my absolute pleasure, Ms. Watson. Here are your room keys and Wi-Fi password. Enjoy your stay with us!" }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Marcus (Nam / Lễ tân):** Chào buổi tối! Chào mừng quý khách đến với Khách sạn Grand Horizon. Tôi có thể hỗ trợ gì cho quý khách tối nay ạ?\n
- **Emma (Nữ / Khách lưu trú):** Chào anh. Tôi có đặt phòng dưới tên Emma Watson cho ba đêm.\n
- **Marcus (Nam / Lễ tân):** Cảm ơn cô Watson. Để tôi mở thông tin đặt phòng trên hệ thống. Vâng, đây rồi ạ: một phòng Deluxe King hướng thành phố, bao gồm bữa sáng hàng ngày.\n
- **Emma (Nữ / Khách lưu trú):** Đúng rồi anh. Nếu được, tôi có thể xin một phòng ở tầng cao và cách xa thang máy không? Tôi rất khó ngủ và ngày mai có buổi hội thảo sớm.\n
- **Marcus (Nam / Lễ tân):** Chắc chắn rồi ạ! Chúng tôi còn một phòng góc rất yên tĩnh ở tầng 14 hướng ra sân vườn nội khu. Phòng này sẽ đảm bảo cho cô một giấc ngủ ngon không bị quấy rầy.\n
- **Emma (Nữ / Khách lưu trú):** Nghe tuyệt quá! Bữa sáng phục vụ từ mấy giờ vào buổi sáng và nhà hàng ở đâu vậy anh?\n
- **Marcus (Nam / Lễ tân):** Bữa sáng phục vụ từ 6:30 đến 10:30 sáng tại Nhà hàng Terrace Bistro ở tầng 2. Chúng tôi có cả tiệc buffet kiểu Âu và quầy trứng chiên làm theo yêu cầu.\n
- **Emma (Nữ / Khách lưu trú):** Tuyệt vời. Thêm nữa, khách sạn mình có dịch vụ xe buýt miễn phí đưa ra sân bay quốc tế vào thứ Tư không anh?\n
- **Marcus (Nam / Lễ tân):** Dạ có ạ, xe buýt đưa đón sân bay khởi hành vào đầu mỗi tiếng. Cô có thể đăng ký giữ chỗ tại quầy hỗ trợ khách hàng trước giờ khởi hành ít nhất 3 tiếng.\n
- **Emma (Nữ / Khách lưu trú):** Cảm ơn sự hỗ trợ rất chu đáo của anh nhé, Marcus. Tôi rất cảm kích.\n
- **Marcus (Nam / Lễ tân):** Đó là niềm vinh hạnh của tôi, thưa cô Watson. Đây là thẻ phòng và mật khẩu Wi-Fi. Chúc cô có kỳ nghỉ thật thoải mái tại khách sạn!""",
        "keyVocab": [
            { "word": "reservation", "ipa": "/ˌrez.ɚˈveɪ.ʃən/", "meaning": "sự đặt phòng/chỗ trước" },
            { "word": "amenity", "ipa": "/əˈmen.ə.t̬i/", "meaning": "tiện nghi, dịch vụ kèm theo" },
            { "word": "light sleeper", "ipa": "/laɪt ˈsliː.pɚ/", "meaning": "người thính ngủ, dễ bị đánh thức" },
            { "word": "complimentary", "ipa": "/ˌkɑːm.pləˈmen.t̬ɚ.i/", "meaning": "miễn phí (dịch vụ kèm theo)" },
            { "word": "concierge", "ipa": "/koʊn.siˈerʒ/", "meaning": "nhân viên hỗ trợ thông tin và dịch vụ khách hàng" }
        ],
        "questions": [
            {
                "id": "q-24-1",
                "question": "What special room request did Emma make during check-in?",
                "options": [
                    "A. She requested a room next to the fitness center.",
                    "B. She wanted a room on a higher floor away from the elevator because she is a light sleeper.",
                    "C. She asked for an extra bed for her pet dog.",
                    "D. She demanded an immediate upgrade to the presidential suite for free."
                ],
                "answerIndex": 1,
                "explanation": "Emma nói rõ: 'could I request a room on a higher floor away from the elevator? I am a light sleeper'."
            },
            {
                "id": "q-24-2",
                "question": "Where and when is breakfast served at the hotel?",
                "options": [
                    "A. On the rooftop from 8:00 AM to noon.",
                    "B. Inside the guest room upon dial-in order.",
                    "C. At the Terrace Bistro on the second floor from 6:30 AM to 10:30 AM.",
                    "D. At a nearby public cafe down the street."
                ],
                "answerIndex": 2,
                "explanation": "Marcus thông báo: 'Breakfast is served from 6:30 AM to 10:30 AM in the Terrace Bistro on the second floor'."
            },
            {
                "id": "q-24-3",
                "question": "How often does the hotel's airport shuttle depart?",
                "options": [
                    "A. Once a day at midnight.",
                    "B. Every hour on the hour.",
                    "C. Every fifteen minutes around the clock.",
                    "D. Only on weekends."
                ],
                "answerIndex": 1,
                "explanation": "Marcus giải thích: 'our airport shuttle departs every hour on the hour'."
            },
            {
                "id": "q-24-4",
                "question": "What must guests do to use the airport shuttle service?",
                "options": [
                    "A. Pay twenty dollars in cash directly to the driver.",
                    "B. Walk five kilometers to the bus terminal.",
                    "C. Reserve a seat with the concierge at least three hours before departure.",
                    "D. Bring their own bicycle."
                ],
                "answerIndex": 2,
                "explanation": "Marcus lưu ý: 'You can reserve your seat with the concierge desk at least three hours before departure'."
            }
        ]
    },

    # ---------------- MODULE 25 ----------------
    {
        "id": "read-25",
        "title": "How Remote Work is Transforming City Life",
        "type": "passage",
        "topic": "Công nghệ & Xã hội",
        "level": "B1 - B2",
        "summary": "Bài đọc phân tích xu hướng làm việc từ xa (remote work) và mô hình kết hợp (hybrid), tác động đến giao thông, nhà ở và kinh tế địa phương.",
        "content": """Over the past decade, the rapid advancement of cloud computing and high-speed fiber internet has reshaped modern employment. What began as a temporary measure during global emergencies has evolved into a permanent structural shift known as remote and hybrid work. Today, millions of knowledge workers across the globe no longer commute to downtown office towers five days a week. Instead, they divide their workweek between home offices, local shared workspaces, and periodic corporate meetings.\n\nThis shift has produced profound consequences for urban geography. For decades, major metropolises were designed around the assumption that workers would travel into central business districts every morning and leave every evening. Consequently, commercial centers boasted dense concentrations of coffee shops, restaurants, and retail stores catering strictly to daytime office workers. With lower daily foot traffic, downtown businesses have had to reinvent themselves, while residential suburban neighborhoods are experiencing a vibrant revitalization as residents spend more money close to home.\n\nMoreover, the flexibility of working from anywhere has encouraged many young families to relocate from cramped metropolitan apartments to spacious suburban or rural towns. When daily physical presence in an office is no longer mandatory, affordable housing, larger backyards, and access to nature become far more appealing than a short commute. Small towns that once struggled with population decline are now attracting skilled digital professionals, which stimulates local economies and tax revenues.\n\nNevertheless, remote work poses distinct organizational challenges. Team leaders must adopt structured communication tools to prevent employee isolation and maintain creative collaboration. Establishing clear boundaries between professional responsibilities and personal life is equally critical, as home workers frequently struggle to disconnect after business hours. Overall, finding an equitable balance between digital flexibility and in-person connection will define the future of sustainable workplace culture.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Trong thập kỷ qua, sự phát triển vượt bậc của điện toán đám mây và internet cáp quang tốc độ cao đã định hình lại việc làm hiện đại. Điều ban đầu vốn là giải pháp tạm thời trong các tình huống khẩn cấp toàn cầu nay đã tiến hóa thành một sự thay đổi cấu trúc lâu dài được gọi là làm việc từ xa và làm việc kết hợp (hybrid). Ngày nay, hàng triệu lao động tri thức trên toàn cầu không còn phải di chuyển vào các tòa tháp văn phòng trung tâm năm ngày một tuần. Thay vào đó, họ phân chia tuần làm việc giữa góc làm việc tại nhà, các không gian làm việc chung tại địa phương và những buổi họp trực tiếp định kỳ tại công ty.\n\nSự thay đổi này đã mang lại những hệ quả sâu sắc đối với địa lý đô thị. Trong nhiều thập kỷ, các đại đô thị được thiết kế dựa trên giả định rằng người lao động sẽ đổ xô vào các quận thương mại trung tâm mỗi sáng và rời đi vào mỗi tối. Do đó, các khu trung tâm thương mại từng tập trung dày đặc các quán cà phê, nhà hàng và cửa hàng bán lẻ chỉ phục vụ riêng cho dân văn phòng vào ban ngày. Khi lượng người đi lại hàng ngày giảm đi, các doanh nghiệp trung tâm buộc phải tự làm mới mình, trong khi các khu dân cư ngoại ô lại đón nhận sự hồi sinh sôi động khi người dân chi tiêu nhiều tiền hơn gần nhà.\n\nHơn nữa, sự linh hoạt khi có thể làm việc từ bất cứ đâu đã khuyến khích nhiều gia đình trẻ chuyển từ các căn hộ chật chội ở thành phố lớn về các thị trấn ngoại ô hoặc nông thôn rộng rãi hơn. Khi việc có mặt trực tiếp mỗi ngày ở văn phòng không còn là bắt buộc, nhà ở giá cả phải chăng, sân vườn rộng hơn và khả năng tiếp cận thiên nhiên trở nên hấp dẫn hơn nhiều so với việc chỉ để tiết kiệm thời gian đi làm. Những thị trấn nhỏ từng đối mặt với sự suy giảm dân số giờ đây lại thu hút các chuyên gia kỹ thuật số có tay nghề, giúp kích thích kinh tế và nguồn thu thuế địa phương.\n\nTuy nhiên, làm việc từ xa cũng đặt ra những thách thức đáng kể về mặt tổ chức. Các nhà lãnh đạo đội ngũ phải áp dụng các công cụ giao tiếp có cấu trúc để ngăn ngừa tình trạng nhân viên bị cô lập và duy trì sự hợp tác sáng tạo. Việc thiết lập ranh giới rõ ràng giữa trách nhiệm công việc và cuộc sống cá nhân cũng mang tính sống còn không kém, bởi những người làm việc tại nhà thường gặp khó khăn trong việc ngắt kết nối sau giờ làm. Nhìn chung, việc tìm kiếm sự cân bằng công bằng giữa tính linh hoạt kỹ thuật số và sự kết nối trực tiếp sẽ định hình tương lai của văn hóa làm việc bền vững.""",
        "keyVocab": [
            { "word": "hybrid work", "ipa": "/ˈhaɪ.brɪd wɝːk/", "meaning": "mô hình làm việc kết hợp giữa tại nhà và tại văn phòng" },
            { "word": "revitalization", "ipa": "/ˌriːˌvaɪ.t̬əl.əˈzeɪ.ʃən/", "meaning": "sự hồi sinh, tái sinh sức sống" },
            { "word": "relocate", "ipa": "/ˌriːˈloʊ.keɪt/", "meaning": "chuyển địa điểm sinh sống hoặc làm việc" },
            { "word": "isolation", "ipa": "/ˌaɪ.səˈleɪ.ʃən/", "meaning": "sự cô lập, cảm giác tách biệt" },
            { "word": "equitable", "ipa": "/ˈek.wə.t̬ə.bəl/", "meaning": "công bằng, hợp lý" }
        ],
        "questions": [
            {
                "id": "q-25-1",
                "question": "What technological foundations enabled the rise of remote and hybrid work?",
                "options": [
                    "A. Diesel generators and analog telephone wires.",
                    "B. Cloud computing and high-speed fiber internet.",
                    "C. Traditional fax machines and courier mail.",
                    "D. Electric scooters and battery storage."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu rõ: 'the rapid advancement of cloud computing and high-speed fiber internet has reshaped modern employment'."
            },
            {
                "id": "q-25-2",
                "question": "How has the shift to remote work affected suburban neighborhoods?",
                "options": [
                    "A. Suburban neighborhoods are becoming deserted and silent.",
                    "B. All local cafes in suburbs have been closed permanently.",
                    "C. Suburbs are experiencing revitalization as residents spend more money close to home.",
                    "D. Suburbs are replacing houses with heavy industrial factories."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 2 giải thích: 'residential suburban neighborhoods are experiencing a vibrant revitalization as residents spend more money close to home'."
            },
            {
                "id": "q-25-3",
                "question": "Why are many young families moving away from downtown metropolitan apartments?",
                "options": [
                    "A. Because downtown cities banned children from living in apartments.",
                    "B. They desire affordable housing, larger yards, and access to nature without daily commuting.",
                    "C. Because Internet connections are disabled in big cities.",
                    "D. They want to avoid using computers altogether."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 phân tích: 'affordable housing, larger backyards, and access to nature become far more appealing than a short commute'."
            },
            {
                "id": "q-25-4",
                "question": "What is one major challenge remote workers face regarding work-life balance?",
                "options": [
                    "A. Forgetting their company email passwords every week.",
                    "B. Having to wear a formal business suit at their desk all day.",
                    "C. Struggling to disconnect and establish clear boundaries after working hours.",
                    "D. Being unable to order groceries online."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 4 nhấn mạnh: 'home workers frequently struggle to disconnect after business hours'."
            }
        ]
    },

    # ---------------- MODULE 26 ----------------
    {
        "id": "read-26",
        "title": "At the Doctor's Office: Describing Symptoms & Medical Advice",
        "type": "conversation",
        "topic": "Sức khỏe & Y tế",
        "level": "B1 - B2",
        "summary": "Cuộc khám bệnh giữa bác sĩ gia đình và bệnh nhân bị ho kéo dài, sốt nhẹ và mệt mỏi sau khi chuyển mùa.",
        "content": [
            { "speaker": "Dr. Arthur (Male / Physician)", "text": "Good morning, Maya. Come on in and have a seat. What brings you into the clinic today?" },
            { "speaker": "Maya (Female / Patient)", "text": "Good morning, Dr. Arthur. I have not been feeling well for the past four days. I have a persistent dry cough, a mild fever, and a sore throat." },
            { "speaker": "Dr. Arthur (Male / Physician)", "text": "I see. Have you experienced any shortness of breath, chest tightness, or chills during the night?" },
            { "speaker": "Maya (Female / Patient)", "text": "No difficulty breathing, but I feel unusually fatigued, and my muscles ache after normal walking." },
            { "speaker": "Dr. Arthur (Male / Physician)", "text": "Let me check your vital signs. Your temperature is thirty-eight point two degrees Celsius, and your oxygen saturation is ninety-nine percent, which is reassuring. Now, let me listen to your lungs. Please take a deep breath through your mouth." },
            { "speaker": "Maya (Female / Patient)", "text": "(Breathes deeply) How do my lungs sound, Doctor?" },
            { "speaker": "Dr. Arthur (Male / Physician)", "text": "Your lungs sound completely clear—no wheezing or fluid congestion. It appears to be an acute viral upper respiratory infection, commonly known as a seasonal flu." },
            { "speaker": "Maya (Female / Patient)", "text": "Do I need to take antibiotics to clear this up?" },
            { "speaker": "Dr. Arthur (Male / Physician)", "text": "No, antibiotics only target bacterial infections and are ineffective against viruses. Taking them unnecessarily can disrupt your gut flora and cause resistance. Instead, I recommend plenty of bed rest, warm fluids, and paracetamol for the fever and body aches." },
            { "speaker": "Maya (Female / Patient)", "text": "Understood. Should I stay home from work for a few days?" },
            { "speaker": "Dr. Arthur (Male / Physician)", "text": "Yes, I will write you a medical certificate for three days of rest. If your fever persists beyond five days or you develop chest pain, please return immediately for a follow-up." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Bác sĩ Arthur (Nam / Bác sĩ):** Chào buổi sáng, Maya. Mời cô vào phòng và ngồi xuống. Hôm nay có vấn đề gì khiến cô phải đến phòng khám vậy?\n
- **Maya (Nữ / Bệnh nhân):** Chào bác sĩ Arthur. Bốn ngày nay tôi thấy không được khỏe. Tôi bị ho khan kéo dài, sốt nhẹ và đau rát họng.\n
- **Bác sĩ Arthur (Nam / Bác sĩ):** Tôi hiểu rồi. Cô có thấy khó thở, tức ngực hay bị ớn lạnh vào ban đêm không?\n
- **Maya (Nữ / Bệnh nhân):** Dạ không khó thở, nhưng tôi cảm thấy mệt mỏi bất thường và các cơ bắp bị nhức mỏi dù chỉ đi bộ bình thường.\n
- **Bác sĩ Arthur (Nam / Bác sĩ):** Để tôi kiểm tra các chỉ số sinh tồn của cô nhé. Thân nhiệt của cô là 38,2 độ C, và độ bão hòa oxy là 99%, chỉ số này rất an tâm. Bây giờ, hãy để tôi nghe phổi của cô. Hãy hít một hơi thật sâu bằng miệng nhé.\n
- **Maya (Nữ / Bệnh nhân):** (Hít sâu) Phổi của tôi nghe thế nào vậy bác sĩ?\n
- **Bác sĩ Arthur (Nam / Bác sĩ):** Phổi của cô rất trong—không có tiếng khò khè hay ứ dịch. Có vẻ đây là tình trạng nhiễm trùng đường hô hấp trên cấp tính do virus, thường gọi là cảm cúm theo mùa.\n
- **Maya (Nữ / Bệnh nhân):** Tôi có cần uống thuốc kháng sinh để khỏi dứt điểm không bác sĩ?\n
- **Bác sĩ Arthur (Nam / Bác sĩ):** Không nên đâu cô, thuốc kháng sinh chỉ tiêu diệt vi khuẩn và hoàn toàn không có tác dụng đối với virus. Uống kháng sinh không cần thiết có thể làm rối loạn hệ vi sinh đường ruột và gây kháng thuốc. Thay vào đó, tôi khuyên cô nên nghỉ ngơi nhiều trên giường, uống nhiều nước ấm và dùng paracetamol để hạ sốt và giảm đau mỏi cơ.\n
- **Maya (Nữ / Bệnh nhân):** Tôi hiểu rồi ạ. Tôi có nên xin nghỉ làm ở nhà vài hôm không?\n
- **Bác sĩ Arthur (Nam / Bác sĩ):** Có chứ, tôi sẽ viết giấy nghỉ ốm cho cô trong 3 ngày để nghỉ ngơi. Nếu cơn sốt kéo dài quá 5 ngày hoặc cô thấy đau ngực, hãy quay lại tái khám ngay nhé.""",
        "keyVocab": [
            { "word": "persistent", "ipa": "/pɚˈsɪs.tənt/", "meaning": "dai dẳng, kéo dài liên tục" },
            { "word": "vital signs", "ipa": "/ˈvaɪ.t̬əl saɪnz/", "meaning": "các chỉ số sinh tồn (mạch, huyết áp, nhiệt độ, oxy)" },
            { "word": "respiratory infection", "ipa": "/ˈres.pɚ.ə.tɔːr.i ɪnˈfek.ʃən/", "meaning": "nhiễm trùng đường hô hấp" },
            { "word": "ineffective", "ipa": "/ˌɪn.ɪˈfek.tɪv/", "meaning": "không có hiệu quả, vô hiệu" },
            { "word": "follow-up", "ipa": "/ˈfɑː.loʊ.ʌp/", "meaning": "tái khám, theo dõi tiếp theo" }
        ],
        "questions": [
            {
                "id": "q-26-1",
                "question": "What primary symptoms did Maya present with at the clinic?",
                "options": [
                    "A. Severe toothache and blurred vision.",
                    "B. A persistent dry cough, mild fever, sore throat, and muscle fatigue.",
                    "C. A sprained ankle from playing tennis.",
                    "D. Ear infection and stomach cramps."
                ],
                "answerIndex": 1,
                "explanation": "Maya trình bày: 'I have a persistent dry cough, a mild fever, and a sore throat... feel unusually fatigued, and my muscles ache'."
            },
            {
                "id": "q-26-2",
                "question": "What diagnosis did Dr. Arthur give after examining Maya's lungs?",
                "options": [
                    "A. Severe bacterial pneumonia requiring immediate hospitalization.",
                    "B. Chronic asthma triggered by animal allergies.",
                    "C. An acute viral upper respiratory infection (seasonal flu).",
                    "D. A broken rib caused by heavy lifting."
                ],
                "answerIndex": 2,
                "explanation": "Bác sĩ kết luận: 'an acute viral upper respiratory infection, commonly known as a seasonal flu'."
            },
            {
                "id": "q-26-3",
                "question": "Why did Dr. Arthur advise against taking antibiotics for Maya's condition?",
                "options": [
                    "A. The clinic had run out of antibiotics in the pharmacy.",
                    "B. Antibiotics are only effective against bacteria, not viruses, and can cause resistance.",
                    "C. Antibiotics are illegal to prescribe to adults.",
                    "D. Maya requested herbal tea instead."
                ],
                "answerIndex": 1,
                "explanation": "Bác sĩ giải thích rõ: 'antibiotics only target bacterial infections and are ineffective against viruses. Taking them unnecessarily can disrupt your gut flora and cause resistance'."
            },
            {
                "id": "q-26-4",
                "question": "Under what circumstance should Maya return immediately to the clinic?",
                "options": [
                    "A. If she feels hungry in the evening.",
                    "B. If her fever persists beyond five days or she develops chest pain.",
                    "C. If she finishes reading her favorite book.",
                    "D. If her coworker asks for her medical note."
                ],
                "answerIndex": 1,
                "explanation": "Bác sĩ dặn: 'If your fever persists beyond five days or you develop chest pain, please return immediately for a follow-up'."
            }
        ]
    },

    # ---------------- MODULE 27 ----------------
    {
        "id": "read-27",
        "title": "Smart Budgeting Tips for Young Professionals",
        "type": "passage",
        "topic": "Tài chính cá nhân",
        "level": "B1 - B2",
        "summary": "Bài đọc hướng dẫn quy tắc quản lý tài chính 50/30/20, xây dựng quỹ khẩn cấp và thiết lập thói quen chi tiêu thông minh cho người trẻ.",
        "content": """Entering the workforce and receiving a regular monthly salary is an exciting milestone for young adults. However, without deliberate financial planning, rising living costs and impulsive consumerism can rapidly deplete earnings. Many graduates discover that despite earning decent salaries, they live paycheck to paycheck, struggling to cover unexpected emergencies or make meaningful investments. Learning foundational personal finance habits early in one's career lays the groundwork for lasting peace of mind.\n\nA widely praised and practical budgeting framework is the 50/30/20 rule, popularized by financial educators. Under this straightforward formula, fifty percent of net after-tax income is allocated to essential needs, such as rent, utilities, groceries, and student loan payments. Thirty percent is dedicated to discretionary wants—dining out with friends, hobby supplies, entertainment subscriptions, and weekend leisure. The remaining twenty percent must be directed toward savings, debt elimination, and long-term investment vehicles.\n\nBefore exploring high-risk investment avenues such as equities or cryptocurrencies, financial planners unanimously recommend building a robust emergency fund. An emergency cushion consisting of three to six months of basic living expenses protects individuals against unforeseen setbacks, such as sudden medical bills, automotive breakdowns, or unexpected unemployment. Storing these funds in a high-yield savings account ensures that money remains immediately accessible while earning modest interest against inflation.\n\nUltimately, mastering personal finance is less about achieving extreme frugality and more about fostering intentionality. By tracking daily expenditures on mobile banking apps and automating recurring transfers to savings accounts on payday, young professionals build wealth effortlessly. Financial freedom does not mean denying yourself every pleasure; rather, it empowers you to make informed life decisions without the chronic burden of monetary distress.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Bước chân vào thị trường lao động và nhận được mức lương hàng tháng đều đặn là một cột mốc thú vị đối với những người trẻ tuổi. Tuy nhiên, nếu không có kế hoạch tài chính có chủ đích, chi phí sinh hoạt ngày càng tăng và chủ nghĩa tiêu dùng bốc đồng có thể nhanh chóng làm cạn kiệt thu nhập. Nhiều người mới tốt nghiệp nhận thấy rằng dù kiếm được mức lương khá, họ vẫn sống trong cảnh \"chờ lương từng tháng\", chật vật trang trải các trường hợp khẩn cấp bất ngờ hoặc không thể đầu tư có ý nghĩa. Học các thói quen tài chính cá nhân nền tảng từ sớm trong sự nghiệp sẽ đặt nền móng cho sự an tâm lâu dài.\n\nMột khuôn khổ lập ngân sách thực tế và được khen ngợi rộng rãi là quy tắc 50/30/20, được các chuyên gia giáo dục tài chính phổ biến. Theo công thức đơn giản này, 50% thu nhập ròng sau thuế được phân bổ cho các nhu cầu thiết yếu như tiền thuê nhà, điện nước, thực phẩm và các khoản trả nợ học phí. 30% dành cho những mong muốn sở thích—đi ăn ngoài với bạn bè, đồ dùng theo sở thích, các gói giải trí và thư giãn cuối tuần. 20% còn lại bắt buộc phải dành cho tiết kiệm, xóa nợ và các kênh đầu tư dài hạn.\n\nTrước khi tìm hiểu các kênh đầu tư rủi ro cao như cổ phiếu hay tiền kỹ thuật số, các nhà hoạch định tài chính đều đồng lòng khuyến nghị xây dựng một quỹ khẩn cấp vững chắc. Một chiếc đệm dự phòng khẩn cấp bao gồm 3 đến 6 tháng chi phí sinh hoạt cơ bản sẽ bảo vệ các cá nhân trước những biến cố khó lường, chẳng hạn như hóa đơn y tế đột xuất, hỏng xe hoặc thất nghiệp bất ngờ. Giữ số tiền này trong một tài khoản tiết kiệm lãi suất cao đảm bảo rằng tiền vẫn có thể sử dụng được ngay lập tức trong khi vẫn sinh lãi nhẹ để chống lạm phát.\n\nSuy cho cùng, việc làm chủ tài chính cá nhân không phải là hướng tới lối sống quá mức tằn tiện, mà là thúc đẩy tính có chủ đích. Bằng cách theo dõi các khoản chi tiêu hàng ngày trên ứng dụng ngân hàng di động và tự động hóa các khoản chuyển tiền định kỳ vào tài khoản tiết kiệm vào ngày nhận lương, những người đi làm trẻ tuổi có thể xây dựng sự giàu có một cách nhẹ nhàng. Tự do tài chính không có nghĩa là từ chối mọi niềm vui; đúng hơn, nó trao quyền cho bạn đưa ra những quyết định cuộc đời sáng suốt mà không phải chịu gánh nặng kinh niên của nỗi lo tiền bạc.""",
        "keyVocab": [
            { "word": "impulsive", "ipa": "/ɪmˈpʌl.sɪv/", "meaning": "bốc đồng, ngẫu hứng không suy tính" },
            { "word": "paycheck to paycheck", "ipa": "/ˈpeɪ.tʃek tə ˈpeɪ.tʃek/", "meaning": "sống chật vật tháng nào xào hết tháng đó" },
            { "word": "discretionary", "ipa": "/dɪˈskreʃ.ən.er.i/", "meaning": "tùy ý, tự do quyết định (khoản chi không bắt buộc)" },
            { "word": "emergency fund", "ipa": "/ɪˈmɝː.dʒən.si fʌnd/", "meaning": "quỹ dự phòng tài chính khẩn cấp" },
            { "word": "frugality", "ipa": "/fruːˈɡæl.ə.t̬i/", "meaning": "lối sống tiết kiệm, thanh đạm" }
        ],
        "questions": [
            {
                "id": "q-27-1",
                "question": "According to the 50/30/20 rule, how should net income be distributed?",
                "options": [
                    "A. 50% for luxury holidays, 30% for restaurants, 20% for taxes.",
                    "B. 50% for essential needs, 30% for discretionary wants, and 20% for savings and debt reduction.",
                    "C. 50% for cryptocurrency, 30% for rent, 20% for shopping.",
                    "D. Equal one-third shares for food, clothes, and technology."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 giải thích rõ ràng: 'fifty percent of net after-tax income is allocated to essential needs... thirty percent is dedicated to discretionary wants... remaining twenty percent must be directed toward savings'."
            },
            {
                "id": "q-27-2",
                "question": "How much money should ideally be stored in an emergency fund?",
                "options": [
                    "A. Exactly one week of grocery costs.",
                    "B. Three to six months of basic living expenses.",
                    "C. Five years of maximum luxury travel expenses.",
                    "D. One thousand dollars regardless of living cost."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 khuyến nghị: 'An emergency cushion consisting of three to six months of basic living expenses protects individuals against unforeseen setbacks'."
            },
            {
                "id": "q-27-3",
                "question": "Why is keeping emergency money in an accessible high-yield account recommended?",
                "options": [
                    "A. It prevents banks from asking questions about taxes.",
                    "B. It ensures money is immediately accessible for emergencies while earning interest against inflation.",
                    "C. It guarantees a ten-fold profit every single month.",
                    "D. It locks the funds permanently so you cannot spend them."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 nhấn mạnh: 'ensures that money remains immediately accessible while earning modest interest against inflation'."
            },
            {
                "id": "q-27-4",
                "question": "What is the true underlying philosophy of financial freedom described in the text?",
                "options": [
                    "A. Denying yourself all simple pleasures and never buying gifts.",
                    "B. Becoming a millionaire before the age of twenty-five.",
                    "C. Fostering intentionality and making informed life decisions without chronic money stress.",
                    "D. Borrowing money from family whenever expenses arise."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 4 kết luận: 'Financial freedom does not mean denying yourself every pleasure; rather, it empowers you to make informed life decisions without the chronic burden of monetary distress'."
            }
        ]
    },

    # ---------------- MODULE 28 ----------------
    {
        "id": "read-28",
        "title": "Dining Out: Ordering Food, Dietary Preferences & Settling the Bill",
        "type": "conversation",
        "topic": "Ẩm thực & Nhà hàng",
        "level": "B1 - B2",
        "summary": "Tình huống giao tiếp thực tế tại nhà hàng Ý: Gọi món khai vị, món chính, thông báo dị ứng đậu phộng và chia hóa đơn thanh toán.",
        "content": [
            { "speaker": "Julian (Male / Waiter)", "text": "Good evening and welcome to Bella Italia Bistro. Are you ready to order, or would you like a few more minutes to browse the menu?" },
            { "speaker": "Chloe (Female / Diner)", "text": "Good evening! We are ready to order. To start, could we get the bruschetta with heirloom tomatoes and fresh basil?" },
            { "speaker": "Julian (Male / Waiter)", "text": "An excellent choice. Our chef bakes the sourdough bread fresh every afternoon. And for your main courses?" },
            { "speaker": "Chloe (Female / Diner)", "text": "I would like the handmade seafood linguine with garlic and white wine sauce. However, my friend has a severe peanut and pine nut allergy. Does the basil pesto pasta contain any nuts?" },
            { "speaker": "Julian (Male / Waiter)", "text": "I am very glad you informed me. Yes, our traditional pesto contains crushed pine nuts. I will notify the kitchen immediately to prepare her dish separately to avoid cross-contamination, or she could try our wild mushroom risotto, which is completely nut-free." },
            { "speaker": "Chloe (Female / Diner)", "text": "The wild mushroom risotto sounds wonderful for her, thank you so much for being so vigilant." },
            { "speaker": "Julian (Male / Waiter)", "text": "You are very welcome. Would you care for any drinks to accompany your meal—perhaps a bottle of sparkling mineral water?" },
            { "speaker": "Chloe (Female / Diner)", "text": "Yes, a large bottle of sparkling water with lemon slices would be great." },
            { "speaker": "Julian (Male / Waiter)", "text": "(Later) Here is your bill whenever you are ready. Take your time, no rush at all." },
            { "speaker": "Chloe (Female / Diner)", "text": "Thank you, Julian. The food was exquisite! Could we split the bill evenly between two credit cards, and please include a fifteen percent gratuity for your exceptional service?" },
            { "speaker": "Julian (Male / Waiter)", "text": "Certainly, I can split that right here on the terminal. Thank you so much for dining with us tonight!" }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Julian (Nam / Nhân viên phục vụ):** Chào buổi tối và chào mừng quý khách đến với Bella Italia Bistro. Quý khách đã sẵn sàng gọi món chưa, hay muốn có thêm vài phút để xem thực đơn ạ?\n
- **Chloe (Nữ / Thực khách):** Chào anh! Chúng tôi đã sẵn sàng gọi món rồi. Để khai vị, chúng tôi xin gọi món bánh mì nướng bruschetta cà chua và húng quế tươi nhé.\n
- **Julian (Nam / Nhân viên phục vụ):** Một lựa chọn tuyệt vời ạ. Bếp trưởng của chúng tôi nướng bánh mì chua tươi vào mỗi buổi chiều. Còn về các món chính thì sao ạ?\n
- **Chloe (Nữ / Thực khách):** Tôi muốn gọi món mì linguine hải sản thủ công sốt tỏi và rượu vang trắng. Tuy nhiên, bạn tôi bị dị ứng rất nặng với đậu phộng và hạt thông. Món mì sốt pesto húng quế có chứa hạt nào không anh?\n
- **Julian (Nam / Nhân viên phục vụ):** Rất may là cô đã báo trước cho tôi biết. Vâng, sốt pesto truyền thống của chúng tôi có chứa hạt thông giã nhỏ. Tôi sẽ báo với bếp ngay lập tức để làm món ăn của cô ấy riêng biệt nhằm tránh nhiễm chéo, hoặc cô ấy có thể thử món cơm Ý risotto nấm rừng hoàn toàn không chứa các loại hạt.\n
- **Chloe (Nữ / Thực khách):** Món risotto nấm rừng nghe rất hợp với bạn tôi, cảm ơn anh đã rất cẩn thận và chu đáo.\n
- **Julian (Nam / Nhân viên phục vụ):** Không có chi ạ. Quý khách có muốn dùng đồ uống gì kèm bữa ăn không—ví dụ một chai nước khoáng có ga nhé?\n
- **Chloe (Nữ / Thực khách):** Vâng, cho chúng tôi một chai nước khoáng có ga lớn kèm vài lát chanh tươi nhé.\n
- **Julian (Nam / Nhân viên phục vụ):** (Lúc sau) Hóa đơn của quý khách đây ạ, quý khách cứ thư thả không cần vội đâu nhé.\n
- **Chloe (Nữ / Thực khách):** Cảm ơn anh Julian. Đồ ăn ngon tuyệt vời! Chúng tôi có thể chia đôi hóa đơn này ra hai thẻ tín dụng không, và hãy tính thêm 15% tiền tip cho sự phục vụ xuất sắc của anh nhé?\n
- **Julian (Nam / Nhân viên phục vụ):** Dạ chắc chắn rồi ạ, tôi có thể chia hóa đơn ngay trên máy quẹt thẻ cầm tay này. Cảm ơn quý khách rất nhiều vì đã dùng bữa tại nhà hàng tối nay!""",
        "keyVocab": [
            { "word": "appetizer", "ipa": "/ˈæp.ə.taɪ.zɚ/", "meaning": "món khai vị" },
            { "word": "cross-contamination", "ipa": "/ˌkrɑːs kənˌtæm.əˈneɪ.ʃən/", "meaning": "sự lây nhiễm chéo (chất dị ứng giữa các món)" },
            { "word": "vigilant", "ipa": "/ˈvɪdʒ.əl.ənt/", "meaning": "cẩn trọng, cảnh giác, chu đáo" },
            { "word": "exquisite", "ipa": "/ɪkˈskwɪz.ɪt/", "meaning": "tuyệt hảo, tinh tế xuất sắc" },
            { "word": "gratuity", "ipa": "/ɡrəˈtuː.ə.t̬i/", "meaning": "tiền tip, tiền thưởng cho phục vụ" }
        ],
        "questions": [
            {
                "id": "q-28-1",
                "question": "What appetizer did Chloe order for the table?",
                "options": [
                    "A. Crispy fried calamari with tartar sauce.",
                    "B. Tomato bruschetta with fresh basil on sourdough bread.",
                    "C. A bowl of spicy chicken wings.",
                    "D. French onion soup with cheese croutons."
                ],
                "answerIndex": 1,
                "explanation": "Chloe gọi: 'could we get the bruschetta with heirloom tomatoes and fresh basil?'"
            },
            {
                "id": "q-28-2",
                "question": "Why did Julian advise Chloe's friend against ordering the traditional basil pesto?",
                "options": [
                    "A. The kitchen had run out of basil leaves.",
                    "B. The pesto contains crushed pine nuts, which would trigger her friend's severe allergy.",
                    "C. The pesto dish is only served during lunch hours.",
                    "D. The chef refuses to cook pasta without hot chili peppers."
                ],
                "answerIndex": 1,
                "explanation": "Julian giải thích: 'our traditional pesto contains crushed pine nuts... avoid cross-contamination'."
            },
            {
                "id": "q-28-3",
                "question": "What nut-free alternative dish did Julian suggest for Chloe's friend?",
                "options": [
                    "A. Beef cheeseburger with fries.",
                    "B. Wild mushroom risotto.",
                    "C. Raw oysters on ice.",
                    "D. Peanut butter noodles."
                ],
                "answerIndex": 1,
                "explanation": "Julian gợi ý: 'she could try our wild mushroom risotto, which is completely nut-free'."
            },
            {
                "id": "q-28-4",
                "question": "How did Chloe request to settle the bill at the conclusion of dinner?",
                "options": [
                    "A. Asking to wash dishes in the kitchen.",
                    "B. Paying completely in cash with no tip.",
                    "C. Splitting the bill evenly between two credit cards with a 15% gratuity included.",
                    "D. Requesting an invoice to be sent to her company office next month."
                ],
                "answerIndex": 2,
                "explanation": "Chloe nói: 'Could we split the bill evenly between two credit cards, and please include a fifteen percent gratuity'."
            }
        ]
    },

    # ---------------- MODULE 29 ----------------
    {
        "id": "read-29",
        "title": "The Impact of Fast Fashion on the Environment",
        "type": "passage",
        "topic": "Môi trường & Tiêu dùng",
        "level": "B1 - B2",
        "summary": "Bài đọc khám phá mô hình thời trang nhanh, lượng rác thải dệt may khổng lồ và sự trỗi dậy của lối sống tiêu dùng thời trang bền vững.",
        "content": """The global fashion industry has undergone a radical transformation over the past three decades. Historically, apparel brands operated on four distinct seasonal cycles: spring, summer, autumn, and winter. Today, global retail giants operate on a micro-season model, releasing up to fifty-two micro-collections every single year. This business strategy, universally known as fast fashion, relies on mass-producing trendy garments rapidly at exceptionally low consumer prices, encouraging shoppers to treat clothes as disposable commodities.\n\nWhile fast fashion has democratized access to trendy styles, its environmental toll is catastrophic. The textile manufacturing process requires staggering quantities of natural resources. Producing a single pair of conventional cotton jeans consumes approximately seven thousand liters of clean fresh water. Furthermore, synthetic fabrics like polyester, nylon, and acrylic are derived from petroleum. Every time these synthetic garments are washed in household washing machines, they shed thousands of microscopic plastic fibers that bypass filtration systems and contaminate oceanic ecosystems.\n\nIn addition to water depletion and chemical pollution, fast fashion generates unprecedented mountains of solid waste. Consumers purchase sixty percent more clothing items today than they did in the year 2000, yet retain them for only half as long. Millions of tons of discarded synthetic clothes end up in municipal landfills or are dumped in fragile deserts in the Global South, where they take hundreds of years to decompose while releasing hazardous greenhouse gases.\n\nFortunately, a burgeoning counter-movement prioritizing sustainable and circular fashion is gaining momentum worldwide. Conscious consumers are increasingly embracing thrift shopping, clothes swapping, and renting formal outfits for special occasions. Moreover, innovative apparel startups are investing in eco-friendly fabrics, such as organic linen, recycled cotton, and plant-based leather alternatives. By choosing quality over quantity and repairing beloved garments rather than discarding them, consumers can significantly reduce their ecological footprint.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Ngành công nghiệp thời trang toàn cầu đã trải qua một cuộc chuyển đổi triệt để trong ba thập kỷ qua. Trong lịch sử, các thương hiệu may mặc hoạt động theo bốn chu kỳ mùa riêng biệt: xuân, hạ, thu và đông. Ngày nay, các người khổng lồ bán lẻ toàn cầu hoạt động theo mô hình \"vi mùa\", tung ra tới 52 bộ sưu tập nhỏ mỗi năm. Chiến lược kinh doanh này, được biết đến rộng rãi với tên gọi thời trang nhanh, dựa trên việc sản xuất hàng loạt các bộ trang phục bắt kịp xu hướng một cách thần tốc với mức giá người tiêu dùng đặc biệt thấp, khuyến khích người mua sắm coi quần áo như những món đồ dùng một lần.\n\nMặc dù thời trang nhanh đã phổ cập hóa cơ hội tiếp cận các phong cách hợp thời, cái giá phải trả đối với môi trường là vô cùng thảm khốc. Quy trình sản xuất dệt may đòi hỏi lượng tài nguyên thiên nhiên đáng kinh ngạc. Sản xuất một chiếc quần jean cotton truyền thống tiêu tốn khoảng 7.000 lít nước ngọt sạch. Hơn nữa, các loại vải tổng hợp như polyester, nylon và acrylic đều có nguồn gốc từ dầu mỏ. Mỗi khi những bộ quần áo tổng hợp này được giặt trong máy giặt gia đình, chúng rụng ra hàng ngàn sợi nhựa siêu nhỏ vượt qua hệ thống lọc và gây ô nhiễm các hệ sinh thái đại dương.\n\nBên cạnh việc cạn kiệt nguồn nước và ô nhiễm hóa chất, thời trang nhanh còn tạo ra những núi rác thải rắn chưa từng có. Người tiêu dùng ngày nay mua sắm nhiều quần áo hơn 60% so với năm 2000, nhưng chỉ giữ chúng trong thời gian ngắn bằng một nửa. Hàng triệu tấn quần áo tổng hợp bị vứt bỏ nằm tại các bãi rác đô thị hoặc bị đổ bừa bãi tại các sa mạc mỏng manh ở bán cầu Nam, nơi chúng phải mất hàng trăm năm để phân hủy trong khi liên tục giải phóng các loại khí nhà kính độc hại.\n\nMay mắn thay, một phong trào đối trọng đang phát triển ưu tiên thời trang bền vững và tuần hoàn đang lấy lại đà trên toàn thế giới. Những người tiêu dùng có ý thức đang ngày càng hào hứng với việc mua sắm đồ cũ (thrifting), trao đổi quần áo và thuê trang phục dạ hội cho các dịp đặc biệt. Hơn nữa, các công ty khởi nghiệp may mặc sáng tạo đang đầu tư vào các loại vải thân thiện với môi trường, chẳng hạn như vải lanh hữu cơ, cotton tái chế và các chất liệu da thay thế từ thực vật. Bằng cách chọn chất lượng thay vì số lượng và sửa chữa những bộ quần áo yêu quý thay vì vứt bỏ chúng, người tiêu dùng có thể giảm đáng kể dấu chân sinh thái của mình.""",
        "keyVocab": [
            { "word": "commodity", "ipa": "/kəˈmɑː.də.t̬i/", "meaning": "hàng hóa, vật phẩm tiêu dùng" },
            { "word": "catastrophic", "ipa": "/ˌkæt̬.əˈstrɑː.fɪk/", "meaning": "thảm khốc, gây tai họa lớn" },
            { "word": "microfiber", "ipa": "/ˈmaɪ.kroʊˌfaɪ.bɚ/", "meaning": "vi sợi nhựa (rụng ra từ vải tổng hợp)" },
            { "word": "landfill", "ipa": "/ˈlænd.fɪl/", "meaning": "bãi chôn lấp rác thải" },
            { "word": "circular fashion", "ipa": "/ˈsɝː.kjə.lɚ ˈfæʃ.ən/", "meaning": "thời trang tuần hoàn (tái chế, tái sử dụng liên tục)" }
        ],
        "questions": [
            {
                "id": "q-29-1",
                "question": "How often do modern fast fashion retailers release new micro-collections?",
                "options": [
                    "A. Only once every two years.",
                    "B. Four times a year matching seasonal solstices.",
                    "C. Up to fifty-two times a year (every week).",
                    "D. Exactly once a decade."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 1 nêu rõ: 'global retail giants operate on a micro-season model, releasing up to fifty-two micro-collections every single year'."
            },
            {
                "id": "q-29-2",
                "question": "What happens when synthetic clothes like polyester are washed in home washing machines?",
                "options": [
                    "A. They turn into organic plant fertilizer.",
                    "B. They release thousands of microscopic plastic fibers that contaminate waterways and oceans.",
                    "C. They generate clean solar electricity for the home.",
                    "D. They shrink into pure cotton threads."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 giải thích: 'Every time these synthetic garments are washed... they shed thousands of microscopic plastic fibers that bypass filtration systems and contaminate oceanic ecosystems'."
            },
            {
                "id": "q-29-3",
                "question": "Compared to the year 2000, how has consumer clothing behavior changed?",
                "options": [
                    "A. People buy sixty percent more clothes but keep them only half as long.",
                    "B. People weave all their own clothes by hand.",
                    "C. People wear the exact same pair of trousers for twenty years.",
                    "D. People spend ninety percent less money on clothing."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 3 chỉ ra: 'Consumers purchase sixty percent more clothing items today than they did in the year 2000, yet retain them for only half as long'."
            },
            {
                "id": "q-29-4",
                "question": "What is one way conscious consumers are promoting sustainable fashion?",
                "options": [
                    "A. Burning their old garments in the backyard.",
                    "B. Buying fifteen cheap t-shirts every weekend online.",
                    "C. Embracing secondhand thrift shopping, clothes swapping, and repairing damaged garments.",
                    "D. Throwing away clothes as soon as they get slightly dusty."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 4 nêu rõ: 'embracing thrift shopping, clothes swapping... choosing quality over quantity and repairing beloved garments'."
            }
        ]
    },

    # ---------------- MODULE 30 ----------------
    {
        "id": "read-30",
        "title": "Tech Support: Troubleshooting Home Wi-Fi & Internet Issues",
        "type": "conversation",
        "topic": "Công nghệ & Đời sống",
        "level": "B1 - B2",
        "summary": "Cuộc gọi hỗ trợ kỹ thuật xử lý sự cố mạng Internet gia đình bị chập chờn, kiểm tra modem và đổi kênh tần số Wi-Fi.",
        "content": [
            { "speaker": "Daniel (Male / Support Agent)", "text": "Thank you for calling Apex Fiber Customer Support. My name is Daniel. May I have your account number and registered name, please?" },
            { "speaker": "Sarah (Female / Customer)", "text": "Hello Daniel. My account number is AF-84920, and my name is Sarah Jenkins. I am calling because my Wi-Fi keeps disconnecting every twenty minutes, which makes working from home impossible." },
            { "speaker": "Daniel (Male / Support Agent)", "text": "I completely understand how frustrating that must be, Ms. Jenkins. Let me run a diagnostic test on your optical terminal from our system. Could you take a quick look at your router and tell me what the indicator lights look like?" },
            { "speaker": "Sarah (Female / Customer)", "text": "Sure. The power light is solid green, but the internet globe symbol is flashing amber intermittently." },
            { "speaker": "Daniel (Male / Support Agent)", "text": "That indicates a signal synchronization drop between the router and our neighborhood exchange. First, let us perform a complete power cycle. Could you unplug the power cord from the back of the modem?" },
            { "speaker": "Sarah (Female / Customer)", "text": "Okay, I have unplugged it. How long should I leave it disconnected?" },
            { "speaker": "Daniel (Male / Support Agent)", "text": "Please leave it unplugged for thirty full seconds to allow all residual electrical charge in the capacitors to dissipate. After that, plug it back in firmly." },
            { "speaker": "Sarah (Female / Customer)", "text": "(After thirty seconds) Okay, I just plugged it back in. The lights are cycling through red, amber, and now turning solid blue." },
            { "speaker": "Daniel (Male / Support Agent)", "text": "Solid blue means the high-speed fiber connection has synchronized properly. I also noticed on my diagnostic screen that your router was operating on a crowded 2.4 GHz channel. I have just remotely switched your primary network to the 5 GHz band, which offers significantly less interference." },
            { "speaker": "Sarah (Female / Customer)", "text": "Let me test it on my laptop right now. Wow, the speed test shows ninety-five megabits per second, and my video conference reconnected immediately!" },
            { "speaker": "Daniel (Male / Support Agent)", "text": "That is fantastic news. If the connection drops again over the next forty-eight hours, your ticket remains open, and we will dispatch a field technician at no charge." },
            { "speaker": "Sarah (Female / Customer)", "text": "You have been tremendously helpful, Daniel. Thank you so much for resolving this so promptly!" }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Cảm ơn quý khách đã gọi đến Tổng đài Hỗ trợ Khách hàng Apex Fiber. Tôi tên là Daniel. Tôi có thể xin số tài khoản và tên đăng ký của quý khách được không ạ?\n
- **Sarah (Nữ / Khách hàng):** Chào Daniel. Số tài khoản của tôi là AF-84920, tên tôi là Sarah Jenkins. Tôi gọi vì mạng Wi-Fi nhà tôi cứ 20 phút lại bị ngắt kết nối một lần, khiến tôi không thể nào làm việc tại nhà được.\n
- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Tôi hoàn toàn hiểu sự bất tiện khó chịu đó, cô Jenkins. Để tôi chạy bài kiểm tra chẩn đoán trên thiết bị đầu cuối cáp quang của cô từ hệ thống. Cô có thể nhìn nhanh vào modem Wi-Fi và cho tôi biết các đèn báo đang hiển thị thế nào không ạ?\n
- **Sarah (Nữ / Khách hàng):** Được rồi. Đèn nguồn đang sáng xanh liên tục, nhưng biểu tượng quả địa cầu internet thì thỉnh thoảng lại nhấp nháy màu vàng cam.\n
- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Dấu hiệu đó cho thấy việc mất đồng bộ tín hiệu giữa modem và trạm phát khu vực của chúng tôi. Trước tiên, chúng ta hãy thử khởi động lại nguồn hoàn toàn nhé. Cô có thể rút dây nguồn ở phía sau modem ra không ạ?\n
- **Sarah (Nữ / Khách hàng):** Được rồi, tôi đã rút dây ra rồi. Tôi nên để ngắt điện trong bao lâu?\n
- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Cô hãy để ngắt điện trong đủ 30 giây để toàn bộ điện tích dư trong các tụ điện được xả hết. Sau đó, hãy cắm lại thật chặt nhé.\n
- **Sarah (Nữ / Khách hàng):** (Sau 30 giây) Được rồi, tôi vừa cắm lại rồi. Các đèn đang chuyển từ đỏ, vàng cam và giờ đã chuyển sang màu xanh lam sáng ổn định.\n
- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Đèn xanh lam ổn định có nghĩa là kết nối cáp quang tốc độ cao đã đồng bộ chuẩn xác. Tôi cũng nhận thấy trên màn hình chẩn đoán rằng modem của cô trước đó chạy trên kênh 2.4 GHz bị nghẽn sóng. Tôi vừa chuyển từ xa mạng chính của cô sang băng tần 5 GHz, băng tần này ít bị nhiễu sóng hơn rất nhiều.\n
- **Sarah (Nữ / Khách hàng):** Để tôi thử ngay trên máy tính xách tay nhé. Tuyệt quá, bài kiểm tra tốc độ đạt tới 95 Mbps và cuộc gọi video họp trực tuyến của tôi đã kết nối lại ngay lập tức!\n
- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Thật là tin tuyệt vời. Nếu kết nối lại chập chờn trong 48 giờ tới, phiếu hỗ trợ của cô vẫn được mở và chúng tôi sẽ cử kỹ thuật viên đến tận nhà kiểm tra miễn phí.\n
- **Sarah (Nữ / Khách hàng):** Anh đã giúp đỡ tôi vô cùng nhiệt tình, Daniel. Cảm ơn anh rất nhiều vì đã xử lý nhanh chóng như vậy!""",
        "keyVocab": [
            { "word": "troubleshoot", "ipa": "/ˈtrʌb.əl.ʃuːt/", "meaning": "khắc phục sự cố kỹ thuật" },
            { "word": "intermittently", "ipa": "/ˌɪn.t̬ɚˈmɪt.ənt.li/", "meaning": "chập chờn, ngắt quãng lúc có lúc không" },
            { "word": "power cycle", "ipa": "/ˈpaʊ.ɚ ˌsaɪ.kəl/", "meaning": "khởi động lại thiết bị bằng cách tắt bật nguồn" },
            { "word": "interference", "ipa": "/ˌɪn.t̬ɚˈfɪr.əns/", "meaning": "sự can nhiễu sóng tín hiệu" },
            { "word": "dispatch", "ipa": "/dɪˈspætʃ/", "meaning": "điều phối, cử nhân viên đi làm nhiệm vụ" }
        ],
        "questions": [
            {
                "id": "q-30-1",
                "question": "What primary problem prompted Sarah to call tech support?",
                "options": [
                    "A. Her computer screen was completely cracked.",
                    "B. Her Wi-Fi disconnected repeatedly every twenty minutes while working from home.",
                    "C. She forgot her email password.",
                    "D. Her printer ran out of black ink."
                ],
                "answerIndex": 1,
                "explanation": "Sarah cho biết: 'my Wi-Fi keeps disconnecting every twenty minutes, which makes working from home impossible'."
            },
            {
                "id": "q-30-2",
                "question": "Why did Daniel ask Sarah to leave the modem unplugged for thirty full seconds?",
                "options": [
                    "A. To allow the plastic casing to cool down from the sun.",
                    "B. To allow all residual electrical charge in internal capacitors to dissipate fully.",
                    "C. To give himself enough time to eat his lunch.",
                    "D. Because company rules forbid faster restarts."
                ],
                "answerIndex": 1,
                "explanation": "Daniel giải thích: 'allow all residual electrical charge in the capacitors to dissipate'."
            },
            {
                "id": "q-30-3",
                "question": "What adjustment did Daniel make remotely to improve Sarah's Wi-Fi stability?",
                "options": [
                    "A. He doubled her monthly bill without warning.",
                    "B. He switched her primary network from the crowded 2.4 GHz channel to the 5 GHz band.",
                    "C. He turned off the neighborhood cell phone tower.",
                    "D. He instructed her to buy a brand new television."
                ],
                "answerIndex": 1,
                "explanation": "Daniel cho biết: 'I have just remotely switched your primary network to the 5 GHz band, which offers significantly less interference'."
            },
            {
                "id": "q-30-4",
                "question": "What guarantee did Daniel provide in case the connection drops again within forty-eight hours?",
                "options": [
                    "A. Sarah will have to buy an entirely new contract.",
                    "B. A field technician will be dispatched at no charge.",
                    "C. The company will cancel her account immediately.",
                    "D. She will receive a twenty percent discount on grocery stores."
                ],
                "answerIndex": 1,
                "explanation": "Daniel đảm bảo: 'If the connection drops again over the next forty-eight hours... we will dispatch a field technician at no charge'."
            }
        ]
    },

    # ---------------- MODULE 31 ----------------
    {
        "id": "read-31",
        "title": "Effective Strategies for Learning a Second Language",
        "type": "passage",
        "topic": "Học tập & Kỹ năng",
        "level": "B1 - B2",
        "summary": "Bài đọc tổng hợp các phương pháp khoa học giúp người học tiếp thu ngoại ngữ hiệu quả: lặp lại ngắt quãng, tạo môi trường đắm chìm và không sợ mắc lỗi.",
        "content": """Acquiring a foreign language as an adult is frequently perceived as a daunting and tedious endeavor. Traditional classroom environments often emphasize rote memorization of grammatical rules, conjugation tables, and isolated vocabulary lists. Unfortunately, this rigid pedagogical method frequently results in students who can score high marks on written examinations but remain paralyzed with anxiety when attempting to hold a spontaneous conversation with native speakers. Modern cognitive neuroscience demonstrates that practical fluency requires a far more dynamic approach.\n\nA cornerstone of rapid vocabulary acquisition is spaced repetition systems (SRS). Human memory naturally decays along a predictable forgetting curve. If a newly learned word is reviewed immediately before the brain forgets it, neural pathways are reinforced and the memory is transferred into long-term storage. Rather than cramming hundreds of words the night before an exam, spending just fifteen minutes each day reviewing digital flashcards with intelligent spaced intervals achieves vastly superior retention with minimal mental fatigue.\n\nFurthermore, creating an immersive linguistic environment at home is essential for developing intuitive listening comprehension. Language learners do not need to purchase expensive plane tickets to immerse themselves in English. By switching smartphone operating systems to English, listening to conversational podcasts during daily commutes, and watching movies with English subtitles, learners continuously train their ears to recognize natural cadence, contractions, and authentic slang in meaningful contexts.\n\nAbove all, overcoming the fear of making mistakes is the single most critical psychological barrier to fluency. Language is primarily an instrument for human connection, not a performance test of grammatical perfection. Native speakers appreciate genuine communicative effort and rarely judge minor prepositions or tense slips. By embracing mistakes as valuable feedback rather than embarrassing failures, learners unlock confidence and achieve communicative fluency far more rapidly.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Việc học một ngoại ngữ khi đã là người trưởng thành thường bị xem là một nỗ lực đầy nản lòng và tẻ nhạt. Môi trường lớp học truyền thống thường nhấn mạnh vào việc học vẹt các quy tắc ngữ pháp, bảng chia động từ và danh sách từ vựng rời rạc. Thật không may, phương pháp sư phạm cứng nhắc này thường tạo ra những học viên có thể đạt điểm cao trong các bài thi viết nhưng lại bị tê liệt vì lo lắng khi cố gắng trò chuyện tự nhiên với người bản xứ. Khoa học thần kinh nhận thức hiện đại chứng minh rằng sự lưu loát thực tế đòi hỏi một cách tiếp cận năng động hơn rất nhiều.\n\nMột nền tảng của việc tiếp thu từ vựng nhanh chóng là hệ thống lặp lại ngắt quãng (SRS). Trí nhớ con người tự nhiên suy giảm theo một đường cong lãng quên có thể dự đoán được. Nếu một từ mới học được ôn lại ngay trước khi não bộ chuẩn bị quên nó, các liên kết nơ-ron sẽ được củng cố và ký ức được chuyển vào bộ nhớ dài hạn. Thay vì nhồi nhét hàng trăm từ vào đêm trước kỳ thi, chỉ cần dành 15 phút mỗi ngày để ôn lại flashcard kỹ thuật số với các khoảng thời gian ngắt quãng thông minh sẽ đạt được khả năng ghi nhớ vượt trội với mức độ mệt mỏi tinh thần tối thiểu.\n\nHơn nữa, việc tạo ra một môi trường ngôn ngữ đắm chìm ngay tại nhà là điều cần thiết để phát triển khả năng nghe hiểu theo trực giác. Người học không cần phải mua vé máy bay đắt đỏ để có thể đắm chìm trong tiếng Anh. Bằng cách chuyển ngôn ngữ hệ điều hành điện thoại sang tiếng Anh, nghe podcast hội thoại trong khi đi làm hàng ngày và xem phim với phụ đề tiếng Anh, người học sẽ liên tục rèn luyện đôi tai nhận biết nhịp điệu tự nhiên, các từ rút gọn và tiếng lóng chân thực trong các ngữ cảnh có ý nghĩa.\n\nTrên hết, việc vượt qua nỗi sợ mắc lỗi chính là rào cản tâm lý quan trọng nhất trên con đường chinh phục sự lưu loát. Ngôn ngữ trước hết là một công cụ để kết nối giữa con người với nhau, chứ không phải một bài kiểm tra biểu diễn sự hoàn hảo về ngữ pháp. Người bản xứ trân trọng sự nỗ lực giao tiếp chân thành và hiếm khi để ý những lỗi nhỏ về giới từ hay thì động từ. Bằng cách đón nhận lỗi sai như những phản hồi quý giá thay vì những thất bại đáng xấu hổ, người học sẽ mở khóa sự tự tin và đạt được sự lưu loát trong giao tiếp nhanh hơn rất nhiều.""",
        "keyVocab": [
            { "word": "daunting", "ipa": "/ˈdɑːn.t̬ɪŋ/", "meaning": "đầy thử thách, làm nản lòng" },
            { "word": "rote memorization", "ipa": "/roʊt ˌmem.ə.rəˈzeɪ.ʃən/", "meaning": "sự học vẹt, học thuộc lòng máy móc" },
            { "word": "spaced repetition", "ipa": "/speɪst ˌrep.əˈtɪʃ.ən/", "meaning": "phương pháp lặp lại ngắt quãng (khoa học ghi nhớ)" },
            { "word": "immersion", "ipa": "/ɪˈmɝː.ʃən/", "meaning": "sự đắm chìm, bao quanh hoàn toàn bằng ngôn ngữ" },
            { "word": "fluency", "ipa": "/ˈfluː.ən.si/", "meaning": "sự trôi chảy, lưu loát" }
        ],
        "questions": [
            {
                "id": "q-31-1",
                "question": "What shortcoming of traditional classroom language teaching does the passage criticize?",
                "options": [
                    "A. Providing too many free textbooks.",
                    "B. Focusing heavily on rote grammar rules, leaving students anxious when speaking spontaneously.",
                    "C. Forcing students to travel abroad every semester.",
                    "D. Teaching only conversational slang without reading books."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 phân tích: 'Traditional classroom environments often emphasize rote memorization... students score high marks on written exams but remain paralyzed with anxiety when attempting to hold spontaneous conversation'."
            },
            {
                "id": "q-31-2",
                "question": "How does spaced repetition systems (SRS) improve vocabulary retention?",
                "options": [
                    "A. By reviewing words right before the brain forgets them, strengthening neural pathways into long-term memory.",
                    "B. By forcing students to write each word five hundred times in a notebook.",
                    "C. By deleting difficult words permanently from study lists.",
                    "D. By testing students only once a year."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 2 chỉ ra: 'If a newly learned word is reviewed immediately before the brain forgets it, neural pathways are reinforced and the memory is transferred into long-term storage'."
            },
            {
                "id": "q-31-3",
                "question": "What is an accessible way to create an immersion environment at home without traveling?",
                "options": [
                    "A. Buying foreign furniture for the living room.",
                    "B. Switching phone settings to English, listening to podcasts, and watching movies with subtitles.",
                    "C. Refusing to talk to anyone in your family.",
                    "D. Memorizing a paper dictionary from page one to the end."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 gợi ý: 'switching smartphone operating systems to English, listening to conversational podcasts... and watching movies with English subtitles'."
            },
            {
                "id": "q-31-4",
                "question": "According to the passage, what is the most critical psychological barrier to language fluency?",
                "options": [
                    "A. The high cost of smartphone apps.",
                    "B. The fear of making mistakes.",
                    "C. Not having a university degree in linguistics.",
                    "D. Having an introverted personality."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 4 nhấn mạnh: 'overcoming the fear of making mistakes is the single most critical psychological barrier to fluency'."
            }
        ]
    },

    # ---------------- MODULE 32 ----------------
    {
        "id": "read-32",
        "title": "Renting an Apartment: Lease Agreement & Utilities",
        "type": "conversation",
        "topic": "Đời sống & Nhà ở",
        "level": "B1 - B2",
        "summary": "Thương thảo hợp đồng thuê nhà giữa chủ nhà và người thuê: Thời hạn hợp đồng, tiền đặt cọc, chi phí tiện ích và quy định nuôi thú cưng.",
        "content": [
            { "speaker": "Richard (Male / Landlord)", "text": "Good afternoon, Olivia. Thank you for coming back for a second viewing of apartment 4B. What are your impressions after seeing the space during daylight?" },
            { "speaker": "Olivia (Female / Tenant)", "text": "Good afternoon, Mr. Richard. The natural light in the living room is wonderful, and the kitchen appliances look virtually brand new. I am definitely interested in leasing the apartment." },
            { "speaker": "Richard (Male / Landlord)", "text": "I am delighted to hear that. As mentioned earlier, our standard lease term is twelve months, beginning on the first of next month. The monthly rent is twelve hundred dollars, payable on the first day of each month." },
            { "speaker": "Olivia (Female / Tenant)", "text": "That fits my budget well. What are the upfront move-in costs, and what does the security deposit cover?" },
            { "speaker": "Richard (Male / Landlord)", "text": "Upon signing the lease, we require the first month's rent plus a security deposit equivalent to one month's rent. The security deposit is fully refundable at the end of the tenancy, provided there is no structural damage beyond standard wear and tear." },
            { "speaker": "Olivia (Female / Tenant)", "text": "That is completely fair. Are utility bills such as high-speed internet, water, and electricity included in the base rent?" },
            { "speaker": "Richard (Male / Landlord)", "text": "Water, trash collection, and building maintenance are included. However, electricity, gas for cooking, and fiber internet are billed separately in your own name." },
            { "speaker": "Olivia (Female / Tenant)", "text": "Good to know. Also, I have a small domestic cat who is quiet and well-trained. What is your policy regarding pets?" },
            { "speaker": "Richard (Male / Landlord)", "text": "We welcome cats and small dogs under fifteen kilograms. We just ask for a one-time non-refundable pet sanitation deposit of one hundred and fifty dollars." },
            { "speaker": "Olivia (Female / Tenant)", "text": "That sounds very reasonable. What documents do you need from me to proceed with the tenancy application?" },
            { "speaker": "Richard (Male / Landlord)", "text": "Please provide proof of employment, two recent pay stubs, and a copy of your government ID. Once approved, we can sign the lease electronically tomorrow!" }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Richard (Nam / Chủ nhà):** Chào buổi chiều, Olivia. Cảm ơn cô đã quay lại xem căn hộ 4B lần thứ hai. Cảm nhận của cô thế nào sau khi thấy không gian vào ban ngày?\n
- **Olivia (Nữ / Người thuê nhà):** Chào buổi chiều, chú Richard. Ánh sáng tự nhiên trong phòng khách rất tuyệt vời, và các thiết bị nhà bếp trông gần như mới tinh. Cháu chắc chắn rất muốn thuê căn hộ này ạ.\n
- **Richard (Nam / Chủ nhà):** Tôi rất mừng khi nghe điều đó. Như đã trao đổi trước đây, thời hạn hợp đồng tiêu chuẩn là 12 tháng, bắt đầu vào ngày mùng 1 tháng sau. Giá thuê hàng tháng là 1.200 đô la, thanh toán vào ngày đầu tiên của mỗi tháng.\n
- **Olivia (Nữ / Người thuê nhà):** Mức giá đó rất phù hợp với ngân sách của cháu. Các chi phí ban đầu khi chuyển vào là gì, và khoản tiền đặt cọc đảm bảo bao gồm những gì ạ?\n
- **Richard (Nam / Chủ nhà):** Khi ký hợp đồng, bên tôi yêu cầu thanh toán tiền thuê tháng đầu tiên cộng với tiền cọc tương đương một tháng tiền nhà. Tiền đặt cọc sẽ được hoàn trả toàn bộ khi hết hạn hợp đồng thuê, với điều kiện căn hộ không bị hư hỏng kết cấu vượt quá mức hao mòn thông thường.\n
- **Olivia (Nữ / Người thuê nhà):** Dạ như vậy rất hợp lý. Các hóa đơn tiện ích như internet tốc độ cao, tiền nước và tiền điện đã bao gồm trong giá thuê gốc chưa ạ?\n
- **Richard (Nam / Chủ nhà):** Tiền nước, phí thu gom rác và phí bảo trì tòa nhà đã được bao gồm. Tuy nhiên, tiền điện, gas nấu ăn và internet cáp quang sẽ tính riêng dưới tên của cô.\n
- **Olivia (Nữ / Người thuê nhà):** Dạ cháu hiểu rồi. Thêm nữa, cháu có nuôi một bé mèo ta nhỏ rất ngoan và sạch sẽ. Quy định của tòa nhà về thú cưng như thế nào ạ?\n
- **Richard (Nam / Chủ nhà):** Tòa nhà hoan nghênh mèo và chó nhỏ dưới 15 kg. Chúng tôi chỉ thu một khoản phí vệ sinh khử khuẩn thú cưng một lần không hoàn lại là 150 đô la.\n
- **Olivia (Nữ / Người thuê nhà):** Dạ rất hợp lý ạ. Cháu cần cung cấp những giấy tờ gì để hoàn tất thủ tục đăng ký thuê nhà ạ?\n
- **Richard (Nam / Chủ nhà):** Cô vui lòng cung cấp giấy xác nhận việc làm, hai phiếu lương gần nhất và bản sao giấy tờ tùy thân. Khi hồ sơ được duyệt, chúng ta có thể ký hợp đồng điện tử ngay ngày mai!""",
        "keyVocab": [
            { "word": "lease agreement", "ipa": "/liːs əˈɡriː.mənt/", "meaning": "hợp đồng cho thuê nhà" },
            { "word": "security deposit", "ipa": "/səˈkjʊr.ə.t̬i dɪˌpɑː.zɪt/", "meaning": "tiền đặt cọc bảo đảm tài sản" },
            { "word": "wear and tear", "ipa": "/ˌwer ən ˈter/", "meaning": "sự hao mòn tự nhiên theo thời gian" },
            { "word": "utilities", "ipa": "/juːˈtɪl.ə.t̬iz/", "meaning": "các dịch vụ tiện ích thiết yếu (điện, nước, gas, internet)" },
            { "word": "refundable", "ipa": "/rɪˈfʌn.də.bəl/", "meaning": "có thể được hoàn lại tiền" }
        ],
        "questions": [
            {
                "id": "q-32-1",
                "question": "What is the standard lease term and monthly rent for apartment 4B?",
                "options": [
                    "A. Six months at eight hundred dollars per month.",
                    "B. Twelve months at twelve hundred dollars per month.",
                    "C. Two years at two thousand dollars per month.",
                    "D. One month trial at no cost."
                ],
                "answerIndex": 1,
                "explanation": "Richard nêu rõ: 'our standard lease term is twelve months... The monthly rent is twelve hundred dollars'."
            },
            {
                "id": "q-32-2",
                "question": "Under what condition will Olivia receive her full security deposit back?",
                "options": [
                    "A. Only if she buys all the apartment furniture.",
                    "B. Provided there is no structural damage beyond standard wear and tear.",
                    "C. If she agrees to repaint the entire building herself.",
                    "D. Security deposits are non-refundable under all circumstances."
                ],
                "answerIndex": 1,
                "explanation": "Richard giải thích: 'fully refundable at the end of the tenancy, provided there is no structural damage beyond standard wear and tear'."
            },
            {
                "id": "q-32-3",
                "question": "Which utilities are already included in the base rent?",
                "options": [
                    "A. Electricity and private international phone lines.",
                    "B. Water, trash collection, and building maintenance.",
                    "C. Daily maid service and dry cleaning.",
                    "D. High-speed gaming internet and premium television."
                ],
                "answerIndex": 1,
                "explanation": "Richard chỉ rõ: 'Water, trash collection, and building maintenance are included'."
            },
            {
                "id": "q-32-4",
                "question": "What is the landlord's policy regarding Olivia's pet cat?",
                "options": [
                    "A. Cats are strictly prohibited under municipal housing laws.",
                    "B. Cats are allowed with a one-time non-refundable pet sanitation deposit of $150.",
                    "C. Olivia must pay double rent every single month.",
                    "D. The cat must stay on the balcony at all times."
                ],
                "answerIndex": 1,
                "explanation": "Richard giải thích: 'We welcome cats and small dogs under fifteen kilograms. We just ask for a one-time non-refundable pet sanitation deposit of one hundred and fifty dollars'."
            }
        ]
    },

    # ---------------- MODULE 33 ----------------
    {
        "id": "read-33",
        "title": "The Rise of E-Commerce and Digital Payment Habits",
        "type": "passage",
        "topic": "Kinh tế & Xu hướng",
        "level": "B1 - B2",
        "summary": "Bài đọc phân tích sự bùng nổ của mua sắm trực tuyến, các ứng dụng ví điện tử và sự thay đổi trong hành vi tiêu dùng thời đại số.",
        "content": """The retail landscape has experienced an unprecedented revolution over the past two decades. Before the digital era, shopping was an inherently physical activity requiring consumers to travel to brick-and-mortar storefronts, wait in long cashier lines, and carry physical cash or paper checkbooks. Today, the ubiquity of smartphones and secure e-commerce platforms has transformed commerce into an instantaneous, frictionless experience accessible from anywhere with an internet connection.\n\nA fundamental catalyst of this commercial shift is the rapid adoption of digital wallets and contactless payment systems. Mobile applications like Apple Pay, Google Wallet, and regional digital payment services enable shoppers to finalize transactions with a simple fingerprint scan or facial recognition tap. For consumers, digital transactions offer speed, detailed automated expense tracking, and valuable cashback reward incentives. For merchants, eliminating paper currency reduces register theft, accelerates checkout throughput, and simplifies automated inventory reconciliation.\n\nFurthermore, artificial intelligence has fundamentally transformed digital product discovery. Modern e-commerce algorithms analyze previous browsing history, purchase frequency, and consumer demographic data to deliver personalized product recommendations. Rather than searching through endless catalogs, shoppers are presented with curated suggestions tailored precisely to their tastes. Combined with flexible return policies and expedited same-day delivery logistics, online shopping now rivals—and often exceeds—the convenience of traditional physical retail.\n\nHowever, this seamless purchasing convenience introduces new challenges. Financial psychologists caution that when physical currency is absent from transactions, the psychological \"pain of paying\" is diminished, making consumers significantly more vulnerable to impulsive spending. Furthermore, digital payment ecosystems require robust cybersecurity safeguards to defend against identity theft and fraudulent transactions. Balancing technological convenience with personal financial discipline remains essential in our increasingly cashless society.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Bối cảnh ngành bán lẻ đã trải qua một cuộc cách mạng chưa từng có trong hai thập kỷ qua. Trước kỷ nguyên số, mua sắm vốn dĩ là một hoạt động thể chất đòi hỏi người tiêu dùng phải di chuyển đến các cửa hàng vật lý truyền thống, xếp hàng dài chờ đợi thanh toán và mang theo tiền mặt hoặc sổ séc giấy. Ngày nay, sự phổ biến của điện thoại thông minh và các nền tảng thương mại điện tử bảo mật đã biến thương mại thành một trải nghiệm tức thì, mượt mà và có thể tiếp cận từ bất kỳ đâu chỉ cần có kết nối internet.\n\nMột chất xúc tác nền tảng của sự chuyển đổi thương mại này là việc áp dụng nhanh chóng các ví kỹ thuật số và hệ thống thanh toán không tiếp xúc. Các ứng dụng di động như Apple Pay, Google Wallet và các dịch vụ thanh toán kỹ thuật số khu vực cho phép người mua sắm hoàn tất giao dịch chỉ bằng một cái chạm quét vân tay hoặc nhận diện khuôn mặt. Đối với người tiêu dùng, giao dịch kỹ thuật số mang lại tốc độ, khả năng theo dõi chi tiêu tự động chi tiết và các ưu đãi hoàn tiền hấp dẫn. Đối với người bán, việc loại bỏ tiền giấy giúp giảm nguy cơ trộm cắp tại quầy thu ngân, tăng tốc độ thanh toán và đơn giản hóa việc đối soát hàng tồn kho tự động.\n\nHơn nữa, trí tuệ nhân tạo đã làm thay đổi căn bản cách khám phá sản phẩm kỹ thuật số. Các thuật toán thương mại điện tử hiện đại phân tích lịch sử duyệt web trước đó, tần suất mua hàng và dữ liệu nhân khẩu học của người tiêu dùng để đưa ra các đề xuất sản phẩm được cá nhân hóa. Thay vì phải tìm kiếm qua các danh mục vô tận, người mua sắm được hiển thị các gợi ý chọn lọc phù hợp chính xác với sở thích của họ. Kết hợp với chính sách đổi trả linh hoạt và dịch vụ hậu cần giao hàng nhanh trong ngày, mua sắm trực tuyến hiện nay cạnh tranh sòng phẳng—và thường vượt trội—về sự tiện lợi so với bán lẻ truyền thống.\n\nTuy nhiên, sự tiện lợi liền mạch này cũng mang đến những thách thức mới. Các nhà tâm lý học tài chính cảnh báo rằng khi tiền mặt vật lý vắng bóng trong các giao dịch, cảm giác tâm lý \"xót tiền khi chi trả\" sẽ giảm đi, khiến người tiêu dùng dễ bị tổn thương hơn trước những chi tiêu bốc đồng. Hơn nữa, các hệ sinh thái thanh toán kỹ thuật số đòi hỏi các biện pháp bảo vệ an ninh mạng vững chắc để chống lại việc đánh cắp danh tính và các giao dịch lừa đảo. Cân bằng giữa sự tiện lợi công nghệ với kỷ luật tài chính cá nhân vẫn là điều thiết yếu trong xã hội ngày càng không dùng tiền mặt của chúng ta.""",
        "keyVocab": [
            { "word": "brick-and-mortar", "ipa": "/ˌbrɪk ən ˈmɔːr.t̬ɚ/", "meaning": "cửa hàng truyền thống có địa điểm vật lý thực tế" },
            { "word": "frictionless", "ipa": "/ˈfrɪk.ʃən.ləs/", "meaning": "mượt mà, không gặp trở ngại hay ma sát" },
            { "word": "cashback incentive", "ipa": "/ˈkæʃ.bæk ɪnˈsen.t̬ɪv/", "meaning": "ưu đãi hoàn tiền kích thích mua sắm" },
            { "word": "curated", "ipa": "/kjʊˈreɪ.t̬ɪd/", "meaning": "được tuyển chọn, chắt lọc kỹ lưỡng" },
            { "word": "cashless society", "ipa": "/ˈkæʃ.ləs səˈsaɪ.ə.t̬i/", "meaning": "xã hội không dùng tiền mặt" }
        ],
        "questions": [
            {
                "id": "q-33-1",
                "question": "What technological tools have served as primary catalysts for the digital commerce shift?",
                "options": [
                    "A. Paper checkbooks and mechanical cash registers.",
                    "B. Mobile digital wallets and contactless payment systems.",
                    "C. Traditional post office money orders.",
                    "D. Coin sorting machines in banks."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 nêu rõ: 'A fundamental catalyst of this commercial shift is the rapid adoption of digital wallets and contactless payment systems'."
            },
            {
                "id": "q-33-2",
                "question": "How does artificial intelligence improve the online shopping experience for consumers?",
                "options": [
                    "A. By requiring customers to pass a math exam before buying items.",
                    "B. By generating random fake prices every hour.",
                    "C. By analyzing browsing history and purchasing habits to provide personalized product recommendations.",
                    "D. By permanently disabling product returns."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 3 giải thích: 'Modern e-commerce algorithms analyze previous browsing history... to deliver personalized product recommendations'."
            },
            {
                "id": "q-33-3",
                "question": "According to financial psychologists, what unintended risk arises from frictionless digital spending?",
                "options": [
                    "A. The psychological \"pain of paying\" decreases, making consumers more prone to impulsive overspending.",
                    "B. Mobile phones will stop charging batteries.",
                    "C. People will forget how to count paper banknotes.",
                    "D. Supermarkets will refuse to sell food."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 4 cảnh báo: 'when physical currency is absent from transactions, the psychological \"pain of paying\" is diminished, making consumers significantly more vulnerable to impulsive spending'."
            },
            {
                "id": "q-33-4",
                "question": "What benefit do digital payments provide to business merchants?",
                "options": [
                    "A. They make stores exempt from paying electricity bills.",
                    "B. They eliminate register theft, speed up checkout times, and simplify inventory reconciliation.",
                    "C. They allow stores to operate without any employees.",
                    "D. They guarantee that no product will ever break."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 chỉ ra: 'eliminating paper currency reduces register theft, accelerates checkout throughput, and simplifies automated inventory reconciliation'."
            }
        ]
    },

    # ---------------- MODULE 34 ----------------
    {
        "id": "read-34",
        "title": "Planning a Company Team-Building Retreat",
        "type": "conversation",
        "topic": "Công sở & Sự kiện",
        "level": "B1 - B2",
        "summary": "Cuộc thảo luận lập kế hoạch dã ngoại gắn kết nhân viên giữa Trưởng phòng Nhân sự và Chuyên viên tổ chức sự kiện chuyên nghiệp.",
        "content": [
            { "speaker": "Brandon (Male / HR Manager)", "text": "Good morning, Clara. Thank you for meeting with me. Our leadership team wants to organize a two-day team-building retreat for our forty employees next month." },
            { "speaker": "Clara (Female / Event Planner)", "text": "Good morning, Brandon! That is fantastic. Team retreats are powerful tools for boosting morale and strengthening interdepartmental relationships. What primary objectives does leadership have in mind?" },
            { "speaker": "Brandon (Male / HR Manager)", "text": "Our engineering and marketing teams have been working remotely for over a year. We want a balanced itinerary that blends collaborative problem-solving workshops with relaxing outdoor activities where people can connect informally." },
            { "speaker": "Clara (Female / Event Planner)", "text": "Understood. I would recommend the Pine Valley Eco-Resort, located ninety minutes outside the city. It features modern conference halls equipped with audiovisual technology, alongside forest hiking trails and an outdoor barbecue pavilion." },
            { "speaker": "Brandon (Male / HR Manager)", "text": "That location sounds ideal. How do you propose structuring the agenda across the two days?" },
            { "speaker": "Clara (Female / Event Planner)", "text": "On Friday morning, we could hold an interactive company roadmap session followed by lunch. In the afternoon, we can conduct an outdoor scavenger hunt that requires cross-functional teamwork. The evening would be reserved for a casual campfire dinner." },
            { "speaker": "Brandon (Male / HR Manager)", "text": "I really like that sequence. What about Saturday morning?" },
            { "speaker": "Clara (Female / Event Planner)", "text": "Saturday morning can feature optional wellness workshops like morning yoga or a guided nature walk, followed by an open feedback retrospective before heading home after lunch." },
            { "speaker": "Brandon (Male / HR Manager)", "text": "Excellent. We have several team members with dietary restrictions—vegetarian, gluten-free, and halal. Can the resort cater to those needs?" },
            { "speaker": "Clara (Female / Event Planner)", "text": "Absolutely. The catering team specializes in customized dietary menus with labeled stations to prevent any cross-contact." },
            { "speaker": "Brandon (Male / HR Manager)", "text": "Terrific! Please send me a comprehensive cost breakdown and formal proposal by Thursday so I can present it to our financial director." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Brandon (Nam / Trưởng phòng Nhân sự):** Chào buổi sáng, Clara. Cảm ơn cô đã dành thời gian gặp tôi. Ban lãnh đạo công ty chúng tôi muốn tổ chức một chuyến dã ngoại gắn kết đội ngũ 2 ngày cho 40 nhân viên vào tháng tới.\n
- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Chào buổi sáng, anh Brandon! Thật tuyệt vời. Những chuyến dã ngoại đội ngũ là công cụ đắc lực để nâng cao tinh thần làm việc và thắt chặt mối quan hệ giữa các phòng ban. Ban lãnh đạo đang hướng tới những mục tiêu chính nào vậy anh?\n
- **Brandon (Nam / Trưởng phòng Nhân sự):** Đội ngũ kỹ thuật và tiếp thị của chúng tôi đã làm việc từ xa hơn một năm nay. Chúng tôi muốn có một lịch trình cân bằng, kết hợp giữa các buổi hội thảo giải quyết vấn đề mang tính hợp tác với các hoạt động thư giãn ngoài trời để mọi người có thể kết nối thoải mái và thân mật.\n
- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Tôi hiểu rồi. Tôi xin gợi ý Khu nghỉ dưỡng sinh thái Pine Valley, cách thành phố khoảng 90 phút đi xe. Nơi đây có các phòng hội nghị hiện đại trang bị đầy đủ công nghệ âm thanh ánh sáng, bên cạnh đó là những con đường mòn đi bộ xuyên rừng và khu vực tiệc nướng ngoài trời.\n
- **Brandon (Nam / Trưởng phòng Nhân sự):** Địa điểm đó nghe rất lý tưởng. Cô đề xuất sắp xếp lịch trình trong hai ngày như thế nào?\n
- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Vào sáng thứ Sáu, chúng ta có thể tổ chức buổi chia sẻ lộ trình phát triển công ty mang tính tương tác, sau đó là bữa trưa. Buổi chiều, chúng ta tổ chức trò chơi truy tìm kho báu ngoài trời đòi hỏi sự phối hợp liên phòng ban. Buổi tối sẽ dành cho bữa tiệc nướng lửa trại ấm cúng.\n
- **Brandon (Nam / Trưởng phòng Nhân sự):** Tôi rất thích trình tự đó. Còn sáng thứ Bảy thì sao cô?\n
- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Sáng thứ Bảy có thể có các hoạt động chăm sóc sức khỏe tự chọn như tập yoga buổi sáng hoặc đi bộ ngắm thiên nhiên có hướng dẫn, tiếp theo là buổi nhìn lại và đóng góp ý kiến cởi mở trước khi khởi hành về sau bữa trưa.\n
- **Brandon (Nam / Trưởng phòng Nhân sự):** Tuyệt vời. Công ty chúng tôi có một số thành viên ăn kiêng—ăn chay, kiêng gluten và đồ ăn chuẩn Halal. Khu nghỉ dưỡng có thể đáp ứng được những thực đơn đó không?\n
- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Chắc chắn được ạ. Đội ngũ ẩm thực ở đó chuyên phục vụ các thực đơn ăn kiêng tùy chỉnh với các quầy đồ ăn được gắn nhãn rõ ràng để tránh tiếp xúc chéo.\n
- **Brandon (Nam / Trưởng phòng Nhân sự):** Quá tốt rồi! Cô vui lòng gửi cho tôi bảng dự toán chi phí chi tiết và bản đề xuất chính thức trước thứ Năm để tôi trình giám đốc tài chính nhé.""",
        "keyVocab": [
            { "word": "retreat", "ipa": "/rɪˈtriːt/", "meaning": "chuyến dã ngoại, kỳ nghỉ dưỡng gắn kết tập thể" },
            { "word": "itinerary", "ipa": "/aɪˈtɪn.ə.rer.i/", "meaning": "lịch trình chi tiết chuyến đi" },
            { "word": "cross-functional", "ipa": "/ˌkrɑːs ˈfʌŋk.ʃən.əl/", "meaning": "liên phòng ban, đa chức năng" },
            { "word": "scavenger hunt", "ipa": "/ˈskæv.ən.dʒɚ hʌnt/", "meaning": "trò chơi truy tìm kho báu/đồ vật theo manh mối" },
            { "word": "retrospective", "ipa": "/ˌret.rəˈspek.tɪv/", "meaning": "buổi họp nhìn lại, đánh giá và rút kinh nghiệm" }
        ],
        "questions": [
            {
                "id": "q-34-1",
                "question": "How many employees will be attending the company retreat next month?",
                "options": [
                    "A. Exactly ten managers.",
                    "B. Forty employees.",
                    "C. Two hundred international delegates.",
                    "D. Only new interns."
                ],
                "answerIndex": 1,
                "explanation": "Brandon nêu rõ: 'organize a two-day team-building retreat for our forty employees next month'."
            },
            {
                "id": "q-34-2",
                "question": "What venue did Clara recommend for the retreat?",
                "options": [
                    "A. An airport transit hotel.",
                    "B. Pine Valley Eco-Resort, located ninety minutes outside the city.",
                    "C. The basement cafeteria of the head office.",
                    "D. A crowded public shopping mall."
                ],
                "answerIndex": 1,
                "explanation": "Clara đề xuất: 'I would recommend the Pine Valley Eco-Resort, located ninety minutes outside the city'."
            },
            {
                "id": "q-34-3",
                "question": "What activity is planned for Friday afternoon to encourage cross-functional collaboration?",
                "options": [
                    "A. A standardized grammar test.",
                    "B. An outdoor scavenger hunt requiring cross-functional teamwork.",
                    "C. Silent meditation in individual rooms.",
                    "D. A competitive video game tournament."
                ],
                "answerIndex": 1,
                "explanation": "Clara gợi ý: 'conduct an outdoor scavenger hunt that requires cross-functional teamwork'."
            },
            {
                "id": "q-34-4",
                "question": "How will the venue accommodate employees with special dietary restrictions?",
                "options": [
                    "A. By asking those employees to bring their own packed lunch from home.",
                    "B. By charging each person fifty dollars extra per meal.",
                    "C. By preparing customized dietary menus with labeled food stations to prevent cross-contact.",
                    "D. By serving fast food burgers to everyone."
                ],
                "answerIndex": 2,
                "explanation": "Clara đảm bảo: 'The catering team specializes in customized dietary menus with labeled stations to prevent any cross-contact'."
            }
        ]
    },

    # ---------------- MODULE 35 ----------------
    {
        "id": "read-35",
        "title": "Daily Stress Management and Mental Well-being",
        "type": "passage",
        "topic": "Tâm lý & Đời sống",
        "level": "B1 - B2",
        "summary": "Bài đọc khám phá cơ chế sinh lý của căng thẳng (stress), tác hại của cortisol dư thừa và các phương pháp phục hồi năng lượng tinh thần hiệu quả.",
        "content": """Stress is an innate evolutionary survival mechanism designed to protect living organisms from acute physical hazards. When primitive ancestors encountered predatory threats, the human brain triggered an immediate physiological reaction known as the \"fight-or-flight\" response. Heart rates surged, blood pressure escalated, and stress hormones like adrenaline and cortisol flooded the bloodstream, temporarily diverting energy away from non-essential systems like digestion and immunity toward muscle activation.\n\nWhile this biological response remains vital for genuine physical crises, modern psychological stressors operate in an entirely different manner. Contemporary challenges—tight workplace deadlines, financial anxieties, and relentless digital notifications—are chronic rather than momentary. When the nervous system remains in a perpetual state of hyper-arousal, sustained elevated cortisol levels disrupt sleep architecture, impair immune defense, and foster chronic fatigue and cardiovascular strain.\n\nFortunately, clinical psychological research highlights several accessible practices that actively deactivate the physiological stress response. One of the most potent interventions is controlled diaphragmatic breathing, particularly the \"box breathing\" technique used by athletes and tactical specialists. By inhaling deeply for four seconds, holding for four, exhaling slowly for four, and pausing for four, the parasympathetic nervous system is stimulated, signaling the heart rate to decelerate and blood pressure to normalize within minutes.\n\nIn addition to conscious breathwork, cultivating regular digital detox intervals and engaging in physical movement in natural environments yield profound cognitive restoration. Spending just twenty minutes walking in an urban park or forest—a practice known in Japan as \"shinrin-yoku\" or forest bathing—significantly lowers salivary cortisol and restores depleted attention spans. Incorporating these intentional restorative rituals into daily routines ensures that individuals navigate modern pressures without compromising their long-term health and mental vitality.""",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Căng thẳng (stress) là một cơ chế sinh tồn tiến hóa bẩm sinh được thiết kế để bảo vệ các sinh vật sống khỏi những mối nguy hiểm thể chất cấp tính. Khi tổ tiên nguyên thủy đối mặt với các loài thú săn mồi đe dọa, bộ não con người lập tức kích hoạt một phản ứng sinh lý được gọi là phản ứng \"chiến đấu hay bỏ chạy\". Nhịp tim tăng vọt, huyết áp tăng cao, và các hormone gây căng thẳng như adrenaline và cortisol tràn vào máu, tạm thời chuyển hướng năng lượng khỏi các hệ thống không thiết yếu như tiêu hóa và miễn dịch để dồn cho sự kích hoạt cơ bắp.\n\nMặc dù phản ứng sinh học này vẫn mang tính sống còn đối với các cuộc khủng hoảng thể chất thực sự, những tác nhân gây căng thẳng tâm lý hiện đại lại hoạt động theo cách hoàn toàn khác. Những thách thức đương đại—hạn chót công việc gấp gáp, nỗi lo tài chính và những thông báo kỹ thuật số không ngừng nghỉ—mang tính chất kinh niên dai dẳng thay vì chỉ diễn ra trong chốc lát. Khi hệ thần kinh duy trì liên tục ở trạng thái kích động cao độ, mức cortisol tăng cao kéo dài sẽ phá vỡ cấu trúc giấc ngủ, làm suy giảm hệ miễn dịch và gây ra tình trạng mệt mỏi mạn tính cùng áp lực cho hệ tim mạch.\n\nMay mắn thay, các nghiên cứu tâm lý học lâm sàng chỉ ra một số phương pháp dễ tiếp cận có thể chủ động vô hiệu hóa phản ứng căng thẳng sinh lý này. Một trong những biện pháp can thiệp hiệu quả nhất là hít thở cơ hoành có kiểm soát, đặc biệt là kỹ thuật \"thở hộp\" được các vận động viên và chuyên gia tác chiến sử dụng. Bằng cách hít sâu trong 4 giây, giữ hơi trong 4 giây, thở ra từ từ trong 4 giây và dừng lại trong 4 giây, hệ thần kinh đối giao cảm sẽ được kích thích, phát tín hiệu cho nhịp tim chậm lại và huyết áp trở về mức bình thường chỉ trong vài phút.\n\nBên cạnh việc thở có ý thức, việc duy trì các khoảng thời gian cai nghiện kỹ thuật số định kỳ và vận động thể chất trong môi trường thiên nhiên mang lại sự phục hồi nhận thức sâu sắc. Chỉ cần dành 20 phút đi dạo trong công viên đô thị hoặc khu rừng—một phương pháp ở Nhật Bản gọi là \"tắm rừng\" (shinrin-yoku)—sẽ làm giảm đáng kể nồng độ cortisol trong nước bọt và phục hồi khả năng chú ý đang bị cạn kiệt. Việc kết hợp những nghi thức phục hồi có chủ đích này vào thói quen hàng ngày sẽ đảm bảo rằng mỗi người có thể vượt qua áp lực hiện đại mà không làm tổn hại đến sức khỏe lâu dài và sức sống tinh thần.""",
        "keyVocab": [
            { "word": "fight-or-flight", "ipa": "/ˌfaɪt ɔːr ˈflaɪt/", "meaning": "phản ứng chiến đấu hay bỏ chạy (phản xạ sinh tồn trước nguy hiểm)" },
            { "word": "chronic", "ipa": "/ˈkrɑː.nɪk/", "meaning": "mạn tính, kéo dài dai dẳng thường xuyên" },
            { "word": "hyper-arousal", "ipa": "/ˌhaɪ.pɚ.əˈraʊ.zəl/", "meaning": "trạng thái kích động, căng thẳng thần kinh tột độ" },
            { "word": "diaphragmatic breathing", "ipa": "/ˌdaɪ.ə.fræɡˈmæt̬.ɪk ˈbriː.ðɪŋ/", "meaning": "phương pháp hít thở sâu bằng cơ hoành (bụng)" },
            { "word": "cognitive restoration", "ipa": "/ˈkɑːɡ.nə.t̬ɪv ˌres.təˈreɪ.ʃən/", "meaning": "sự phục hồi năng lượng và khả năng nhận thức của não bộ" }
        ],
        "questions": [
            {
                "id": "q-35-1",
                "question": "What is the primary evolutionary purpose of the human stress response?",
                "options": [
                    "A. To help students write essays more quickly.",
                    "B. An innate survival mechanism designed to protect organisms from acute physical hazards.",
                    "C. To permanently suppress emotional feelings of love.",
                    "D. To digest heavy meals after midnight."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu rõ: 'an innate evolutionary survival mechanism designed to protect living organisms from acute physical hazards'."
            },
            {
                "id": "q-35-2",
                "question": "What consequence occurs when cortisol levels remain perpetually elevated from modern chronic stressors?",
                "options": [
                    "A. It permanently turns hair bright green.",
                    "B. It disrupts sleep architecture, impairs immune defense, and strains cardiovascular health.",
                    "C. It makes people immune to all future diseases.",
                    "D. It improves eyesight in the dark."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 giải thích: 'sustained elevated cortisol levels disrupt sleep architecture, impair immune defense, and foster chronic fatigue and cardiovascular strain'."
            },
            {
                "id": "q-35-3",
                "question": "How does the \"box breathing\" technique stimulate the parasympathetic nervous system?",
                "options": [
                    "A. By drinking three cups of black espresso in five minutes.",
                    "B. By holding one's breath for three full minutes underwater.",
                    "C. By inhaling for four seconds, holding for four, exhaling for four, and pausing for four seconds.",
                    "D. By sprinting as fast as possible up a steep hill."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 3 mô tả cụ thể: 'inhaling deeply for four seconds, holding for four, exhaling slowly for four, and pausing for four, the parasympathetic nervous system is stimulated'."
            },
            {
                "id": "q-35-4",
                "question": "What proven benefit does twenty minutes of nature walking (\"forest bathing\") provide?",
                "options": [
                    "A. It reduces salivary cortisol and restores depleted attention spans.",
                    "B. It replaces the need to sleep at night.",
                    "C. It guarantees a promotion at work the next morning.",
                    "D. It cures all dental cavities immediately."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 4 nhấn mạnh: 'Spending just twenty minutes walking in an urban park or forest... significantly lowers salivary cortisol and restores depleted attention spans'."
            }
        ]
    },

    # ---------------- MODULE 36 ----------------
    {
        "id": "read-36",
        "title": "Returning an Online Purchase & Customer Service",
        "type": "conversation",
        "topic": "Mua sắm & Dịch vụ",
        "level": "B1 - B2",
        "summary": "Tình huống đổi trả hàng mua qua mạng do giao nhầm cỡ áo và lỗi đường chỉ, cùng quy trình hoàn tiền vào tài khoản gốc.",
        "content": [
            { "speaker": "Liam (Male / Service Representative)", "text": "Thank you for contacting Urban Wardrobe Customer Care. My name is Liam. How can I help you today?" },
            { "speaker": "Emily (Female / Shopper)", "text": "Hello Liam. I recently ordered an autumn wool overcoat, order number UW-93814. I received the parcel yesterday, but there are two significant issues with the item." },
            { "speaker": "Liam (Male / Service Representative)", "text": "I am so sorry to hear that, Ms. Emily. Could you please specify what happened with the shipment?" },
            { "speaker": "Emily (Female / Shopper)", "text": "Firstly, I ordered a medium size in camel brown, but the tag inside the coat indicates it is a large. Secondly, there is loose stitching along the left interior pocket lining." },
            { "speaker": "Liam (Male / Service Representative)", "text": "I sincerely apologize for that warehouse fulfillment error and the defective seam. That certainly does not meet our quality standards. Would you prefer an exchange for the correct size or a full refund to your original payment method?" },
            { "speaker": "Emily (Female / Shopper)", "text": "Since the weather is getting cold, I would love an exchange if you have the camel brown overcoat available in medium." },
            { "speaker": "Liam (Male / Service Representative)", "text": "Let me check our distribution inventory right now. Yes, we have three units in stock in medium. I have just reserved one for you." },
            { "speaker": "Emily (Female / Shopper)", "text": "That is wonderful! Do I need to pay for the return postage of the incorrect coat?" },
            { "speaker": "Liam (Male / Service Representative)", "text": "Not at all. Because this was our error, return shipping is completely complimentary. I have just emailed you a prepaid prepaid return shipping label with a QR code." },
            { "speaker": "Emily (Female / Shopper)", "text": "Do I need to print out the label myself?" },
            { "speaker": "Liam (Male / Service Representative)", "text": "Not necessarily. You can simply show the QR code on your smartphone at any local post office branch, and the clerk will print and affix the shipping label for you. As soon as the carrier scans the parcel, your replacement coat will be dispatched via priority shipping." },
            { "speaker": "Emily (Female / Shopper)", "text": "That is remarkably convenient and reassuring. Thank you so much for your swift resolution, Liam!" },
            { "speaker": "Liam (Male / Service Representative)", "text": "You are very welcome, Emily. Thank you for your patience and for shopping with Urban Wardrobe!" }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Cảm ơn quý khách đã liên hệ với Bộ phận Chăm sóc Khách hàng của Urban Wardrobe. Tôi tên là Liam. Tôi có thể hỗ trợ gì cho quý khách hôm nay ạ?\n
- **Emily (Nữ / Người mua hàng):** Chào Liam. Gần đây tôi có đặt mua một chiếc áo khoác dạ mùa thu, mã đơn hàng là UW-93814. Hôm qua tôi đã nhận được gói hàng, nhưng có hai vấn đề nghiêm trọng với sản phẩm.\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Rất tiếc khi nghe điều đó, cô Emily. Cô có thể cho tôi biết cụ thể đã xảy ra vấn đề gì với đơn hàng không ạ?\n
- **Emily (Nữ / Người mua hàng):** Thứ nhất, tôi đặt cỡ M màu nâu lạc đà, nhưng mác bên trong áo lại ghi cỡ L. Thứ hai, có một đoạn chỉ bị tuột dọc theo lớp lót túi áo bên trái phía trong.\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Tôi thành thật xin lỗi vì sự nhầm lẫn trong khâu đóng gói tại kho và lỗi đường chỉ may đó. Điều này chắc chắn không đúng với tiêu chuẩn chất lượng của chúng tôi. Cô muốn đổi sang đúng cỡ áo hay muốn được hoàn tiền toàn bộ về phương thức thanh toán ban đầu ạ?\n
- **Emily (Nữ / Người mua hàng):** Vì thời tiết đang trở lạnh nên tôi rất muốn đổi hàng nếu bên anh còn chiếc áo khoác màu nâu lạc đà cỡ M.\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Để tôi kiểm tra lượng hàng tồn kho ngay bây giờ nhé. Vâng, chúng tôi còn đúng ba chiếc cỡ M tại kho. Tôi vừa giữ riêng một chiếc cho cô rồi ạ.\n
- **Emily (Nữ / Người mua hàng):** Thật tuyệt vời! Tôi có phải trả phí bưu điện để gửi trả chiếc áo bị giao nhầm không?\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Hoàn toàn không ạ. Vì đây là lỗi từ phía công ty chúng tôi nên phí vận chuyển hoàn trả là hoàn toàn miễn phí. Tôi vừa gửi cho cô một phiếu vận chuyển trả hàng trả trước có kèm mã QR qua email.\n
- **Emily (Nữ / Người mua hàng):** Tôi có cần phải tự in phiếu vận chuyển đó ra không?\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Không nhất thiết đâu ạ. Cô chỉ cần xuất trình mã QR trên điện thoại thông minh tại bất kỳ bưu cục địa phương nào, nhân viên bưu điện sẽ tự in và dán phiếu gửi hàng cho cô. Ngay khi đơn vị vận chuyển quét mã kiện hàng, chiếc áo thay thế của cô sẽ được gửi đi bằng đường chuyển phát hỏa tốc ưu tiên.\n
- **Emily (Nữ / Người mua hàng):** Thật là tiện lợi và yên tâm quá. Cảm ơn anh rất nhiều vì cách xử lý nhanh chóng như vậy, Liam!\n
- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Không có chi, cô Emily. Cảm ơn sự kiên nhẫn của cô và cảm ơn cô đã mua sắm tại Urban Wardrobe!""",
        "keyVocab": [
            { "word": "parcel", "ipa": "/ˈpɑːr.səl/", "meaning": "gói hàng, bưu kiện" },
            { "word": "defective seam", "ipa": "/dɪˈfek.tɪv siːm/", "meaning": "đường may bị lỗi, hỏng" },
            { "word": "fulfillment error", "ipa": "/fʊlˈfɪl.mənt ˈer.ɚ/", "meaning": "lỗi xử lý và đóng gói đơn hàng" },
            { "word": "prepaid label", "ipa": "/ˌpriːˈpeɪd ˈleɪ.bəl/", "meaning": "nhãn gửi hàng đã thanh toán cước trước" },
            { "word": "priority shipping", "ipa": "/praɪˈɔːr.ə.t̬i ˈʃɪp.ɪŋ/", "meaning": "giao hàng hỏa tốc, ưu tiên" }
        ],
        "questions": [
            {
                "id": "q-36-1",
                "question": "What two defects did Emily discover upon receiving her coat?",
                "options": [
                    "A. The coat was dirty and missing all buttons.",
                    "B. The size was large instead of medium, and the pocket lining had loose stitching.",
                    "C. The package was completely empty.",
                    "D. The coat was made of paper instead of wool."
                ],
                "answerIndex": 1,
                "explanation": "Emily giải thích: 'Firstly, I ordered a medium size in camel brown, but the tag inside the coat indicates it is a large. Secondly, there is loose stitching along the left interior pocket lining'."
            },
            {
                "id": "q-36-2",
                "question": "What resolution did Emily choose between an exchange and a refund?",
                "options": [
                    "A. She demanded a full refund in cash.",
                    "B. She chose an exchange for the correct medium size coat.",
                    "C. She decided to keep the large coat without complaining.",
                    "D. She asked for five gift certificates."
                ],
                "answerIndex": 1,
                "explanation": "Emily nói: 'Since the weather is getting cold, I would love an exchange if you have the camel brown overcoat available in medium'."
            },
            {
                "id": "q-36-3",
                "question": "Who pays for the return shipping postage?",
                "options": [
                    "A. Emily must pay thirty dollars at the post office.",
                    "B. The courier driver splits the cost with Emily.",
                    "C. The company covers the return shipping completely with a prepaid label because it was their fulfillment error.",
                    "D. The city government pays the postage."
                ],
                "answerIndex": 2,
                "explanation": "Liam khẳng định: 'Because this was our error, return shipping is completely complimentary. I have just emailed you a prepaid return shipping label'."
            },
            {
                "id": "q-36-4",
                "question": "How can Emily send the return parcel without owning a home printer?",
                "options": [
                    "A. By writing the address on the box with lipstick.",
                    "B. By showing the QR code on her smartphone at the local post office for the clerk to print.",
                    "C. By waiting three weeks for a paper letter.",
                    "D. She must visit the company headquarters in person."
                ],
                "answerIndex": 1,
                "explanation": "Liam hướng dẫn: 'You can simply show the QR code on your smartphone at any local post office branch, and the clerk will print and affix the shipping label for you'."
            }
        ]
    }
]

def main():
    root = Path(__file__).resolve().parent.parent
    reading_file = root / "js" / "reading_data.js"
    
    # Read existing content
    content = reading_file.read_text(encoding="utf-8")
    
    # Extract the original READING_DATA
    # We can load it using node or by parsing JSON/eval
    import subprocess
    cmd = ["node", "-e", "const { READING_DATA } = require('./js/reading_data.js'); console.log(JSON.stringify(READING_DATA));"]
    result = subprocess.run(cmd, cwd=root, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        print("Error executing node:", result.stderr)
        return
        
    existing_lessons = json.loads(result.stdout)
    print(f"Loaded {len(existing_lessons)} existing lessons.")
    
    # Merge new lessons (check if already added)
    existing_ids = {item["id"] for item in existing_lessons}
    added_count = 0
    merged_lessons = list(existing_lessons)
    for lesson in NEW_B1_B2_LESSONS:
        if lesson["id"] not in existing_ids:
            merged_lessons.append(lesson)
            added_count += 1
            
    print(f"Merged {added_count} new B1-B2 lessons. Total now: {len(merged_lessons)}")
    
    # Generate clean JS file
    js_code = "// Bộ dữ liệu 36 bài tập Đọc hiểu (Reading Passages) & Hội thoại (Conversations)\n"
    js_code += "// Phân loại độ khó rõ ràng (B1 - B2 & B2 - C1), kèm trắc nghiệm, giải thích chi tiết và bản dịch song ngữ\n\n"
    js_code += "const READING_DATA = " + json.dumps(merged_lessons, ensure_ascii=False, indent=4) + ";\n\n"
    js_code += "if (typeof module !== 'undefined' && module.exports) {\n"
    js_code += "    module.exports = { READING_DATA };\n"
    js_code += "}\n"
    
    reading_file.write_text(js_code, encoding="utf-8")
    print("Successfully wrote updated js/reading_data.js!")

if __name__ == "__main__":
    main()
