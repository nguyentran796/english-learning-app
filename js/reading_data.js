// Bộ dữ liệu 36 bài tập Đọc hiểu (Reading Passages) & Hội thoại (Conversations)
// Phân loại độ khó rõ ràng (B1 - B2 & B2 - C1), kèm trắc nghiệm, giải thích chi tiết và bản dịch song ngữ

const READING_DATA = [
    {
        "id": "read-1",
        "title": "Contract Negotiation & Scope Alignment",
        "type": "conversation",
        "topic": "Công sở & Đàm phán",
        "level": "B2 - C1",
        "summary": "Cuộc đàm phán hợp đồng phần mềm giữa Giám đốc dự án và Đại diện khách hàng về ngân sách và thời hạn bàn giao.",
        "content": [
            {
                "speaker": "David (Male / Project Lead)",
                "text": "Good morning, Sarah. Thank you for making time today. We reviewed your requested revisions for the enterprise software rollout, particularly the expedited timeline."
            },
            {
                "speaker": "Sarah (Female / Client Rep)",
                "text": "Good morning, David. We appreciate your quick turnaround. As you know, our board expects the new billing system to go live before the third quarter to avoid fiscal overlap."
            },
            {
                "speaker": "David (Male / Project Lead)",
                "text": "We completely understand your strategic urgency. However, accelerating delivery by six weeks introduces substantial risks regarding security audits and stress testing. If we rush deployment, we risk system bottlenecks during peak transaction hours."
            },
            {
                "speaker": "Sarah (Female / Client Rep)",
                "text": "I see your point. Reliability is paramount for our financial operations. Is there a viable compromise that protects data integrity without forfeiting our third-quarter launch?"
            },
            {
                "speaker": "David (Male / Project Lead)",
                "text": "Precisely. We propose a phased implementation. We can deploy the core payment gateway and customer accounts on your target date, while deferring advanced analytics and automated reporting to phase two, four weeks later."
            },
            {
                "speaker": "Sarah (Female / Client Rep)",
                "text": "That sounds pragmatic. It addresses our immediate operational need while mitigating technical vulnerabilities. Does this phased approach impact the agreed budget?"
            },
            {
                "speaker": "David (Male / Project Lead)",
                "text": "The overall contract price remains unchanged. We merely reallocate engineering hours to prioritize core functionalities first."
            },
            {
                "speaker": "Sarah (Female / Client Rep)",
                "text": "Excellent. Please draft an addendum with this milestone schedule, and I will submit it to our executive committee for final sign-off."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **David (Nam / Trưởng dự án):** Chào buổi sáng, Sarah. Cảm ơn cô đã dành thời gian hôm nay. Chúng tôi đã xem xét các yêu cầu chỉnh sửa của bên cô cho đợt triển khai phần mềm doanh nghiệp, đặc biệt là tiến độ gấp rút.\n\n- **Sarah (Nữ / Đại diện khách hàng):** Chào David. Chúng tôi đánh giá cao sự phản hồi nhanh chóng của bên anh. Như anh đã biết, hội đồng quản trị của chúng tôi kỳ vọng hệ thống thanh toán mới sẽ đi vào hoạt động trước quý 3 để tránh trùng lặp năm tài chính.\n\n- **David (Nam / Trưởng dự án):** Chúng tôi hoàn toàn hiểu tính cấp bách mang tính chiến lược của bên cô. Tuy nhiên, việc đẩy nhanh tiến độ bàn giao sớm 6 tuần sẽ tiềm ẩn rủi ro đáng kể liên quan đến kiểm toán bảo mật và thử nghiệm chịu tải. Nếu vội vàng triển khai, hệ thống có nguy cơ nghẽn mạng vào giờ cao điểm.\n\n- **Sarah (Nữ / Đại diện khách hàng):** Tôi hiểu quan điểm của anh. Độ tin cậy là điều tối quan trọng đối với hoạt động tài chính của chúng tôi. Liệu có phương án thỏa hiệp khả thi nào vừa bảo vệ tính toàn vẹn dữ liệu mà không làm lỡ đợt ra mắt quý 3 không?\n\n- **David (Nam / Trưởng dự án):** Chính xác là vậy. Chúng tôi đề xuất triển khai theo giai đoạn. Chúng ta có thể đưa cổng thanh toán cốt lõi và tài khoản khách hàng vận hành đúng ngày mục tiêu của cô, trong khi dời phần phân tích nâng cao và báo cáo tự động sang giai đoạn hai, sau đó 4 tuần.\n\n- **Sarah (Nữ / Đại diện khách hàng):** Nghe rất thực tế. Cách này giải quyết được nhu cầu vận hành tức thì trong khi giảm thiểu các lỗ hổng kỹ thuật. Liệu cách tiếp cận theo giai đoạn này có ảnh hưởng đến ngân sách đã thỏa thuận không?\n\n- **David (Nam / Trưởng dự án):** Tổng giá trị hợp đồng vẫn giữ nguyên. Chúng tôi chỉ phân bổ lại số giờ kỹ thuật để ưu tiên các chức năng cốt lõi trước.\n\n- **Sarah (Nữ / Đại diện khách hàng):** Tuyệt vời. Xin hãy soạn một phụ lục hợp đồng với lịch trình các cột mốc này, tôi sẽ nộp lên ban điều hành để ký duyệt chính thức.",
        "keyVocab": [
            {
                "word": "expedited timeline",
                "ipa": "/ˈek.spə.daɪ.t̬ɪd ˈtaɪm.laɪn/",
                "meaning": "tiến độ được đẩy nhanh/rút ngắn"
            },
            {
                "word": "paramount",
                "ipa": "/ˈper.ə.maʊnt/",
                "meaning": "tối quan trọng, hàng đầu"
            },
            {
                "word": "bottleneck",
                "ipa": "/ˈbɑː.t̬əl.nek/",
                "meaning": "điểm nghẽn, sự đình trệ"
            },
            {
                "word": "phased implementation",
                "ipa": "/feɪzd ˌɪm.plə.menˈteɪ.ʃən/",
                "meaning": "triển khai chia theo từng giai đoạn"
            },
            {
                "word": "addendum",
                "ipa": "/əˈden.dəm/",
                "meaning": "phụ lục bổ sung hợp đồng"
            }
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
    {
        "id": "read-2",
        "title": "The Transformative Role of AI in Contemporary Medicine",
        "type": "passage",
        "topic": "Khoa học & Công nghệ",
        "level": "B2 - C1",
        "summary": "Đoạn văn phân tích cách trí tuệ nhân tạo đang cách mạng hóa chẩn đoán y khoa, đồng thời đặt ra những thách thức về đạo đức và trách nhiệm giải trình.",
        "content": "The integration of artificial intelligence into diagnostic healthcare represents one of the most remarkable technological paradigm shifts of the twenty-first century. For decades, medical practitioners relied strictly on empirical clinical observation, manual laboratory assays, and radiological scans interpreted solely through human judgment. While experienced clinicians possess profound diagnostic intuition, human stamina is intrinsically finite, and cognitive fatigue inevitably impairs diagnostic precision during prolonged shifts.\n\nDeep learning convolutional neural networks have begun augmenting clinical workflows by analyzing vast databases of high-resolution magnetic resonance imaging (MRI) and computerized tomography (CT) scans. In oncology, specialized algorithms routinely detect micro-calcifications and malignant cellular clusters several months before they become perceptible to the naked human eye. By cross-referencing patient biometric histories with millions of digitized international clinical records, predictive algorithms also calculate individualized risk scores for cardiovascular deterioration, empowering physicians to prescribe preventative interventions well before acute episodes occur.\n\nNonetheless, medical ethicists caution against premature euphoria. A central challenge lies in the \"black box\" dilemma—the inherent opacity of deep neural networks whose internal weighting mechanisms are largely inscrutable even to their software architects. When an autonomous algorithmic system recommends an invasive surgical intervention or withholds a life-saving therapy, establishing legal liability and ethical accountability becomes intensely contentious. If a flawed recommendation arises from skewed training datasets that underrepresent specific demographic groups, diagnostic disparities are perpetuated rather than eradicated.\n\nConsequently, the prevailing consensus within the international medical community advocates for an augmented intelligence model rather than outright clinical automation. In this framework, artificial intelligence functions as an indispensable copilot: synthesizing complex telemetry, flagging anomalies, and eliminating repetitive clerical administrative burdens, while leaving empathetic bedside communication, nuanced ethical deliberations, and ultimate treatment authorization firmly in human hands.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nViệc tích hợp trí tuệ nhân tạo vào chẩn đoán y tế đại diện cho một trong những bước chuyển đổi hệ hình công nghệ đáng chú ý nhất của thế kỷ 21. Trong nhiều thập kỷ, các bác sĩ chỉ dựa vào quan sát lâm sàng thực nghiệm, các xét nghiệm thủ công trong phòng thí nghiệm và phim chụp X-quang được diễn giải hoàn toàn bằng đánh giá của con người. Mặc dù các bác sĩ giàu kinh nghiệm sở hữu trực giác chẩn đoán sâu sắc, sức bền của con người về bản chất là có hạn, và sự mệt mỏi về nhận thức chắc chắn làm suy giảm độ chính xác của chẩn đoán trong các ca trực kéo dài.\n\nMạng nơ-ron tích chập học sâu đã bắt đầu hỗ trợ quy trình lâm sàng bằng cách phân tích cơ sở dữ liệu khổng lồ gồm các ảnh chụp cộng hưởng từ (MRI) và cắt lớp vi tính (CT) độ phân giải cao. Trong khoa ung bướu, các thuật toán chuyên biệt thường xuyên phát hiện các ổ vi vôi hóa và các cụm tế bào ác tính vài tháng trước khi chúng có thể nhìn thấy bằng mắt thường. Bằng cách đối chiếu lịch sử sinh trắc học của bệnh nhân với hàng triệu hồ sơ bệnh án quốc tế được số hóa, các thuật toán dự đoán cũng tính toán điểm rủi ro cá nhân hóa đối với sự suy giảm tim mạch, trao quyền cho bác sĩ kê đơn can thiệp phòng ngừa rất lâu trước khi các đợt cấp tính xảy ra.\n\nTuy nhiên, các nhà đạo đức học y tế cảnh báo không nên quá lạc quan sớm. Một thách thức cốt lõi nằm ở thế tiến thoái lưỡng nan \"hộp đen\"—sự mờ đục vốn có của các mạng nơ-ron sâu mà các cơ chế trọng số bên trong của chúng phần lớn là không thể hiểu thấu ngay cả đối với chính các kiến trúc sư phần mềm tạo ra chúng. Khi một hệ thống thuật toán tự chủ đề xuất một can thiệp phẫu thuật xâm lấn hoặc từ chối một liệu pháp cứu mạng, việc xác định trách nhiệm pháp lý và trách nhiệm giải trình đạo đức trở nên vô cùng căng thẳng. Nếu một khuyến nghị sai sót phát sinh từ bộ dữ liệu huấn luyện bị lệch thiên lệch, vốn ít đại diện cho các nhóm nhân khẩu học cụ thể, thì sự chênh lệch trong chẩn đoán sẽ bị duy trì kéo dài thay vì bị loại bỏ.\n\nDo đó, sự đồng thuận phổ biến trong cộng đồng y tế quốc tế ủng hộ mô hình \"trí tuệ tăng cường\" thay vì tự động hóa lâm sàng hoàn toàn. Trong khuôn khổ này, trí tuệ nhân tạo hoạt động như một trợ lý không thể thiếu: tổng hợp dữ liệu viễn thám phức tạp, gắn cờ các điểm bất thường và loại bỏ gánh nặng hành chính lặp đi lặp lại, đồng thời để việc giao tiếp thấu cảm bên giường bệnh, những cân nhắc đạo đức tinh tế và quyết định điều trị cuối cùng nằm chắc chắn trong tay con người.",
        "keyVocab": [
            {
                "word": "paradigm shift",
                "ipa": "/ˈper.ə.daɪm ʃɪft/",
                "meaning": "bước chuyển đổi hệ hình tư duy/công nghệ"
            },
            {
                "word": "micro-calcification",
                "ipa": "/ˌmaɪ.kroʊ kæl.sə.fəˈkeɪ.ʃən/",
                "meaning": "vi vôi hóa (dấu hiệu sớm của khối u ác tính)"
            },
            {
                "word": "black box dilemma",
                "ipa": "/blæk bɑːks dɪˈlem.ə/",
                "meaning": "thế tiến thoái lưỡng nan về tính không minh bạch của AI"
            },
            {
                "word": "inscrutable",
                "ipa": "/ɪnˈskruː.t̬ə.bəl/",
                "meaning": "khôn dò, không thể giải mã/hiểu thấu"
            },
            {
                "word": "augmented intelligence",
                "ipa": "/ɑːɡˈmen.t̬ɪd ɪnˈtel.ə.dʒəns/",
                "meaning": "trí tuệ tăng cường (AI hỗ trợ con người thay vì thay thế)"
            }
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
    {
        "id": "read-3",
        "title": "Resolving Interdepartmental Friction",
        "type": "conversation",
        "topic": "Công sở & Đàm phán",
        "level": "B2 - C1",
        "summary": "Cuộc đối thoại giữa Trưởng phòng Tiếp thị và Nữ Trưởng phòng Kỹ thuật nhằm tháo gỡ bất đồng về tính năng sản phẩm và cam kết với khách hàng.",
        "content": [
            {
                "speaker": "Liam (Male / Marketing Director)",
                "text": "Elena, thanks for sitting down with me. We noticed some tension during yesterday's all-hands briefing regarding the Q4 feature roadmap."
            },
            {
                "speaker": "Elena (Female / Head of Engineering)",
                "text": "I'll be candid, Liam. The marketing team announced real-time collaboration features in your public promotional webinars before engineering even finalized the backend architecture. That puts unfair pressure on my developers."
            },
            {
                "speaker": "Liam (Male / Marketing Director)",
                "text": "I acknowledge your frustration. Our sales reps were facing aggressive counter-campaigns from our primary rival, and we felt compelled to demonstrate our competitive edge. But I admit we jumped the gun without verifying sprint capacities."
            },
            {
                "speaker": "Elena (Female / Head of Engineering)",
                "text": "When marketing makes promises without technical vetting, it leads to two bad outcomes: either we cut corners on code quality and release buggy software, or my team burns the midnight oil and suffers demoralizing burnout."
            },
            {
                "speaker": "Liam (Male / Marketing Director)",
                "text": "Neither outcome is acceptable to anyone in leadership. Let's establish a formal synchronization protocol. Moving forward, marketing will not publicize any capability that has not cleared stage-three QA testing."
            },
            {
                "speaker": "Elena (Female / Head of Engineering)",
                "text": "I appreciate that commitment. In return, I will designate a senior technical lead to attend your bi-weekly campaign brainstorms to provide realistic feasibility assessments early on."
            },
            {
                "speaker": "Liam (Male / Marketing Director)",
                "text": "That would be immensely helpful. It guarantees that our client messaging remains innovative while grounded in technical reality."
            },
            {
                "speaker": "Elena (Female / Head of Engineering)",
                "text": "Agreed. Let us communicate this unified alignment to our respective departments this afternoon."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Liam (Nam / Giám đốc Tiếp thị):** Elena, cảm ơn cô đã ngồi lại cùng tôi. Chúng tôi nhận thấy có chút căng thẳng trong buổi họp toàn thể hôm qua liên quan đến lộ trình tính năng quý 4.\n\n- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Tôi xin nói thẳng thắn, Liam. Đội tiếp thị của anh đã công bố các tính năng cộng tác theo thời gian thực trên các hội thảo quảng bá công khai trước khi đội kỹ thuật hoàn tất kiến trúc phụ trợ. Điều đó tạo ra áp lực bất công lên các lập trình viên của tôi.\n\n- **Liam (Nam / Giám đốc Tiếp thị):** Tôi thừa nhận sự bức xúc của cô. Đội ngũ bán hàng của chúng tôi đang phải đối mặt với các chiến dịch đối đầu gay gắt từ đối thủ cạnh tranh chính, và chúng tôi cảm thấy buộc phải thể hiện lợi thế cạnh tranh của mình. Nhưng tôi thừa nhận chúng tôi đã vội vàng cầm đèn chạy trước ô tô mà chưa xác minh công suất của đợt chạy nước rút (sprint).\n\n- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Khi tiếp thị hứa hẹn mà không có sự kiểm tra kỹ thuật, điều đó dẫn đến hai kết quả tồi tệ: hoặc là chúng tôi làm ẩu giảm chất lượng mã nguồn và phát hành phần mềm nhiều lỗi, hoặc là đội của tôi phải thức thâu đêm làm việc và bị kiệt sức làm suy giảm tinh thần.\n\n- **Liam (Nam / Giám đốc Tiếp thị):** Cả hai kết cục đó đều không thể chấp nhận được đối với ban lãnh đạo. Chúng ta hãy thiết lập một quy trình đồng bộ hóa chính thức. Kể từ nay trở đi, tiếp thị sẽ không công bố bất kỳ tính năng nào chưa vượt qua bài kiểm tra đảm bảo chất lượng (QA) giai đoạn ba.\n\n- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Tôi đánh giá cao cam kết đó. Đổi lại, tôi sẽ chỉ định một trưởng nhóm kỹ thuật cao cấp tham gia các buổi thảo luận chiến dịch hai tuần một lần của bên anh để đưa ra các đánh giá tính khả thi thực tế ngay từ đầu.\n\n- **Liam (Nam / Giám đốc Tiếp thị):** Điều đó sẽ vô cùng hữu ích. Nó đảm bảo thông điệp gửi tới khách hàng của chúng ta vừa mang tính đổi mới vừa dựa trên thực tế kỹ thuật.\n\n- **Elena (Nữ / Trưởng phòng Kỹ thuật):** Nhất trí. Chiều nay chúng ta hãy truyền đạt sự thống nhất này tới các phòng ban tương ứng của mình.",
        "keyVocab": [
            {
                "word": "candid",
                "ipa": "/ˈkæn.dɪd/",
                "meaning": "thẳng thắn, bộc trực"
            },
            {
                "word": "jump the gun",
                "ipa": "/dʒʌmp ðə ɡʌn/",
                "meaning": "cầm đèn chạy trước ô tô, hành động quá vội vàng"
            },
            {
                "word": "cut corners",
                "ipa": "/kʌt ˈkɔːr.nɚz/",
                "meaning": "làm ẩu, bớt xén quy trình"
            },
            {
                "word": "burn the midnight oil",
                "ipa": "/bɜːrn ðə ˈmɪd.naɪt ɔɪl/",
                "meaning": "thức khuya miệt mài làm việc"
            },
            {
                "word": "technical vetting",
                "ipa": "/ˈtek.nɪ.kəl ˈvet̬.ɪŋ/",
                "meaning": "sự kiểm tra/thẩm định kỹ thuật"
            }
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
    {
        "id": "read-4",
        "title": "The Architecture of Sustainable Urban Ecosystems",
        "type": "passage",
        "topic": "Môi trường & Xã hội",
        "level": "B2 - C1",
        "summary": "Bài luận về việc tái cấu trúc các đại đô thị hiện đại nhằm giảm thiểu phát thải carbon, tích hợp không gian xanh và thúc đẩy giao thông bền vững.",
        "content": "By the mid-twenty-first century, demographic projections estimate that over two-thirds of the planetary population will reside in metropolitan sprawls. Rapid, uncontrolled urbanization historically inflicted catastrophic ecological tolls: vast swathes of heat-absorbing asphalt, rampant carbon emissions from combustion-engine gridlock, and the widespread eradication of native biodiversity. In response, avant-garde urban planners are repudiating the legacy twentieth-century ethos of car-centric zoning in favor of regenerative, circular urban design.\n\nAt the forefront of this transformation is the \"15-minute city\" paradigm, which reorganizes urban topology so that essential daily amenities—grocery markets, primary healthcare centers, educational facilities, and communal parks—are accessible within a quarter-hour walk or bicycle ride from any residence. By decentralizing public infrastructure, municipalities curtail vehicular dependency, dramatically suppressing localized nitrogen dioxide and particulate emissions while invigorating neighborhood social cohesion.\n\nSimultaneously, structural engineering is experiencing an organic renaissance through the adoption of biophilic architecture and carbon-sequestering building materials. Traditional concrete and steel production generates approximately fifteen percent of global greenhouse emissions. Progressive developers are pioneering structural cross-laminated timber (CLT)—sustainably harvested wood engineered to match the compressive strength of reinforced concrete while functioning as a permanent carbon sink. Furthermore, retrofitting urban facades with vertical forests and permeable sponge-city pavements mitigates the deadly urban heat island effect, allowing metropolitan centers to absorb flash flood monsoons naturally.\n\nNevertheless, implementing systemic urban regeneration requires navigating precarious socioeconomic fault lines. Aggressive infrastructural beautification frequently precipitates \"green gentrification\"—an inflationary cycle where escalating property valuations displace long-standing low-income communities who endured decades of environmental disinvestment. Therefore, genuine urban sustainability cannot remain a purely architectural pursuit; it necessitates rigorous municipal rent stabilization covenants and equitable transit equity subsidies to guarantee that cleaner, greener cities shelter all socioeconomic tiers unconditionally.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nĐến giữa thế kỷ 21, các dự báo nhân khẩu học ước tính rằng hơn 2/3 dân số hành tinh sẽ cư trú tại các đô thị mở rộng. Quá trình đô thị hóa nhanh chóng, mất kiểm soát trong lịch sử đã gây ra những tổn thất sinh thái thảm khốc: những dải nhựa đường hấp thụ nhiệt khổng lồ, lượng khí thải carbon tràn lan từ nạn kẹt xe động cơ đốt trong và sự xóa sổ diện rộng đa dạng sinh học bản địa. Để đối phó, các nhà quy hoạch đô thị tiên phong đang bác bỏ đặc tính quy hoạch lấy xe hơi làm trung tâm của thế kỷ 20 để hướng tới thiết kế đô thị tuần hoàn, có tính tái tạo.\n\nĐi đầu trong sự chuyển đổi này là mô hình \"thành phố 15 phút\", tổ chức lại địa hình đô thị sao cho các tiện ích thiết yếu hàng ngày—chợ tạp hóa, trung tâm y tế ban đầu, cơ sở giáo dục và công viên công cộng—có thể tiếp cận được trong vòng 15 phút đi bộ hoặc đạp xe từ bất kỳ nơi cư trú nào. Bằng cách phân cấp cơ sở hạ tầng công cộng, chính quyền đô thị hạn chế sự phụ thuộc vào phương tiện giao thông, ngăn chặn đáng kể lượng khí thải nitơ dioxide và bụi mịn cục bộ, đồng thời tiếp thêm sinh lực cho sự gắn kết xã hội trong khu phố.\n\nĐồng thời, kỹ thuật kết cấu đang trải qua một thời kỳ phục hưng hữu cơ thông qua việc áp dụng kiến trúc ưa sinh học (biophilic) và các vật liệu xây dựng cô lập carbon. Sản xuất bê tông và thép truyền thống tạo ra khoảng 15% lượng khí thải nhà kính toàn cầu. Các nhà phát triển tiến bộ đang tiên phong sử dụng gỗ nhiều lớp cấu trúc (CLT)—loại gỗ được thu hoạch bền vững được chế tạo để sánh ngang với cường độ nén của bê tông cốt thép trong khi hoạt động như một bể chứa carbon vĩnh viễn. Hơn nữa, việc cải tạo các mặt đứng đô thị bằng các khu rừng thẳng đứng và vỉa hè thấm nước theo mô hình \"thành phố bọt biển\" giúp giảm thiểu hiệu ứng đảo nhiệt đô thị chết người, cho phép các trung tâm đô thị hấp thụ các trận lũ quét do gió mùa một cách tự nhiên.\n\nTuy nhiên, việc thực hiện tái tạo đô thị mang tính hệ thống đòi hỏi phải vượt qua những ranh giới kinh tế xã hội bấp bênh. Việc chỉnh trang cơ sở hạ tầng quá mức thường dẫn đến \"chỉnh trang đô thị xanh\" (green gentrification)—một chu kỳ lạm phát nơi giá trị bất động sản leo thang làm dịch chuyển, đẩy những cộng đồng thu nhập thấp lâu đời, những người đã chịu đựng hàng thập kỷ thiếu đầu tư môi trường, ra khỏi nơi ở. Do đó, tính bền vững đô thị thực sự không thể chỉ là một mục tiêu kiến trúc thuần túy; nó đòi hỏi các thỏa ước bình ổn giá thuê nhà nghiêm ngặt của chính quyền thành phố và các khoản trợ cấp bình đẳng về giao thông công cộng để đảm bảo rằng các thành phố sạch hơn, xanh hơn sẽ che chở cho tất cả các tầng lớp kinh tế xã hội một cách vô điều kiện.",
        "keyVocab": [
            {
                "word": "metropolitan sprawl",
                "ipa": "/ˌmet.rəˈpɑː.lɪ.tən sprɑːl/",
                "meaning": "sự mở rộng đô thị quá mức"
            },
            {
                "word": "15-minute city",
                "ipa": "/ˌfɪf.tiːn ˈmɪn.ɪt ˈsɪt.i/",
                "meaning": "mô hình đô thị tiện ích 15 phút"
            },
            {
                "word": "cross-laminated timber",
                "ipa": "/krɑːs ˈlæm.ə.neɪ.t̬ɪd ˈtɪm.bɚ/",
                "meaning": "gỗ dán nhiều lớp cấu trúc chịu lực (CLT)"
            },
            {
                "word": "sponge-city pavement",
                "ipa": "/spʌndʒ ˈsɪt.i ˈpeɪv.mənt/",
                "meaning": "vỉa hè thấm nước theo mô hình thành phố bọt biển"
            },
            {
                "word": "green gentrification",
                "ipa": "/ɡriːn ˌdʒen.trə.fəˈkeɪ.ʃən/",
                "meaning": "chỉnh trang xanh đẩy giá nhà cao khiến người nghèo bị di dời"
            }
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
    {
        "id": "read-5",
        "title": "Flight Cancellation & Emergency Rerouting",
        "type": "conversation",
        "topic": "Du lịch & Tình huống khẩn cấp",
        "level": "B1 - B2",
        "summary": "Tình huống giao tiếp thực tế tại quầy dịch vụ sân bay quốc tế khi hành khách bị hủy chuyến bay nối chuyến do bão tuyết.",
        "content": [
            {
                "speaker": "James (Male / Stranded Passenger)",
                "text": "Excuse me, miss. My connecting flight to Frankfurt, LH 402, was abruptly marked as canceled on the departures board. I have an indispensable business summit tomorrow morning."
            },
            {
                "speaker": "Emily (Female / Airline Customer Representative)",
                "text": "I truly apologize for the disruption, sir. A severe blizzard over northern Europe prompted ground stops across several hub airports. Let me pull up your booking reference."
            },
            {
                "speaker": "James (Male / Stranded Passenger)",
                "text": "Here is my passport and boarding pass. Are there any partner airlines operating flights later this evening, even with an alternate layover?"
            },
            {
                "speaker": "Emily (Female / Airline Customer Representative)",
                "text": "Let me check our Star Alliance network. There is a Swiss International Air flight departing at 9:30 PM via Zurich with a two-hour transfer, landing in Frankfurt at 7:15 AM tomorrow."
            },
            {
                "speaker": "James (Male / Stranded Passenger)",
                "text": "That would get me to my conference just in the nick of time. Can you confirm a confirmed seat for me on that route?"
            },
            {
                "speaker": "Emily (Female / Airline Customer Representative)",
                "text": "Yes, I managed to secure an aisle seat in economy. I am transferring your checked baggage directly to the Zurich route, so you will not need to re-claim it here."
            },
            {
                "speaker": "James (Male / Stranded Passenger)",
                "text": "That is a huge relief. Since I have a five-hour wait until the 9:30 PM departure, does the airline provide meal compensation?"
            },
            {
                "speaker": "Emily (Female / Airline Customer Representative)",
                "text": "Certainly. Here is a thirty-euro meal voucher valid at any terminal restaurant, alongside your updated boarding passes. Gate B22 opens at 8:45 PM."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **James (Nam / Hành khách bị lỡ chuyến):** Xin lỗi cô. Chuyến bay nối chuyến của tôi đi Frankfurt, số hiệu LH 402, vừa đột ngột bị thông báo hủy trên bảng khởi hành. Tôi có một hội nghị kinh doanh tối quan trọng vào sáng mai.\n\n- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Tôi rất xin lỗi vì sự gián đoạn này, thưa quý khách. Một trận bão tuyết dữ dội ở Bắc Âu đã khiến nhiều sân bay trung chuyển phải dừng bay mặt đất. Xin để tôi mở mã đặt chỗ của quý khách.\n\n- **James (Nam / Hành khách bị lỡ chuyến):** Hộ chiếu và thẻ lên máy bay của tôi đây. Liệu có hãng bay đối tác nào có chuyến bay tối nay không, kể cả phải quá cảnh ở điểm khác?\n\n- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Để tôi kiểm tra trong mạng lưới liên minh Star Alliance. Có một chuyến bay của hãng Thụy Sĩ (Swiss International Air) khởi hành lúc 9:30 tối quá cảnh qua Zurich trong 2 giờ, hạ cánh xuống Frankfurt lúc 7:15 sáng mai.\n\n- **James (Nam / Hành khách bị lỡ chuyến):** Lịch trình đó sẽ giúp tôi đến hội nghị vừa kịp lúc sát nút. Cô có thể xác nhận cho tôi một ghế chắc chắn trên chuyến bay đó không?\n\n- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Vâng, tôi đã giữ được một ghế lối đi ở hạng phổ thông cho quý khách. Tôi đang chuyển hành lý ký gửi của quý khách trực tiếp sang chặng Zurich, nên quý khách không cần phải lấy lại hành lý tại đây.\n\n- **James (Nam / Hành khách bị lỡ chuyến):** Thật là nhẹ nhõm. Vì tôi phải chờ 5 tiếng cho đến giờ bay 9:30 tối, hãng có bồi hoàn bữa ăn không?\n\n- **Emily (Nữ / Đại diện dịch vụ hãng bay):** Chắc chắn rồi ạ. Đây là phiếu ăn trị giá 30 euro có giá trị tại bất kỳ nhà hàng nào trong nhà ga, cùng với thẻ lên máy bay mới của quý khách. Cửa B22 sẽ mở lúc 8:45 tối ạ.",
        "keyVocab": [
            {
                "word": "indispensable",
                "ipa": "/ˌɪn.dɪˈspen.sə.bəl/",
                "meaning": "không thể thiếu, tối quan trọng"
            },
            {
                "word": "blizzard",
                "ipa": "/ˈblɪz.ɚd/",
                "meaning": "cơn bão tuyết dữ dội"
            },
            {
                "word": "layover",
                "ipa": "/ˈleɪˌoʊ.vɚ/",
                "meaning": "thời gian quá cảnh/dừng nghỉ giữa chuyến bay"
            },
            {
                "word": "in the nick of time",
                "ipa": "/ɪn ðə nɪk əv taɪm/",
                "meaning": "vừa kịp lúc, sát nút"
            },
            {
                "word": "meal voucher",
                "ipa": "/miːl ˈvaʊ.tʃɚ/",
                "meaning": "phiếu ăn miễn phí bồi hoàn"
            }
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
    {
        "id": "read-6",
        "title": "The Psychology of Habit Formation & Cognitive Momentum",
        "type": "passage",
        "topic": "Tâm lý & Nhận thức",
        "level": "B2 - C1",
        "summary": "Phân tích khoa học thần kinh về cách não bộ hình thành thói quen thông qua vòng lặp gợi ý - hành động - phần thưởng, và chiến lược xây dựng đà nhận thức bền vững.",
        "content": "Human behavior is fundamentally dictated not by conscious, deliberative willpower, but by deeply automated neural habit loops. Cognitive neuroscientists estimate that between forty to fifty percent of daily human activities—from brushing teeth to reflexively checking smartphone feeds—are executed under subcortical automaticity. The brain, evolved to conserve scarce glucose, continually seeks to streamline repetitive decision-making by delegating routine behavioral sequences to the basal ganglia.\n\nThis automaticity operates via a three-part mechanism: the cue, the routine, and the reward. The cue acts as a sensory or temporal trigger that alerts the brain to initiate a specialized behavioral routine. Once the behavior executes, the brain receives a biochemical reward—frequently a pulse of dopamine—which reinforces neural synaptic pathways, cementing the likelihood that the routine will recur upon subsequent exposure to the identical cue. Over time, anticipation of the reward transforms into a subconscious neurological craving.\n\nCrucially, common self-help doctrines that urge individuals to rely exclusively on raw willpower to overhaul their lives fail to appreciate the physiology of cognitive depletion. Deliberate decision-making resides in the prefrontal cortex, a metabolically demanding brain region susceptible to decision fatigue. Under prolonged emotional stress or physical exhaustion, prefrontal executive control atrophies, causing the individual to default reflexively to hardwired, legacy habit routines—often destructive vices like compulsive snacking or sedentary procrastination.\n\nConsequently, behavioral architects advocate for \"habit stacking\" and environmental optimization rather than heroic self-discipline. By anchoring a desired nascent habit directly onto an immutable pre-existing routine (for example: \"Immediately after pouring my morning coffee, I will review ten English vocabulary cards for five minutes\"), friction is minimized. Furthermore, designing an environment where beneficial cues are glaringly obvious and counterproductive distractions are physically obstructed leverages the brain's innate inertia, transforming deliberate aspirations into frictionless, lifelong momentum.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nHành vi của con người về cơ bản không được quyết định bởi ý chí có ý thức, suy tính kỹ lưỡng, mà bởi các vòng lặp thói quen thần kinh tự động hóa sâu sắc. Các nhà khoa học thần kinh nhận thức ước tính rằng từ 40 đến 50% các hoạt động hàng ngày của con người—từ đánh răng đến phản xạ kiểm tra bảng tin điện thoại thông minh—được thực hiện dưới sự tự động hóa của vùng dưới vỏ não. Bộ não, vốn tiến hóa để bảo tồn lượng glucose khan hiếm, liên tục tìm cách tinh giản việc ra quyết định lặp đi lặp lại bằng cách ủy quyền các chuỗi hành vi thường nhật cho hạch nền (basal ganglia).\n\nCơ chế tự động hóa này vận hành thông qua một quy trình ba phần: gợi ý (cue), thói quen hành động (routine) và phần thưởng (reward). Gợi ý đóng vai trò là tác nhân kích hoạt cảm giác hoặc thời gian báo cho não bắt đầu một chuỗi hành động chuyên biệt. Sau khi hành vi thực hiện xong, não nhận được phần thưởng sinh hóa—thường là một đợt giải phóng dopamine—giúp củng cố các đường dẫn synap thần kinh, khắc sâu khả năng thói quen đó sẽ tái diễn khi gặp lại gợi ý giống hệt. Theo thời gian, sự mong đợi phần thưởng sẽ biến thành một cơn thèm muốn thần kinh trong tiềm thức.\n\nĐiều quan trọng là các giáo lý phát triển bản thân phổ biến thúc giục các cá nhân chỉ dựa vào ý chí đơn thuần để thay đổi cuộc sống đã không nhận thức được sinh lý học của sự cạn kiệt nhận thức. Việc ra quyết định có chủ ý nằm ở vỏ não trước trán, một vùng não đòi hỏi nhiều năng lượng trao đổi chất và rất dễ bị mệt mỏi khi phải ra quyết định liên tục. Dưới sự căng thẳng cảm xúc kéo dài hoặc kiệt sức thể chất, khả năng kiểm soát điều hành của vỏ não trước trán bị suy giảm, khiến cá nhân quay trở lại một cách vô thức với các thói quen cũ đã ăn sâu—thường là những tật xấu tiêu cực như ăn vặt theo cảm xúc hoặc trì hoãn thụ động.\n\nDo đó, các nhà kiến trúc hành vi ủng hộ phương pháp \"xếp chồng thói quen\" (habit stacking) và tối ưu hóa môi trường hơn là sự tự kỷ luật phi thường mang tính anh hùng. Bằng cách gắn một thói quen mới mong muốn trực tiếp vào một thói quen cũ đã bất biến (ví dụ: \"Ngay sau khi rót cà phê buổi sáng, tôi sẽ xem lại 10 thẻ từ vựng tiếng Anh trong 5 phút\"), lực cản sẽ được giảm thiểu. Hơn nữa, việc thiết kế một môi trường nơi các tín hiệu có lợi hiển hiện rõ ràng và những thứ gây xao nhãng phản tác dụng bị cản trở về mặt vật lý sẽ tận dụng quán tính bẩm sinh của não bộ, biến những khát vọng có chủ ý thành đà phát triển trơn tru, bền bỉ suốt đời.",
        "keyVocab": [
            {
                "word": "automaticity",
                "ipa": "/ˌɑː.t̬ə.məˈtɪs.ə.t̬i/",
                "meaning": "tính tự động hóa trong phản xạ thần kinh"
            },
            {
                "word": "basal ganglia",
                "ipa": "/ˈbeɪ.səl ˈɡæŋ.ɡli.ə/",
                "meaning": "hạch nền não bộ (nơi lưu trữ thói quen tự động)"
            },
            {
                "word": "decision fatigue",
                "ipa": "/dɪˈsɪʒ.ən fəˈtiːɡ/",
                "meaning": "sự mệt mỏi khi phải đưa ra quá nhiều quyết định"
            },
            {
                "word": "habit stacking",
                "ipa": "/ˈhæb.ɪt ˈstæk.ɪŋ/",
                "meaning": "kỹ thuật xếp chồng thói quen mới lên thói quen cũ"
            },
            {
                "word": "cognitive momentum",
                "ipa": "/ˈkɑːɡ.nə.t̬ɪv moʊˈmen.t̬əm/",
                "meaning": "đà phát triển nhận thức trơn tru không ma sát"
            }
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
    {
        "id": "read-7",
        "title": "Cross-Border Supply Chain Disruption",
        "type": "conversation",
        "topic": "Logistics & Thương mại quốc tế",
        "level": "B2 - C1",
        "summary": "Cuộc thảo luận khẩn cấp giữa Giám đốc Vận tải Quốc tế và Nữ Giám đốc Thu mua Toàn cầu để điều phối lộ trình vận chuyển sau sự cố tắc nghẽn cảng biển.",
        "content": [
            {
                "speaker": "Marcus (Male / Logistics Director)",
                "text": "Lin, we just received an alert from our freight forwarding syndicate. Severe port congestion at the regional transshipment hub has delayed our inbound container vessels by at least twelve days."
            },
            {
                "speaker": "Lin (Female / Global Sourcing Manager)",
                "text": "That is alarming, Marcus. Our domestic assembly facilities are operating on a lean inventory model. If the semiconductor modules don't arrive by Tuesday, our production line faces an indefinite standstill."
            },
            {
                "speaker": "Marcus (Male / Logistics Director)",
                "text": "We anticipated this bottleneck. I have already initiated contingency protocols with air-freight carriers. We can air-lift twenty metric tons of critical chips directly from the fabrication plant to stave off a factory shutdown."
            },
            {
                "speaker": "Lin (Female / Global Sourcing Manager)",
                "text": "Air cargo rates are currently four times higher than maritime transit. How will this cost spike impact our quarterly procurement margins?"
            },
            {
                "speaker": "Marcus (Male / Logistics Director)",
                "text": "The freight premium will indeed increase logistical overhead by approximately eighty thousand dollars. However, the contractual penalties for halting client deliveries would surpass half a million dollars."
            },
            {
                "speaker": "Lin (Female / Global Sourcing Manager)",
                "text": "When you frame it against liquidated damages, the expenditure is entirely justified. What about the non-urgent bulk raw materials?"
            },
            {
                "speaker": "Marcus (Male / Logistics Director)",
                "text": "Those will be rerouted via secondary feeder vessels to a less congested neighboring terminal and trucked overland."
            },
            {
                "speaker": "Lin (Female / Global Sourcing Manager)",
                "text": "Splendid decision. Please authorize the air charters immediately and keep me posted on customs clearance timestamps."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Lin, chúng ta vừa nhận được cảnh báo từ nghiệp đoàn giao nhận vận tải. Tình trạng tắc nghẽn nghiêm trọng tại cảng trung chuyển khu vực đã làm chậm các tàu chở container cập bến ít nhất 12 ngày.\n\n- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Điều đó thật đáng báo động, Marcus. Các cơ sở lắp ráp trong nước của chúng ta đang vận hành theo mô hình tồn kho tinh gọn. Nếu các mô-đun bán dẫn không đến trước thứ Ba, dây chuyền sản xuất sẽ phải dừng hoạt động vô thời hạn.\n\n- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Chúng tôi đã lường trước nút thắt cổ chai này. Tôi đã kích hoạt các quy trình dự phòng với các hãng vận chuyển hàng không. Chúng ta có thể không vận 20 tấn chip quan trọng trực tiếp từ nhà máy chế tạo để ngăn chặn việc đóng cửa nhà máy.\n\n- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Giá cước hàng không hiện cao gấp 4 lần vận tải đường biển. Sự tăng vọt chi phí này sẽ ảnh hưởng thế nào đến biên lợi nhuận thu mua quý của chúng ta?\n\n- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Phí chênh lệch vận chuyển thực sự sẽ làm tăng chi phí hậu cần khoảng 80.000 USD. Tuy nhiên, các khoản phạt hợp đồng do ngừng giao hàng cho khách hàng sẽ vượt quá nửa triệu đô la.\n\n- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Khi so sánh với tiền bồi thường thiệt hại theo hợp đồng, khoản chi này hoàn toàn chính đáng. Còn các nguyên liệu thô số lượng lớn không khẩn cấp thì sao?\n\n- **Marcus (Nam / Giám đốc Vận tải Quốc tế):** Những chuyến hàng đó sẽ được chuyển hướng qua các tàu gom hàng phụ đến một bến cảng lân cận ít tắc nghẽn hơn và vận chuyển bằng đường bộ.\n\n- **Lin (Nữ / Giám đốc Thu mua Toàn cầu):** Quyết định tuyệt vời. Xin vui lòng phê duyệt các chuyến bay thuê chuyến ngay lập tức và cập nhật cho tôi mốc thời gian thông quan hải quan.",
        "keyVocab": [
            {
                "word": "freight forwarding syndicate",
                "ipa": "/freɪt ˈfɔːr.wɚ.dɪŋ ˈsɪn.dɪ.kət/",
                "meaning": "nghiệp đoàn/tập đoàn giao nhận vận tải"
            },
            {
                "word": "lean inventory model",
                "ipa": "/liːn ˈɪn.vən.tɔːri ˈmɑː.dəl/",
                "meaning": "mô hình quản lý kho tinh gọn"
            },
            {
                "word": "stave off",
                "ipa": "/steɪv ɔːf/",
                "meaning": "ngăn chặn tạm thời (khủng hoảng, đình trệ)"
            },
            {
                "word": "liquidated damages",
                "ipa": "/ˈlɪk.wə.deɪ.t̬ɪd ˈdæm.ɪ.dʒɪz/",
                "meaning": "tiền bồi thường thiệt hại ấn định trong hợp đồng"
            },
            {
                "word": "customs clearance",
                "ipa": "/ˈkʌs.təmz ˈklɪr.əns/",
                "meaning": "thủ tục thông quan hải quan"
            }
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
    {
        "id": "read-8",
        "title": "The Neurological Underpinnings of Bilingualism",
        "type": "passage",
        "topic": "Não bộ & Ngôn ngữ học",
        "level": "B2 - C1",
        "summary": "Nghiên cứu về cách bộ não đa ngôn ngữ định hình lại cấu trúc tế bào thần kinh, tăng cường khả năng kiểm soát điều hành và làm chậm sự khởi phát của chứng sa sút trí tuệ.",
        "content": "For centuries, educational dogma erroneously asserted that teaching children multiple languages simultaneously would burden immature cognitive faculties, precipitating linguistic confusion and developmental delays. Modern cognitive neuroscience has resoundingly refuted this misconception. Structural neuroimaging investigations demonstrate that managing multiple linguistic codes alters the brain's micro-architecture, fostering superior neural plasticity and reinforcing executive control networks housed within the dorsolateral prefrontal cortex.\n\nAt the core of the bilingual cognitive advantage is the relentless demand for attentional inhibition. In a bilingual brain, both linguistic systems remain perpetually active in parallel. When a bilingual speaker formulates an utterance, semantic concepts activate candidate representations in both tongues simultaneously. To articulate a coherent sentence without unwanted lexical intrusion, the brain's executive control system must actively suppress the competing, non-target language while amplifying the target vocabulary. This continuous mental workout strengthens domain-general inhibitory mechanisms, enabling bilingual individuals to excel in tasks demanding cognitive flexibility, selective attention, and rapid task-switching.\n\nFurthermore, the neuroprotective implications of sustained bilingualism are profound. Longitudinal epidemiological studies reveal that lifelong bilingual individuals manifest symptomatic onset of neurodegenerative disorders, such as Alzheimer's disease, approximately four to five years later than monolingual peers matched for socioeconomic background and education. While bilingualism does not shield neural tissue from microscopic tau tangles or amyloid plaques, it builds formidable \"cognitive reserve.\" The enriched synaptic connectivity provides alternative compensatory neural pathways, allowing individuals to maintain lucid everyday functioning despite underlying pathological degradation.\n\nUltimately, acquiring an additional language transcends communicative utility; it is a profound form of cognitive gymnastics. By compelling the brain to navigate competing linguistic frameworks continually, bilingualism endows individuals with resilient neural scaffolding that withstands cognitive wear throughout the human lifespan.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nTrong nhiều thế kỷ, giáo điều sư phạm đã khẳng định sai lầm rằng việc dạy trẻ em nhiều ngôn ngữ cùng lúc sẽ tạo gánh nặng cho năng lực nhận thức non nớt, gây ra sự nhầm lẫn ngôn ngữ và chậm phát triển. Khoa học thần kinh nhận thức hiện đại đã bác bỏ hoàn toàn quan niệm sai lầm này. Các cuộc điều tra hình ảnh thần kinh cấu trúc chứng minh rằng việc quản lý nhiều hệ thống ngôn ngữ làm thay đổi cấu trúc vi mô của não, thúc đẩy tính mềm dẻo thần kinh vượt trội và củng cố các mạng lưới kiểm soát điều hành nằm trong vỏ não trước trán lưng bên.\n\nCốt lõi của lợi thế nhận thức song ngữ là nhu cầu liên tục về sự ức chế chú ý. Trong bộ não song ngữ, cả hai hệ thống ngôn ngữ luôn duy trì hoạt động song song. Khi người nói song ngữ hình thành một phát ngôn, các khái niệm ngữ nghĩa sẽ kích hoạt các biểu diễn ứng viên ở cả hai ngôn ngữ cùng một lúc. Để nói ra một câu mạch lạc mà không bị xâm nhập từ vựng ngoài ý muốn, hệ thống kiểm soát điều hành của não phải chủ động ức chế ngôn ngữ cạnh tranh (không phải mục tiêu) trong khi khuếch đại từ vựng mục tiêu. Sự rèn luyện tinh thần liên tục này củng cố các cơ chế ức chế chung, giúp các cá nhân song ngữ vượt trội trong các nhiệm vụ đòi hỏi sự linh hoạt nhận thức, chú ý có chọn lọc và chuyển đổi nhiệm vụ nhanh chóng.\n\nHơn nữa, ý nghĩa bảo vệ thần kinh của việc sử dụng song ngữ lâu dài là vô cùng sâu sắc. Các nghiên cứu dịch tễ học theo chiều dọc cho thấy rằng những người song ngữ suốt đời biểu hiện các triệu chứng khởi phát của các rối loạn thoái hóa thần kinh, chẳng hạn như bệnh Alzheimer, muộn hơn khoảng 4 đến 5 năm so với những người đơn ngữ có cùng hoàn cảnh kinh tế xã hội và trình độ học vấn. Mặc dù song ngữ không che chở cho mô thần kinh khỏi các đám rối tau vi thể hoặc mảng amyloid, nhưng nó xây dựng nên một \"dự trữ nhận thức\" đáng gờm. Khả năng kết nối synap phong phú cung cấp các con đường thần kinh bù trừ thay thế, cho phép các cá nhân duy trì hoạt động hàng ngày minh mẫn bất chấp sự suy thoái bệnh lý tiềm ẩn.\n\nCuối cùng, việc tiếp thu thêm một ngôn ngữ vượt xa tiện ích giao tiếp thông thường; đó là một hình thức tập thể dục nhận thức sâu sắc. Bằng cách buộc não bộ liên tục điều hướng các khuôn khổ ngôn ngữ cạnh tranh, song ngữ ban tặng cho các cá nhân một giàn giáo thần kinh kiên cường, chống chọi lại sự hao mòn nhận thức trong suốt cuộc đời.",
        "keyVocab": [
            {
                "word": "educational dogma",
                "ipa": "/ˌedʒ.əˈkeɪ.ʃən.əl ˈdɑːɡ.mə/",
                "meaning": "giáo điều sư phạm cũ kỹ"
            },
            {
                "word": "attentional inhibition",
                "ipa": "/əˈten.ʃən.əl ˌɪn.həˈbɪʃ.ən/",
                "meaning": "sự ức chế chú ý (gạt bỏ thông tin nhiễu)"
            },
            {
                "word": "task-switching",
                "ipa": "/tæsk ˈswɪtʃ.ɪŋ/",
                "meaning": "khả năng chuyển đổi qua lại giữa các tác vụ"
            },
            {
                "word": "cognitive reserve",
                "ipa": "/ˈkɑːɡ.nə.t̬ɪv rɪˈzɜːrv/",
                "meaning": "dự trữ nhận thức chống đỡ thoái hóa não"
            },
            {
                "word": "compensatory pathway",
                "ipa": "/kəmˈpen.sə.tɔːr.i ˈpæθ.weɪ/",
                "meaning": "con đường thần kinh bù trừ thay thế"
            }
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
    {
        "id": "read-9",
        "title": "Quarterly Performance Appraisal & Salary Review",
        "type": "conversation",
        "topic": "Nhân sự & Phát triển sự nghiệp",
        "level": "B2 - C1",
        "summary": "Buổi đánh giá hiệu suất công việc và đàm phán thăng tiến giữa Trưởng phòng Kỹ thuật và Nữ Chuyên gia Khoa học Dữ liệu cấp cao.",
        "content": [
            {
                "speaker": "Richard (Male / Department Head)",
                "text": "Chloe, thank you for coming in. Your self-evaluation submitted last Friday was exceptionally thorough. I want to formally review your contributions to our Q3 data engineering initiatives."
            },
            {
                "speaker": "Chloe (Female / Senior Data Scientist)",
                "text": "Thank you, Richard. Over the past nine months, I concentrated primarily on overhauling our customer churn prediction architecture and reducing algorithm training latency."
            },
            {
                "speaker": "Richard (Male / Department Head)",
                "text": "The executive committee took note. Your predictive churn model yielded an eight percent boost in customer retention, translating directly into nearly three million dollars in recurring annual revenue."
            },
            {
                "speaker": "Chloe (Female / Senior Data Scientist)",
                "text": "I'm delighted by those outcomes. Beyond model accuracy, I also mentored two junior analysts and established rigorous documentation standards across our code repositories."
            },
            {
                "speaker": "Richard (Male / Department Head)",
                "text": "Your leadership maturity has been evident. Therefore, management is enthusiastically recommending your promotion to Lead Machine Learning Architect."
            },
            {
                "speaker": "Chloe (Female / Senior Data Scientist)",
                "text": "I truly appreciate that recognition. In conjunction with this expanded architectural scope, I would like to discuss compensation alignment. Based on current industry benchmarks for lead roles, I am seeking a twelve percent base salary adjustment."
            },
            {
                "speaker": "Richard (Male / Department Head)",
                "text": "Given standard corporate compensation bands, a twelve percent immediate jump in base salary requires executive sign-off. However, I can offer an eight percent base increase immediately, paired with a higher tranche of performance-based equity options."
            },
            {
                "speaker": "Chloe (Female / Senior Data Scientist)",
                "text": "That package demonstrates strong alignment with long-term company valuation. If we can incorporate a performance bonus tied to Q1 model deployment milestones, I would gladly accept."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Richard (Nam / Trưởng phòng Kỹ thuật):** Chloe, cảm ơn cô đã đến. Bản tự đánh giá cô nộp thứ Sáu tuần trước rất kỹ lưỡng. Tôi muốn chính thức xem xét những đóng góp của cô cho các sáng kiến kỹ thuật dữ liệu quý 3 của chúng ta.\n\n- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Cảm ơn Richard. Trong 9 tháng qua, tôi tập trung chủ yếu vào việc đại tu kiến trúc dự đoán tỷ lệ khách hàng rời bỏ và giảm độ trễ huấn luyện thuật toán.\n\n- **Richard (Nam / Trưởng phòng Kỹ thuật):** Ban điều hành đã ghi nhận điều đó. Mô hình dự đoán khách hàng rời bỏ của cô đã mang lại mức tăng 8% trong việc giữ chân khách hàng, trực tiếp chuyển hóa thành gần 3 triệu đô la doanh thu định kỳ hàng năm.\n\n- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Tôi rất vui mừng về những kết quả đó. Ngoài độ chính xác của mô hình, tôi cũng đã hướng dẫn 2 nhà phân tích cấp dưới và thiết lập các tiêu chuẩn tài liệu nghiêm ngặt trên toàn bộ kho mã nguồn.\n\n- **Richard (Nam / Trưởng phòng Kỹ thuật):** Sự trưởng thành trong vai trò lãnh đạo của cô rất rõ rệt. Vì vậy, ban quản lý nhiệt liệt đề xuất thăng chức cho cô lên vị trí Kiến trúc sư Trưởng Học máy (Lead ML Architect).\n\n- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Tôi thực sự đánh giá cao sự công nhận đó. Đi đôi với phạm vi kiến trúc mở rộng này, tôi muốn thảo luận về việc điều chỉnh mức đãi ngộ. Dựa trên các tiêu chuẩn ngành hiện tại cho các vai trò trưởng nhóm, tôi mong muốn mức điều chỉnh lương cơ bản là 12%.\n\n- **Richard (Nam / Trưởng phòng Kỹ thuật):** Với khung lương tiêu chuẩn của công ty, mức tăng ngay 12% lương cơ bản cần sự phê duyệt của ban điều hành. Tuy nhiên, tôi có thể đề xuất mức tăng 8% lương cơ bản ngay lập tức, kết hợp với một đợt phân bổ quyền chọn cổ phiếu hiệu suất cao hơn.\n\n- **Chloe (Nữ / Chuyên gia Khoa học Dữ liệu cấp cao):** Gói đãi ngộ đó thể hiện sự gắn kết chặt chẽ với giá trị dài hạn của công ty. Nếu chúng ta có thể kết hợp thêm khoản thưởng hiệu suất gắn với các cột mốc triển khai mô hình quý 1, tôi rất sẵn lòng đồng ý.",
        "keyVocab": [
            {
                "word": "performance appraisal",
                "ipa": "/pɚˈfɔːr.məns əˈpreɪ.zəl/",
                "meaning": "đánh giá hiệu suất công việc định kỳ"
            },
            {
                "word": "churn prediction",
                "ipa": "/tʃɜːrn prɪˈdɪk.ʃən/",
                "meaning": "dự đoán tỷ lệ khách hàng rời bỏ dịch vụ"
            },
            {
                "word": "recurring revenue",
                "ipa": "/rɪˈkɝː.ɪŋ ˈrev.ə.nuː/",
                "meaning": "doanh thu định kỳ lặp lại"
            },
            {
                "word": "compensation band",
                "ipa": "/ˌkɑːm.penˈseɪ.ʃən bænd/",
                "meaning": "khung bậc lương và đãi ngộ chuẩn"
            },
            {
                "word": "equity options",
                "ipa": "/ˈek.wə.t̬i ˈɑːp.ʃənz/",
                "meaning": "quyền chọn cổ phần doanh nghiệp"
            }
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
    {
        "id": "read-10",
        "title": "Decentralized Finance and Sovereign Monetary Policy",
        "type": "passage",
        "topic": "Tài chính & Tiền tệ",
        "level": "B2 - C1",
        "summary": "Bài phân tích về sự trỗi dậy của tài chính phi tập trung (DeFi), hợp đồng thông minh và tác động đối với chính sách tiền tệ của các ngân hàng trung ương.",
        "content": "The emergence of decentralized finance (DeFi) represents a philosophical and technological assault on the foundational architecture of contemporary commercial banking. For over three centuries, sovereign nation-states preserved an unchallenged monopoly over monetary issuance, financial intermediation, and interest rate governance. Central banks exercised macroeconomic equilibrium by adjusting reserve requirements and managing discount window liquidity. However, open-source blockchain architectures are substituting institutional trust with mathematical cryptographic consensus.\n\nAt the operational core of decentralized finance lie smart contracts—self-executing lines of code stored on immutable distributed ledgers. In traditional capital markets, securing a commercial loan necessitates extensive underwriting, credit score verification, legal notarization, and substantial bureaucratic overhead. DeFi liquidity protocols dismantle these intermediaries. By depositing digital collateral into algorithmic automated liquidity pools, borrowers can instantly draw syndicated loans governed purely by predetermined loan-to-value ratios without human authorization.\n\nNevertheless, this algorithmic disintermediation poses severe systemic risks. While traditional banking systems feature deposit insurance safeguards and central bank lenders of last resort, DeFi ecosystems are acutely vulnerable to cascading liquidation cascades. When underlying collateral assets experience sudden market devaluation, algorithmic liquidation bots aggressively trigger automated asset dumping, depressing token valuations and generating systemic insolvency across interconnected protocols. Furthermore, the anonymity afforded by pseudo-anonymous cryptographic wallets complicates sovereign efforts to combat international capital flight and cross-border tax evasion.\n\nConsequently, central monetary authorities worldwide are accelerating initiatives to introduce Central Bank Digital Currencies (CBDCs). By synthesizing the transactional speed and programmability of blockchain tokens with the legal backing and stability of sovereign fiat currency, governments seek to neutralize DeFi's disruptive encroachment. The brewing confrontation between decentralized sovereign-free capital and state-administered programmable digital fiat will fundamentally redefine global financial governance for decades to come.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nSự xuất hiện của tài chính phi tập trung (DeFi) đại diện cho một cuộc công kích triết học và công nghệ vào kiến trúc nền tảng của ngân hàng thương mại đương đại. Trong hơn 3 thế kỷ, các quốc gia có chủ quyền đã duy trì thế độc quyền không thể tranh cãi đối với việc phát hành tiền tệ, trung gian tài chính và quản trị lãi suất. Các ngân hàng trung ương thực thi trạng thái cân bằng kinh tế vĩ mô bằng cách điều chỉnh các yêu cầu dự trữ và quản lý thanh khoản cửa sổ chiết khấu. Tuy nhiên, các kiến trúc chuỗi khối nguồn mở đang thay thế niềm tin thể chế bằng sự đồng thuận mật mã toán học.\n\nCốt lõi hoạt động của tài chính phi tập trung là các hợp đồng thông minh—những dòng mã tự thực thi được lưu trữ trên các sổ cái phân tán bất biến. Trong các thị trường vốn truyền thống, việc đảm bảo một khoản vay thương mại đòi hỏi sự bảo lãnh phát hành sâu rộng, xác minh điểm tín dụng, công chứng pháp lý và chi phí hành chính đáng kể. Các giao thức thanh khoản DeFi tháo dỡ các bên trung gian này. Bằng cách gửi tài sản thế chấp kỹ thuật số vào các quỹ thanh khoản tự động theo thuật toán, người đi vay có thể vay ngay các khoản vay hợp vốn được quản lý hoàn toàn bằng tỷ lệ khoản vay trên giá trị (LTV) định trước mà không cần sự phê duyệt của con người.\n\nTuy nhiên, sự phi trung gian hóa theo thuật toán này gây ra những rủi ro mang tính hệ thống nghiêm trọng. Trong khi các hệ thống ngân hàng truyền thống có các biện pháp bảo vệ bảo hiểm tiền gửi và người cho vay cuối cùng của ngân hàng trung ương, các hệ sinh thái DeFi rất dễ bị tổn thương trước các đợt thanh lý xếp tầng liên hoàn. Khi các tài sản thế chấp tiềm ẩn bị mất giá đột ngột, các bot thanh lý thuật toán sẽ kích hoạt bán tháo tài sản một cách quyết liệt, làm sụt giảm định giá và gây ra tình trạng mất khả năng thanh toán mang tính hệ thống trên các giao thức kết nối với nhau. Hơn nữa, tính ẩn danh của các ví mật mã làm phức tạp các nỗ lực của quốc gia nhằm chống lại dòng vốn tháo chạy quốc tế và trốn thuế xuyên biên giới.\n\nDo đó, các cơ quan quản lý tiền tệ trung ương trên toàn thế giới đang đẩy nhanh các sáng kiến giới thiệu Tiền kỹ thuật số của Ngân hàng Trung ương (CBDC). Bằng cách tổng hợp tốc độ giao dịch và khả năng lập trình của các mã thông báo chuỗi khối với sự bảo đảm pháp lý và tính ổn định của tiền pháp định có chủ quyền, các chính phủ tìm cách vô hiệu hóa sự lấn sân đột phá của DeFi. Cuộc đối đầu đang hình thành giữa dòng vốn phi tập trung không có chủ quyền và tiền pháp định kỹ thuật số có thể lập trình do nhà nước quản lý sẽ định nghĩa lại cơ bản nền quản trị tài chính toàn cầu trong nhiều thập kỷ tới.",
        "keyVocab": [
            {
                "word": "financial intermediation",
                "ipa": "/faɪˈnæn.ʃəl ˌɪn.t̬ɚˌmiː.diˈeɪ.ʃən/",
                "meaning": "sự trung gian tài chính (ngân hàng làm trung gian)"
            },
            {
                "word": "immutable ledger",
                "ipa": "/ɪˈmjuː.t̬ə.bəl ˈledʒ.ɚ/",
                "meaning": "sổ cái bất biến không thể sửa xóa"
            },
            {
                "word": "liquidation cascade",
                "ipa": "/ˌlɪk.wəˈdeɪ.ʃən kæsˈkeɪd/",
                "meaning": "làn sóng thanh lý tài sản thế chấp dây chuyền"
            },
            {
                "word": "lender of last resort",
                "ipa": "/ˈlen.dɚ əv læst rɪˈzɔːrt/",
                "meaning": "người cho vay cứu cánh cuối cùng (Ngân hàng Trung ương)"
            },
            {
                "word": "sovereign fiat currency",
                "ipa": "/ˈsɑːv.rən ˈfiː.æt ˈkɝː.ən.si/",
                "meaning": "tiền pháp định có chủ quyền quốc gia"
            }
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
    {
        "id": "read-11",
        "title": "Startup Pitch & Angel Investor Interrogation",
        "type": "conversation",
        "topic": "Khởi nghiệp & Gọi vốn",
        "level": "B2 - C1",
        "summary": "Phiên thẩm định đầu tư hạt giống giữa Nhà đầu tư thiên thần và Nữ sáng lập công ty công nghệ sinh học.",
        "content": [
            {
                "speaker": "Julian (Male / Angel Investor)",
                "text": "Olivia, your investor deck for SynthoBio is certainly compelling. However, pitching a three-million-dollar pre-money valuation at the pre-revenue stage requires extraordinary justification."
            },
            {
                "speaker": "Olivia (Female / Biotech Startup Founder)",
                "text": "I appreciate your scrutiny, Julian. While we have not commercialized yet, we hold two broad provisional patents on our enzymatic carbon-capture biopolymer. Our bench-scale prototypes achieve ninety-two percent synthesis efficiency."
            },
            {
                "speaker": "Julian (Male / Angel Investor)",
                "text": "Lab bench efficiency rarely scales linearly to pilot industrial manufacturing. What is your current monthly burn rate, and what runway does this seed financing provide?"
            },
            {
                "speaker": "Olivia (Female / Biotech Startup Founder)",
                "text": "Our current burn rate is forty-five thousand dollars monthly, primarily allocated to analytical chemistry equipment and two PhD research salaries. Securing five hundred thousand dollars guarantees an eighteen-month runway to reach bioreactor pilot scale."
            },
            {
                "speaker": "Julian (Male / Angel Investor)",
                "text": "What about your regulatory clearance pathway? Environmental safety agencies scrutinize novel synthetic polymers aggressively before approving commercial packaging."
            },
            {
                "speaker": "Olivia (Female / Biotech Startup Founder)",
                "text": "We designed the polymer backbone strictly from GRAS—Generally Recognized As Safe—organic feedstocks. Pre-submission toxicity assays indicate zero microplastic residue, which substantially expedites our compliance trajectory."
            },
            {
                "speaker": "Julian (Male / Angel Investor)",
                "text": "That addresses my primary bio-hazard concern. What terms are you willing to accept on a SAFE note regarding valuation caps and discounts?"
            },
            {
                "speaker": "Olivia (Female / Biotech Startup Founder)",
                "text": "We are offering a standard post-money SAFE with a four-million-dollar valuation cap and a twenty percent conversion discount for our lead investor."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Julian (Nam / Nhà đầu tư thiên thần):** Olivia, hồ sơ thuyết trình đầu tư cho SynthoBio của cô chắc chắn rất hấp dẫn. Tuy nhiên, việc đưa ra mức định giá 3 triệu đô la trước khi có doanh thu đòi hỏi sự biện minh phi thường.\n\n- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Tôi đánh giá cao sự xem xét kỹ lưỡng của anh, Julian. Mặc dù chúng tôi chưa thương mại hóa, nhưng chúng tôi nắm giữ 2 bằng sáng chế tạm thời đối với polyme sinh học thu giữ carbon bằng enzyme. Các mẫu thử nghiệm quy mô phòng thí nghiệm của chúng tôi đạt hiệu suất tổng hợp 92%.\n\n- **Julian (Nam / Nhà đầu tư thiên thần):** Hiệu suất trong phòng thí nghiệm hiếm khi mở rộng tuyến tính lên sản xuất công nghiệp thử nghiệm. Tốc độ đốt tiền (burn rate) hàng tháng hiện tại của cô là bao nhiêu, và vòng tài trợ hạt giống này mang lại thời gian hoạt động (runway) bao lâu?\n\n- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Tốc độ đốt tiền hiện tại của chúng tôi là 45.000 đô la hàng tháng, chủ yếu phân bổ cho thiết bị hóa phân tích và lương của 2 tiến sĩ nghiên cứu. Việc huy động được 500.000 đô la đảm bảo thời gian hoạt động 18 tháng để đạt quy mô thử nghiệm lò phản ứng sinh học.\n\n- **Julian (Nam / Nhà đầu tư thiên thần):** Còn lộ trình phê duyệt theo quy định thì sao? Các cơ quan an toàn môi trường giám sát rất gắt gao các polyme tổng hợp mới trước khi phê duyệt bao bì thương mại.\n\n- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Chúng tôi đã thiết kế khung polyme hoàn toàn từ nguyên liệu hữu cơ đạt chuẩn GRAS (Được công nhận là an toàn). Các xét nghiệm độc tính trước khi nộp hồ sơ cho thấy không có cặn vi nhựa, điều này giúp đẩy nhanh đáng kể lộ trình tuân thủ của chúng tôi.\n\n- **Julian (Nam / Nhà đầu tư thiên thần):** Điều đó giải quyết mối lo ngại hàng đầu của tôi về rủi ro sinh học. Cô sẵn sàng chấp nhận các điều khoản nào trên hợp đồng SAFE về mức trần định giá và tỷ lệ chiết khấu?\n\n- **Olivia (Nữ / Sáng lập Khởi nghiệp Công nghệ sinh học):** Chúng tôi đưa ra thỏa thuận SAFE sau đầu tư tiêu chuẩn với mức trần định giá 4 triệu đô la và chiết khấu chuyển đổi 20% cho nhà đầu tư dẫn dắt.",
        "keyVocab": [
            {
                "word": "pre-money valuation",
                "ipa": "/priː ˈmʌn.i ˌvæl.juˈeɪ.ʃən/",
                "meaning": "định giá doanh nghiệp trước khi nhận vốn"
            },
            {
                "word": "burn rate",
                "ipa": "/bɜːrn reɪt/",
                "meaning": "tốc độ tiêu tiền vốn hàng tháng của startup"
            },
            {
                "word": "runway",
                "ipa": "/ˈrʌn.weɪ/",
                "meaning": "thời gian startup có thể duy trì hoạt động trước khi cạn tiền"
            },
            {
                "word": "GRAS feedstock",
                "ipa": "/ɡræs ˈfiːd.stɑːk/",
                "meaning": "nguyên liệu được công nhận an toàn tuyệt đối"
            },
            {
                "word": "valuation cap",
                "ipa": "/ˌvæl.juˈeɪ.ʃən kæp/",
                "meaning": "mức trần định giá trong thỏa thuận đầu tư SAFE"
            }
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
    {
        "id": "read-12",
        "title": "The Ethics of Genetic Engineering & CRISPR Therapeutics",
        "type": "passage",
        "topic": "Y sinh & Đạo đức sinh học",
        "level": "B2 - C1",
        "summary": "Phân tích tiềm năng điều trị bệnh hiểm nghèo bằng công nghệ chỉnh sửa gen CRISPR và lằn ranh đạo đức trong can thiệp dòng mầm di truyền.",
        "content": "The advent of CRISPR-Cas9 genome editing represents a quantum leap in molecular biology, shifting medical science from symptom management to direct hereditary intervention. Originally deciphered as an adaptive immune mechanism in bacterial organisms against bacteriophage viruses, this enzymatic tool enables scientists to introduce double-stranded DNA breaks at precise nucleotide coordinates with unprecedented fidelity. Monogenic diseases that have tormented humanity for millennia—including sickle-cell anemia, cystic fibrosis, and Huntington's chorea—are transitioning from fatal prognoses into potentially curable conditions.\n\nClinical trials have already demonstrated spectacular somatic cell therapies. By harvesting hematopoietic stem cells from patients afflicted with sickle-cell disease, excising the defective hemoglobin gene ex vivo, and re-infusing the edited cells into bone marrow, clinicians have successfully restored normal red blood cell morphology without provoking immune rejection. Because somatic edits are confined strictly to differentiated bodily tissues, they vanish upon the patient's death and are never transmitted to subsequent generations.\n\nConversely, germline gene editing—the genetic modification of human embryos, sperm, or oocytes—propels humanity into precarious bioethical territory. In germline interventions, artificial alterations become permanent, heritable fixtures of the human gene pool. Proponents argue that germline editing offers the ultimate compassionate opportunity to eradicate devastating genetic pathologies from familial lineages forever. However, bioethicists warn against off-target mutagenesis, where the Cas9 enzyme inadvertently cleaves non-targeted genomic sequences, potentially introducing catastrophic oncogenic mutations that propagate down generations.\n\nBeyond biophysical safety, the prospect of germline enhancement invokes chilling sociological perils. If gene editing transitions from curative medicine to elective cosmetic and cognitive enhancement, wealthy elites could purchase biological advantages for their progeny. Such commercialization risks inaugurating a neo-eugenic caste system, cementing socio-economic inequality into immutable biological destiny. Therefore, the global scientific community firmly demands strict regulatory moratoria until safety thresholds and universal democratic consensus are unequivocally established.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nSự ra đời của công cụ chỉnh sửa bộ gen CRISPR-Cas9 đại diện cho một bước nhảy vọt lượng tử trong sinh học phân tử, chuyển khoa học y tế từ việc quản lý triệu chứng sang can thiệp di truyền trực tiếp. Ban đầu được giải mã như một cơ chế miễn dịch thích ứng ở vi khuẩn chống lại virus thực khuẩn thể, công cụ enzyme này cho phép các nhà khoa học tạo ra các vết cắt DNA chuỗi kép tại các tọa độ nucleotide chính xác với độ trung thực chưa từng có. Các bệnh đơn gen từng hành hạ nhân loại hàng thiên niên kỷ—bao gồm thiếu máu hồng cầu hình liềm, xơ nang và bệnh múa giật Huntington—đang chuyển đổi từ tiên lượng tử vong sang các tình trạng có khả năng chữa khỏi.\n\nCác thử nghiệm lâm sàng đã chứng minh các liệu pháp tế bào soma ngoạn mục. Bằng cách thu hoạch các tế bào gốc tạo máu từ những bệnh nhân mắc bệnh hồng cầu hình liềm, cắt bỏ gen hemoglobin bị lỗi ngoài cơ thể (ex vivo) và truyền lại các tế bào đã chỉnh sửa vào tủy xương, các bác sĩ lâm sàng đã khôi phục thành công hình thái hồng cầu bình thường mà không gây ra phản ứng đào thải miễn dịch. Bởi vì các chỉnh sửa soma chỉ giới hạn nghiêm ngặt ở các mô cơ thể biệt hóa, chúng sẽ biến mất khi bệnh nhân qua đời và không bao giờ được truyền sang các thế hệ sau.\n\nNgược lại, việc chỉnh sửa gen dòng mầm—sự biến đổi gen của phôi người, tinh trùng hoặc tế bào trứng—đưa nhân loại vào lãnh địa đạo đức sinh học bấp bênh. Trong các can thiệp dòng mầm, các thay đổi nhân tạo trở thành những đặc điểm di truyền vĩnh viễn trong vốn gen của con người. Những người ủng hộ lập luận rằng chỉnh sửa dòng mầm mang lại cơ hội nhân đạo tối thượng để xóa bỏ vĩnh viễn các bệnh lý di truyền tàn khốc khỏi các dòng họ. Tuy nhiên, các nhà đạo đức sinh học cảnh báo về sự đột biến lệch mục tiêu (off-target mutagenesis), nơi enzyme Cas9 vô tình cắt các chuỗi gen ngoài mục tiêu, có khả năng gây ra các đột biến gây ung thư thảm khốc truyền qua các thế hệ.\n\nVượt ra ngoài sự an toàn sinh lý học, viễn cảnh tăng cường gen dòng mầm gợi lên những mối nguy hiểm xã hội học đáng sợ. Nếu chỉnh sửa gen chuyển từ y học chữa bệnh sang nâng cấp thẩm mỹ và nhận thức tự chọn, giới tinh hoa giàu có có thể mua các lợi thế sinh học cho con cháu của họ. Việc thương mại hóa như vậy có nguy cơ mở ra một hệ thống đẳng cấp ưu sinh học mới, khắc sâu sự bất bình đẳng kinh tế xã hội thành số phận sinh học bất biến. Do đó, cộng đồng khoa học toàn cầu kiên quyết yêu cầu các lệnh tạm ngừng theo quy định nghiêm ngặt cho đến khi các ngưỡng an toàn và sự đồng thuận dân chủ phổ quát được thiết lập một cách rõ ràng.",
        "keyVocab": [
            {
                "word": "quantum leap",
                "ipa": "/ˌkwɑːn.təm ˈliːp/",
                "meaning": "bước nhảy vọt vĩ đại"
            },
            {
                "word": "monogenic disease",
                "ipa": "/ˌmɑː.nəˈdʒen.ɪk dɪˈziːz/",
                "meaning": "bệnh do đột biến một gen đơn lẻ"
            },
            {
                "word": "somatic cell therapy",
                "ipa": "/soʊˈmæt̬.ɪk sel ˈθer.ə.pi/",
                "meaning": "liệu pháp tế bào soma (không di truyền sang đời sau)"
            },
            {
                "word": "germline editing",
                "ipa": "/ˈdʒɝːm.laɪn ˈed.ɪ.tɪŋ/",
                "meaning": "chỉnh sửa gen dòng mầm (di truyền sang các thế hệ sau)"
            },
            {
                "word": "off-target mutagenesis",
                "ipa": "/ɔːf ˈtɑːr.ɡɪt ˌmjuː.t̬əˈdʒen.ə.sɪs/",
                "meaning": "sự gây đột biến ngoài vị trí mục tiêu"
            }
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
    {
        "id": "read-13",
        "title": "Crisis Management: Data Breach & PR Response",
        "type": "conversation",
        "topic": "An ninh mạng & Xử lý khủng hoảng",
        "level": "B2 - C1",
        "summary": "Cuộc họp ứng phó khẩn cấp giữa Giám đốc An ninh Thông tin và Nữ Trưởng phòng Quan hệ Công chúng khi hệ thống dữ liệu khách hàng bị tấn công mạng.",
        "content": [
            {
                "speaker": "Alex (Male / Chief Information Security Officer)",
                "text": "Victoria, thank you for rushing down. At 03:00 UTC, our automated intrusion detection system caught unauthorized exfiltration traffic originating from our European customer database shard."
            },
            {
                "speaker": "Victoria (Female / Head of Public Relations)",
                "text": "Good heavens, Alex. How extensive is the blast radius? Were customer credentials or unencrypted financial records compromised?"
            },
            {
                "speaker": "Alex (Male / Chief Information Security Officer)",
                "text": "The threat actors exploited a zero-day vulnerability in a third-party caching plugin. Approximately two hundred thousand customer profile records were accessed, including salted hashed passwords and email addresses, but our payment tokens remain strictly encrypted."
            },
            {
                "speaker": "Victoria (Female / Head of Public Relations)",
                "text": "Under GDPR regulations, we face a statutory seventy-two-hour window to report this incident to data protection authorities. When will our containment protocol be complete?"
            },
            {
                "speaker": "Alex (Male / Chief Information Security Officer)",
                "text": "My incident response team has already isolated the compromised cluster, revoked all API tokens, and patched the caching vulnerability. Forensic log analysis is eighty percent complete."
            },
            {
                "speaker": "Victoria (Female / Head of Public Relations)",
                "text": "That enables us to maintain an offensive communication posture. If we proactively notify affected users before investigative journalists break the story, we preserve brand credibility."
            },
            {
                "speaker": "Alex (Male / Chief Information Security Officer)",
                "text": "I agree completely. We should also enforce a mandatory password reset for all impacted accounts upon their next login session."
            },
            {
                "speaker": "Victoria (Female / Head of Public Relations)",
                "text": "I will draft the transparent public advisory immediately, emphasizing our swift mitigation and offering complimentary credit monitoring services for affected users."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Alex (Nam / Giám đốc An ninh Thông tin):** Victoria, cảm ơn cô đã đến gấp. Vào lúc 03:00 UTC, hệ thống phát hiện xâm nhập tự động của chúng ta đã phát hiện lưu lượng trích xuất trái phép bắt nguồn từ phân vùng cơ sở dữ liệu khách hàng châu Âu.\n\n- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Trời ơi, Alex. Bán kính ảnh hưởng rộng đến mức nào? Thông tin đăng nhập của khách hàng hoặc hồ sơ tài chính không được mã hóa có bị xâm phạm không?\n\n- **Alex (Nam / Giám đốc An ninh Thông tin):** Các tác nhân đe dọa đã khai thác lỗ hổng zero-day trong một plugin bộ đệm của bên thứ ba. Khoảng 200.000 hồ sơ khách hàng đã bị truy cập, bao gồm mật khẩu đã băm và địa chỉ email, nhưng các mã thanh toán vẫn được mã hóa nghiêm ngặt.\n\n- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Theo quy định GDPR, chúng ta có khung thời gian luật định 72 giờ để báo cáo sự cố này cho các cơ quan bảo vệ dữ liệu. Khi nào giao thức khoanh vùng của bên anh hoàn tất?\n\n- **Alex (Nam / Giám đốc An ninh Thông tin):** Đội phản ứng sự cố của tôi đã cô lập cụm máy chủ bị xâm phạm, thu hồi tất cả mã khóa API và vá lỗ hổng bộ đệm. Phân tích nhật ký điều tra đã hoàn tất 80%.\n\n- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Điều đó cho phép chúng ta duy trì thế chủ động trong truyền thông. Nếu chúng ta chủ động thông báo cho những người dùng bị ảnh hưởng trước khi các nhà báo điều tra đưa tin, chúng ta sẽ bảo vệ được uy tín thương hiệu.\n\n- **Alex (Nam / Giám đốc An ninh Thông tin):** Tôi hoàn toàn đồng ý. Chúng ta cũng nên thực thi việc đặt lại mật khẩu bắt buộc cho tất cả các tài khoản bị ảnh hưởng trong phiên đăng nhập tiếp theo.\n\n- **Victoria (Nữ / Trưởng phòng Quan hệ Công chúng):** Tôi sẽ soạn thông báo công khai minh bạch ngay lập tức, nhấn mạnh khả năng giảm thiểu thiệt hại nhanh chóng của chúng ta và cung cấp dịch vụ giám sát tín dụng miễn phí cho người dùng bị ảnh hưởng.",
        "keyVocab": [
            {
                "word": "intrusion detection system",
                "ipa": "/ɪnˈtruː.ʒən dɪˈtek.ʃən ˈsɪs.təm/",
                "meaning": "hệ thống phát hiện xâm nhập mạng (IDS)"
            },
            {
                "word": "blast radius",
                "ipa": "/blæst ˈreɪ.di.əs/",
                "meaning": "phạm vi/bán kính ảnh hưởng của sự cố"
            },
            {
                "word": "zero-day vulnerability",
                "ipa": "/ˌzɪr.oʊ deɪ ˌvʌl.nɚ.əˈbɪl.ə.t̬i/",
                "meaning": "lỗ hổng bảo mật chưa có bản vá"
            },
            {
                "word": "statutory window",
                "ipa": "/ˈstætʃ.ə.tɔːr.i ˈwɪn.doʊ/",
                "meaning": "thời hạn bắt buộc theo luật định"
            },
            {
                "word": "mitigation",
                "ipa": "/ˌmɪt̬.əˈɡeɪ.ʃən/",
                "meaning": "sự giảm thiểu tổn thất/tác hại"
            }
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
    {
        "id": "read-14",
        "title": "The Economics of Renewable Transition and Grid Modernization",
        "type": "passage",
        "topic": "Năng lượng & Biến đổi khí hậu",
        "level": "B2 - C1",
        "summary": "Đoạn văn khảo sát tính kinh tế của việc dịch chuyển sang năng lượng tái tạo, rào cản lưu trữ pin và nhu cầu hiện đại hóa hạ tầng lưới điện.",
        "content": "The global energy sector is traversing an unprecedented structural transition as the levelized cost of energy (LCOE) for solar photovoltaics and onshore wind continues its precipitous descent. Across multiple geopolitical territories, renewable generation has achieved unsubsidized grid parity, outcompeting traditional thermal coal and combined-cycle gas plants on marginal generation costs alone. Yet, celebratory declarations of a friction-free clean energy revolution overlook an obstinate physical impediment: the fundamental inadequacy of legacy transmission grids.\n\nTwentieth-century electrical grids were engineered around centralized, dispatchable generation. Fossil-fuel and nuclear facilities generated steady baseload power that flowed unidirectionally through high-voltage corridors to regional demand centers. In contrast, wind and solar assets are intrinsically intermittent and geographically dispersed, frequently situated in remote plains or offshore shoals far removed from metropolitan consumption hubs. When weather conditions precipitate sudden surges in generation, antiquated regional transmission lines become congested, compelling grid operators to mandate costly \"curtailment\"—the deliberate discarding of zero-carbon clean electricity.\n\nResolving this structural mismatch requires enormous capital deployment toward two complementary domains: utility-scale energy storage and high-voltage direct current (HVDC) transmission superhighways. While lithium-iron-phosphate battery packs excel at short-duration frequency regulation and four-hour evening peak shaving, they remain economically unviable for multi-day seasonal lulls. Long-duration energy storage alternatives—such as vanadium redox flow batteries, pumped-storage hydroelectric facilities, and green hydrogen electrolysis—are essential to ensure winter baseload reliability.\n\nSimultaneously, deploying continental HVDC corridors enables grid operators to balance weather variability across thousands of kilometers. When overcast skies suppress solar harvesting in Western Europe, surplus wind energy from North Sea offshore turbines can be channeled instantaneously across borders to sustain industrial operations. Ultimately, decarbonization is not merely a contest of building solar arrays; it is an epochal civil engineering campaign to rebuild the continental nervous system of electric power.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nNgành năng lượng toàn cầu đang trải qua một quá trình chuyển đổi cơ cấu chưa từng có khi chi phí quy dẫn của năng lượng (LCOE) cho điện mặt trời và điện gió trên bờ tiếp tục giảm mạnh. Trên nhiều vùng lãnh thổ địa chính trị, sản lượng điện tái tạo đã đạt mức ngang bằng lưới điện mà không cần trợ cấp, vượt trội so với các nhà máy nhiệt điện than truyền thống và tuabin khí chu trình hỗn hợp chỉ tính riêng về chi phí phát điện biên. Tuy nhiên, những tuyên bố ăn mừng về một cuộc cách mạng năng lượng sạch không ma sát đã bỏ qua một trở ngại vật lý ngoan cố: sự không thỏa đáng cơ bản của các lưới điện truyền tải cũ kỹ.\n\nLưới điện của thế kỷ 20 được thiết kế dựa trên các nguồn phát điện tập trung, có thể điều độ được. Các cơ sở nhiên liệu hóa thạch và hạt nhân tạo ra nguồn điện phụ tải đáy ổn định, chảy một chiều qua các hành lang điện áp cao đến các trung tâm phụ tải khu vực. Ngược lại, các tài sản gió và mặt trời vốn có tính chất gián đoạn và phân tán về mặt địa lý, thường nằm ở các vùng đồng bằng xa xôi hoặc bãi cạn ngoài khơi cách xa các trung tâm tiêu thụ đô thị. Khi điều kiện thời tiết tạo ra sự gia tăng đột biến về sản lượng điện, các đường dây truyền tải cũ trong khu vực bị tắc nghẽn, buộc các nhà vận hành lưới điện phải áp dụng biện pháp \"cắt giảm phát điện\" (curtailment) tốn kém—việc cố tình vứt bỏ lượng điện sạch không phát thải carbon.\n\nViệc giải quyết sự mất cân đối về cấu trúc này đòi hỏi phải triển khai vốn khổng lồ vào hai lĩnh vực bổ sung: lưu trữ năng lượng quy mô lưới điện và các siêu xa lộ truyền tải điện một chiều siêu cao áp (HVDC). Mặc dù các bộ pin lithium-iron-phosphate vượt trội trong việc điều chỉnh tần số thời lượng ngắn và cắt giảm phụ tải đỉnh buổi tối trong 4 giờ, nhưng chúng vẫn không khả thi về mặt kinh tế đối với sự sụt giảm phát điện theo mùa kéo dài nhiều ngày. Các giải pháp thay thế lưu trữ năng lượng thời lượng dài—chẳng hạn như pin dòng oxy hóa khử vanadium, các cơ sở thủy điện tích năng và điện phân hydro xanh—là cần thiết để đảm bảo độ tin cậy của phụ tải đáy mùa đông.\n\nĐồng thời, việc triển khai các hành lang HVDC xuyên lục địa cho phép các nhà điều hành lưới điện cân bằng sự biến động của thời tiết qua hàng nghìn km. Khi trời nhiều mây làm giảm khả năng thu năng lượng mặt trời ở Tây Âu, lượng điện gió dư thừa từ các tuabin ngoài khơi Biển Bắc có thể được dẫn ngay lập tức qua biên giới để duy trì các hoạt động công nghiệp. Cuối cùng, khử cacbon không chỉ đơn thuần là cuộc đua lắp đặt các tấm pin mặt trời; đó là một chiến dịch kỹ thuật dân dụng mang tính thời đại nhằm xây dựng lại hệ thống thần kinh lục địa của năng lượng điện.",
        "keyVocab": [
            {
                "word": "levelized cost of energy",
                "ipa": "/ˈlev.əl.aɪzd kɑːst əv ˈen.ɚ.dʒi/",
                "meaning": "chi phí quy dẫn của năng lượng (LCOE)"
            },
            {
                "word": "grid parity",
                "ipa": "/ɡrɪd ˈper.ə.t̬i/",
                "meaning": "điểm cân bằng chi phí lưới điện không cần trợ cấp"
            },
            {
                "word": "curtailment",
                "ipa": "/kɚˈteɪl.mənt/",
                "meaning": "sự cắt giảm phát điện bắt buộc do quá tải lưới"
            },
            {
                "word": "peak shaving",
                "ipa": "/piːk ˈʃeɪ.vɪŋ/",
                "meaning": "cắt giảm phụ tải đỉnh giờ cao điểm"
            },
            {
                "word": "high-voltage direct current",
                "ipa": "/haɪ ˈvoʊl.tɪdʒ daɪˈrekt ˈkɝː.ənt/",
                "meaning": "truyền tải điện một chiều cao áp (HVDC)"
            }
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
    {
        "id": "read-15",
        "title": "Architectural Critique & Sustainable Building Design",
        "type": "conversation",
        "topic": "Kiến trúc & Bất động sản",
        "level": "B2 - C1",
        "summary": "Cuộc trao đổi chuyên môn giữa Kỹ sư Kết cấu Trưởng và Nữ Kiến trúc sư Trưởng về việc tối ưu hóa hiệu quả nhiệt và thông gió tự nhiên cho tòa tháp phức hợp.",
        "content": [
            {
                "speaker": "Ethan (Male / Chief Structural Engineer)",
                "text": "Sophia, I scrutinized your updated schematics for the Meridian Tower atrium. While the ninety-meter glass curtain wall creates breathtaking aesthetics, its thermal envelope will impose an immense load on our HVAC chillers during July."
            },
            {
                "speaker": "Sophia (Female / Lead Architect)",
                "text": "I anticipated that concern, Ethan. If you examine section D, we are not installing monolithic glazing. We specified electrochromic triple-pane glass integrated with motorized exterior ceramic louvers calibrated to solar azimuth angles."
            },
            {
                "speaker": "Ethan (Male / Chief Structural Engineer)",
                "text": "That definitely mitigates solar heat gain coefficients. What about structural deflection under wind turbulence? The cantilevered sky-bridge connecting the twin towers generates significant torsional stress."
            },
            {
                "speaker": "Sophia (Female / Lead Architect)",
                "text": "We worked with aerodynamic consultants to incorporate a tuned mass damper at level forty-two, alongside porous kinetic wind dampers that deflect cross-winds without stiffening the primary trusses excessively."
            },
            {
                "speaker": "Ethan (Male / Chief Structural Engineer)",
                "text": "That is an elegant structural compromise. Have you accounted for embodied carbon restrictions mandated by municipal zero-emission building codes?"
            },
            {
                "speaker": "Sophia (Female / Lead Architect)",
                "text": "Yes. We replaced forty percent of Portland cement in our foundation mix with pozzolanic volcanic ash and recycled blast furnace slag, which reduces our concrete embodied carbon by thirty-two percent."
            },
            {
                "speaker": "Ethan (Male / Chief Structural Engineer)",
                "text": "Remarkable. That keeps us well beneath municipal carbon thresholds while maintaining sixty-megapascal compressive strength."
            },
            {
                "speaker": "Sophia (Female / Lead Architect)",
                "text": "Let us finalize the load calculation dossier so we can submit the blueprint to the municipal building safety board before Friday's deadline."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Sophia, tôi đã xem xét kỹ các bản vẽ sơ đồ cập nhật của cô cho giếng trời Tòa tháp Meridian. Mặc dù bức tường kính cao 90 mét tạo ra tính thẩm mỹ ngoạn mục, nhưng lớp vỏ bọc nhiệt của nó sẽ gây tải trọng khổng lồ cho các máy làm lạnh HVAC của chúng ta vào tháng Bảy.\n\n- **Sophia (Nữ / Kiến trúc sư Trưởng):** Tôi đã lường trước mối lo ngại đó, Ethan. Nếu anh kiểm tra phần D, chúng tôi không lắp đặt kính nguyên khối thông thường. Chúng tôi đã chỉ định kính ba lớp điện sắc kết hợp với các thanh chắn gốm cơ giới bên ngoài được hiệu chuẩn theo góc phương vị mặt trời.\n\n- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Điều đó chắc chắn làm giảm hệ số hấp thụ nhiệt mặt trời. Còn độ võng kết cấu dưới tác động của nhiễu động gió thì sao? Cầu kính công-xôn nối hai tòa tháp tạo ra ứng suất xoắn đáng kể.\n\n- **Sophia (Nữ / Kiến trúc sư Trưởng):** Chúng tôi đã làm việc với các chuyên gia khí động học để kết hợp một thiết bị giảm chấn khối lượng điều chỉnh (tuned mass damper) ở tầng 42, cùng với các van điều tiết gió động học xốp giúp làm lệch hướng gió ngược mà không làm cứng các giàn chịu lực chính quá mức.\n\n- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Đó là một sự thỏa hiệp kết cấu thanh lịch. Cô đã tính đến các hạn chế về carbon tiềm ẩn theo quy định của các bộ luật xây dựng không phát thải của thành phố chưa?\n\n- **Sophia (Nữ / Kiến trúc sư Trưởng):** Rồi. Chúng tôi đã thay thế 40% xi măng Portland trong hỗn hợp móng bằng tro núi lửa pozzolanic và xỉ lò cao tái chế, giúp giảm 32% lượng carbon tiềm ẩn trong bê tông của chúng ta.\n\n- **Ethan (Nam / Kỹ sư Kết cấu Trưởng):** Thật đáng nể. Điều đó giúp chúng ta duy trì mức phát thải thấp hơn nhiều so với ngưỡng carbon của thành phố trong khi vẫn duy trì cường độ nén 60 megapascal.\n\n- **Sophia (Nữ / Kiến trúc sư Trưởng):** Chúng ta hãy hoàn thiện hồ sơ tính toán tải trọng để có thể nộp bản thiết kế lên hội đồng an toàn xây dựng thành phố trước hạn chót thứ Sáu.",
        "keyVocab": [
            {
                "word": "thermal envelope",
                "ipa": "/ˈθɝː.məl ˈen.və.loʊp/",
                "meaning": "lớp vỏ bọc cách nhiệt công trình"
            },
            {
                "word": "electrochromic glass",
                "ipa": "/iˌlek.troʊˈkroʊ.mɪk ɡlæs/",
                "meaning": "kính điện sắc thông minh (đổi màu theo nhiệt độ)"
            },
            {
                "word": "torsional stress",
                "ipa": "/ˈtɔːr.ʃən.əl stres/",
                "meaning": "ứng suất xoắn trong kết cấu chịu lực"
            },
            {
                "word": "tuned mass damper",
                "ipa": "/tjuːnd mæs ˈdæm.pɚ/",
                "meaning": "quả cầu giảm chấn điều hòa dao động cho tòa nhà cao tầng"
            },
            {
                "word": "embodied carbon",
                "ipa": "/ɪmˈbɑː.did ˈkɑːr.bən/",
                "meaning": "lượng carbon tiềm ẩn trong sản xuất vật liệu xây dựng"
            }
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
    {
        "id": "read-16",
        "title": "Cognitive Biases in Executive Decision-Making",
        "type": "passage",
        "topic": "Tâm lý học quản trị",
        "level": "B2 - C1",
        "summary": "Khảo cứu tâm lý học hành vi về các bẫy thiên kiến nhận thức trong phòng họp điều hành doanh nghiệp và các giao thức hiệu chỉnh quyết định.",
        "content": "In corporate boardrooms and executive suites, strategic deliberations are frequently celebrated as paragons of rational analysis, underpinned by sophisticated econometric projections, discounted cash-flow models, and rigorous statistical regression. Yet, decades of empirical behavioral economics demonstrate that corporate leaders are routinely sabotaged by the very cognitive heuristics that enabled ancestral human survival. Under conditions of acute uncertainty and high stakes, intuitive cognitive shortcuts metastasize into insidious decision-making blind spots.\n\nAmong the most destructive of these psychological distortions is the sunk cost fallacy. When an enterprise sinks hundreds of millions of dollars into an underperforming software platform or failing foreign subsidiary, executive leadership frequently displays irrational escalation of commitment. Rather than acknowledging that historical expenditures are irrecoverable and evaluating the asset strictly through prospective future returns, executives channel additional capital into doomed ventures to safeguard personal prestige and evade the public humiliation of admitting strategic error.\n\nCompounding this vulnerability is confirmation bias, vigorously reinforced by boardroom groupthink. When a charismatic Chief Executive champions an aggressive corporate acquisition, sycophantic advisory teams subconsciously filter intelligence, accentuating market synergies while downplaying integration friction and regulatory antitrust hazards. Dissenting voices are subtly marginalized or self-silenced to preserve superficial consensus. The resulting epistemic echo chamber fosters an illusion of invulnerability, culminating in disastrous mergers that destroy shareholder valuation.\n\nTo inoculate organizations against these systemic biases, forward-thinking enterprises institute formal adversarial protocols. One highly effective technique is the Gary Klein \"pre-mortem\" analysis. Prior to finalizing a monumental acquisition or capital deployment, the executive committee convenes under the explicit hypothetical premise: \"Imagine we are five years in the future, and this initiative has suffered catastrophic failure. Write a comprehensive post-mortem explaining why.\" By legitimizing pessimism and dismantling the social stigma associated with dissent, pre-mortems unmask latent vulnerabilities before capital is irretrievably squandered.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nTrong các phòng họp hội đồng quản trị và các dãy phòng điều hành doanh nghiệp, các cuộc cân nhắc chiến lược thường được tôn vinh là hình mẫu của sự phân tích hợp lý, được củng cố bởi các dự báo kinh tế lượng tinh vi, mô hình chiết khấu dòng tiền và hồi quy thống kê nghiêm ngặt. Tuy nhiên, hàng thập kỷ kinh tế học hành vi thực nghiệm chứng minh rằng các nhà lãnh đạo doanh nghiệp thường xuyên bị phá hoại bởi chính những lối tắt nhận thức (heuristics) từng giúp tổ tiên loài người sinh tồn. Dưới các điều kiện bất định gay gắt và rủi ro cao, các lối tắt trực giác biến chứng thành những điểm mù ra quyết định nguy hiểm.\n\nTrong số những biến dạng tâm lý mang tính hủy diệt nhất là ngụy biện chi phí chìm (sunk cost fallacy). Khi một doanh nghiệp đã rót hàng trăm triệu đô la vào một nền tảng phần mềm hoạt động kém hiệu quả hoặc một công ty con nước ngoài đang thua lỗ, ban lãnh đạo thường thể hiện sự leo thang cam kết phi lý. Thay vì thừa nhận rằng các khoản chi tiêu trong quá khứ là không thể thu hồi và đánh giá tài sản nghiêm ngặt thông qua lợi nhuận tương lai kỳ vọng, các giám đốc điều hành tiếp tục đổ thêm vốn vào các dự án chắc chắn thất bại để bảo vệ uy tín cá nhân và tránh sự sỉ nhục công khai khi phải thừa nhận sai lầm chiến lược.\n\nLàm trầm trọng thêm lỗ hổng này là thiên kiến xác nhận (confirmation bias), được củng cố mạnh mẽ bởi hội chứng tư duy tập thể a dua (groupthink). Khi một Giám đốc điều hành có sức lôi cuốn ủng hộ một thương vụ mua lại công ty quyết liệt, các nhóm cố vấn xu nịnh sẽ vô thức sàng lọc thông tin, nhấn mạnh sự hiệp lực thị trường trong khi giảm nhẹ ma sát tích hợp và các mối nguy hiểm chống độc quyền từ cơ quan quản lý. Những tiếng nói bất đồng tinh tế bị gạt ra ngoài lề hoặc tự im lặng để giữ gìn sự đồng thuận hời hợt. Kết quả là một buồng vang nhận thức tạo ra ảo tưởng về sự bất khả chiến bại, dẫn đến những vụ sáp nhập thảm khốc phá hủy giá trị cổ đông.\n\nĐể tiêm chủng cho các tổ chức chống lại những thiên kiến mang tính hệ thống này, các doanh nghiệp có tư duy tiến bộ thiết lập các quy trình phản biện chính thức. Một kỹ thuật rất hiệu quả là phân tích \"mổ xẻ trước thực thi\" (pre-mortem) của Gary Klein. Trước khi hoàn tất một thương vụ mua lại hoặc triển khai vốn lớn, ủy ban điều hành họp lại dưới một giả định rõ ràng: \"Hãy tưởng tượng chúng ta đang ở 5 năm sau trong tương lai, và sáng kiến này đã thất bại thảm hại. Hãy viết một báo cáo khám nghiệm toàn diện giải thích lý do tại sao.\" Bằng cách hợp pháp hóa sự bi quan và dỡ bỏ sự kỳ thị xã hội gắn liền với sự bất đồng, các cuộc họp pre-mortem vạch trần các lỗ hổng tiềm ẩn trước khi vốn liếng bị lãng phí không thể cứu vãn.",
        "keyVocab": [
            {
                "word": "econometric projection",
                "ipa": "/iˌkɑː.nəˈmet.rɪk prəˈdʒek.ʃən/",
                "meaning": "dự báo kinh tế lượng"
            },
            {
                "word": "sunk cost fallacy",
                "ipa": "/sʌŋk kɑːst ˈfæl.ə.si/",
                "meaning": "ngụy biện chi phí chìm"
            },
            {
                "word": "escalation of commitment",
                "ipa": "/ˌes.kəˈleɪ.ʃən əv kəˈmɪt.mənt/",
                "meaning": "sự leo thang cam kết mù quáng"
            },
            {
                "word": "confirmation bias",
                "ipa": "/ˌkɑːn.fɚˈmeɪ.ʃən ˈbaɪ.əs/",
                "meaning": "thiên kiến xác nhận (chỉ nghe điều mình muốn)"
            },
            {
                "word": "pre-mortem analysis",
                "ipa": "/priː ˈmɔːr.təm əˈnæl.ə.sɪs/",
                "meaning": "phân tích dự báo nguyên nhân thất bại trước khi bắt đầu"
            }
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
    {
        "id": "read-17",
        "title": "Handling Customer Dispute & Warranty Litigation",
        "type": "conversation",
        "topic": "Chăm sóc khách hàng & Pháp lý",
        "level": "B1 - B2",
        "summary": "Cuộc thảo luận phương án hòa giải giữa Quản lý Trải nghiệm Khách hàng và Nữ Luật sư Doanh nghiệp đối với khiếu nại bảo hành của khách hàng VIP.",
        "content": [
            {
                "speaker": "Daniel (Male / Customer Experience Manager)",
                "text": "Emma, thanks for consulting on this matter. One of our enterprise accounts, Apex Logistics, sent a formal intent-to-sue notice regarding fifty fleet telematics modules that suffered battery drainage issues."
            },
            {
                "speaker": "Emma (Female / Corporate Legal Counsel)",
                "text": "I reviewed the master purchase agreement, Daniel. Did the hardware failure occur within the twelve-month limited warranty period, or has coverage lapsed?"
            },
            {
                "speaker": "Daniel (Male / Customer Experience Manager)",
                "text": "The units were installed thirteen months ago—technically four weeks beyond the warranty cutoff. However, the client argues that a firmware update we deployed caused the premature battery degradation."
            },
            {
                "speaker": "Emma (Female / Corporate Legal Counsel)",
                "text": "From a strict contractual standpoint, section 8.2 disclaims implied fitness for a particular purpose after twelve months. But if their engineering team proves our firmware update altered voltage thresholds, a latent defect claim could gain traction in commercial arbitration."
            },
            {
                "speaker": "Daniel (Male / Customer Experience Manager)",
                "text": "Litigation costs would dwarf the replacement expense. Replacing all fifty modules costs us roughly twelve thousand dollars, while Apex represents over eighty thousand dollars in recurring software subscriptions."
            },
            {
                "speaker": "Emma (Female / Corporate Legal Counsel)",
                "text": "Then commercial prudence dictates an amicable settlement. We should offer an out-of-warranty replacement as a goodwill gesture, contingent on Apex signing a mutual release of claims."
            },
            {
                "speaker": "Daniel (Male / Customer Experience Manager)",
                "text": "That protects our subscription revenue while extinguishing legal exposure. Can you draft the release of claims agreement by this afternoon?"
            },
            {
                "speaker": "Emma (Female / Corporate Legal Counsel)",
                "text": "Certainly. I will include a confidentiality covenant ensuring they cannot publicize this hardware replacement to other enterprise clients."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Emma, cảm ơn cô đã tư vấn về vấn đề này. Một trong những khách hàng doanh nghiệp của chúng ta, Apex Logistics, đã gửi thông báo chính thức về ý định khởi kiện liên quan đến 50 mô-đun viễn thông giám sát đội xe bị lỗi hao pin.\n\n- **Emma (Nữ / Luật sư Doanh nghiệp):** Tôi đã xem lại hợp đồng mua bán khung, Daniel. Lỗi phần cứng xảy ra trong thời hạn bảo hành giới hạn 12 tháng hay thời hạn bảo hiểm đã hết hiệu lực?\n\n- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Các thiết bị đã được lắp đặt cách đây 13 tháng—về mặt kỹ thuật là quá hạn bảo hành 4 tuần. Tuy nhiên, khách hàng lập luận rằng bản cập nhật chương trình cơ sở (firmware) mà chúng ta triển khai đã gây ra hiện tượng chai pin sớm.\n\n- **Emma (Nữ / Luật sư Doanh nghiệp):** Từ góc độ hợp đồng nghiêm ngặt, mục 8.2 miễn trừ bảo đảm ngụ ý về sự phù hợp cho một mục đích cụ thể sau 12 tháng. Nhưng nếu đội ngũ kỹ thuật của họ chứng minh bản cập nhật firmware của chúng ta đã làm thay đổi ngưỡng điện áp, khiếu nại về khuyết tật ẩn tàng có thể giành được ưu thế tại trọng tài thương mại.\n\n- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Chi phí kiện tụng sẽ vượt xa chi phí thay thế. Việc thay thế toàn bộ 50 mô-đun khiến chúng ta tốn khoảng 12.000 USD, trong khi Apex mang lại hơn 80.000 USD tiền thuê bao phần mềm định kỳ hàng năm.\n\n- **Emma (Nữ / Luật sư Doanh nghiệp):** Vậy thì sự thận trọng trong kinh doanh đòi hỏi một giải pháp hòa giải thân thiện. Chúng ta nên đề xuất thay thế ngoài bảo hành như một cử chỉ thiện chí, với điều kiện Apex phải ký vào thỏa thuận miễn trừ khiếu nại lẫn nhau.\n\n- **Daniel (Nam / Quản lý Trải nghiệm Khách hàng):** Cách đó vừa bảo vệ doanh thu thuê bao của chúng ta vừa dập tắt nguy cơ pháp lý. Cô có thể soạn thảo thỏa thuận từ bỏ khiếu nại vào chiều nay không?\n\n- **Emma (Nữ / Luật sư Doanh nghiệp):** Chắc chắn rồi. Tôi sẽ đưa vào một điều khoản bảo mật đảm bảo họ không thể công khai việc thay thế phần cứng này cho các khách hàng doanh nghiệp khác.",
        "keyVocab": [
            {
                "word": "intent-to-sue notice",
                "ipa": "/ɪnˈtent tuː suː ˈnoʊ.t̬ɪs/",
                "meaning": "thông báo chính thức về ý định khởi kiện"
            },
            {
                "word": "coverage lapsed",
                "ipa": "/ˈkʌv.ɚ.ɪdʒ læpst/",
                "meaning": "thời hạn bảo hành/bảo hiểm đã hết hiệu lực"
            },
            {
                "word": "latent defect",
                "ipa": "/ˈleɪ.tənt ˈdiː.fekt/",
                "meaning": "khuyết tật ẩn tàng của sản phẩm (khó thấy lúc mua)"
            },
            {
                "word": "goodwill gesture",
                "ipa": "/ɡʊdˈwɪl ˈdʒes.tʃɚ/",
                "meaning": "cử chỉ thiện chí thương mại"
            },
            {
                "word": "release of claims",
                "ipa": "/rɪˈliːs əv kleɪmz/",
                "meaning": "văn bản từ bỏ quyền khiếu nại/kiện tụng"
            }
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
    {
        "id": "read-18",
        "title": "The Epistemology of Misinformation in the Algorithmic Age",
        "type": "passage",
        "topic": "Truyền thông & Xã hội số",
        "level": "B2 - C1",
        "summary": "Tiểu luận về cơ chế phát tán thông tin sai lệch trên mạng xã hội, các thuật toán tối ưu hóa tương tác gây kích động và kỹ thuật tiêm chủng nhận thức.",
        "content": "In the embryonic dawn of the World Wide Web, cyber-utopians proclaimed that frictionless digital connectivity would inaugurate a golden era of democratic enlightenment. The decentralized dissemination of knowledge, advocates argued, would dismantle authoritarian information monopolies, empower citizen journalism, and eradicate societal ignorance. Three decades later, this idealistic prophecy has curdled into a hyper-polarized infosphere plagued by algorithmic radicalization, synthetic media, and the systemic erosion of consensus reality.\n\nThe structural vector driving this epistemological crisis is the economic architecture of the attention economy. Commercial social media platforms do not optimize their recommendation algorithms for objective veracity or nuanced pedagogical value; they optimize strictly for user engagement—measured in watch duration, retweets, and emotive commenting. Behavioral psychologists have long established that human cognition is asymmetrically stimulated by moral outrage, existential dread, and in-group tribal validation. Consequently, algorithms systematically amplify sensationalist falsehoods, which diffuse across social networks up to six times faster than verified factual corrections.\n\nOver time, sustained exposure to algorithmic curation produces hermetically sealed epistemic bubbles. Within these algorithmic echo chambers, alternative perspectives are systematically filtered out, and counter-evidence is reflexively dismissed as malevolent propaganda manufactured by untrustworthy institutional elites. When synthetic deepfakes and automated generative disinformation bots are introduced into these fertile ideological soils, the boundary between empirical actuality and manufactured fiction dissolves completely, precipitating acute social fragmentation.\n\nConfronting this existential crisis requires moving beyond reactive, whack-a-mole content censorship toward \"cognitive inoculation.\" Pioneered by social psychologists, pre-bunking strategies expose internet users to weakened, micro-dosed examples of manipulation techniques—such as emotional scapegoating and fake expert endorsements—before they encounter viral misinformation in the wild. By cultivating digital media literacy and fostering structural algorithmic transparency, open societies can build societal resilience without sacrificing the inviolable principles of free expression.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nVào buổi bình minh sơ khai của mạng World Wide Web, những người theo chủ nghĩa không tưởng trên không gian mạng đã tuyên bố rằng sự kết nối kỹ thuật số không ma sát sẽ mở ra một kỷ nguyên vàng của sự khai sáng dân chủ. Những người ủng hộ lập luận rằng việc phổ biến kiến thức phi tập trung sẽ phá bỏ sự độc quyền thông tin độc tài, trao quyền cho báo chí công dân và xóa bỏ sự thiếu hiểu biết của xã hội. Ba thập kỷ sau, lời tiên tri duy tâm này đã biến chất thành một bầu không khí thông tin siêu phân cực bị hoành hành bởi sự cực đoan hóa theo thuật toán, truyền thông tổng hợp và sự xói mòn mang tính hệ thống của thực tế đồng thuận.\n\nVéc-tơ cấu trúc thúc đẩy cuộc khủng hoảng nhận thức luận này là kiến trúc kinh tế của nền kinh tế chú ý. Các nền tảng truyền thông xã hội thương mại không tối ưu hóa các thuật toán đề xuất của họ cho tính xác thực khách quan hoặc giá trị sư phạm tinh tế; họ tối ưu hóa nghiêm ngặt cho sự tương tác của người dùng—được đo bằng thời lượng xem, lượt chia sẻ lại và bình luận đầy cảm xúc. Các nhà tâm lý học hành vi từ lâu đã xác định rằng nhận thức của con người bị kích thích bất đối xứng bởi sự phẫn nộ đạo đức, nỗi sợ hãi hiện sinh và sự chứng thực của bộ tộc nhóm nội bộ. Do đó, các thuật toán khuếch đại một cách có hệ thống những thông tin sai lệch giật gân, lan truyền trên các mạng xã hội nhanh hơn gấp 6 lần so với các đính chính thực tế đã được xác minh.\n\nTheo thời gian, việc tiếp xúc liên tục với sự tuyển chọn của thuật toán sẽ tạo ra các bong bóng nhận thức khép kín. Trong các buồng vang thuật toán này, các góc nhìn thay thế bị lọc bỏ một cách có hệ thống, và các bằng chứng phản bác bị bác bỏ theo phản xạ như là tuyên truyền độc hại do các tầng lớp tinh hoa thể chế không đáng tin cậy tạo ra. Khi các video deepfake tổng hợp và các bot thông tin sai lệch tự động được đưa vào các mảnh đất ý thức hệ màu mỡ này, ranh giới giữa thực tế thực nghiệm và tiểu thuyết ngụy tạo sẽ tan biến hoàn toàn, gây ra sự phân mảnh xã hội gay gắt.\n\nĐối mặt với cuộc khủng hoảng hiện sinh này đòi hỏi phải vượt ra ngoài việc kiểm duyệt nội dung mang tính phản ứng đối phó để hướng tới \"tiêm chủng nhận thức\". Được tiên phong bởi các nhà tâm lý học xã hội, các chiến lược \"bác bỏ trước\" (pre-bunking) cho người dùng internet tiếp xúc với các ví dụ liều nhỏ về các kỹ thuật thao túng—chẳng hạn như việc đổ lỗi cảm xúc và sự chứng thực của chuyên gia giả mạo—trước khi họ bắt gặp thông tin sai lệch trên mạng. Bằng cách trau dồi hiểu biết về truyền thông kỹ thuật số và thúc đẩy tính minh bạch của thuật toán cấu trúc, các xã hội cởi mở có thể xây dựng khả năng phục hồi của xã hội mà không phải hy sinh các nguyên tắc bất khả xâm phạm về tự do ngôn luận.",
        "keyVocab": [
            {
                "word": "attention economy",
                "ipa": "/əˈten.ʃən iˈkɑː.nə.mi/",
                "meaning": "nền kinh tế chú ý (kinh doanh sự chú ý của người dùng)"
            },
            {
                "word": "epistemic bubble",
                "ipa": "/ˌep.əˈstiː.mɪk ˈbʌb.əl/",
                "meaning": "bong bóng nhận thức khép kín"
            },
            {
                "word": "echo chamber",
                "ipa": "/ˈek.oʊ ˌtʃeɪm.bɚ/",
                "meaning": "buồng vang thông tin (chỉ lặp lại quan điểm của mình)"
            },
            {
                "word": "cognitive inoculation",
                "ipa": "/ˈkɑːɡ.nə.t̬ɪv ɪˌnɑː.kjəˈleɪ.ʃən/",
                "meaning": "tiêm chủng nhận thức phòng ngừa tin giả"
            },
            {
                "word": "pre-bunking",
                "ipa": "/priː ˈbʌŋk.ɪŋ/",
                "meaning": "bác bỏ và giải thích thủ thuật lừa đảo trước khi bị tiếp cận"
            }
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
    {
        "id": "read-19",
        "title": "Academic Thesis Defense & Cross-Examination",
        "type": "conversation",
        "topic": "Giáo dục & Nghiên cứu học thuật",
        "level": "B2 - C1",
        "summary": "Phiên phản biện luận án tiến sĩ thiên văn học giữa Giáo sư Chủ tịch Hội đồng và Nữ Nghiên cứu sinh về dữ liệu quang phổ sao neutron.",
        "content": [
            {
                "speaker": "Professor Arthur (Male / Dissertation Committee Chair)",
                "text": "Dr. Maya, congratulations on a compelling dissertation presentation. However, committee member Dr. Vance raised a formidable methodological objection regarding your spectral analysis of neutron star binary mergers."
            },
            {
                "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)",
                "text": "Thank you, Professor Arthur. I welcome the committee's rigorous scrutiny. Is the objection directed at our gravitational wave signal filtering, or our electromagnetic counterpart calibrations?"
            },
            {
                "speaker": "Professor Arthur (Male / Dissertation Committee Chair)",
                "text": "Specifically, chapter four assumes that the observed high-energy gamma-ray burst exhibits isotropic emission. Given relativistic beaming physics, if the jet angle was tilted merely five degrees off our line of sight, your total calculated kilonova ejecta mass would be overstated by thirty percent."
            },
            {
                "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)",
                "text": "That is an astute critique. In appendix C, we anticipated that exact geometric degeneracy. To counteract line-of-sight ambiguity, we cross-validated the gamma-ray telemetry against late-time synchrotron radio afterglow data collected across sixteen months by the Very Large Array."
            },
            {
                "speaker": "Professor Arthur (Male / Dissertation Committee Chair)",
                "text": "Radio afterglow modeling requires robust assumptions regarding circumstellar medium density. How did you break the degeneracy between density and jet opening angle?"
            },
            {
                "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)",
                "text": "We utilized relativistic hydrodynamical simulations constrained by polarimetric optical observations. This narrowed our opening angle confidence interval to within three point two degrees, reaffirming that our ejecta mass bounds remain statistically robust at three sigma."
            },
            {
                "speaker": "Professor Arthur (Male / Dissertation Committee Chair)",
                "text": "That is an extraordinarily thorough defense. The incorporation of radio polarimetry addresses our primary theoretical skepticism."
            },
            {
                "speaker": "Dr. Maya (Female / PhD Candidate in Astrophysics)",
                "text": "Thank you, Professor. I will incorporate this cross-validation synthesis prominently into the final dissertation revision before archiving."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Maya, chúc mừng cô vì một bài thuyết trình luận án rất thuyết phục. Tuy nhiên, thành viên hội đồng là Tiến sĩ Vance đã nêu ra một sự phản đối phương pháp luận đáng gờm liên quan đến phân tích quang phổ của cô về các vụ sáp nhập sao neutron đôi.\n\n- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Cảm ơn Giáo sư Arthur. Tôi rất hoan nghênh sự xem xét kỹ lưỡng của hội đồng. Sự phản đối nhắm vào việc lọc tín hiệu sóng hấp dẫn hay hiệu chuẩn phần bức xạ điện từ tương ứng?\n\n- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Cụ thể, chương 4 giả định rằng vụ nổ tia gamma năng lượng cao quan sát được thể hiện sự phát xạ đẳng hướng. Dựa trên vật lý chùm tia tương đối tính, nếu góc tia chỉ bị nghiêng 5 độ so với đường ngắm của chúng ta, tổng khối lượng vật chất phóng ra từ vụ nổ kilonova được tính toán của cô sẽ bị phóng đại quá mức 30%.\n\n- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Đó là một lời phê bình sắc bén. Trong phụ lục C, chúng tôi đã dự đoán chính xác sự suy biến hình học đó. Để triệt tiêu sự mơ hồ về đường ngắm, chúng tôi đã kiểm định chéo dữ liệu đo từ xa của tia gamma với dữ liệu phát xạ vô tuyến synchrotron giai đoạn muộn được thu thập trong 16 tháng bởi mảng kính thiên văn Very Large Array.\n\n- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Mô hình phát xạ vô tuyến sau vụ nổ đòi hỏi các giả định vững chắc về mật độ môi trường xung quanh sao. Cô đã phá vỡ sự suy biến giữa mật độ và góc mở của tia phóng như thế nào?\n\n- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Chúng tôi đã sử dụng các mô phỏng thủy động lực học tương đối tính bị hạn chế bởi các quan sát phân cực quang học. Điều này thu hẹp khoảng tin cậy của góc mở xuống trong phạm vi 3,2 độ, tái khẳng định rằng ranh giới khối lượng vật chất phóng ra của chúng tôi vẫn vững chắc về mặt thống kê ở mức 3 sigma.\n\n- **Giáo sư Arthur (Nam / Chủ tịch Hội đồng Luận án):** Đó là một sự bảo vệ luận án cực kỳ kỹ lưỡng. Việc kết hợp phép đo phân cực vô tuyến đã giải quyết được sự hoài nghi lý thuyết chính của chúng tôi.\n\n- **Maya (Nữ / Nghiên cứu sinh Tiến sĩ Vật lý thiên văn):** Cảm ơn Giáo sư. Tôi sẽ đưa phần tổng hợp kiểm định chéo này vào vị trí nổi bật trong bản sửa đổi luận án cuối cùng trước khi lưu trữ.",
        "keyVocab": [
            {
                "word": "spectral analysis",
                "ipa": "/ˈspek.trəl əˈnæl.ə.sɪs/",
                "meaning": "phân tích quang phổ học"
            },
            {
                "word": "relativistic beaming",
                "ipa": "/ˌrel.ə.tɪˈvɪs.tɪk ˈbiː.mɪŋ/",
                "meaning": "hiệu ứng chùm tia tương đối tính"
            },
            {
                "word": "geometric degeneracy",
                "ipa": "/ˌdʒiː.əˈmet.rɪk dɪˈdʒen.ɚ.ə.si/",
                "meaning": "sự suy biến hình học trong đo đạc thiên văn"
            },
            {
                "word": "cross-validation",
                "ipa": "/ˌkrɑːs væl.əˈdeɪ.ʃən/",
                "meaning": "kiểm định chéo đối chiếu giữa các nguồn dữ liệu"
            },
            {
                "word": "statistically robust",
                "ipa": "/stəˈtɪs.tɪ.kəl.i roʊˈbʌst/",
                "meaning": "vững chắc về mặt thống kê học (độ tin cậy cao)"
            }
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
    {
        "id": "read-20",
        "title": "Microbiome Diversity and Psychosomatic Well-being",
        "type": "passage",
        "topic": "Sức khỏe & Y học dự phòng",
        "level": "B2 - C1",
        "summary": "Nghiên cứu y sinh về trục ruột - não (gut-brain axis), vai trò của hệ vi sinh đường ruột trong việc tổng hợp chất dẫn truyền thần kinh và điều hòa tâm trạng.",
        "content": "For more than a century, orthodox psychiatric pathology operated under a strictly neuro-centric paradigm. Mood disorders, depressive episodes, and chronic generalized anxiety were conceptualized solely as neurochemical imbalances localized within the cerebral cortex, primarily driven by monoaminergic dysregulation in synaptic junctions. Modern gastroenterology and molecular microbiology have shattered this cerebral insularity by unveiling the gut-brain axis—a bidirectional biochemical communication superhighway linking the central nervous system with the enteric microbiota.\n\nHousing over one hundred trillion microbial organisms spanning thousands of bacterial species, the human gastrointestinal tract functions as a sophisticated endocrine and neurochemical synthesis laboratory. Remarkably, an estimated ninety percent of the human body's serotonin—a critical neurotransmitter governing mood stability, circadian rhythm, and emotional valence—is synthesized not in the cranial brain, but by enterochromaffin cells in the gut lining, tightly modulated by indigenous microbiome communities.\n\nMicrobial communication with the central nervous system proceeds via multiple physiological pathways. Commensal bacteria metabolize dietary indigestible fibers into short-chain fatty acids (SCFAs), notably butyrate, acetate, and propionate. These organic metabolites cross the intestinal epithelial barrier to stimulate the vagus nerve—the primary cranial nerve connecting the brainstem to abdominal visceral organs. Furthermore, SCFAs modulate systemic immune tolerance by suppressing pro-inflammatory cytokines that otherwise compromise blood-brain barrier integrity, shielding neural tissue from neuroinflammation.\n\nConversely, chronic psychological distress and ultra-processed diets precipitate gastrointestinal dysbiosis. When harmful pathogenic bacterial strains outcompete beneficial commensals, intestinal permeability increases—a clinical condition colloquially termed \"leaky gut.\" Bacterial endotoxins, such as lipopolysaccharides, leak into peripheral bloodstream circulation, triggering systemic low-grade inflammation that directly incites depressive lethargy and cognitive fog. Consequently, nutritional psychiatry is pioneering targeted psychobiotics—beneficial bacterial strains formulated to restore microbiome homeostasis and alleviate psychiatric distress from the inside out.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nTrong hơn một thế kỷ, bệnh học tâm thần chính thống đã vận hành dưới một hệ hình hoàn toàn lấy não bộ làm trung tâm. Rối loạn tâm trạng, các đợt trầm cảm và lo âu mãn tính được khái niệm hóa thuần túy là sự mất cân bằng hóa thần kinh khu trú trong vỏ não, chủ yếu do rối loạn điều hòa monoaminergic tại các khớp synap. Khoa tiêu hóa và vi sinh phân tử hiện đại đã phá vỡ sự cô lập não bộ này bằng cách khám phá ra trục ruột - não—một siêu xa lộ truyền thông sinh hóa hai chiều kết nối hệ thần kinh trung ương với hệ vi sinh vật đường ruột.\n\nLà nơi cư trú của hơn 100 nghìn tỷ sinh vật vi sinh bao gồm hàng nghìn loài vi khuẩn, đường tiêu hóa của con người hoạt động như một phòng thí nghiệm tổng hợp hóa thần kinh và nội tiết tinh vi. Đáng chú ý, ước tính khoảng 90% lượng serotonin của cơ thể con người—một chất dẫn truyền thần kinh quan trọng chi phối sự ổn định tâm trạng, nhịp sinh học và cảm xúc—được tổng hợp không phải trong não bộ, mà bởi các tế bào enterochromaffin trong niêm mạc ruột, được điều hòa chặt chẽ bởi các cộng đồng vi sinh vật bản địa.\n\nGiao tiếp của vi sinh vật với hệ thần kinh trung ương diễn ra qua nhiều con đường sinh lý. Vi khuẩn cộng sinh chuyển hóa chất xơ không tiêu hóa được trong chế độ ăn uống thành các axit béo chuỗi ngắn (SCFA), đáng chú ý là butyrate, acetate và propionate. Các chất chuyển hóa hữu cơ này vượt qua hàng rào biểu mô ruột để kích thích dây thần kinh phế vị (vagus nerve)—dây thần kinh sọ chính kết nối thân não với các cơ quan nội tạng bụng. Hơn nữa, SCFA điều hòa khả năng dung nạp miễn dịch toàn thân bằng cách ức chế các cytokine gây viêm vốn có thể làm tổn hại tính toàn vẹn của hàng rào máu - não, che chở cho mô thần kinh khỏi viêm thần kinh.\n\nNgược lại, sự căng thẳng tâm lý mãn tính và chế độ ăn uống siêu chế biến gây ra sự mất cân bằng hệ vi sinh đường ruột (dysbiosis). Khi các chủng vi khuẩn gây bệnh có hại cạnh tranh lấn át các vi khuẩn cộng sinh có lợi, tính thấm của ruột tăng lên—một tình trạng lâm sàng thường được gọi là \"hội chứng rò rỉ ruột\". Các nội độc tố vi khuẩn, chẳng hạn như lipopolysaccharide, rò rỉ vào tuần hoàn máu ngoại vi, kích hoạt phản ứng viêm mức độ thấp toàn thân, trực tiếp gây ra sự lờ đờ uể oải và sương mù nhận thức. Do đó, ngành tâm thần học dinh dưỡng đang tiên phong sử dụng các loại psychobiotics có mục tiêu—các chủng vi khuẩn có lợi được bào chế để khôi phục cân bằng nội môi hệ vi sinh vật và làm giảm bớt sự đau khổ tâm thần từ trong ra ngoài.",
        "keyVocab": [
            {
                "word": "gut-brain axis",
                "ipa": "/ɡʌt breɪn ˈæk.sɪs/",
                "meaning": "trục não - ruột (kết nối hai chiều)"
            },
            {
                "word": "vagus nerve",
                "ipa": "/ˈveɪ.ɡəs nɝːv/",
                "meaning": "dây thần kinh phế vị (dây thần kinh số X)"
            },
            {
                "word": "short-chain fatty acids",
                "ipa": "/ʃɔːrt tʃeɪn ˈfæt.i ˈæs.ɪdz/",
                "meaning": "axit béo chuỗi ngắn (SCFA)"
            },
            {
                "word": "dysbiosis",
                "ipa": "/ˌdɪs.baɪˈoʊ.sɪs/",
                "meaning": "sự mất cân bằng hệ vi sinh đường ruột"
            },
            {
                "word": "psychobiotics",
                "ipa": "/ˌsaɪ.koʊ.baɪˈɑː.t̬ɪks/",
                "meaning": "chế phẩm sinh học lợi khuẩn điều trị tâm lý"
            }
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
    {
        "id": "read-21",
        "title": "High-Stakes Real Estate Acquisition & Zoning Compliance",
        "type": "conversation",
        "topic": "Bất động sản & Đàm phán thương mại",
        "level": "B2 - C1",
        "summary": "Đàm phán quy hoạch phân vùng và cam kết mật độ xây dựng giữa Nhà phát triển bất động sản thương mại và Nữ Chuyên viên Quy hoạch đô thị chính quyền thành phố.",
        "content": [
            {
                "speaker": "Brandon (Male / Commercial Property Developer)",
                "text": "Clara, thank you for agreeing to review our redevelopment dossier for the Old Waterfront Wharf. Our syndicate is prepared to invest eighty million dollars to convert the derelict industrial shipyard into a mixed-use commercial and residential hub."
            },
            {
                "speaker": "Clara (Female / Municipal Urban Planning Officer)",
                "text": "We applaud your private capital commitment, Brandon. However, the municipal zoning code currently designates that riverbank parcel strictly as M-2 light industrial. Transitioning to mixed-use requires a formal zoning variance and municipal council approval."
            },
            {
                "speaker": "Brandon (Male / Commercial Property Developer)",
                "text": "Understood. Our blueprints propose a floor-area ratio (FAR) of four point five, accommodating three residential towers, ground-floor retail, and an open civic amphitheater."
            },
            {
                "speaker": "Clara (Female / Municipal Urban Planning Officer)",
                "text": "A FAR of four point five exceeds our waterfront density master plan by thirty percent. Furthermore, community advocates will vigorously oppose any development that impedes public riverbank access."
            },
            {
                "speaker": "Brandon (Male / Commercial Property Developer)",
                "text": "We anticipated those objections. To offset density concerns, we are dedicating forty percent of the parcel footprint to a continuous public riparian park and boardwalk, while offering a binding easement covenant to the city in perpetuity."
            },
            {
                "speaker": "Clara (Female / Municipal Urban Planning Officer)",
                "text": "The public easement covenant is a significant concession. What about mandatory inclusionary housing requirements? Municipal ordinance mandates that fifteen percent of units must qualify as affordable housing."
            },
            {
                "speaker": "Brandon (Male / Commercial Property Developer)",
                "text": "We are fully compliant. In fact, we designated eighteen percent of all one- and two-bedroom apartments as subsidized affordable units for low-to-middle income families."
            },
            {
                "speaker": "Clara (Female / Municipal Urban Planning Officer)",
                "text": "With an eighteen percent affordable commitment and a deeded public park easement, your variance application presents compelling civic merit. I will recommend it favorably for public hearing next month."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Clara, cảm ơn cô đã đồng ý xem xét hồ sơ tái phát triển của chúng tôi cho khu Cảng Bến tàu cũ. Nghiệp đoàn của chúng tôi sẵn sàng đầu tư 80 triệu đô la để chuyển đổi xưởng đóng tàu công nghiệp bỏ hoang thành một trung tâm thương mại và dân cư phức hợp.\n\n- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Chúng tôi hoan nghênh cam kết vốn tư nhân của bên anh, Brandon. Tuy nhiên, quy hoạch phân vùng của thành phố hiện chỉ định khu đất ven sông đó là đất công nghiệp nhẹ M-2. Việc chuyển đổi sang mục đích sử dụng hỗn hợp đòi hỏi phải có sự điều chỉnh quy hoạch phân vùng chính thức và sự phê duyệt của hội đồng thành phố.\n\n- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Đã hiểu. Bản thiết kế của chúng tôi đề xuất hệ số sử dụng đất (FAR) là 4,5, bao gồm 3 tòa tháp dân cư, khu bán lẻ ở tầng trệt và một khán đài công cộng ngoài trời.\n\n- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Hệ số FAR 4,5 vượt quá quy hoạch tổng thể mật độ ven sông của chúng tôi 30%. Hơn nữa, các đại diện cộng đồng sẽ kịch liệt phản đối bất kỳ sự phát triển nào cản trở lối tiếp cận bờ sông của công chúng.\n\n- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Chúng tôi đã lường trước những phản đối đó. Để bù đắp cho những lo ngại về mật độ, chúng tôi dành 40% diện tích khu đất cho công viên và lối đi lót ván ven sông công cộng liên tục, đồng thời cung cấp cam kết quyền địa dịch ràng buộc cho thành phố vĩnh viễn.\n\n- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Cam kết quyền địa dịch công cộng là một sự nhượng bộ đáng kể. Còn các yêu cầu bắt buộc về nhà ở xã hội hòa nhập thì sao? Quy định của thành phố bắt buộc 15% số căn hộ phải đủ điều kiện là nhà ở giá phải chăng.\n\n- **Brandon (Nam / Nhà phát triển Bất động sản Thương mại):** Chúng tôi hoàn toàn tuân thủ. Trên thực tế, chúng tôi đã chỉ định 18% tổng số căn hộ 1 và 2 phòng ngủ làm các căn hộ được trợ cấp giá phải chăng cho các gia đình có thu nhập thấp đến trung bình.\n\n- **Clara (Nữ / Chuyên viên Quy hoạch Đô thị Thành phố):** Với cam kết 18% nhà ở giá phải chăng và chứng thư quyền địa dịch công viên công cộng, đơn xin điều chỉnh quy hoạch của anh thể hiện giá trị công dân rất thuyết phục. Tôi sẽ đưa ra khuyến nghị tích cực cho buổi điều trần công khai vào tháng tới.",
        "keyVocab": [
            {
                "word": "zoning variance",
                "ipa": "/ˈzoʊ.nɪŋ ˈver.i.əns/",
                "meaning": "sự điều chỉnh/miễn trừ quy hoạch phân vùng"
            },
            {
                "word": "floor-area ratio",
                "ipa": "/flɔːr ˈer.i.ə ˈreɪ.ʃi.oʊ/",
                "meaning": "hệ số sử dụng đất (FAR)"
            },
            {
                "word": "riparian park",
                "ipa": "/raɪˈper.i.ən pɑːrk/",
                "meaning": "công viên sinh thái ven bờ sông"
            },
            {
                "word": "easement covenant",
                "ipa": "/ˈiːz.mənt ˈkʌv.ə.nənt/",
                "meaning": "cam kết quyền địa dịch công cộng (cho phép người dân đi lại vĩnh viễn)"
            },
            {
                "word": "inclusionary housing",
                "ipa": "/ɪnˈkluː.ʒən.er.i ˈhaʊ.zɪŋ/",
                "meaning": "chính sách nhà ở xã hội hòa nhập bắt buộc"
            }
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
    },
    {
        "id": "read-22",
        "title": "Job Interview: Strengths, Weaknesses, and Career Goals",
        "type": "conversation",
        "topic": "Công sở & Nghề nghiệp",
        "level": "B1 - B2",
        "summary": "Buổi phỏng vấn xin việc vị trí Chuyên viên Tiếp thị Kỹ thuật số giữa Giám đốc tuyển dụng và ứng viên tiềm năng.",
        "content": [
            {
                "speaker": "Alex (Male / Hiring Manager)",
                "text": "Good afternoon, Linh. Welcome to our office. Did you have any trouble finding our building today?"
            },
            {
                "speaker": "Linh (Female / Candidate)",
                "text": "Good afternoon, Mr. Alex. Not at all. Your directions were very clear, and the commute was quite pleasant."
            },
            {
                "speaker": "Alex (Male / Hiring Manager)",
                "text": "Wonderful. To begin, could you tell me a little bit about yourself and why you applied for this Digital Marketing Specialist position?"
            },
            {
                "speaker": "Linh (Female / Candidate)",
                "text": "Certainly. I have worked in social media marketing for over three years. In my previous role, I managed organic campaigns that increased our website traffic by thirty-five percent. I applied here because your company produces educational technology that truly empowers students."
            },
            {
                "speaker": "Alex (Male / Hiring Manager)",
                "text": "That is impressive. How do you handle unexpected deadlines or shifting priorities when multiple campaigns run concurrently?"
            },
            {
                "speaker": "Linh (Female / Candidate)",
                "text": "I prioritize tasks using a project management board. If urgent revisions arise, I communicate promptly with my teammates so we can redistribute workloads without missing critical milestones."
            },
            {
                "speaker": "Alex (Male / Hiring Manager)",
                "text": "Every professional has areas to improve. What would you consider your greatest professional weakness?"
            },
            {
                "speaker": "Linh (Female / Candidate)",
                "text": "In the past, I sometimes hesitated to delegate tasks because I wanted every detail to be perfect. However, I have learned that trusting capable colleagues produces better outcomes and fosters team growth."
            },
            {
                "speaker": "Alex (Male / Hiring Manager)",
                "text": "That shows great self-awareness. Do you have any questions for me regarding our team culture or expectations?"
            },
            {
                "speaker": "Linh (Female / Candidate)",
                "text": "Yes, thank you. Could you share what qualities distinguish the most successful marketers within your organization?"
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Alex (Nam / Trưởng phòng tuyển dụng):** Chào buổi chiều, Linh. Chào mừng bạn đến văn phòng của chúng tôi. Hôm nay bạn tìm đường đến tòa nhà có thuận lợi không?\n\n- **Linh (Nữ / Ứng viên):** Chào buổi chiều, anh Alex. Rất thuận lợi ạ. Hướng dẫn chỉ đường của công ty rất rõ ràng và việc đi lại khá thoải mái.\n\n- **Alex (Nam / Trưởng phòng tuyển dụng):** Tuyệt vời. Để bắt đầu, bạn có thể giới thiệu một chút về bản thân và lý do bạn ứng tuyển vào vị trí Chuyên viên Tiếp thị Kỹ thuật số này không?\n\n- **Linh (Nữ / Ứng viên):** Dạ chắc chắn rồi ạ. Tôi đã làm việc trong lĩnh vực tiếp thị truyền thông xã hội hơn ba năm. Ở vị trí trước đây, tôi quản lý các chiến dịch tự nhiên giúp tăng lưu lượng truy cập trang web lên 35%. Tôi ứng tuyển vào đây vì công ty tạo ra các sản phẩm công nghệ giáo dục thực sự trao quyền cho học sinh.\n\n- **Alex (Nam / Trưởng phòng tuyển dụng):** Rất ấn tượng. Bạn xử lý thế nào trước các hạn chót bất ngờ hoặc các mức độ ưu tiên thay đổi khi nhiều chiến dịch chạy đồng thời?\n\n- **Linh (Nữ / Ứng viên):** Tôi sắp xếp thứ tự ưu tiên cho công việc bằng bảng quản lý dự án. Nếu có yêu cầu chỉnh sửa khẩn cấp, tôi trao đổi ngay với đồng đội để có thể phân bổ lại khối lượng công việc mà không trễ các cột mốc quan trọng.\n\n- **Alex (Nam / Trưởng phòng tuyển dụng):** Bất kỳ chuyên gia nào cũng có điểm cần hoàn thiện. Bạn coi điểm yếu lớn nhất trong công việc của mình là gì?\n\n- **Linh (Nữ / Ứng viên):** Trước đây, tôi đôi khi ngần ngại giao việc cho người khác vì muốn mọi chi tiết đều phải hoàn hảo. Tuy nhiên, tôi đã học được rằng việc tin tưởng các đồng nghiệp có năng lực sẽ mang lại kết quả tốt hơn và thúc đẩy sự phát triển của cả nhóm.\n\n- **Alex (Nam / Trưởng phòng tuyển dụng):** Điều đó cho thấy khả năng tự nhận thức rất tốt. Bạn có câu hỏi nào dành cho tôi về văn hóa đội ngũ hoặc các kỳ vọng không?\n\n- **Linh (Nữ / Ứng viên):** Dạ có ạ, cảm ơn anh. Anh có thể chia sẻ những phẩm chất nào tạo nên sự khác biệt của những chuyên viên tiếp thị thành công nhất trong tổ chức của mình không ạ?",
        "keyVocab": [
            {
                "word": "commute",
                "ipa": "/kəˈmjuːt/",
                "meaning": "quãng đường đi lại giữa nhà và nơi làm việc"
            },
            {
                "word": "concurrently",
                "ipa": "/kənˈkɝː.ənt.li/",
                "meaning": "đồng thời, cùng một lúc"
            },
            {
                "word": "prioritize",
                "ipa": "/praɪˈɔːr.ə.taɪz/",
                "meaning": "sắp xếp thứ tự ưu tiên"
            },
            {
                "word": "delegate",
                "ipa": "/ˈdel.ə.ɡeɪt/",
                "meaning": "ủy quyền, giao phó trách nhiệm"
            },
            {
                "word": "self-awareness",
                "ipa": "/ˌself.əˈwer.nəs/",
                "meaning": "sự tự nhận thức, hiểu rõ bản thân"
            }
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
    {
        "id": "read-23",
        "title": "The Art of Mindful Eating and Healthy Habits",
        "type": "passage",
        "topic": "Sức khỏe & Lối sống",
        "level": "B1 - B2",
        "summary": "Bài đọc khám phá phương pháp ăn uống chánh niệm, tác hại của việc ăn vội trước màn hình và cách xây dựng mối quan hệ lành mạnh với thực phẩm.",
        "content": "In modern society, busy schedules and digital distractions have fundamentally changed the way we consume food. Many working adults eat their meals in front of computer monitors or while scrolling through social media notifications on their smartphones. Consequently, people frequently swallow large meals in less than ten minutes without truly tasting their food or paying attention to physiological signals of fullness. Nutritionists refer to this pattern as absent-minded consumption, which often leads to overeating and digestive discomfort.\n\nMindful eating offers a refreshing antidote to this chaotic habit. Rooted in mindfulness practices, it encourages individuals to engage all five senses during mealtime. When practicing mindful eating, you begin by observing the vivid colors and pleasant aromas of the ingredients before taking your first bite. Chewing slowly allows digestive enzymes in saliva to break down nutrients effectively, while giving the brain sufficient time—typically twenty minutes—to register satiety hormones released by the stomach.\n\nFurthermore, developing a mindful approach to eating helps people distinguish between emotional hunger and physical hunger. Emotional hunger strikes suddenly, demanding immediate satisfaction through high-sugar or ultra-processed comfort foods during moments of stress or boredom. In contrast, genuine physical hunger develops gradually and can be satisfied by a diverse variety of nourishing whole foods. Recognizing this difference prevents guilt and empowers individuals to cultivate a sustainable, positive relationship with nutrition.\n\nAdopting mindful eating does not require strict dietary restrictions or counting every calorie. Simple lifestyle adjustments, such as sitting down at a proper dining table, putting down utensils between mouthfuls, and savoring the unique flavors of home-cooked meals, can dramatically enhance digestion and emotional well-being. By treating each meal as an intentional pause rather than a chore, we reconnect with the nourishing power of wholesome food.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nTrong xã hội hiện đại, lịch trình bận rộn và những xao nhãng kỹ thuật số đã thay đổi căn bản cách chúng ta ăn uống. Nhiều người trưởng thành đi làm thường ăn cơm trước màn hình máy tính hoặc trong khi lướt thông báo mạng xã hội trên điện thoại thông minh. Do đó, mọi người thường nuốt chửng những bữa ăn lớn chỉ trong chưa đầy mười phút mà không thực sự nếm trải hương vị thức ăn hay chú ý đến các tín hiệu sinh lý báo hiệu đã no. Các chuyên gia dinh dưỡng gọi kiểu ăn uống này là tiêu thụ thiếu chú tâm, điều thường dẫn đến việc ăn quá no và khó chịu về tiêu hóa.\n\nĂn uống chánh niệm mang lại một liều thuốc giải sảng khoái cho thói quen hỗn loạn này. Có nguồn gốc từ các bài thực hành chánh niệm, phương pháp này khuyến khích mỗi cá nhân vận dụng cả năm giác quan trong bữa ăn. Khi thực hành ăn uống chánh niệm, bạn bắt đầu bằng việc quan sát màu sắc sống động và mùi thơm dễ chịu của các nguyên liệu trước khi cắn miếng đầu tiên. Việc nhai chậm cho phép các enzyme tiêu hóa trong nước bọt phân giải chất dinh dưỡng hiệu quả, đồng thời cho não bộ đủ thời gian—thường là khoảng hai mươi phút—để tiếp nhận các hormone báo no do dạ dày giải phóng.\n\nHơn nữa, việc phát triển cách tiếp cận chánh niệm đối với ăn uống giúp con người phân biệt được giữa đói cảm xúc và đói thể chất. Cơn đói cảm xúc ập đến bất ngờ, đòi hỏi sự thỏa mãn tức thì thông qua các món ăn nhiều đường hoặc thực phẩm chế biến sẵn để giải tỏa trong những lúc căng thẳng hoặc buồn chán. Ngược lại, cơn đói thể chất thực sự phát triển dần dần và có thể được thỏa mãn bởi nhiều loại thực phẩm nguyên phần bổ dưỡng. Nhận biết được sự khác biệt này giúp ngăn ngừa cảm giác tội lỗi và trao quyền cho mỗi người xây dựng một mối quan hệ tích cực, bền vững với dinh dưỡng.\n\nÁp dụng ăn uống chánh niệm không đòi hỏi chế độ ăn kiêng nghiêm ngặt hay phải đếm từng calo. Những điều chỉnh lối sống đơn giản, chẳng hạn như ngồi vào bàn ăn đàng hoàng, đặt thìa dĩa xuống giữa các lần nhai và thưởng thức trọn vẹn hương vị độc đáo của những bữa cơm nhà nấu, có thể cải thiện đáng kể hệ tiêu hóa và sức khỏe tinh thần. Bằng cách coi mỗi bữa ăn như một khoảng dừng có chủ đích thay vì một việc vặt, chúng ta kết nối lại với sức mạnh nuôi dưỡng của thực phẩm lành mạnh.",
        "keyVocab": [
            {
                "word": "distraction",
                "ipa": "/dɪˈstræk.ʃən/",
                "meaning": "sự xao nhãng, mất tập trung"
            },
            {
                "word": "antidote",
                "ipa": "/ˈæn.t̬i.doʊt/",
                "meaning": "liều thuốc giải, giải pháp khắc phục"
            },
            {
                "word": "satiety",
                "ipa": "/səˈtaɪ.ə.t̬i/",
                "meaning": "cảm giác no bụng, thỏa mãn"
            },
            {
                "word": "emotional hunger",
                "ipa": "/ɪˈmoʊ.ʃən.əl ˈhʌŋ.ɡɚ/",
                "meaning": "cơn đói do cảm xúc (buồn, stress) gây ra"
            },
            {
                "word": "sustainable",
                "ipa": "/səˈsteɪ.nə.bəl/",
                "meaning": "bền vững, duy trì lâu dài"
            }
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
    {
        "id": "read-24",
        "title": "Hotel Check-In & Requesting Room Amenities",
        "type": "conversation",
        "topic": "Du lịch & Khách sạn",
        "level": "B1 - B2",
        "summary": "Cuộc đối thoại tại quầy lễ tân khách sạn khi khách làm thủ tục nhận phòng, yêu cầu phòng tầng cao yên tĩnh và tìm hiểu dịch vụ xe đưa đón.",
        "content": [
            {
                "speaker": "Marcus (Male / Front Desk)",
                "text": "Good evening! Welcome to the Grand Horizon Hotel. How may I assist you this evening?"
            },
            {
                "speaker": "Emma (Female / Guest)",
                "text": "Good evening. I have a reservation under the name Emma Watson for three nights."
            },
            {
                "speaker": "Marcus (Male / Front Desk)",
                "text": "Thank you, Ms. Watson. Let me pull up your booking in our reservation system. Yes, here it is: a Deluxe King room with city views, including daily breakfast."
            },
            {
                "speaker": "Emma (Female / Guest)",
                "text": "That is correct. If possible, could I request a room on a higher floor away from the elevator? I am a light sleeper and have an early conference tomorrow."
            },
            {
                "speaker": "Marcus (Male / Front Desk)",
                "text": "Certainly! We have a quiet corner room available on the fourteenth floor that faces the internal courtyard. It should ensure an uninterrupted night of rest."
            },
            {
                "speaker": "Emma (Female / Guest)",
                "text": "That sounds perfect! What time is breakfast served in the morning, and where is the restaurant located?"
            },
            {
                "speaker": "Marcus (Male / Front Desk)",
                "text": "Breakfast is served from 6:30 AM to 10:30 AM in the Terrace Bistro on the second floor. We offer both a continental buffet and made-to-order omelets."
            },
            {
                "speaker": "Emma (Female / Guest)",
                "text": "Wonderful. Also, does the hotel provide a complimentary shuttle service to the international airport on Wednesday?"
            },
            {
                "speaker": "Marcus (Male / Front Desk)",
                "text": "Yes, our airport shuttle departs every hour on the hour. You can reserve your seat with the concierge desk at least three hours before departure."
            },
            {
                "speaker": "Emma (Female / Guest)",
                "text": "Thank you so much for your attentive help, Marcus. I really appreciate it."
            },
            {
                "speaker": "Marcus (Male / Front Desk)",
                "text": "It is my absolute pleasure, Ms. Watson. Here are your room keys and Wi-Fi password. Enjoy your stay with us!"
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Marcus (Nam / Lễ tân):** Chào buổi tối! Chào mừng quý khách đến với Khách sạn Grand Horizon. Tôi có thể hỗ trợ gì cho quý khách tối nay ạ?\n\n- **Emma (Nữ / Khách lưu trú):** Chào anh. Tôi có đặt phòng dưới tên Emma Watson cho ba đêm.\n\n- **Marcus (Nam / Lễ tân):** Cảm ơn cô Watson. Để tôi mở thông tin đặt phòng trên hệ thống. Vâng, đây rồi ạ: một phòng Deluxe King hướng thành phố, bao gồm bữa sáng hàng ngày.\n\n- **Emma (Nữ / Khách lưu trú):** Đúng rồi anh. Nếu được, tôi có thể xin một phòng ở tầng cao và cách xa thang máy không? Tôi rất khó ngủ và ngày mai có buổi hội thảo sớm.\n\n- **Marcus (Nam / Lễ tân):** Chắc chắn rồi ạ! Chúng tôi còn một phòng góc rất yên tĩnh ở tầng 14 hướng ra sân vườn nội khu. Phòng này sẽ đảm bảo cho cô một giấc ngủ ngon không bị quấy rầy.\n\n- **Emma (Nữ / Khách lưu trú):** Nghe tuyệt quá! Bữa sáng phục vụ từ mấy giờ vào buổi sáng và nhà hàng ở đâu vậy anh?\n\n- **Marcus (Nam / Lễ tân):** Bữa sáng phục vụ từ 6:30 đến 10:30 sáng tại Nhà hàng Terrace Bistro ở tầng 2. Chúng tôi có cả tiệc buffet kiểu Âu và quầy trứng chiên làm theo yêu cầu.\n\n- **Emma (Nữ / Khách lưu trú):** Tuyệt vời. Thêm nữa, khách sạn mình có dịch vụ xe buýt miễn phí đưa ra sân bay quốc tế vào thứ Tư không anh?\n\n- **Marcus (Nam / Lễ tân):** Dạ có ạ, xe buýt đưa đón sân bay khởi hành vào đầu mỗi tiếng. Cô có thể đăng ký giữ chỗ tại quầy hỗ trợ khách hàng trước giờ khởi hành ít nhất 3 tiếng.\n\n- **Emma (Nữ / Khách lưu trú):** Cảm ơn sự hỗ trợ rất chu đáo của anh nhé, Marcus. Tôi rất cảm kích.\n\n- **Marcus (Nam / Lễ tân):** Đó là niềm vinh hạnh của tôi, thưa cô Watson. Đây là thẻ phòng và mật khẩu Wi-Fi. Chúc cô có kỳ nghỉ thật thoải mái tại khách sạn!",
        "keyVocab": [
            {
                "word": "reservation",
                "ipa": "/ˌrez.ɚˈveɪ.ʃən/",
                "meaning": "sự đặt phòng/chỗ trước"
            },
            {
                "word": "amenity",
                "ipa": "/əˈmen.ə.t̬i/",
                "meaning": "tiện nghi, dịch vụ kèm theo"
            },
            {
                "word": "light sleeper",
                "ipa": "/laɪt ˈsliː.pɚ/",
                "meaning": "người thính ngủ, dễ bị đánh thức"
            },
            {
                "word": "complimentary",
                "ipa": "/ˌkɑːm.pləˈmen.t̬ɚ.i/",
                "meaning": "miễn phí (dịch vụ kèm theo)"
            },
            {
                "word": "concierge",
                "ipa": "/koʊn.siˈerʒ/",
                "meaning": "nhân viên hỗ trợ thông tin và dịch vụ khách hàng"
            }
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
    {
        "id": "read-25",
        "title": "How Remote Work is Transforming City Life",
        "type": "passage",
        "topic": "Công nghệ & Xã hội",
        "level": "B1 - B2",
        "summary": "Bài đọc phân tích xu hướng làm việc từ xa (remote work) và mô hình kết hợp (hybrid), tác động đến giao thông, nhà ở và kinh tế địa phương.",
        "content": "Over the past decade, the rapid advancement of cloud computing and high-speed fiber internet has reshaped modern employment. What began as a temporary measure during global emergencies has evolved into a permanent structural shift known as remote and hybrid work. Today, millions of knowledge workers across the globe no longer commute to downtown office towers five days a week. Instead, they divide their workweek between home offices, local shared workspaces, and periodic corporate meetings.\n\nThis shift has produced profound consequences for urban geography. For decades, major metropolises were designed around the assumption that workers would travel into central business districts every morning and leave every evening. Consequently, commercial centers boasted dense concentrations of coffee shops, restaurants, and retail stores catering strictly to daytime office workers. With lower daily foot traffic, downtown businesses have had to reinvent themselves, while residential suburban neighborhoods are experiencing a vibrant revitalization as residents spend more money close to home.\n\nMoreover, the flexibility of working from anywhere has encouraged many young families to relocate from cramped metropolitan apartments to spacious suburban or rural towns. When daily physical presence in an office is no longer mandatory, affordable housing, larger backyards, and access to nature become far more appealing than a short commute. Small towns that once struggled with population decline are now attracting skilled digital professionals, which stimulates local economies and tax revenues.\n\nNevertheless, remote work poses distinct organizational challenges. Team leaders must adopt structured communication tools to prevent employee isolation and maintain creative collaboration. Establishing clear boundaries between professional responsibilities and personal life is equally critical, as home workers frequently struggle to disconnect after business hours. Overall, finding an equitable balance between digital flexibility and in-person connection will define the future of sustainable workplace culture.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nTrong thập kỷ qua, sự phát triển vượt bậc của điện toán đám mây và internet cáp quang tốc độ cao đã định hình lại việc làm hiện đại. Điều ban đầu vốn là giải pháp tạm thời trong các tình huống khẩn cấp toàn cầu nay đã tiến hóa thành một sự thay đổi cấu trúc lâu dài được gọi là làm việc từ xa và làm việc kết hợp (hybrid). Ngày nay, hàng triệu lao động tri thức trên toàn cầu không còn phải di chuyển vào các tòa tháp văn phòng trung tâm năm ngày một tuần. Thay vào đó, họ phân chia tuần làm việc giữa góc làm việc tại nhà, các không gian làm việc chung tại địa phương và những buổi họp trực tiếp định kỳ tại công ty.\n\nSự thay đổi này đã mang lại những hệ quả sâu sắc đối với địa lý đô thị. Trong nhiều thập kỷ, các đại đô thị được thiết kế dựa trên giả định rằng người lao động sẽ đổ xô vào các quận thương mại trung tâm mỗi sáng và rời đi vào mỗi tối. Do đó, các khu trung tâm thương mại từng tập trung dày đặc các quán cà phê, nhà hàng và cửa hàng bán lẻ chỉ phục vụ riêng cho dân văn phòng vào ban ngày. Khi lượng người đi lại hàng ngày giảm đi, các doanh nghiệp trung tâm buộc phải tự làm mới mình, trong khi các khu dân cư ngoại ô lại đón nhận sự hồi sinh sôi động khi người dân chi tiêu nhiều tiền hơn gần nhà.\n\nHơn nữa, sự linh hoạt khi có thể làm việc từ bất cứ đâu đã khuyến khích nhiều gia đình trẻ chuyển từ các căn hộ chật chội ở thành phố lớn về các thị trấn ngoại ô hoặc nông thôn rộng rãi hơn. Khi việc có mặt trực tiếp mỗi ngày ở văn phòng không còn là bắt buộc, nhà ở giá cả phải chăng, sân vườn rộng hơn và khả năng tiếp cận thiên nhiên trở nên hấp dẫn hơn nhiều so với việc chỉ để tiết kiệm thời gian đi làm. Những thị trấn nhỏ từng đối mặt với sự suy giảm dân số giờ đây lại thu hút các chuyên gia kỹ thuật số có tay nghề, giúp kích thích kinh tế và nguồn thu thuế địa phương.\n\nTuy nhiên, làm việc từ xa cũng đặt ra những thách thức đáng kể về mặt tổ chức. Các nhà lãnh đạo đội ngũ phải áp dụng các công cụ giao tiếp có cấu trúc để ngăn ngừa tình trạng nhân viên bị cô lập và duy trì sự hợp tác sáng tạo. Việc thiết lập ranh giới rõ ràng giữa trách nhiệm công việc và cuộc sống cá nhân cũng mang tính sống còn không kém, bởi những người làm việc tại nhà thường gặp khó khăn trong việc ngắt kết nối sau giờ làm. Nhìn chung, việc tìm kiếm sự cân bằng công bằng giữa tính linh hoạt kỹ thuật số và sự kết nối trực tiếp sẽ định hình tương lai của văn hóa làm việc bền vững.",
        "keyVocab": [
            {
                "word": "hybrid work",
                "ipa": "/ˈhaɪ.brɪd wɝːk/",
                "meaning": "mô hình làm việc kết hợp giữa tại nhà và tại văn phòng"
            },
            {
                "word": "revitalization",
                "ipa": "/ˌriːˌvaɪ.t̬əl.əˈzeɪ.ʃən/",
                "meaning": "sự hồi sinh, tái sinh sức sống"
            },
            {
                "word": "relocate",
                "ipa": "/ˌriːˈloʊ.keɪt/",
                "meaning": "chuyển địa điểm sinh sống hoặc làm việc"
            },
            {
                "word": "isolation",
                "ipa": "/ˌaɪ.səˈleɪ.ʃən/",
                "meaning": "sự cô lập, cảm giác tách biệt"
            },
            {
                "word": "equitable",
                "ipa": "/ˈek.wə.t̬ə.bəl/",
                "meaning": "công bằng, hợp lý"
            }
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
    {
        "id": "read-26",
        "title": "At the Doctor's Office: Describing Symptoms & Medical Advice",
        "type": "conversation",
        "topic": "Sức khỏe & Y tế",
        "level": "B1 - B2",
        "summary": "Cuộc khám bệnh giữa bác sĩ gia đình và bệnh nhân bị ho kéo dài, sốt nhẹ và mệt mỏi sau khi chuyển mùa.",
        "content": [
            {
                "speaker": "Dr. Arthur (Male / Physician)",
                "text": "Good morning, Maya. Come on in and have a seat. What brings you into the clinic today?"
            },
            {
                "speaker": "Maya (Female / Patient)",
                "text": "Good morning, Dr. Arthur. I have not been feeling well for the past four days. I have a persistent dry cough, a mild fever, and a sore throat."
            },
            {
                "speaker": "Dr. Arthur (Male / Physician)",
                "text": "I see. Have you experienced any shortness of breath, chest tightness, or chills during the night?"
            },
            {
                "speaker": "Maya (Female / Patient)",
                "text": "No difficulty breathing, but I feel unusually fatigued, and my muscles ache after normal walking."
            },
            {
                "speaker": "Dr. Arthur (Male / Physician)",
                "text": "Let me check your vital signs. Your temperature is thirty-eight point two degrees Celsius, and your oxygen saturation is ninety-nine percent, which is reassuring. Now, let me listen to your lungs. Please take a deep breath through your mouth."
            },
            {
                "speaker": "Maya (Female / Patient)",
                "text": "(Breathes deeply) How do my lungs sound, Doctor?"
            },
            {
                "speaker": "Dr. Arthur (Male / Physician)",
                "text": "Your lungs sound completely clear—no wheezing or fluid congestion. It appears to be an acute viral upper respiratory infection, commonly known as a seasonal flu."
            },
            {
                "speaker": "Maya (Female / Patient)",
                "text": "Do I need to take antibiotics to clear this up?"
            },
            {
                "speaker": "Dr. Arthur (Male / Physician)",
                "text": "No, antibiotics only target bacterial infections and are ineffective against viruses. Taking them unnecessarily can disrupt your gut flora and cause resistance. Instead, I recommend plenty of bed rest, warm fluids, and paracetamol for the fever and body aches."
            },
            {
                "speaker": "Maya (Female / Patient)",
                "text": "Understood. Should I stay home from work for a few days?"
            },
            {
                "speaker": "Dr. Arthur (Male / Physician)",
                "text": "Yes, I will write you a medical certificate for three days of rest. If your fever persists beyond five days or you develop chest pain, please return immediately for a follow-up."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Bác sĩ Arthur (Nam / Bác sĩ):** Chào buổi sáng, Maya. Mời cô vào phòng và ngồi xuống. Hôm nay có vấn đề gì khiến cô phải đến phòng khám vậy?\n\n- **Maya (Nữ / Bệnh nhân):** Chào bác sĩ Arthur. Bốn ngày nay tôi thấy không được khỏe. Tôi bị ho khan kéo dài, sốt nhẹ và đau rát họng.\n\n- **Bác sĩ Arthur (Nam / Bác sĩ):** Tôi hiểu rồi. Cô có thấy khó thở, tức ngực hay bị ớn lạnh vào ban đêm không?\n\n- **Maya (Nữ / Bệnh nhân):** Dạ không khó thở, nhưng tôi cảm thấy mệt mỏi bất thường và các cơ bắp bị nhức mỏi dù chỉ đi bộ bình thường.\n\n- **Bác sĩ Arthur (Nam / Bác sĩ):** Để tôi kiểm tra các chỉ số sinh tồn của cô nhé. Thân nhiệt của cô là 38,2 độ C, và độ bão hòa oxy là 99%, chỉ số này rất an tâm. Bây giờ, hãy để tôi nghe phổi của cô. Hãy hít một hơi thật sâu bằng miệng nhé.\n\n- **Maya (Nữ / Bệnh nhân):** (Hít sâu) Phổi của tôi nghe thế nào vậy bác sĩ?\n\n- **Bác sĩ Arthur (Nam / Bác sĩ):** Phổi của cô rất trong—không có tiếng khò khè hay ứ dịch. Có vẻ đây là tình trạng nhiễm trùng đường hô hấp trên cấp tính do virus, thường gọi là cảm cúm theo mùa.\n\n- **Maya (Nữ / Bệnh nhân):** Tôi có cần uống thuốc kháng sinh để khỏi dứt điểm không bác sĩ?\n\n- **Bác sĩ Arthur (Nam / Bác sĩ):** Không nên đâu cô, thuốc kháng sinh chỉ tiêu diệt vi khuẩn và hoàn toàn không có tác dụng đối với virus. Uống kháng sinh không cần thiết có thể làm rối loạn hệ vi sinh đường ruột và gây kháng thuốc. Thay vào đó, tôi khuyên cô nên nghỉ ngơi nhiều trên giường, uống nhiều nước ấm và dùng paracetamol để hạ sốt và giảm đau mỏi cơ.\n\n- **Maya (Nữ / Bệnh nhân):** Tôi hiểu rồi ạ. Tôi có nên xin nghỉ làm ở nhà vài hôm không?\n\n- **Bác sĩ Arthur (Nam / Bác sĩ):** Có chứ, tôi sẽ viết giấy nghỉ ốm cho cô trong 3 ngày để nghỉ ngơi. Nếu cơn sốt kéo dài quá 5 ngày hoặc cô thấy đau ngực, hãy quay lại tái khám ngay nhé.",
        "keyVocab": [
            {
                "word": "persistent",
                "ipa": "/pɚˈsɪs.tənt/",
                "meaning": "dai dẳng, kéo dài liên tục"
            },
            {
                "word": "vital signs",
                "ipa": "/ˈvaɪ.t̬əl saɪnz/",
                "meaning": "các chỉ số sinh tồn (mạch, huyết áp, nhiệt độ, oxy)"
            },
            {
                "word": "respiratory infection",
                "ipa": "/ˈres.pɚ.ə.tɔːr.i ɪnˈfek.ʃən/",
                "meaning": "nhiễm trùng đường hô hấp"
            },
            {
                "word": "ineffective",
                "ipa": "/ˌɪn.ɪˈfek.tɪv/",
                "meaning": "không có hiệu quả, vô hiệu"
            },
            {
                "word": "follow-up",
                "ipa": "/ˈfɑː.loʊ.ʌp/",
                "meaning": "tái khám, theo dõi tiếp theo"
            }
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
    {
        "id": "read-27",
        "title": "Smart Budgeting Tips for Young Professionals",
        "type": "passage",
        "topic": "Tài chính cá nhân",
        "level": "B1 - B2",
        "summary": "Bài đọc hướng dẫn quy tắc quản lý tài chính 50/30/20, xây dựng quỹ khẩn cấp và thiết lập thói quen chi tiêu thông minh cho người trẻ.",
        "content": "Entering the workforce and receiving a regular monthly salary is an exciting milestone for young adults. However, without deliberate financial planning, rising living costs and impulsive consumerism can rapidly deplete earnings. Many graduates discover that despite earning decent salaries, they live paycheck to paycheck, struggling to cover unexpected emergencies or make meaningful investments. Learning foundational personal finance habits early in one's career lays the groundwork for lasting peace of mind.\n\nA widely praised and practical budgeting framework is the 50/30/20 rule, popularized by financial educators. Under this straightforward formula, fifty percent of net after-tax income is allocated to essential needs, such as rent, utilities, groceries, and student loan payments. Thirty percent is dedicated to discretionary wants—dining out with friends, hobby supplies, entertainment subscriptions, and weekend leisure. The remaining twenty percent must be directed toward savings, debt elimination, and long-term investment vehicles.\n\nBefore exploring high-risk investment avenues such as equities or cryptocurrencies, financial planners unanimously recommend building a robust emergency fund. An emergency cushion consisting of three to six months of basic living expenses protects individuals against unforeseen setbacks, such as sudden medical bills, automotive breakdowns, or unexpected unemployment. Storing these funds in a high-yield savings account ensures that money remains immediately accessible while earning modest interest against inflation.\n\nUltimately, mastering personal finance is less about achieving extreme frugality and more about fostering intentionality. By tracking daily expenditures on mobile banking apps and automating recurring transfers to savings accounts on payday, young professionals build wealth effortlessly. Financial freedom does not mean denying yourself every pleasure; rather, it empowers you to make informed life decisions without the chronic burden of monetary distress.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nBước chân vào thị trường lao động và nhận được mức lương hàng tháng đều đặn là một cột mốc thú vị đối với những người trẻ tuổi. Tuy nhiên, nếu không có kế hoạch tài chính có chủ đích, chi phí sinh hoạt ngày càng tăng và chủ nghĩa tiêu dùng bốc đồng có thể nhanh chóng làm cạn kiệt thu nhập. Nhiều người mới tốt nghiệp nhận thấy rằng dù kiếm được mức lương khá, họ vẫn sống trong cảnh \"chờ lương từng tháng\", chật vật trang trải các trường hợp khẩn cấp bất ngờ hoặc không thể đầu tư có ý nghĩa. Học các thói quen tài chính cá nhân nền tảng từ sớm trong sự nghiệp sẽ đặt nền móng cho sự an tâm lâu dài.\n\nMột khuôn khổ lập ngân sách thực tế và được khen ngợi rộng rãi là quy tắc 50/30/20, được các chuyên gia giáo dục tài chính phổ biến. Theo công thức đơn giản này, 50% thu nhập ròng sau thuế được phân bổ cho các nhu cầu thiết yếu như tiền thuê nhà, điện nước, thực phẩm và các khoản trả nợ học phí. 30% dành cho những mong muốn sở thích—đi ăn ngoài với bạn bè, đồ dùng theo sở thích, các gói giải trí và thư giãn cuối tuần. 20% còn lại bắt buộc phải dành cho tiết kiệm, xóa nợ và các kênh đầu tư dài hạn.\n\nTrước khi tìm hiểu các kênh đầu tư rủi ro cao như cổ phiếu hay tiền kỹ thuật số, các nhà hoạch định tài chính đều đồng lòng khuyến nghị xây dựng một quỹ khẩn cấp vững chắc. Một chiếc đệm dự phòng khẩn cấp bao gồm 3 đến 6 tháng chi phí sinh hoạt cơ bản sẽ bảo vệ các cá nhân trước những biến cố khó lường, chẳng hạn như hóa đơn y tế đột xuất, hỏng xe hoặc thất nghiệp bất ngờ. Giữ số tiền này trong một tài khoản tiết kiệm lãi suất cao đảm bảo rằng tiền vẫn có thể sử dụng được ngay lập tức trong khi vẫn sinh lãi nhẹ để chống lạm phát.\n\nSuy cho cùng, việc làm chủ tài chính cá nhân không phải là hướng tới lối sống quá mức tằn tiện, mà là thúc đẩy tính có chủ đích. Bằng cách theo dõi các khoản chi tiêu hàng ngày trên ứng dụng ngân hàng di động và tự động hóa các khoản chuyển tiền định kỳ vào tài khoản tiết kiệm vào ngày nhận lương, những người đi làm trẻ tuổi có thể xây dựng sự giàu có một cách nhẹ nhàng. Tự do tài chính không có nghĩa là từ chối mọi niềm vui; đúng hơn, nó trao quyền cho bạn đưa ra những quyết định cuộc đời sáng suốt mà không phải chịu gánh nặng kinh niên của nỗi lo tiền bạc.",
        "keyVocab": [
            {
                "word": "impulsive",
                "ipa": "/ɪmˈpʌl.sɪv/",
                "meaning": "bốc đồng, ngẫu hứng không suy tính"
            },
            {
                "word": "paycheck to paycheck",
                "ipa": "/ˈpeɪ.tʃek tə ˈpeɪ.tʃek/",
                "meaning": "sống chật vật tháng nào xào hết tháng đó"
            },
            {
                "word": "discretionary",
                "ipa": "/dɪˈskreʃ.ən.er.i/",
                "meaning": "tùy ý, tự do quyết định (khoản chi không bắt buộc)"
            },
            {
                "word": "emergency fund",
                "ipa": "/ɪˈmɝː.dʒən.si fʌnd/",
                "meaning": "quỹ dự phòng tài chính khẩn cấp"
            },
            {
                "word": "frugality",
                "ipa": "/fruːˈɡæl.ə.t̬i/",
                "meaning": "lối sống tiết kiệm, thanh đạm"
            }
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
    {
        "id": "read-28",
        "title": "Dining Out: Ordering Food, Dietary Preferences & Settling the Bill",
        "type": "conversation",
        "topic": "Ẩm thực & Nhà hàng",
        "level": "B1 - B2",
        "summary": "Tình huống giao tiếp thực tế tại nhà hàng Ý: Gọi món khai vị, món chính, thông báo dị ứng đậu phộng và chia hóa đơn thanh toán.",
        "content": [
            {
                "speaker": "Julian (Male / Waiter)",
                "text": "Good evening and welcome to Bella Italia Bistro. Are you ready to order, or would you like a few more minutes to browse the menu?"
            },
            {
                "speaker": "Chloe (Female / Diner)",
                "text": "Good evening! We are ready to order. To start, could we get the bruschetta with heirloom tomatoes and fresh basil?"
            },
            {
                "speaker": "Julian (Male / Waiter)",
                "text": "An excellent choice. Our chef bakes the sourdough bread fresh every afternoon. And for your main courses?"
            },
            {
                "speaker": "Chloe (Female / Diner)",
                "text": "I would like the handmade seafood linguine with garlic and white wine sauce. However, my friend has a severe peanut and pine nut allergy. Does the basil pesto pasta contain any nuts?"
            },
            {
                "speaker": "Julian (Male / Waiter)",
                "text": "I am very glad you informed me. Yes, our traditional pesto contains crushed pine nuts. I will notify the kitchen immediately to prepare her dish separately to avoid cross-contamination, or she could try our wild mushroom risotto, which is completely nut-free."
            },
            {
                "speaker": "Chloe (Female / Diner)",
                "text": "The wild mushroom risotto sounds wonderful for her, thank you so much for being so vigilant."
            },
            {
                "speaker": "Julian (Male / Waiter)",
                "text": "You are very welcome. Would you care for any drinks to accompany your meal—perhaps a bottle of sparkling mineral water?"
            },
            {
                "speaker": "Chloe (Female / Diner)",
                "text": "Yes, a large bottle of sparkling water with lemon slices would be great."
            },
            {
                "speaker": "Julian (Male / Waiter)",
                "text": "(Later) Here is your bill whenever you are ready. Take your time, no rush at all."
            },
            {
                "speaker": "Chloe (Female / Diner)",
                "text": "Thank you, Julian. The food was exquisite! Could we split the bill evenly between two credit cards, and please include a fifteen percent gratuity for your exceptional service?"
            },
            {
                "speaker": "Julian (Male / Waiter)",
                "text": "Certainly, I can split that right here on the terminal. Thank you so much for dining with us tonight!"
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Julian (Nam / Nhân viên phục vụ):** Chào buổi tối và chào mừng quý khách đến với Bella Italia Bistro. Quý khách đã sẵn sàng gọi món chưa, hay muốn có thêm vài phút để xem thực đơn ạ?\n\n- **Chloe (Nữ / Thực khách):** Chào anh! Chúng tôi đã sẵn sàng gọi món rồi. Để khai vị, chúng tôi xin gọi món bánh mì nướng bruschetta cà chua và húng quế tươi nhé.\n\n- **Julian (Nam / Nhân viên phục vụ):** Một lựa chọn tuyệt vời ạ. Bếp trưởng của chúng tôi nướng bánh mì chua tươi vào mỗi buổi chiều. Còn về các món chính thì sao ạ?\n\n- **Chloe (Nữ / Thực khách):** Tôi muốn gọi món mì linguine hải sản thủ công sốt tỏi và rượu vang trắng. Tuy nhiên, bạn tôi bị dị ứng rất nặng với đậu phộng và hạt thông. Món mì sốt pesto húng quế có chứa hạt nào không anh?\n\n- **Julian (Nam / Nhân viên phục vụ):** Rất may là cô đã báo trước cho tôi biết. Vâng, sốt pesto truyền thống của chúng tôi có chứa hạt thông giã nhỏ. Tôi sẽ báo với bếp ngay lập tức để làm món ăn của cô ấy riêng biệt nhằm tránh nhiễm chéo, hoặc cô ấy có thể thử món cơm Ý risotto nấm rừng hoàn toàn không chứa các loại hạt.\n\n- **Chloe (Nữ / Thực khách):** Món risotto nấm rừng nghe rất hợp với bạn tôi, cảm ơn anh đã rất cẩn thận và chu đáo.\n\n- **Julian (Nam / Nhân viên phục vụ):** Không có chi ạ. Quý khách có muốn dùng đồ uống gì kèm bữa ăn không—ví dụ một chai nước khoáng có ga nhé?\n\n- **Chloe (Nữ / Thực khách):** Vâng, cho chúng tôi một chai nước khoáng có ga lớn kèm vài lát chanh tươi nhé.\n\n- **Julian (Nam / Nhân viên phục vụ):** (Lúc sau) Hóa đơn của quý khách đây ạ, quý khách cứ thư thả không cần vội đâu nhé.\n\n- **Chloe (Nữ / Thực khách):** Cảm ơn anh Julian. Đồ ăn ngon tuyệt vời! Chúng tôi có thể chia đôi hóa đơn này ra hai thẻ tín dụng không, và hãy tính thêm 15% tiền tip cho sự phục vụ xuất sắc của anh nhé?\n\n- **Julian (Nam / Nhân viên phục vụ):** Dạ chắc chắn rồi ạ, tôi có thể chia hóa đơn ngay trên máy quẹt thẻ cầm tay này. Cảm ơn quý khách rất nhiều vì đã dùng bữa tại nhà hàng tối nay!",
        "keyVocab": [
            {
                "word": "appetizer",
                "ipa": "/ˈæp.ə.taɪ.zɚ/",
                "meaning": "món khai vị"
            },
            {
                "word": "cross-contamination",
                "ipa": "/ˌkrɑːs kənˌtæm.əˈneɪ.ʃən/",
                "meaning": "sự lây nhiễm chéo (chất dị ứng giữa các món)"
            },
            {
                "word": "vigilant",
                "ipa": "/ˈvɪdʒ.əl.ənt/",
                "meaning": "cẩn trọng, cảnh giác, chu đáo"
            },
            {
                "word": "exquisite",
                "ipa": "/ɪkˈskwɪz.ɪt/",
                "meaning": "tuyệt hảo, tinh tế xuất sắc"
            },
            {
                "word": "gratuity",
                "ipa": "/ɡrəˈtuː.ə.t̬i/",
                "meaning": "tiền tip, tiền thưởng cho phục vụ"
            }
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
    {
        "id": "read-29",
        "title": "The Impact of Fast Fashion on the Environment",
        "type": "passage",
        "topic": "Môi trường & Tiêu dùng",
        "level": "B1 - B2",
        "summary": "Bài đọc khám phá mô hình thời trang nhanh, lượng rác thải dệt may khổng lồ và sự trỗi dậy của lối sống tiêu dùng thời trang bền vững.",
        "content": "The global fashion industry has undergone a radical transformation over the past three decades. Historically, apparel brands operated on four distinct seasonal cycles: spring, summer, autumn, and winter. Today, global retail giants operate on a micro-season model, releasing up to fifty-two micro-collections every single year. This business strategy, universally known as fast fashion, relies on mass-producing trendy garments rapidly at exceptionally low consumer prices, encouraging shoppers to treat clothes as disposable commodities.\n\nWhile fast fashion has democratized access to trendy styles, its environmental toll is catastrophic. The textile manufacturing process requires staggering quantities of natural resources. Producing a single pair of conventional cotton jeans consumes approximately seven thousand liters of clean fresh water. Furthermore, synthetic fabrics like polyester, nylon, and acrylic are derived from petroleum. Every time these synthetic garments are washed in household washing machines, they shed thousands of microscopic plastic fibers that bypass filtration systems and contaminate oceanic ecosystems.\n\nIn addition to water depletion and chemical pollution, fast fashion generates unprecedented mountains of solid waste. Consumers purchase sixty percent more clothing items today than they did in the year 2000, yet retain them for only half as long. Millions of tons of discarded synthetic clothes end up in municipal landfills or are dumped in fragile deserts in the Global South, where they take hundreds of years to decompose while releasing hazardous greenhouse gases.\n\nFortunately, a burgeoning counter-movement prioritizing sustainable and circular fashion is gaining momentum worldwide. Conscious consumers are increasingly embracing thrift shopping, clothes swapping, and renting formal outfits for special occasions. Moreover, innovative apparel startups are investing in eco-friendly fabrics, such as organic linen, recycled cotton, and plant-based leather alternatives. By choosing quality over quantity and repairing beloved garments rather than discarding them, consumers can significantly reduce their ecological footprint.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nNgành công nghiệp thời trang toàn cầu đã trải qua một cuộc chuyển đổi triệt để trong ba thập kỷ qua. Trong lịch sử, các thương hiệu may mặc hoạt động theo bốn chu kỳ mùa riêng biệt: xuân, hạ, thu và đông. Ngày nay, các người khổng lồ bán lẻ toàn cầu hoạt động theo mô hình \"vi mùa\", tung ra tới 52 bộ sưu tập nhỏ mỗi năm. Chiến lược kinh doanh này, được biết đến rộng rãi với tên gọi thời trang nhanh, dựa trên việc sản xuất hàng loạt các bộ trang phục bắt kịp xu hướng một cách thần tốc với mức giá người tiêu dùng đặc biệt thấp, khuyến khích người mua sắm coi quần áo như những món đồ dùng một lần.\n\nMặc dù thời trang nhanh đã phổ cập hóa cơ hội tiếp cận các phong cách hợp thời, cái giá phải trả đối với môi trường là vô cùng thảm khốc. Quy trình sản xuất dệt may đòi hỏi lượng tài nguyên thiên nhiên đáng kinh ngạc. Sản xuất một chiếc quần jean cotton truyền thống tiêu tốn khoảng 7.000 lít nước ngọt sạch. Hơn nữa, các loại vải tổng hợp như polyester, nylon và acrylic đều có nguồn gốc từ dầu mỏ. Mỗi khi những bộ quần áo tổng hợp này được giặt trong máy giặt gia đình, chúng rụng ra hàng ngàn sợi nhựa siêu nhỏ vượt qua hệ thống lọc và gây ô nhiễm các hệ sinh thái đại dương.\n\nBên cạnh việc cạn kiệt nguồn nước và ô nhiễm hóa chất, thời trang nhanh còn tạo ra những núi rác thải rắn chưa từng có. Người tiêu dùng ngày nay mua sắm nhiều quần áo hơn 60% so với năm 2000, nhưng chỉ giữ chúng trong thời gian ngắn bằng một nửa. Hàng triệu tấn quần áo tổng hợp bị vứt bỏ nằm tại các bãi rác đô thị hoặc bị đổ bừa bãi tại các sa mạc mỏng manh ở bán cầu Nam, nơi chúng phải mất hàng trăm năm để phân hủy trong khi liên tục giải phóng các loại khí nhà kính độc hại.\n\nMay mắn thay, một phong trào đối trọng đang phát triển ưu tiên thời trang bền vững và tuần hoàn đang lấy lại đà trên toàn thế giới. Những người tiêu dùng có ý thức đang ngày càng hào hứng với việc mua sắm đồ cũ (thrifting), trao đổi quần áo và thuê trang phục dạ hội cho các dịp đặc biệt. Hơn nữa, các công ty khởi nghiệp may mặc sáng tạo đang đầu tư vào các loại vải thân thiện với môi trường, chẳng hạn như vải lanh hữu cơ, cotton tái chế và các chất liệu da thay thế từ thực vật. Bằng cách chọn chất lượng thay vì số lượng và sửa chữa những bộ quần áo yêu quý thay vì vứt bỏ chúng, người tiêu dùng có thể giảm đáng kể dấu chân sinh thái của mình.",
        "keyVocab": [
            {
                "word": "commodity",
                "ipa": "/kəˈmɑː.də.t̬i/",
                "meaning": "hàng hóa, vật phẩm tiêu dùng"
            },
            {
                "word": "catastrophic",
                "ipa": "/ˌkæt̬.əˈstrɑː.fɪk/",
                "meaning": "thảm khốc, gây tai họa lớn"
            },
            {
                "word": "microfiber",
                "ipa": "/ˈmaɪ.kroʊˌfaɪ.bɚ/",
                "meaning": "vi sợi nhựa (rụng ra từ vải tổng hợp)"
            },
            {
                "word": "landfill",
                "ipa": "/ˈlænd.fɪl/",
                "meaning": "bãi chôn lấp rác thải"
            },
            {
                "word": "circular fashion",
                "ipa": "/ˈsɝː.kjə.lɚ ˈfæʃ.ən/",
                "meaning": "thời trang tuần hoàn (tái chế, tái sử dụng liên tục)"
            }
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
    {
        "id": "read-30",
        "title": "Tech Support: Troubleshooting Home Wi-Fi & Internet Issues",
        "type": "conversation",
        "topic": "Công nghệ & Đời sống",
        "level": "B1 - B2",
        "summary": "Cuộc gọi hỗ trợ kỹ thuật xử lý sự cố mạng Internet gia đình bị chập chờn, kiểm tra modem và đổi kênh tần số Wi-Fi.",
        "content": [
            {
                "speaker": "Daniel (Male / Support Agent)",
                "text": "Thank you for calling Apex Fiber Customer Support. My name is Daniel. May I have your account number and registered name, please?"
            },
            {
                "speaker": "Sarah (Female / Customer)",
                "text": "Hello Daniel. My account number is AF-84920, and my name is Sarah Jenkins. I am calling because my Wi-Fi keeps disconnecting every twenty minutes, which makes working from home impossible."
            },
            {
                "speaker": "Daniel (Male / Support Agent)",
                "text": "I completely understand how frustrating that must be, Ms. Jenkins. Let me run a diagnostic test on your optical terminal from our system. Could you take a quick look at your router and tell me what the indicator lights look like?"
            },
            {
                "speaker": "Sarah (Female / Customer)",
                "text": "Sure. The power light is solid green, but the internet globe symbol is flashing amber intermittently."
            },
            {
                "speaker": "Daniel (Male / Support Agent)",
                "text": "That indicates a signal synchronization drop between the router and our neighborhood exchange. First, let us perform a complete power cycle. Could you unplug the power cord from the back of the modem?"
            },
            {
                "speaker": "Sarah (Female / Customer)",
                "text": "Okay, I have unplugged it. How long should I leave it disconnected?"
            },
            {
                "speaker": "Daniel (Male / Support Agent)",
                "text": "Please leave it unplugged for thirty full seconds to allow all residual electrical charge in the capacitors to dissipate. After that, plug it back in firmly."
            },
            {
                "speaker": "Sarah (Female / Customer)",
                "text": "(After thirty seconds) Okay, I just plugged it back in. The lights are cycling through red, amber, and now turning solid blue."
            },
            {
                "speaker": "Daniel (Male / Support Agent)",
                "text": "Solid blue means the high-speed fiber connection has synchronized properly. I also noticed on my diagnostic screen that your router was operating on a crowded 2.4 GHz channel. I have just remotely switched your primary network to the 5 GHz band, which offers significantly less interference."
            },
            {
                "speaker": "Sarah (Female / Customer)",
                "text": "Let me test it on my laptop right now. Wow, the speed test shows ninety-five megabits per second, and my video conference reconnected immediately!"
            },
            {
                "speaker": "Daniel (Male / Support Agent)",
                "text": "That is fantastic news. If the connection drops again over the next forty-eight hours, your ticket remains open, and we will dispatch a field technician at no charge."
            },
            {
                "speaker": "Sarah (Female / Customer)",
                "text": "You have been tremendously helpful, Daniel. Thank you so much for resolving this so promptly!"
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Cảm ơn quý khách đã gọi đến Tổng đài Hỗ trợ Khách hàng Apex Fiber. Tôi tên là Daniel. Tôi có thể xin số tài khoản và tên đăng ký của quý khách được không ạ?\n\n- **Sarah (Nữ / Khách hàng):** Chào Daniel. Số tài khoản của tôi là AF-84920, tên tôi là Sarah Jenkins. Tôi gọi vì mạng Wi-Fi nhà tôi cứ 20 phút lại bị ngắt kết nối một lần, khiến tôi không thể nào làm việc tại nhà được.\n\n- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Tôi hoàn toàn hiểu sự bất tiện khó chịu đó, cô Jenkins. Để tôi chạy bài kiểm tra chẩn đoán trên thiết bị đầu cuối cáp quang của cô từ hệ thống. Cô có thể nhìn nhanh vào modem Wi-Fi và cho tôi biết các đèn báo đang hiển thị thế nào không ạ?\n\n- **Sarah (Nữ / Khách hàng):** Được rồi. Đèn nguồn đang sáng xanh liên tục, nhưng biểu tượng quả địa cầu internet thì thỉnh thoảng lại nhấp nháy màu vàng cam.\n\n- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Dấu hiệu đó cho thấy việc mất đồng bộ tín hiệu giữa modem và trạm phát khu vực của chúng tôi. Trước tiên, chúng ta hãy thử khởi động lại nguồn hoàn toàn nhé. Cô có thể rút dây nguồn ở phía sau modem ra không ạ?\n\n- **Sarah (Nữ / Khách hàng):** Được rồi, tôi đã rút dây ra rồi. Tôi nên để ngắt điện trong bao lâu?\n\n- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Cô hãy để ngắt điện trong đủ 30 giây để toàn bộ điện tích dư trong các tụ điện được xả hết. Sau đó, hãy cắm lại thật chặt nhé.\n\n- **Sarah (Nữ / Khách hàng):** (Sau 30 giây) Được rồi, tôi vừa cắm lại rồi. Các đèn đang chuyển từ đỏ, vàng cam và giờ đã chuyển sang màu xanh lam sáng ổn định.\n\n- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Đèn xanh lam ổn định có nghĩa là kết nối cáp quang tốc độ cao đã đồng bộ chuẩn xác. Tôi cũng nhận thấy trên màn hình chẩn đoán rằng modem của cô trước đó chạy trên kênh 2.4 GHz bị nghẽn sóng. Tôi vừa chuyển từ xa mạng chính của cô sang băng tần 5 GHz, băng tần này ít bị nhiễu sóng hơn rất nhiều.\n\n- **Sarah (Nữ / Khách hàng):** Để tôi thử ngay trên máy tính xách tay nhé. Tuyệt quá, bài kiểm tra tốc độ đạt tới 95 Mbps và cuộc gọi video họp trực tuyến của tôi đã kết nối lại ngay lập tức!\n\n- **Daniel (Nam / Nhân viên hỗ trợ kỹ thuật):** Thật là tin tuyệt vời. Nếu kết nối lại chập chờn trong 48 giờ tới, phiếu hỗ trợ của cô vẫn được mở và chúng tôi sẽ cử kỹ thuật viên đến tận nhà kiểm tra miễn phí.\n\n- **Sarah (Nữ / Khách hàng):** Anh đã giúp đỡ tôi vô cùng nhiệt tình, Daniel. Cảm ơn anh rất nhiều vì đã xử lý nhanh chóng như vậy!",
        "keyVocab": [
            {
                "word": "troubleshoot",
                "ipa": "/ˈtrʌb.əl.ʃuːt/",
                "meaning": "khắc phục sự cố kỹ thuật"
            },
            {
                "word": "intermittently",
                "ipa": "/ˌɪn.t̬ɚˈmɪt.ənt.li/",
                "meaning": "chập chờn, ngắt quãng lúc có lúc không"
            },
            {
                "word": "power cycle",
                "ipa": "/ˈpaʊ.ɚ ˌsaɪ.kəl/",
                "meaning": "khởi động lại thiết bị bằng cách tắt bật nguồn"
            },
            {
                "word": "interference",
                "ipa": "/ˌɪn.t̬ɚˈfɪr.əns/",
                "meaning": "sự can nhiễu sóng tín hiệu"
            },
            {
                "word": "dispatch",
                "ipa": "/dɪˈspætʃ/",
                "meaning": "điều phối, cử nhân viên đi làm nhiệm vụ"
            }
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
    {
        "id": "read-31",
        "title": "Effective Strategies for Learning a Second Language",
        "type": "passage",
        "topic": "Học tập & Kỹ năng",
        "level": "B1 - B2",
        "summary": "Bài đọc tổng hợp các phương pháp khoa học giúp người học tiếp thu ngoại ngữ hiệu quả: lặp lại ngắt quãng, tạo môi trường đắm chìm và không sợ mắc lỗi.",
        "content": "Acquiring a foreign language as an adult is frequently perceived as a daunting and tedious endeavor. Traditional classroom environments often emphasize rote memorization of grammatical rules, conjugation tables, and isolated vocabulary lists. Unfortunately, this rigid pedagogical method frequently results in students who can score high marks on written examinations but remain paralyzed with anxiety when attempting to hold a spontaneous conversation with native speakers. Modern cognitive neuroscience demonstrates that practical fluency requires a far more dynamic approach.\n\nA cornerstone of rapid vocabulary acquisition is spaced repetition systems (SRS). Human memory naturally decays along a predictable forgetting curve. If a newly learned word is reviewed immediately before the brain forgets it, neural pathways are reinforced and the memory is transferred into long-term storage. Rather than cramming hundreds of words the night before an exam, spending just fifteen minutes each day reviewing digital flashcards with intelligent spaced intervals achieves vastly superior retention with minimal mental fatigue.\n\nFurthermore, creating an immersive linguistic environment at home is essential for developing intuitive listening comprehension. Language learners do not need to purchase expensive plane tickets to immerse themselves in English. By switching smartphone operating systems to English, listening to conversational podcasts during daily commutes, and watching movies with English subtitles, learners continuously train their ears to recognize natural cadence, contractions, and authentic slang in meaningful contexts.\n\nAbove all, overcoming the fear of making mistakes is the single most critical psychological barrier to fluency. Language is primarily an instrument for human connection, not a performance test of grammatical perfection. Native speakers appreciate genuine communicative effort and rarely judge minor prepositions or tense slips. By embracing mistakes as valuable feedback rather than embarrassing failures, learners unlock confidence and achieve communicative fluency far more rapidly.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nViệc học một ngoại ngữ khi đã là người trưởng thành thường bị xem là một nỗ lực đầy nản lòng và tẻ nhạt. Môi trường lớp học truyền thống thường nhấn mạnh vào việc học vẹt các quy tắc ngữ pháp, bảng chia động từ và danh sách từ vựng rời rạc. Thật không may, phương pháp sư phạm cứng nhắc này thường tạo ra những học viên có thể đạt điểm cao trong các bài thi viết nhưng lại bị tê liệt vì lo lắng khi cố gắng trò chuyện tự nhiên với người bản xứ. Khoa học thần kinh nhận thức hiện đại chứng minh rằng sự lưu loát thực tế đòi hỏi một cách tiếp cận năng động hơn rất nhiều.\n\nMột nền tảng của việc tiếp thu từ vựng nhanh chóng là hệ thống lặp lại ngắt quãng (SRS). Trí nhớ con người tự nhiên suy giảm theo một đường cong lãng quên có thể dự đoán được. Nếu một từ mới học được ôn lại ngay trước khi não bộ chuẩn bị quên nó, các liên kết nơ-ron sẽ được củng cố và ký ức được chuyển vào bộ nhớ dài hạn. Thay vì nhồi nhét hàng trăm từ vào đêm trước kỳ thi, chỉ cần dành 15 phút mỗi ngày để ôn lại flashcard kỹ thuật số với các khoảng thời gian ngắt quãng thông minh sẽ đạt được khả năng ghi nhớ vượt trội với mức độ mệt mỏi tinh thần tối thiểu.\n\nHơn nữa, việc tạo ra một môi trường ngôn ngữ đắm chìm ngay tại nhà là điều cần thiết để phát triển khả năng nghe hiểu theo trực giác. Người học không cần phải mua vé máy bay đắt đỏ để có thể đắm chìm trong tiếng Anh. Bằng cách chuyển ngôn ngữ hệ điều hành điện thoại sang tiếng Anh, nghe podcast hội thoại trong khi đi làm hàng ngày và xem phim với phụ đề tiếng Anh, người học sẽ liên tục rèn luyện đôi tai nhận biết nhịp điệu tự nhiên, các từ rút gọn và tiếng lóng chân thực trong các ngữ cảnh có ý nghĩa.\n\nTrên hết, việc vượt qua nỗi sợ mắc lỗi chính là rào cản tâm lý quan trọng nhất trên con đường chinh phục sự lưu loát. Ngôn ngữ trước hết là một công cụ để kết nối giữa con người với nhau, chứ không phải một bài kiểm tra biểu diễn sự hoàn hảo về ngữ pháp. Người bản xứ trân trọng sự nỗ lực giao tiếp chân thành và hiếm khi để ý những lỗi nhỏ về giới từ hay thì động từ. Bằng cách đón nhận lỗi sai như những phản hồi quý giá thay vì những thất bại đáng xấu hổ, người học sẽ mở khóa sự tự tin và đạt được sự lưu loát trong giao tiếp nhanh hơn rất nhiều.",
        "keyVocab": [
            {
                "word": "daunting",
                "ipa": "/ˈdɑːn.t̬ɪŋ/",
                "meaning": "đầy thử thách, làm nản lòng"
            },
            {
                "word": "rote memorization",
                "ipa": "/roʊt ˌmem.ə.rəˈzeɪ.ʃən/",
                "meaning": "sự học vẹt, học thuộc lòng máy móc"
            },
            {
                "word": "spaced repetition",
                "ipa": "/speɪst ˌrep.əˈtɪʃ.ən/",
                "meaning": "phương pháp lặp lại ngắt quãng (khoa học ghi nhớ)"
            },
            {
                "word": "immersion",
                "ipa": "/ɪˈmɝː.ʃən/",
                "meaning": "sự đắm chìm, bao quanh hoàn toàn bằng ngôn ngữ"
            },
            {
                "word": "fluency",
                "ipa": "/ˈfluː.ən.si/",
                "meaning": "sự trôi chảy, lưu loát"
            }
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
    {
        "id": "read-32",
        "title": "Renting an Apartment: Lease Agreement & Utilities",
        "type": "conversation",
        "topic": "Đời sống & Nhà ở",
        "level": "B1 - B2",
        "summary": "Thương thảo hợp đồng thuê nhà giữa chủ nhà và người thuê: Thời hạn hợp đồng, tiền đặt cọc, chi phí tiện ích và quy định nuôi thú cưng.",
        "content": [
            {
                "speaker": "Richard (Male / Landlord)",
                "text": "Good afternoon, Olivia. Thank you for coming back for a second viewing of apartment 4B. What are your impressions after seeing the space during daylight?"
            },
            {
                "speaker": "Olivia (Female / Tenant)",
                "text": "Good afternoon, Mr. Richard. The natural light in the living room is wonderful, and the kitchen appliances look virtually brand new. I am definitely interested in leasing the apartment."
            },
            {
                "speaker": "Richard (Male / Landlord)",
                "text": "I am delighted to hear that. As mentioned earlier, our standard lease term is twelve months, beginning on the first of next month. The monthly rent is twelve hundred dollars, payable on the first day of each month."
            },
            {
                "speaker": "Olivia (Female / Tenant)",
                "text": "That fits my budget well. What are the upfront move-in costs, and what does the security deposit cover?"
            },
            {
                "speaker": "Richard (Male / Landlord)",
                "text": "Upon signing the lease, we require the first month's rent plus a security deposit equivalent to one month's rent. The security deposit is fully refundable at the end of the tenancy, provided there is no structural damage beyond standard wear and tear."
            },
            {
                "speaker": "Olivia (Female / Tenant)",
                "text": "That is completely fair. Are utility bills such as high-speed internet, water, and electricity included in the base rent?"
            },
            {
                "speaker": "Richard (Male / Landlord)",
                "text": "Water, trash collection, and building maintenance are included. However, electricity, gas for cooking, and fiber internet are billed separately in your own name."
            },
            {
                "speaker": "Olivia (Female / Tenant)",
                "text": "Good to know. Also, I have a small domestic cat who is quiet and well-trained. What is your policy regarding pets?"
            },
            {
                "speaker": "Richard (Male / Landlord)",
                "text": "We welcome cats and small dogs under fifteen kilograms. We just ask for a one-time non-refundable pet sanitation deposit of one hundred and fifty dollars."
            },
            {
                "speaker": "Olivia (Female / Tenant)",
                "text": "That sounds very reasonable. What documents do you need from me to proceed with the tenancy application?"
            },
            {
                "speaker": "Richard (Male / Landlord)",
                "text": "Please provide proof of employment, two recent pay stubs, and a copy of your government ID. Once approved, we can sign the lease electronically tomorrow!"
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Richard (Nam / Chủ nhà):** Chào buổi chiều, Olivia. Cảm ơn cô đã quay lại xem căn hộ 4B lần thứ hai. Cảm nhận của cô thế nào sau khi thấy không gian vào ban ngày?\n\n- **Olivia (Nữ / Người thuê nhà):** Chào buổi chiều, chú Richard. Ánh sáng tự nhiên trong phòng khách rất tuyệt vời, và các thiết bị nhà bếp trông gần như mới tinh. Cháu chắc chắn rất muốn thuê căn hộ này ạ.\n\n- **Richard (Nam / Chủ nhà):** Tôi rất mừng khi nghe điều đó. Như đã trao đổi trước đây, thời hạn hợp đồng tiêu chuẩn là 12 tháng, bắt đầu vào ngày mùng 1 tháng sau. Giá thuê hàng tháng là 1.200 đô la, thanh toán vào ngày đầu tiên của mỗi tháng.\n\n- **Olivia (Nữ / Người thuê nhà):** Mức giá đó rất phù hợp với ngân sách của cháu. Các chi phí ban đầu khi chuyển vào là gì, và khoản tiền đặt cọc đảm bảo bao gồm những gì ạ?\n\n- **Richard (Nam / Chủ nhà):** Khi ký hợp đồng, bên tôi yêu cầu thanh toán tiền thuê tháng đầu tiên cộng với tiền cọc tương đương một tháng tiền nhà. Tiền đặt cọc sẽ được hoàn trả toàn bộ khi hết hạn hợp đồng thuê, với điều kiện căn hộ không bị hư hỏng kết cấu vượt quá mức hao mòn thông thường.\n\n- **Olivia (Nữ / Người thuê nhà):** Dạ như vậy rất hợp lý. Các hóa đơn tiện ích như internet tốc độ cao, tiền nước và tiền điện đã bao gồm trong giá thuê gốc chưa ạ?\n\n- **Richard (Nam / Chủ nhà):** Tiền nước, phí thu gom rác và phí bảo trì tòa nhà đã được bao gồm. Tuy nhiên, tiền điện, gas nấu ăn và internet cáp quang sẽ tính riêng dưới tên của cô.\n\n- **Olivia (Nữ / Người thuê nhà):** Dạ cháu hiểu rồi. Thêm nữa, cháu có nuôi một bé mèo ta nhỏ rất ngoan và sạch sẽ. Quy định của tòa nhà về thú cưng như thế nào ạ?\n\n- **Richard (Nam / Chủ nhà):** Tòa nhà hoan nghênh mèo và chó nhỏ dưới 15 kg. Chúng tôi chỉ thu một khoản phí vệ sinh khử khuẩn thú cưng một lần không hoàn lại là 150 đô la.\n\n- **Olivia (Nữ / Người thuê nhà):** Dạ rất hợp lý ạ. Cháu cần cung cấp những giấy tờ gì để hoàn tất thủ tục đăng ký thuê nhà ạ?\n\n- **Richard (Nam / Chủ nhà):** Cô vui lòng cung cấp giấy xác nhận việc làm, hai phiếu lương gần nhất và bản sao giấy tờ tùy thân. Khi hồ sơ được duyệt, chúng ta có thể ký hợp đồng điện tử ngay ngày mai!",
        "keyVocab": [
            {
                "word": "lease agreement",
                "ipa": "/liːs əˈɡriː.mənt/",
                "meaning": "hợp đồng cho thuê nhà"
            },
            {
                "word": "security deposit",
                "ipa": "/səˈkjʊr.ə.t̬i dɪˌpɑː.zɪt/",
                "meaning": "tiền đặt cọc bảo đảm tài sản"
            },
            {
                "word": "wear and tear",
                "ipa": "/ˌwer ən ˈter/",
                "meaning": "sự hao mòn tự nhiên theo thời gian"
            },
            {
                "word": "utilities",
                "ipa": "/juːˈtɪl.ə.t̬iz/",
                "meaning": "các dịch vụ tiện ích thiết yếu (điện, nước, gas, internet)"
            },
            {
                "word": "refundable",
                "ipa": "/rɪˈfʌn.də.bəl/",
                "meaning": "có thể được hoàn lại tiền"
            }
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
    {
        "id": "read-33",
        "title": "The Rise of E-Commerce and Digital Payment Habits",
        "type": "passage",
        "topic": "Kinh tế & Xu hướng",
        "level": "B1 - B2",
        "summary": "Bài đọc phân tích sự bùng nổ của mua sắm trực tuyến, các ứng dụng ví điện tử và sự thay đổi trong hành vi tiêu dùng thời đại số.",
        "content": "The retail landscape has experienced an unprecedented revolution over the past two decades. Before the digital era, shopping was an inherently physical activity requiring consumers to travel to brick-and-mortar storefronts, wait in long cashier lines, and carry physical cash or paper checkbooks. Today, the ubiquity of smartphones and secure e-commerce platforms has transformed commerce into an instantaneous, frictionless experience accessible from anywhere with an internet connection.\n\nA fundamental catalyst of this commercial shift is the rapid adoption of digital wallets and contactless payment systems. Mobile applications like Apple Pay, Google Wallet, and regional digital payment services enable shoppers to finalize transactions with a simple fingerprint scan or facial recognition tap. For consumers, digital transactions offer speed, detailed automated expense tracking, and valuable cashback reward incentives. For merchants, eliminating paper currency reduces register theft, accelerates checkout throughput, and simplifies automated inventory reconciliation.\n\nFurthermore, artificial intelligence has fundamentally transformed digital product discovery. Modern e-commerce algorithms analyze previous browsing history, purchase frequency, and consumer demographic data to deliver personalized product recommendations. Rather than searching through endless catalogs, shoppers are presented with curated suggestions tailored precisely to their tastes. Combined with flexible return policies and expedited same-day delivery logistics, online shopping now rivals—and often exceeds—the convenience of traditional physical retail.\n\nHowever, this seamless purchasing convenience introduces new challenges. Financial psychologists caution that when physical currency is absent from transactions, the psychological \"pain of paying\" is diminished, making consumers significantly more vulnerable to impulsive spending. Furthermore, digital payment ecosystems require robust cybersecurity safeguards to defend against identity theft and fraudulent transactions. Balancing technological convenience with personal financial discipline remains essential in our increasingly cashless society.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nBối cảnh ngành bán lẻ đã trải qua một cuộc cách mạng chưa từng có trong hai thập kỷ qua. Trước kỷ nguyên số, mua sắm vốn dĩ là một hoạt động thể chất đòi hỏi người tiêu dùng phải di chuyển đến các cửa hàng vật lý truyền thống, xếp hàng dài chờ đợi thanh toán và mang theo tiền mặt hoặc sổ séc giấy. Ngày nay, sự phổ biến của điện thoại thông minh và các nền tảng thương mại điện tử bảo mật đã biến thương mại thành một trải nghiệm tức thì, mượt mà và có thể tiếp cận từ bất kỳ đâu chỉ cần có kết nối internet.\n\nMột chất xúc tác nền tảng của sự chuyển đổi thương mại này là việc áp dụng nhanh chóng các ví kỹ thuật số và hệ thống thanh toán không tiếp xúc. Các ứng dụng di động như Apple Pay, Google Wallet và các dịch vụ thanh toán kỹ thuật số khu vực cho phép người mua sắm hoàn tất giao dịch chỉ bằng một cái chạm quét vân tay hoặc nhận diện khuôn mặt. Đối với người tiêu dùng, giao dịch kỹ thuật số mang lại tốc độ, khả năng theo dõi chi tiêu tự động chi tiết và các ưu đãi hoàn tiền hấp dẫn. Đối với người bán, việc loại bỏ tiền giấy giúp giảm nguy cơ trộm cắp tại quầy thu ngân, tăng tốc độ thanh toán và đơn giản hóa việc đối soát hàng tồn kho tự động.\n\nHơn nữa, trí tuệ nhân tạo đã làm thay đổi căn bản cách khám phá sản phẩm kỹ thuật số. Các thuật toán thương mại điện tử hiện đại phân tích lịch sử duyệt web trước đó, tần suất mua hàng và dữ liệu nhân khẩu học của người tiêu dùng để đưa ra các đề xuất sản phẩm được cá nhân hóa. Thay vì phải tìm kiếm qua các danh mục vô tận, người mua sắm được hiển thị các gợi ý chọn lọc phù hợp chính xác với sở thích của họ. Kết hợp với chính sách đổi trả linh hoạt và dịch vụ hậu cần giao hàng nhanh trong ngày, mua sắm trực tuyến hiện nay cạnh tranh sòng phẳng—và thường vượt trội—về sự tiện lợi so với bán lẻ truyền thống.\n\nTuy nhiên, sự tiện lợi liền mạch này cũng mang đến những thách thức mới. Các nhà tâm lý học tài chính cảnh báo rằng khi tiền mặt vật lý vắng bóng trong các giao dịch, cảm giác tâm lý \"xót tiền khi chi trả\" sẽ giảm đi, khiến người tiêu dùng dễ bị tổn thương hơn trước những chi tiêu bốc đồng. Hơn nữa, các hệ sinh thái thanh toán kỹ thuật số đòi hỏi các biện pháp bảo vệ an ninh mạng vững chắc để chống lại việc đánh cắp danh tính và các giao dịch lừa đảo. Cân bằng giữa sự tiện lợi công nghệ với kỷ luật tài chính cá nhân vẫn là điều thiết yếu trong xã hội ngày càng không dùng tiền mặt của chúng ta.",
        "keyVocab": [
            {
                "word": "brick-and-mortar",
                "ipa": "/ˌbrɪk ən ˈmɔːr.t̬ɚ/",
                "meaning": "cửa hàng truyền thống có địa điểm vật lý thực tế"
            },
            {
                "word": "frictionless",
                "ipa": "/ˈfrɪk.ʃən.ləs/",
                "meaning": "mượt mà, không gặp trở ngại hay ma sát"
            },
            {
                "word": "cashback incentive",
                "ipa": "/ˈkæʃ.bæk ɪnˈsen.t̬ɪv/",
                "meaning": "ưu đãi hoàn tiền kích thích mua sắm"
            },
            {
                "word": "curated",
                "ipa": "/kjʊˈreɪ.t̬ɪd/",
                "meaning": "được tuyển chọn, chắt lọc kỹ lưỡng"
            },
            {
                "word": "cashless society",
                "ipa": "/ˈkæʃ.ləs səˈsaɪ.ə.t̬i/",
                "meaning": "xã hội không dùng tiền mặt"
            }
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
    {
        "id": "read-34",
        "title": "Planning a Company Team-Building Retreat",
        "type": "conversation",
        "topic": "Công sở & Sự kiện",
        "level": "B1 - B2",
        "summary": "Cuộc thảo luận lập kế hoạch dã ngoại gắn kết nhân viên giữa Trưởng phòng Nhân sự và Chuyên viên tổ chức sự kiện chuyên nghiệp.",
        "content": [
            {
                "speaker": "Brandon (Male / HR Manager)",
                "text": "Good morning, Clara. Thank you for meeting with me. Our leadership team wants to organize a two-day team-building retreat for our forty employees next month."
            },
            {
                "speaker": "Clara (Female / Event Planner)",
                "text": "Good morning, Brandon! That is fantastic. Team retreats are powerful tools for boosting morale and strengthening interdepartmental relationships. What primary objectives does leadership have in mind?"
            },
            {
                "speaker": "Brandon (Male / HR Manager)",
                "text": "Our engineering and marketing teams have been working remotely for over a year. We want a balanced itinerary that blends collaborative problem-solving workshops with relaxing outdoor activities where people can connect informally."
            },
            {
                "speaker": "Clara (Female / Event Planner)",
                "text": "Understood. I would recommend the Pine Valley Eco-Resort, located ninety minutes outside the city. It features modern conference halls equipped with audiovisual technology, alongside forest hiking trails and an outdoor barbecue pavilion."
            },
            {
                "speaker": "Brandon (Male / HR Manager)",
                "text": "That location sounds ideal. How do you propose structuring the agenda across the two days?"
            },
            {
                "speaker": "Clara (Female / Event Planner)",
                "text": "On Friday morning, we could hold an interactive company roadmap session followed by lunch. In the afternoon, we can conduct an outdoor scavenger hunt that requires cross-functional teamwork. The evening would be reserved for a casual campfire dinner."
            },
            {
                "speaker": "Brandon (Male / HR Manager)",
                "text": "I really like that sequence. What about Saturday morning?"
            },
            {
                "speaker": "Clara (Female / Event Planner)",
                "text": "Saturday morning can feature optional wellness workshops like morning yoga or a guided nature walk, followed by an open feedback retrospective before heading home after lunch."
            },
            {
                "speaker": "Brandon (Male / HR Manager)",
                "text": "Excellent. We have several team members with dietary restrictions—vegetarian, gluten-free, and halal. Can the resort cater to those needs?"
            },
            {
                "speaker": "Clara (Female / Event Planner)",
                "text": "Absolutely. The catering team specializes in customized dietary menus with labeled stations to prevent any cross-contact."
            },
            {
                "speaker": "Brandon (Male / HR Manager)",
                "text": "Terrific! Please send me a comprehensive cost breakdown and formal proposal by Thursday so I can present it to our financial director."
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Brandon (Nam / Trưởng phòng Nhân sự):** Chào buổi sáng, Clara. Cảm ơn cô đã dành thời gian gặp tôi. Ban lãnh đạo công ty chúng tôi muốn tổ chức một chuyến dã ngoại gắn kết đội ngũ 2 ngày cho 40 nhân viên vào tháng tới.\n\n- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Chào buổi sáng, anh Brandon! Thật tuyệt vời. Những chuyến dã ngoại đội ngũ là công cụ đắc lực để nâng cao tinh thần làm việc và thắt chặt mối quan hệ giữa các phòng ban. Ban lãnh đạo đang hướng tới những mục tiêu chính nào vậy anh?\n\n- **Brandon (Nam / Trưởng phòng Nhân sự):** Đội ngũ kỹ thuật và tiếp thị của chúng tôi đã làm việc từ xa hơn một năm nay. Chúng tôi muốn có một lịch trình cân bằng, kết hợp giữa các buổi hội thảo giải quyết vấn đề mang tính hợp tác với các hoạt động thư giãn ngoài trời để mọi người có thể kết nối thoải mái và thân mật.\n\n- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Tôi hiểu rồi. Tôi xin gợi ý Khu nghỉ dưỡng sinh thái Pine Valley, cách thành phố khoảng 90 phút đi xe. Nơi đây có các phòng hội nghị hiện đại trang bị đầy đủ công nghệ âm thanh ánh sáng, bên cạnh đó là những con đường mòn đi bộ xuyên rừng và khu vực tiệc nướng ngoài trời.\n\n- **Brandon (Nam / Trưởng phòng Nhân sự):** Địa điểm đó nghe rất lý tưởng. Cô đề xuất sắp xếp lịch trình trong hai ngày như thế nào?\n\n- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Vào sáng thứ Sáu, chúng ta có thể tổ chức buổi chia sẻ lộ trình phát triển công ty mang tính tương tác, sau đó là bữa trưa. Buổi chiều, chúng ta tổ chức trò chơi truy tìm kho báu ngoài trời đòi hỏi sự phối hợp liên phòng ban. Buổi tối sẽ dành cho bữa tiệc nướng lửa trại ấm cúng.\n\n- **Brandon (Nam / Trưởng phòng Nhân sự):** Tôi rất thích trình tự đó. Còn sáng thứ Bảy thì sao cô?\n\n- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Sáng thứ Bảy có thể có các hoạt động chăm sóc sức khỏe tự chọn như tập yoga buổi sáng hoặc đi bộ ngắm thiên nhiên có hướng dẫn, tiếp theo là buổi nhìn lại và đóng góp ý kiến cởi mở trước khi khởi hành về sau bữa trưa.\n\n- **Brandon (Nam / Trưởng phòng Nhân sự):** Tuyệt vời. Công ty chúng tôi có một số thành viên ăn kiêng—ăn chay, kiêng gluten và đồ ăn chuẩn Halal. Khu nghỉ dưỡng có thể đáp ứng được những thực đơn đó không?\n\n- **Clara (Nữ / Chuyên viên tổ chức sự kiện):** Chắc chắn được ạ. Đội ngũ ẩm thực ở đó chuyên phục vụ các thực đơn ăn kiêng tùy chỉnh với các quầy đồ ăn được gắn nhãn rõ ràng để tránh tiếp xúc chéo.\n\n- **Brandon (Nam / Trưởng phòng Nhân sự):** Quá tốt rồi! Cô vui lòng gửi cho tôi bảng dự toán chi phí chi tiết và bản đề xuất chính thức trước thứ Năm để tôi trình giám đốc tài chính nhé.",
        "keyVocab": [
            {
                "word": "retreat",
                "ipa": "/rɪˈtriːt/",
                "meaning": "chuyến dã ngoại, kỳ nghỉ dưỡng gắn kết tập thể"
            },
            {
                "word": "itinerary",
                "ipa": "/aɪˈtɪn.ə.rer.i/",
                "meaning": "lịch trình chi tiết chuyến đi"
            },
            {
                "word": "cross-functional",
                "ipa": "/ˌkrɑːs ˈfʌŋk.ʃən.əl/",
                "meaning": "liên phòng ban, đa chức năng"
            },
            {
                "word": "scavenger hunt",
                "ipa": "/ˈskæv.ən.dʒɚ hʌnt/",
                "meaning": "trò chơi truy tìm kho báu/đồ vật theo manh mối"
            },
            {
                "word": "retrospective",
                "ipa": "/ˌret.rəˈspek.tɪv/",
                "meaning": "buổi họp nhìn lại, đánh giá và rút kinh nghiệm"
            }
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
    {
        "id": "read-35",
        "title": "Daily Stress Management and Mental Well-being",
        "type": "passage",
        "topic": "Tâm lý & Đời sống",
        "level": "B1 - B2",
        "summary": "Bài đọc khám phá cơ chế sinh lý của căng thẳng (stress), tác hại của cortisol dư thừa và các phương pháp phục hồi năng lượng tinh thần hiệu quả.",
        "content": "Stress is an innate evolutionary survival mechanism designed to protect living organisms from acute physical hazards. When primitive ancestors encountered predatory threats, the human brain triggered an immediate physiological reaction known as the \"fight-or-flight\" response. Heart rates surged, blood pressure escalated, and stress hormones like adrenaline and cortisol flooded the bloodstream, temporarily diverting energy away from non-essential systems like digestion and immunity toward muscle activation.\n\nWhile this biological response remains vital for genuine physical crises, modern psychological stressors operate in an entirely different manner. Contemporary challenges—tight workplace deadlines, financial anxieties, and relentless digital notifications—are chronic rather than momentary. When the nervous system remains in a perpetual state of hyper-arousal, sustained elevated cortisol levels disrupt sleep architecture, impair immune defense, and foster chronic fatigue and cardiovascular strain.\n\nFortunately, clinical psychological research highlights several accessible practices that actively deactivate the physiological stress response. One of the most potent interventions is controlled diaphragmatic breathing, particularly the \"box breathing\" technique used by athletes and tactical specialists. By inhaling deeply for four seconds, holding for four, exhaling slowly for four, and pausing for four, the parasympathetic nervous system is stimulated, signaling the heart rate to decelerate and blood pressure to normalize within minutes.\n\nIn addition to conscious breathwork, cultivating regular digital detox intervals and engaging in physical movement in natural environments yield profound cognitive restoration. Spending just twenty minutes walking in an urban park or forest—a practice known in Japan as \"shinrin-yoku\" or forest bathing—significantly lowers salivary cortisol and restores depleted attention spans. Incorporating these intentional restorative rituals into daily routines ensures that individuals navigate modern pressures without compromising their long-term health and mental vitality.",
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\nCăng thẳng (stress) là một cơ chế sinh tồn tiến hóa bẩm sinh được thiết kế để bảo vệ các sinh vật sống khỏi những mối nguy hiểm thể chất cấp tính. Khi tổ tiên nguyên thủy đối mặt với các loài thú săn mồi đe dọa, bộ não con người lập tức kích hoạt một phản ứng sinh lý được gọi là phản ứng \"chiến đấu hay bỏ chạy\". Nhịp tim tăng vọt, huyết áp tăng cao, và các hormone gây căng thẳng như adrenaline và cortisol tràn vào máu, tạm thời chuyển hướng năng lượng khỏi các hệ thống không thiết yếu như tiêu hóa và miễn dịch để dồn cho sự kích hoạt cơ bắp.\n\nMặc dù phản ứng sinh học này vẫn mang tính sống còn đối với các cuộc khủng hoảng thể chất thực sự, những tác nhân gây căng thẳng tâm lý hiện đại lại hoạt động theo cách hoàn toàn khác. Những thách thức đương đại—hạn chót công việc gấp gáp, nỗi lo tài chính và những thông báo kỹ thuật số không ngừng nghỉ—mang tính chất kinh niên dai dẳng thay vì chỉ diễn ra trong chốc lát. Khi hệ thần kinh duy trì liên tục ở trạng thái kích động cao độ, mức cortisol tăng cao kéo dài sẽ phá vỡ cấu trúc giấc ngủ, làm suy giảm hệ miễn dịch và gây ra tình trạng mệt mỏi mạn tính cùng áp lực cho hệ tim mạch.\n\nMay mắn thay, các nghiên cứu tâm lý học lâm sàng chỉ ra một số phương pháp dễ tiếp cận có thể chủ động vô hiệu hóa phản ứng căng thẳng sinh lý này. Một trong những biện pháp can thiệp hiệu quả nhất là hít thở cơ hoành có kiểm soát, đặc biệt là kỹ thuật \"thở hộp\" được các vận động viên và chuyên gia tác chiến sử dụng. Bằng cách hít sâu trong 4 giây, giữ hơi trong 4 giây, thở ra từ từ trong 4 giây và dừng lại trong 4 giây, hệ thần kinh đối giao cảm sẽ được kích thích, phát tín hiệu cho nhịp tim chậm lại và huyết áp trở về mức bình thường chỉ trong vài phút.\n\nBên cạnh việc thở có ý thức, việc duy trì các khoảng thời gian cai nghiện kỹ thuật số định kỳ và vận động thể chất trong môi trường thiên nhiên mang lại sự phục hồi nhận thức sâu sắc. Chỉ cần dành 20 phút đi dạo trong công viên đô thị hoặc khu rừng—một phương pháp ở Nhật Bản gọi là \"tắm rừng\" (shinrin-yoku)—sẽ làm giảm đáng kể nồng độ cortisol trong nước bọt và phục hồi khả năng chú ý đang bị cạn kiệt. Việc kết hợp những nghi thức phục hồi có chủ đích này vào thói quen hàng ngày sẽ đảm bảo rằng mỗi người có thể vượt qua áp lực hiện đại mà không làm tổn hại đến sức khỏe lâu dài và sức sống tinh thần.",
        "keyVocab": [
            {
                "word": "fight-or-flight",
                "ipa": "/ˌfaɪt ɔːr ˈflaɪt/",
                "meaning": "phản ứng chiến đấu hay bỏ chạy (phản xạ sinh tồn trước nguy hiểm)"
            },
            {
                "word": "chronic",
                "ipa": "/ˈkrɑː.nɪk/",
                "meaning": "mạn tính, kéo dài dai dẳng thường xuyên"
            },
            {
                "word": "hyper-arousal",
                "ipa": "/ˌhaɪ.pɚ.əˈraʊ.zəl/",
                "meaning": "trạng thái kích động, căng thẳng thần kinh tột độ"
            },
            {
                "word": "diaphragmatic breathing",
                "ipa": "/ˌdaɪ.ə.fræɡˈmæt̬.ɪk ˈbriː.ðɪŋ/",
                "meaning": "phương pháp hít thở sâu bằng cơ hoành (bụng)"
            },
            {
                "word": "cognitive restoration",
                "ipa": "/ˈkɑːɡ.nə.t̬ɪv ˌres.təˈreɪ.ʃən/",
                "meaning": "sự phục hồi năng lượng và khả năng nhận thức của não bộ"
            }
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
    {
        "id": "read-36",
        "title": "Returning an Online Purchase & Customer Service",
        "type": "conversation",
        "topic": "Mua sắm & Dịch vụ",
        "level": "B1 - B2",
        "summary": "Tình huống đổi trả hàng mua qua mạng do giao nhầm cỡ áo và lỗi đường chỉ, cùng quy trình hoàn tiền vào tài khoản gốc.",
        "content": [
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "Thank you for contacting Urban Wardrobe Customer Care. My name is Liam. How can I help you today?"
            },
            {
                "speaker": "Emily (Female / Shopper)",
                "text": "Hello Liam. I recently ordered an autumn wool overcoat, order number UW-93814. I received the parcel yesterday, but there are two significant issues with the item."
            },
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "I am so sorry to hear that, Ms. Emily. Could you please specify what happened with the shipment?"
            },
            {
                "speaker": "Emily (Female / Shopper)",
                "text": "Firstly, I ordered a medium size in camel brown, but the tag inside the coat indicates it is a large. Secondly, there is loose stitching along the left interior pocket lining."
            },
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "I sincerely apologize for that warehouse fulfillment error and the defective seam. That certainly does not meet our quality standards. Would you prefer an exchange for the correct size or a full refund to your original payment method?"
            },
            {
                "speaker": "Emily (Female / Shopper)",
                "text": "Since the weather is getting cold, I would love an exchange if you have the camel brown overcoat available in medium."
            },
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "Let me check our distribution inventory right now. Yes, we have three units in stock in medium. I have just reserved one for you."
            },
            {
                "speaker": "Emily (Female / Shopper)",
                "text": "That is wonderful! Do I need to pay for the return postage of the incorrect coat?"
            },
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "Not at all. Because this was our error, return shipping is completely complimentary. I have just emailed you a prepaid prepaid return shipping label with a QR code."
            },
            {
                "speaker": "Emily (Female / Shopper)",
                "text": "Do I need to print out the label myself?"
            },
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "Not necessarily. You can simply show the QR code on your smartphone at any local post office branch, and the clerk will print and affix the shipping label for you. As soon as the carrier scans the parcel, your replacement coat will be dispatched via priority shipping."
            },
            {
                "speaker": "Emily (Female / Shopper)",
                "text": "That is remarkably convenient and reassuring. Thank you so much for your swift resolution, Liam!"
            },
            {
                "speaker": "Liam (Male / Service Representative)",
                "text": "You are very welcome, Emily. Thank you for your patience and for shopping with Urban Wardrobe!"
            }
        ],
        "vietnameseTranslation": "**Bản dịch tiếng Việt:**\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Cảm ơn quý khách đã liên hệ với Bộ phận Chăm sóc Khách hàng của Urban Wardrobe. Tôi tên là Liam. Tôi có thể hỗ trợ gì cho quý khách hôm nay ạ?\n\n- **Emily (Nữ / Người mua hàng):** Chào Liam. Gần đây tôi có đặt mua một chiếc áo khoác dạ mùa thu, mã đơn hàng là UW-93814. Hôm qua tôi đã nhận được gói hàng, nhưng có hai vấn đề nghiêm trọng với sản phẩm.\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Rất tiếc khi nghe điều đó, cô Emily. Cô có thể cho tôi biết cụ thể đã xảy ra vấn đề gì với đơn hàng không ạ?\n\n- **Emily (Nữ / Người mua hàng):** Thứ nhất, tôi đặt cỡ M màu nâu lạc đà, nhưng mác bên trong áo lại ghi cỡ L. Thứ hai, có một đoạn chỉ bị tuột dọc theo lớp lót túi áo bên trái phía trong.\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Tôi thành thật xin lỗi vì sự nhầm lẫn trong khâu đóng gói tại kho và lỗi đường chỉ may đó. Điều này chắc chắn không đúng với tiêu chuẩn chất lượng của chúng tôi. Cô muốn đổi sang đúng cỡ áo hay muốn được hoàn tiền toàn bộ về phương thức thanh toán ban đầu ạ?\n\n- **Emily (Nữ / Người mua hàng):** Vì thời tiết đang trở lạnh nên tôi rất muốn đổi hàng nếu bên anh còn chiếc áo khoác màu nâu lạc đà cỡ M.\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Để tôi kiểm tra lượng hàng tồn kho ngay bây giờ nhé. Vâng, chúng tôi còn đúng ba chiếc cỡ M tại kho. Tôi vừa giữ riêng một chiếc cho cô rồi ạ.\n\n- **Emily (Nữ / Người mua hàng):** Thật tuyệt vời! Tôi có phải trả phí bưu điện để gửi trả chiếc áo bị giao nhầm không?\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Hoàn toàn không ạ. Vì đây là lỗi từ phía công ty chúng tôi nên phí vận chuyển hoàn trả là hoàn toàn miễn phí. Tôi vừa gửi cho cô một phiếu vận chuyển trả hàng trả trước có kèm mã QR qua email.\n\n- **Emily (Nữ / Người mua hàng):** Tôi có cần phải tự in phiếu vận chuyển đó ra không?\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Không nhất thiết đâu ạ. Cô chỉ cần xuất trình mã QR trên điện thoại thông minh tại bất kỳ bưu cục địa phương nào, nhân viên bưu điện sẽ tự in và dán phiếu gửi hàng cho cô. Ngay khi đơn vị vận chuyển quét mã kiện hàng, chiếc áo thay thế của cô sẽ được gửi đi bằng đường chuyển phát hỏa tốc ưu tiên.\n\n- **Emily (Nữ / Người mua hàng):** Thật là tiện lợi và yên tâm quá. Cảm ơn anh rất nhiều vì cách xử lý nhanh chóng như vậy, Liam!\n\n- **Liam (Nam / Nhân viên chăm sóc khách hàng):** Không có chi, cô Emily. Cảm ơn sự kiên nhẫn của cô và cảm ơn cô đã mua sắm tại Urban Wardrobe!",
        "keyVocab": [
            {
                "word": "parcel",
                "ipa": "/ˈpɑːr.səl/",
                "meaning": "gói hàng, bưu kiện"
            },
            {
                "word": "defective seam",
                "ipa": "/dɪˈfek.tɪv siːm/",
                "meaning": "đường may bị lỗi, hỏng"
            },
            {
                "word": "fulfillment error",
                "ipa": "/fʊlˈfɪl.mənt ˈer.ɚ/",
                "meaning": "lỗi xử lý và đóng gói đơn hàng"
            },
            {
                "word": "prepaid label",
                "ipa": "/ˌpriːˈpeɪd ˈleɪ.bəl/",
                "meaning": "nhãn gửi hàng đã thanh toán cước trước"
            },
            {
                "word": "priority shipping",
                "ipa": "/praɪˈɔːr.ə.t̬i ˈʃɪp.ɪŋ/",
                "meaning": "giao hàng hỏa tốc, ưu tiên"
            }
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
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { READING_DATA };
}
