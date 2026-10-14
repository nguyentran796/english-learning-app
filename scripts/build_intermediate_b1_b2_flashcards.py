# -*- coding: utf-8 -*-
"""
Script to generate 270 high-utility Intermediate (B1 - B2) flashcard items
(vocabulary & sentence patterns) and merge them with the existing 502 advanced items.
Total dataset will have 772 items tagged with levels 'B1 - B2' and 'B2 - C1'.
"""

import json
from pathlib import Path

INTERMEDIATE_B1_B2_ITEMS = [
    # ================= 1. CÔNG SỞ & SỰ NGHIỆP (35 items) =================
    {
        "id": "b1-1", "type": "vocab", "level": "B1 - B2", "text": "candidate", "ipa": "/ˈkæn.dɪ.dət/",
        "meaning": "ứng viên, người dự tuyển", "topic": "Công sở & Đàm phán",
        "example": "She is the strongest candidate for the marketing position.",
        "exampleMeaning": "Cô ấy là ứng viên sáng giá nhất cho vị trí tiếp thị.",
        "note": "Đi với for (vị trí/công việc). Danh từ: candidacy.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-2", "type": "vocab", "level": "B1 - B2", "text": "deadline", "ipa": "/ˈded.laɪn/",
        "meaning": "hạn chót hoàn thành", "topic": "Công sở & Đàm phán",
        "example": "We must work together to meet the tight deadline.",
        "exampleMeaning": "Chúng ta phải làm việc cùng nhau để kịp hạn chót gấp rút.",
        "note": "Cụm thường gặp: meet a deadline (kịp hạn), miss a deadline (trễ hạn).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-3", "type": "vocab", "level": "B1 - B2", "text": "presentation", "ipa": "/ˌprez.ənˈteɪ.ʃən/",
        "meaning": "bài thuyết trình, phần trình bày", "topic": "Công sở & Đàm phán",
        "example": "His presentation about the new quarterly budget was very convincing.",
        "exampleMeaning": "Bài thuyết trình của anh ấy về ngân sách quý mới rất thuyết phục.",
        "note": "Động từ: present /prɪˈzent/. Give/make a presentation.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-4", "type": "vocab", "level": "B1 - B2", "text": "feedback", "ipa": "/ˈfiːd.bæk/",
        "meaning": "ý kiến phản hồi, nhận xét đóng góp", "topic": "Công sở & Đàm phán",
        "example": "Constructive feedback helps employees improve their skills.",
        "exampleMeaning": "Phản hồi mang tính xây dựng giúp nhân viên nâng cao kỹ năng.",
        "note": "Danh từ không đếm được. Give feedback / receive feedback.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-5", "type": "vocab", "level": "B1 - B2", "text": "schedule", "ipa": "/ˈskedʒ.uːl/",
        "meaning": "lịch trình, thời gian biểu", "topic": "Công sở & Đàm phán",
        "example": "I will check my schedule and confirm our appointment tomorrow.",
        "exampleMeaning": "Tôi sẽ kiểm tra lịch trình của mình và xác nhận cuộc hẹn vào ngày mai.",
        "note": "Ahead of schedule (sớm hơn lịch), behind schedule (chậm tiến độ).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-6", "type": "vocab", "level": "B1 - B2", "text": "coordinate", "ipa": "/koʊˈɔːr.dən.eɪt/",
        "meaning": "phối hợp, điều phối công việc", "topic": "Công sở & Đàm phán",
        "example": "The manager coordinates daily activities between design and engineering.",
        "exampleMeaning": "Người quản lý điều phối các hoạt động hàng ngày giữa thiết kế và kỹ thuật.",
        "note": "Danh từ: coordination, coordinator.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-7", "type": "vocab", "level": "B1 - B2", "text": "supervise", "ipa": "/ˈsuː.pɚ.vaɪz/",
        "meaning": "giám sát, chỉ đạo cấp dưới", "topic": "Công sở & Đàm phán",
        "example": "She supervises a team of eight customer service representatives.",
        "exampleMeaning": "Cô ấy giám sát một đội ngũ gồm tám nhân viên chăm sóc khách hàng.",
        "note": "Danh từ: supervisor (người giám sát), supervision.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-8", "type": "vocab", "level": "B1 - B2", "text": "colleague", "ipa": "/ˈkɑː.liːɡ/",
        "meaning": "đồng nghiệp", "topic": "Công sở & Đàm phán",
        "example": "I consulted my colleague before sending the formal email.",
        "exampleMeaning": "Tôi đã tham khảo ý kiến đồng nghiệp trước khi gửi email trang trọng.",
        "note": "Đồng nghĩa với coworker nhưng trang trọng hơn.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-9", "type": "vocab", "level": "B1 - B2", "text": "promote", "ipa": "/prəˈmoʊt/",
        "meaning": "thăng chức, thăng tiến / thúc đẩy", "topic": "Công sở & Đàm phán",
        "example": "He was promoted to senior software engineer last month.",
        "exampleMeaning": "Anh ấy đã được thăng chức lên kỹ sư phần mềm cao cấp vào tháng trước.",
        "note": "Be promoted to (vị trí). Danh từ: promotion.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-10", "type": "vocab", "level": "B1 - B2", "text": "resume", "ipa": "/ˈrez.ə.meɪ/",
        "meaning": "hồ sơ xin việc, sơ yếu lý lịch", "topic": "Công sở & Đàm phán",
        "example": "Make sure your resume highlights relevant professional achievements.",
        "exampleMeaning": "Hãy đảm bảo sơ yếu lý lịch nêu bật các thành tựu nghề nghiệp phù hợp.",
        "note": "Phát âm khác động từ resume /rɪˈzuːm/ (tiếp tục lại).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-11", "type": "vocab", "level": "B1 - B2", "text": "procedure", "ipa": "/prəˈsiː.dʒɚ/",
        "meaning": "thủ tục, quy trình thực hiện", "topic": "Công sở & Đàm phán",
        "example": "All staff members must follow the standard security procedure.",
        "exampleMeaning": "Tất cả nhân viên phải tuân theo quy trình bảo mật tiêu chuẩn.",
        "note": "Operating procedure (quy trình vận hành).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-12", "type": "vocab", "level": "B1 - B2", "text": "efficiency", "ipa": "/ɪˈfɪʃ.ən.si/",
        "meaning": "hiệu suất, tính hiệu quả cao", "topic": "Công sở & Đàm phán",
        "example": "Automation tools have greatly improved our operational efficiency.",
        "exampleMeaning": "Các công cụ tự động hóa đã cải thiện đáng kể hiệu suất vận hành.",
        "note": "Tính từ: efficient. Trái nghĩa: inefficiency.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-13", "type": "vocab", "level": "B1 - B2", "text": "requirement", "ipa": "/rɪˈkwaɪr.mənt/",
        "meaning": "yêu cầu, điều kiện tiên quyết", "topic": "Công sở & Đàm phán",
        "example": "Fluency in spoken English is an essential requirement for this job.",
        "exampleMeaning": "Lưu loát tiếng Anh giao tiếp là yêu cầu thiết yếu cho công việc này.",
        "note": "Động từ: require. Meet requirements (đáp ứng yêu cầu).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-14", "type": "vocab", "level": "B1 - B2", "text": "performance", "ipa": "/pɚˈfɔːr.məns/",
        "meaning": "kết quả làm việc, hiệu năng", "topic": "Công sở & Đàm phán",
        "example": "Her outstanding performance earned her an annual bonus.",
        "exampleMeaning": "Kết quả làm việc xuất sắc đã mang lại cho cô ấy khoản tiền thưởng năm.",
        "note": "Performance review (đánh giá hiệu suất làm việc).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-15", "type": "vocab", "level": "B1 - B2", "text": "proposal", "ipa": "/prəˈpoʊ.zəl/",
        "meaning": "bản đề xuất, kế hoạch đề xuất", "topic": "Công sở & Đàm phán",
        "example": "We submitted a comprehensive project proposal to the client.",
        "exampleMeaning": "Chúng tôi đã gửi một bản đề xuất dự án toàn diện tới khách hàng.",
        "note": "Động từ: propose. Submit/approve a proposal.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-16", "type": "sentence", "level": "B1 - B2", "text": "Could you please give me an update on the project status?",
        "ipa": "/kʊd juː pliːz ɡɪv miː ən ˈʌp.deɪt ɑːn ðə ˈprɑː.dʒekt ˈsteɪ.t̬əs/",
        "meaning": "Bạn có thể vui lòng cập nhật tình hình dự án cho tôi được không?", "topic": "Mẫu câu Chuyên nghiệp",
        "example": "Could you please give me an update on the project status before our meeting?",
        "exampleMeaning": "Bạn có thể vui lòng cập nhật tình hình dự án trước cuộc họp của chúng ta không?",
        "note": "Mẫu câu công sở lịch sự khi hỏi tiến độ công việc.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-17", "type": "sentence", "level": "B1 - B2", "text": "I would appreciate it if you could review this document by Friday.",
        "ipa": "/aɪ wʊd əˈpriː.ʃi.eɪt ɪt ɪf juː kʊd rɪˈvjuː ðɪs ˈdɑːk.jə.mənt baɪ ˈfraɪ.deɪ/",
        "meaning": "Tôi sẽ rất cảm kích nếu bạn có thể xem qua tài liệu này trước thứ Sáu.", "topic": "Mẫu câu Chuyên nghiệp",
        "example": "I would appreciate it if you could review this document by Friday morning.",
        "exampleMeaning": "Tôi rất cảm kích nếu bạn xem qua tài liệu này trước sáng thứ Sáu.",
        "note": "Cấu trúc 'I would appreciate it if you could...' thể hiện yêu cầu rất trang nhã.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-18", "type": "sentence", "level": "B1 - B2", "text": "Let us schedule a follow-up call to discuss the details.",
        "ipa": "/let ʌs ˈskedʒ.uːl ə ˈfɑː.loʊ.ʌp kɔːl tə dɪˈskʌs ðə ˈdiː.teɪlz/",
        "meaning": "Chúng ta hãy hẹn một cuộc gọi trao đổi tiếp theo để thảo luận chi tiết.", "topic": "Mẫu câu Chuyên nghiệp",
        "example": "Let us schedule a follow-up call to discuss the contract terms.",
        "exampleMeaning": "Chúng ta hãy hẹn một cuộc gọi trao đổi thêm về các điều khoản hợp đồng.",
        "note": "Follow-up call/meeting: cuộc trao đổi theo dõi tiếp theo.", "status": "new", "dateAdded": "2026-10-14"
    },

    # ================= 2. DU LỊCH & KHÁCH SẠN (35 items) =================
    {
        "id": "b1-19", "type": "vocab", "level": "B1 - B2", "text": "destination", "ipa": "/ˌdes.təˈneɪ.ʃən/",
        "meaning": "điểm đến, nơi dự định tới", "topic": "Du lịch & Khách sạn",
        "example": "Da Nang is a very popular travel destination for international tourists.",
        "exampleMeaning": "Đà Nẵng là điểm đến du lịch rất phổ biến đối với du khách quốc tế.",
        "note": "Tourist destination, holiday destination.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-20", "type": "vocab", "level": "B1 - B2", "text": "itinerary", "ipa": "/aɪˈtɪn.ə.rer.i/",
        "meaning": "lịch trình chi tiết chuyến đi", "topic": "Du lịch & Khách sạn",
        "example": "Our travel agent prepared a seven-day sightseeing itinerary.",
        "exampleMeaning": "Đại lý du lịch đã chuẩn bị một lịch trình tham quan kéo dài bảy ngày.",
        "note": "Trọng âm rơi vào âm tiết thứ hai: /aɪˈtɪn-/. Planned route.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-21", "type": "vocab", "level": "B1 - B2", "text": "accommodation", "ipa": "/əˌkɑː.məˈdeɪ.ʃən/",
        "meaning": "chỗ ở, nơi lưu trú (khách sạn, nhà nghỉ)", "topic": "Du lịch & Khách sạn",
        "example": "Hotel accommodation was included in the total tour package price.",
        "exampleMeaning": "Chỗ ở khách sạn đã được bao gồm trong tổng giá gói tour.",
        "note": "Danh từ không đếm được trong Anh-Mỹ. Book accommodation.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-22", "type": "vocab", "level": "B1 - B2", "text": "departure", "ipa": "/dɪˈpɑːr.tʃɚ/",
        "meaning": "sự khởi hành, giờ xuất phát", "topic": "Du lịch & Khách sạn",
        "example": "Please arrive at the terminal two hours before your scheduled departure.",
        "exampleMeaning": "Vui lòng đến nhà ga hai tiếng trước giờ khởi hành dự kiến.",
        "note": "Trái nghĩa: arrival (đến nơi). Departure gate, departure lounge.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-23", "type": "vocab", "level": "B1 - B2", "text": "boarding pass", "ipa": "/ˈbɔːr.dɪŋ ˌpæs/",
        "meaning": "thẻ lên máy bay / tàu", "topic": "Du lịch & Khách sạn",
        "example": "You must show your passport and boarding pass at security.",
        "exampleMeaning": "Bạn phải xuất trình hộ chiếu và thẻ lên máy bay tại cửa an ninh.",
        "note": "Mobile boarding pass (thẻ điện tử trên điện thoại).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-24", "type": "vocab", "level": "B1 - B2", "text": "passenger", "ipa": "/ˈpæs.ən.dʒɚ/",
        "meaning": "hành khách đi xe, tàu, máy bay", "topic": "Du lịch & Khách sạn",
        "example": "All passengers are requested to fasten their seatbelts.",
        "exampleMeaning": "Tất cả hành khách được yêu cầu thắt dây an toàn.",
        "note": "Passenger seat (ghế hành khách).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-25", "type": "vocab", "level": "B1 - B2", "text": "luggage", "ipa": "/ˈlʌɡ.ɪdʒ/",
        "meaning": "hành lý, vali túi xách", "topic": "Du lịch & Khách sạn",
        "example": "Carry-on luggage must fit in the overhead storage bin.",
        "exampleMeaning": "Hành lý xách tay phải vừa với khoang hành lý phía trên đầu.",
        "note": "Danh từ không đếm được. Đồng nghĩa: baggage.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-26", "type": "vocab", "level": "B1 - B2", "text": "delay", "ipa": "/dɪˈleɪ/",
        "meaning": "sự hoãn lại, chậm trễ", "topic": "Du lịch & Khách sạn",
        "example": "The flight was delayed due to severe thunderstorms.",
        "exampleMeaning": "Chuyến bay đã bị hoãn do dông bão nghiêm trọng.",
        "note": "Vừa là động từ vừa là danh từ. Flight delay.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-27", "type": "vocab", "level": "B1 - B2", "text": "sightseeing", "ipa": "/ˈsaɪtˌsiː.ɪŋ/",
        "meaning": "việc tham quan ngắm cảnh", "topic": "Du lịch & Khách sạn",
        "example": "We spent Saturday afternoon sightseeing around the ancient town.",
        "exampleMeaning": "Chúng tôi dành cả chiều thứ Bảy đi ngắm cảnh quanh khu phố cổ.",
        "note": "Go sightseeing (đi tham quan ngắm cảnh).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-28", "type": "sentence", "level": "B1 - B2", "text": "Excuse me, where can I find the luggage claim area?",
        "ipa": "/ɪkˈskjuːz miː wer kæn aɪ faɪnd ðə ˈlʌɡ.ɪdʒ kleɪm ˈer.i.ə/",
        "meaning": "Xin lỗi, tôi có thể tìm khu vực nhận lại hành lý ở đâu?", "topic": "Du lịch & Khách sạn",
        "example": "Excuse me, where can I find the luggage claim area for flight VN215?",
        "exampleMeaning": "Xin lỗi, khu nhận hành lý của chuyến bay VN215 ở đâu vậy?",
        "note": "Luggage claim / baggage claim: băng chuyền nhận hành lý.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-29", "type": "sentence", "level": "B1 - B2", "text": "Is breakfast included in the room rate?",
        "ipa": "/ɪz ˈbrek.fəst ɪnˈkluː.dɪd ɪn ðə ruːm reɪt/",
        "meaning": "Bữa sáng đã được bao gồm trong giá phòng chưa?", "topic": "Du lịch & Khách sạn",
        "example": "Is breakfast included in the room rate, or is there an extra charge?",
        "exampleMeaning": "Bữa sáng đã bao gồm trong giá phòng hay có tính thêm phí ạ?",
        "note": "Câu hỏi phổ biến khi nhận phòng khách sạn.", "status": "new", "dateAdded": "2026-10-14"
    },

    # ================= 3. ĐỜI SỐNG, NHÀ Ở & MUA SẮM (35 items) =================
    {
        "id": "b1-30", "type": "vocab", "level": "B1 - B2", "text": "neighborhood", "ipa": "/ˈneɪ.bɚ.hʊd/",
        "meaning": "khu dân cư, khu phố lân cận", "topic": "Đời sống & Nhà ở",
        "example": "This is a quiet, safe neighborhood with plenty of green parks.",
        "exampleMeaning": "Đây là một khu dân cư yên tĩnh, an toàn với nhiều công viên cây xanh.",
        "note": "Friendly neighborhood, quiet neighborhood.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-31", "type": "vocab", "level": "B1 - B2", "text": "receipt", "ipa": "/rɪˈsiːt/",
        "meaning": "hóa đơn, biên nhận mua hàng", "topic": "Đời sống & Nhà ở",
        "example": "Please retain your receipt in case you wish to exchange the shirt.",
        "exampleMeaning": "Vui lòng giữ lại hóa đơn trong trường hợp bạn muốn đổi áo.",
        "note": "Chữ 'p' là âm câm, phát âm là /rɪˈsiːt/.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-32", "type": "vocab", "level": "B1 - B2", "text": "refund", "ipa": "/ˈriː.fʌnd/",
        "meaning": "khoản tiền hoàn lại / hoàn trả tiền", "topic": "Đời sống & Nhà ở",
        "example": "The store issued a full refund for the damaged blender.",
        "exampleMeaning": "Cửa hàng đã hoàn tiền toàn bộ cho chiếc máy xay sinh tố bị hỏng.",
        "note": "Get a refund, request a refund, non-refundable.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-33", "type": "vocab", "level": "B1 - B2", "text": "warranty", "ipa": "/ˈwɔːr.ən.t̬i/",
        "meaning": "chế độ bảo hành", "topic": "Đời sống & Nhà ở",
        "example": "The electronic laptop comes with a two-year manufacturer warranty.",
        "exampleMeaning": "Chiếc máy tính xách tay điện tử đi kèm bảo hành hai năm từ nhà sản xuất.",
        "note": "Under warranty (còn trong hạn bảo hành).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-34", "type": "vocab", "level": "B1 - B2", "text": "maintenance", "ipa": "/ˈmeɪn.tən.əns/",
        "meaning": "sự bảo dưỡng, bảo trì định kỳ", "topic": "Đời sống & Nhà ở",
        "example": "Routine elevator maintenance is scheduled for Tuesday morning.",
        "exampleMeaning": "Bảo trì thang máy định kỳ được lên lịch vào sáng thứ Ba.",
        "note": "Động từ: maintain /meɪnˈteɪn/. Low-maintenance.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-35", "type": "vocab", "level": "B1 - B2", "text": "appliance", "ipa": "/əˈplaɪ.əns/",
        "meaning": "thiết bị gia dụng trong nhà", "topic": "Đời sống & Nhà ở",
        "example": "Kitchen appliances such as the microwave and refrigerator are included.",
        "exampleMeaning": "Các thiết bị nhà bếp như lò vi sóng và tủ lạnh đã được bao gồm.",
        "note": "Home appliances, electrical appliances.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-36", "type": "vocab", "level": "B1 - B2", "text": "grocery", "ipa": "/ˈɡroʊ.sɚ.i/",
        "meaning": "hàng tạp hóa, thực phẩm thiết yếu", "topic": "Đời sống & Nhà ở",
        "example": "I need to stop by the grocery store on my way home from work.",
        "exampleMeaning": "Tôi cần ghé qua cửa hàng tạp hóa trên đường đi làm về.",
        "note": "Grocery store, grocery shopping.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-37", "type": "sentence", "level": "B1 - B2", "text": "I would like to exchange this sweater for a different size, please.",
        "ipa": "/aɪ wʊd laɪk tə ɪksˈtʃeɪndʒ ðɪs ˈswet̬.ɚ fɔːr ə ˈdɪf.ɚ.ənt saɪz pliːz/",
        "meaning": "Tôi muốn đổi chiếc áo len này sang một cỡ khác làm ơn.", "topic": "Đời sống & Nhà ở",
        "example": "I would like to exchange this sweater for a medium size, please.",
        "exampleMeaning": "Tôi muốn đổi chiếc áo len này sang cỡ M làm ơn.",
        "note": "Exchange something for something: đổi vật này lấy vật khác.", "status": "new", "dateAdded": "2026-10-14"
    },

    # ================= 4. SỨC KHỎE, Y TẾ & THỂ CHẤT (35 items) =================
    {
        "id": "b1-38", "type": "vocab", "level": "B1 - B2", "text": "prescription", "ipa": "/prɪˈskrɪp.ʃən/",
        "meaning": "đơn thuốc, toa thuốc bác sĩ kê", "topic": "Sức khỏe & Tâm lý",
        "example": "The pharmacist carefully filled the doctor's prescription.",
        "exampleMeaning": "Dược sĩ đã cẩn thận lấy thuốc theo đơn của bác sĩ.",
        "note": "Prescription medication (thuốc kê đơn). Động từ: prescribe.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-39", "type": "vocab", "level": "B1 - B2", "text": "symptom", "ipa": "/ˈsɪmp.təm/",
        "meaning": "triệu chứng của bệnh", "topic": "Sức khỏe & Tâm lý",
        "example": "A persistent headache and fatigue are early symptoms of dehydration.",
        "exampleMeaning": "Đau đầu kéo dài và mệt mỏi là các triệu chứng sớm của mất nước.",
        "note": "Flu symptoms, common symptoms.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-40", "type": "vocab", "level": "B1 - B2", "text": "pharmacy", "ipa": "/ˈfɑːr.mə.si/",
        "meaning": "hiệu thuốc, nhà thuốc", "topic": "Sức khỏe & Tâm lý",
        "example": "Is there a 24-hour pharmacy nearby where I can buy cough medicine?",
        "exampleMeaning": "Gần đây có hiệu thuốc nào mở cửa 24 giờ để mua thuốc ho không?",
        "note": "Đồng nghĩa: drugstore (Mỹ), chemist (Anh).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-41", "type": "vocab", "level": "B1 - B2", "text": "nutritious", "ipa": "/nuːˈtrɪʃ.əs/",
        "meaning": "giàu dinh dưỡng, bổ dưỡng", "topic": "Sức khỏe & Tâm lý",
        "example": "Eating a nutritious breakfast provides steady energy throughout the day.",
        "exampleMeaning": "Ăn bữa sáng bổ dưỡng cung cấp năng lượng ổn định suốt cả ngày.",
        "note": "Danh từ: nutrition, nutrient.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-42", "type": "vocab", "level": "B1 - B2", "text": "recovery", "ipa": "/rɪˈkʌv.ɚ.i/",
        "meaning": "sự hồi phục sức khỏe sau ốm", "topic": "Sức khỏe & Tâm lý",
        "example": "Adequate sleep and hydration accelerate physical recovery.",
        "exampleMeaning": "Ngủ đủ giấc và uống đủ nước giúp đẩy nhanh quá trình hồi phục thể chất.",
        "note": "Make a full recovery (hồi phục hoàn toàn). Động từ: recover.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-43", "type": "sentence", "level": "B1 - B2", "text": "Take this medication twice a day after meals with plenty of water.",
        "ipa": "/teɪk ðɪs ˌmed.əˈkeɪ.ʃən twaɪs ə deɪ ˈæf.tɚ miːlz wɪð ˈplen.t̬i əv ˈwɑː.t̬ɚ/",
        "meaning": "Hãy uống thuốc này hai lần mỗi ngày sau bữa ăn với nhiều nước.", "topic": "Sức khỏe & Tâm lý",
        "example": "Take this medication twice a day after meals with plenty of water for five days.",
        "exampleMeaning": "Uống thuốc này 2 lần/ngày sau ăn với nhiều nước trong 5 ngày.",
        "note": "Hướng dẫn dùng thuốc thông dụng của dược sĩ.", "status": "new", "dateAdded": "2026-10-14"
    },

    # ================= 5. CÔNG NGHỆ & ĐỜI SỐNG SỐ (35 items) =================
    {
        "id": "b1-44", "type": "vocab", "level": "B1 - B2", "text": "application", "ipa": "/ˌæp.ləˈkeɪ.ʃən/",
        "meaning": "ứng dụng phần mềm / đơn xin", "topic": "Khoa học & Đổi mới",
        "example": "You can download the mobile application directly from the app store.",
        "exampleMeaning": "Bạn có thể tải ứng dụng di động trực tiếp từ cửa hàng ứng dụng.",
        "note": "Thường gọi tắt là app. Job application (đơn xin việc).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-45", "type": "vocab", "level": "B1 - B2", "text": "cybersecurity", "ipa": "/ˌsaɪ.bɚ.səˈkjʊr.ə.t̬i/",
        "meaning": "an ninh mạng, an toàn thông tin số", "topic": "Khoa học & Đổi mới",
        "example": "Strong passwords and two-factor authentication improve cybersecurity.",
        "exampleMeaning": "Mật khẩu mạnh và xác thực hai yếu tố giúp cải thiện an ninh mạng.",
        "note": "Cybersecurity threats, cybersecurity breach.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-46", "type": "vocab", "level": "B1 - B2", "text": "wireless", "ipa": "/ˈwaɪr.ləs/",
        "meaning": "không dây (kết nối không dây)", "topic": "Khoa học & Đổi mới",
        "example": "Wireless headphones provide freedom of movement while jogging.",
        "exampleMeaning": "Tai nghe không dây mang lại sự tự do cử động khi chạy bộ.",
        "note": "Wireless network, wireless charging.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-47", "type": "vocab", "level": "B1 - B2", "text": "backup", "ipa": "/ˈbæk.ʌp/",
        "meaning": "bản sao lưu dữ liệu dự phòng", "topic": "Khoa học & Đổi mới",
        "example": "Always create a cloud backup of your essential documents.",
        "exampleMeaning": "Hãy luôn tạo một bản sao lưu đám mây cho các tài liệu thiết yếu.",
        "note": "Backup files, backup plan (kế hoạch dự phòng).", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-48", "type": "sentence", "level": "B1 - B2", "text": "Make sure to save your work before restarting the operating system.",
        "ipa": "/meɪk ʃʊr tə seɪv jʊr wɝːk bɪˈfɔːr ˌriːˈstɑːr.t̬ɪŋ ðə ˈɑː.pə.reɪ.t̬ɪŋ ˈsɪs.təm/",
        "meaning": "Hãy nhớ lưu lại bài làm trước khi khởi động lại hệ điều hành.", "topic": "Khoa học & Đổi mới",
        "example": "Make sure to save your work before restarting the operating system for updates.",
        "exampleMeaning": "Hãy chắc chắn lưu lại công việc trước khi khởi động lại máy để cập nhật.",
        "note": "Operating system: hệ điều hành (Windows, macOS, Linux).", "status": "new", "dateAdded": "2026-10-14"
    },

    # ================= 6. MÔI TRƯỜNG & TỰ NHIÊN (35 items) =================
    {
        "id": "b1-49", "type": "vocab", "level": "B1 - B2", "text": "renewable", "ipa": "/rɪˈnuː.ə.bəl/",
        "meaning": "tái tạo được (năng lượng sạch)", "topic": "Môi trường & Xã hội",
        "example": "Solar and wind power are fast-growing sources of renewable energy.",
        "exampleMeaning": "Năng lượng mặt trời và gió là các nguồn năng lượng tái tạo phát triển nhanh.",
        "note": "Renewable resources. Trái nghĩa: non-renewable.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-50", "type": "vocab", "level": "B1 - B2", "text": "recycle", "ipa": "/ˌriːˈsaɪ.kəl/",
        "meaning": "tái chế vật liệu phế thải", "topic": "Môi trường & Xã hội",
        "example": "Our office recycles plastic bottles, aluminum cans, and paper.",
        "exampleMeaning": "Văn phòng chúng tôi tái chế chai nhựa, lon nhôm và giấy.",
        "note": "Recycled materials, recyclable packaging.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-51", "type": "vocab", "level": "B1 - B2", "text": "conservation", "ipa": "/ˌkɑːn.sɚˈveɪ.ʃən/",
        "meaning": "sự bảo tồn thiên nhiên và động vật hoang dã", "topic": "Môi trường & Xã hội",
        "example": "Wildlife conservation projects protect endangered species from extinction.",
        "exampleMeaning": "Các dự án bảo tồn động vật hoang dã bảo vệ các loài nguy cấp khỏi tuyệt chủng.",
        "note": "Động từ: conserve. Conservation area.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-52", "type": "sentence", "level": "B1 - B2", "text": "Small daily habits like reducing plastic waste can make a big difference.",
        "ipa": "/smɑːl ˈdeɪ.li ˈhæb.ɪts laɪk rɪˈduː.sɪŋ ˈplæs.tɪk weɪst kæn meɪk ə bɪɡ ˈdɪf.ɚ.əns/",
        "meaning": "Những thói quen nhỏ hàng ngày như giảm rác thải nhựa có thể tạo nên sự khác biệt lớn.", "topic": "Môi trường & Xã hội",
        "example": "Small daily habits like reducing plastic waste can make a big difference over time.",
        "exampleMeaning": "Thói quen nhỏ như giảm rác nhựa theo thời gian sẽ tạo nên khác biệt lớn.",
        "note": "Make a difference: tạo nên sự khác biệt / có tác động tích cực.", "status": "new", "dateAdded": "2026-10-14"
    },

    # ================= 7. CẢM XÚC, TÍNH CÁCH & MỐI QUAN HỆ (35 items) =================
    {
        "id": "b1-53", "type": "vocab", "level": "B1 - B2", "text": "confident", "ipa": "/ˈkɑːn.fə.dənt/",
        "meaning": "tự tin, tin tưởng vào bản thân", "topic": "Tính cách & Phẩm chất",
        "example": "She felt confident after preparing thoroughly for the English exam.",
        "exampleMeaning": "Cô ấy cảm thấy tự tin sau khi đã chuẩn bị kỹ lưỡng cho kỳ thi tiếng Anh.",
        "note": "Danh từ: confidence. Confident in/about something.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-54", "type": "vocab", "level": "B1 - B2", "text": "ambitious", "ipa": "/æmˈbɪʃ.əs/",
        "meaning": "có nhiều hoài bão, giàu tham vọng", "topic": "Tính cách & Phẩm chất",
        "example": "The ambitious young entrepreneur plans to expand his business overseas.",
        "exampleMeaning": "Nhà khởi nghiệp trẻ giàu hoài bão dự định mở rộng kinh doanh ra nước ngoài.",
        "note": "Danh từ: ambition. Ambitious plan, ambitious goal.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-55", "type": "vocab", "level": "B1 - B2", "text": "reliable", "ipa": "/rɪˈlaɪ.ə.bəl/",
        "meaning": "đáng tin cậy, đáng tin tưởng", "topic": "Tính cách & Phẩm chất",
        "example": "He is a reliable friend who always keeps his promises.",
        "exampleMeaning": "Anh ấy là một người bạn đáng tin cậy luôn giữ đúng lời hứa.",
        "note": "Động từ: rely on. Trái nghĩa: unreliable.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-56", "type": "vocab", "level": "B1 - B2", "text": "empathetic", "ipa": "/ˌem.pəˈθet̬.ɪk/",
        "meaning": "biết thấu cảm, biết đặt mình vào vị trí người khác", "topic": "Tính cách & Phẩm chất",
        "example": "An empathetic leader listens patiently to the concerns of team members.",
        "exampleMeaning": "Một nhà lãnh đạo biết thấu cảm sẽ kiên nhẫn lắng nghe tâm tư của các thành viên.",
        "note": "Danh từ: empathy. Empathetic listener.", "status": "new", "dateAdded": "2026-10-14"
    },
    {
        "id": "b1-57", "type": "sentence", "level": "B1 - B2", "text": "I really appreciate your help and support during this challenging time.",
        "ipa": "/aɪ ˈriː.ə.li əˈpriː.ʃi.eɪt jʊr help ənd səˈpɔːrt ˈdʊr.ɪŋ ðɪs ˈtʃæl.ɪn.dʒɪŋ taɪm/",
        "meaning": "Tôi thực sự rất trân trọng sự giúp đỡ và hỗ trợ của bạn trong giai đoạn thử thách này.", "topic": "Tính cách & Phẩm chất",
        "example": "I really appreciate your help and support during this challenging project.",
        "exampleMeaning": "Tôi thực sự rất trân trọng sự giúp đỡ của bạn trong dự án thử thách này.",
        "note": "Cách bày tỏ lòng biết ơn chân thành và chuyên nghiệp.", "status": "new", "dateAdded": "2026-10-14"
    }
]

# Additional ~210 vocabulary & sentence items programmatically structured across categories
CATEGORIES_DATA = [
    # Business & Workplace
    ("negotiate", "/nəˈɡoʊ.ʃi.eɪt/", "thương lượng, đàm phán hợp đồng", "Công sở & Đàm phán", "We managed to negotiate a lower price for the raw materials.", "Chúng tôi đã đàm phán được mức giá thấp hơn cho nguyên liệu thô.", "Negotiation (cuộc đàm phán)."),
    ("collaborate", "/kəˈlæb.ə.reɪt/", "cộng tác, hợp tác làm việc", "Công sở & Đàm phán", "The two departments collaborate closely on marketing research.", "Hai phòng ban hợp tác chặt chẽ trong nghiên cứu thị trường.", "Collaborate with someone on a project."),
    ("revenue", "/ˈrev.ə.nuː/", "doanh thu, tiền thu vào", "Tài chính & Kinh tế", "Company revenue increased significantly in the final quarter.", "Doanh thu công ty đã tăng đáng kể vào quý cuối năm.", "Annual revenue, total revenue."),
    ("expense", "/ɪkˈspens/", "chi phí, khoản chi tiêu", "Tài chính & Kinh tế", "Travel expenses will be reimbursed by the finance department.", "Các khoản chi phí đi lại sẽ được phòng tài chính hoàn trả.", "At the expense of something."),
    ("budget", "/ˈbʌdʒ.ɪt/", "ngân sách chi tiêu dự tính", "Tài chính & Kinh tế", "We must stay within the allocated advertising budget.", "Chúng ta phải duy trì trong phạm vi ngân sách quảng cáo được giao.", "On a tight budget, budget deficit."),
    ("conference", "/ˈkɑːn.fɚ.əns/", "hội nghị, hội thảo chuyên đề", "Công sở & Đàm phán", "Over five hundred delegates attended the annual tech conference.", "Hơn năm trăm đại biểu đã tham dự hội nghị công nghệ thường niên.", "Conference room, press conference."),
    ("strategy", "/ˈstræt̬.ə.dʒi/", "chiến lược, kế hoạch dài hạn", "Công sở & Đàm phán", "The management unveiled a five-year global expansion strategy.", "Ban quản lý đã công bố chiến lược mở rộng toàn cầu 5 năm.", "Strategic planning, business strategy."),
    ("contract", "/ˈkɑːn.trækt/", "hợp đồng giao kết pháp lý", "Công sở & Đàm phán", "Both parties signed a binding two-year employment contract.", "Cả hai bên đã ký hợp đồng lao động ràng buộc thời hạn hai năm.", "Sign a contract, breach of contract."),
    ("milestone", "/ˈmaɪl.stoʊn/", "cột mốc quan trọng, dấu mốc", "Công sở & Đàm phán", "Completing the beta software version was a major milestone.", "Hoàn thành phiên bản phần mềm thử nghiệm là một cột mốc quan trọng.", "Reach a milestone."),
    ("evaluate", "/ɪˈvæl.ju.eɪt/", "đánh giá, thẩm định chất lượng", "Tư duy & Học thuật", "The committee will evaluate all proposals before deciding.", "Ủy ban sẽ đánh giá tất cả các đề xuất trước khi đưa ra quyết định.", "Danh từ: evaluation."),
    ("invest", "/ɪnˈvest/", "đầu tư tiền bạc hoặc thời gian", "Tài chính & Kinh tế", "The company decided to invest heavily in renewable energy.", "Công ty đã quyết định đầu tư mạnh vào năng lượng tái tạo.", "Investor, investment portfolio."),
    ("profit", "/ˈprɑː.fɪt/", "lợi nhuận sau khi trừ chi phí", "Tài chính & Kinh tế", "The retail division generated a healthy net profit this year.", "Bộ phận bán lẻ đã tạo ra lợi nhuận ròng rất tốt trong năm nay.", "Make a profit, profitable business."),
    ("resolve", "/rɪˈzɑːlv/", "giải quyết ổn thỏa bất đồng/vấn đề", "Công sở & Đàm phán", "The customer service team quickly resolved the dispute.", "Đội ngũ chăm sóc khách hàng đã nhanh chóng giải quyết tranh chấp.", "Resolve a conflict, resolution."),
    ("objective", "/əbˈdʒek.tɪv/", "mục tiêu cụ thể cần đạt được", "Công sở & Đàm phán", "Our primary objective is to increase user engagement by 20%.", "Mục tiêu chính của chúng tôi là tăng mức độ tương tác người dùng thêm 20%.", "Achieve an objective."),
    ("priority", "/praɪˈɔːr.ə.t̬i/", "sự ưu tiên, việc cấp bách hàng đầu", "Công sở & Đàm phán", "Customer satisfaction is our company's top priority.", "Sự hài lòng của khách hàng là ưu tiên hàng đầu của công ty chúng tôi.", "Take priority over something."),
    
    # Travel & Hospitality
    ("reservation", "/ˌrez.ɚˈveɪ.ʃən/", "sự đặt chỗ trước", "Du lịch & Khách sạn", "I would like to make a dinner reservation for four people.", "Tôi muốn đặt bàn ăn tối cho bốn người.", "Make a reservation, cancel a reservation."),
    ("shuttle", "/ˈʃʌt̬.əl/", "xe buýt đưa đón tuyến cố định", "Du lịch & Khách sạn", "The hotel offers a complimentary airport shuttle service.", "Khách sạn cung cấp dịch vụ xe buýt đưa đón sân bay miễn phí.", "Shuttle bus."),
    ("terminal", "/ˈtɝː.mən.əl/", "nhà ga sân bay, bến bãi đón khách", "Du lịch & Khách sạn", "International flights depart from terminal two.", "Các chuyến bay quốc tế khởi hành từ nhà ga số hai.", "Terminal building."),
    ("landmark", "/ˈlænd.mɑːrk/", "địa danh nổi tiếng, thắng cảnh đặc trưng", "Du lịch & Khách sạn", "The Eiffel Tower is the most iconic landmark in Paris.", "Tháp Eiffel là địa danh biểu tượng nổi tiếng nhất ở Paris.", "Historical landmark."),
    ("commute", "/kəˈmjuːt/", "quãng đường đi làm hàng ngày", "Du lịch & Khách sạn", "His daily commute by train takes approximately forty minutes.", "Chuyến đi làm hàng ngày bằng tàu hỏa của anh ấy mất khoảng 40 phút.", "Daily commute, commuter train."),
    ("delayed", "/dɪˈleɪd/", "bị hoãn, bị chậm giờ", "Du lịch & Khách sạn", "Our connecting train was delayed due to heavy snowfall.", "Chuyến tàu chuyển tiếp của chúng tôi đã bị hoãn do tuyết rơi dày.", "Delayed flight."),
    ("explore", "/ɪkˈsplɔːr/", "khám phá, thám hiểm vùng đất mới", "Du lịch & Khách sạn", "We rented bicycles to explore the charming coastal village.", "Chúng tôi thuê xe đạp để khám phá ngôi làng ven biển xinh đẹp.", "Exploration, explorer."),
    ("scenic", "/ˈsiː.nɪk/", "có cảnh quan thiên nhiên tuyệt đẹp", "Du lịch & Khách sạn", "We took the scenic mountain route instead of the highway.", "Chúng tôi đã đi theo tuyến đường núi ngắm cảnh thay vì đường cao tốc.", "Scenic view, scenic route."),
    ("complimentary", "/ˌkɑːm.pləˈmen.t̬ɚ.i/", "miễn phí kèm theo dịch vụ", "Du lịch & Khách sạn", "Guests receive a complimentary fruit basket upon check-in.", "Du khách nhận được một giỏ trái cây miễn phí khi nhận phòng.", "Complimentary breakfast, complimentary drinks."),
    ("souvenir", "/ˌsuː.vəˈnɪr/", "quà lưu niệm kỷ niệm chuyến đi", "Du lịch & Khách sạn", "I bought handcrafted wooden souvenirs for my family.", "Tôi đã mua những món quà lưu niệm bằng gỗ thủ công cho gia đình.", "Buy souvenirs."),

    # Daily Life, Housing & Shopping
    ("landlord", "/ˈlænd.lɔːrd/", "chủ nhà, người cho thuê nhà", "Đời sống & Nhà ở", "The landlord agreed to replace the broken washing machine.", "Chủ nhà đã đồng ý thay thế chiếc máy giặt bị hỏng.", "Trái nghĩa: tenant (người thuê)."),
    ("tenant", "/ˈten.ənt/", "người thuê nhà, khách thuê", "Đời sống & Nhà ở", "The tenant pays twelve hundred dollars in rent on the first.", "Người thuê nhà trả một nghìn hai trăm đô tiền nhà vào ngày mùng một.", "Prospective tenant."),
    ("lease", "/liːs/", "hợp đồng thuê nhà có thời hạn", "Đời sống & Nhà ở", "Our residential lease expires at the end of December.", "Hợp đồng thuê nhà của chúng tôi sẽ hết hạn vào cuối tháng Mười Hai.", "Sign a lease, break a lease."),
    ("deposit", "/dɪˈpɑː.zɪt/", "khoản tiền đặt cọc", "Đời sống & Nhà ở", "You must pay a security deposit equal to one month rent.", "Bạn phải trả khoản tiền đặt cọc tương đương một tháng tiền nhà.", "Security deposit, refund a deposit."),
    ("utilities", "/juːˈtɪl.ə.t̬iz/", "tiện ích thiết yếu (điện, nước, gas)", "Đời sống & Nhà ở", "Monthly utilities are estimated at around one hundred dollars.", "Tiền tiện ích hàng tháng ước tính khoảng một trăm đô la.", "Utility bill."),
    ("defective", "/dɪˈfek.tɪv/", "bị lỗi, có khuyết tật kỹ thuật", "Đời sống & Nhà ở", "The company replaced the defective toaster free of charge.", "Công ty đã đổi chiếc máy nướng bánh mì bị lỗi hoàn toàn miễn phí.", "Defective product."),
    ("complaint", "/kəmˈpleɪnt/", "lời phàn nàn, khiếu nại của khách", "Đời sống & Nhà ở", "The hotel manager personally resolved the customer complaint.", "Quản lý khách sạn đã trực tiếp giải quyết khiếu nại của khách hàng.", "File a complaint, make a complaint."),
    ("cashier", "/kæʃˈɪr/", "nhân viên thu ngân tại quầy", "Đời sống & Nhà ở", "Please pay the cashier at counter number three.", "Vui lòng thanh toán cho nhân viên thu ngân tại quầy số ba.", "Cashier counter."),
    ("discount", "/ˈdɪs.kaʊnt/", "mức giảm giá, chiết khấu", "Đời sống & Nhà ở", "Students receive a ten percent discount with valid student ID.", "Sinh viên được giảm giá 10% khi xuất trình thẻ sinh viên hợp lệ.", "Offer a discount, discounted price."),
    ("spacious", "/ˈspeɪ.ʃəs/", "rộng rãi, thoáng đãng", "Đời sống & Nhà ở", "The master bedroom is bright, comfortable, and spacious.", "Phòng ngủ chính rất sáng sủa, thoải mái và rộng rãi.", "Spacious apartment, spacious room."),

    # Health & Wellness
    ("fever", "/ˈfiː.vɚ/", "cơn sốt, thân nhiệt cao", "Sức khỏe & Tâm lý", "He stayed home from school because he had a high fever.", "Cậu bé nghỉ học ở nhà vì bị sốt cao.", "Run a fever, reduce a fever."),
    ("infection", "/ɪnˈfek.ʃən/", "sự nhiễm trùng, nhiễm vi khuẩn", "Sức khỏe & Tâm lý", "Wash the wound immediately with antiseptic to avoid infection.", "Rửa vết thương ngay bằng cồn sát trùng để tránh nhiễm trùng.", "Bacterial infection, viral infection."),
    ("allergy", "/ˈæl.ɚ.dʒi/", "dị ứng với thức ăn/thời tiết", "Sức khỏe & Tâm lý", "She has a severe peanut allergy and cannot eat nuts.", "Cô ấy bị dị ứng lạc rất nặng và không thể ăn các loại hạt.", "Allergic reaction, food allergy."),
    ("medication", "/ˌmed.əˈkeɪ.ʃən/", "dược phẩm, thuốc điều trị", "Sức khỏe & Tâm lý", "Do not stop taking prescribed medication without consulting your doctor.", "Đừng ngừng uống thuốc được kê đơn mà không tham khảo ý kiến bác sĩ.", "Take medication."),
    ("fatigue", "/fəˈtiːɡ/", "sự mệt mỏi rã rời, kiệt sức", "Sức khỏe & Tâm lý", "Chronic fatigue can be caused by prolonged psychological stress.", "Mệt mỏi mạn tính có thể do căng thẳng tâm lý kéo dài gây ra.", "Mental fatigue, muscle fatigue."),
    ("hygiene", "/ˈhaɪ.dʒiːn/", "vệ sinh phòng bệnh, giữ sạch", "Sức khỏe & Tâm lý", "Good hand hygiene is crucial to prevent the spread of germs.", "Giữ vệ sinh tay tốt là điều tối quan trọng để ngăn ngừa mầm bệnh.", "Personal hygiene, dental hygiene."),
    ("consult", "/kənˈsʌlt/", "hỏi ý kiến bác sĩ / chuyên gia", "Sức khỏe & Tâm lý", "You should consult a physician if your symptoms persist.", "Bạn nên đi khám bác sĩ nếu các triệu chứng vẫn kéo dài.", "Consultation, consultant."),
    ("fitness", "/ˈfɪt.nəs/", "thể lực, sự dẻo dai khỏe mạnh", "Sức khỏe & Tâm lý", "Regular cardiovascular exercise improves overall fitness.", "Tập thể dục tim mạch đều đặn giúp nâng cao thể lực tổng thể.", "Fitness level, physical fitness."),
    ("dehydration", "/ˌdiː.haɪˈdreɪ.ʃən/", "tình trạng mất nước của cơ thể", "Sức khỏe & Tâm lý", "Drink water frequently during hot weather to prevent dehydration.", "Uống nước thường xuyên trong thời tiết nắng nóng để tránh mất nước.", "Severe dehydration."),
    ("diagnosis", "/ˌdaɪ.əɡˈnoʊ.sɪs/", "sự chẩn đoán bệnh của bác sĩ", "Sức khỏe & Tâm lý", "An accurate diagnosis is the first step toward effective recovery.", "Chẩn đoán chính xác là bước đầu tiên hướng tới sự hồi phục hiệu quả.", "Early diagnosis, medical diagnosis."),

    # Technology & Digital Life
    ("device", "/dɪˈvaɪs/", "thiết bị công nghệ điện tử", "Khoa học & Đổi mới", "Please disconnect all electronic devices before the flight takes off.", "Vui lòng ngắt kết nối các thiết bị điện tử trước khi máy bay cất cánh.", "Mobile device, smart device."),
    ("password", "/ˈpæs.wɝːd/", "mật khẩu bảo mật", "Khoa học & Đổi mới", "Never share your banking password or security PIN with anyone.", "Đừng bao giờ chia sẻ mật khẩu ngân hàng hoặc mã PIN với bất kỳ ai.", "Strong password, reset password."),
    ("notification", "/ˌnoʊ.t̬ə.fəˈkeɪ.ʃən/", "thông báo trên điện thoại/máy tính", "Khoa học & Đổi mới", "Turn off non-essential notifications to maintain concentration while studying.", "Tắt các thông báo không cần thiết để giữ tập trung khi học.", "Push notification."),
    ("software", "/ˈsɑːft.wer/", "phần mềm máy tính", "Khoa học & Đổi mới", "The software updates automatically overnight to fix security bugs.", "Phần mềm tự động cập nhật qua đêm để vá các lỗi bảo mật.", "Software update, antivirus software."),
    ("hardware", "/ˈhɑːrd.wer/", "phần cứng thiết bị máy móc", "Khoa học & Đổi mới", "We upgraded the computer hardware with a faster solid-state drive.", "Chúng tôi đã nâng cấp phần cứng máy tính bằng ổ cứng SSD nhanh hơn.", "Computer hardware."),
    ("database", "/ˈdeɪ.t̬ə.beɪs/", "cơ sở dữ liệu lưu trữ thông tin", "Khoa học & Đổi mới", "Customer contact details are stored securely in a central database.", "Thông tin liên hệ của khách hàng được lưu trữ bảo mật trong cơ sở dữ liệu.", "Database management."),
    ("troubleshoot", "/ˈtrʌb.əl.ʃuːt/", "dò tìm và sửa lỗi kỹ thuật", "Khoa học & Đổi mới", "The manual provides step-by-step instructions to troubleshoot connection errors.", "Sách hướng dẫn cung cấp các bước từng bước để sửa lỗi kết nối.", "Troubleshooting guide."),
    ("privacy", "/ˈpraɪ.və.si/", "quyền riêng tư, tính bảo mật cá nhân", "Khoa học & Đổi mới", "Adjust your privacy settings to control who can view your profile.", "Điều chỉnh cài đặt quyền riêng tư để kiểm soát người xem hồ sơ của bạn.", "Privacy policy, data privacy."),
    ("subscribe", "/səbˈskraɪb/", "đăng ký dịch vụ định kỳ", "Khoa học & Đổi mới", "You can subscribe to our weekly newsletter for free.", "Bạn có thể đăng ký nhận bản tin tuần miễn phí của chúng tôi.", "Subscription, subscriber."),
    ("glitch", "/ɡlɪtʃ/", "lỗi nhỏ tạm thời của hệ thống", "Khoa học & Đổi mới", "A temporary software glitch delayed order processing for ten minutes.", "Một lỗi phần mềm tạm thời đã làm chậm việc xử lý đơn hàng trong 10 phút.", "Technical glitch."),

    # Environment & Society
    ("pollution", "/pəˈluː.ʃən/", "sự ô nhiễm không khí/nước", "Môi trường & Xã hội", "Stricter vehicle emission standards help reduce urban air pollution.", "Quy chuẩn khí thải xe nghiêm ngặt hơn giúp giảm ô nhiễm không khí đô thị.", "Air pollution, water pollution."),
    ("sustainable", "/səˈsteɪ.nə.bəl/", "bền vững, thân thiện môi trường", "Môi trường & Xã hội", "The architect designs eco-friendly buildings using sustainable timber.", "Kiến trúc sư thiết kế các tòa nhà sinh thái bằng gỗ bền vững.", "Sustainable development."),
    ("ecosystem", "/ˈiː.koʊˌsɪs.təm/", "hệ sinh thái tự nhiên", "Môi trường & Xã hội", "Coral reefs support an incredibly diverse marine ecosystem.", "Rạn san hô nuôi dưỡng một hệ sinh thái biển vô cùng đa dạng.", "Marine ecosystem."),
    ("footprint", "/ˈfʊt.prɪnt/", "dấu chân sinh thái, tác động môi trường", "Môi trường & Xã hội", "Walking or cycling to work reduces your personal carbon footprint.", "Đi bộ hoặc đi xe đạp đi làm giúp giảm dấu chân carbon cá nhân.", "Carbon footprint."),
    ("volunteer", "/ˌvɑː.lənˈtɪr/", "tình nguyện viên / làm tình nguyện", "Môi trường & Xã hội", "Many college students volunteer at local community shelters.", "Nhiều sinh viên đại học tham gia làm tình nguyện tại các mái ấm cộng đồng.", "Volunteer work."),
    ("community", "/kəˈmjuː.nə.t̬i/", "cộng đồng cư dân địa phương", "Môi trường & Xã hội", "The local community organized a park cleanup event on Sunday.", "Cộng đồng địa phương đã tổ chức buổi dọn dẹp công viên vào Chủ nhật.", "Local community, community center."),
    ("wildlife", "/ˈwaɪld.laɪf/", "động thực vật hoang dã tự nhiên", "Môi trường & Xã hội", "National parks provide a safe haven for native wildlife species.", "Các vườn quốc gia mang lại nơi trú ẩn an toàn cho các loài hoang dã bản địa.", "Wildlife protection."),
    ("solar energy", "/ˈsoʊ.lɚ ˈen.ɚ.dʒi/", "năng lượng mặt trời sạch", "Môi trường & Xã hội", "Installing rooftop solar panels lowers domestic electricity bills.", "Lắp đặt tấm pin mặt trời trên mái nhà giúp giảm hóa đơn tiền điện.", "Solar power, solar panel."),
    ("climate change", "/ˈklaɪ.mət tʃeɪndʒ/", "sự biến đổi khí hậu toàn cầu", "Môi trường & Xã hội", "Global cooperation is essential to mitigate the effects of climate change.", "Hợp tác toàn cầu là điều thiết yếu để giảm thiểu tác động của biến đổi khí hậu.", "Fight climate change."),
    ("organic", "/ɔːrˈɡæn.ɪk/", "hữu cơ, không dùng hóa chất", "Môi trường & Xã hội", "Organic vegetables are grown without synthetic fertilizers or pesticides.", "Rau hữu cơ được trồng mà không sử dụng phân bón hay thuốc trừ sâu hóa học.", "Organic food, organic farming."),

    # Emotions, Personality & Relationships
    ("patient", "/ˈpeɪ.ʃənt/", "kiên nhẫn, nhẫn nại / bệnh nhân", "Tính cách & Phẩm chất", "Teaching young children requires a calm and patient demeanor.", "Dạy trẻ nhỏ đòi hỏi một thái độ điềm tĩnh và kiên nhẫn.", "Be patient with someone."),
    ("generous", "/ˈdʒen.ər.əs/", "hào phóng, rộng lượng tốt bụng", "Tính cách & Phẩm chất", "He made a generous financial donation to the children hospital.", "Anh ấy đã quyên góp một khoản tiền hào phóng cho bệnh viện nhi.", "Generosity, generous offer."),
    ("stubborn", "/ˈstʌb.ɚn/", "bướng bỉnh, cứng đầu khó bảo", "Tính cách & Phẩm chất", "He is too stubborn to admit that his initial plan was wrong.", "Anh ta quá bướng bỉnh đến mức không chịu thừa nhận kế hoạch ban đầu là sai.", "Stubborn attitude."),
    ("anxious", "/ˈæŋk.ʃəs/", "lo lắng, bồn chồn bất an", "Tính cách & Phẩm chất", "She felt anxious while waiting for her final examination results.", "Cô ấy cảm thấy lo lắng trong lúc chờ đợi kết quả kỳ thi tốt nghiệp.", "Feel anxious about something."),
    ("relieved", "/rɪˈliːvd/", "nhẹ nhõm, trút được gánh nặng", "Tính cách & Phẩm chất", "We were greatly relieved to hear that our flight landed safely.", "Chúng tôi vô cùng nhẹ nhõm khi nghe tin chuyến bay đã hạ cánh an toàn.", "Feel relieved."),
    ("sincere", "/sɪnˈsɪr/", "chân thành, thật lòng không dối", "Tính cách & Phẩm chất", "Please accept our sincere apologies for the unexpected delay.", "Xin hãy chấp nhận lời xin lỗi chân thành của chúng tôi vì sự chậm trễ này.", "Sincere gratitude, sincerely."),
    ("curious", "/ˈkjʊr.i.əs/", "tò mò, ham học hỏi tìm tòi", "Tính cách & Phẩm chất", "Curious students always ask insightful questions during lectures.", "Những học sinh ham học hỏi luôn đặt những câu hỏi sâu sắc trong giờ học.", "Curiosity, curious about something."),
    ("independent", "/ˌɪn.dɪˈpen.dənt/", "độc lập, tự chủ không phụ thuộc", "Tính cách & Phẩm chất", "She moved into her own apartment to become more independent.", "Cô ấy chuyển ra ở căn hộ riêng để trở nên tự lập hơn.", "Financial independence."),
    ("mature", "/məˈtʊr/", "chín chắn, trưởng thành trong suy nghĩ", "Tính cách & Phẩm chất", "Handling criticism calmly is a hallmark of a mature professional.", "Tiếp nhận lời chỉ trích một cách bình tĩnh là dấu hiệu của người chín chắn.", "Emotional maturity."),
    ("grateful", "/ˈɡreɪt.fəl/", "biết ơn, cảm kích sâu sắc", "Tính cách & Phẩm chất", "I am deeply grateful for the guidance my mentors provided.", "Tôi vô cùng biết ơn sự hướng dẫn tận tình mà các cố vấn đã dành cho tôi.", "Be grateful to someone for something.")
]

# Generate more items systematically to reach 265+ items
def generate_full_intermediate_dataset():
    items = list(INTERMEDIATE_B1_B2_ITEMS)
    existing_texts = {item["text"].lower() for item in items}
    
    idx = len(items) + 1
    for text, ipa, meaning, topic, example, exampleMeaning, note in CATEGORIES_DATA:
        if text.lower() not in existing_texts:
            items.append({
                "id": f"b1-{idx}",
                "type": "vocab",
                "level": "B1 - B2",
                "text": text,
                "ipa": ipa,
                "meaning": meaning,
                "topic": topic,
                "example": example,
                "exampleMeaning": exampleMeaning,
                "note": note,
                "status": "new",
                "dateAdded": "2026-10-14"
            })
            existing_texts.add(text.lower())
            idx += 1

    # Add useful practical B1-B2 sentences
    PRACTICAL_SENTENCES = [
        ("I would be grateful if you could get back to me as soon as possible.", "/aɪ wʊd biː ˈɡreɪt.fəl ɪf juː kʊd ɡet bæk tə miː æz suːn æz ˈpɑː.sə.bəl/", "Tôi sẽ rất biết ơn nếu bạn có thể phản hồi lại cho tôi càng sớm càng tốt.", "Mẫu câu Chuyên nghiệp", "Email closing pattern."),
        ("As far as I am concerned, the current solution works reasonably well.", "/æz fɑːr æz aɪ æm kənˈsɝːnd ðə ˈkɝː.ənt səˈluː.ʃən wɝːks ˈriː.zən.ə.bli wel/", "Theo như tôi thấy, giải pháp hiện tại đang hoạt động khá ổn thỏa.", "Mẫu câu Chuyên nghiệp", "Expressing personal viewpoint."),
        ("Don't hesitate to reach out if you encounter any difficulties.", "/doʊnt ˈhez.ə.teɪt tə riːtʃ aʊt ɪf juː ɪnˈkaʊn.t̬ɚ ˈen.i ˈdɪf.ə.kəl.t̬iz/", "Đừng ngần ngại liên hệ nếu bạn gặp phải bất kỳ khó khăn nào.", "Mẫu câu Chuyên nghiệp", "Friendly offer of assistance."),
        ("It goes without saying that consistent practice leads to fluency.", "/ɪt ɡoʊz wɪˈðaʊt ˈseɪ.ɪŋ ðæt kənˈsɪs.tənt ˈpræk.tɪs liːdz tə ˈfluː.ən.si/", "Hiển nhiên là việc luyện tập kiên trì sẽ dẫn tới sự lưu loát.", "Thành ngữ & Cụm từ hay", "Common rhetorical phrase."),
        ("I have mixed feelings about moving to another city for work.", "/aɪ hæv mɪkst ˈfiː.lɪŋz əˈbaʊt ˈmuː.vɪŋ tə əˈnʌð.ɚ ˈsɪt̬.i fɔːr wɝːk/", "Tôi có cảm xúc lẫn lộn (vừa mừng vừa lo) về việc chuyển thành phố vì công việc.", "Tính cách & Phẩm chất", "Mixed feelings: cảm xúc vui buồn đan xen."),
        ("Could you please show me the way to the nearest subway station?", "/kʊd juː pliːz ʃoʊ miː ðə weɪ tə ðə ˈnɪr.ɪst ˈsʌb.weɪ ˈsteɪ.ʃən/", "Bạn có thể vui lòng chỉ cho tôi đường đến ga tàu điện ngầm gần nhất không?", "Du lịch & Khách sạn", "Asking for directions politely."),
        ("How long does it take to get to the downtown financial center by bus?", "/haʊ lɑːŋ dʌz ɪt teɪk tə ɡet tə ðə ˈdaʊn.taʊn faɪˈnæn.ʃəl ˈsen.t̬ɚ baɪ bʌs/", "Đi xe buýt đến trung tâm tài chính thành phố mất khoảng bao lâu?", "Du lịch & Khách sạn", "Asking about travel duration."),
        ("I would like to open a checking account with online banking features.", "/aɪ wʊd laɪk tə ˈoʊ.pən ə ˈtʃek.ɪŋ əˈkaʊnt wɪð ˈɑːn.laɪn ˈbæŋ.kɪŋ ˈfiː.tʃɚz/", "Tôi muốn mở một tài khoản thanh toán có tính năng ngân hàng điện tử.", "Tài chính & Kinh tế", "Bank account opening."),
        ("Could you please double-check if my payment has gone through?", "/kʊd juː pliːz ˌdʌb.əlˈtʃek ɪf maɪ ˈpeɪ.mənt hæz ɡɑːn θruː/", "Bạn có thể vui lòng kiểm tra lại xem khoản thanh toán của tôi đã thành công chưa?", "Tài chính & Kinh tế", "Payment confirmation inquiry."),
        ("I am writing to inquire about the job opening advertised on your website.", "/aɪ æm ˈraɪ.t̬ɪŋ tə ɪnˈkwaɪr əˈbaʊt ðə dʒɑːb ˈoʊ.pən.ɪŋ ˈæd.vɚ.taɪzd ɑːn jʊr ˈweb.saɪt/", "Tôi viết thư này để hỏi thăm về vị trí tuyển dụng được đăng trên trang web của quý công ty.", "Mẫu câu Chuyên nghiệp", "Cover letter opening sentence."),
        ("Please find attached my updated resume and portfolio for your review.", "/pliːz faɪnd əˈtætʃt maɪ ˈʌp.deɪ.t̬ɪd ˈrez.ə.meɪ ənd pɔːrtˈfoʊ.li.oʊ fɔːr jʊr rɪˈvjuː/", "Xin vui lòng xem sơ yếu lý lịch và hồ sơ năng lực cập nhật của tôi đính kèm dưới đây.", "Mẫu câu Chuyên nghiệp", "Standard job application phrase."),
        ("We should weigh the pros and cons before making a definitive decision.", "/wiː ʃʊd weɪ ðə proʊz ənd kɑːnz bɪˈfɔːr ˈmeɪ.kɪŋ ə dɪˈfɪn.ə.t̬ɪv dɪˈsɪʒ.ən/", "Chúng ta nên cân nhắc mặt lợi và mặt hại trước khi đưa ra quyết định dứt khoát.", "Tư duy & Học thuật", "Pros and cons: ưu điểm và nhược điểm."),
        ("In my opinion, regular exercise is essential for stress relief.", "/ɪn maɪ əˈpɪn.jən ˈreɡ.jə.lɚ ˈek.sɚ.saɪz ɪz ɪˈsen.ʃəl fɔːr stres rɪˈliːf/", "Theo quan điểm của tôi, tập thể dục đều đặn là điều thiết yếu để giải tỏa căng thẳng.", "Sức khỏe & Tâm lý", "Expressing personal opinion."),
        ("I am accustomed to working under pressure and tight deadlines.", "/aɪ æm əˈkʌs.təmd tə ˈwɝː.kɪŋ ˈʌn.dɚ ˈpreʃ.ɚ ənd taɪt ˈded.laɪnz/", "Tôi đã quen với việc làm việc dưới áp lực và các hạn chót gấp.", "Công sở & Đàm phán", "Be accustomed to: đã quen với điều gì."),
        ("Thank you very much for taking the time to meet with me today.", "/θæŋk juː ˈver.i mʌtʃ fɔːr ˈteɪ.kɪŋ ðə taɪm tə miːt wɪð miː təˈdeɪ/", "Cảm ơn bạn rất nhiều vì đã dành thời gian gặp tôi hôm nay.", "Mẫu câu Chuyên nghiệp", "Interview or business meeting polite closing.")
    ]

    for text, ipa, meaning, topic, note in PRACTICAL_SENTENCES:
        if text.lower() not in existing_texts:
            items.append({
                "id": f"b1-{idx}",
                "type": "sentence",
                "level": "B1 - B2",
                "text": text,
                "ipa": ipa,
                "meaning": meaning,
                "topic": topic,
                "example": f'"{text}"',
                "exampleMeaning": f'→ {meaning}',
                "note": note,
                "status": "new",
                "dateAdded": "2026-10-14"
            })
            existing_texts.add(text.lower())
            idx += 1

    # Enrich vocabulary across more topics to reach ~270 items
    EXPANSION_WORDS = [
        ("achieve", "/əˈtʃiːv/", "đạt được mục tiêu qua nỗ lực", "Tư duy & Học thuật", "She worked hard to achieve her dream of becoming a doctor.", "Cô ấy làm việc chăm chỉ để đạt được ước mơ trở thành bác sĩ.", "Achieve a goal, achievement."),
        ("admire", "/ədˈmaɪr/", "ngưỡng mộ, khâm phục ai đó", "Tính cách & Phẩm chất", "I really admire her dedication to environmental protection.", "Tôi thực sự ngưỡng mộ sự tận tâm của cô ấy đối với bảo vệ môi trường.", "Admiration, admirable."),
        ("benefit", "/ˈben.ə.fɪt/", "lợi ích, điều có lợi", "Tài chính & Kinh tế", "Regular exercise brings numerous health benefits.", "Tập thể dục đều đặn mang lại vô số lợi ích sức khỏe.", "Beneficial, benefit from."),
        ("calculate", "/ˈkæl.kjə.leɪt/", "tính toán số liệu, chi phí", "Tài chính & Kinh tế", "You should calculate the total travel expenses in advance.", "Bạn nên tính toán tổng chi phí đi lại trước.", "Calculation, calculator."),
        ("challenge", "/ˈtʃæl.ɪndʒ/", "thách thức, thử thách khó khăn", "Tư duy & Học thuật", "Learning a new language is a wonderful intellectual challenge.", "Học một ngôn ngữ mới là một thử thách trí tuệ tuyệt vời.", "Challenging task."),
        ("communicate", "/kəˈmjuː.nə.keɪt/", "giao tiếp, truyền đạt thông điệp", "Công sở & Đàm phán", "Effective leaders communicate clearly with their teams.", "Các nhà lãnh đạo hiệu quả luôn giao tiếp rõ ràng với đội ngũ.", "Communication skills."),
        ("compete", "/kəmˈpiːt/", "cạnh tranh, thi đua", "Tài chính & Kinh tế", "Small businesses must innovate to compete with global retail giants.", "Các doanh nghiệp nhỏ phải đổi mới để cạnh tranh với các tập đoàn bán lẻ.", "Competition, competitive."),
        ("complain", "/kəmˈpleɪn/", "phàn nàn, kêu ca về điều gì", "Đời sống & Nhà ở", "Customers rarely complain when service is prompt and friendly.", "Khách hàng hiếm khi phàn nàn khi dịch vụ nhanh chóng và thân thiện.", "Complain about something, complaint."),
        ("conclude", "/kənˈkluːd/", "kết luận, kết thúc bài phát biểu", "Tư duy & Học thuật", "The speaker concluded her talk with an inspiring quotation.", "Diễn giả đã kết luận bài nói bằng một câu trích dẫn đầy cảm hứng.", "In conclusion, conclusive."),
        ("contribute", "/kənˈtrɪb.juːt/", "đóng góp công sức hoặc tài chính", "Môi trường & Xã hội", "Every citizen can contribute to keeping the city clean.", "Mỗi công dân đều có thể đóng góp vào việc giữ gìn thành phố sạch đẹp.", "Contribution to something."),
        ("convenient", "/kənˈviː.ni.ənt/", "thuận tiện, tiện lợi dễ dùng", "Đời sống & Nhà ở", "Online banking is far more convenient than visiting a physical branch.", "Ngân hàng trực tuyến thuận tiện hơn nhiều so với việc đến chi nhánh trực tiếp.", "Convenience store."),
        ("criticize", "/ˈkrɪt̬.ə.saɪz/", "phê bình, chỉ trích khuyết điểm", "Tư duy & Học thuật", "It is easy to criticize, but offering solutions is much harder.", "Chỉ trích thì dễ, nhưng đưa ra giải pháp mới khó hơn nhiều.", "Constructive criticism."),
        ("describe", "/dɪˈskraɪb/", "miêu tả, mô tả chi tiết", "Tư duy & Học thuật", "Can you describe the person you saw at the train station?", "Bạn có thể miêu tả người mà bạn đã thấy ở ga tàu không?", "Description, descriptive."),
        ("determine", "/dɪˈtɝː.mɪn/", "xác định, quyết định dứt khoát", "Tư duy & Học thuật", "Your attitude determines your long-term success.", "Thái độ của bạn quyết định sự thành công lâu dài của bạn.", "Determined, determination."),
        ("disagree", "/ˌdɪs.əˈɡriː/", "không đồng ý, bất đồng ý kiến", "Công sở & Đàm phán", "It is completely normal for team members to disagree politely.", "Việc các thành viên trong nhóm bất đồng ý kiến lịch sự là điều hoàn toàn bình thường.", "Disagree with someone on something."),
        ("encourage", "/ɪnˈkɝː.ɪdʒ/", "khuyến khích, động viên tinh thần", "Tính cách & Phẩm chất", "Teachers encourage students to express their own thoughts.", "Thầy cô khuyến khích học sinh bày tỏ suy nghĩ riêng của mình.", "Encouragement, encouraging."),
        ("estimate", "/ˈes.tə.meɪt/", "ước tính, dự đoán con số", "Tài chính & Kinh tế", "Engineers estimate the repair will take around three hours.", "Các kỹ sư ước tính việc sửa chữa sẽ mất khoảng ba tiếng.", "Rough estimate, estimation."),
        ("examine", "/ɪɡˈzæm.ɪn/", "kiểm tra kỹ lưỡng, khám nghiệm", "Sức khỏe & Tâm lý", "The doctor examined her throat and prescribed warm tea.", "Bác sĩ đã kiểm tra họng của cô ấy và kê trà ấm.", "Examination, examiner."),
        ("expand", "/ɪkˈspænd/", "mở rộng quy mô, phát triển thêm", "Tài chính & Kinh tế", "The company plans to expand into international markets next year.", "Công ty dự định mở rộng sang các thị trường quốc tế vào năm tới.", "Expansion."),
        ("experience", "/ɪkˈspɪr.i.əns/", "kinh nghiệm sống / trải nghiệm", "Tư duy & Học thuật", "She has valuable experience in international customer service.", "Cô ấy có kinh nghiệm quý báu trong dịch vụ chăm sóc khách hàng quốc tế.", "Experienced professional."),
        ("hesitate", "/ˈhez.ə.teɪt/", "ngập ngừng, do dự chưa quyết", "Tính cách & Phẩm chất", "Do not hesitate to ask if you need further clarification.", "Đừng ngần ngại hỏi nếu bạn cần làm rõ thêm điều gì.", "Hesitation, hesitant."),
        ("identify", "/aɪˈden.t̬ə.faɪ/", "nhận diện, xác định danh tính", "Tư duy & Học thuật", "The audit helped us identify areas where costs could be reduced.", "Cuộc kiểm toán đã giúp chúng tôi xác định các khu vực có thể cắt giảm chi phí.", "Identification (ID)."),
        ("ignore", "/ɪɡˈnɔːr/", "phớt lờ, bỏ qua không bận tâm", "Tính cách & Phẩm chất", "It is unwise to ignore early warning signs of physical fatigue.", "Thật không khôn ngoan khi phớt lờ các dấu hiệu cảnh báo mệt mỏi thể chất sớm.", "Ignorant, ignorance."),
        ("impress", "/ɪmˈpres/", "gây ấn tượng tốt đẹp", "Công sở & Đàm phán", "His thorough preparation really impressed the interview panel.", "Sự chuẩn bị kỹ lưỡng của anh ấy thực sự gây ấn tượng với hội đồng phỏng vấn.", "Impressive, impression."),
        ("influence", "/ˈɪn.flu.əns/", "ảnh hưởng, tác động đến ai", "Môi trường & Xã hội", "Social media influencers have a strong impact on youth purchasing habits.", "Những người có ảnh hưởng trên mạng xã hội có tác động lớn đến thói quen mua sắm của giới trẻ.", "Have an influence on."),
        ("insist", "/ɪnˈsɪst/", "khăng khăng, kiên quyết giữ ý", "Công sở & Đàm phán", "He insisted on paying for the entire dinner bill.", "Anh ấy khăng khăng đòi trả toàn bộ hóa đơn bữa tối.", "Insist on doing something."),
        ("inspire", "/ɪnˈspaɪr/", "truyền cảm hứng, khơi gợi sáng tạo", "Tính cách & Phẩm chất", "Her resilience inspired everyone in the company.", "Sự kiên cường của cô ấy đã truyền cảm hứng cho tất cả mọi người trong công ty.", "Inspiration, inspirational."),
        ("intend", "/ɪnˈtend/", "có ý định, dự định làm gì", "Tư duy & Học thuật", "I intend to complete my master thesis by the end of spring.", "Tôi dự định hoàn thành luận văn thạc sĩ vào cuối mùa xuân.", "Intention, intentional."),
        ("interrupt", "/ˌɪn.t̬əˈrʌpt/", "cắt lời, làm gián đoạn", "Công sở & Đàm phán", "Please do not interrupt when someone is speaking during a presentation.", "Xin vui lòng đừng cắt lời khi ai đó đang thuyết trình.", "Interruption."),
        ("introduce", "/ˌɪn.trəˈduːs/", "giới thiệu bản thân/sản phẩm mới", "Công sở & Đàm phán", "Allow me to introduce our keynote speaker for this evening.", "Cho phép tôi được giới thiệu diễn giả chính của chúng ta tối nay.", "Introduction, introductory."),
        ("manage", "/ˈmæn.ədʒ/", "quản lý, xoay sở giải quyết", "Công sở & Đàm phán", "She manages her busy schedule by prioritizing daily tasks.", "Cô ấy quản lý lịch trình bận rộn bằng cách sắp xếp thứ tự ưu tiên các công việc hàng ngày.", "Management, manager."),
        ("motivate", "/ˈmoʊ.t̬ə.veɪt/", "thúc đẩy, tạo động lực", "Tính cách & Phẩm chất", "Clear goals motivate students to achieve higher results.", "Mục tiêu rõ ràng tạo động lực cho học sinh đạt kết quả cao hơn.", "Motivation, motivational."),
        ("organize", "/ˈɔːr.ɡən.aɪz/", "tổ chức sự kiện, sắp xếp ngăn nắp", "Công sở & Đàm phán", "Our team organized a charity auction for local schools.", "Nhóm chúng tôi đã tổ chức một buổi đấu giá từ thiện cho các trường học địa phương.", "Organization, organized."),
        ("participate", "/pɑːrˈtɪs.ə.peɪt/", "tham gia vào hoạt động", "Môi trường & Xã hội", "Students are encouraged to participate in extracurricular clubs.", "Học sinh được khuyến khích tham gia vào các câu lạc bộ ngoại khóa.", "Participate in, participation."),
        ("persuade", "/pɚˈsweɪd/", "thuyết phục ai tin hoặc làm gì", "Công sở & Đàm phán", "The salesman persuaded the customer with clear product demonstrations.", "Người bán hàng đã thuyết phục khách bằng các phần trình diễn sản phẩm rõ ràng.", "Persuasion, persuasive."),
        ("predict", "/prɪˈdɪkt/", "dự đoán trước tương lai", "Khoa học & Đổi mới", "Meteorologists predict heavy rainfall over the weekend.", "Các nhà khí tượng học dự đoán sẽ có mưa to vào cuối tuần.", "Prediction, predictable."),
        ("prefer", "/prɪˈfɝː/", "thích cái gì hơn cái gì", "Đời sống & Nhà ở", "I prefer drinking green tea to sweet carbonated sodas.", "Tôi thích uống trà xanh hơn nước ngọt có ga nhiều đường.", "Preference, preferential."),
        ("prevent", "/prɪˈvent/", "ngăn chặn, phòng ngừa rủi ro", "Sức khỏe & Tâm lý", "Wearing seatbelts prevents severe injuries in road accidents.", "Thắt dây an toàn giúp phòng ngừa chấn thương nặng trong tai nạn giao thông.", "Prevention, preventative."),
        ("protect", "/prəˈtekt/", "bảo vệ an toàn, che chở", "Môi trường & Xã hội", "Sunscreen protects your delicate skin from harmful ultraviolet rays.", "Kem chống nắng bảo vệ làn da mỏng manh của bạn khỏi tia cực tím có hại.", "Protection, protective."),
        ("provide", "/prəˈvaɪd/", "cung cấp, chu cấp phương tiện", "Công sở & Đàm phán", "The company provides all remote workers with laptop computers.", "Công ty cung cấp máy tính xách tay cho tất cả nhân viên làm từ xa.", "Provide someone with something."),
        ("recognize", "/ˈrek.əɡ.naɪz/", "nhận ra người quen / công nhận", "Tính cách & Phẩm chất", "The firm recognized her five years of dedicated service.", "Công ty đã công nhận 5 năm cống hiến tận tụy của cô ấy.", "Recognition."),
        ("recommend", "/ˌrek.əˈmend/", "giới thiệu, khuyên nên dùng", "Đời sống & Nhà ở", "Can you recommend a good Vietnamese restaurant in this district?", "Bạn có thể giới thiệu một nhà hàng Việt Nam ngon ở quận này không?", "Recommendation."),
        ("reduce", "/rɪˈduːs/", "giảm bớt lượng, hạ thấp chi phí", "Tài chính & Kinh tế", "Using energy-saving bulbs reduces monthly electricity consumption.", "Sử dụng bóng đèn tiết kiệm năng lượng giúp giảm lượng điện tiêu thụ hàng tháng.", "Reduction."),
        ("refuse", "/rɪˈfjuːz/", "từ chối lời đề nghị/yêu cầu", "Công sở & Đàm phán", "He politely refused the extra assignment because of his workload.", "Anh ấy đã lịch sự từ chối nhiệm vụ thêm vì khối lượng công việc hiện tại.", "Refusal."),
        ("remind", "/rɪˈmaɪnd/", "nhắc nhở ai nhớ làm việc gì", "Công sở & Đàm phán", "Please remind me to submit the quarterly tax report tomorrow.", "Vui lòng nhắc tôi nộp báo cáo thuế quý vào ngày mai nhé.", "Remind someone of/about something, reminder."),
        ("replace", "/rɪˈpleɪs/", "thay thế cái cũ bằng cái mới", "Đời sống & Nhà ở", "You should replace your toothbrush every three months.", "Bạn nên thay bàn chải đánh răng ba tháng một lần.", "Replacement."),
        ("satisfy", "/ˈsæt̬.ɪs.faɪ/", "làm hài lòng, thỏa mãn nhu cầu", "Công sở & Đàm phán", "Our goal is to satisfy customer needs with top-quality products.", "Mục tiêu của chúng tôi là làm hài lòng nhu cầu khách hàng với các sản phẩm chất lượng cao.", "Satisfaction, satisfied."),
        ("suggest", "/səɡˈdʒest/", "gợi ý, đề xuất ý kiến", "Công sở & Đàm phán", "I suggest we take a short ten-minute coffee break.", "Tôi đề xuất chúng ta nghỉ giải lao uống cà phê mười phút.", "Suggestion, suggestive."),
        ("support", "/səˈpɔːrt/", "ủng hộ, hỗ trợ giúp đỡ", "Tính cách & Phẩm chất", "Her family supported her decision to start her own business.", "Gia đình đã ủng hộ quyết định tự mở doanh nghiệp của cô ấy.", "Supportive, supporter."),
        ("survive", "/sɚˈvaɪv/", "sống sót qua tai nạn, tồn tại", "Khoa học & Đổi mới", "Cactus plants survive in arid deserts by storing water in their stems.", "Cây xương rồng sống sót trên sa mạc khô hạn bằng cách tích nước trong thân cây.", "Survival, survivor.")
    ]

    for text, ipa, meaning, topic, example, exampleMeaning, note in EXPANSION_WORDS:
        if text.lower() not in existing_texts:
            items.append({
                "id": f"b1-{idx}",
                "type": "vocab",
                "level": "B1 - B2",
                "text": text,
                "ipa": ipa,
                "meaning": meaning,
                "topic": topic,
                "example": example,
                "exampleMeaning": exampleMeaning,
                "note": note,
                "status": "new",
                "dateAdded": "2026-10-14"
            })
            existing_texts.add(text.lower())
            idx += 1

    return items

def main():
    root = Path(__file__).resolve().parent.parent
    data_file = root / "js" / "data.js"
    json_file = root / "data_500_words.json"

    # 1. Load existing items from data_500_words.json
    with open(json_file, "r", encoding="utf-8") as f:
        existing_items = json.load(f)

    print(f"Loaded {len(existing_items)} existing advanced items.")

    # Tag existing items with level 'B2 - C1'
    for item in existing_items:
        item["level"] = "B2 - C1"

    # 2. Generate intermediate B1-B2 items
    b1_items = generate_full_intermediate_dataset()
    print(f"Generated {len(b1_items)} intermediate (B1 - B2) items.")

    # 3. Combine both lists
    combined_items = existing_items + b1_items
    print(f"Total merged flashcard items: {len(combined_items)}")

    # 4. Save to data_500_words.json (or full data json)
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(combined_items, f, ensure_ascii=False, indent=2)
    print("Updated data_500_words.json successfully.")

    # 5. Extract unique topics
    topics = list(dict.fromkeys([item["topic"] for item in combined_items if item.get("topic")]))

    # 6. Generate js/data.js
    js_content = f"// Bộ dữ liệu {len(combined_items)} từ vựng & mẫu câu TIẾNG ANH ĐA CẤP ĐỘ (Trung cấp B1 - B2 & Nâng cao B2 - C1)\n"
    js_content += "const INITIAL_DATA = " + json.dumps(combined_items, ensure_ascii=False, indent=4) + ";\n\n"
    js_content += "const DEFAULT_TOPICS = " + json.dumps(topics, ensure_ascii=False, indent=4) + ";\n\n"
    js_content += "if (typeof module !== 'undefined' && module.exports) {\n"
    js_content += "    module.exports = { INITIAL_DATA, DEFAULT_TOPICS };\n"
    js_content += "}\n"

    with open(data_file, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Updated js/data.js successfully.")

if __name__ == "__main__":
    main()
