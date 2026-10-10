# -*- coding: utf-8 -*-
"""
Script to generate the complete 21 Reading & Dialogue modules (6 original + 15 new).
Includes distinct Male & Female speaker tagging for all conversations,
comprehensive Vietnamese translations, key vocabulary with IPA,
and 4 multiple-choice questions per module with pedagogical explanations.
"""
import json
import os

READING_DATA = [
    # ---------------- MODULE 1 ----------------
    {
        "id": "read-1",
        "title": "Contract Negotiation & Scope Alignment",
        "type": "conversation",
        "topic": "Công sở & Đàm phán",
        "level": "B2 - C1",
        "summary": "Cuộc đàm phán hợp đồng phần mềm giữa Giám đốc dự án và Đại diện khách hàng về ngân sách và thời hạn bàn giao.",
        "content": [
            { "speaker": "David (Male / Project Lead)", "text": "Good morning, Sarah. Thank you for making time today. We reviewed your requested revisions for the enterprise software rollout, particularly the expedited timeline." },
            { "speaker": "Sarah (Female / Client Rep)", "text": "Good morning, David. We appreciate your quick turnaround. As you know, our board expects the new billing system to go live before the third quarter to avoid fiscal overlap." },
            { "speaker": "David (Male / Project Lead)", "text": "We completely understand your strategic urgency. However, accelerating delivery by six weeks introduces substantial risks regarding security audits and stress testing. If we rush deployment, we risk system bottlenecks during peak transaction hours." },
            { "speaker": "Sarah (Female / Client Rep)", "text": "I see your point. Reliability is paramount for our financial operations. Is there a viable compromise that protects data integrity without forfeiting our third-quarter launch?" },
            { "speaker": "David (Male / Project Lead)", "text": "Precisely. We propose a phased implementation. We can deploy the core payment gateway and customer accounts on your target date, while deferring advanced analytics and automated reporting to phase two, four weeks later." },
            { "speaker": "Sarah (Female / Client Rep)", "text": "That sounds pragmatic. It addresses our immediate operational need while mitigating technical vulnerabilities. Does this phased approach impact the agreed budget?" },
            { "speaker": "David (Male / Project Lead)", "text": "The overall contract price remains unchanged. We merely reallocate engineering hours to prioritize core functionalities first." },
            { "speaker": "Sarah (Female / Client Rep)", "text": "Excellent. Please draft an addendum with this milestone schedule, and I will submit it to our executive committee for final sign-off." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **David (Nam / Trưởng dự án):** Chào buổi sáng, Sarah. Cảm ơn cô đã dành thời gian hôm nay. Chúng tôi đã xem xét các yêu cầu chỉnh sửa của bên cô cho đợt triển khai phần mềm doanh nghiệp, đặc biệt là tiến độ gấp rút.\n
- **Sarah (Nữ / Đại diện khách hàng):** Chào David. Chúng tôi đánh giá cao sự phản hồi nhanh chóng của bên anh. Như anh đã biết, hội đồng quản trị của chúng tôi kỳ vọng hệ thống thanh toán mới sẽ đi vào hoạt động trước quý 3 để tránh trùng lặp năm tài chính.\n
- **David (Nam / Trưởng dự án):** Chúng tôi hoàn toàn hiểu tính cấp bách mang tính chiến lược của bên cô. Tuy nhiên, việc đẩy nhanh tiến độ bàn giao sớm 6 tuần sẽ tiềm ẩn rủi ro đáng kể liên quan đến kiểm toán bảo mật và thử nghiệm chịu tải. Nếu vội vàng triển khai, hệ thống có nguy cơ nghẽn mạng vào giờ cao điểm.\n
- **Sarah (Nữ / Đại diện khách hàng):** Tôi hiểu quan điểm của anh. Độ tin cậy là điều tối quan trọng đối với hoạt động tài chính của chúng tôi. Liệu có phương án thỏa hiệp khả thi nào vừa bảo vệ tính toàn vẹn dữ liệu mà không làm lỡ đợt ra mắt quý 3 không?\n
- **David (Nam / Trưởng dự án):** Chính xác là vậy. Chúng tôi đề xuất triển khai theo giai đoạn. Chúng ta có thể đưa cổng thanh toán cốt lõi và tài khoản khách hàng vận hành đúng ngày mục tiêu của cô, trong khi dời phần phân tích nâng cao và báo cáo tự động sang giai đoạn hai, sau đó 4 tuần.\n
- **Sarah (Nữ / Đại diện khách hàng):** Nghe rất thực tế. Cách này giải quyết được nhu cầu vận hành tức thì trong khi giảm thiểu các lỗ hổng kỹ thuật. Liệu cách tiếp cận theo giai đoạn này có ảnh hưởng đến ngân sách đã thỏa thuận không?\n
- **David (Nam / Trưởng dự án):** Tổng giá trị hợp đồng vẫn giữ nguyên. Chúng tôi chỉ phân bổ lại số giờ kỹ thuật để ưu tiên các chức năng cốt lõi trước.\n
- **Sarah (Nữ / Đại diện khách hàng):** Tuyệt vời. Xin hãy soạn một phụ lục hợp đồng với lịch trình các cột mốc này, tôi sẽ nộp lên ban điều hành để ký duyệt chính thức.""",
        "keyVocab": [
            { "word": "expedited timeline", "ipa": "/ˈek.spə.daɪ.t̬ɪd ˈtaɪm.laɪn/", "meaning": "tiến độ được đẩy nhanh/rút ngắn" },
            { "word": "paramount", "ipa": "/ˈper.ə.maʊnt/", "meaning": "tối quan trọng, hàng đầu" },
            { "word": "bottleneck", "ipa": "/ˈbɑː.t̬əl.nek/", "meaning": "điểm nghẽn, sự đình trệ" },
            { "word": "phased implementation", "ipa": "/feɪzd ˌɪm.plə.menˈteɪ.ʃən/", "meaning": "triển khai chia theo từng giai đoạn" },
            { "word": "addendum", "ipa": "/əˈden.dəm/", "meaning": "phụ lục bổ sung hợp đồng" }
        ],
        "questions": [
            {
                "id": "q-1-1",
                "question": "What is Sarah's primary concern regarding the project's launch date?",
                "options": [
                    "A. Her team wants to cancel the contract before quarterly reviews.",
                    "B. The board requires the system live before Q3 to avoid financial fiscal overlap.",
                    "C. The company lacks the budget to pay for Phase 2 development.",
                    "D. Competitors are releasing a similar billing portal on the same day."
                ],
                "answerIndex": 1,
                "explanation": "Trong bài, Sarah nói: 'our board expects the new billing system to go live before the third quarter to avoid fiscal overlap' (Hội đồng quản trị yêu cầu hệ thống vận hành trước Q3 để tránh trùng lặp tài khóa)."
            },
            {
                "id": "q-1-2",
                "question": "Why does David advise against rushing the entire software deployment?",
                "options": [
                    "A. His engineering team has taken an unexpected vacation.",
                    "B. The client refused to pay the mandatory upfront deposit.",
                    "C. Rushing compromises security audits and risks server bottlenecks during peak hours.",
                    "D. Advanced analytics are impossible to develop on current servers."
                ],
                "answerIndex": 2,
                "explanation": "David giải thích: 'accelerating delivery by six weeks introduces substantial risks regarding security audits and stress testing... system bottlenecks during peak transaction hours'."
            },
            {
                "id": "q-1-3",
                "question": "What compromise does David propose to meet the client's deadline?",
                "options": [
                    "A. Eliminating customer account security verification permanently.",
                    "B. Outsourcing data storage to an unverified third-party provider.",
                    "C. Delaying the entire software release until the end of the year.",
                    "D. Launching core features on schedule and deferring advanced reporting to Phase 2."
                ],
                "answerIndex": 3,
                "explanation": "David đề xuất: 'a phased implementation. We can deploy the core payment gateway... while deferring advanced analytics and automated reporting to phase two'."
            },
            {
                "id": "q-1-4",
                "question": "How does the proposed phased implementation affect the overall financial cost?",
                "options": [
                    "A. The contract price increases by twenty-five percent.",
                    "B. The overall contract price remains unchanged as hours are merely reallocated.",
                    "C. The client receives a fifty percent discount for accepting delays.",
                    "D. Sarah must pay immediate cash bonuses to the engineering leads."
                ],
                "answerIndex": 1,
                "explanation": "David khẳng định rõ: 'The overall contract price remains unchanged. We merely reallocate engineering hours to prioritize core functionalities first'."
            }
        ]
    },

    # ---------------- MODULE 2 ----------------
    {
        "id": "read-2",
        "title": "The Transformative Role of AI in Contemporary Medicine",
        "type": "passage",
        "topic": "Khoa học & Công nghệ",
        "level": "B2 - C1",
        "summary": "Đoạn văn phân tích cách trí tuệ nhân tạo đang cách mạng hóa chẩn đoán y khoa, đồng thời đặt ra những thách thức về đạo đức và trách nhiệm giải trình.",
        "content": "The integration of artificial intelligence into diagnostic healthcare represents one of the most remarkable technological paradigm shifts of the twenty-first century. For decades, medical practitioners relied strictly on empirical clinical observation, manual laboratory assays, and radiological scans interpreted solely through human judgment. While experienced clinicians possess profound diagnostic intuition, human stamina is intrinsically finite, and cognitive fatigue inevitably impairs diagnostic precision during prolonged shifts.\n\nDeep learning convolutional neural networks have begun augmenting clinical workflows by analyzing vast databases of high-resolution magnetic resonance imaging (MRI) and computerized tomography (CT) scans. In oncology, specialized algorithms routinely detect micro-calcifications and malignant cellular clusters several months before they become perceptible to the naked human eye. By cross-referencing patient biometric histories with millions of digitized international clinical records, predictive algorithms also calculate individualized risk scores for cardiovascular deterioration, empowering physicians to prescribe preventative interventions well before acute episodes occur.\n\nNonetheless, medical ethicists caution against premature euphoria. A central challenge lies in the \"black box\" dilemma—the inherent opacity of deep neural networks whose internal weighting mechanisms are largely inscrutable even to their software architects. When an autonomous algorithmic system recommends an invasive surgical intervention or withholds a life-saving therapy, establishing legal liability and ethical accountability becomes intensely contentious. If a flawed recommendation arises from skewed training datasets that underrepresent specific demographic groups, diagnostic disparities are perpetuated rather than eradicated.\n\nConsequently, the prevailing consensus within the international medical community advocates for an augmented intelligence model rather than outright clinical automation. In this framework, artificial intelligence functions as an indispensable copilot: synthesizing complex telemetry, flagging anomalies, and eliminating repetitive clerical administrative burdens, while leaving empathetic bedside communication, nuanced ethical deliberations, and ultimate treatment authorization firmly in human hands.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Việc tích hợp trí tuệ nhân tạo vào chẩn đoán y tế đại diện cho một trong những bước chuyển đổi hệ hình công nghệ đáng chú ý nhất của thế kỷ 21. Trong nhiều thập kỷ, các bác sĩ chỉ dựa vào quan sát lâm sàng thực nghiệm, các xét nghiệm thủ công trong phòng thí nghiệm và phim chụp X-quang được diễn giải hoàn toàn bằng đánh giá của con người. Mặc dù các bác sĩ giàu kinh nghiệm sở hữu trực giác chẩn đoán sâu sắc, sức bền của con người về bản chất là có hạn, và sự mệt mỏi về nhận thức chắc chắn làm suy giảm độ chính xác của chẩn đoán trong các ca trực kéo dài.\n
Mạng nơ-ron tích chập học sâu đã bắt đầu hỗ trợ quy trình lâm sàng bằng cách phân tích cơ sở dữ liệu khổng lồ gồm các ảnh chụp cộng hưởng từ (MRI) và cắt lớp vi tính (CT) độ phân giải cao. Trong khoa ung bướu, các thuật toán chuyên biệt thường xuyên phát hiện các ổ vi vôi hóa và các cụm tế bào ác tính vài tháng trước khi chúng có thể nhìn thấy bằng mắt thường. Bằng cách đối chiếu lịch sử sinh trắc học của bệnh nhân với hàng triệu hồ sơ bệnh án quốc tế được số hóa, các thuật toán dự đoán cũng tính toán điểm rủi ro cá nhân hóa đối với sự suy giảm tim mạch, trao quyền cho bác sĩ kê đơn can thiệp phòng ngừa rất lâu trước khi các đợt cấp tính xảy ra.\n
Tuy nhiên, các nhà đạo đức học y tế cảnh báo không nên quá lạc quan sớm. Một thách thức cốt lõi nằm ở thế tiến thoái lưỡng nan "hộp đen"—sự mờ đục vốn có của các mạng nơ-ron sâu mà các cơ chế trọng số bên trong của chúng phần lớn là không thể hiểu thấu ngay cả đối với chính các kiến trúc sư phần mềm tạo ra chúng. Khi một hệ thống thuật toán tự chủ đề xuất một can thiệp phẫu thuật xâm lấn hoặc từ chối một liệu pháp cứu mạng, việc xác định trách nhiệm pháp lý và trách nhiệm giải trình đạo đức trở nên vô cùng căng thẳng. Nếu một khuyến nghị sai sót phát sinh từ bộ dữ liệu huấn luyện bị lệch thiên lệch, vốn ít đại diện cho các nhóm nhân khẩu học cụ thể, thì sự chênh lệch trong chẩn đoán sẽ bị duy trì kéo dài thay vì bị loại bỏ.\n
Do đó, sự đồng thuận phổ biến trong cộng đồng y tế quốc tế ủng hộ mô hình "trí tuệ tăng cường" thay vì tự động hóa lâm sàng hoàn toàn. Trong khuôn khổ này, trí tuệ nhân tạo hoạt động như một trợ lý không thể thiếu: tổng hợp dữ liệu viễn thám phức tạp, gắn cờ các điểm bất thường và loại bỏ gánh nặng hành chính lặp đi lặp lại, đồng thời để việc giao tiếp thấu cảm bên giường bệnh, những cân nhắc đạo đức tinh tế và quyết định điều trị cuối cùng nằm chắc chắn trong tay con người.""",
        "keyVocab": [
            { "word": "paradigm shift", "ipa": "/ˈper.ə.daɪm ʃɪft/", "meaning": "bước chuyển đổi hệ hình tư duy/công nghệ" },
            { "word": "micro-calcification", "ipa": "/ˌmaɪ.kroʊ kæl.sə.fəˈkeɪ.ʃən/", "meaning": "vi vôi hóa (dấu hiệu sớm của khối u ác tính)" },
            { "word": "black box dilemma", "ipa": "/blæk bɑːks dɪˈlem.ə/", "meaning": "thế tiến thoái lưỡng nan về tính không minh bạch của AI" },
            { "word": "inscrutable", "ipa": "/ɪnˈskruː.t̬ə.bəl/", "meaning": "khôn dò, không thể giải mã/hiểu thấu" },
            { "word": "augmented intelligence", "ipa": "/ɑːɡˈmen.t̬ɪd ɪnˈtel.ə.dʒəns/", "meaning": "trí tuệ tăng cường (AI hỗ trợ con người thay vì thay thế)" }
        ],
        "questions": [
            {
                "id": "q-2-1",
                "question": "According to paragraph 1, what is a primary limitation of purely human medical diagnosis?",
                "options": [
                    "A. Human doctors are incapable of showing empathy to bedridden patients.",
                    "B. Experienced clinicians completely lack diagnostic intuition.",
                    "C. Cognitive exhaustion during long shifts inevitably diminishes human diagnostic precision.",
                    "D. Medical schools no longer instruct students in manual laboratory assays."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 1 nêu rõ: 'human stamina is intrinsically finite, and cognitive fatigue inevitably impairs diagnostic precision during prolonged shifts' (sự mệt mỏi nhận thức làm suy giảm độ chính xác chẩn đoán)."
            },
            {
                "id": "q-2-2",
                "question": "How do deep learning networks aid oncologists in cancer detection?",
                "options": [
                    "A. By replacing surgical oncologists inside active operating rooms.",
                    "B. By spotting micro-calcifications and malignant cell clusters months before they are visible to the naked human eye.",
                    "C. By producing synthetic chemical pharmaceuticals without regulatory authorization.",
                    "D. By eliminating the necessity of taking patient radiological scans altogether."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 nêu: 'algorithms routinely detect micro-calcifications and malignant cellular clusters several months before they become perceptible to the naked human eye'."
            },
            {
                "id": "q-2-3",
                "question": "What ethical concern is highlighted regarding the 'black box' dilemma in healthcare algorithms?",
                "options": [
                    "A. The high electricity cost of running cloud graphics processing units.",
                    "B. The difficulty in assigning liability and accountability when opaque internal algorithms produce flawed advice.",
                    "C. Patients refusing to look at computerized screens during checkups.",
                    "D. Software developers demanding clinical medical degrees."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 phân tích: 'the inherent opacity of deep neural networks whose internal weighting mechanisms are largely inscrutable... establishing legal liability and ethical accountability becomes intensely contentious'."
            },
            {
                "id": "q-2-4",
                "question": "What is the prevailing medical consensus regarding future clinical workflow design?",
                "options": [
                    "A. An augmented intelligence model where AI copilots synthesize data while humans retain final authority and empathy.",
                    "B. Complete algorithmic automation where physical hospitals operate without human physicians.",
                    "C. Banning artificial intelligence completely from clinical environments.",
                    "D. Diagnostic software should only be deployed in veterinary medicine."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn cuối kết luận: 'advocates for an augmented intelligence model... artificial intelligence functions as an indispensable copilot... while leaving empathetic bedside communication... and ultimate treatment authorization firmly in human hands'."
            }
        ]
    },

    # ---------------- MODULE 3 ----------------
    {
        "id": "read-3",
        "title": "Resolving Interdepartmental Friction",
        "type": "conversation",
        "topic": "Công sở & Đàm phán",
        "level": "B2 - C1",
        "summary": "Cuộc đối thoại giữa Trưởng phòng Tiếp thị và Nữ Trưởng phòng Kỹ thuật nhằm tháo gỡ bất đồng về tính năng sản phẩm và cam kết với khách hàng.",
        "content": [
            { "speaker": "Liam (Male / Marketing Director)", "text": "Elena, thanks for sitting down with me. We noticed some tension during yesterday's all-hands briefing regarding the Q4 feature roadmap." },
            { "speaker": "Elena (Female / Head of Engineering)", "text": "I'll be candid, Liam. The marketing team announced real-time collaboration features in your public promotional webinars before engineering even finalized the backend architecture. That puts unfair pressure on my developers." },
            { "speaker": "Liam (Male / Marketing Director)", "text": "I acknowledge your frustration. Our sales reps were facing aggressive counter-campaigns from our primary rival, and we felt compelled to demonstrate our competitive edge. But I admit we jumped the gun without verifying sprint capacities." },
            { "speaker": "Elena (Female / Head of Engineering)", "text": "When marketing makes promises without technical vetting, it leads to two bad outcomes: either we cut corners on code quality and release buggy software, or my team burns the midnight oil and suffers demoralizing burnout." },
            { "speaker": "Liam (Male / Marketing Director)", "text": "Neither outcome is acceptable to anyone in leadership. Let's establish a formal synchronization protocol. Moving forward, marketing will not publicize any capability that has not cleared stage-three QA testing." },
            { "speaker": "Elena (Female / Head of Engineering)", "text": "I appreciate that commitment. In return, I will designate a senior technical lead to attend your bi-weekly campaign brainstorms to provide realistic feasibility assessments early on." },
            { "speaker": "Liam (Male / Marketing Director)", "text": "That would be immensely helpful. It guarantees that our client messaging remains innovative while grounded in technical reality." },
            { "speaker": "Elena (Female / Head of Engineering)", "text": "Agreed. Let us communicate this unified alignment to our respective departments this afternoon." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Liam (Nam / Giám đốc Tiếp thị):** Elena, cảm ơn cô đã ngồi lại cùng tôi. Chúng tôi nhận thấy có chút căng thẳng trong buổi họp toàn thể hôm qua liên quan đến lộ trình tính năng quý 4.\n
- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Tôi xin nói thẳng thắn, Liam. Đội tiếp thị của anh đã công bố các tính năng cộng tác theo thời gian thực trên các hội thảo quảng bá công khai trước khi đội kỹ thuật hoàn tất kiến trúc phụ trợ. Điều đó tạo ra áp lực bất công lên các lập trình viên của tôi.\n
- **Liam (Nam / Giám đốc Tiếp thị):** Tôi thừa nhận sự bức xúc của cô. Đội ngũ bán hàng của chúng tôi đang phải đối mặt với các chiến dịch đối đầu gay gắt từ đối thủ cạnh tranh chính, và chúng tôi cảm thấy buộc phải thể hiện lợi thế cạnh tranh của mình. Nhưng tôi thừa nhận chúng tôi đã vội vàng cầm đèn chạy trước ô tô mà chưa xác minh công suất của đợt chạy nước rút (sprint).\n
- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Khi tiếp thị hứa hẹn mà không có sự kiểm tra kỹ thuật, điều đó dẫn đến hai kết quả tồi tệ: hoặc là chúng tôi làm ẩu giảm chất lượng mã nguồn và phát hành phần mềm nhiều lỗi, hoặc là đội của tôi phải thức thâu đêm làm việc và bị kiệt sức làm suy giảm tinh thần.\n
- **Liam (Nam / Giám đốc Tiếp thị):** Cả hai kết cục đó đều không thể chấp nhận được đối với ban lãnh đạo. Chúng ta hãy thiết lập một quy trình đồng bộ hóa chính thức. Kể từ nay trở đi, tiếp thị sẽ không công bố bất kỳ tính năng nào chưa vượt qua bài kiểm tra đảm bảo chất lượng (QA) giai đoạn ba.\n
- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Tôi đánh giá cao cam kết đó. Đổi lại, tôi sẽ chỉ định một trưởng nhóm kỹ thuật cao cấp tham gia các buổi thảo luận chiến dịch hai tuần một lần của bên anh để đưa ra các đánh giá tính khả thi thực tế ngay từ đầu.\n
- **Liam (Nam / Giám đốc Tiếp thị):** Điều đó sẽ vô cùng hữu ích. Nó đảm bảo thông điệp gửi tới khách hàng của chúng ta vừa mang tính đổi mới vừa dựa trên thực tế kỹ thuật.\n
- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Nhất trí. Chiều nay chúng ta hãy truyền đạt sự thống nhất này tới các phòng ban tương ứng của mình.""",
        "keyVocab": [
            { "word": "candid", "ipa": "/ˈkæn.dɪd/", "meaning": "thẳng thắn, bộc trực" },
            { "word": "jump the gun", "ipa": "/dʒʌmp ðə ɡʌn/", "meaning": "cầm đèn chạy trước ô tô, hành động quá vội vàng" },
            { "word": "cut corners", "ipa": "/kʌt ˈkɔːr.nɚz/", "meaning": "làm ẩu, bớt xén quy trình" },
            { "word": "burn the midnight oil", "ipa": "/bɜːrn ðə ˈmɪd.naɪt ɔɪl/", "meaning": "thức khuya miệt mài làm việc" },
            { "word": "technical vetting", "ipa": "/ˈtek.nɪ.kəl ˈvet̬.ɪŋ/", "meaning": "sự kiểm tra/thẩm định kỹ thuật" }
        ],
        "questions": [
            {
                "id": "q-3-1",
                "question": "What initiated the conflict between Marketing and Engineering?",
                "options": [
                    "A. Engineering demanded a fifty percent budget increase for software tools.",
                    "B. Marketing announced features publicly before Engineering finalized the architecture.",
                    "C. Both departments wanted to lay off junior staff members.",
                    "D. Liam publicly accused Elena of financial fraud during a press conference."
                ],
                "answerIndex": 1,
                "explanation": "Elena giải thích nguyên nhân: 'The marketing team announced real-time collaboration features in your public promotional webinars before engineering even finalized the backend architecture'."
            },
            {
                "id": "q-3-2",
                "question": "Why did Liam's team rush to announce the new features?",
                "options": [
                    "A. They wanted to sabotage the engineering team's morale.",
                    "B. They were legally obligated by government regulations to advertise immediately.",
                    "C. They were countering aggressive competitor marketing and wanted to show an edge.",
                    "D. They had already received advance payments from all corporate subscribers."
                ],
                "answerIndex": 2,
                "explanation": "Liam chia sẻ: 'Our sales reps were facing aggressive counter-campaigns from our primary rival, and we felt compelled to demonstrate our competitive edge'."
            },
            {
                "id": "q-3-3",
                "question": "What two negative outcomes does Elena warn will occur if false promises continue?",
                "options": [
                    "A. Higher office rent and reduced lunch breaks.",
                    "B. Hardware fires and data center relocations.",
                    "C. Cutting corners resulting in buggy code, or developer burnout from overwork.",
                    "D. Immediate bankruptcy and loss of cloud hosting licenses."
                ],
                "answerIndex": 2,
                "explanation": "Elena cảnh báo: 'either we cut corners on code quality and release buggy software, or my team burns the midnight oil and suffers demoralizing burnout'."
            },
            {
                "id": "q-3-4",
                "question": "What systemic solution do both leaders agree upon for future projects?",
                "options": [
                    "A. Merging both departments under a single external contractor.",
                    "B. Marketing will only announce features after Stage 3 QA, and an engineering lead will attend brainstorms.",
                    "C. Canceling all feature announcements permanently until next year.",
                    "D. Banning sales reps from attending company webinars."
                ],
                "answerIndex": 1,
                "explanation": "Liam cam kết marketing không công bố tính năng chưa qua QA stage-3, và Elena đồng ý cử một senior technical lead tham gia các buổi họp chiến dịch tiếp thị."
            }
        ]
    },

    # ---------------- MODULE 4 ----------------
    {
        "id": "read-4",
        "title": "The Architecture of Sustainable Urban Ecosystems",
        "type": "passage",
        "topic": "Môi trường & Xã hội",
        "level": "B2 - C1",
        "summary": "Bài luận về việc tái cấu trúc các đại đô thị hiện đại nhằm giảm thiểu phát thải carbon, tích hợp không gian xanh và thúc đẩy giao thông bền vững.",
        "content": "By the mid-twenty-first century, demographic projections estimate that over two-thirds of the planetary population will reside in metropolitan sprawls. Rapid, uncontrolled urbanization historically inflicted catastrophic ecological tolls: vast swathes of heat-absorbing asphalt, rampant carbon emissions from combustion-engine gridlock, and the widespread eradication of native biodiversity. In response, avant-garde urban planners are repudiating the legacy twentieth-century ethos of car-centric zoning in favor of regenerative, circular urban design.\n\nAt the forefront of this transformation is the \"15-minute city\" paradigm, which reorganizes urban topology so that essential daily amenities—grocery markets, primary healthcare centers, educational facilities, and communal parks—are accessible within a quarter-hour walk or bicycle ride from any residence. By decentralizing public infrastructure, municipalities curtail vehicular dependency, dramatically suppressing localized nitrogen dioxide and particulate emissions while invigorating neighborhood social cohesion.\n\nSimultaneously, structural engineering is experiencing an organic renaissance through the adoption of biophilic architecture and carbon-sequestering building materials. Traditional concrete and steel production generates approximately fifteen percent of global greenhouse emissions. Progressive developers are pioneering structural cross-laminated timber (CLT)—sustainably harvested wood engineered to match the compressive strength of reinforced concrete while functioning as a permanent carbon sink. Furthermore, retrofitting urban facades with vertical forests and permeable sponge-city pavements mitigates the deadly urban heat island effect, allowing metropolitan centers to absorb flash flood monsoons naturally.\n\nNevertheless, implementing systemic urban regeneration requires navigating precarious socioeconomic fault lines. Aggressive infrastructural beautification frequently precipitates \"green gentrification\"—an inflationary cycle where escalating property valuations displace long-standing low-income communities who endured decades of environmental disinvestment. Therefore, genuine urban sustainability cannot remain a purely architectural pursuit; it necessitates rigorous municipal rent stabilization covenants and equitable transit equity subsidies to guarantee that cleaner, greener cities shelter all socioeconomic tiers unconditionally.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Đến giữa thế kỷ 21, các dự báo nhân khẩu học ước tính rằng hơn 2/3 dân số hành tinh sẽ cư trú tại các đô thị mở rộng. Quá trình đô thị hóa nhanh chóng, mất kiểm soát trong lịch sử đã gây ra những tổn thất sinh thái thảm khốc: những dải nhựa đường hấp thụ nhiệt khổng lồ, lượng khí thải carbon tràn lan từ nạn kẹt xe động cơ đốt trong và sự xóa sổ diện rộng đa dạng sinh học bản địa. Để đối phó, các nhà quy hoạch đô thị tiên phong đang bác bỏ đặc tính quy hoạch lấy xe hơi làm trung tâm của thế kỷ 20 để hướng tới thiết kế đô thị tuần hoàn, có tính tái tạo.\n
Đi đầu trong sự chuyển đổi này là mô hình "thành phố 15 phút", tổ chức lại địa hình đô thị sao cho các tiện ích thiết yếu hàng ngày—chợ tạp hóa, trung tâm y tế ban đầu, cơ sở giáo dục và công viên công cộng—có thể tiếp cận được trong vòng 15 phút đi bộ hoặc đạp xe từ bất kỳ nơi cư trú nào. Bằng cách phân cấp cơ sở hạ tầng công cộng, chính quyền đô thị hạn chế sự phụ thuộc vào phương tiện giao thông, ngăn chặn đáng kể lượng khí thải nitơ dioxide và bụi mịn cục bộ, đồng thời tiếp thêm sinh lực cho sự gắn kết xã hội trong khu phố.\n
Đồng thời, kỹ thuật kết cấu đang trải qua một thời kỳ phục hưng hữu cơ thông qua việc áp dụng kiến trúc ưa sinh học (biophilic) và các vật liệu xây dựng cô lập carbon. Sản xuất bê tông và thép truyền thống tạo ra khoảng 15% lượng khí thải nhà kính toàn cầu. Các nhà phát triển tiến bộ đang tiên phong sử dụng gỗ nhiều lớp cấu trúc (CLT)—loại gỗ được thu hoạch bền vững được chế tạo để sánh ngang với cường độ nén của bê tông cốt thép trong khi hoạt động như một bể chứa carbon vĩnh viễn. Hơn nữa, việc cải tạo các mặt đứng đô thị bằng các khu rừng thẳng đứng và vỉa hè thấm nước theo mô hình "thành phố bọt biển" giúp giảm thiểu hiệu ứng đảo nhiệt đô thị chết người, cho phép các trung tâm đô thị hấp thụ các trận lũ quét do gió mùa một cách tự nhiên.\n
Tuy nhiên, việc thực hiện tái tạo đô thị mang tính hệ thống đòi hỏi phải vượt qua những ranh giới kinh tế xã hội bấp bênh. Việc chỉnh trang cơ sở hạ tầng quá mức thường dẫn đến "chỉnh trang đô thị xanh" (green gentrification)—một chu kỳ lạm phát nơi giá trị bất động sản leo thang làm dịch chuyển, đẩy những cộng đồng thu nhập thấp lâu đời, những người đã chịu đựng hàng thập kỷ thiếu đầu tư môi trường, ra khỏi nơi ở. Do đó, tính bền vững đô thị thực sự không thể chỉ là một mục tiêu kiến trúc thuần túy; nó đòi hỏi các thỏa ước bình ổn giá thuê nhà nghiêm ngặt của chính quyền thành phố và các khoản trợ cấp bình đẳng về giao thông công cộng để đảm bảo rằng các thành phố sạch hơn, xanh hơn sẽ che chở cho tất cả các tầng lớp kinh tế xã hội một cách vô điều kiện.""",
        "keyVocab": [
            { "word": "metropolitan sprawl", "ipa": "/ˌmet.rəˈpɑː.lɪ.tən sprɑːl/", "meaning": "sự mở rộng đô thị quá mức" },
            { "word": "15-minute city", "ipa": "/ˌfɪf.tiːn ˈmɪn.ɪt ˈsɪt.i/", "meaning": "mô hình đô thị tiện ích 15 phút" },
            { "word": "cross-laminated timber", "ipa": "/krɑːs ˈlæm.ə.neɪ.t̬ɪd ˈtɪm.bɚ/", "meaning": "gỗ dán nhiều lớp cấu trúc chịu lực (CLT)" },
            { "word": "sponge-city pavement", "ipa": "/spʌndʒ ˈsɪt.i ˈpeɪv.mənt/", "meaning": "vỉa hè thấm nước theo mô hình thành phố bọt biển" },
            { "word": "green gentrification", "ipa": "/ɡriːn ˌdʒen.trə.fəˈkeɪ.ʃən/", "meaning": "chỉnh trang xanh đẩy giá nhà cao khiến người nghèo bị di dời" }
        ],
        "questions": [
            {
                "id": "q-4-1",
                "question": "What is the core principle of the '15-minute city' model mentioned in paragraph 2?",
                "options": [
                    "A. Highway speed limits must allow drivers to cross cities in 15 minutes.",
                    "B. All citizens must work exactly 15 hours per week.",
                    "C. Daily amenities should be accessible within a 15-minute walk or bike ride from home.",
                    "D. Commuters are banned from using public buses during morning peak hours."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 2 giải thích: 'essential daily amenities... are accessible within a quarter-hour walk or bicycle ride from any residence'."
            },
            {
                "id": "q-4-2",
                "question": "Why is cross-laminated timber (CLT) praised by progressive structural developers?",
                "options": [
                    "A. It acts as a permanent carbon sink while matching the strength of reinforced concrete.",
                    "B. It is entirely waterproof without needing any chemical treatments.",
                    "C. It is completely transparent and replaces window glass.",
                    "D. It generates electricity when exposed to rainfall."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 3 chỉ ra: 'engineered to match the compressive strength of reinforced concrete while functioning as a permanent carbon sink'."
            },
            {
                "id": "q-4-3",
                "question": "What is 'green gentrification' as defined in paragraph 4?",
                "options": [
                    "A. Planting too many trees causing allergies among office workers.",
                    "B. Property value inflation following eco-upgrades that displaces low-income residents.",
                    "C. Cities losing green spaces to illegal industrial strip mining.",
                    "D. Governments imposing heavy fines on electric bicycle riders."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 4 nêu: 'an inflationary cycle where escalating property valuations displace long-standing low-income communities who endured decades of environmental disinvestment'."
            },
            {
                "id": "q-4-4",
                "question": "What does the author suggest to ensure urban sustainability is socially equitable?",
                "options": [
                    "A. Banning all private property ownership in downtown areas.",
                    "B. Forcing all citizens to live in high-rise timber apartments.",
                    "C. Implementing municipal rent stabilization and equitable transit subsidies.",
                    "D. Relying exclusively on private real estate philanthropy."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn cuối kết luận: 'necessitates rigorous municipal rent stabilization covenants and equitable transit equity subsidies to guarantee that cleaner, greener cities shelter all socioeconomic tiers unconditionally'."
            }
        ]
    },

    # ---------------- MODULE 5 ----------------
    {
        "id": "read-5",
        "title": "Flight Cancellation & Emergency Rerouting",
        "type": "conversation",
        "topic": "Du lịch & Tình huống khẩn cấp",
        "level": "B1 - B2",
        "summary": "Tình huống giao tiếp thực tế tại quầy dịch vụ sân bay quốc tế khi hành khách bị hủy chuyến bay nối chuyến do bão tuyết.",
        "content": [
            { "speaker": "James (Male / Stranded Passenger)", "text": "Excuse me, miss. My connecting flight to Frankfurt, LH 402, was abruptly marked as canceled on the departures board. I have an indispensable business summit tomorrow morning." },
            { "speaker": "Emily (Female / Airline Customer Representative)", "text": "I truly apologize for the disruption, sir. A severe blizzard over northern Europe prompted ground stops across several hub airports. Let me pull up your booking reference." },
            { "speaker": "James (Male / Stranded Passenger)", "text": "Here is my passport and boarding pass. Are there any partner airlines operating flights later this evening, even with an alternate layover?" },
            { "speaker": "Emily (Female / Airline Customer Representative)", "text": "Let me check our Star Alliance network. There is a Swiss International Air flight departing at 9:30 PM via Zurich with a two-hour transfer, landing in Frankfurt at 7:15 AM tomorrow." },
            { "speaker": "James (Male / Stranded Passenger)", "text": "That would get me to my conference just in the nick of time. Can you confirm a confirmed seat for me on that route?" },
            { "speaker": "Emily (Female / Airline Customer Representative)", "text": "Yes, I managed to secure an aisle seat in economy. I am transferring your checked baggage directly to the Zurich route, so you will not need to re-claim it here." },
            { "speaker": "James (Male / Stranded Passenger)", "text": "That is a huge relief. Since I have a five-hour wait until the 9:30 PM departure, does the airline provide meal compensation?" },
            { "speaker": "Emily (Female / Airline Customer Representative)", "text": "Certainly. Here is a thirty-euro meal voucher valid at any terminal restaurant, alongside your updated boarding passes. Gate B22 opens at 8:45 PM." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **James (Nam / Hành khách bị lỡ chuyến):** Xin lỗi cô. Chuyến bay nối chuyến của tôi đi Frankfurt, số hiệu LH 402, vừa đột ngột bị thông báo hủy trên bảng khởi hành. Tôi có một hội nghị kinh doanh tối quan trọng vào sáng mai.\n
- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Tôi rất xin lỗi vì sự gián đoạn này, thưa quý khách. Một trận bão tuyết dữ dội ở Bắc Âu đã khiến nhiều sân bay trung chuyển phải dừng bay mặt đất. Xin để tôi mở mã đặt chỗ của quý khách.\n
- **James (Nam / Hành khách bị lỡ chuyến):** Hộ chiếu và thẻ lên máy bay của tôi đây. Liệu có hãng bay đối tác nào có chuyến bay tối nay không, kể cả phải quá cảnh ở điểm khác?\n
- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Để tôi kiểm tra trong mạng lưới liên minh Star Alliance. Có một chuyến bay của hãng Thụy Sĩ (Swiss International Air) khởi hành lúc 9:30 tối quá cảnh qua Zurich trong 2 giờ, hạ cánh xuống Frankfurt lúc 7:15 sáng mai.\n
- **James (Nam / Hành khách bị lỡ chuyến):** Lịch trình đó sẽ giúp tôi đến hội nghị vừa kịp lúc sát nút. Cô có thể xác nhận cho tôi một ghế chắc chắn trên chuyến bay đó không?\n
- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Vâng, tôi đã giữ được một ghế lối đi ở hạng phổ thông cho quý khách. Tôi đang chuyển hành lý ký gửi của quý khách trực tiếp sang chặng Zurich, nên quý khách không cần phải lấy lại hành lý tại đây.\n
- **James (Nam / Hành khách bị lỡ chuyến):** Thật là nhẹ nhõm. Vì tôi phải chờ 5 tiếng cho đến giờ bay 9:30 tối, hãng có bồi hoàn bữa ăn không?\n
- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Chắc chắn rồi ạ. Đây là phiếu ăn trị giá 30 euro có giá trị tại bất kỳ nhà hàng nào trong nhà ga, cùng với thẻ lên máy bay mới của quý khách. Cửa B22 sẽ mở lúc 8:45 tối ạ.""",
        "keyVocab": [
            { "word": "indispensable", "ipa": "/ˌɪn.dɪˈspen.sə.bəl/", "meaning": "không thể thiếu, tối quan trọng" },
            { "word": "blizzard", "ipa": "/ˈblɪz.ɚd/", "meaning": "cơn bão tuyết dữ dội" },
            { "word": "layover", "ipa": "/ˈleɪˌoʊ.vɚ/", "meaning": "thời gian quá cảnh/dừng nghỉ giữa chuyến bay" },
            { "word": "in the nick of time", "ipa": "/ɪn ðə nɪk əv taɪm/", "meaning": "vừa kịp lúc, sát nút" },
            { "word": "meal voucher", "ipa": "/miːl ˈvaʊ.tʃɚ/", "meaning": "phiếu ăn miễn phí bồi hoàn" }
        ],
        "questions": [
            {
                "id": "q-5-1",
                "question": "Why was James's initial flight to Frankfurt canceled?",
                "options": [
                    "A. The airline went bankrupt without advance warning.",
                    "B. A severe blizzard over northern Europe triggered ground stops.",
                    "C. James arrived at the airport two hours after boarding closed.",
                    "D. Frankfurt Airport was permanently closed for renovations."
                ],
                "answerIndex": 1,
                "explanation": "Emily giải thích: 'A severe blizzard over northern Europe prompted ground stops across several hub airports'."
            },
            {
                "id": "q-5-2",
                "question": "What alternative itinerary does Emily find for James?",
                "options": [
                    "A. A high-speed overnight train through the Alps.",
                    "B. A flight departing tomorrow evening direct to Berlin.",
                    "C. A 9:30 PM flight via Zurich that arrives in Frankfurt at 7:15 AM tomorrow.",
                    "D. A cruise ship departing from Hamburg."
                ],
                "answerIndex": 2,
                "explanation": "Emily tìm thấy: 'Swiss International Air flight departing at 9:30 PM via Zurich with a two-hour transfer, landing in Frankfurt at 7:15 AM tomorrow'."
            },
            {
                "id": "q-5-3",
                "question": "What happens to James's checked baggage?",
                "options": [
                    "A. It is automatically transferred directly to the new Zurich route.",
                    "B. James must reclaim it from the carousel and re-check it immediately.",
                    "C. It was accidentally lost and declared unrecoverable.",
                    "D. The airline will ship it to his home address next week."
                ],
                "answerIndex": 0,
                "explanation": "Emily khẳng định: 'I am transferring your checked baggage directly to the Zurich route, so you will not need to re-claim it here'."
            },
            {
                "id": "q-5-4",
                "question": "What compensation does the airline offer James for his five-hour wait?",
                "options": [
                    "A. A free ticket to any destination in Europe.",
                    "B. A luxury limousine ride to a five-star hotel.",
                    "C. A thirty-euro meal voucher valid at any terminal restaurant.",
                    "D. Free upgrades to First Class on all future flights."
                ],
                "answerIndex": 2,
                "explanation": "Emily cung cấp: 'Here is a thirty-euro meal voucher valid at any terminal restaurant, alongside your updated boarding passes'."
            }
        ]
    },

    # ---------------- MODULE 6 ----------------
    {
        "id": "read-6",
        "title": "The Psychology of Habit Formation & Cognitive Momentum",
        "type": "passage",
        "topic": "Tâm lý & Nhận thức",
        "level": "B2 - C1",
        "summary": "Phân tích khoa học thần kinh về cách não bộ hình thành thói quen thông qua vòng lặp gợi ý - hành động - phần thưởng, và chiến lược xây dựng đà nhận thức bền vững.",
        "content": "Human behavior is fundamentally dictated not by conscious, deliberative willpower, but by deeply automated neural habit loops. Cognitive neuroscientists estimate that between forty to fifty percent of daily human activities—from brushing teeth to reflexively checking smartphone feeds—are executed under subcortical automaticity. The brain, evolved to conserve scarce glucose, continually seeks to streamline repetitive decision-making by delegating routine behavioral sequences to the basal ganglia.\n\nThis automaticity operates via a three-part mechanism: the cue, the routine, and the reward. The cue acts as a sensory or temporal trigger that alerts the brain to initiate a specialized behavioral routine. Once the behavior executes, the brain receives a biochemical reward—frequently a pulse of dopamine—which reinforces neural synaptic pathways, cementing the likelihood that the routine will recur upon subsequent exposure to the identical cue. Over time, anticipation of the reward transforms into a subconscious neurological craving.\n\nCrucially, common self-help doctrines that urge individuals to rely exclusively on raw willpower to overhaul their lives fail to appreciate the physiology of cognitive depletion. Deliberate decision-making resides in the prefrontal cortex, a metabolically demanding brain region susceptible to decision fatigue. Under prolonged emotional stress or physical exhaustion, prefrontal executive control atrophies, causing the individual to default reflexively to hardwired, legacy habit routines—often destructive vices like compulsive snacking or sedentary procrastination.\n\nConsequently, behavioral architects advocate for \"habit stacking\" and environmental optimization rather than heroic self-discipline. By anchoring a desired nascent habit directly onto an immutable pre-existing routine (for example: \"Immediately after pouring my morning coffee, I will review ten English vocabulary cards for five minutes\"), friction is minimized. Furthermore, designing an environment where beneficial cues are glaringly obvious and counterproductive distractions are physically obstructed leverages the brain's innate inertia, transforming deliberate aspirations into frictionless, lifelong momentum.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Hành vi của con người về cơ bản không được quyết định bởi ý chí có ý thức, suy tính kỹ lưỡng, mà bởi các vòng lặp thói quen thần kinh tự động hóa sâu sắc. Các nhà khoa học thần kinh nhận thức ước tính rằng từ 40 đến 50% các hoạt động hàng ngày của con người—từ đánh răng đến phản xạ kiểm tra bảng tin điện thoại thông minh—được thực hiện dưới sự tự động hóa của vùng dưới vỏ não. Bộ não, vốn tiến hóa để bảo tồn lượng glucose khan hiếm, liên tục tìm cách tinh giản việc ra quyết định lặp đi lặp lại bằng cách ủy quyền các chuỗi hành vi thường nhật cho hạch nền (basal ganglia).\n
Cơ chế tự động hóa này vận hành thông qua một quy trình ba phần: gợi ý (cue), thói quen hành động (routine) và phần thưởng (reward). Gợi ý đóng vai trò là tác nhân kích hoạt cảm giác hoặc thời gian báo cho não bắt đầu một chuỗi hành động chuyên biệt. Sau khi hành vi thực hiện xong, não nhận được phần thưởng sinh hóa—thường là một đợt giải phóng dopamine—giúp củng cố các đường dẫn synap thần kinh, khắc sâu khả năng thói quen đó sẽ tái diễn khi gặp lại gợi ý giống hệt. Theo thời gian, sự mong đợi phần thưởng sẽ biến thành một cơn thèm muốn thần kinh trong tiềm thức.\n
Điều quan trọng là các giáo lý phát triển bản thân phổ biến thúc giục các cá nhân chỉ dựa vào ý chí đơn thuần để thay đổi cuộc sống đã không nhận thức được sinh lý học của sự cạn kiệt nhận thức. Việc ra quyết định có chủ ý nằm ở vỏ não trước trán, một vùng não đòi hỏi nhiều năng lượng trao đổi chất và rất dễ bị mệt mỏi khi phải ra quyết định liên tục. Dưới sự căng thẳng cảm xúc kéo dài hoặc kiệt sức thể chất, khả năng kiểm soát điều hành của vỏ não trước trán bị suy giảm, khiến cá nhân quay trở lại một cách vô thức với các thói quen cũ đã ăn sâu—thường là những tật xấu tiêu cực như ăn vặt theo cảm xúc hoặc trì hoãn thụ động.\n
Do đó, các nhà kiến trúc hành vi ủng hộ phương pháp "xếp chồng thói quen" (habit stacking) và tối ưu hóa môi trường hơn là sự tự kỷ luật phi thường mang tính anh hùng. Bằng cách gắn một thói quen mới mong muốn trực tiếp vào một thói quen cũ đã bất biến (ví dụ: "Ngay sau khi rót cà phê buổi sáng, tôi sẽ xem lại 10 thẻ từ vựng tiếng Anh trong 5 phút"), lực cản sẽ được giảm thiểu. Hơn nữa, việc thiết kế một môi trường nơi các tín hiệu có lợi hiển hiện rõ ràng và những thứ gây xao nhãng phản tác dụng bị cản trở về mặt vật lý sẽ tận dụng quán tính bẩm sinh của não bộ, biến những khát vọng có chủ ý thành đà phát triển trơn tru, bền bỉ suốt đời.""",
        "keyVocab": [
            { "word": "automaticity", "ipa": "/ˌɑː.t̬ə.məˈtɪs.ə.t̬i/", "meaning": "tính tự động hóa trong phản xạ thần kinh" },
            { "word": "basal ganglia", "ipa": "/ˈbeɪ.səl ˈɡæŋ.ɡli.ə/", "meaning": "hạch nền não bộ (nơi lưu trữ thói quen tự động)" },
            { "word": "decision fatigue", "ipa": "/dɪˈsɪʒ.ən fəˈtiːɡ/", "meaning": "sự mệt mỏi khi phải đưa ra quá nhiều quyết định" },
            { "word": "habit stacking", "ipa": "/ˈhæb.ɪt ˈstæk.ɪŋ/", "meaning": "kỹ thuật xếp chồng thói quen mới lên thói quen cũ" },
            { "word": "cognitive momentum", "ipa": "/ˈkɑːɡ.nə.t̬ɪv moʊˈmen.t̬əm/", "meaning": "đà phát triển nhận thức trơn tru không ma sát" }
        ],
        "questions": [
            {
                "id": "q-6-1",
                "question": "According to cognitive neuroscientists, what portion of daily human activity is driven by habit loops?",
                "options": [
                    "A. Less than five percent.",
                    "B. Exactly one hundred percent.",
                    "C. Between forty and fifty percent.",
                    "D. Only during nighttime sleep cycles."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 1 chỉ rõ: 'Cognitive neuroscientists estimate that between forty to fifty percent of daily human activities... are executed under subcortical automaticity'."
            },
            {
                "id": "q-6-2",
                "question": "What are the three core components of the neurological habit loop?",
                "options": [
                    "A. Memory, ambition, and punishment.",
                    "B. The cue, the routine, and the reward.",
                    "C. Genetic heritage, diet, and physical exercise.",
                    "D. Prefrontal willpower, social peer pressure, and dopamine."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 nêu định nghĩa: 'This automaticity operates via a three-part mechanism: the cue, the routine, and the reward'."
            },
            {
                "id": "q-6-3",
                "question": "Why does relying purely on raw willpower often fail over time?",
                "options": [
                    "A. The prefrontal cortex suffers from metabolic decision fatigue under stress and exhaustion.",
                    "B. Human beings are genetically incapable of learning foreign languages.",
                    "C. Dopamine receptors completely shut down after age twenty-five.",
                    "D. Willpower is an imaginary concept invented by advertising firms."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 3 giải thích: 'Deliberate decision-making resides in the prefrontal cortex, a metabolically demanding brain region susceptible to decision fatigue. Under prolonged emotional stress or physical exhaustion, prefrontal executive control atrophies'."
            },
            {
                "id": "q-6-4",
                "question": "What is an effective example of 'habit stacking' described in the text?",
                "options": [
                    "A. Refusing to sleep until fifty vocabulary textbooks are memorized.",
                    "B. Reviewing ten vocabulary cards immediately after pouring morning coffee.",
                    "C. Drinking six cups of coffee while studying throughout the night.",
                    "D. Deleting all social media accounts permanently every weekend."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 4 minh họa cụ thể: 'anchoring a desired nascent habit directly onto an immutable pre-existing routine (for example: \"Immediately after pouring my morning coffee, I will review ten English vocabulary cards for five minutes\")'."
            }
        ]
    },

    # ---------------- MODULE 7 (NEW) ----------------
    {
        "id": "read-7",
        "title": "Cross-Border Supply Chain Disruption",
        "type": "conversation",
        "topic": "Logistics & Thương mại quốc tế",
        "level": "B2 - C1",
        "summary": "Cuộc thảo luận khẩn cấp giữa Giám đốc Vận tải Quốc tế và Nữ Giám đốc Thu mua Toàn cầu để điều phối lộ trình vận chuyển sau sự cố tắc nghẽn cảng biển.",
        "content": [
            { "speaker": "Marcus (Male / Logistics Director)", "text": "Lin, we just received an alert from our freight forwarding syndicate. Severe port congestion at the regional transshipment hub has delayed our inbound container vessels by at least twelve days." },
            { "speaker": "Lin (Female / Global Sourcing Manager)", "text": "That is alarming, Marcus. Our domestic assembly facilities are operating on a lean inventory model. If the semiconductor modules don't arrive by Tuesday, our production line faces an indefinite standstill." },
            { "speaker": "Marcus (Male / Logistics Director)", "text": "We anticipated this bottleneck. I have already initiated contingency protocols with air-freight carriers. We can air-lift twenty metric tons of critical chips directly from the fabrication plant to stave off a factory shutdown." },
            { "speaker": "Lin (Female / Global Sourcing Manager)", "text": "Air cargo rates are currently four times higher than maritime transit. How will this cost spike impact our quarterly procurement margins?" },
            { "speaker": "Marcus (Male / Logistics Director)", "text": "The freight premium will indeed increase logistical overhead by approximately eighty thousand dollars. However, the contractual penalties for halting client deliveries would surpass half a million dollars." },
            { "speaker": "Lin (Female / Global Sourcing Manager)", "text": "When you frame it against liquidated damages, the expenditure is entirely justified. What about the non-urgent bulk raw materials?" },
            { "speaker": "Marcus (Male / Logistics Director)", "text": "Those will be rerouted via secondary feeder vessels to a less congested neighboring terminal and trucked overland." },
            { "speaker": "Lin (Female / Global Sourcing Manager)", "text": "Splendid decision. Please authorize the air charters immediately and keep me posted on customs clearance timestamps." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Lin, chúng ta vừa nhận được cảnh báo từ nghiệp đoàn giao nhận vận tải. Tình trạng tắc nghẽn nghiêm trọng tại cảng trung chuyển khu vực đã làm chậm các tàu chở container cập bến ít nhất 12 ngày.\n
- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Điều đó thật đáng báo động, Marcus. Các cơ sở lắp ráp trong nước của chúng ta đang vận hành theo mô hình tồn kho tinh gọn. Nếu các mô-đun bán dẫn không đến trước thứ Ba, dây chuyền sản xuất sẽ phải dừng hoạt động vô thời hạn.\n
- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Chúng tôi đã lường trước nút thắt cổ chai này. Tôi đã kích hoạt các quy trình dự phòng với các hãng vận chuyển hàng không. Chúng ta có thể không vận 20 tấn chip quan trọng trực tiếp từ nhà máy chế tạo để ngăn chặn việc đóng cửa nhà máy.\n
- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Giá cước hàng không hiện cao gấp 4 lần vận tải đường biển. Sự tăng vọt chi phí này sẽ ảnh hưởng thế nào đến biên lợi nhuận thu mua quý của chúng ta?\n
- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Phí chênh lệch vận chuyển thực sự sẽ làm tăng chi phí hậu cần khoảng 80.000 USD. Tuy nhiên, các khoản phạt hợp đồng do ngừng giao hàng cho khách hàng sẽ vượt quá nửa triệu đô la.\n
- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Khi so sánh với tiền bồi thường thiệt hại theo hợp đồng, khoản chi này hoàn toàn chính đáng. Còn các nguyên liệu thô số lượng lớn không khẩn cấp thì sao?\n
- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Những chuyến hàng đó sẽ được chuyển hướng qua các tàu gom hàng phụ đến một bến cảng lân cận ít tắc nghẽn hơn và vận chuyển bằng đường bộ.\n
- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Quyết định tuyệt vời. Xin vui lòng phê duyệt các chuyến bay thuê chuyến ngay lập tức và cập nhật cho tôi mốc thời gian thông quan hải quan.""",
        "keyVocab": [
            { "word": "freight forwarding syndicate", "ipa": "/freɪt ˈfɔːr.wɚ.dɪŋ ˈsɪn.dɪ.kət/", "meaning": "nghiệp đoàn/tập đoàn giao nhận vận tải" },
            { "word": "lean inventory model", "ipa": "/liːn ˈɪn.vən.tɔːri ˈmɑː.dəl/", "meaning": "mô hình quản lý kho tinh gọn" },
            { "word": "stave off", "ipa": "/steɪv ɔːf/", "meaning": "ngăn chặn tạm thời (khủng hoảng, đình trệ)" },
            { "word": "liquidated damages", "ipa": "/ˈlɪk.wə.deɪ.t̬ɪd ˈdæm.ɪ.dʒɪz/", "meaning": "tiền bồi thường thiệt hại ấn định trong hợp đồng" },
            { "word": "customs clearance", "ipa": "/ˈkʌs.təmz ˈklɪr.əns/", "meaning": "thủ tục thông quan hải quan" }
        ],
        "questions": [
            {
                "id": "q-7-1",
                "question": "What logistics emergency has arisen according to Marcus?",
                "options": [
                    "A. Customs officials seized all cargo due to counterfeit paperwork.",
                    "B. Severe port congestion delayed inbound container vessels by twelve days.",
                    "C. A maritime collision destroyed all semiconductor inventory.",
                    "D. Warehouse workers launched an indefinite strike across Europe."
                ],
                "answerIndex": 1,
                "explanation": "Marcus thông báo ngay câu đầu: 'Severe port congestion at the regional transshipment hub has delayed our inbound container vessels by at least twelve days'."
            },
            {
                "id": "q-7-2",
                "question": "Why is the delay particularly critical for Lin's assembly facilities?",
                "options": [
                    "A. The assembly plants are scheduled for demolition next month.",
                    "B. The facilities operate on a lean inventory model and will halt without chips by Tuesday.",
                    "C. The company does not possess electricity generator backups.",
                    "D. Overseas clients have canceled all contractual purchase orders."
                ],
                "answerIndex": 1,
                "explanation": "Lin giải thích: 'Our domestic assembly facilities are operating on a lean inventory model. If the semiconductor modules don't arrive by Tuesday, our production line faces an indefinite standstill'."
            },
            {
                "id": "q-7-3",
                "question": "How does Marcus justify the eighty-thousand-dollar expense of air freight?",
                "options": [
                    "A. The airline offered complimentary first-class seats for executives.",
                    "B. Contractual breach penalties for delivery failure would exceed half a million dollars.",
                    "C. Maritime shipping companies refunded all previous transit fees.",
                    "D. The government covers all air transportation expenses during crises."
                ],
                "answerIndex": 1,
                "explanation": "Marcus so sánh: 'The freight premium will indeed increase logistical overhead by approximately eighty thousand dollars. However, the contractual penalties for halting client deliveries would surpass half a million dollars'."
            },
            {
                "id": "q-7-4",
                "question": "What is the secondary plan for non-urgent bulk materials?",
                "options": [
                    "A. Discarding them in oceanic international waters.",
                    "B. Selling them to competitor manufacturers at scrap value.",
                    "C. Rerouting them via feeder vessels to a less congested terminal and trucking overland.",
                    "D. Storing them in maritime containers indefinitely until next year."
                ],
                "answerIndex": 2,
                "explanation": "Marcus nêu rõ: 'Those will be rerouted via secondary feeder vessels to a less congested neighboring terminal and trucked overland'."
            }
        ]
    },

    # ---------------- MODULE 8 (NEW) ----------------
    {
        "id": "read-8",
        "title": "The Neurological Underpinnings of Bilingualism",
        "type": "passage",
        "topic": "Não bộ & Ngôn ngữ học",
        "level": "B2 - C1",
        "summary": "Nghiên cứu về cách bộ não đa ngôn ngữ định hình lại cấu trúc tế bào thần kinh, tăng cường khả năng kiểm soát điều hành và làm chậm sự khởi phát của chứng sa sút trí tuệ.",
        "content": "For centuries, educational dogma erroneously asserted that teaching children multiple languages simultaneously would burden immature cognitive faculties, precipitating linguistic confusion and developmental delays. Modern cognitive neuroscience has resoundingly refuted this misconception. Structural neuroimaging investigations demonstrate that managing multiple linguistic codes alters the brain's micro-architecture, fostering superior neural plasticity and reinforcing executive control networks housed within the dorsolateral prefrontal cortex.\n\nAt the core of the bilingual cognitive advantage is the relentless demand for attentional inhibition. In a bilingual brain, both linguistic systems remain perpetually active in parallel. When a bilingual speaker formulates an utterance, semantic concepts activate candidate representations in both tongues simultaneously. To articulate a coherent sentence without unwanted lexical intrusion, the brain's executive control system must actively suppress the competing, non-target language while amplifying the target vocabulary. This continuous mental workout strengthens domain-general inhibitory mechanisms, enabling bilingual individuals to excel in tasks demanding cognitive flexibility, selective attention, and rapid task-switching.\n\nFurthermore, the neuroprotective implications of sustained bilingualism are profound. Longitudinal epidemiological studies reveal that lifelong bilingual individuals manifest symptomatic onset of neurodegenerative disorders, such as Alzheimer's disease, approximately four to five years later than monolingual peers matched for socioeconomic background and education. While bilingualism does not shield neural tissue from microscopic tau tangles or amyloid plaques, it builds formidable \"cognitive reserve.\" The enriched synaptic connectivity provides alternative compensatory neural pathways, allowing individuals to maintain lucid everyday functioning despite underlying pathological degradation.\n\nUltimately, acquiring an additional language transcends communicative utility; it is a profound form of cognitive gymnastics. By compelling the brain to navigate competing linguistic frameworks continually, bilingualism endows individuals with resilient neural scaffolding that withstands cognitive wear throughout the human lifespan.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Trong nhiều thế kỷ, giáo điều sư phạm đã khẳng định sai lầm rằng việc dạy trẻ em nhiều ngôn ngữ cùng lúc sẽ tạo gánh nặng cho năng lực nhận thức non nớt, gây ra sự nhầm lẫn ngôn ngữ và chậm phát triển. Khoa học thần kinh nhận thức hiện đại đã bác bỏ hoàn toàn quan niệm sai lầm này. Các cuộc điều tra hình ảnh thần kinh cấu trúc chứng minh rằng việc quản lý nhiều hệ thống ngôn ngữ làm thay đổi cấu trúc vi mô của não, thúc đẩy tính mềm dẻo thần kinh vượt trội và củng cố các mạng lưới kiểm soát điều hành nằm trong vỏ não trước trán lưng bên.\n
Cốt lõi của lợi thế nhận thức song ngữ là nhu cầu liên tục về sự ức chế chú ý. Trong bộ não song ngữ, cả hai hệ thống ngôn ngữ luôn duy trì hoạt động song song. Khi người nói song ngữ hình thành một phát ngôn, các khái niệm ngữ nghĩa sẽ kích hoạt các biểu diễn ứng viên ở cả hai ngôn ngữ cùng một lúc. Để nói ra một câu mạch lạc mà không bị xâm nhập từ vựng ngoài ý muốn, hệ thống kiểm soát điều hành của não phải chủ động ức chế ngôn ngữ cạnh tranh (không phải mục tiêu) trong khi khuếch đại từ vựng mục tiêu. Sự rèn luyện tinh thần liên tục này củng cố các cơ chế ức chế chung, giúp các cá nhân song ngữ vượt trội trong các nhiệm vụ đòi hỏi sự linh hoạt nhận thức, chú ý có chọn lọc và chuyển đổi nhiệm vụ nhanh chóng.\n
Hơn nữa, ý nghĩa bảo vệ thần kinh của việc sử dụng song ngữ lâu dài là vô cùng sâu sắc. Các nghiên cứu dịch tễ học theo chiều dọc cho thấy rằng những người song ngữ suốt đời biểu hiện các triệu chứng khởi phát của các rối loạn thoái hóa thần kinh, chẳng hạn như bệnh Alzheimer, muộn hơn khoảng 4 đến 5 năm so với những người đơn ngữ có cùng hoàn cảnh kinh tế xã hội và trình độ học vấn. Mặc dù song ngữ không che chở cho mô thần kinh khỏi các đám rối tau vi thể hoặc mảng amyloid, nhưng nó xây dựng nên một \"dự trữ nhận thức\" đáng gờm. Khả năng kết nối synap phong phú cung cấp các con đường thần kinh bù trừ thay thế, cho phép các cá nhân duy trì hoạt động hàng ngày minh mẫn bất chấp sự suy thoái bệnh lý tiềm ẩn.\n
Cuối cùng, việc tiếp thu thêm một ngôn ngữ vượt xa tiện ích giao tiếp thông thường; đó là một hình thức tập thể dục nhận thức sâu sắc. Bằng cách buộc não bộ liên tục điều hướng các khuôn khổ ngôn ngữ cạnh tranh, song ngữ ban tặng cho các cá nhân một giàn giáo thần kinh kiên cường, chống chọi lại sự hao mòn nhận thức trong suốt cuộc đời.""",
        "keyVocab": [
            { "word": "educational dogma", "ipa": "/ˌedʒ.əˈkeɪ.ʃən.əl ˈdɑːɡ.mə/", "meaning": "giáo điều sư phạm cũ kỹ" },
            { "word": "attentional inhibition", "ipa": "/əˈten.ʃən.əl ˌɪn.həˈbɪʃ.ən/", "meaning": "sự ức chế chú ý (gạt bỏ thông tin nhiễu)" },
            { "word": "task-switching", "ipa": "/tæsk ˈswɪtʃ.ɪŋ/", "meaning": "khả năng chuyển đổi qua lại giữa các tác vụ" },
            { "word": "cognitive reserve", "ipa": "/ˈkɑːɡ.nə.t̬ɪv rɪˈzɜːrv/", "meaning": "dự trữ nhận thức chống đỡ thoái hóa não" },
            { "word": "compensatory pathway", "ipa": "/kəmˈpen.sə.tɔːr.i ˈpæθ.weɪ/", "meaning": "con đường thần kinh bù trừ thay thế" }
        ],
        "questions": [
            {
                "id": "q-8-1",
                "question": "What historical misconception about childhood bilingualism does modern neuroscience refute?",
                "options": [
                    "A. That bilingual children develop superhuman photographic memory.",
                    "B. That acquiring multiple languages causes mental confusion and developmental delay.",
                    "C. That monolingual children learn mathematical concepts twice as fast.",
                    "D. That bilingualism causes permanent hearing loss in early childhood."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu: 'For centuries, educational dogma erroneously asserted that teaching children multiple languages simultaneously would burden immature cognitive faculties, precipitating linguistic confusion and developmental delays'."
            },
            {
                "id": "q-8-2",
                "question": "How does the bilingual brain prevent lexical interference during speech formulation?",
                "options": [
                    "A. By permanently forgetting one language whenever speaking the other.",
                    "B. By speaking both languages simultaneously in every conversation.",
                    "C. By using executive control to suppress the non-target language while amplifying the target tongue.",
                    "D. By whispering words before saying them aloud."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 2 giải thích: 'the brain's executive control system must actively suppress the competing, non-target language while amplifying the target vocabulary'."
            },
            {
                "id": "q-8-3",
                "question": "According to epidemiological studies, how does lifelong bilingualism impact neurodegenerative diseases?",
                "options": [
                    "A. It completely cures all known genetic neurological conditions.",
                    "B. It delays the symptomatic onset of Alzheimer's by approximately four to five years.",
                    "C. It speeds up the accumulation of brain plaques.",
                    "D. It eliminates the need for medical care after age seventy."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 chỉ ra: 'manifest symptomatic onset of neurodegenerative disorders... approximately four to five years later than monolingual peers'."
            },
            {
                "id": "q-8-4",
                "question": "What is the primary function of 'cognitive reserve' built through bilingualism?",
                "options": [
                    "A. Storing audio recordings inside the cerebellum.",
                    "B. Providing compensatory neural pathways to maintain lucid functioning despite underlying pathology.",
                    "C. Increasing physical bone density and stamina.",
                    "D. Preventing eye fatigue during long reading sessions."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 kết luận: 'The enriched synaptic connectivity provides alternative compensatory neural pathways, allowing individuals to maintain lucid everyday functioning despite underlying pathological degradation'."
            }
        ]
    },

    # ---------------- MODULE 9 (NEW) ----------------
    {
        "id": "read-9",
        "title": "Quarterly Performance Appraisal & Salary Review",
        "type": "conversation",
        "topic": "Nhân sự & Phát triển sự nghiệp",
        "level": "B2 - C1",
        "summary": "Buổi đánh giá hiệu suất công việc và đàm phán thăng tiến giữa Trưởng phòng Kỹ thuật và Nữ Chuyên gia Khoa học Dữ liệu cấp cao.",
        "content": [
            { "speaker": "Richard (Male / Department Head)", "text": "Chloe, thank you for coming in. Your self-evaluation submitted last Friday was exceptionally thorough. I want to formally review your contributions to our Q3 data engineering initiatives." },
            { "speaker": "Chloe (Female / Senior Data Scientist)", "text": "Thank you, Richard. Over the past nine months, I concentrated primarily on overhauling our customer churn prediction architecture and reducing algorithm training latency." },
            { "speaker": "Richard (Male / Department Head)", "text": "The executive committee took note. Your predictive churn model yielded an eight percent boost in customer retention, translating directly into nearly three million dollars in recurring annual revenue." },
            { "speaker": "Chloe (Female / Senior Data Scientist)", "text": "I'm delighted by those outcomes. Beyond model accuracy, I also mentored two junior analysts and established rigorous documentation standards across our code repositories." },
            { "speaker": "Richard (Male / Department Head)", "text": "Your leadership maturity has been evident. Therefore, management is enthusiastically recommending your promotion to Lead Machine Learning Architect." },
            { "speaker": "Chloe (Female / Senior Data Scientist)", "text": "I truly appreciate that recognition. In conjunction with this expanded architectural scope, I would like to discuss compensation alignment. Based on current industry benchmarks for lead roles, I am seeking a twelve percent base salary adjustment." },
            { "speaker": "Richard (Male / Department Head)", "text": "Given standard corporate compensation bands, a twelve percent immediate jump in base salary requires executive sign-off. However, I can offer an eight percent base increase immediately, paired with a higher tranche of performance-based equity options." },
            { "speaker": "Chloe (Female / Senior Data Scientist)", "text": "That package demonstrates strong alignment with long-term company valuation. If we can incorporate a performance bonus tied to Q1 model deployment milestones, I would gladly accept." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Richard (Nam / Trưởng phòng Kỹ thuật):** Chloe, cảm ơn cô đã đến. Bản tự đánh giá cô nộp thứ Sáu tuần trước rất kỹ lưỡng. Tôi muốn chính thức xem xét những đóng góp của cô cho các sáng kiến kỹ thuật dữ liệu quý 3 của chúng ta.\n
- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Cảm ơn Richard. Trong 9 tháng qua, tôi tập trung chủ yếu vào việc đại tu kiến trúc dự đoán tỷ lệ khách hàng rời bỏ và giảm độ trễ huấn luyện thuật toán.\n
- **Richard (Nam / Trưởng phòng Kỹ thuật):** Ban điều hành đã ghi nhận điều đó. Mô hình dự đoán khách hàng rời bỏ của cô đã mang lại mức tăng 8% trong việc giữ chân khách hàng, trực tiếp chuyển hóa thành gần 3 triệu đô la doanh thu định kỳ hàng năm.\n
- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Tôi rất vui mừng về những kết quả đó. Ngoài độ chính xác của mô hình, tôi cũng đã hướng dẫn 2 nhà phân tích cấp dưới và thiết lập các tiêu chuẩn tài liệu nghiêm ngặt trên toàn bộ kho mã nguồn.\n
- **Richard (Nam / Trưởng phòng Kỹ thuật):** Sự trưởng thành trong vai trò lãnh đạo của cô rất rõ rệt. Vì vậy, ban quản lý nhiệt liệt đề xuất thăng chức cho cô lên vị trí Kiến trúc sư Trưởng Học máy (Lead ML Architect).\n
- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Tôi thực sự đánh giá cao sự công nhận đó. Đi đôi với phạm vi kiến trúc mở rộng này, tôi muốn thảo luận về việc điều chỉnh mức đãi ngộ. Dựa trên các tiêu chuẩn ngành hiện tại cho các vai trò trưởng nhóm, tôi mong muốn mức điều chỉnh lương cơ bản là 12%.\n
- **Richard (Nam / Trưởng phòng Kỹ thuật):** Với khung lương tiêu chuẩn của công ty, mức tăng ngay 12% lương cơ bản cần sự phê duyệt của ban điều hành. Tuy nhiên, tôi có thể đề xuất mức tăng 8% lương cơ bản ngay lập tức, kết hợp với một đợt phân bổ quyền chọn cổ phiếu hiệu suất cao hơn.\n
- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Gói đãi ngộ đó thể hiện sự gắn kết chặt chẽ với giá trị dài hạn của công ty. Nếu chúng ta có thể kết hợp thêm khoản thưởng hiệu suất gắn với các cột mốc triển khai mô hình quý 1, tôi rất sẵn lòng đồng ý.""",
        "keyVocab": [
            { "word": "performance appraisal", "ipa": "/pɚˈfɔːr.məns əˈpreɪ.zəl/", "meaning": "đánh giá hiệu suất công việc định kỳ" },
            { "word": "churn prediction", "ipa": "/tʃɜːrn prɪˈdɪk.ʃən/", "meaning": "dự đoán tỷ lệ khách hàng rời bỏ dịch vụ" },
            { "word": "recurring revenue", "ipa": "/rɪˈkɝː.ɪŋ ˈrev.ə.nuː/", "meaning": "doanh thu định kỳ lặp lại" },
            { "word": "compensation band", "ipa": "/ˌkɑːm.penˈseɪ.ʃən bænd/", "meaning": "khung bậc lương và đãi ngộ chuẩn" },
            { "word": "equity options", "ipa": "/ˈek.wə.t̬i ˈɑːp.ʃənz/", "meaning": "quyền chọn cổ phần doanh nghiệp" }
        ],
        "questions": [
            {
                "id": "q-9-1",
                "question": "What measurable business impact did Chloe's predictive churn model achieve?",
                "options": [
                    "A. It reduced server electricity consumption by fifty percent.",
                    "B. It boosted customer retention by 8%, generating nearly $3 million in recurring revenue.",
                    "C. It doubled the total head count of the engineering department.",
                    "D. It completely automated customer service support without humans."
                ],
                "answerIndex": 1,
                "explanation": "Richard chỉ rõ: 'Your predictive churn model yielded an eight percent boost in customer retention, translating directly into nearly three million dollars in recurring annual revenue'."
            },
            {
                "id": "q-9-2",
                "question": "What leadership contribution did Chloe emphasize beyond raw model accuracy?",
                "options": [
                    "A. Organizing monthly social sporting outings.",
                    "B. Taking over all human resources recruiting interviews.",
                    "C. Mentoring junior analysts and establishing rigorous documentation standards.",
                    "D. Negotiating software discounts with cloud hosting vendors."
                ],
                "answerIndex": 2,
                "explanation": "Chloe chia sẻ: 'I also mentored two junior analysts and established rigorous documentation standards across our code repositories'."
            },
            {
                "id": "q-9-3",
                "question": "What new promotion title is management offering Chloe?",
                "options": [
                    "A. Chief Operating Officer.",
                    "B. Lead Machine Learning Architect.",
                    "C. Junior Database Administrator.",
                    "D. Marketing Campaign Coordinator."
                ],
                "answerIndex": 1,
                "explanation": "Richard thông báo: 'management is enthusiastically recommending your promotion to Lead Machine Learning Architect'."
            },
            {
                "id": "q-9-4",
                "question": "What counter-proposal does Richard offer regarding compensation?",
                "options": [
                    "A. A pay cut accompanied by longer office working hours.",
                    "B. An 8% base salary increase plus a higher tranche of equity options.",
                    "C. Immediate cash payment in cryptocurrency.",
                    "D. A six-month unpaid sabbatical vacation."
                ],
                "answerIndex": 1,
                "explanation": "Richard đề xuất: 'I can offer an eight percent base increase immediately, paired with a higher tranche of performance-based equity options'."
            }
        ]
    },

    # ---------------- MODULE 10 (NEW) ----------------
    {
        "id": "read-10",
        "title": "Decentralized Finance and Sovereign Monetary Policy",
        "type": "passage",
        "topic": "Tài chính & Tiền tệ",
        "level": "B2 - C1",
        "summary": "Bài phân tích về sự trỗi dậy của tài chính phi tập trung (DeFi), hợp đồng thông minh và tác động đối với chính sách tiền tệ của các ngân hàng trung ương.",
        "content": "The emergence of decentralized finance (DeFi) represents a philosophical and technological assault on the foundational architecture of contemporary commercial banking. For over three centuries, sovereign nation-states preserved an unchallenged monopoly over monetary issuance, financial intermediation, and interest rate governance. Central banks exercised macroeconomic equilibrium by adjusting reserve requirements and managing discount window liquidity. However, open-source blockchain architectures are substituting institutional trust with mathematical cryptographic consensus.\n\nAt the operational core of decentralized finance lie smart contracts—self-executing lines of code stored on immutable distributed ledgers. In traditional capital markets, securing a commercial loan necessitates extensive underwriting, credit score verification, legal notarization, and substantial bureaucratic overhead. DeFi liquidity protocols dismantle these intermediaries. By depositing digital collateral into algorithmic automated liquidity pools, borrowers can instantly draw syndicated loans governed purely by predetermined loan-to-value ratios without human authorization.\n\nNevertheless, this algorithmic disintermediation poses severe systemic risks. While traditional banking systems feature deposit insurance safeguards and central bank lenders of last resort, DeFi ecosystems are acutely vulnerable to cascading liquidation cascades. When underlying collateral assets experience sudden market devaluation, algorithmic liquidation bots aggressively trigger automated asset dumping, depressing token valuations and generating systemic insolvency across interconnected protocols. Furthermore, the anonymity afforded by pseudo-anonymous cryptographic wallets complicates sovereign efforts to combat international capital flight and cross-border tax evasion.\n\nConsequently, central monetary authorities worldwide are accelerating initiatives to introduce Central Bank Digital Currencies (CBDCs). By synthesizing the transactional speed and programmability of blockchain tokens with the legal backing and stability of sovereign fiat currency, governments seek to neutralize DeFi's disruptive encroachment. The brewing confrontation between decentralized sovereign-free capital and state-administered programmable digital fiat will fundamentally redefine global financial governance for decades to come.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Sự xuất hiện của tài chính phi tập trung (DeFi) đại diện cho một cuộc công kích triết học và công nghệ vào kiến trúc nền tảng của ngân hàng thương mại đương đại. Trong hơn 3 thế kỷ, các quốc gia có chủ quyền đã duy trì thế độc quyền không thể tranh cãi đối với việc phát hành tiền tệ, trung gian tài chính và quản trị lãi suất. Các ngân hàng trung ương thực thi trạng thái cân bằng kinh tế vĩ mô bằng cách điều chỉnh các yêu cầu dự trữ và quản lý thanh khoản cửa sổ chiết khấu. Tuy nhiên, các kiến trúc chuỗi khối nguồn mở đang thay thế niềm tin thể chế bằng sự đồng thuận mật mã toán học.\n
Cốt lõi hoạt động của tài chính phi tập trung là các hợp đồng thông minh—những dòng mã tự thực thi được lưu trữ trên các sổ cái phân tán bất biến. Trong các thị trường vốn truyền thống, việc đảm bảo một khoản vay thương mại đòi hỏi sự bảo lãnh phát hành sâu rộng, xác minh điểm tín dụng, công chứng pháp lý và chi phí hành chính đáng kể. Các giao thức thanh khoản DeFi tháo dỡ các bên trung gian này. Bằng cách gửi tài sản thế chấp kỹ thuật số vào các quỹ thanh khoản tự động theo thuật toán, người đi vay có thể vay ngay các khoản vay hợp vốn được quản lý hoàn toàn bằng tỷ lệ khoản vay trên giá trị (LTV) định trước mà không cần sự phê duyệt của con người.\n
Tuy nhiên, sự phi trung gian hóa theo thuật toán này gây ra những rủi ro mang tính hệ thống nghiêm trọng. Trong khi các hệ thống ngân hàng truyền thống có các biện pháp bảo vệ bảo hiểm tiền gửi và người cho vay cuối cùng của ngân hàng trung ương, các hệ sinh thái DeFi rất dễ bị tổn thương trước các đợt thanh lý xếp tầng liên hoàn. Khi các tài sản thế chấp tiềm ẩn bị mất giá đột ngột, các bot thanh lý thuật toán sẽ kích hoạt bán tháo tài sản một cách quyết liệt, làm sụt giảm định giá và gây ra tình trạng mất khả năng thanh toán mang tính hệ thống trên các giao thức kết nối với nhau. Hơn nữa, tính ẩn danh của các ví mật mã làm phức tạp các nỗ lực của quốc gia nhằm chống lại dòng vốn tháo chạy quốc tế và trốn thuế xuyên biên giới.\n
Do đó, các cơ quan quản lý tiền tệ trung ương trên toàn thế giới đang đẩy nhanh các sáng kiến giới thiệu Tiền kỹ thuật số của Ngân hàng Trung ương (CBDC). Bằng cách tổng hợp tốc độ giao dịch và khả năng lập trình của các mã thông báo chuỗi khối với sự bảo đảm pháp lý và tính ổn định của tiền pháp định có chủ quyền, các chính phủ tìm cách vô hiệu hóa sự lấn sân đột phá của DeFi. Cuộc đối đầu đang hình thành giữa dòng vốn phi tập trung không có chủ quyền và tiền pháp định kỹ thuật số có thể lập trình do nhà nước quản lý sẽ định nghĩa lại cơ bản nền quản trị tài chính toàn cầu trong nhiều thập kỷ tới.""",
        "keyVocab": [
            { "word": "financial intermediation", "ipa": "/faɪˈnæn.ʃəl ˌɪn.t̬ɚˌmiː.diˈeɪ.ʃən/", "meaning": "sự trung gian tài chính (ngân hàng làm trung gian)" },
            { "word": "immutable ledger", "ipa": "/ɪˈmjuː.t̬ə.bəl ˈledʒ.ɚ/", "meaning": "sổ cái bất biến không thể sửa xóa" },
            { "word": "liquidation cascade", "ipa": "/ˌlɪk.wəˈdeɪ.ʃən kæsˈkeɪd/", "meaning": "làn sóng thanh lý tài sản thế chấp dây chuyền" },
            { "word": "lender of last resort", "ipa": "/ˈlen.dɚ əv læst rɪˈzɔːrt/", "meaning": "người cho vay cứu cánh cuối cùng (Ngân hàng Trung ương)" },
            { "word": "sovereign fiat currency", "ipa": "/ˈsɑːv.rən ˈfiː.æt ˈkɝː.ən.si/", "meaning": "tiền pháp định có chủ quyền quốc gia" }
        ],
        "questions": [
            {
                "id": "q-10-1",
                "question": "What traditional institution does decentralized finance (DeFi) seek to replace with cryptographic code?",
                "options": [
                    "A. International agricultural trade unions.",
                    "B. Commercial banking and institutional financial intermediaries.",
                    "C. Public road construction companies.",
                    "D. Postal mailing and package delivery services."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu rõ: 'an assault on the foundational architecture of contemporary commercial banking... substituting institutional trust with mathematical cryptographic consensus'."
            },
            {
                "id": "q-10-2",
                "question": "How do smart contracts eliminate bureaucratic hurdles in loan issuance?",
                "options": [
                    "A. By offering unlimited free money to all citizens without collateral.",
                    "B. By dispensing loans automatically from liquidity pools based on predetermined collateral ratios.",
                    "C. By eliminating debt repayment obligations permanently.",
                    "D. By requiring borrowers to attend in-person court hearings."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 giải thích: 'By depositing digital collateral into algorithmic automated liquidity pools, borrowers can instantly draw syndicated loans governed purely by predetermined loan-to-value ratios without human authorization'."
            },
            {
                "id": "q-10-3",
                "question": "What danger occurs when underlying collateral experiences sudden devaluation in DeFi?",
                "options": [
                    "A. Automated bots trigger cascading liquidations, threatening systemic protocol solvency.",
                    "B. Government banks immediately deposit free fiat cash to rescue borrowers.",
                    "C. All digital computers around the world automatically restart.",
                    "D. Crypto exchanges are legally absorbed into post offices."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 3 cảnh báo: 'When underlying collateral assets experience sudden market devaluation, algorithmic liquidation bots aggressively trigger automated asset dumping... generating systemic insolvency'."
            },
            {
                "id": "q-10-4",
                "question": "Why are central banks developing Central Bank Digital Currencies (CBDCs)?",
                "options": [
                    "A. To ban the internet permanently in major cities.",
                    "B. To merge blockchain speed and programmability with the stability and legal backing of sovereign fiat.",
                    "C. To encourage citizens to stop paying income taxes.",
                    "D. To abolish the legal concept of money altogether."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 4 nêu: 'By synthesizing the transactional speed and programmability of blockchain tokens with the legal backing and stability of sovereign fiat currency, governments seek to neutralize DeFi's disruptive encroachment'."
            }
        ]
    },

    # ---------------- MODULE 11 (NEW) ----------------
    {
        "id": "read-11",
        "title": "Startup Pitch & Angel Investor Interrogation",
        "type": "conversation",
        "topic": "Khởi nghiệp & Gọi vốn",
        "level": "B2 - C1",
        "summary": "Phiên thẩm định đầu tư hạt giống giữa Nhà đầu tư thiên thần và Nữ sáng lập công ty công nghệ sinh học.",
        "content": [
            { "speaker": "Julian (Male / Angel Investor)", "text": "Olivia, your investor deck for SynthoBio is certainly compelling. However, pitching a three-million-dollar pre-money valuation at the pre-revenue stage requires extraordinary justification." },
            { "speaker": "Olivia (Female / Biotech Startup Founder)", "text": "I appreciate your scrutiny, Julian. While we have not commercialized yet, we hold two broad provisional patents on our enzymatic carbon-capture biopolymer. Our bench-scale prototypes achieve ninety-two percent synthesis efficiency." },
            { "speaker": "Julian (Male / Angel Investor)", "text": "Lab bench efficiency rarely scales linearly to pilot industrial manufacturing. What is your current monthly burn rate, and what runway does this seed financing provide?" },
            { "speaker": "Olivia (Female / Biotech Startup Founder)", "text": "Our current burn rate is forty-five thousand dollars monthly, primarily allocated to analytical chemistry equipment and two PhD research salaries. Securing five hundred thousand dollars guarantees an eighteen-month runway to reach bioreactor pilot scale." },
            { "speaker": "Julian (Male / Angel Investor)", "text": "What about your regulatory clearance pathway? Environmental safety agencies scrutinize novel synthetic polymers aggressively before approving commercial packaging." },
            { "speaker": "Olivia (Female / Biotech Startup Founder)", "text": "We designed the polymer backbone strictly from GRAS—Generally Recognized As Safe—organic feedstocks. Pre-submission toxicity assays indicate zero microplastic residue, which substantially expedites our compliance trajectory." },
            { "speaker": "Julian (Male / Angel Investor)", "text": "That addresses my primary bio-hazard concern. What terms are you willing to accept on a SAFE note regarding valuation caps and discounts?" },
            { "speaker": "Olivia (Female / Biotech Startup Founder)", "text": "We are offering a standard post-money SAFE with a four-million-dollar valuation cap and a twenty percent conversion discount for our lead investor." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Julian (Nam / Nhà đầu tư thiên thần):** Olivia, hồ sơ thuyết trình đầu tư cho SynthoBio của cô chắc chắn rất hấp dẫn. Tuy nhiên, việc đưa ra mức định giá 3 triệu đô la trước khi có doanh thu đòi hỏi sự biện minh phi thường.\n
- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Tôi đánh giá cao sự xem xét kỹ lưỡng của anh, Julian. Mặc dù chúng tôi chưa thương mại hóa, nhưng chúng tôi nắm giữ 2 bằng sáng chế tạm thời đối với polyme sinh học thu giữ carbon bằng enzyme. Các mẫu thử nghiệm quy mô phòng thí nghiệm của chúng tôi đạt hiệu suất tổng hợp 92%.\n
- **Julian (Nam / Nhà đầu tư thiên thần):** Hiệu suất trong phòng thí nghiệm hiếm khi mở rộng tuyến tính lên sản xuất công nghiệp thử nghiệm. Tốc độ đốt tiền (burn rate) hàng tháng hiện tại của cô là bao nhiêu, và vòng tài trợ hạt giống này mang lại thời gian hoạt động (runway) bao lâu?\n
- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Tốc độ đốt tiền hiện tại của chúng tôi là 45.000 đô la hàng tháng, chủ yếu phân bổ cho thiết bị hóa phân tích và lương của 2 tiến sĩ nghiên cứu. Việc huy động được 500.000 đô la đảm bảo thời gian hoạt động 18 tháng để đạt quy mô thử nghiệm lò phản ứng sinh học.\n
- **Julian (Nam / Nhà đầu tư thiên thần):** Còn lộ trình phê duyệt theo quy định thì sao? Các cơ quan an toàn môi trường giám sát rất gắt gao các polyme tổng hợp mới trước khi phê duyệt bao bì thương mại.\n
- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Chúng tôi đã thiết kế khung polyme hoàn toàn từ nguyên liệu hữu cơ đạt chuẩn GRAS (Được công nhận là an toàn). Các xét nghiệm độc tính trước khi nộp hồ sơ cho thấy không có cặn vi nhựa, điều này giúp đẩy nhanh đáng kể lộ trình tuân thủ của chúng tôi.\n
- **Julian (Nam / Nhà đầu tư thiên thần):** Điều đó giải quyết mối lo ngại hàng đầu của tôi về rủi ro sinh học. Cô sẵn sàng chấp nhận các điều khoản nào trên hợp đồng SAFE về mức trần định giá và tỷ lệ chiết khấu?\n
- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Chúng tôi đưa ra thỏa thuận SAFE sau đầu tư tiêu chuẩn với mức trần định giá 4 triệu đô la và chiết khấu chuyển đổi 20% cho nhà đầu tư dẫn dắt.""",
        "keyVocab": [
            { "word": "pre-money valuation", "ipa": "/priː ˈmʌn.i ˌvæl.juˈeɪ.ʃən/", "meaning": "định giá doanh nghiệp trước khi nhận vốn" },
            { "word": "burn rate", "ipa": "/bɜːrn reɪt/", "meaning": "tốc độ tiêu tiền vốn hàng tháng của startup" },
            { "word": "runway", "ipa": "/ˈrʌn.weɪ/", "meaning": "thời gian startup có thể duy trì hoạt động trước khi cạn tiền" },
            { "word": "GRAS feedstock", "ipa": "/ɡræs ˈfiːd.stɑːk/", "meaning": "nguyên liệu được công nhận an toàn tuyệt đối" },
            { "word": "valuation cap", "ipa": "/ˌvæl.juˈeɪ.ʃən kæp/", "meaning": "mức trần định giá trong thỏa thuận đầu tư SAFE" }
        ],
        "questions": [
            {
                "id": "q-11-1",
                "question": "What makes Julian initially skeptical about Olivia's startup pitch?",
                "options": [
                    "A. Her lack of academic scientific credentials.",
                    "B. Pitching a high three-million-dollar valuation while still in the pre-revenue phase.",
                    "C. Competitors having acquired all available patent rights.",
                    "D. Her refusal to reveal the chemical formula of the product."
                ],
                "answerIndex": 1,
                "explanation": "Julian nêu nghi vấn ban đầu: 'pitching a three-million-dollar pre-money valuation at the pre-revenue stage requires extraordinary justification'."
            },
            {
                "id": "q-11-2",
                "question": "What is SynthoBio's current monthly burn rate?",
                "options": [
                    "A. Ten thousand dollars.",
                    "B. Forty-five thousand dollars.",
                    "C. Two hundred thousand dollars.",
                    "D. One million dollars."
                ],
                "answerIndex": 1,
                "explanation": "Olivia trả lời chính xác: 'Our current burn rate is forty-five thousand dollars monthly, primarily allocated to analytical chemistry equipment and two PhD research salaries'."
            },
            {
                "id": "q-11-3",
                "question": "Why does Olivia believe regulatory approval will proceed smoothly?",
                "options": [
                    "A. The government has abolished all chemical testing requirements.",
                    "B. Her father is the chief director of the environmental agency.",
                    "C. The polymer uses GRAS-certified organic feedstocks and leaves zero microplastic residue.",
                    "D. The company plans to sell products exclusively in international waters."
                ],
                "answerIndex": 2,
                "explanation": "Olivia khẳng định: 'We designed the polymer backbone strictly from GRAS... feedstocks. Pre-submission toxicity assays indicate zero microplastic residue'."
            },
            {
                "id": "q-11-4",
                "question": "What terms does Olivia offer for the lead investor's SAFE agreement?",
                "options": [
                    "A. A fifty percent equity stake with immediate voting control.",
                    "B. A four-million-dollar valuation cap with a twenty percent conversion discount.",
                    "C. Repayment of the loan with ten percent cash interest within sixty days.",
                    "D. Free shares in her next three startup ventures."
                ],
                "answerIndex": 1,
                "explanation": "Olivia đưa ra điều khoản: 'a standard post-money SAFE with a four-million-dollar valuation cap and a twenty percent conversion discount for our lead investor'."
            }
        ]
    },

    # ---------------- MODULE 12 (NEW) ----------------
    {
        "id": "read-12",
        "title": "The Ethics of Genetic Engineering & CRISPR Therapeutics",
        "type": "passage",
        "topic": "Y sinh & Đạo đức sinh học",
        "level": "B2 - C1",
        "summary": "Phân tích tiềm năng điều trị bệnh hiểm nghèo bằng công nghệ chỉnh sửa gen CRISPR và lằn ranh đạo đức trong can thiệp dòng mầm di truyền.",
        "content": "The advent of CRISPR-Cas9 genome editing represents a quantum leap in molecular biology, shifting medical science from symptom management to direct hereditary intervention. Originally deciphered as an adaptive immune mechanism in bacterial organisms against bacteriophage viruses, this enzymatic tool enables scientists to introduce double-stranded DNA breaks at precise nucleotide coordinates with unprecedented fidelity. Monogenic diseases that have tormented humanity for millennia—including sickle-cell anemia, cystic fibrosis, and Huntington's chorea—are transitioning from fatal prognoses into potentially curable conditions.\n\nClinical trials have already demonstrated spectacular somatic cell therapies. By harvesting hematopoietic stem cells from patients afflicted with sickle-cell disease, excising the defective hemoglobin gene ex vivo, and re-infusing the edited cells into bone marrow, clinicians have successfully restored normal red blood cell morphology without provoking immune rejection. Because somatic edits are confined strictly to differentiated bodily tissues, they vanish upon the patient's death and are never transmitted to subsequent generations.\n\nConversely, germline gene editing—the genetic modification of human embryos, sperm, or oocytes—propels humanity into precarious bioethical territory. In germline interventions, artificial alterations become permanent, heritable fixtures of the human gene pool. Proponents argue that germline editing offers the ultimate compassionate opportunity to eradicate devastating genetic pathologies from familial lineages forever. However, bioethicists warn against off-target mutagenesis, where the Cas9 enzyme inadvertently cleaves non-targeted genomic sequences, potentially introducing catastrophic oncogenic mutations that propagate down generations.\n\nBeyond biophysical safety, the prospect of germline enhancement invokes chilling sociological perils. If gene editing transitions from curative medicine to elective cosmetic and cognitive enhancement, wealthy elites could purchase biological advantages for their progeny. Such commercialization risks inaugurating a neo-eugenic caste system, cementing socio-economic inequality into immutable biological destiny. Therefore, the global scientific community firmly demands strict regulatory moratoria until safety thresholds and universal democratic consensus are unequivocally established.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Sự ra đời của công cụ chỉnh sửa bộ gen CRISPR-Cas9 đại diện cho một bước nhảy vọt lượng tử trong sinh học phân tử, chuyển khoa học y tế từ việc quản lý triệu chứng sang can thiệp di truyền trực tiếp. Ban đầu được giải mã như một cơ chế miễn dịch thích ứng ở vi khuẩn chống lại virus thực khuẩn thể, công cụ enzyme này cho phép các nhà khoa học tạo ra các vết cắt DNA chuỗi kép tại các tọa độ nucleotide chính xác với độ trung thực chưa từng có. Các bệnh đơn gen từng hành hạ nhân loại hàng thiên niên kỷ—bao gồm thiếu máu hồng cầu hình liềm, xơ nang và bệnh múa giật Huntington—đang chuyển đổi từ tiên lượng tử vong sang các tình trạng có khả năng chữa khỏi.\n
Các thử nghiệm lâm sàng đã chứng minh các liệu pháp tế bào soma ngoạn mục. Bằng cách thu hoạch các tế bào gốc tạo máu từ những bệnh nhân mắc bệnh hồng cầu hình liềm, cắt bỏ gen hemoglobin bị lỗi ngoài cơ thể (ex vivo) và truyền lại các tế bào đã chỉnh sửa vào tủy xương, các bác sĩ lâm sàng đã khôi phục thành công hình thái hồng cầu bình thường mà không gây ra phản ứng đào thải miễn dịch. Bởi vì các chỉnh sửa soma chỉ giới hạn nghiêm ngặt ở các mô cơ thể biệt hóa, chúng sẽ biến mất khi bệnh nhân qua đời và không bao giờ được truyền sang các thế hệ sau.\n
Ngược lại, việc chỉnh sửa gen dòng mầm—sự biến đổi gen của phôi người, tinh trùng hoặc tế bào trứng—đưa nhân loại vào lãnh địa đạo đức sinh học bấp bênh. Trong các can thiệp dòng mầm, các thay đổi nhân tạo trở thành những đặc điểm di truyền vĩnh viễn trong vốn gen của con người. Những người ủng hộ lập luận rằng chỉnh sửa dòng mầm mang lại cơ hội nhân đạo tối thượng để xóa bỏ vĩnh viễn các bệnh lý di truyền tàn khốc khỏi các dòng họ. Tuy nhiên, các nhà đạo đức sinh học cảnh báo về sự đột biến lệch mục tiêu (off-target mutagenesis), nơi enzyme Cas9 vô tình cắt các chuỗi gen ngoài mục tiêu, có khả năng gây ra các đột biến gây ung thư thảm khốc truyền qua các thế hệ.\n
Vượt ra ngoài sự an toàn sinh lý học, viễn cảnh tăng cường gen dòng mầm gợi lên những mối nguy hiểm xã hội học đáng sợ. Nếu chỉnh sửa gen chuyển từ y học chữa bệnh sang nâng cấp thẩm mỹ và nhận thức tự chọn, giới tinh hoa giàu có có thể mua các lợi thế sinh học cho con cháu của họ. Việc thương mại hóa như vậy có nguy cơ mở ra một hệ thống đẳng cấp ưu sinh học mới, khắc sâu sự bất bình đẳng kinh tế xã hội thành số phận sinh học bất biến. Do đó, cộng đồng khoa học toàn cầu kiên quyết yêu cầu các lệnh tạm ngừng theo quy định nghiêm ngặt cho đến khi các ngưỡng an toàn và sự đồng thuận dân chủ phổ quát được thiết lập một cách rõ ràng.""",
        "keyVocab": [
            { "word": "quantum leap", "ipa": "/ˌkwɑːn.təm ˈliːp/", "meaning": "bước nhảy vọt vĩ đại" },
            { "word": "monogenic disease", "ipa": "/ˌmɑː.nəˈdʒen.ɪk dɪˈziːz/", "meaning": "bệnh do đột biến một gen đơn lẻ" },
            { "word": "somatic cell therapy", "ipa": "/soʊˈmæt̬.ɪk sel ˈθer.ə.pi/", "meaning": "liệu pháp tế bào soma (không di truyền sang đời sau)" },
            { "word": "germline editing", "ipa": "/ˈdʒɝːm.laɪn ˈed.ɪ.tɪŋ/", "meaning": "chỉnh sửa gen dòng mầm (di truyền sang các thế hệ sau)" },
            { "word": "off-target mutagenesis", "ipa": "/ɔːf ˈtɑːr.ɡɪt ˌmjuː.t̬əˈdʒen.ə.sɪs/", "meaning": "sự gây đột biến ngoài vị trí mục tiêu" }
        ],
        "questions": [
            {
                "id": "q-12-1",
                "question": "What is the biological origin of the CRISPR-Cas9 system?",
                "options": [
                    "A. A synthetic compound formulated in industrial chemical factories.",
                    "B. An adaptive bacterial immune defense mechanism against bacteriophage viruses.",
                    "C. A venom peptide extracted from poisonous marine mollusks.",
                    "D. A natural hormone produced by the human pituitary gland."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu rõ: 'Originally deciphered as an adaptive immune mechanism in bacterial organisms against bacteriophage viruses'."
            },
            {
                "id": "q-12-2",
                "question": "Why are somatic cell therapies considered less ethically contentious than germline modifications?",
                "options": [
                    "A. Somatic edits are completely free of financial cost for all hospitals.",
                    "B. Somatic edits do not require any laboratory equipment.",
                    "C. Somatic edits are confined to differentiated tissues and are not passed on to future generations.",
                    "D. Somatic edits can only be performed on laboratory mice."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 2 giải thích: 'Because somatic edits are confined strictly to differentiated bodily tissues, they vanish upon the patient's death and are never transmitted to subsequent generations'."
            },
            {
                "id": "q-12-3",
                "question": "What biophysical risk is associated with germline Cas9 cleavage?",
                "options": [
                    "A. Extreme tooth decay and vision loss.",
                    "B. Inadvertent off-target cleaving potentially introducing heritable oncogenic mutations.",
                    "C. The patient's blood permanently turning purple.",
                    "D. Immediate loss of the ability to digest carbohydrates."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 cảnh báo: 'bioethicists warn against off-target mutagenesis, where the Cas9 enzyme inadvertently cleaves non-targeted genomic sequences, potentially introducing catastrophic oncogenic mutations that propagate down generations'."
            },
            {
                "id": "q-12-4",
                "question": "What sociological danger does the author warn could occur if genetic enhancement is commercialized?",
                "options": [
                    "A. International sports competitions will be permanently canceled.",
                    "B. A neo-eugenic caste system where wealthy elites cement socio-economic privilege into biological destiny.",
                    "C. High school biology textbooks becoming too complicated to understand.",
                    "D. Governments making cosmetic surgery mandatory for all citizens."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 4 cảnh báo: 'Such commercialization risks inaugurating a neo-eugenic caste system, cementing socio-economic inequality into immutable biological destiny'."
            }
        ]
    },

    # ---------------- MODULE 13 (NEW) ----------------
    {
        "id": "read-13",
        "title": "Crisis Management: Data Breach & PR Response",
        "type": "conversation",
        "topic": "An ninh mạng & Xử lý khủng hoảng",
        "level": "B2 - C1",
        "summary": "Cuộc họp ứng phó khẩn cấp giữa Giám đốc An ninh Thông tin và Nữ Trưởng phòng Quan hệ Công chúng khi hệ thống dữ liệu khách hàng bị tấn công mạng.",
        "content": [
            { "speaker": "Alex (Male / Chief Information Security Officer)", "text": "Victoria, thank you for rushing down. At 03:00 UTC, our automated intrusion detection system caught unauthorized exfiltration traffic originating from our European customer database shard." },
            { "speaker": "Victoria (Female / Head of Public Relations)", "text": "Good heavens, Alex. How extensive is the blast radius? Were customer credentials or unencrypted financial records compromised?" },
            { "speaker": "Alex (Male / Chief Information Security Officer)", "text": "The threat actors exploited a zero-day vulnerability in a third-party caching plugin. Approximately two hundred thousand customer profile records were accessed, including salted hashed passwords and email addresses, but our payment tokens remain strictly encrypted." },
            { "speaker": "Victoria (Female / Head of Public Relations)", "text": "Under GDPR regulations, we face a statutory seventy-two-hour window to report this incident to data protection authorities. When will our containment protocol be complete?" },
            { "speaker": "Alex (Male / Chief Information Security Officer)", "text": "My incident response team has already isolated the compromised cluster, revoked all API tokens, and patched the caching vulnerability. Forensic log analysis is eighty percent complete." },
            { "speaker": "Victoria (Female / Head of Public Relations)", "text": "That enables us to maintain an offensive communication posture. If we proactively notify affected users before investigative journalists break the story, we preserve brand credibility." },
            { "speaker": "Alex (Male / Chief Information Security Officer)", "text": "I agree completely. We should also enforce a mandatory password reset for all impacted accounts upon their next login session." },
            { "speaker": "Victoria (Female / Head of Public Relations)", "text": "I will draft the transparent public advisory immediately, emphasizing our swift mitigation and offering complimentary credit monitoring services for affected users." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Alex (Nam / Giám đốc An ninh Thông tin):** Victoria, cảm ơn cô đã đến gấp. Vào lúc 03:00 UTC, hệ thống phát hiện xâm nhập tự động của chúng ta đã phát hiện lưu lượng trích xuất trái phép bắt nguồn từ phân vùng cơ sở dữ liệu khách hàng châu Âu.\n
- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Trời ơi, Alex. Bán kính ảnh hưởng rộng đến mức nào? Thông tin đăng nhập của khách hàng hoặc hồ sơ tài chính không được mã hóa có bị xâm phạm không?\n
- **Alex (Nam / Giám đốc An ninh Thông tin):** Các tác nhân đe dọa đã khai thác lỗ hổng zero-day trong một plugin bộ đệm của bên thứ ba. Khoảng 200.000 hồ sơ khách hàng đã bị truy cập, bao gồm mật khẩu đã băm và địa chỉ email, nhưng các mã thanh toán vẫn được mã hóa nghiêm ngặt.\n
- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Theo quy định GDPR, chúng ta có khung thời gian luật định 72 giờ để báo cáo sự cố này cho các cơ quan bảo vệ dữ liệu. Khi nào giao thức khoanh vùng của bên anh hoàn tất?\n
- **Alex (Nam / Giám đốc An ninh Thông tin):** Đội phản ứng sự cố của tôi đã cô lập cụm máy chủ bị xâm phạm, thu hồi tất cả mã khóa API và vá lỗ hổng bộ đệm. Phân tích nhật ký điều tra đã hoàn tất 80%.\n
- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Điều đó cho phép chúng ta duy trì thế chủ động trong truyền thông. Nếu chúng ta chủ động thông báo cho những người dùng bị ảnh hưởng trước khi các nhà báo điều tra đưa tin, chúng ta sẽ bảo vệ được uy tín thương hiệu.\n
- **Alex (Nam / Giám đốc An ninh Thông tin):** Tôi hoàn toàn đồng ý. Chúng ta cũng nên thực thi việc đặt lại mật khẩu bắt buộc cho tất cả các tài khoản bị ảnh hưởng trong phiên đăng nhập tiếp theo.\n
- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Tôi sẽ soạn thông báo công khai minh bạch ngay lập tức, nhấn mạnh khả năng giảm thiểu thiệt hại nhanh chóng của chúng ta và cung cấp dịch vụ giám sát tín dụng miễn phí cho người dùng bị ảnh hưởng.""",
        "keyVocab": [
            { "word": "intrusion detection system", "ipa": "/ɪnˈtruː.ʒən dɪˈtek.ʃən ˈsɪs.təm/", "meaning": "hệ thống phát hiện xâm nhập mạng (IDS)" },
            { "word": "blast radius", "ipa": "/blæst ˈreɪ.di.əs/", "meaning": "phạm vi/bán kính ảnh hưởng của sự cố" },
            { "word": "zero-day vulnerability", "ipa": "/ˌzɪr.oʊ deɪ ˌvʌl.nɚ.əˈbɪl.ə.t̬i/", "meaning": "lỗ hổng bảo mật chưa có bản vá" },
            { "word": "statutory window", "ipa": "/ˈstætʃ.ə.tɔːr.i ˈwɪn.doʊ/", "meaning": "thời hạn bắt buộc theo luật định" },
            { "word": "mitigation", "ipa": "/ˌmɪt̬.əˈɡeɪ.ʃən/", "meaning": "sự giảm thiểu tổn thất/tác hại" }
        ],
        "questions": [
            {
                "id": "q-13-1",
                "question": "How did cyber threat actors gain unauthorized access to the customer database?",
                "options": [
                    "A. By bribing an internal database administrator.",
                    "B. By exploiting a zero-day vulnerability in a third-party caching plugin.",
                    "C. By physically breaking into the company's European headquarters.",
                    "D. By guessing the administrative master password."
                ],
                "answerIndex": 1,
                "explanation": "Alex xác nhận: 'The threat actors exploited a zero-day vulnerability in a third-party caching plugin'."
            },
            {
                "id": "q-13-2",
                "question": "Were customers' credit card and payment tokens compromised in the breach?",
                "options": [
                    "A. Yes, all banking details were leaked to public forums.",
                    "B. Only the credit cards of premium subscribers were leaked.",
                    "C. No, payment tokens remained strictly encrypted.",
                    "D. The company never stores payment tokens digitally."
                ],
                "answerIndex": 2,
                "explanation": "Alex giải thích: 'Approximately two hundred thousand customer profile records were accessed... but our payment tokens remain strictly encrypted'."
            },
            {
                "id": "q-13-3",
                "question": "What statutory deadline does Victoria mention under GDPR compliance rules?",
                "options": [
                    "A. Twenty-four hours to delete all customer records.",
                    "B. Seventy-two hours to report the incident to data protection authorities.",
                    "C. Thirty days to pay financial compensation.",
                    "D. One year to upgrade company server hardware."
                ],
                "answerIndex": 1,
                "explanation": "Victoria nhấn mạnh: 'Under GDPR regulations, we face a statutory seventy-two-hour window to report this incident to data protection authorities'."
            },
            {
                "id": "q-13-4",
                "question": "What proactive PR strategy does Victoria advocate to protect brand reputation?",
                "options": [
                    "A. Denying all rumors and threatening to sue investigative journalists.",
                    "B. Shutting down the entire corporate website indefinitely.",
                    "C. Proactively notifying users transparently and offering complimentary credit monitoring services.",
                    "D. Blaming the European Union for weak cyber regulations."
                ],
                "answerIndex": 2,
                "explanation": "Victoria đề xuất: 'I will draft the transparent public advisory immediately, emphasizing our swift mitigation and offering complimentary credit monitoring services for affected users'."
            }
        ]
    },

    # ---------------- MODULE 14 (NEW) ----------------
    {
        "id": "read-14",
        "title": "The Economics of Renewable Transition and Grid Modernization",
        "type": "passage",
        "topic": "Năng lượng & Biến đổi khí hậu",
        "level": "B2 - C1",
        "summary": "Đoạn văn khảo sát tính kinh tế của việc dịch chuyển sang năng lượng tái tạo, rào cản lưu trữ pin và nhu cầu hiện đại hóa hạ tầng lưới điện.",
        "content": "The global energy sector is traversing an unprecedented structural transition as the levelized cost of energy (LCOE) for solar photovoltaics and onshore wind continues its precipitous descent. Across multiple geopolitical territories, renewable generation has achieved unsubsidized grid parity, outcompeting traditional thermal coal and combined-cycle gas plants on marginal generation costs alone. Yet, celebratory declarations of a friction-free clean energy revolution overlook an obstinate physical impediment: the fundamental inadequacy of legacy transmission grids.\n\nTwentieth-century electrical grids were engineered around centralized, dispatchable generation. Fossil-fuel and nuclear facilities generated steady baseload power that flowed unidirectionally through high-voltage corridors to regional demand centers. In contrast, wind and solar assets are intrinsically intermittent and geographically dispersed, frequently situated in remote plains or offshore shoals far removed from metropolitan consumption hubs. When weather conditions precipitate sudden surges in generation, antiquated regional transmission lines become congested, compelling grid operators to mandate costly \"curtailment\"—the deliberate discarding of zero-carbon clean electricity.\n\nResolving this structural mismatch requires enormous capital deployment toward two complementary domains: utility-scale energy storage and high-voltage direct current (HVDC) transmission superhighways. While lithium-iron-phosphate battery packs excel at short-duration frequency regulation and four-hour evening peak shaving, they remain economically unviable for multi-day seasonal lulls. Long-duration energy storage alternatives—such as vanadium redox flow batteries, pumped-storage hydroelectric facilities, and green hydrogen electrolysis—are essential to ensure winter baseload reliability.\n\nSimultaneously, deploying continental HVDC corridors enables grid operators to balance weather variability across thousands of kilometers. When overcast skies suppress solar harvesting in Western Europe, surplus wind energy from North Sea offshore turbines can be channeled instantaneously across borders to sustain industrial operations. Ultimately, decarbonization is not merely a contest of building solar arrays; it is an epochal civil engineering campaign to rebuild the continental nervous system of electric power.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Ngành năng lượng toàn cầu đang trải qua một quá trình chuyển đổi cơ cấu chưa từng có khi chi phí quy dẫn của năng lượng (LCOE) cho điện mặt trời và điện gió trên bờ tiếp tục giảm mạnh. Trên nhiều vùng lãnh thổ địa chính trị, sản lượng điện tái tạo đã đạt mức ngang bằng lưới điện mà không cần trợ cấp, vượt trội so với các nhà máy nhiệt điện than truyền thống và tuabin khí chu trình hỗn hợp chỉ tính riêng về chi phí phát điện biên. Tuy nhiên, những tuyên bố ăn mừng về một cuộc cách mạng năng lượng sạch không ma sát đã bỏ qua một trở ngại vật lý ngoan cố: sự không thỏa đáng cơ bản của các lưới điện truyền tải cũ kỹ.\n
Lưới điện của thế kỷ 20 được thiết kế dựa trên các nguồn phát điện tập trung, có thể điều độ được. Các cơ sở nhiên liệu hóa thạch và hạt nhân tạo ra nguồn điện phụ tải đáy ổn định, chảy một chiều qua các hành lang điện áp cao đến các trung tâm phụ tải khu vực. Ngược lại, các tài sản gió và mặt trời vốn có tính chất gián đoạn và phân tán về mặt địa lý, thường nằm ở các vùng đồng bằng xa xôi hoặc bãi cạn ngoài khơi cách xa các trung tâm tiêu thụ đô thị. Khi điều kiện thời tiết tạo ra sự gia tăng đột biến về sản lượng điện, các đường dây truyền tải cũ trong khu vực bị tắc nghẽn, buộc các nhà vận hành lưới điện phải áp dụng biện pháp \"cắt giảm phát điện\" (curtailment) tốn kém—việc cố tình vứt bỏ lượng điện sạch không phát thải carbon.\n
Việc giải quyết sự mất cân đối về cấu trúc này đòi hỏi phải triển khai vốn khổng lồ vào hai lĩnh vực bổ sung: lưu trữ năng lượng quy mô lưới điện và các siêu xa lộ truyền tải điện một chiều siêu cao áp (HVDC). Mặc dù các bộ pin lithium-iron-phosphate vượt trội trong việc điều chỉnh tần số thời lượng ngắn và cắt giảm phụ tải đỉnh buổi tối trong 4 giờ, nhưng chúng vẫn không khả thi về mặt kinh tế đối với sự sụt giảm phát điện theo mùa kéo dài nhiều ngày. Các giải pháp thay thế lưu trữ năng lượng thời lượng dài—chẳng hạn như pin dòng oxy hóa khử vanadium, các cơ sở thủy điện tích năng và điện phân hydro xanh—là cần thiết để đảm bảo độ tin cậy của phụ tải đáy mùa đông.\n
Đồng thời, việc triển khai các hành lang HVDC xuyên lục địa cho phép các nhà điều hành lưới điện cân bằng sự biến động của thời tiết qua hàng nghìn km. Khi trời nhiều mây làm giảm khả năng thu năng lượng mặt trời ở Tây Âu, lượng điện gió dư thừa từ các tuabin ngoài khơi Biển Bắc có thể được dẫn ngay lập tức qua biên giới để duy trì các hoạt động công nghiệp. Cuối cùng, khử cacbon không chỉ đơn thuần là cuộc đua lắp đặt các tấm pin mặt trời; đó là một chiến dịch kỹ thuật dân dụng mang tính thời đại nhằm xây dựng lại hệ thống thần kinh lục địa của năng lượng điện.""",
        "keyVocab": [
            { "word": "levelized cost of energy", "ipa": "/ˈlev.əl.aɪzd kɑːst əv ˈen.ɚ.dʒi/", "meaning": "chi phí quy dẫn của năng lượng (LCOE)" },
            { "word": "grid parity", "ipa": "/ɡrɪd ˈper.ə.t̬i/", "meaning": "điểm cân bằng chi phí lưới điện không cần trợ cấp" },
            { "word": "curtailment", "ipa": "/kɚˈteɪl.mənt/", "meaning": "sự cắt giảm phát điện bắt buộc do quá tải lưới" },
            { "word": "peak shaving", "ipa": "/piːk ˈʃeɪ.vɪŋ/", "meaning": "cắt giảm phụ tải đỉnh giờ cao điểm" },
            { "word": "high-voltage direct current", "ipa": "/haɪ ˈvoʊl.tɪdʒ daɪˈrekt ˈkɝː.ənt/", "meaning": "truyền tải điện một chiều cao áp (HVDC)" }
        ],
        "questions": [
            {
                "id": "q-14-1",
                "question": "What milestone has renewable power achieved across multiple territories?",
                "options": [
                    "A. Banning all fossil fuels by international decree.",
                    "B. Achieving unsubsidized grid parity, outcompeting traditional thermal generation on marginal cost.",
                    "C. Producing hundred percent of global industrial electricity.",
                    "D. Generating power without needing sunlight or wind."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 1 nêu: 'renewable generation has achieved unsubsidized grid parity, outcompeting traditional thermal coal and combined-cycle gas plants on marginal generation costs alone'."
            },
            {
                "id": "q-14-2",
                "question": "Why does grid congestion frequently cause 'curtailment' of clean electricity?",
                "options": [
                    "A. Solar panels break down whenever temperatures exceed twenty degrees.",
                    "B. Remote solar and wind farms produce surges that overwhelm antiquated unidirectional regional transmission lines.",
                    "C. Power plant operators prefer burning coal out of tradition.",
                    "D. Batteries absorb all electricity and refuse to release it."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 giải thích: 'When weather conditions precipitate sudden surges in generation, antiquated regional transmission lines become congested, compelling grid operators to mandate costly \"curtailment\"'."
            },
            {
                "id": "q-14-3",
                "question": "What limitation do lithium-iron-phosphate battery systems have for seasonal energy storage?",
                "options": [
                    "A. They explode when exposed to winter air temperatures.",
                    "B. They cannot store electricity for more than ten seconds.",
                    "C. They are economically unviable for multi-day seasonal generation lulls.",
                    "D. They require radioactive fuel rods to function."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 3 chỉ ra: 'they remain economically unviable for multi-day seasonal lulls. Long-duration energy storage alternatives... are essential to ensure winter baseload reliability'."
            },
            {
                "id": "q-14-4",
                "question": "How do continental HVDC corridors assist during regional weather fluctuations?",
                "options": [
                    "A. By channeling surplus offshore wind power across borders to areas where solar power is diminished.",
                    "B. By heating clouds to prevent winter snowfall.",
                    "C. By eliminating the necessity of power lines altogether.",
                    "D. By storing electricity inside underground natural gas caverns."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 4 minh họa: 'When overcast skies suppress solar harvesting in Western Europe, surplus wind energy from North Sea offshore turbines can be channeled instantaneously across borders'."
            }
        ]
    },

    # ---------------- MODULE 15 (NEW) ----------------
    {
        "id": "read-15",
        "title": "Architectural Critique & Sustainable Building Design",
        "type": "conversation",
        "topic": "Kiến trúc & Bất động sản",
        "level": "B2 - C1",
        "summary": "Cuộc trao đổi chuyên môn giữa Kỹ sư Kết cấu Trưởng và Nữ Kiến trúc sư Trưởng về việc tối ưu hóa hiệu quả nhiệt và thông gió tự nhiên cho tòa tháp phức hợp.",
        "content": [
            { "speaker": "Ethan (Male / Chief Structural Engineer)", "text": "Sophia, I scrutinized your updated schematics for the Meridian Tower atrium. While the ninety-meter glass curtain wall creates breathtaking aesthetics, its thermal envelope will impose an immense load on our HVAC chillers during July." },
            { "speaker": "Sophia (Female / Lead Architect)", "text": "I anticipated that concern, Ethan. If you examine section D, we are not installing monolithic glazing. We specified electrochromic triple-pane glass integrated with motorized exterior ceramic louvers calibrated to solar azimuth angles." },
            { "speaker": "Ethan (Male / Chief Structural Engineer)", "text": "That definitely mitigates solar heat gain coefficients. What about structural deflection under wind turbulence? The cantilevered sky-bridge connecting the twin towers generates significant torsional stress." },
            { "speaker": "Sophia (Female / Lead Architect)", "text": "We worked with aerodynamic consultants to incorporate a tuned mass damper at level forty-two, alongside porous kinetic wind dampers that deflect cross-winds without stiffening the primary trusses excessively." },
            { "speaker": "Ethan (Male / Chief Structural Engineer)", "text": "That is an elegant structural compromise. Have you accounted for embodied carbon restrictions mandated by municipal zero-emission building codes?" },
            { "speaker": "Sophia (Female / Lead Architect)", "text": "Yes. We replaced forty percent of Portland cement in our foundation mix with pozzolanic volcanic ash and recycled blast furnace slag, which reduces our concrete embodied carbon by thirty-two percent." },
            { "speaker": "Ethan (Male / Chief Structural Engineer)", "text": "Remarkable. That keeps us well beneath municipal carbon thresholds while maintaining sixty-megapascal compressive strength." },
            { "speaker": "Sophia (Female / Lead Architect)", "text": "Let us finalize the load calculation dossier so we can submit the blueprint to the municipal building safety board before Friday's deadline." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Sophia, tôi đã xem xét kỹ các bản vẽ sơ đồ cập nhật của cô cho giếng trời Tòa tháp Meridian. Mặc dù bức tường kính cao 90 mét tạo ra tính thẩm mỹ ngoạn mục, nhưng lớp vỏ bọc nhiệt của nó sẽ gây tải trọng khổng lồ cho các máy làm lạnh HVAC của chúng ta vào tháng Bảy.\n
- **Sophia (Nữ / Kiến trúc sư Trưởng):** Tôi đã lường trước mối lo ngại đó, Ethan. Nếu anh kiểm tra phần D, chúng tôi không lắp đặt kính nguyên khối thông thường. Chúng tôi đã chỉ định kính ba lớp điện sắc kết hợp với các thanh chắn gốm cơ giới bên ngoài được hiệu chuẩn theo góc phương vị mặt trời.\n
- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Điều đó chắc chắn làm giảm hệ số hấp thụ nhiệt mặt trời. Còn độ võng kết cấu dưới tác động của nhiễu động gió thì sao? Cầu kính công-xôn nối hai tòa tháp tạo ra ứng suất xoắn đáng kể.\n
- **Sophia (Nữ / Kiến trúc sư Trưởng):** Chúng tôi đã làm việc với các chuyên gia khí động học để kết hợp một thiết bị giảm chấn khối lượng điều chỉnh (tuned mass damper) ở tầng 42, cùng với các van điều tiết gió động học xốp giúp làm lệch hướng gió ngược mà không làm cứng các giàn chịu lực chính quá mức.\n
- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Đó là một sự thỏa hiệp kết cấu thanh lịch. Cô đã tính đến các hạn chế về carbon tiềm ẩn theo quy định của các bộ luật xây dựng không phát thải của thành phố chưa?\n
- **Sophia (Nữ / Kiến trúc sư Trưởng):** Rồi. Chúng tôi đã thay thế 40% xi măng Portland trong hỗn hợp móng bằng tro núi lửa pozzolanic và xỉ lò cao tái chế, giúp giảm 32% lượng carbon tiềm ẩn trong bê tông của chúng ta.\n
- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Thật đáng nể. Điều đó giúp chúng ta duy trì mức phát thải thấp hơn nhiều so với ngưỡng carbon của thành phố trong khi vẫn duy trì cường độ nén 60 megapascal.\n
- **Sophia (Nữ / Kiến trúc sư Trưởng):** Chúng ta hãy hoàn thiện hồ sơ tính toán tải trọng để có thể nộp bản thiết kế lên hội đồng an toàn xây dựng thành phố trước hạn chót thứ Sáu.""",
        "keyVocab": [
            { "word": "thermal envelope", "ipa": "/ˈθɝː.məl ˈen.və.loʊp/", "meaning": "lớp vỏ bọc cách nhiệt công trình" },
            { "word": "electrochromic glass", "ipa": "/iˌlek.troʊˈkroʊ.mɪk ɡlæs/", "meaning": "kính điện sắc thông minh (đổi màu theo nhiệt độ)" },
            { "word": "torsional stress", "ipa": "/ˈtɔːr.ʃən.əl stres/", "meaning": "ứng suất xoắn trong kết cấu chịu lực" },
            { "word": "tuned mass damper", "ipa": "/tjuːnd mæs ˈdæm.pɚ/", "meaning": "quả cầu giảm chấn điều hòa dao động cho tòa nhà cao tầng" },
            { "word": "embodied carbon", "ipa": "/ɪmˈbɑː.did ˈkɑːr.bən/", "meaning": "lượng carbon tiềm ẩn trong sản xuất vật liệu xây dựng" }
        ],
        "questions": [
            {
                "id": "q-15-1",
                "question": "What initial thermal performance concern does Ethan raise regarding the atrium?",
                "options": [
                    "A. The atrium would cause water condensation leaks during rain.",
                    "B. The 90-meter glass curtain wall would place an immense cooling load on HVAC chillers.",
                    "C. The glass would shatter under winter freezing temperatures.",
                    "D. Construction workers refuse to install windows above floor ten."
                ],
                "answerIndex": 1,
                "explanation": "Ethan nêu rõ: 'While the ninety-meter glass curtain wall creates breathtaking aesthetics, its thermal envelope will impose an immense load on our HVAC chillers during July'."
            },
            {
                "id": "q-15-2",
                "question": "How does Sophia mitigate solar heat gain across the glass facade?",
                "options": [
                    "A. Painting the glass with black opaque enamel paint.",
                    "B. Using electrochromic triple-pane glass and exterior ceramic louvers calibrated to solar angles.",
                    "C. Installing dark blackout curtains inside all private offices.",
                    "D. Removing all windows and replacing them with solid steel sheets."
                ],
                "answerIndex": 1,
                "explanation": "Sophia giải thích: 'We specified electrochromic triple-pane glass integrated with motorized exterior ceramic louvers calibrated to solar azimuth angles'."
            },
            {
                "id": "q-15-3",
                "question": "What device is installed at level forty-two to address wind turbulence on the sky-bridge?",
                "options": [
                    "A. A massive emergency parachute.",
                    "B. A tuned mass damper and porous kinetic wind dampers.",
                    "C. A collection of giant industrial electric fans.",
                    "D. A steel cable tethered to neighboring skyscrapers."
                ],
                "answerIndex": 1,
                "explanation": "Sophia cho biết: 'incorporate a tuned mass damper at level forty-two, alongside porous kinetic wind dampers that deflect cross-winds'."
            },
            {
                "id": "q-15-4",
                "question": "How did the design team reduce the concrete foundation's embodied carbon by 32%?",
                "options": [
                    "A. By importing sand from tropical desert beaches.",
                    "B. By replacing 40% of Portland cement with volcanic ash and recycled blast furnace slag.",
                    "C. By using hollow plastic tubes inside the foundation piles.",
                    "D. By delaying concrete pouring until winter months."
                ],
                "answerIndex": 1,
                "explanation": "Sophia nêu rõ: 'We replaced forty percent of Portland cement in our foundation mix with pozzolanic volcanic ash and recycled blast furnace slag, which reduces our concrete embodied carbon by thirty-two percent'."
            }
        ]
    },

    # ---------------- MODULE 16 (NEW) ----------------
    {
        "id": "read-16",
        "title": "Cognitive Biases in Executive Decision-Making",
        "type": "passage",
        "topic": "Tâm lý học quản trị",
        "level": "B2 - C1",
        "summary": "Khảo cứu tâm lý học hành vi về các bẫy thiên kiến nhận thức trong phòng họp điều hành doanh nghiệp và các giao thức hiệu chỉnh quyết định.",
        "content": "In corporate boardrooms and executive suites, strategic deliberations are frequently celebrated as paragons of rational analysis, underpinned by sophisticated econometric projections, discounted cash-flow models, and rigorous statistical regression. Yet, decades of empirical behavioral economics demonstrate that corporate leaders are routinely sabotaged by the very cognitive heuristics that enabled ancestral human survival. Under conditions of acute uncertainty and high stakes, intuitive cognitive shortcuts metastasize into insidious decision-making blind spots.\n\nAmong the most destructive of these psychological distortions is the sunk cost fallacy. When an enterprise sinks hundreds of millions of dollars into an underperforming software platform or failing foreign subsidiary, executive leadership frequently displays irrational escalation of commitment. Rather than acknowledging that historical expenditures are irrecoverable and evaluating the asset strictly through prospective future returns, executives channel additional capital into doomed ventures to safeguard personal prestige and evade the public humiliation of admitting strategic error.\n\nCompounding this vulnerability is confirmation bias, vigorously reinforced by boardroom groupthink. When a charismatic Chief Executive champions an aggressive corporate acquisition, sycophantic advisory teams subconsciously filter intelligence, accentuating market synergies while downplaying integration friction and regulatory antitrust hazards. Dissenting voices are subtly marginalized or self-silenced to preserve superficial consensus. The resulting epistemic echo chamber fosters an illusion of invulnerability, culminating in disastrous mergers that destroy shareholder valuation.\n\nTo inoculate organizations against these systemic biases, forward-thinking enterprises institute formal adversarial protocols. One highly effective technique is the Gary Klein \"pre-mortem\" analysis. Prior to finalizing a monumental acquisition or capital deployment, the executive committee convenes under the explicit hypothetical premise: \"Imagine we are five years in the future, and this initiative has suffered catastrophic failure. Write a comprehensive post-mortem explaining why.\" By legitimizing pessimism and dismantling the social stigma associated with dissent, pre-mortems unmask latent vulnerabilities before capital is irretrievably squandered.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Trong các phòng họp hội đồng quản trị và các dãy phòng điều hành doanh nghiệp, các cuộc cân nhắc chiến lược thường được tôn vinh là hình mẫu của sự phân tích hợp lý, được củng cố bởi các dự báo kinh tế lượng tinh vi, mô hình chiết khấu dòng tiền và hồi quy thống kê nghiêm ngặt. Tuy nhiên, hàng thập kỷ kinh tế học hành vi thực nghiệm chứng minh rằng các nhà lãnh đạo doanh nghiệp thường xuyên bị phá hoại bởi chính những lối tắt nhận thức (heuristics) từng giúp tổ tiên loài người sinh tồn. Dưới các điều kiện bất định gay gắt và rủi ro cao, các lối tắt trực giác biến chứng thành những điểm mù ra quyết định nguy hiểm.\n
Trong số những biến dạng tâm lý mang tính hủy diệt nhất là ngụy biện chi phí chìm (sunk cost fallacy). Khi một doanh nghiệp đã rót hàng trăm triệu đô la vào một nền tảng phần mềm hoạt động kém hiệu quả hoặc một công ty con nước ngoài đang thua lỗ, ban lãnh đạo thường thể hiện sự leo thang cam kết phi lý. Thay vì thừa nhận rằng các khoản chi tiêu trong quá khứ là không thể thu hồi và đánh giá tài sản nghiêm ngặt thông qua lợi nhuận tương lai kỳ vọng, các giám đốc điều hành tiếp tục đổ thêm vốn vào các dự án chắc chắn thất bại để bảo vệ uy tín cá nhân và tránh sự sỉ nhục công khai khi phải thừa nhận sai lầm chiến lược.\n
Làm trầm trọng thêm lỗ hổng này là thiên kiến xác nhận (confirmation bias), được củng cố mạnh mẽ bởi hội chứng tư duy tập thể a dua (groupthink). Khi một Giám đốc điều hành có sức lôi cuốn ủng hộ một thương vụ mua lại công ty quyết liệt, các nhóm cố vấn xu nịnh sẽ vô thức sàng lọc thông tin, nhấn mạnh sự hiệp lực thị trường trong khi giảm nhẹ ma sát tích hợp và các mối nguy hiểm chống độc quyền từ cơ quan quản lý. Những tiếng nói bất đồng tinh tế bị gạt ra ngoài lề hoặc tự im lặng để giữ gìn sự đồng thuận hời hợt. Kết quả là một buồng vang nhận thức tạo ra ảo tưởng về sự bất khả chiến bại, dẫn đến những vụ sáp nhập thảm khốc phá hủy giá trị cổ đông.\n
Để tiêm chủng cho các tổ chức chống lại những thiên kiến mang tính hệ thống này, các doanh nghiệp có tư duy tiến bộ thiết lập các quy trình phản biện chính thức. Một kỹ thuật rất hiệu quả là phân tích \"mổ xẻ trước thực thi\" (pre-mortem) của Gary Klein. Trước khi hoàn tất một thương vụ mua lại hoặc triển khai vốn lớn, ủy ban điều hành họp lại dưới một giả định rõ ràng: \"Hãy tưởng tượng chúng ta đang ở 5 năm sau trong tương lai, và sáng kiến này đã thất bại thảm hại. Hãy viết một báo cáo khám nghiệm toàn diện giải thích lý do tại sao.\" Bằng cách hợp pháp hóa sự bi quan và dỡ bỏ sự kỳ thị xã hội gắn liền với sự bất đồng, các cuộc họp pre-mortem vạch trần các lỗ hổng tiềm ẩn trước khi vốn liếng bị lãng phí không thể cứu vãn.""",
        "keyVocab": [
            { "word": "econometric projection", "ipa": "/iˌkɑː.nəˈmet.rɪk prəˈdʒek.ʃən/", "meaning": "dự báo kinh tế lượng" },
            { "word": "sunk cost fallacy", "ipa": "/sʌŋk kɑːst ˈfæl.ə.si/", "meaning": "ngụy biện chi phí chìm" },
            { "word": "escalation of commitment", "ipa": "/ˌes.kəˈleɪ.ʃən əv kəˈmɪt.mənt/", "meaning": "sự leo thang cam kết mù quáng" },
            { "word": "confirmation bias", "ipa": "/ˌkɑːn.fɚˈmeɪ.ʃən ˈbaɪ.əs/", "meaning": "thiên kiến xác nhận (chỉ nghe điều mình muốn)" },
            { "word": "pre-mortem analysis", "ipa": "/priː ˈmɔːr.təm əˈnæl.ə.sɪs/", "meaning": "phân tích dự báo nguyên nhân thất bại trước khi bắt đầu" }
        ],
        "questions": [
            {
                "id": "q-16-1",
                "question": "What psychological trap causes executives to pour capital into failing historical investments?",
                "options": [
                    "A. The sunk cost fallacy and irrational escalation of commitment.",
                    "B. The fear of international currency hyperinflation.",
                    "C. Mandatory legal instructions from state central banks.",
                    "D. Technological amnesia caused by lack of sleep."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 2 nêu rõ: 'the sunk cost fallacy... executive leadership frequently displays irrational escalation of commitment... channel additional capital into doomed ventures to safeguard personal prestige'."
            },
            {
                "id": "q-16-2",
                "question": "How does boardroom groupthink distort information regarding proposed company acquisitions?",
                "options": [
                    "A. Advisory teams amplify market synergies while muting integration and regulatory hazards.",
                    "B. Board members vote exclusively using anonymous coin tosses.",
                    "C. Outside consulting firms refuse to read corporate financial balance sheets.",
                    "D. Company attorneys leak confidential trade secrets to public news media."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 3 giải thích: 'sycophantic advisory teams subconsciously filter intelligence, accentuating market synergies while downplaying integration friction and regulatory antitrust hazards'."
            },
            {
                "id": "q-16-3",
                "question": "What is the core premise of a 'pre-mortem' analysis according to Gary Klein?",
                "options": [
                    "A. Firing the lowest-performing ten percent of workers every six months.",
                    "B. Imagining the project has catastrophically failed in the future and writing reasons why.",
                    "C. Celebrating executive bonuses before any work has commenced.",
                    "D. Requiring all employees to pass a psychological examination."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 4 mô tả kỹ thuật: 'The executive committee convenes under the explicit hypothetical premise: \"Imagine we are five years in the future, and this initiative has suffered catastrophic failure. Write a comprehensive post-mortem explaining why\".'"
            },
            {
                "id": "q-16-4",
                "question": "Why is the pre-mortem protocol structurally effective inside corporate leadership teams?",
                "options": [
                    "A. It reduces corporate income tax liability automatically.",
                    "B. It guarantees that company stock valuation doubles immediately.",
                    "C. It legitimizes constructive pessimism and removes the social stigma of dissenting views.",
                    "D. It replaces all human directors with automated econometric software."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 4 kết luận: 'By legitimizing pessimism and dismantling the social stigma associated with dissent, pre-mortems unmask latent vulnerabilities before capital is irretrievably squandered'."
            }
        ]
    },

    # ---------------- MODULE 17 (NEW) ----------------
    {
        "id": "read-17",
        "title": "Handling Customer Dispute & Warranty Litigation",
        "type": "conversation",
        "topic": "Chăm sóc khách hàng & Pháp lý",
        "level": "B1 - B2",
        "summary": "Cuộc thảo luận phương án hòa giải giữa Quản lý Trải nghiệm Khách hàng và Nữ Luật sư Doanh nghiệp đối với khiếu nại bảo hành của khách hàng VIP.",
        "content": [
            { "speaker": "Daniel (Male / Customer Experience Manager)", "text": "Emma, thanks for consulting on this matter. One of our enterprise accounts, Apex Logistics, sent a formal intent-to-sue notice regarding fifty fleet telematics modules that suffered battery drainage issues." },
            { "speaker": "Emma (Female / Corporate Legal Counsel)", "text": "I reviewed the master purchase agreement, Daniel. Did the hardware failure occur within the twelve-month limited warranty period, or has coverage lapsed?" },
            { "speaker": "Daniel (Male / Customer Experience Manager)", "text": "The units were installed thirteen months ago—technically four weeks beyond the warranty cutoff. However, the client argues that a firmware update we deployed caused the premature battery degradation." },
            { "speaker": "Emma (Female / Corporate Legal Counsel)", "text": "From a strict contractual standpoint, section 8.2 disclaims implied fitness for a particular purpose after twelve months. But if their engineering team proves our firmware update altered voltage thresholds, a latent defect claim could gain traction in commercial arbitration." },
            { "speaker": "Daniel (Male / Customer Experience Manager)", "text": "Litigation costs would dwarf the replacement expense. Replacing all fifty modules costs us roughly twelve thousand dollars, while Apex represents over eighty thousand dollars in recurring software subscriptions." },
            { "speaker": "Emma (Female / Corporate Legal Counsel)", "text": "Then commercial prudence dictates an amicable settlement. We should offer an out-of-warranty replacement as a goodwill gesture, contingent on Apex signing a mutual release of claims." },
            { "speaker": "Daniel (Male / Customer Experience Manager)", "text": "That protects our subscription revenue while extinguishing legal exposure. Can you draft the release of claims agreement by this afternoon?" },
            { "speaker": "Emma (Female / Corporate Legal Counsel)", "text": "Certainly. I will include a confidentiality covenant ensuring they cannot publicize this hardware replacement to other enterprise clients." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Emma, cảm ơn cô đã tư vấn về vấn đề này. Một trong những khách hàng doanh nghiệp của chúng ta, Apex Logistics, đã gửi thông báo chính thức về ý định khởi kiện liên quan đến 50 mô-đun viễn thông giám sát đội xe bị lỗi hao pin.\n
- **Emma (Nữ / Luật sư Doanh nghiệp):** Tôi đã xem lại hợp đồng mua bán khung, Daniel. Lỗi phần cứng xảy ra trong thời hạn bảo hành giới hạn 12 tháng hay thời hạn bảo hiểm đã hết hiệu lực?\n
- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Các thiết bị đã được lắp đặt cách đây 13 tháng—về mặt kỹ thuật là quá hạn bảo hành 4 tuần. Tuy nhiên, khách hàng lập luận rằng bản cập nhật chương trình cơ sở (firmware) mà chúng ta triển khai đã gây ra hiện tượng chai pin sớm.\n
- **Emma (Nữ / Luật sư Doanh nghiệp):** Từ góc độ hợp đồng nghiêm ngặt, mục 8.2 miễn trừ bảo đảm ngụ ý về sự phù hợp cho một mục đích cụ thể sau 12 tháng. Nhưng nếu đội ngũ kỹ thuật của họ chứng minh bản cập nhật firmware của chúng ta đã làm thay đổi ngưỡng điện áp, khiếu nại về khuyết tật ẩn tàng có thể giành được ưu thế tại trọng tài thương mại.\n
- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Chi phí kiện tụng sẽ vượt xa chi phí thay thế. Việc thay thế toàn bộ 50 mô-đun khiến chúng ta tốn khoảng 12.000 USD, trong khi Apex mang lại hơn 80.000 USD tiền thuê bao phần mềm định kỳ hàng năm.\n
- **Emma (Nữ / Luật sư Doanh nghiệp):** Vậy thì sự thận trọng trong kinh doanh đòi hỏi một giải pháp hòa giải thân thiện. Chúng ta nên đề xuất thay thế ngoài bảo hành như một cử chỉ thiện chí, với điều kiện Apex phải ký vào thỏa thuận miễn trừ khiếu nại lẫn nhau.\n
- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Cách đó vừa bảo vệ doanh thu thuê bao của chúng ta vừa dập tắt nguy cơ pháp lý. Cô có thể soạn thảo thỏa thuận từ bỏ khiếu nại vào chiều nay không?\n
- **Emma (Nữ / Luật sư Doanh nghiệp):** Chắc chắn rồi. Tôi sẽ đưa vào một điều khoản bảo mật đảm bảo họ không thể công khai việc thay thế phần cứng này cho các khách hàng doanh nghiệp khác.""",
        "keyVocab": [
            { "word": "intent-to-sue notice", "ipa": "/ɪnˈtent tuː suː ˈnoʊ.t̬ɪs/", "meaning": "thông báo chính thức về ý định khởi kiện" },
            { "word": "coverage lapsed", "ipa": "/ˈkʌv.ɚ.ɪdʒ læpst/", "meaning": "thời hạn bảo hành/bảo hiểm đã hết hiệu lực" },
            { "word": "latent defect", "ipa": "/ˈleɪ.tənt ˈdiː.fekt/", "meaning": "khuyết tật ẩn tàng của sản phẩm (khó thấy lúc mua)" },
            { "word": "goodwill gesture", "ipa": "/ɡʊdˈwɪl ˈdʒes.tʃɚ/", "meaning": "cử chỉ thiện chí thương mại" },
            { "word": "release of claims", "ipa": "/rɪˈliːs əv kleɪmz/", "meaning": "văn bản từ bỏ quyền khiếu nại/kiện tụng" }
        ],
        "questions": [
            {
                "id": "q-17-1",
                "question": "What technical complaint did Apex Logistics file against the company's hardware?",
                "options": [
                    "A. Telematics modules catching fire during highway transit.",
                    "B. Severe battery drainage issues allegedly caused by a firmware update.",
                    "C. Hardware screens displaying inaccurate international language translations.",
                    "D. Units failing to connect to Wi-Fi networks in private homes."
                ],
                "answerIndex": 1,
                "explanation": "Daniel nêu rõ: 'fifty fleet telematics modules that suffered battery drainage issues... the client argues that a firmware update we deployed caused the premature battery degradation'."
            },
            {
                "id": "q-17-2",
                "question": "Why is the warranty coverage technically questionable from a contractual viewpoint?",
                "options": [
                    "A. The units were stolen from another competitor's warehouse.",
                    "B. The units were installed thirteen months ago, four weeks past the twelve-month cutoff.",
                    "C. Apex Logistics never paid the initial invoice deposit.",
                    "D. Telematics devices are legally excluded from consumer warranties."
                ],
                "answerIndex": 1,
                "explanation": "Daniel giải thích: 'The units were installed thirteen months ago—technically four weeks beyond the warranty cutoff'."
            },
            {
                "id": "q-17-3",
                "question": "Why does Daniel strongly prefer replacing the hardware rather than going to court?",
                "options": [
                    "A. Replacement costs twelve thousand dollars, while Apex pays eighty thousand dollars in subscriptions.",
                    "B. The company does not employ any certified trial attorneys.",
                    "C. The local commercial court is permanently shut down.",
                    "D. Apex's CEO is Daniel's close personal relative."
                ],
                "answerIndex": 0,
                "explanation": "Daniel so sánh chi phí: 'Replacing all fifty modules costs us roughly twelve thousand dollars, while Apex represents over eighty thousand dollars in recurring software subscriptions'."
            },
            {
                "id": "q-17-4",
                "question": "What crucial protective clause will Emma include in the settlement agreement?",
                "options": [
                    "A. Apex must buy fifty additional vehicles immediately.",
                    "B. A mutual release of claims and a strict confidentiality covenant.",
                    "C. Daniel must apologize publicly on international television.",
                    "D. Apex must surrender all intellectual property rights to the company."
                ],
                "answerIndex": 1,
                "explanation": "Emma khẳng định: 'signing a mutual release of claims... I will include a confidentiality covenant ensuring they cannot publicize this hardware replacement to other enterprise clients'."
            }
        ]
    },

    # ---------------- MODULE 18 (NEW) ----------------
    {
        "id": "read-18",
        "title": "The Epistemology of Misinformation in the Algorithmic Age",
        "type": "passage",
        "topic": "Truyền thông & Xã hội số",
        "level": "B2 - C1",
        "summary": "Tiểu luận về cơ chế phát tán thông tin sai lệch trên mạng xã hội, các thuật toán tối ưu hóa tương tác gây kích động và kỹ thuật tiêm chủng nhận thức.",
        "content": "In the embryonic dawn of the World Wide Web, cyber-utopians proclaimed that frictionless digital connectivity would inaugurate a golden era of democratic enlightenment. The decentralized dissemination of knowledge, advocates argued, would dismantle authoritarian information monopolies, empower citizen journalism, and eradicate societal ignorance. Three decades later, this idealistic prophecy has curdled into a hyper-polarized infosphere plagued by algorithmic radicalization, synthetic media, and the systemic erosion of consensus reality.\n\nThe structural vector driving this epistemological crisis is the economic architecture of the attention economy. Commercial social media platforms do not optimize their recommendation algorithms for objective veracity or nuanced pedagogical value; they optimize strictly for user engagement—measured in watch duration, retweets, and emotive commenting. Behavioral psychologists have long established that human cognition is asymmetrically stimulated by moral outrage, existential dread, and in-group tribal validation. Consequently, algorithms systematically amplify sensationalist falsehoods, which diffuse across social networks up to six times faster than verified factual corrections.\n\nOver time, sustained exposure to algorithmic curation produces hermetically sealed epistemic bubbles. Within these algorithmic echo chambers, alternative perspectives are systematically filtered out, and counter-evidence is reflexively dismissed as malevolent propaganda manufactured by untrustworthy institutional elites. When synthetic deepfakes and automated generative disinformation bots are introduced into these fertile ideological soils, the boundary between empirical actuality and manufactured fiction dissolves completely, precipitating acute social fragmentation.\n\nConfronting this existential crisis requires moving beyond reactive, whack-a-mole content censorship toward \"cognitive inoculation.\" Pioneered by social psychologists, pre-bunking strategies expose internet users to weakened, micro-dosed examples of manipulation techniques—such as emotional scapegoating and fake expert endorsements—before they encounter viral misinformation in the wild. By cultivating digital media literacy and fostering structural algorithmic transparency, open societies can build societal resilience without sacrificing the inviolable principles of free expression.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Vào buổi bình minh sơ khai của mạng World Wide Web, những người theo chủ nghĩa không tưởng trên không gian mạng đã tuyên bố rằng sự kết nối kỹ thuật số không ma sát sẽ mở ra một kỷ nguyên vàng của sự khai sáng dân chủ. Những người ủng hộ lập luận rằng việc phổ biến kiến thức phi tập trung sẽ phá bỏ sự độc quyền thông tin độc tài, trao quyền cho báo chí công dân và xóa bỏ sự thiếu hiểu biết của xã hội. Ba thập kỷ sau, lời tiên tri duy tâm này đã biến chất thành một bầu không khí thông tin siêu phân cực bị hoành hành bởi sự cực đoan hóa theo thuật toán, truyền thông tổng hợp và sự xói mòn mang tính hệ thống của thực tế đồng thuận.\n
Véc-tơ cấu trúc thúc đẩy cuộc khủng hoảng nhận thức luận này là kiến trúc kinh tế của nền kinh tế chú ý. Các nền tảng truyền thông xã hội thương mại không tối ưu hóa các thuật toán đề xuất của họ cho tính xác thực khách quan hoặc giá trị sư phạm tinh tế; họ tối ưu hóa nghiêm ngặt cho sự tương tác của người dùng—được đo bằng thời lượng xem, lượt chia sẻ lại và bình luận đầy cảm xúc. Các nhà tâm lý học hành vi từ lâu đã xác định rằng nhận thức của con người bị kích thích bất đối xứng bởi sự phẫn nộ đạo đức, nỗi sợ hãi hiện sinh và sự chứng thực của bộ tộc nhóm nội bộ. Do đó, các thuật toán khuếch đại một cách có hệ thống những thông tin sai lệch giật gân, lan truyền trên các mạng xã hội nhanh hơn gấp 6 lần so với các đính chính thực tế đã được xác minh.\n
Theo thời gian, việc tiếp xúc liên tục với sự tuyển chọn của thuật toán sẽ tạo ra các bong bóng nhận thức khép kín. Trong các buồng vang thuật toán này, các góc nhìn thay thế bị lọc bỏ một cách có hệ thống, và các bằng chứng phản bác bị bác bỏ theo phản xạ như là tuyên truyền độc hại do các tầng lớp tinh hoa thể chế không đáng tin cậy tạo ra. Khi các video deepfake tổng hợp và các bot thông tin sai lệch tự động được đưa vào các mảnh đất ý thức hệ màu mỡ này, ranh giới giữa thực tế thực nghiệm và tiểu thuyết ngụy tạo sẽ tan biến hoàn toàn, gây ra sự phân mảnh xã hội gay gắt.\n
Đối mặt với cuộc khủng hoảng hiện sinh này đòi hỏi phải vượt ra ngoài việc kiểm duyệt nội dung mang tính phản ứng đối phó để hướng tới \"tiêm chủng nhận thức\". Được tiên phong bởi các nhà tâm lý học xã hội, các chiến lược \"bác bỏ trước\" (pre-bunking) cho người dùng internet tiếp xúc với các ví dụ liều nhỏ về các kỹ thuật thao túng—chẳng hạn như việc đổ lỗi cảm xúc và sự chứng thực của chuyên gia giả mạo—trước khi họ bắt gặp thông tin sai lệch trên mạng. Bằng cách trau dồi hiểu biết về truyền thông kỹ thuật số và thúc đẩy tính minh bạch của thuật toán cấu trúc, các xã hội cởi mở có thể xây dựng khả năng phục hồi của xã hội mà không phải hy sinh các nguyên tắc bất khả xâm phạm về tự do ngôn luận.""",
        "keyVocab": [
            { "word": "attention economy", "ipa": "/əˈten.ʃən iˈkɑː.nə.mi/", "meaning": "nền kinh tế chú ý (kinh doanh sự chú ý của người dùng)" },
            { "word": "epistemic bubble", "ipa": "/ˌep.əˈstiː.mɪk ˈbʌb.əl/", "meaning": "bong bóng nhận thức khép kín" },
            { "word": "echo chamber", "ipa": "/ˈek.oʊ ˌtʃeɪm.bɚ/", "meaning": "buồng vang thông tin (chỉ lặp lại quan điểm của mình)" },
            { "word": "cognitive inoculation", "ipa": "/ˈkɑːɡ.nə.t̬ɪv ɪˌnɑː.kjəˈleɪ.ʃən/", "meaning": "tiêm chủng nhận thức phòng ngừa tin giả" },
            { "word": "pre-bunking", "ipa": "/priː ˈbʌŋk.ɪŋ/", "meaning": "bác bỏ và giải thích thủ thuật lừa đảo trước khi bị tiếp cận" }
        ],
        "questions": [
            {
                "id": "q-18-1",
                "question": "What primary metric do commercial social media algorithms optimize for?",
                "options": [
                    "A. Verifiable factual truth and peer-reviewed educational value.",
                    "B. User engagement measured in viewing duration, retweets, and emotional comments.",
                    "C. Protecting users' mental calmness and promoting physical exercise.",
                    "D. Reducing server electricity consumption during evening hours."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 2 nêu rõ: 'commercial social media platforms do not optimize their recommendation algorithms for objective veracity... they optimize strictly for user engagement—measured in watch duration, retweets, and emotive commenting'."
            },
            {
                "id": "q-18-2",
                "question": "According to behavioral research, how much faster do sensationalist falsehoods spread compared to factual corrections?",
                "options": [
                    "A. Exactly at the same identical speed.",
                    "B. Twice as slow because fact-checkers intervene immediately.",
                    "C. Up to six times faster across social networks.",
                    "D. They only spread through printed newspapers."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 2 chỉ ra: 'algorithms systematically amplify sensationalist falsehoods, which diffuse across social networks up to six times faster than verified factual corrections'."
            },
            {
                "id": "q-18-3",
                "question": "What occurs inside 'algorithmic echo chambers' over prolonged periods?",
                "options": [
                    "A. Users become bilingual automatically without textbooks.",
                    "B. Diverse viewpoints are filtered out and counter-evidence is dismissed as malicious propaganda.",
                    "C. Social media accounts are deleted automatically after thirty days.",
                    "D. Governments subsidize high-speed internet connections for all citizens."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 giải thích: 'alternative perspectives are systematically filtered out, and counter-evidence is reflexively dismissed as malevolent propaganda manufactured by untrustworthy institutional elites'."
            },
            {
                "id": "q-18-4",
                "question": "What proactive psychological strategy is recommended under 'cognitive inoculation'?",
                "options": [
                    "A. Shutting down the entire internet permanently across all nations.",
                    "B. Banning all public speech on controversial scientific topics.",
                    "C. Exposing users to micro-dosed examples of manipulation tactics before encountering viral misinformation.",
                    "D. Forcing citizens to pay fines whenever sharing news articles online."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 4 kết luận: 'pre-bunking strategies expose internet users to weakened, micro-dosed examples of manipulation techniques... before they encounter viral misinformation in the wild'."
            }
        ]
    },

    # ---------------- MODULE 19 (NEW) ----------------
    {
        "id": "read-19",
        "title": "Academic Thesis Defense & Cross-Examination",
        "type": "conversation",
        "topic": "Giáo dục & Nghiên cứu học thuật",
        "level": "B2 - C1",
        "summary": "Phiên phản biện luận án tiến sĩ thiên văn học giữa Giáo sư Chủ tịch Hội đồng và Nữ Nghiên cứu sinh về dữ liệu quang phổ sao neutron.",
        "content": [
            { "speaker": "Professor Arthur (Male / Dissertation Committee Chair)", "text": "Dr. Maya, congratulations on a compelling dissertation presentation. However, committee member Dr. Vance raised a formidable methodological objection regarding your spectral analysis of neutron star binary mergers." },
            { "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)", "text": "Thank you, Professor Arthur. I welcome the committee's rigorous scrutiny. Is the objection directed at our gravitational wave signal filtering, or our electromagnetic counterpart calibrations?" },
            { "speaker": "Professor Arthur (Male / Dissertation Committee Chair)", "text": "Specifically, chapter four assumes that the observed high-energy gamma-ray burst exhibits isotropic emission. Given relativistic beaming physics, if the jet angle was tilted merely five degrees off our line of sight, your total calculated kilonova ejecta mass would be overstated by thirty percent." },
            { "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)", "text": "That is an astute critique. In appendix C, we anticipated that exact geometric degeneracy. To counteract line-of-sight ambiguity, we cross-validated the gamma-ray telemetry against late-time synchrotron radio afterglow data collected across sixteen months by the Very Large Array." },
            { "speaker": "Professor Arthur (Male / Dissertation Committee Chair)", "text": "Radio afterglow modeling requires robust assumptions regarding circumstellar medium density. How did you break the degeneracy between density and jet opening angle?" },
            { "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)", "text": "We utilized relativistic hydrodynamical simulations constrained by polarimetric optical observations. This narrowed our opening angle confidence interval to within three point two degrees, reaffirming that our ejecta mass bounds remain statistically robust at three sigma." },
            { "speaker": "Professor Arthur (Male / Dissertation Committee Chair)", "text": "That is an extraordinarily thorough defense. The incorporation of radio polarimetry addresses our primary theoretical skepticism." },
            { "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)", "text": "Thank you, Professor. I will incorporate this cross-validation synthesis prominently into the final dissertation revision before archiving." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Maya, chúc mừng cô vì một bài thuyết trình luận án rất thuyết phục. Tuy nhiên, thành viên hội đồng là Tiến sĩ Vance đã nêu ra một sự phản đối phương pháp luận đáng gờm liên quan đến phân tích quang phổ của cô về các vụ sáp nhập sao neutron đôi.\n
- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Cảm ơn Giáo sư Arthur. Tôi rất hoan nghênh sự xem xét kỹ lưỡng của hội đồng. Sự phản đối nhắm vào việc lọc tín hiệu sóng hấp dẫn hay hiệu chuẩn phần bức xạ điện từ tương ứng?\n
- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Cụ thể, chương 4 giả định rằng vụ nổ tia gamma năng lượng cao quan sát được thể hiện sự phát xạ đẳng hướng. Dựa trên vật lý chùm tia tương đối tính, nếu góc tia chỉ bị nghiêng 5 độ so với đường ngắm của chúng ta, tổng khối lượng vật chất phóng ra từ vụ nổ kilonova được tính toán của cô sẽ bị phóng đại quá mức 30%.\n
- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Đó là một lời phê bình sắc bén. Trong phụ lục C, chúng tôi đã dự đoán chính xác sự suy biến hình học đó. Để triệt tiêu sự mơ hồ về đường ngắm, chúng tôi đã kiểm định chéo dữ liệu đo từ xa của tia gamma với dữ liệu phát xạ vô tuyến synchrotron giai đoạn muộn được thu thập trong 16 tháng bởi mảng kính thiên văn Very Large Array.\n
- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Mô hình phát xạ vô tuyến sau vụ nổ đòi hỏi các giả định vững chắc về mật độ môi trường xung quanh sao. Cô đã phá vỡ sự suy biến giữa mật độ và góc mở của tia phóng như thế nào?\n
- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Chúng tôi đã sử dụng các mô phỏng thủy động lực học tương đối tính bị hạn chế bởi các quan sát phân cực quang học. Điều này thu hẹp khoảng tin cậy của góc mở xuống trong phạm vi 3,2 độ, tái khẳng định rằng ranh giới khối lượng vật chất phóng ra của chúng tôi vẫn vững chắc về mặt thống kê ở mức 3 sigma.\n
- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Đó là một sự bảo vệ luận án cực kỳ kỹ lưỡng. Việc kết hợp phép đo phân cực vô tuyến đã giải quyết được sự hoài nghi lý thuyết chính của chúng tôi.\n
- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Cảm ơn Giáo sư. Tôi sẽ đưa phần tổng hợp kiểm định chéo này vào vị trí nổi bật trong bản sửa đổi luận án cuối cùng trước khi lưu trữ.""",
        "keyVocab": [
            { "word": "spectral analysis", "ipa": "/ˈspek.trəl əˈnæl.ə.sɪs/", "meaning": "phân tích quang phổ học" },
            { "word": "relativistic beaming", "ipa": "/ˌrel.ə.tɪˈvɪs.tɪk ˈbiː.mɪŋ/", "meaning": "hiệu ứng chùm tia tương đối tính" },
            { "word": "geometric degeneracy", "ipa": "/ˌdʒiː.əˈmet.rɪk dɪˈdʒen.ɚ.ə.si/", "meaning": "sự suy biến hình học trong đo đạc thiên văn" },
            { "word": "cross-validation", "ipa": "/ˌkrɑːs væl.əˈdeɪ.ʃən/", "meaning": "kiểm định chéo đối chiếu giữa các nguồn dữ liệu" },
            { "word": "statistically robust", "ipa": "/stəˈtɪs.tɪ.kəl.i roʊˈbʌst/", "meaning": "vững chắc về mặt thống kê học (độ tin cậy cao)" }
        ],
        "questions": [
            {
                "id": "q-19-1",
                "question": "What potential flaw did Professor Arthur raise regarding chapter four's assumptions?",
                "options": [
                    "A. Maya plagiarized her computer coding scripts from a website.",
                    "B. Assuming isotropic gamma-ray emission could overestimate kilonova ejecta mass by 30% if tilted.",
                    "C. The thesis failed to include mathematical calculations altogether.",
                    "D. The telescope used in the research was proven completely defective."
                ],
                "answerIndex": 1,
                "explanation": "Giáo sư Arthur chỉ rõ: 'chapter four assumes that the observed high-energy gamma-ray burst exhibits isotropic emission. Given relativistic beaming physics, if the jet angle was tilted merely five degrees... your total calculated kilonova ejecta mass would be overstated by thirty percent'."
            },
            {
                "id": "q-19-2",
                "question": "How did Maya resolve the geometric ambiguity in her calculations?",
                "options": [
                    "A. By guessing random numbers until the equations balanced.",
                    "B. By deleting chapter four entirely from the dissertation.",
                    "C. By cross-validating telemetry against 16 months of synchrotron radio afterglow data from the VLA.",
                    "D. By claiming neutron stars do not obey relativistic physics."
                ],
                "answerIndex": 2,
                "explanation": "Maya giải thích: 'we cross-validated the gamma-ray telemetry against late-time synchrotron radio afterglow data collected across sixteen months by the Very Large Array'."
            },
            {
                "id": "q-19-3",
                "question": "What supplementary simulation and observation technique narrowed the jet angle confidence interval?",
                "options": [
                    "A. Relativistic hydrodynamical simulations constrained by polarimetric optical observations.",
                    "B. Simple hand drawings on a physical chalkboard.",
                    "C. Taking photographs using standard commercial smartphones.",
                    "D. Asking undergraduate astronomy students for informal advice."
                ],
                "answerIndex": 0,
                "explanation": "Maya nêu rõ: 'We utilized relativistic hydrodynamical simulations constrained by polarimetric optical observations'."
            },
            {
                "id": "q-19-4",
                "question": "What was the committee chair's final reaction to Maya's defense?",
                "options": [
                    "A. Rejecting the dissertation and demanding a retake next year.",
                    "B. Conceding that the thorough radio polarimetry synthesis resolved theoretical skepticism.",
                    "C. Expelling Maya from the doctoral research department.",
                    "D. Refusing to allow any publications in scientific journals."
                ],
                "answerIndex": 1,
                "explanation": "Giáo sư Arthur hài lòng: 'That is an extraordinarily thorough defense. The incorporation of radio polarimetry addresses our primary theoretical skepticism'."
            }
        ]
    },

    # ---------------- MODULE 20 (NEW) ----------------
    {
        "id": "read-20",
        "title": "Microbiome Diversity and Psychosomatic Well-being",
        "type": "passage",
        "topic": "Sức khỏe & Y học dự phòng",
        "level": "B2 - C1",
        "summary": "Nghiên cứu y sinh về trục ruột - não (gut-brain axis), vai trò của hệ vi sinh đường ruột trong việc tổng hợp chất dẫn truyền thần kinh và điều hòa tâm trạng.",
        "content": "For more than a century, orthodox psychiatric pathology operated under a strictly neuro-centric paradigm. Mood disorders, depressive episodes, and chronic generalized anxiety were conceptualized solely as neurochemical imbalances localized within the cerebral cortex, primarily driven by monoaminergic dysregulation in synaptic junctions. Modern gastroenterology and molecular microbiology have shattered this cerebral insularity by unveiling the gut-brain axis—a bidirectional biochemical communication superhighway linking the central nervous system with the enteric microbiota.\n\nHousing over one hundred trillion microbial organisms spanning thousands of bacterial species, the human gastrointestinal tract functions as a sophisticated endocrine and neurochemical synthesis laboratory. Remarkably, an estimated ninety percent of the human body's serotonin—a critical neurotransmitter governing mood stability, circadian rhythm, and emotional valence—is synthesized not in the cranial brain, but by enterochromaffin cells in the gut lining, tightly modulated by indigenous microbiome communities.\n\nMicrobial communication with the central nervous system proceeds via multiple physiological pathways. Commensal bacteria metabolize dietary indigestible fibers into short-chain fatty acids (SCFAs), notably butyrate, acetate, and propionate. These organic metabolites cross the intestinal epithelial barrier to stimulate the vagus nerve—the primary cranial nerve connecting the brainstem to abdominal visceral organs. Furthermore, SCFAs modulate systemic immune tolerance by suppressing pro-inflammatory cytokines that otherwise compromise blood-brain barrier integrity, shielding neural tissue from neuroinflammation.\n\nConversely, chronic psychological distress and ultra-processed diets precipitate gastrointestinal dysbiosis. When harmful pathogenic bacterial strains outcompete beneficial commensals, intestinal permeability increases—a clinical condition colloquially termed \"leaky gut.\" Bacterial endotoxins, such as lipopolysaccharides, leak into peripheral bloodstream circulation, triggering systemic low-grade inflammation that directly incites depressive lethargy and cognitive fog. Consequently, nutritional psychiatry is pioneering targeted psychobiotics—beneficial bacterial strains formulated to restore microbiome homeostasis and alleviate psychiatric distress from the inside out.",
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
Trong hơn một thế kỷ, bệnh học tâm thần chính thống đã vận hành dưới một hệ hình hoàn toàn lấy não bộ làm trung tâm. Rối loạn tâm trạng, các đợt trầm cảm và lo âu mãn tính được khái niệm hóa thuần túy là sự mất cân bằng hóa thần kinh khu trú trong vỏ não, chủ yếu do rối loạn điều hòa monoaminergic tại các khớp synap. Khoa tiêu hóa và vi sinh phân tử hiện đại đã phá vỡ sự cô lập não bộ này bằng cách khám phá ra trục ruột - não—một siêu xa lộ truyền thông sinh hóa hai chiều kết nối hệ thần kinh trung ương với hệ vi sinh vật đường ruột.\n
Là nơi cư trú của hơn 100 nghìn tỷ sinh vật vi sinh bao gồm hàng nghìn loài vi khuẩn, đường tiêu hóa của con người hoạt động như một phòng thí nghiệm tổng hợp hóa thần kinh và nội tiết tinh vi. Đáng chú ý, ước tính khoảng 90% lượng serotonin của cơ thể con người—một chất dẫn truyền thần kinh quan trọng chi phối sự ổn định tâm trạng, nhịp sinh học và cảm xúc—được tổng hợp không phải trong não bộ, mà bởi các tế bào enterochromaffin trong niêm mạc ruột, được điều hòa chặt chẽ bởi các cộng đồng vi sinh vật bản địa.\n
Giao tiếp của vi sinh vật với hệ thần kinh trung ương diễn ra qua nhiều con đường sinh lý. Vi khuẩn cộng sinh chuyển hóa chất xơ không tiêu hóa được trong chế độ ăn uống thành các axit béo chuỗi ngắn (SCFA), đáng chú ý là butyrate, acetate và propionate. Các chất chuyển hóa hữu cơ này vượt qua hàng rào biểu mô ruột để kích thích dây thần kinh phế vị (vagus nerve)—dây thần kinh sọ chính kết nối thân não với các cơ quan nội tạng bụng. Hơn nữa, SCFA điều hòa khả năng dung nạp miễn dịch toàn thân bằng cách ức chế các cytokine gây viêm vốn có thể làm tổn hại tính toàn vẹn của hàng rào máu - não, che chở cho mô thần kinh khỏi viêm thần kinh.\n
Ngược lại, sự căng thẳng tâm lý mãn tính và chế độ ăn uống siêu chế biến gây ra sự mất cân bằng hệ vi sinh đường ruột (dysbiosis). Khi các chủng vi khuẩn gây bệnh có hại cạnh tranh lấn át các vi khuẩn cộng sinh có lợi, tính thấm của ruột tăng lên—một tình trạng lâm sàng thường được gọi là \"hội chứng rò rỉ ruột\". Các nội độc tố vi khuẩn, chẳng hạn như lipopolysaccharide, rò rỉ vào tuần hoàn máu ngoại vi, kích hoạt phản ứng viêm mức độ thấp toàn thân, trực tiếp gây ra sự lờ đờ uể oải và sương mù nhận thức. Do đó, ngành tâm thần học dinh dưỡng đang tiên phong sử dụng các loại psychobiotics có mục tiêu—các chủng vi khuẩn có lợi được bào chế để khôi phục cân bằng nội môi hệ vi sinh vật và làm giảm bớt sự đau khổ tâm thần từ trong ra ngoài.""",
        "keyVocab": [
            { "word": "gut-brain axis", "ipa": "/ɡʌt breɪn ˈæk.sɪs/", "meaning": "trục não - ruột (kết nối hai chiều)" },
            { "word": "vagus nerve", "ipa": "/ˈveɪ.ɡəs nɝːv/", "meaning": "dây thần kinh phế vị (dây thần kinh số X)" },
            { "word": "short-chain fatty acids", "ipa": "/ʃɔːrt tʃeɪn ˈfæt.i ˈæs.ɪdz/", "meaning": "axit béo chuỗi ngắn (SCFA)" },
            { "word": "dysbiosis", "ipa": "/ˌdɪs.baɪˈoʊ.sɪs/", "meaning": "sự mất cân bằng hệ vi sinh đường ruột" },
            { "word": "psychobiotics", "ipa": "/ˌsaɪ.koʊ.baɪˈɑː.t̬ɪks/", "meaning": "chế phẩm sinh học lợi khuẩn điều trị tâm lý" }
        ],
        "questions": [
            {
                "id": "q-20-1",
                "question": "Where is an estimated ninety percent of the human body's serotonin synthesized?",
                "options": [
                    "A. Exclusively in the prefrontal cerebral cortex.",
                    "B. In the marrow of the femur bones.",
                    "C. By enterochromaffin cells in the gut lining, modulated by the microbiome.",
                    "D. Inside hair follicles on the scalp."
                ],
                "answerIndex": 2,
                "explanation": "Đoạn 2 nêu rõ: 'an estimated ninety percent of the human body's serotonin... is synthesized not in the cranial brain, but by enterochromaffin cells in the gut lining, tightly modulated by indigenous microbiome communities'."
            },
            {
                "id": "q-20-2",
                "question": "What primary cranial nerve connects the brainstem directly to abdominal visceral organs?",
                "options": [
                    "A. The optic nerve.",
                    "B. The vagus nerve.",
                    "C. The olfactory nerve.",
                    "D. The auditory vestibular nerve."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 chỉ ra: 'stimulate the vagus nerve—the primary cranial nerve connecting the brainstem to abdominal visceral organs'."
            },
            {
                "id": "q-20-3",
                "question": "How do short-chain fatty acids (SCFAs) protect neural tissue from inflammation?",
                "options": [
                    "A. By destroying all red blood cells in circulation.",
                    "B. By suppressing pro-inflammatory cytokines that compromise blood-brain barrier integrity.",
                    "C. By preventing humans from digesting any dietary proteins.",
                    "D. By permanently disabling the immune system."
                ],
                "answerIndex": 1,
                "explanation": "Đoạn 3 giải thích: 'SCFAs modulate systemic immune tolerance by suppressing pro-inflammatory cytokines that otherwise compromise blood-brain barrier integrity, shielding neural tissue from neuroinflammation'."
            },
            {
                "id": "q-20-4",
                "question": "What happens during intestinal 'leaky gut' caused by dysbiosis?",
                "options": [
                    "A. Bacterial endotoxins leak into bloodstream circulation, triggering systemic low-grade inflammation.",
                    "B. Stomach acid disappears completely from the digestive tract.",
                    "C. The digestive system begins producing pure oxygen gas.",
                    "D. Brain tissue is converted into muscle fiber."
                ],
                "answerIndex": 0,
                "explanation": "Đoạn 4 nêu: 'Bacterial endotoxins, such as lipopolysaccharides, leak into peripheral bloodstream circulation, triggering systemic low-grade inflammation that directly incites depressive lethargy and cognitive fog'."
            }
        ]
    },

    # ---------------- MODULE 21 (NEW) ----------------
    {
        "id": "read-21",
        "title": "High-Stakes Real Estate Acquisition & Zoning Compliance",
        "type": "conversation",
        "topic": "Bất động sản & Đàm phán thương mại",
        "level": "B2 - C1",
        "summary": "Đàm phán quy hoạch phân vùng và cam kết mật độ xây dựng giữa Nhà phát triển bất động sản thương mại và Nữ Chuyên viên Quy hoạch đô thị chính quyền thành phố.",
        "content": [
            { "speaker": "Brandon (Male / Commercial Property Developer)", "text": "Clara, thank you for agreeing to review our redevelopment dossier for the Old Waterfront Wharf. Our syndicate is prepared to invest eighty million dollars to convert the derelict industrial shipyard into a mixed-use commercial and residential hub." },
            { "speaker": "Clara (Female / Municipal Urban Planning Officer)", "text": "We applaud your private capital commitment, Brandon. However, the municipal zoning code currently designates that riverbank parcel strictly as M-2 light industrial. Transitioning to mixed-use requires a formal zoning variance and municipal council approval." },
            { "speaker": "Brandon (Male / Commercial Property Developer)", "text": "Understood. Our blueprints propose a floor-area ratio (FAR) of four point five, accommodating three residential towers, ground-floor retail, and an open civic amphitheater." },
            { "speaker": "Clara (Female / Municipal Urban Planning Officer)", "text": "A FAR of four point five exceeds our waterfront density master plan by thirty percent. Furthermore, community advocates will vigorously oppose any development that impedes public riverbank access." },
            { "speaker": "Brandon (Male / Commercial Property Developer)", "text": "We anticipated those objections. To offset density concerns, we are dedicating forty percent of the parcel footprint to a continuous public riparian park and boardwalk, while offering a binding easement covenant to the city in perpetuity." },
            { "speaker": "Clara (Female / Municipal Urban Planning Officer)", "text": "The public easement covenant is a significant concession. What about mandatory inclusionary housing requirements? Municipal ordinance mandates that fifteen percent of units must qualify as affordable housing." },
            { "speaker": "Brandon (Male / Commercial Property Developer)", "text": "We are fully compliant. In fact, we designated eighteen percent of all one- and two-bedroom apartments as subsidized affordable units for low-to-middle income families." },
            { "speaker": "Clara (Female / Municipal Urban Planning Officer)", "text": "With an eighteen percent affordable commitment and a deeded public park easement, your variance application presents compelling civic merit. I will recommend it favorably for public hearing next month." }
        ],
        "vietnameseTranslation": """**Bản dịch tiếng Việt:**\n
- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Clara, cảm ơn cô đã đồng ý xem xét hồ sơ tái phát triển của chúng tôi cho khu Cảng Bến tàu cũ. Nghiệp đoàn của chúng tôi sẵn sàng đầu tư 80 triệu đô la để chuyển đổi xưởng đóng tàu công nghiệp bỏ hoang thành một trung tâm thương mại và dân cư phức hợp.\n
- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Chúng tôi hoan nghênh cam kết vốn tư nhân của bên anh, Brandon. Tuy nhiên, quy hoạch phân vùng của thành phố hiện chỉ định khu đất ven sông đó là đất công nghiệp nhẹ M-2. Việc chuyển đổi sang mục đích sử dụng hỗn hợp đòi hỏi phải có sự điều chỉnh quy hoạch phân vùng chính thức và sự phê duyệt của hội đồng thành phố.\n
- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Đã hiểu. Bản thiết kế của chúng tôi đề xuất hệ số sử dụng đất (FAR) là 4,5, bao gồm 3 tòa tháp dân cư, khu bán lẻ ở tầng trệt và một khán đài công cộng ngoài trời.\n
- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Hệ số FAR 4,5 vượt quá quy hoạch tổng thể mật độ ven sông của chúng tôi 30%. Hơn nữa, các đại diện cộng đồng sẽ kịch liệt phản đối bất kỳ sự phát triển nào cản trở lối tiếp cận bờ sông của công chúng.\n
- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Chúng tôi đã lường trước những phản đối đó. Để bù đắp cho những lo ngại về mật độ, chúng tôi dành 40% diện tích khu đất cho công viên và lối đi lót ván ven sông công cộng liên tục, đồng thời cung cấp cam kết quyền địa dịch ràng buộc cho thành phố vĩnh viễn.\n
- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Cam kết quyền địa dịch công cộng là một sự nhượng bộ đáng kể. Còn các yêu cầu bắt buộc về nhà ở xã hội hòa nhập thì sao? Quy định của thành phố bắt buộc 15% số căn hộ phải đủ điều kiện là nhà ở giá phải chăng.\n
- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Chúng tôi hoàn toàn tuân thủ. Trên thực tế, chúng tôi đã chỉ định 18% tổng số căn hộ 1 và 2 phòng ngủ làm các căn hộ được trợ cấp giá phải chăng cho các gia đình có thu nhập thấp đến trung bình.\n
- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Với cam kết 18% nhà ở giá phải chăng và chứng thư quyền địa dịch công viên công cộng, đơn xin điều chỉnh quy hoạch của anh thể hiện giá trị công dân rất thuyết phục. Tôi sẽ đưa ra khuyến nghị tích cực cho buổi điều trần công khai vào tháng tới.""",
        "keyVocab": [
            { "word": "zoning variance", "ipa": "/ˈzoʊ.nɪŋ ˈver.i.əns/", "meaning": "sự điều chỉnh/miễn trừ quy hoạch phân vùng" },
            { "word": "floor-area ratio", "ipa": "/flɔːr ˈer.i.ə ˈreɪ.ʃi.oʊ/", "meaning": "hệ số sử dụng đất (FAR)" },
            { "word": "riparian park", "ipa": "/raɪˈper.i.ən pɑːrk/", "meaning": "công viên sinh thái ven bờ sông" },
            { "word": "easement covenant", "ipa": "/ˈiːz.mənt ˈkʌv.ə.nənt/", "meaning": "cam kết quyền địa dịch công cộng (cho phép người dân đi lại vĩnh viễn)" },
            { "word": "inclusionary housing", "ipa": "/ɪnˈkluː.ʒən.er.i ˈhaʊ.zɪŋ/", "meaning": "chính sách nhà ở xã hội hòa nhập bắt buộc" }
        ],
        "questions": [
            {
                "id": "q-21-1",
                "question": "What legal zoning obstacle does Clara highlight regarding the shipyard parcel?",
                "options": [
                    "A. The river is legally owned by a foreign naval fleet.",
                    "B. The parcel is zoned strictly as M-2 light industrial, requiring a formal variance to build mixed-use.",
                    "C. Building any apartments is strictly illegal across the entire country.",
                    "D. The land is contaminated with nuclear radiation."
                ],
                "answerIndex": 1,
                "explanation": "Clara giải thích: 'the municipal zoning code currently designates that riverbank parcel strictly as M-2 light industrial. Transitioning to mixed-use requires a formal zoning variance and municipal council approval'."
            },
            {
                "id": "q-21-2",
                "question": "How does Brandon address community concerns about riverbank access?",
                "options": [
                    "A. Building a twenty-foot concrete wall topped with barbed wire.",
                    "B. Charging a mandatory twenty-dollar entrance fee to all visitors.",
                    "C. Dedicating 40% of the parcel to a public riparian park and boardwalk with a permanent easement covenant.",
                    "D. Forcing visitors to arrive exclusively by motorized speedboats."
                ],
                "answerIndex": 2,
                "explanation": "Brandon cam kết: 'we are dedicating forty percent of the parcel footprint to a continuous public riparian park and boardwalk, while offering a binding easement covenant to the city in perpetuity'."
            },
            {
                "id": "q-21-3",
                "question": "What percentage of units does Brandon pledge for affordable housing, compared to the 15% mandate?",
                "options": [
                    "A. Zero percent.",
                    "B. Exactly five percent.",
                    "C. Eighteen percent.",
                    "D. One hundred percent."
                ],
                "answerIndex": 2,
                "explanation": "Brandon nêu rõ: 'In fact, we designated eighteen percent of all one- and two-bedroom apartments as subsidized affordable units for low-to-middle income families'."
            },
            {
                "id": "q-21-4",
                "question": "What is Clara's final stance regarding the redevelopment proposal?",
                "options": [
                    "A. Recommending immediate criminal prosecution against Brandon.",
                    "B. Recommending the variance application favorably for next month's public municipal hearing.",
                    "C. Demanding that Brandon double his personal cash deposit.",
                    "D. Ordering the shipyard to be turned into a commercial coal terminal."
                ],
                "answerIndex": 1,
                "explanation": "Clara kết luận tích cực: 'With an eighteen percent affordable commitment and a deeded public park easement, your variance application presents compelling civic merit. I will recommend it favorably for public hearing next month'."
            }
        ]
    }
]

def main():
    target_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'js', 'reading_data.js')
    
    js_content = "// Bộ dữ liệu 21 bài tập Đọc hiểu (Reading Passages) & Hội thoại (Conversations)\n"
    js_content += "// Phân vai Giọng Nam & Giọng Nữ rõ ràng, kèm trắc nghiệm, giải thích chi tiết và bản dịch song ngữ\n\n"
    js_content += "const READING_DATA = " + json.dumps(READING_DATA, ensure_ascii=False, indent=4) + ";\n\n"
    js_content += "if (typeof module !== 'undefined' && module.exports) {\n"
    js_content += "    module.exports = { READING_DATA };\n"
    js_content += "}\n"

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Successfully generated {len(READING_DATA)} modules into {target_path}")

if __name__ == '__main__':
    main()
