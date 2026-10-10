// Bộ dữ liệu bài tập Đọc hiểu (Reading Passages) & Hội thoại (Conversations)
// Kèm câu hỏi trắc nghiệm, giải thích chi tiết, từ vựng trọng tâm và bản dịch song ngữ

const READING_DATA = [
    {
        id: "read-1",
        title: "Contract Negotiation & Scope Alignment",
        type: "conversation",
        topic: "Công sở & Đàm phán",
        level: "B2 - C1",
        summary: "Cuộc đàm phán hợp đồng phần mềm giữa Giám đốc dự án và Đại diện khách hàng về ngân sách và thời hạn bàn giao.",
        content: [
            { speaker: "David (Project Lead)", text: "Good morning, Sarah. Thank you for making time today. We reviewed your requested revisions for the enterprise software rollout, particularly the expedited timeline." },
            { speaker: "Sarah (Client Rep)", text: "Good morning, David. We appreciate your quick turnaround. As you know, our board expects the new billing system to go live before the third quarter to avoid fiscal overlap." },
            { speaker: "David (Project Lead)", text: "We completely understand your strategic urgency. However, accelerating delivery by six weeks introduces substantial risks regarding security audits and stress testing. If we rush deployment, we risk system bottlenecks during peak transaction hours." },
            { speaker: "Sarah (Client Rep)", text: "I see your point. Reliability is paramount for our financial operations. Is there a viable compromise that protects data integrity without forfeiting our third-quarter launch?" },
            { speaker: "David (Project Lead)", text: "Precisely. We propose a phased implementation. We can deploy the core payment gateway and customer accounts on your target date, while deferring advanced analytics and automated reporting to phase two, four weeks later." },
            { speaker: "Sarah (Client Rep)", text: "That sounds pragmatic. It addresses our immediate operational need while mitigating technical vulnerabilities. Does this phased approach impact the agreed budget?" },
            { speaker: "David (Project Lead)", text: "The overall contract price remains unchanged. We merely reallocate engineering hours to prioritize core functionalities first." },
            { speaker: "Sarah (Client Rep)", text: "Excellent. Please draft an addendum with this milestone schedule, and I will submit it to our executive committee for final sign-off." }
        ],
        vietnameseTranslation: `**Bản dịch tiếng Việt:**\n
- **David (Trưởng dự án):** Chào buổi sáng, Sarah. Cảm ơn cô đã dành thời gian hôm nay. Chúng tôi đã xem xét các yêu cầu chỉnh sửa của bên cô cho đợt triển khai phần mềm doanh nghiệp, đặc biệt là tiến độ gấp rút.\n
- **Sarah (Đại diện khách hàng):** Chào David. Chúng tôi đánh giá cao sự phản hồi nhanh chóng của bên anh. Như anh đã biết, hội đồng quản trị của chúng tôi kỳ vọng hệ thống thanh toán mới sẽ đi vào hoạt động trước quý 3 để tránh trùng lặp năm tài chính.\n
- **David (Trưởng dự án):** Chúng tôi hoàn toàn hiểu tính cấp bách mang tính chiến lược của bên cô. Tuy nhiên, việc đẩy nhanh tiến độ bàn giao sớm 6 tuần sẽ tiềm ẩn rủi ro đáng kể liên quan đến kiểm toán bảo mật và thử nghiệm chịu tải. Nếu vội vàng triển khai, hệ thống có nguy cơ nghẽn mạng vào giờ cao điểm.\n
- **Sarah (Đại diện khách hàng):** Tôi hiểu quan điểm của anh. Độ tin cậy là điều tối quan trọng đối với hoạt động tài chính của chúng tôi. Liệu có phương án thỏa hiệp khả thi nào vừa bảo vệ tính toàn vẹn dữ liệu mà không làm lỡ đợt ra mắt quý 3 không?\n
- **David (Trưởng dự án):** Chính xác là vậy. Chúng tôi đề xuất triển khai theo giai đoạn. Chúng ta có thể đưa cổng thanh toán cốt lõi và tài khoản khách hàng vận hành đúng ngày mục tiêu của cô, trong khi dời phần phân tích nâng cao và báo cáo tự động sang giai đoạn hai, sau đó 4 tuần.\n
- **Sarah (Đại diện khách hàng):** Nghe rất thực tế. Cách này giải quyết được nhu cầu vận hành tức thì trong khi giảm thiểu các lỗ hổng kỹ thuật. Liệu cách tiếp cận theo giai đoạn này có ảnh hưởng đến ngân sách đã thỏa thuận không?\n
- **David (Trưởng dự án):** Tổng giá trị hợp đồng vẫn giữ nguyên. Chúng tôi chỉ phân bổ lại số giờ kỹ thuật để ưu tiên các chức năng cốt lõi trước.\n
- **Sarah (Đại diện khách hàng):** Tuyệt vời. Xin hãy soạn một phụ lục hợp đồng với lịch trình các cột mốc này, tôi sẽ nộp lên ban điều hành để ký duyệt chính thức.`,
        keyVocab: [
            { word: "expedited timeline", ipa: "/ˈek.spə.daɪ.t̬ɪd ˈtaɪm.laɪn/", meaning: "tiến độ được đẩy nhanh/rút ngắn" },
            { word: "paramount", ipa: "/ˈper.ə.maʊnt/", "meaning": "tối quan trọng, hàng đầu" },
            { word: "bottleneck", ipa: "/ˈbɑː.t̬əl.nek/", "meaning": "điểm nghẽn, sự đình trệ" },
            { word: "phased implementation", ipa: "/feɪzd ˌɪm.plə.menˈteɪ.ʃən/", "meaning": "triển khai chia theo từng giai đoạn" },
            { word: "addendum", ipa: "/əˈden.dəm/", "meaning": "phụ lục bổ sung hợp đồng" }
        ],
        questions: [
            {
                id: "q-1-1",
                question: "What is Sarah's primary concern regarding the project's launch date?",
                options: [
                    "A. Her team wants to cancel the contract before quarterly reviews.",
                    "B. The board requires the system live before Q3 to avoid financial fiscal overlap.",
                    "C. The company lacks the budget to pay for Phase 2 development.",
                    "D. Competitors are releasing a similar billing portal on the same day."
                ],
                answerIndex: 1,
                explanation: "Trong bài, Sarah nói: 'our board expects the new billing system to go live before the third quarter to avoid fiscal overlap' (Hội đồng quản trị yêu cầu hệ thống vận hành trước Q3 để tránh trùng lặp tài khóa)."
            },
            {
                id: "q-1-2",
                question: "Why does David advise against rushing the entire software deployment?",
                options: [
                    "A. His engineering team has taken an unexpected vacation.",
                    "B. The client refused to pay the mandatory upfront deposit.",
                    "C. Rushing compromises security audits and risks server bottlenecks during peak hours.",
                    "D. Advanced analytics are impossible to develop on current servers."
                ],
                answerIndex: 2,
                explanation: "David giải thích: 'accelerating delivery by six weeks introduces substantial risks regarding security audits and stress testing... we risk system bottlenecks during peak transaction hours'."
            },
            {
                id: "q-1-3",
                question: "What compromise does David propose to resolve the dilemma?",
                options: [
                    "A. Doubling the contract fee to hire twenty external contractors.",
                    "B. Deploying all features at once without any quality testing.",
                    "C. Delaying the entire software release until the fourth quarter.",
                    "D. Launching core features on schedule and deferring advanced reporting to Phase 2."
                ],
                answerIndex: 3,
                explanation: "David đề xuất: 'a phased implementation. We can deploy the core payment gateway... while deferring advanced analytics and automated reporting to phase two'."
            },
            {
                id: "q-1-4",
                question: "How does the proposed phased implementation affect the overall financial cost?",
                options: [
                    "A. The contract price increases by twenty-five percent.",
                    "B. The overall contract price remains unchanged as hours are merely reallocated.",
                    "C. The client receives a fifty percent discount for accepting delays.",
                    "D. Sarah must pay immediate cash bonuses to the engineering leads."
                ],
                answerIndex: 1,
                explanation: "David khẳng định rõ: 'The overall contract price remains unchanged. We merely reallocate engineering hours to prioritize core functionalities first'."
            }
        ]
    },
    {
        id: "read-2",
        title: "The Transformative Role of AI in Contemporary Medicine",
        type: "passage",
        topic: "Khoa học & Công nghệ",
        level: "B2 - C1",
        summary: "Đoạn văn phân tích cách trí tuệ nhân tạo đang cách mạng hóa chẩn đoán y khoa, đồng thời đặt ra những thách thức về đạo đức và trách nhiệm giải trình.",
        content: `The integration of artificial intelligence into diagnostic healthcare represents one of the most remarkable technological paradigm shifts of the twenty-first century. For decades, medical practitioners relied strictly on empirical clinical observation, manual laboratory assays, and radiological scans interpreted solely through human judgment. While experienced clinicians possess profound diagnostic intuition, human stamina is intrinsically finite, and cognitive fatigue inevitably impairs diagnostic precision during prolonged shifts.\n\nDeep learning convolutional neural networks have begun augmenting clinical workflows by analyzing vast databases of high-resolution magnetic resonance imaging (MRI) and computerized tomography (CT) scans. In oncology, specialized algorithms routinely detect micro-calcifications and malignant cellular clusters several months before they become perceptible to the naked human eye. By cross-referencing patient biometric histories with millions of digitized international clinical records, predictive algorithms also calculate individualized risk scores for cardiovascular deterioration, empowering physicians to prescribe preventative interventions well before acute episodes occur.\n\nNonetheless, medical ethicists caution against premature euphoria. A central challenge lies in the "black box" dilemma—the inherent opacity of deep neural networks whose internal weighting mechanisms are largely inscrutable even to their software architects. When an autonomous algorithmic system recommends an invasive surgical intervention or withholds a life-saving therapy, establishing legal liability and ethical accountability becomes intensely contentious. If a flawed recommendation arises from skewed training datasets that underrepresent specific demographic groups, diagnostic disparities are perpetuated rather than eradicated.\n\nConsequently, the prevailing consensus within the international medical community advocates for an augmented intelligence model rather than outright clinical automation. In this framework, artificial intelligence functions as an indispensable copilot: synthesizing complex telemetry, flagging anomalies, and eliminating repetitive clerical administrative burdens, while leaving empathetic bedside communication, nuanced ethical deliberations, and ultimate treatment authorization firmly in human hands.`,
        vietnameseTranslation: `**Bản dịch tiếng Việt:**\n
Việc tích hợp trí tuệ nhân tạo vào chẩn đoán y tế đại diện cho một trong những bước chuyển đổi hệ hình công nghệ đáng chú ý nhất của thế kỷ 21. Trong nhiều thập kỷ, các bác sĩ chỉ dựa vào quan sát lâm sàng thực nghiệm, các xét nghiệm thủ công trong phòng thí nghiệm và phim chụp X-quang được diễn giải hoàn toàn bằng đánh giá của con người. Mặc dù các bác sĩ giàu kinh nghiệm sở hữu trực giác chẩn đoán sâu sắc, sức bền của con người về bản chất là có hạn, và sự mệt mỏi về nhận thức chắc chắn làm suy giảm độ chính xác của chẩn đoán trong các ca trực kéo dài.\n\nMạng nơ-ron tích chập học sâu đã bắt đầu hỗ trợ quy trình lâm sàng bằng cách phân tích cơ sở dữ liệu khổng lồ gồm các ảnh chụp cộng hưởng từ (MRI) và cắt lớp vi tính (CT) độ phân giải cao. Trong khoa ung bướu, các thuật toán chuyên biệt thường xuyên phát hiện các ổ vi vôi hóa và các cụm tế bào ác tính vài tháng trước khi chúng có thể nhìn thấy bằng mắt thường. Bằng cách đối chiếu lịch sử sinh trắc học của bệnh nhân với hàng triệu hồ sơ bệnh án quốc tế được số hóa, các thuật toán dự đoán cũng tính toán điểm rủi ro cá nhân hóa đối với sự suy giảm tim mạch, trao quyền cho bác sĩ kê đơn can thiệp phòng ngừa rất lâu trước khi các đợt cấp tính xảy ra.\n\nTuy nhiên, các nhà đạo đức học y tế cảnh báo không nên quá lạc quan sớm. Một thách thức cốt lõi nằm ở thế tiến thoái lưỡng nan "hộp đen"—sự mờ đục vốn có của các mạng nơ-ron sâu mà các cơ chế trọng số bên trong của chúng phần lớn là không thể hiểu thấu ngay cả đối với chính các kiến trúc sư phần mềm tạo ra chúng. Khi một hệ thống thuật toán tự chủ đề xuất một can thiệp phẫu thuật xâm lấn hoặc từ chối một liệu pháp cứu mạng, việc xác định trách nhiệm pháp lý và trách nhiệm giải trình đạo đức trở nên vô cùng căng thẳng. Nếu một khuyến nghị sai sót phát sinh từ bộ dữ liệu huấn luyện bị lệch thiên lệch, vốn ít đại diện cho các nhóm nhân khẩu học cụ thể, thì sự chênh lệch trong chẩn đoán sẽ bị duy trì kéo dài thay vì bị loại bỏ.\n\nDo đó, sự đồng thuận phổ biến trong cộng đồng y tế quốc tế ủng hộ mô hình "trí tuệ tăng cường" thay vì tự động hóa lâm sàng hoàn toàn. Trong khuôn khổ này, trí tuệ nhân tạo hoạt động như một trợ lý không thể thiếu: tổng hợp dữ liệu viễn thám phức tạp, gắn cờ các điểm bất thường và loại bỏ gánh nặng hành chính lặp đi lặp lại, đồng thời để việc giao tiếp thấu cảm bên giường bệnh, những cân nhắc đạo đức tinh tế và quyết định điều trị cuối cùng nằm chắc chắn trong tay con người.`,
        keyVocab: [
            { word: "paradigm shift", ipa: "/ˈper.ə.daɪm ʃɪft/", meaning: "bước chuyển đổi hệ hình tư duy/công nghệ" },
            { word: "micro-calcification", ipa: "/ˌmaɪ.kroʊ kæl.sə.fəˈkeɪ.ʃən/", meaning: "vi vôi hóa (dấu hiệu sớm của khối u ác tính)" },
            { word: "black box dilemma", ipa: "/blæk bɑːks dɪˈlem.ə/", meaning: "thế tiến thoái lưỡng nan về tính không minh bạch của AI" },
            { word: "inscrutable", ipa: "/ɪnˈskruː.t̬ə.bəl/", meaning: "khôn dò, không thể giải mã/hiểu thấu" },
            { word: "augmented intelligence", ipa: "/ɑːɡˈmen.t̬ɪd ɪnˈtel.ə.dʒəns/", meaning: "trí tuệ tăng cường (AI hỗ trợ con người thay vì thay thế)" }
        ],
        questions: [
            {
                id: "q-2-1",
                question: "According to paragraph 1, what is a primary limitation of purely human medical diagnosis?",
                options: [
                    "A. Human doctors are incapable of showing empathy to bedridden patients.",
                    "B. Experienced clinicians completely lack diagnostic intuition.",
                    "C. Cognitive exhaustion during long shifts inevitably diminishes human diagnostic precision.",
                    "D. Medical schools no longer instruct students in manual laboratory assays."
                ],
                answerIndex: 2,
                explanation: "Đoạn 1 nêu rõ: 'human stamina is intrinsically finite, and cognitive fatigue inevitably impairs diagnostic precision during prolonged shifts' (Sức bền con người có hạn và mệt mỏi nhận thức làm suy giảm độ chính xác chẩn đoán)."
            },
            {
                id: "q-2-2",
                question: "How do deep learning algorithms aid oncologists in cancer detection?",
                options: [
                    "A. They perform delicate surgical removals without sterile operating rooms.",
                    "B. They detect malignant cellular clusters months before they become visible to human eyes.",
                    "C. They completely replace the need for MRI and CT imaging equipment.",
                    "D. They invent synthetic pharmaceuticals directly inside patient tumors."
                ],
                answerIndex: 1,
                explanation: "Đoạn 2 chỉ ra: 'algorithms routinely detect micro-calcifications and malignant cellular clusters several months before they become perceptible to the naked human eye'."
            },
            {
                id: "q-2-3",
                question: "What ethical dilemma is described by the 'black box' phenomenon?",
                options: [
                    "A. AI servers consume excessive quantities of fossil-fueled electricity.",
                    "B. Deep learning neural weights are opaque and difficult to interpret when justifying treatment decisions.",
                    "C. Medical robots are painted black, frightening pediatric hospital wards.",
                    "D. Hospitals refuse to share electronic health data with international agencies."
                ],
                answerIndex: 1,
                explanation: "Đoạn 3 phân tích: 'the inherent opacity of deep neural networks whose internal weighting mechanisms are largely inscrutable... establishing legal liability and ethical accountability becomes intensely contentious'."
            },
            {
                id: "q-2-4",
                question: "What conclusion does the medical community reach regarding the future implementation of AI?",
                options: [
                    "A. AI should function as an augmented copilot while humans retain final authority and empathetic care.",
                    "B. All human clinicians should be permanently replaced by autonomous robots by 2030.",
                    "C. AI should be outlawed globally due to unmanageable liability risks.",
                    "D. Diagnostic software should only be deployed in veterinary medicine."
                ],
                answerIndex: 0,
                explanation: "Đoạn cuối kết luận: 'advocates for an augmented intelligence model... artificial intelligence functions as an indispensable copilot... while leaving empathetic bedside communication... and ultimate treatment authorization firmly in human hands'."
            }
        ]
    },
    {
        id: "read-3",
        title: "Resolving Interdepartmental Friction",
        type: "conversation",
        topic: "Công sở & Đàm phán",
        level: "B2 - C1",
        summary: "Cuộc đối thoại giữa Trưởng phòng Tiếp thị và Trưởng phòng Kỹ thuật nhằm tháo gỡ bất đồng về tính năng sản phẩm và cam kết với khách hàng.",
        content: [
            { speaker: "Liam (Marketing Director)", text: "Marcus, thanks for sitting down with me. We noticed some tension during yesterday's all-hands briefing regarding the Q4 feature roadmap." },
            { speaker: "Marcus (Head of Engineering)", text: "I'll be candid, Liam. The marketing team announced real-time collaboration features in your public promotional webinars before engineering even finalized the backend architecture. That puts unfair pressure on my developers." },
            { speaker: "Liam (Marketing Director)", text: "I acknowledge your frustration. Our sales reps were facing aggressive counter-campaigns from our primary rival, and we felt compelled to demonstrate our competitive edge. But I admit we jumped the gun without verifying sprint capacities." },
            { speaker: "Marcus (Head of Engineering)", text: "When marketing makes promises without technical vetting, it leads to two bad outcomes: either we cut corners on code quality and release buggy software, or my team burns the midnight oil and suffers demoralizing burnout." },
            { speaker: "Liam (Marketing Director)", text: "Neither outcome is acceptable to anyone in leadership. Let's establish a formal synchronization protocol. Moving forward, marketing will not publicize any capability that has not cleared stage-three QA testing." },
            { speaker: "Marcus (Head of Engineering)", text: "I appreciate that commitment. In return, I will designate a senior technical lead to attend your bi-weekly campaign brainstorms to provide realistic feasibility assessments early on." },
            { speaker: "Liam (Marketing Director)", text: "That would be immensely helpful. It guarantees that our client messaging remains innovative while grounded in technical reality." },
            { speaker: "Marcus (Head of Engineering)", text: "Agreed. Let us communicate this unified alignment to our respective departments this afternoon." }
        ],
        vietnameseTranslation: `**Bản dịch tiếng Việt:**\n
- **Liam (Giám đốc Tiếp thị):** Marcus, cảm ơn anh đã ngồi lại cùng tôi. Chúng tôi nhận thấy có chút căng thẳng trong buổi họp toàn thể hôm qua liên quan đến lộ trình tính năng quý 4.\n
- **Marcus (Trưởng phòng Kỹ thuật):** Tôi xin nói thẳng thắn, Liam. Đội tiếp thị của anh đã công bố các tính năng cộng tác theo thời gian thực trên các hội thảo quảng bá công khai trước khi đội kỹ thuật hoàn tất kiến trúc phụ trợ. Điều đó tạo ra áp lực bất công lên các lập trình viên của tôi.\n
- **Liam (Giám đốc Tiếp thị):** Tôi thừa nhận sự bức xúc của anh. Đội ngũ bán hàng của chúng tôi đang phải đối mặt với các chiến dịch đối đầu gay gắt từ đối thủ cạnh tranh chính, và chúng tôi cảm thấy buộc phải thể hiện lợi thế cạnh tranh của mình. Nhưng tôi thừa nhận chúng tôi đã vội vàng cầm đèn chạy trước ô tô mà chưa xác minh công suất của đợt chạy nước rút (sprint).\n
- **Marcus (Trưởng phòng Kỹ thuật):** Khi tiếp thị hứa hẹn mà không có sự kiểm tra kỹ thuật, điều đó dẫn đến hai kết quả tồi tệ: hoặc là chúng tôi làm ẩu giảm chất lượng mã nguồn và phát hành phần mềm nhiều lỗi, hoặc là đội của tôi phải thức thâu đêm làm việc và bị kiệt sức làm suy giảm tinh thần.\n
- **Liam (Giám đốc Tiếp thị):** Cả hai kết cục đó đều không thể chấp nhận được đối với ban lãnh đạo. Chúng ta hãy thiết lập một quy trình đồng bộ hóa chính thức. Kể từ nay trở đi, tiếp thị sẽ không công bố bất kỳ tính năng nào chưa vượt qua bài kiểm tra đảm bảo chất lượng (QA) giai đoạn ba.\n
- **Marcus (Trưởng phòng Kỹ thuật):** Tôi đánh giá cao cam kết đó. Đổi lại, tôi sẽ chỉ định một trưởng nhóm kỹ thuật cao cấp tham gia các buổi thảo luận chiến dịch hai tuần một lần của bên anh để đưa ra các đánh giá tính khả thi thực tế ngay từ đầu.\n
- **Liam (Giám đốc Tiếp thị):** Điều đó sẽ vô cùng hữu ích. Nó đảm bảo thông điệp gửi tới khách hàng của chúng ta vừa mang tính đổi mới vừa dựa trên thực tế kỹ thuật.\n
- **Marcus (Trưởng phòng Kỹ thuật):** Nhất trí. Chiều nay chúng ta hãy truyền đạt sự thống nhất này tới các phòng ban tương ứng của mình.`,
        keyVocab: [
            { word: "candid", ipa: "/ˈkæn.dɪd/", meaning: "thẳng thắn, bộc trực" },
            { word: "jump the gun", ipa: "/dʒʌmp ðə ɡʌn/", meaning: "cầm đèn chạy trước ô tô, hành động quá vội vàng" },
            { word: "cut corners", ipa: "/kʌt ˈkɔːr.nɚz/", meaning: "làm ẩu, bớt xén quy trình" },
            { word: "burn the midnight oil", ipa: "/bɜːrn ðə ˈmɪd.naɪt ɔɪl/", meaning: "thức khuya miệt mài làm việc" },
            { word: "technical vetting", ipa: "/ˈtek.nɪ.kəl ˈvet̬.ɪŋ/", meaning: "sự kiểm tra/thẩm định kỹ thuật" }
        ],
        questions: [
            {
                id: "q-3-1",
                question: "What initiated the conflict between Marketing and Engineering?",
                options: [
                    "A. Engineering demanded a fifty percent budget increase for software tools.",
                    "B. Marketing announced features publicly before Engineering finalized the architecture.",
                    "C. Both departments wanted to lay off junior staff members.",
                    "D. Marcus publicly accused Liam of financial fraud during a press conference."
                ],
                answerIndex: 1,
                explanation: "Marcus giải thích nguyên nhân: 'The marketing team announced real-time collaboration features in your public promotional webinars before engineering even finalized the backend architecture'."
            },
            {
                id: "q-3-2",
                question: "Why did Liam's team rush to announce the new features?",
                options: [
                    "A. They wanted to sabotage the engineering team's morale.",
                    "B. They were legally obligated by government regulations to advertise immediately.",
                    "C. They were countering aggressive competitor marketing and wanted to show an edge.",
                    "D. They had already received advance payments from all corporate subscribers."
                ],
                answerIndex: 2,
                explanation: "Liam chia sẻ: 'Our sales reps were facing aggressive counter-campaigns from our primary rival, and we felt compelled to demonstrate our competitive edge'."
            },
            {
                id: "q-3-3",
                question: "What two negative outcomes does Marcus warn will occur if false promises continue?",
                options: [
                    "A. Higher office rent and reduced lunch breaks.",
                    "B. Hardware fires and data center relocations.",
                    "C. Cutting corners resulting in buggy code, or developer burnout from overwork.",
                    "D. Immediate bankruptcy and loss of cloud hosting licenses."
                ],
                answerIndex: 2,
                explanation: "Marcus cảnh báo: 'either we cut corners on code quality and release buggy software, or my team burns the midnight oil and suffers demoralizing burnout'."
            },
            {
                id: "q-3-4",
                question: "What systemic solution do both leaders agree upon for future projects?",
                options: [
                    "A. Merging both departments under a single external contractor.",
                    "B. Marketing will only announce features after Stage 3 QA, and an engineering lead will attend brainstorms.",
                    "C. Canceling all feature announcements permanently until next year.",
                    "D. Banning sales reps from attending company webinars."
                ],
                answerIndex: 1,
                explanation: "Liam cam kết marketing không công bố tính năng chưa qua QA stage-3, và Marcus đồng ý cử một senior technical lead tham gia các buổi họp chiến dịch tiếp thị."
            }
        ]
    },
    {
        id: "read-4",
        title: "The Architecture of Sustainable Urban Ecosystems",
        type: "passage",
        topic: "Môi trường & Xã hội",
        level: "B2 - C1",
        summary: "Bài luận về việc tái cấu trúc các đại đô thị hiện đại nhằm giảm thiểu phát thải carbon, tích hợp không gian xanh và thúc đẩy giao thông bền vững.",
        content: `By the mid-twenty-first century, demographic projections estimate that over two-thirds of the planetary population will reside in metropolitan sprawls. Rapid, uncontrolled urbanization historically inflicted catastrophic ecological tolls: vast swathes of heat-absorbing asphalt, rampant carbon emissions from combustion-engine gridlock, and the widespread eradication of native biodiversity. In response, avant-garde urban planners are repudiating the legacy twentieth-century ethos of car-centric zoning in favor of regenerative, circular urban design.\n\nAt the forefront of this transformation is the "15-minute city" paradigm, which reorganizes urban topology so that essential daily amenities—grocery markets, primary healthcare centers, educational facilities, and communal parks—are accessible within a quarter-hour walk or bicycle ride from any residence. By decentralizing public infrastructure, municipalities curtail vehicular dependency, dramatically suppressing localized nitrogen dioxide and particulate emissions while invigorating neighborhood social cohesion.\n\nSimultaneously, structural engineering is experiencing an organic renaissance through the adoption of biophilic architecture and carbon-sequestering building materials. Traditional concrete and steel production generates approximately fifteen percent of global greenhouse emissions. Progressive developers are pioneering structural cross-laminated timber (CLT)—sustainably harvested wood engineered to match the compressive strength of reinforced concrete while functioning as a permanent carbon sink. Furthermore, retrofitting urban facades with vertical forests and permeable sponge-city pavements mitigates the deadly urban heat island effect, allowing metropolitan centers to absorb flash flood monsoons naturally.\n\nNevertheless, implementing systemic urban regeneration requires navigating precarious socioeconomic fault lines. Aggressive infrastructural beautification frequently precipitates "green gentrification"—an inflationary cycle where escalating property valuations displace long-standing low-income communities who endured decades of environmental disinvestment. Therefore, genuine urban sustainability cannot remain a purely architectural pursuit; it necessitates rigorous municipal rent stabilization covenants and equitable transit equity subsidies to guarantee that cleaner, greener cities shelter all socioeconomic tiers unconditionally.`,
        vietnameseTranslation: `**Bản dịch tiếng Việt:**\n
Đến giữa thế kỷ 21, các dự báo nhân khẩu học ước tính rằng hơn 2/3 dân số hành tinh sẽ cư trú tại các đô thị mở rộng. Quá trình đô thị hóa nhanh chóng, mất kiểm soát trong lịch sử đã gây ra những tổn thất sinh thái thảm khốc: những dải nhựa đường hấp thụ nhiệt khổng lồ, lượng khí thải carbon tràn lan từ nạn kẹt xe động cơ đốt trong và sự xóa sổ diện rộng đa dạng sinh học bản địa. Để đối phó, các nhà quy hoạch đô thị tiên phong đang bác bỏ đặc tính quy hoạch lấy xe hơi làm trung tâm của thế kỷ 20 để hướng tới thiết kế đô thị tuần hoàn, có tính tái tạo.\n\nĐi đầu trong sự chuyển đổi này là mô hình "thành phố 15 phút", tổ chức lại địa hình đô thị sao cho các tiện ích thiết yếu hàng ngày—chợ tạp hóa, trung tâm y tế ban đầu, cơ sở giáo dục và công viên công cộng—có thể tiếp cận được trong vòng 15 phút đi bộ hoặc đạp xe từ bất kỳ nơi cư trú nào. Bằng cách phân cấp cơ sở hạ tầng công cộng, chính quyền đô thị hạn chế sự phụ thuộc vào phương tiện giao thông, ngăn chặn đáng kể lượng khí thải nitơ dioxide và bụi mịn cục bộ, đồng thời tiếp thêm sinh lực cho sự gắn kết xã hội trong khu phố.\n\nĐồng thời, kỹ thuật kết cấu đang trải qua một thời kỳ phục hưng hữu cơ thông qua việc áp dụng kiến trúc ưa sinh học (biophilic) và các vật liệu xây dựng cô lập carbon. Sản xuất bê tông và thép truyền thống tạo ra khoảng 15% lượng khí thải nhà kính toàn cầu. Các nhà phát triển tiến bộ đang tiên phong sử dụng gỗ nhiều lớp cấu trúc (CLT)—loại gỗ được thu hoạch bền vững được chế tạo để sánh ngang với cường độ nén của bê tông cốt thép trong khi hoạt động như một bể chứa carbon vĩnh viễn. Hơn nữa, việc cải tạo các mặt đứng đô thị bằng các khu rừng thẳng đứng và vỉa hè thấm nước theo mô hình "thành phố bọt biển" giúp giảm thiểu hiệu ứng đảo nhiệt đô thị chết người, cho phép các trung tâm đô thị hấp thụ các trận lũ quét do gió mùa một cách tự nhiên.\n\nTuy nhiên, việc thực hiện tái tạo đô thị mang tính hệ thống đòi hỏi phải vượt qua những ranh giới kinh tế xã hội bấp bênh. Việc chỉnh trang cơ sở hạ tầng quá mức thường dẫn đến "chỉnh trang đô thị xanh" (green gentrification)—một chu kỳ lạm phát nơi giá trị bất động sản leo thang làm dịch chuyển, đẩy những cộng đồng thu nhập thấp lâu đời, những người đã chịu đựng hàng thập kỷ thiếu đầu tư môi trường, ra khỏi nơi ở. Do đó, tính bền vững đô thị thực sự không thể chỉ là một mục tiêu kiến trúc thuần túy; nó đòi hỏi các thỏa ước bình ổn giá thuê nhà nghiêm ngặt của chính quyền thành phố và các khoản trợ cấp bình đẳng về giao thông công cộng để đảm bảo rằng các thành phố sạch hơn, xanh hơn sẽ che chở cho tất cả các tầng lớp kinh tế xã hội một cách vô điều kiện.`,
        keyVocab: [
            { word: "15-minute city", ipa: "/fɪfˈtiːn ˈmɪn.ɪt ˈsɪt.i/", meaning: "mô hình thành phố 15 phút (tiện ích tiếp cận nhanh)" },
            { word: "carbon sink", ipa: "/ˈkɑːr.bən sɪŋk/", meaning: "bể hấp thụ/cô lập carbon tự nhiên hoặc nhân tạo" },
            { word: "biophilic architecture", ipa: "/ˌbaɪ.oʊˈfɪl.ɪk ˈɑːr.kə.tek.tʃɚ/", meaning: "kiến trúc kết nối con người với thiên nhiên" },
            { word: "sponge-city pavement", ipa: "/spʌndʒ ˈsɪt.i ˈpeɪv.mənt/", meaning: "vỉa hè thấm nước kiểu thành phố bọt biển (chống ngập)" },
            { word: "green gentrification", ipa: "/ɡriːn ˌdʒen.trə.fəˈkeɪ.ʃən/", meaning: "chỉnh trang xanh đẩy người nghèo ra khỏi đô thị do giá nhà tăng" }
        ],
        questions: [
            {
                id: "q-4-1",
                question: "What core philosophy does the '15-minute city' model promote?",
                options: [
                    "A. Building high-speed highways allowing cars to cross metropolitan borders in fifteen minutes.",
                    "B. Ensuring essential daily amenities are reachable within a fifteen-minute walk or bike ride.",
                    "C. Mandating that city workers work no more than fifteen minutes of overtime each day.",
                    "D. Requiring high-speed bullet trains between every residential apartment tower."
                ],
                answerIndex: 1,
                explanation: "Đoạn 2 nêu rõ: 'the 15-minute city paradigm, which reorganizes urban topology so that essential daily amenities... are accessible within a quarter-hour walk or bicycle ride from any residence'."
            },
            {
                id: "q-4-2",
                question: "Why are progressive developers adopting cross-laminated timber (CLT)?",
                options: [
                    "A. It is lighter than plastic and dissolves naturally after five years.",
                    "B. It matches reinforced concrete strength while acting as a permanent carbon sink.",
                    "C. Traditional steel and concrete have been completely banned by the United Nations.",
                    "D. CLT buildings cannot catch fire even under direct flamethrower heat."
                ],
                answerIndex: 1,
                explanation: "Đoạn 3 giải thích: 'cross-laminated timber (CLT)—sustainably harvested wood engineered to match the compressive strength of reinforced concrete while functioning as a permanent carbon sink'."
            },
            {
                id: "q-4-3",
                question: "What socio-economic hazard is termed 'green gentrification' in the passage?",
                options: [
                    "A. Parks becoming overgrown with invasive toxic weed species.",
                    "B. Suburban farms refusing to sell fresh produce to metropolitan supermarkets.",
                    "C. Rising property values displacing low-income residents after environmental upgrades.",
                    "D. Severe municipal budget deficits caused by overspending on bicycle lanes."
                ],
                answerIndex: 2,
                explanation: "Đoạn cuối phân tích: 'green gentrification—an inflationary cycle where escalating property valuations displace long-standing low-income communities'."
            },
            {
                id: "q-4-4",
                question: "According to the final paragraph, what is required alongside architectural changes to achieve true sustainability?",
                options: [
                    "A. Rent stabilization covenants and equitable transit subsidies.",
                    "B. Banning all commercial private businesses from city downtowns.",
                    "C. Relocating all industrial workers to offshore drilling platforms.",
                    "D. Constructing armed checkpoints between distinct residential neighborhoods."
                ],
                answerIndex: 0,
                explanation: "Đoạn cuối nhấn mạnh: 'it necessitates rigorous municipal rent stabilization covenants and equitable transit equity subsidies to guarantee that cleaner, greener cities shelter all socioeconomic tiers unconditionally'."
            }
        ]
    },
    {
        id: "read-5",
        title: "Flight Cancellation & Emergency Rerouting",
        type: "conversation",
        topic: "Du lịch & Giao tiếp sinh tồn",
        level: "B1 - B2",
        summary: "Cuộc hội thoại tại quầy dịch vụ sân bay khi một chuyến bay quốc tế bị hủy do bão và hành khách cần tìm giải pháp bay thay thế khẩn cấp.",
        content: [
            { speaker: "Passenger (Julian)", text: "Excuse me. My connecting flight to Frankfurt, flight LH402, was just marked as canceled on the departures board. I have an indispensable business summit tomorrow morning at nine." },
            { speaker: "Gate Agent (Elena)", text: "I deeply apologize for the inconvenience, sir. Severe freezing rain swept across our northern hub, forcing aviation authorities to ground all departures for safety." },
            { speaker: "Passenger (Julian)", text: "I understand weather constraints are unavoidable, but missing this keynote presentation would inflict irreparable damage on our partnership. Are there any alternate carriers or indirect routings available tonight?" },
            { speaker: "Gate Agent (Elena)", text: "Let me check our global alliance database right away. Most direct flights to Germany are booked solid due to the holiday surge. However, there is a Star Alliance partner flight departing in two hours with a layover in Zurich." },
            { speaker: "Passenger (Julian)", text: "What would the estimated arrival time in Frankfurt be with the Zurich connection?" },
            { speaker: "Gate Agent (Elena)", text: "You would land at Frankfurt International at 7:15 AM tomorrow morning. That provides you with nearly two hours to clear customs and reach the conference center." },
            { speaker: "Passenger (Julian)", text: "That sounds like our best lifeline. Will my checked luggage transfer seamlessly through Zurich, or do I need to re-check my bags?" },
            { speaker: "Gate Agent (Elena)", text: "Because this is an allied partner carrier, your baggage will be rerouted automatically through to Frankfurt. Here are your revised boarding passes. I have also issued an airline meal voucher for the lounge while you await boarding." },
            { speaker: "Passenger (Julian)", text: "Elena, your poise and resourcefulness saved my day. Thank you immensely." }
        ],
        vietnameseTranslation: `**Bản dịch tiếng Việt:**\n
- **Hành khách (Julian):** Xin lỗi cô. Chuyến bay nối chuyến của tôi đi Frankfurt, chuyến LH402, vừa bị báo hủy trên bảng khởi hành. Tôi có một hội nghị thượng đỉnh kinh doanh tối quan trọng vào sáng mai lúc 9 giờ.\n
- **Nhân viên quầy (Elena):** Tôi vô cùng xin lỗi vì sự bất tiện này, thưa quý khách. Mưa băng giá nghiêm trọng vừa quét qua trung tâm trung chuyển phía bắc của chúng tôi, buộc các cơ quan hàng không phải tạm dừng mọi chuyến bay để đảm bảo an toàn.\n
- **Hành khách (Julian):** Tôi hiểu rằng những trở ngại về thời tiết là không thể tránh khỏi, nhưng nếu lỡ bài phát biểu quan trọng này sẽ gây ra thiệt hại không thể khắc phục được cho mối quan hệ đối tác của chúng tôi. Liệu tối nay có chuyến bay của hãng hàng không khác hoặc tuyến bay gián tiếp nào không?\n
- **Nhân viên quầy (Elena):** Để tôi kiểm tra ngay cơ sở dữ liệu liên minh toàn cầu của chúng tôi. Hầu hết các chuyến bay thẳng đến Đức đều đã kín chỗ do đợt cao điểm ngày lễ. Tuy nhiên, có một chuyến bay của đối tác Liên minh Star Alliance khởi hành sau 2 giờ nữa, quá cảnh tại Zurich.\n
- **Hành khách (Julian):** Thời gian đến Frankfurt dự kiến khi quá cảnh ở Zurich sẽ là mấy giờ?\n
- **Nhân viên quầy (Elena):** Quý khách sẽ hạ cánh xuống Sân bay Quốc tế Frankfurt lúc 7:15 sáng mai. Điều đó giúp quý khách có gần hai giờ để làm thủ tục hải quan và đến trung tâm hội nghị.\n
- **Hành khách (Julian):** Đó dường như là chiếc phao cứu sinh tốt nhất của chúng tôi. Liệu hành lý ký gửi của tôi có được chuyển thẳng qua Zurich không, hay tôi cần phải làm thủ tục gửi lại hành lý?\n
- **Nhân viên quầy (Elena):** Vì đây là hãng hàng không đối tác trong liên minh, hành lý của quý khách sẽ tự động được định tuyến lại đến Frankfurt. Đây là thẻ lên máy bay đã được sửa đổi của quý khách. Tôi cũng đã xuất một phiếu ăn miễn phí của hãng tại phòng chờ trong khi quý khách đợi lên máy bay.\n
- **Hành khách (Julian):** Elena, sự điềm tĩnh và tháo vát của cô đã cứu vãn một ngày của tôi. Cảm ơn cô rất nhiều.`,
        keyVocab: [
            { word: "connecting flight", ipa: "/kəˈnek.tɪŋ flaɪt/", meaning: "chuyến bay nối chuyến" },
            { word: "irreparable damage", ipa: "/ɪˈrep.ɚ.ə.bəl ˈdæm.ɪdʒ/", meaning: "thiệt hại không thể cứu vãn/khắc phục" },
            { word: "layover", ipa: "/ˈleɪˌoʊ.vɚ/", meaning: "thời gian quá cảnh tại sân bay trung gian" },
            { word: "reroute", ipa: "/ˌriːˈraʊt/", meaning: "đổi lộ trình, định tuyến lại" },
            { word: "resourcefulness", ipa: "/rɪˈzɔːr.sfəl.nəs/", meaning: "sự tháo vát, khả năng xoay xở nhanh nhạy" }
        ],
        questions: [
            {
                id: "q-5-1",
                question: "Why was Julian's initial flight to Frankfurt canceled?",
                options: [
                    "A. Severe freezing rain forced aviation authorities to ground departures.",
                    "B. The pilot refused to operate the aircraft without extra hazard pay.",
                    "C. The aircraft experienced total electrical system failure on the runway.",
                    "D. Julian arrived thirty minutes past the check-in deadline."
                ],
                answerIndex: 0,
                explanation: "Elena giải thích lý do hủy chuyến: 'Severe freezing rain swept across our northern hub, forcing aviation authorities to ground all departures for safety'."
            },
            {
                id: "q-5-2",
                question: "What route does Elena find to get Julian to his destination?",
                options: [
                    "A. An overnight high-speed train traveling across the Alps.",
                    "B. A charter private helicopter flying directly to Berlin.",
                    "C. A partner airline flight in two hours with a layover in Zurich.",
                    "D. A flight arriving two days later on Tuesday afternoon."
                ],
                answerIndex: 2,
                explanation: "Elena thông báo: 'there is a Star Alliance partner flight departing in two hours with a layover in Zurich'."
            },
            {
                id: "q-5-3",
                question: "What time will Julian arrive in Frankfurt via the alternative route?",
                options: [
                    "A. Exactly at 9:00 AM as his keynote speech begins.",
                    "B. At 7:15 AM the following morning, leaving nearly two hours to reach the summit.",
                    "C. At midnight tonight with nowhere to sleep.",
                    "D. At 3:30 PM tomorrow afternoon after the conference adjourns."
                ],
                answerIndex: 1,
                explanation: "Elena xác nhận: 'You would land at Frankfurt International at 7:15 AM tomorrow morning. That provides you with nearly two hours to clear customs and reach the conference center'."
            },
            {
                id: "q-5-4",
                question: "What happens to Julian's checked luggage during the rerouting?",
                options: [
                    "A. Julian must retrieve his bags immediately and pay a new luggage tariff.",
                    "B. The baggage will be retained at the current airport and shipped by maritime freight.",
                    "C. His bags will transfer automatically through Zurich to Frankfurt because of the airline alliance.",
                    "D. All luggage was lost during the cancellation."
                ],
                answerIndex: 2,
                explanation: "Elena khẳng định: 'Because this is an allied partner carrier, your baggage will be rerouted automatically through to Frankfurt'."
            }
        ]
    },
    {
        id: "read-6",
        title: "The Psychology of Habit Formation & Cognitive Momentum",
        type: "passage",
        topic: "Tâm lý & Nhận thức",
        level: "B2 - C1",
        summary: "Phân tích khoa học thần kinh về cách não bộ hình thành thói quen thông qua vòng lặp gợi ý - hành động - phần thưởng, và chiến lược xây dựng đà nhận thức bền vững.",
        content: `Human behavior is fundamentally dictated not by conscious, deliberative willpower, but by deeply automated neural habit loops. Cognitive neuroscientists estimate that between forty to fifty percent of daily human activities—from brushing teeth to reflexively checking smartphone feeds—are executed under subcortical automaticity. The brain, evolved to conserve scarce glucose, continually seeks to streamline repetitive decision-making by delegating routine behavioral sequences to the basal ganglia.\n\nThis automaticity operates via a three-part mechanism: the cue, the routine, and the reward. The cue acts as a sensory or temporal trigger that alerts the brain to initiate a specialized behavioral routine. Once the behavior executes, the brain receives a biochemical reward—frequently a pulse of dopamine—which reinforces neural synaptic pathways, cementing the likelihood that the routine will recur upon subsequent exposure to the identical cue. Over time, anticipation of the reward transforms into a subconscious neurological craving.\n\nCrucially, common self-help doctrines that urge individuals to rely exclusively on raw willpower to overhaul their lives fail to appreciate the physiology of cognitive depletion. Deliberate decision-making resides in the prefrontal cortex, a metabolically demanding brain region susceptible to decision fatigue. Under prolonged emotional stress or physical exhaustion, prefrontal executive control atrophies, causing the individual to default reflexively to hardwired, legacy habit routines—often destructive vices like compulsive snacking or sedentary procrastination.\n\nConsequently, behavioral architects advocate for "habit stacking" and environmental optimization rather than heroic self-discipline. By anchoring a desired nascent habit directly onto an immutable pre-existing routine (for example: "Immediately after pouring my morning coffee, I will review ten English vocabulary cards for five minutes"), friction is minimized. Furthermore, designing an environment where beneficial cues are glaringly obvious and counterproductive distractions are physically obstructed leverages the brain's innate inertia, transforming deliberate aspirations into frictionless, lifelong momentum.`,
        vietnameseTranslation: `**Bản dịch tiếng Việt:**\n
Hành vi của con người về cơ bản không được quyết định bởi ý chí có ý thức, suy tính kỹ lưỡng, mà bởi các vòng lặp thói quen thần kinh tự động hóa sâu sắc. Các nhà khoa học thần kinh nhận thức ước tính rằng từ 40 đến 50% các hoạt động hàng ngày của con người—từ đánh răng đến phản xạ kiểm tra bảng tin điện thoại thông minh—được thực hiện dưới sự tự động hóa của vùng dưới vỏ não. Bộ não, vốn tiến hóa để bảo tồn lượng glucose khan hiếm, liên tục tìm cách tinh giản việc ra quyết định lặp đi lặp lại bằng cách ủy quyền các chuỗi hành vi thường nhật cho hạch nền (basal ganglia).\n\nCơ chế tự động hóa này vận hành thông qua một quy trình ba phần: gợi ý (cue), thói quen hành động (routine) và phần thưởng (reward). Gợi ý đóng vai trò là tác nhân kích hoạt cảm giác hoặc thời gian báo cho não bắt đầu một chuỗi hành động chuyên biệt. Sau khi hành vi thực hiện xong, não nhận được phần thưởng sinh hóa—thường là một đợt giải phóng dopamine—giúp củng cố các đường dẫn synap thần kinh, khắc sâu khả năng thói quen đó sẽ tái diễn khi gặp lại gợi ý giống hệt. Theo thời gian, sự mong đợi phần thưởng sẽ biến thành một cơn thèm muốn thần kinh trong tiềm thức.\n\nĐiều quan trọng là các giáo lý phát triển bản thân phổ biến thúc giục các cá nhân chỉ dựa vào ý chí đơn thuần để thay đổi cuộc sống đã không nhận thức được sinh lý học của sự cạn kiệt nhận thức. Việc ra quyết định có chủ ý nằm ở vỏ não trước trán, một vùng não đòi hỏi nhiều năng lượng trao đổi chất và rất dễ bị mệt mỏi khi phải ra quyết định liên tục. Dưới sự căng thẳng cảm xúc kéo dài hoặc kiệt sức thể chất, khả năng kiểm soát điều hành của vỏ não trước trán bị suy giảm, khiến cá nhân quay trở lại một cách vô thức với các thói quen cũ đã ăn sâu—thường là những tật xấu tiêu cực như ăn vặt theo cảm xúc hoặc trì hoãn thụ động.\n\nDo đó, các nhà kiến trúc hành vi ủng hộ phương pháp "xếp chồng thói quen" (habit stacking) và tối ưu hóa môi trường hơn là sự tự kỷ luật phi thường mang tính anh hùng. Bằng cách gắn một thói quen mới mong muốn trực tiếp vào một thói quen cũ đã bất biến (ví dụ: "Ngay sau khi rót cà phê buổi sáng, tôi sẽ xem lại 10 thẻ từ vựng tiếng Anh trong 5 phút"), lực cản sẽ được giảm thiểu. Hơn nữa, việc thiết kế một môi trường nơi các tín hiệu có lợi hiển hiện rõ ràng và những thứ gây xao nhãng phản tác dụng bị cản trở về mặt vật lý sẽ tận dụng quán tính bẩm sinh của não bộ, biến những khát vọng có chủ ý thành đà phát triển trơn tru, bền bỉ suốt đời.`,
        keyVocab: [
            { word: "automaticity", ipa: "/ˌɑː.t̬ə.məˈtɪs.ə.t̬i/", meaning: "tính tự động hóa trong phản xạ thần kinh" },
            { word: "basal ganglia", ipa: "/ˈbeɪ.səl ˈɡæŋ.ɡli.ə/", meaning: "hạch nền não bộ (nơi lưu trữ thói quen tự động)" },
            { word: "decision fatigue", ipa: "/dɪˈsɪʒ.ən fəˈtiːɡ/", meaning: "sự mệt mỏi khi phải đưa ra quá nhiều quyết định" },
            { word: "habit stacking", ipa: "/ˈhæb.ɪt ˈstæk.ɪŋ/", meaning: "kỹ thuật xếp chồng thói quen mới lên thói quen cũ" },
            { word: "cognitive momentum", ipa: "/ˈkɑːɡ.nə.t̬ɪv moʊˈmen.t̬əm/", meaning: "đà phát triển nhận thức trơn tru không ma sát" }
        ],
        questions: [
            {
                id: "q-6-1",
                question: "According to cognitive neuroscientists, what portion of daily human activity is driven by habit loops?",
                options: [
                    "A. Less than five percent.",
                    "B. Exactly one hundred percent.",
                    "C. Between forty and fifty percent.",
                    "D. Only during nighttime sleep cycles."
                ],
                answerIndex: 2,
                explanation: "Đoạn 1 chỉ rõ: 'Cognitive neuroscientists estimate that between forty to fifty percent of daily human activities... are executed under subcortical automaticity'."
            },
            {
                id: "q-6-2",
                question: "What are the three core components of the neurological habit loop?",
                options: [
                    "A. Memory, ambition, and punishment.",
                    "B. The cue, the routine, and the reward.",
                    "C. Genetic heritage, diet, and physical exercise.",
                    "D. Prefrontal willpower, social peer pressure, and dopamine."
                ],
                answerIndex: 1,
                explanation: "Đoạn 2 nêu định nghĩa: 'This automaticity operates via a three-part mechanism: the cue, the routine, and the reward'."
            },
            {
                id: "q-6-3",
                question: "Why does relying purely on raw willpower often fail over time?",
                options: [
                    "A. The prefrontal cortex suffers from metabolic decision fatigue under stress and exhaustion.",
                    "B. Human beings are genetically incapable of learning foreign languages.",
                    "C. Dopamine receptors completely shut down after age twenty-five.",
                    "D. Willpower is an imaginary concept invented by advertising firms."
                ],
                answerIndex: 0,
                explanation: "Đoạn 3 giải thích: 'Deliberate decision-making resides in the prefrontal cortex, a metabolically demanding brain region susceptible to decision fatigue. Under prolonged emotional stress or physical exhaustion, prefrontal executive control atrophies'."
            },
            {
                id: "q-6-4",
                question: "What is an effective example of 'habit stacking' described in the text?",
                options: [
                    "A. Refusing to sleep until fifty vocabulary textbooks are memorized.",
                    "B. Reviewing ten vocabulary cards immediately after pouring morning coffee.",
                    "C. Drinking six cups of coffee while studying throughout the night.",
                    "D. Deleting all social media accounts permanently every weekend."
                ],
                answerIndex: 1,
                explanation: "Đoạn 4 minh họa cụ thể: 'anchoring a desired nascent habit directly onto an immutable pre-existing routine (for example: \"Immediately after pouring my morning coffee, I will review ten English vocabulary cards for five minutes\")'."
            }
        ]
    }
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { READING_DATA };
}
