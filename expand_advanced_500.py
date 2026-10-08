import json
import os

# Tập hợp 505 từ vựng & mẫu câu Tiếng Anh Nâng cao (B2 - C1 / IELTS 6.5 - 8.0 / Business & Academic)
# Chia theo 10 chủ đề chuyên sâu:

DATA_CATEGORIES = {
    "Công sở & Đàm phán": [
        ("collaborate", "/kəˈlæb.ə.reɪt/", "hợp tác, cộng tác chặt chẽ", "We need to collaborate with the international engineering team.", "Chúng ta cần hợp tác với đội ngũ kỹ thuật quốc tế.", "Đi với with (người) hoặc on (dự án). Danh từ: collaboration."),
        ("negotiate", "/nəˈɡoʊ.ʃi.eɪt/", "đàm phán, thương lượng", "They are negotiating a long-term strategic partnership.", "Họ đang đàm phán một thỏa thuận hợp tác chiến lược dài hạn.", "Danh từ: negotiation."),
        ("implement", "/ˈɪm.plə.ment/", "triển khai, thi hành chính sách", "The organization decided to implement flexible working hours.", "Tổ chức đã quyết định triển khai giờ làm việc linh hoạt.", "Danh từ: implementation."),
        ("facilitate", "/fəˈsɪl.ə.teɪt/", "tạo điều kiện thuận lợi, điều phối", "Cloud platforms facilitate cross-border collaboration.", "Các nền tảng đám mây tạo điều kiện thuận lợi cho hợp tác xuyên biên giới.", "Từ học thuật trang trọng."),
        ("prioritize", "/praɪˈɔːr.ə.taɪz/", "ưu tiên việc cấp bách", "Project managers must prioritize core deliverables.", "Quản lý dự án phải ưu tiên các hạng mục bàn giao cốt lõi.", "Danh từ: priority."),
        ("delegate", "/ˈdel.ə.ɡeɪt/", "ủy quyền, giao phó trách nhiệm", "Effective leaders delegate operational tasks to subordinates.", "Lãnh đạo hiệu quả ủy quyền các nhiệm vụ vận hành cho cấp dưới.", "Danh từ: delegation."),
        ("optimize", "/ˈɑːp.tə.maɪz/", "tối ưu hóa quy trình", "We must optimize resource allocation to reduce waste.", "Chúng ta phải tối ưu hóa phân bổ nguồn lực để giảm lãng phí.", "Danh từ: optimization."),
        ("streamline", "/ˈstriːm.laɪn/", "tinh giản quy trình, cải tiến", "Automation helped streamline accounting operations.", "Tự động hóa đã giúp tinh giản các hoạt động kế toán.", "Lược bỏ khâu cồng kềnh."),
        ("consensus", "/kənˈsen.səs/", "sự đồng thuận, nhất trí tập thể", "The board finally reached a consensus on the acquisition.", "Hội đồng cuối cùng đã đạt được sự đồng thuận về thương vụ mua lại.", "Reach a consensus."),
        ("milestone", "/ˈmaɪl.stoʊn/", "cột mốc quan trọng", "Securing initial funding was a critical milestone.", "Đạt được khoản vốn ban đầu là một cột mốc mang tính quyết định.", "Achieve/reach a milestone."),
        ("stakeholder", "/ˈsteɪkˌhoʊl.dɚ/", "bên liên quan trực tiếp", "Consulting key stakeholders builds long-term commitment.", "Tham vấn các bên liên quan chủ chốt giúp xây dựng cam kết lâu dài.", "Khách hàng, cổ đông, nhân viên."),
        ("feasible", "/ˈfiː.zə.bəl/", "khả thi về mặt thực tiễn", "Is the aggressive timeline technically feasible?", "Tiến độ gấp gáp này có khả thi về mặt kỹ thuật không?", "Danh từ: feasibility."),
        ("allocate", "/ˈæl.ə.keɪt/", "phân bổ vốn/nhân lực", "Management allocated substantial funds to cybersecurity.", "Ban quản lý đã phân bổ khoản ngân sách đáng kể cho an ninh mạng.", "Allocate budget/resources."),
        ("benchmark", "/ˈbentʃ.mɑːrk/", "tiêu chuẩn đối sánh chuẩn mực", "Their customer retention rate serves as an industry benchmark.", "Tỷ lệ giữ chân khách hàng của họ đóng vai trò là mốc chuẩn toàn ngành.", "Dùng để so sánh hiệu suất."),
        ("bottleneck", "/ˈbɑː.t̬əl.nek/", "điểm nghẽn gây đình trệ", "Supply shortages formed a major bottleneck in manufacturing.", "Tình trạng thiếu hụt nguồn cung đã tạo ra điểm nghẽn lớn trong sản xuất.", "Chỗ làm chậm tiến độ chung."),
        ("contingency", "/kənˈtɪn.dʒən.si/", "phương án dự phòng bất trắc", "We developed a contingency plan for server outages.", "Chúng tôi đã xây dựng kế hoạch dự phòng cho sự cố sập máy chủ.", "Contingency plan / fund."),
        ("leverage", "/ˈlev.ɚ.ɪdʒ/", "tận dụng tối đa đòn bẩy", "The firm leverages data analytics to personalize marketing.", "Công ty tận dụng phân tích dữ liệu để cá nhân hóa tiếp thị.", "Tận dụng lợi thế sẵn có."),
        ("redundant", "/rɪˈdʌn.dənt/", "dư thừa, cắt giảm nhân sự", "Automating workflows rendered legacy software redundant.", "Tự động hóa quy trình khiến phần mềm cũ trở nên dư thừa.", "Make someone redundant."),
        ("sustainable", "/səˈsteɪ.nə.bəl/", "bền vững dài hạn", "Eco-friendly practices foster sustainable business models.", "Thực hành thân thiện môi trường thúc đẩy mô hình kinh doanh bền vững.", "Sustainability."),
        ("synergy", "/ˈsɪn.ɚ.dʒi/", "sức mạnh cộng hưởng", "The merger produced noticeable cost synergies.", "Vụ sáp nhập đã tạo ra sự cộng hưởng chi phí rõ rệt.", "1 + 1 > 2."),
        ("transparency", "/trænˈspær.ən.si/", "sự minh bạch công khai", "Financial transparency reassures cautious investors.", "Minh bạch tài chính trấn an các nhà đầu tư thận trọng.", "Transparent reporting."),
        ("accountability", "/əˌkaʊn.t̬əˈbɪl.ə.t̬i/", "trách nhiệm giải trình", "Public officials must demonstrate strict accountability.", "Các quan chức công quyền phải thể hiện trách nhiệm giải trình nghiêm ngặt.", "Hold someone accountable."),
        ("proactive", "/proʊˈæk.tɪv/", "chủ động đón đầu xu hướng", "Proactive risk mitigation minimizes project failures.", "Giảm thiểu rủi ro chủ động giúp hạn chế tối đa thất bại dự án.", "Trái nghĩa: reactive."),
        ("scalable", "/ˈskeɪ.lə.bəl/", "có khả năng mở rộng quy mô", "The architecture is scalable across millions of concurrent users.", "Kiến trúc có khả năng mở rộng phục vụ hàng triệu người dùng đồng thời.", "Scalability."),
        ("incentive", "/ɪnˈsen.t̬ɪv/", "động lực khích lệ bằng thưởng", "Performance bonuses provide a compelling incentive.", "Thưởng theo hiệu suất tạo ra động lực thúc đẩy hấp dẫn.", "Incentivize employees."),
        ("competency", "/ˈkɑːm.pə.t̬ən.si/", "năng lực cốt lõi chuyên môn", "Analytical thinking is an indispensable competency.", "Tư duy phân tích là một năng lực cốt lõi không thể thiếu.", "Core competency."),
        ("reimburse", "/ˌriː.ɪmˈbɜːrs/", "hoàn trả chi phí công tác", "Submit your receipts to be reimbursed promptly.", "Hãy nộp hóa đơn để được hoàn trả tiền kịp thời.", "Travel reimbursement."),
        ("discrepancy", "/dɪˈskrep.ən.si/", "sai lệch số liệu bất thường", "Auditors flagged an unexplained discrepancy in inventory counts.", "Kiểm toán viên đã cảnh báo một sai lệch khó hiểu trong kiểm kê kho.", "Discrepancy between A and B."),
        ("liability", "/ˌlaɪ.əˈbɪl.ə.t̬i/", "trách nhiệm pháp lý, nợ phải trả", "Product defects expose manufacturers to severe liability.", "Lỗi sản phẩm khiến nhà sản xuất đối mặt với trách nhiệm pháp lý nặng nề.", "Assets and liabilities."),
        ("compliance", "/kəmˈplaɪ.əns/", "tuân thủ luật pháp và chuẩn mực", "The bank instituted strict regulatory compliance protocols.", "Ngân hàng đã thiết lập các quy trình tuân thủ quy định nghiêm ngặt.", "In compliance with."),
        ("turnover", "/ˈtɜːrnˌoʊ.vɚ/", "tỷ lệ nhảy việc, vòng quay vốn", "High employee turnover indicates leadership deficiencies.", "Tỷ lệ luân chuyển nhân sự cao phản ánh sự yếu kém trong ban lãnh đạo.", "Staff turnover / inventory turnover."),
        ("retain", "/rɪˈteɪn/", "giữ chân nhân tài, duy trì", "Competitive compensation helps retain top talent.", "Đãi ngộ cạnh tranh giúp giữ chân nhân tài hàng đầu.", "Talent retention."),
        ("downsize", "/ˈdaʊn.saɪz/", "thu hẹp quy mô tinh giản", "Firms downsized operations to withstand inflation.", "Các công ty đã thu hẹp hoạt động để chống chọi lạm phát.", "Cắt giảm nhân sự do khủng hoảng."),
        ("procure", "/prəˈkjʊr/", "thu mua vật tư đấu thầu", "We procure electronic components from verified suppliers.", "Chúng tôi thu mua linh kiện điện tử từ các nhà cung ứng đã kiểm định.", "Procurement department."),
        ("vendor", "/ˈven.dɚ/", "nhà cung cấp bên ngoài", "Evaluate multiple third-party vendors before contracting.", "Đánh giá nhiều nhà cung cấp bên thứ ba trước khi ký hợp đồng.", "Vendor assessment."),
        ("remuneration", "/rɪˌmjuː.nəˈreɪ.ʃən/", "thù lao lương thưởng trang trọng", "Executives negotiated their annual remuneration package.", "Các giám đốc điều hành đã đàm phán gói thù lao hàng năm của mình.", "Formal term for salary."),
        ("appraisal", "/əˈpreɪ.zəl/", "đánh giá thành tích định kỳ", "Quarterly appraisals identify training opportunities.", "Đánh giá hàng quý giúp nhận diện cơ hội đào tạo nhân viên.", "Performance appraisal."),
        ("diversify", "/daɪˈvɜːr.sə.faɪ/", "đa dạng hóa danh mục", "Companies diversify product offerings to expand market share.", "Doanh nghiệp đa dạng hóa dải sản phẩm để mở rộng thị phần.", "Diversification."),
        ("monopoly", "/məˈnɑː.pəl.i/", "độc quyền thị trường", "Antitrust regulations curb unfair monopolies.", "Quy định chống độc quyền kiềm chế các thế lực độc quyền phi lý.", "Monopolistic market."),
        ("deficit", "/ˈdef.ə.sɪt/", "thâm hụt tài chính", "The trade deficit narrowed due to robust exports.", "Thâm hụt thương mại đã thu hẹp nhờ xuất khẩu tăng mạnh.", "Budget deficit."),
        ("surplus", "/ˈsɜːr.pləs/", "thặng dư thặng dư vốn", "Budget surplus allowed investment in public infrastructure.", "Thặng dư ngân sách cho phép tái đầu tư vào hạ tầng công cộng.", "Trade surplus."),
        ("clause", "/klɔːz/", "điều khoản hợp đồng", "Ensure the termination clause protects our intellectual property.", "Đảm bảo điều khoản chấm dứt hợp đồng bảo vệ quyền sở hữu trí tuệ của chúng ta.", "Contractual clause."),
        ("breach", "/briːtʃ/", "vi phạm cam kết hợp đồng", "Sharing confidential files constitutes an actionable breach.", "Chia sẻ tài liệu bảo mật cấu thành hành vi vi phạm có thể bị kiện.", "Breach of trust/contract."),
        ("arbitration", "/ˌɑːr.bəˈtreɪ.ʃən/", "phân xử trọng tài kinh tế", "Commercial arbitration offers rapid dispute resolution.", "Trọng tài thương mại cung cấp giải pháp giải quyết tranh chấp nhanh chóng.", "Arbitration tribunal."),
        ("oversee", "/ˌoʊ.vɚˈsiː/", "giám sát bao quát toàn cục", "The director oversees international regional offices.", "Giám đốc bao quát và giám sát các văn phòng khu vực quốc tế.", "Supervise / manage."),
        ("execute", "/ˈek.sə.kjuːt/", "triển khai thi hành chính xác", "Flawlessly execute the marketing rollout plan.", "Triển khai hoàn hảo kế hoạch tung chiến dịch tiếp thị.", "Execution capability."),
        ("facilitator", "/fəˈsɪl.ə.teɪ.t̬ɚ/", "người điều phối thảo luận", "An independent facilitator guided the mediation session.", "Một điều phối viên độc lập đã dẫn dắt buổi hòa giải.", "Meeting facilitator."),
        ("empower", "/ɪmˈpaʊ.ɚ/", "trao quyền cho cấp dưới", "Empower frontline employees to solve customer disputes.", "Trao quyền cho nhân viên tuyến đầu giải quyết khiếu nại khách hàng.", "Employee empowerment."),
        ("restructure", "/ˌriːˈstrʌk.tʃɚ/", "tái cơ cấu tổ chức", "The conglomerate restructured to cut administrative bloat.", "Tập đoàn đã tái cơ cấu để cắt giảm sự cồng kềnh trong bộ máy quản lý.", "Corporate restructuring."),
        ("lucrative", "/ˈluː.krə.t̬ɪv/", "sinh lợi nhuận khổng lồ", "Cloud computing remains the firm's most lucrative branch.", "Điện toán đám mây vẫn là nhánh kinh doanh sinh lời nhất của công ty.", "Lucrative opportunity.")
    ],

    "Tư duy & Học thuật": [
        ("scrutinize", "/ˈskruː.tən.aɪz/", "soi xét mổ xẻ phân tích kỹ", "The ethics committee scrutinized the clinical trial data.", "Hội đồng đạo đức đã soi xét kỹ lưỡng dữ liệu thử nghiệm lâm sàng.", "Xem xét chi tiết từng li."),
        ("hypothesize", "/haɪˈpɑː.θə.saɪz/", "đưa ra giả thuyết khoa học", "Astrophysicists hypothesize the existence of dark energy.", "Các nhà vật lý thiên văn giả định về sự tồn tại của năng lượng tối.", "Hypothesis."),
        ("corroborate", "/kəˈrɑː.bə.reɪt/", "chứng thực củng cố chứng cứ", "Witness testimonies corroborated the forensic evidence.", "Lời khai nhân chứng đã củng cố chứng cứ pháp y.", "Xác nhận tính xác thực."),
        ("contradict", "/ˌkɑːn.trəˈdɪkt/", "mâu thuẫn trái ngược hoàn toàn", "The data contradicts initial laboratory assertions.", "Dữ liệu mâu thuẫn hoàn toàn với khẳng định ban đầu trong phòng thí nghiệm.", "Contradiction."),
        ("synthesize", "/ˈsɪn.θə.saɪz/", "tổng hợp chắt lọc tri thức", "Researchers synthesize disparate findings into coherent frameworks.", "Các nhà nghiên cứu tổng hợp các phát hiện rời rạc thành khung lý thuyết mạch lạc.", "Synthesis."),
        ("differentiate", "/ˌdɪf.əˈren.ʃi.eɪt/", "phân biệt bản chất khác nhau", "Experts differentiate benign symptoms from chronic conditions.", "Chuyên gia phân biệt triệu chứng lành tính với bệnh mãn tính.", "Differentiate A from B."),
        ("extrapolate", "/ɪkˈstræp.ə.leɪt/", "ngoại suy dự đoán tương lai", "We cannot extrapolate long-term trends from a single survey.", "Chúng ta không thể ngoại suy xu hướng dài hạn chỉ từ một cuộc khảo sát đơn lẻ.", "Statistical extrapolation."),
        ("deduce", "/dɪˈduːs/", "diễn dịch suy luận logic", "From mathematical proofs, physicists deduced particle mass.", "Từ các chứng minh toán học, các nhà vật lý đã suy luận ra khối lượng hạt.", "Deductive reasoning."),
        ("induce", "/ɪnˈduːs/", "quy nạp logic, gây cảm ứng", "Certain chemicals induce rapid cellular mutations.", "Một số hóa chất gây ra sự đột biến tế bào nhanh chóng.", "Inductive logic."),
        ("empirical", "/emˈpɪr.ɪ.kəl/", "dựa trên chứng cứ thực nghiệm", "Conclusions must rest upon rigorous empirical verification.", "Kết luận phải dựa trên sự xác minh thực nghiệm nghiêm ngặt.", "Empirical research."),
        ("methodology", "/ˌmeθ.əˈdɑː.lə.dʒi/", "phương pháp luận nghiên cứu", "A transparent methodology ensures reproducible science.", "Một phương pháp luận minh bạch đảm bảo khoa học có thể tái lập được.", "Research methodology."),
        ("paradigm", "/ˈper.ə.daɪm/", "mô hình mẫu hệ tư duy", "Quantum computing sparks a paradigm shift in cryptography.", "Điện toán lượng tử châm ngòi cho bước chuyển hệ hình trong mật mã học.", "Paradigm shift."),
        ("fallacy", "/ˈfæl.ə.si/", "ngụy biện logic sai lầm", "The ad hominem attack is a classic rhetorical fallacy.", "Công kích cá nhân là một ngụy biện tu từ học kinh điển.", "Logical fallacy."),
        ("plausible", "/ˈplɑː.zə.bəl/", "nghe hợp lý đáng tin", "He offered a plausible defense during the panel inquiry.", "Anh ấy đã đưa ra lời giải thích hợp lý trong buổi điều trần trước hội đồng.", "Plausibility."),
        ("ambiguous", "/æmˈbɪɡ.ju.əs/", "mơ hồ nước đôi khó đoán", "Ambiguous contractual clauses invite prolonged litigation.", "Những điều khoản hợp đồng mơ hồ sẽ dẫn tới kiện tụng kéo dài.", "Ambiguity."),
        ("coherent", "/koʊˈhɪr.ənt/", "mạch lạc gắn kết chặt chẽ", "She constructed a coherent narrative across all five chapters.", "Cô ấy đã xây dựng câu chuyện mạch lạc xuyên suốt cả năm chương.", "Coherence."),
        ("substantiate", "/səbˈstæn.ʃi.eɪt/", "chứng minh bằng số liệu thật", "The journalist substantiated allegations with verified leaks.", "Nhà báo đã chứng minh các cáo buộc bằng các tài liệu rò rỉ đã xác thực.", "Bổ sung bằng chứng."),
        ("refute", "/rɪˈfjuːt/", "bác bỏ đanh thép luận điểm", "Peer reviews successfully refuted the flawed conclusions.", "Đánh giá đồng cấp đã bác bỏ thành công những kết luận sai sót.", "Refutation."),
        ("anomalous", "/əˈnɑː.mə.ləs/", "dị thường khác quy luật", "Anomalous seismic activity preceded the volcanic eruption.", "Hoạt động địa chấn dị thường đã xuất hiện trước vụ phun trào núi lửa.", "Anomaly."),
        ("prevalent", "/ˈprev.əl.ənt/", "thịnh hành lan rộng", "Sedentary lifestyles are increasingly prevalent among youth.", "Lối sống lười vận động ngày càng phổ biến trong giới trẻ.", "Prevalence."),
        ("ubiquitous", "/juːˈbɪk.wə.t̬əs/", "hiện diện khắp mọi ngóc ngách", "Microplastics have become ubiquitous in ocean marine life.", "Hạt vi nhựa đã trở nên phổ biến khắp nơi trong sinh vật biển đại dương.", "Omnipresent."),
        ("disseminate", "/dɪˈsem.ə.neɪt/", "phổ biến lan truyền thông điệp", "Public agencies disseminate vital immunization advisories.", "Các cơ quan công quyền phổ biến những khuyến cáo tiêm chủng thiết yếu.", "Dissemination."),
        ("rigorous", "/ˈrɪɡ.ɚ.əs/", "nghiêm ngặt khắt khe chuẩn mực", "Academic journals require rigorous double-blind peer review.", "Các tạp chí học thuật đòi hỏi phản biện kín hai chiều nghiêm ngặt.", "Rigorous standards."),
        ("meticulous", "/məˈtɪk.jə.ləs/", "tỉ mỉ chăm chút từng ly", "The historian compiled a meticulous account of the treaty.", "Nhà sử học đã biên soạn một ghi chép tỉ mỉ về hiệp ước.", "Meticulously researched."),
        ("pragmatic", "/præɡˈmæt̬.ɪk/", "thực tế trọng hiệu năng", "We advocate for pragmatic compromise over partisan deadlock.", "Chúng tôi ủng hộ sự thỏa hiệp thực tế thay vì bế tắc giữa các đảng phái.", "Pragmatism."),
        ("dogmatic", "/dɑːɡˈmæt̬.ɪk/", "giáo điều độc đoán bảo thủ", "Dogmatic beliefs impede intellectual curiosity and dialogue.", "Những niềm tin giáo điều cản trở trí tò mò tri thức và đối thoại.", "Dogmatism."),
        ("nuance", "/ˈnuː.ɑːns/", "sắc thái tinh vi nhạy bén", "Skilled diplomats perceive emotional nuances in subtle phrasing.", "Các nhà ngoại giao lão luyện nhận biết được sắc thái cảm xúc trong từng cách diễn đạt tinh tế.", "Nuanced perspective."),
        ("implication", "/ˌɪm.pləˈkeɪ.ʃən/", "hệ quả sâu xa ngầm hiểu", "Gene editing entails profound ethical implications.", "Chỉnh sửa gen kéo theo những hệ lụy đạo đức sâu sắc.", "Policy implications."),
        ("inherent", "/ɪnˈhɪr.ənt/", "cố hữu vốn có trong bản chất", "Volatility is an inherent attribute of developing markets.", "Sự bất ổn là thuộc tính cố hữu của các thị trường đang phát triển.", "Inherent risk."),
        ("paramount", "/ˈper.ə.maʊnt/", "tối thượng quan trọng số một", "National cybersecurity integrity is of paramount urgency.", "Sự toàn vẹn an ninh mạng quốc gia là điều cấp bách tối thượng.", "Of paramount importance."),
        ("indispensable", "/ˌɪn.dɪˈspen.sə.bəl/", "không thể thiếu tách rời", "Critical reasoning is indispensable in democratic discourse.", "Tư duy phản biện là điều không thể thiếu trong diễn ngôn dân chủ.", "Indispensable asset."),
        ("obsolete", "/ˌɑːb.səˈliːt/", "lỗi thời bị đào thải", "Manual switches were rendered obsolete by smart automation.", "Công tắc cơ học đã bị đào thải bởi tự động hóa thông minh.", "Planned obsolescence."),
        ("pervasive", "/pɚˈveɪ.sɪv/", "thâm nhập lan tỏa ngấm sâu", "Corruption exerts a pervasive drag on economic progress.", "Tham nhũng tạo ra lực cản ngấm sâu vào tiến trình kinh tế.", "Pervasive influence."),
        ("detrimental", "/ˌdet.rəˈmen.t̬əl/", "gây tổn hại nghiêm trọng", "Chronic anxiety is detrimental to cardiovascular vitality.", "Lo âu mãn tính gây tổn hại đến sức sống của hệ tim mạch.", "Detrimental impact."),
        ("salient", "/ˈseɪ.li.ənt/", "nổi cộm đáng chú ý nhất", "Highlight the salient differences between both policy drafts.", "Hãy làm nổi bật những khác biệt nổi cộm giữa hai bản thảo chính sách.", "Salient points."),
        ("adversity", "/ədˈvɜːr.sə.t̬i/", "nghịch cảnh phong ba bão táp", "Communities showed immense dignity amidst severe adversity.", "Cộng đồng đã thể hiện sự tôn nghiêm lớn lao giữa nghịch cảnh khắc nghiệt.", "Overcome adversity."),
        ("unprecedented", "/ʌnˈpres.ə.den.t̬ɪd/", "chưa từng có tiền lệ lịch sử", "Astronomers observed an unprecedented supernova explosion.", "Các nhà thiên văn đã quan sát thấy một vụ nổ siêu tân tinh chưa từng có tiền lệ.", "Unprecedented scale."),
        ("conducive", "/kənˈduː.sɪv/", "thuận lợi đưa đến kết quả tốt", "Collaborative culture is conducive to breakthrough innovation.", "Văn hóa cộng tác tạo điều kiện thuận lợi cho đổi mới mang tính đột phá.", "Conducive environment."),
        ("exemplify", "/ɪɡˈzem.plə.faɪ/", "là minh chứng điển hình", "His civic leadership exemplifies genuine public duty.", "Sự lãnh đạo phụng sự cộng đồng của ông là minh chứng điển hình cho nghĩa vụ công dân thực thụ.", "Exemplary conduct."),
        ("catalyst", "/ˈkæt̬.əl.ɪst/", "chất xúc tác tạo đột biến", "Urban density acted as a catalyst for cultural exchange.", "Mật độ đô thị đóng vai trò là chất xúc tác cho giao lưu văn hóa.", "Catalyst for change."),
        ("alleviate", "/əˈliː.vi.eɪt/", "xoa dịu giảm tải gánh nặng", "Targeted subsidies alleviate extreme child poverty.", "Trợ cấp có mục tiêu giúp giảm bớt tình trạng nghèo đói cùng cực ở trẻ em.", "Alleviate suffering."),
        ("tangible", "/ˈtæn.dʒə.bəl/", "hữu hình thấy và đo lường được", "Solar subsidies generated tangible reductions in utility bills.", "Trợ giá điện mặt trời đã tạo ra sự sụt giảm hữu hình trên hóa đơn tiện ích.", "Tangible benefits."),
        ("intangible", "/ɪnˈtæn.dʒə.bəl/", "vô hình mang giá trị tinh thần", "Brand reputation remains a company's priceless intangible asset.", "Danh tiếng thương hiệu vẫn là tài sản vô hình vô giá của công ty.", "Intangible cultural heritage."),
        ("juxtapose", "/ˌdʒʌk.stəˈpoʊz/", "đặt cạnh nhau để đối chiếu", "The documentary juxtaposes lavish wealth with squalor.", "Bộ phim tài liệu đặt sự giàu sang xa hoa đối chiếu bên cạnh cảnh bần hàn.", "Juxtaposition."),
        ("quintessential", "/ˌkwɪn.təˈsen.ʃəl/", "mang tính tinh hoa bản sắc nhất", "The cozy tea room is the quintessential English encounter.", "Phòng trà ấm cúng là trải nghiệm mang đậm bản sắc tinh túy nhất của nước Anh.", "Quintessence."),
        ("disparity", "/dɪˈspær.ə.t̬i/", "sự chênh lệch bất bình đẳng", "Widening wealth disparity strains societal cohesion.", "Khoảng cách giàu nghèo gia tăng gây căng thẳng cho sự gắn kết xã hội.", "Economic disparity."),
        ("ephemeral", "/əˈfem.ɚ.əl/", "phù du chóng vánh ngắn ngủi", "Social media virality offers only ephemeral celebrity status.", "Sự lan truyền trên mạng xã hội chỉ mang lại danh tiếng phù du thoáng chốc.", "Ephemeral trend."),
        ("profound", "/prəˈfaʊnd/", "thâm thúy sâu sắc tột bậc", "Theoretical physics prompts profound philosophical inquiries.", "Vật lý lý thuyết gợi mở những câu hỏi triết học sâu sắc tột bậc.", "Profound insight."),
        ("superficial", "/ˌsuː.pɚˈfɪʃ.əl/", "nông cạn hời hợt trên bề mặt", "A superficial analysis overlooks systemic underlying causes.", "Một phân tích hời hợt sẽ bỏ qua các nguyên nhân mang tính hệ thống bên dưới.", "Superficial knowledge."),
        ("ubiquity", "/juːˈbɪk.wə.t̬i/", "sự phổ biến diện rộng", "The ubiquity of digital screens reshapes human attention spans.", "Sự hiện diện ở khắp mọi nơi của màn hình số đang định hình lại khả năng tập trung của con người.", "Ubiquitous nature.")
    ],

    "Tính cách & Phẩm chất": [
        ("resilient", "/rɪˈzɪl.jənt/", "kiên cường bất khuất phục hồi nhanh", "Resilient communities rebuild promptly following natural catastrophes.", "Những cộng đồng kiên cường tái thiết nhanh chóng sau các thảm họa tự nhiên.", "Resilience."),
        ("empathetic", "/ˌem.pəˈθet̬.ɪk/", "biết thấu cảm lắng nghe sâu sắc", "Empathetic doctors understand nonverbal distress signals.", "Bác sĩ biết thấu cảm sẽ hiểu các tín hiệu đau đớn không lời của người bệnh.", "Empathy."),
        ("diligent", "/ˈdɪl.ə.dʒənt/", "chăm chỉ cần mẫn tỉ mẩn", "Diligent archival research corrected erroneous historical dates.", "Nghiên cứu văn khố cần mẫn đã đính chính các mốc thời gian lịch sử sai sót.", "Diligence."),
        ("versatile", "/ˈvɝː.sə.t̬əl/", "đa năng thích nghi linh hoạt", "Versatile engineers transition seamlessly across development stacks.", "Kỹ sư đa năng chuyển đổi mượt mà giữa các nền tảng công nghệ phát triển.", "Versatility."),
        ("prudent", "/ˈpruː.dənt/", "thận trọng biết nhìn xa trông rộng", "Prudent fiscal governance insulated the economy from crashes.", "Quản trị tài khóa thận trọng đã bảo vệ nền kinh tế khỏi các cú sụp đổ.", "Prudence."),
        ("articulate", "/ɑːrˈtɪk.jə.lət/", "ăn nói lưu loát gãy gọn thuyết phục", "Articulate advocates galvanize public backing for legal reforms.", "Những người ủng hộ hoạt ngôn đã kích hoạt sự hậu thuẫn của công chúng cho cải cách pháp luật.", "Articulate speaker."),
        ("diplomatic", "/ˌdɪp.ləˈmæt̬.ɪk/", "khéo léo ngoại giao hòa giải", "Her diplomatic approach defused heated boardroom confrontations.", "Cách tiếp cận khéo léo của cô ấy đã hóa giải các cuộc đối đầu gay gắt trong phòng họp.", "Diplomacy."),
        ("skeptical", "/ˈskep.tɪ.kəl/", "hoài nghi khoa học không nhẹ dạ", "Be skeptical of miraculous health claims lacking clinical backing.", "Hãy hoài nghi những tuyên bố sức khỏe kỳ diệu thiếu chứng minh lâm sàng.", "Healthy skepticism."),
        ("ambitious", "/æmˈbɪʃ.əs/", "hoài bão lớn lao khát vọng", "The young scientist embarked on an ambitious fusion experiment.", "Nhà khoa học trẻ đã bắt tay vào một thí nghiệm nhiệt hạch đầy tham vọng.", "Ambition."),
        ("tenacious", "/təˈneɪ.ʃəs/", "gan góc ngoan cường bám đuổi", "Her tenacious persistence yielded justice for vulnerable victims.", "Sự kiên trì gan góc của cô ấy đã đem lại công lý cho các nạn nhân yếu thế.", "Tenacity."),
        ("candid", "/ˈkæn.dɪd/", "bộc trực chân tình không né tránh", "In a candid interview, the minister admitted policy oversights.", "Trong cuộc phỏng vấn bộc trực, ngài bộ trưởng đã thừa nhận những sơ suất chính sách.", "Candid remarks."),
        ("charismatic", "/ˌker.ɪzˈmæt̬.ɪk/", "cuốn hút thần thái quyến rũ", "The charismatic founder rallied investors behind her green vision.", "Người sáng lập đầy lôi cuốn đã tập hợp các nhà đầu tư ủng hộ tầm nhìn xanh của mình.", "Charisma."),
        ("altruistic", "/ˌæl.truˈɪs.tɪk/", "vị tha không màng tư lợi", "Altruistic donors established endowments for orphan scholarships.", "Các nhà hảo tâm vị tha đã thành lập quỹ học bổng cho trẻ mồ côi.", "Altruism."),
        ("resourceful", "/rɪˈzɔːr.sfəl/", "tháo vát biết xoay xở", "Resourceful navigators survived blizzards with rudimentary tools.", "Những người hoa tiêu tháo vát đã sống sót qua bão tuyết bằng công cụ thô sơ.", "Resourcefulness."),
        ("stoic", "/ˈstoʊ.ɪk/", "khắc kỷ bất biến giữa dòng đời", "Stoic endurance enabled prisoners of war to retain dignity.", "Sự chịu đựng khắc kỷ đã giúp các tù binh chiến tranh giữ trọn phẩm giá.", "Stoicism."),
        ("fastidious", "/fæsˈtɪd.i.əs/", "cầu toàn kỹ tính từng tiểu tiết", "The curator is fastidious about museum lighting angles.", "Người phụ trách triển lãm rất kỹ tính về các góc chiếu sáng trong bảo tàng.", "Fastidious taste."),
        ("astute", "/əˈstuːt/", "sắc sảo tinh tường mẫn tiệp", "Astute negotiators foresee opponent counterarguments effortlessly.", "Những nhà đàm phán sắc sảo lường trước các phản biện của đối phương rất dễ dàng.", "Astute businessman."),
        ("magnanimous", "/mæɡˈnæn.ə.məs/", "đại lượng hào hiệp bao dung", "The statesman was magnanimous towards defeated political adversaries.", "Vị chính khách đã cư xử hết sức đại lượng đối với các đối thủ chính trị vừa bại trận.", "Magnanimity."),
        ("complacent", "/kəmˈpleɪ.sənt/", "tự mãn lơ là cảnh giác", "Never become complacent when leading a volatile sector.", "Đừng bao giờ trở nên tự mãn khi đang dẫn đầu trong một ngành đầy biến động.", "Complacency."),
        ("cynical", "/ˈsɪn.ɪ.kəl/", "yếm thế bi quan hoài nghi động cơ", "He grew cynical after witnessing pervasive political cronyism.", "Anh ấy trở nên bi quan cay đắng sau khi chứng kiến tệ nạn bè phái chính trị lan tràn.", "Cynicism."),
        ("affable", "/ˈæf.ə.bəl/", "niềm nở dễ gần hiền hòa", "The diplomat's affable demeanor calmed tense international talks.", "Thần thái niềm nở của vị nhà ngoại giao đã làm dịu các cuộc đàm phán quốc tế căng thẳng.", "Affability."),
        ("gregarious", "/ɡrɪˈɡer.i.əs/", "thích giao thiệp hòa đồng bầy đàn", "Gregarious extroverts recharge through dynamic collective gatherings.", "Những người hướng ngoại thích giao thiệp nạp năng lượng qua các buổi tụ họp tập thể sôi nổi.", "Social butterfly."),
        ("introspective", "/ˌɪn.trəˈspek.tɪv/", "hướng nội trầm tư soi mình", "Solitude fosters deeply introspective philosophical contemplation.", "Sự tĩnh lặng thúc đẩy những chiêm nghiệm triết học nội tâm sâu sắc.", "Introspection."),
        ("eccentric", "/ɪkˈsen.trɪk/", "lập dị quái tính độc đáo", "The eccentric inventor lived in a sprawling mansion filled with clocks.", "Nhà phát minh lập dị sống trong một dinh thự rộng lớn chứa đầy đồng hồ.", "Eccentricity."),
        ("audacious", "/ɑːˈdeɪ.ʃəs/", "táo bạo liều lĩnh cả gan", "Mounting an expedition through uncharted glaciers was an audacious feat.", "Tổ chức một chuyến thám hiểm qua sông băng chưa vẽ bản đồ là kỳ tích táo bạo.", "Audacity."),
        ("scrupulous", "/ˈskruː.pjə.ləs/", "nghiêm cẩn liêm chính đạo đức", "The magistrate was scrupulous in adhering to statutory precedent.", "Vị thẩm phán rất nghiêm cẩn trong việc tuân thủ tiền lệ luật định.", "Scrupulous honesty."),
        ("unwavering", "/ʌnˈweɪ.vɚ.ɪŋ/", "vững như bàn thạch không nao núng", "She pursued educational reform with unwavering resolve.", "Cô ấy theo đuổi cải cách giáo dục với quyết tâm không hề nao núng.", "Unwavering commitment."),
        ("vivacious", "/vɪˈveɪ.ʃəs/", "hoạt bát tràn trề sinh lực", "Her vivacious stage presence invigorated classical theater audiences.", "Phong thái biểu diễn hoạt bát trên sân khấu của cô ấy đã tiếp thêm sinh lực cho khán giả kịch cổ điển.", "Vivacity."),
        ("discerning", "/dɪˈsɝː.nɪŋ/", "tinh tế sành sỏi có gu", "Discerning art collectors spot authentic Renaissance masterworks.", "Những nhà sưu tập nghệ thuật sành sỏi nhận diện được các kiệt tác Phục hưng đích thực.", "Discerning palate/eye."),
        ("benevolent", "/bəˈnev.əl.ənt/", "nhân từ bác ái hiền đức", "The benevolent monarch funded free healthcare sanctuaries.", "Vị minh quân nhân từ đã tài trợ cho các trung tâm y tế chữa bệnh miễn phí.", "Benevolence.")
    ],

    "Thành ngữ & Cụm từ hay": [
        ("take something for granted", "/teɪk fɔːr ˈɡræn.t̬ɪd/", "coi là điều hiển nhiên không quý trọng", "Never take family solidarity for granted amidst turbulence.", "Đừng bao giờ coi sự đoàn kết gia đình là điều hiển nhiên giữa sóng gió cuộc đời.", "Trân trọng những gì đang có."),
        ("see eye to eye", "/siː aɪ tuː aɪ/", "đồng thuận hoàn toàn cùng góc nhìn", "The co-founders rarely see eye to eye on scaling priorities.", "Hai nhà đồng sáng lập hiếm khi cùng chung góc nhìn về các ưu tiên mở rộng quy mô.", "See eye to eye on."),
        ("play it by ear", "/pleɪ ɪt baɪ ɪr/", "tùy cơ ứng biến theo tình huống", "Without fixed itineraries, backpackers prefer to play it by ear.", "Không có lịch trình cố định, dân phượt thích tùy cơ ứng biến hơn.", "Improvise."),
        ("burn the midnight oil", "/bɜːrn ðə ˈmɪd.naɪt ɔɪl/", "thức thâu đêm cày cuốc học làm", "Legal teams burned the midnight oil perfecting trial briefs.", "Đội ngũ pháp lý đã thức trắng đêm để hoàn thiện bản tóm tắt hồ sơ xét xử.", "Làm việc miệt mài."),
        ("cost an arm and a leg", "/kɔːst ən ɑːrm ənd ə leɡ/", "đắt cắt cổ ngốn cả gia tài", "Specialized medical treatments abroad cost an arm and a leg.", "Các phương pháp điều trị y tế chuyên biệt ở nước ngoài tốn kém cả một gia tài.", "Exorbitant cost."),
        ("touch base with someone", "/tʌtʃ beɪs wɪð/", "liên lạc cập nhật tình hình nhanh", "Let us touch base next Wednesday to assess quarterly targets.", "Thứ Tư tới chúng ta hãy liên lạc lại để đánh giá các mục tiêu quý nhé.", "Brief check-in."),
        ("call it a day", "/kɔːl ɪt ə deɪ/", "dừng tay kết thúc buổi làm", "After resolving critical bugs, developers decided to call it a day.", "Sau khi gỡ xong các lỗi nghiêm trọng, các lập trình viên quyết định dừng tay.", "Wrap up."),
        ("bite the bullet", "/baɪt ðə ˈbʊl.ɪt/", "nghiến răng đương đầu việc khó", "The CFO bit the bullet and announced necessary workforce reductions.", "Giám đốc tài chính đã cắn răng chịu đựng công bố đợt cắt giảm nhân sự bắt buộc.", "Face inevitable hardship."),
        ("think outside the box", "/θɪŋk aʊtˈsaɪd ðə bɑːks/", "tư duy đột phá vượt lối mòn", "Engineers had to think outside the box to bypass thermal limits.", "Các kỹ sư phải tư duy vượt lối mòn để vượt qua các giới hạn nhiệt năng.", "Innovative thinking."),
        ("hit the nail on the head", "/hɪt ðə neɪl ɑːn ðə hed/", "nói trúng phóc trọng tâm vấn đề", "Her appraisal hit the nail on the head regarding customer churn.", "Đánh giá của cô ấy đã nói trúng phóc nguyên nhân khách hàng rời bỏ dịch vụ.", "Spot on."),
        ("break the ice", "/breɪk ðə aɪs/", "phá vỡ sự ngại ngùng ban đầu", "An interactive icebreaker broke the ice among hesitant delegates.", "Một hoạt động giao lưu tương tác đã phá vỡ sự ngại ngùng giữa các đại biểu.", "Icebreaking."),
        ("burn bridges", "/bɜːrn ˈbrɪdʒ.ɪz/", "chặt đứt đường lui tuyệt giao", "Resign professionally; burning bridges limits future career prospects.", "Hãy từ chức một cách chuyên nghiệp; cắt đứt mọi mối quan hệ sẽ hạn chế triển vọng nghề nghiệp tương lai.", "Preserve relationships."),
        ("read between the lines", "/riːd bɪˈtwiːn ðə laɪnz/", "đọc ra ẩn ý đằng sau câu chữ", "Diplomats read between the lines of subtle official communiqués.", "Các nhà ngoại giao đọc ra ẩn ý đằng sau những thông cáo chính thức tinh tế.", "Discern hidden meaning."),
        ("under the weather", "/ˈʌn.dɚ ðə ˈweð.ɚ/", "khó ở trong người ốm nhẹ", "The keynote speaker felt under the weather and postponed the lecture.", "Diễn giả chính cảm thấy không được khỏe và đã hoãn bài giảng.", "Minor illness."),
        ("on the fence", "/ɑːn ðə fens/", "lưỡng lự chưa ngã ngũ lập trường", "Undecided committee members remain on the fence about the merger.", "Những thành viên ủy ban chưa quyết định vẫn đang lưỡng lự về thương vụ sáp nhập.", "Ambivalent."),
        ("the tip of the iceberg", "/ðə tɪp əv ðiː ˈaɪs.bɜːrɡ/", "mới chỉ là phần nổi tảng băng chìm", "These recorded leaks are merely the tip of the iceberg.", "Những vụ rò rỉ được ghi nhận này mới chỉ là phần nổi của tảng băng chìm.", "Deeper systemic issue."),
        ("actions speak louder than words", "/ˈæk.ʃənz spiːk ˈlaʊ.dɚ ðæn wɜːrdz/", "hành động có sức nặng hơn lời hứa", "Authentic reformers realize actions speak louder than words.", "Những nhà cải cách thực thụ hiểu rằng hành động có sức nặng hơn muôn vàn lời hứa.", "Tangible proof."),
        ("back to the drawing board", "/bæk tuː ðə ˈdrɑː.ɪŋ bɔːrd/", "quay lại làm lại từ đầu", "The prototype failed aerodynamics testing; it is back to the drawing board.", "Mẫu thử nghiệm đã trượt bài kiểm tra khí động học; chúng ta phải quay lại làm lại từ đầu.", "Restart planning."),
        ("cut corners", "/kʌt ˈkɔːr.nɚz/", "đốt cháy giai đoạn làm ẩu", "Aviation maintenance teams must never cut corners on inspections.", "Đội ngũ bảo trì hàng không tuyệt đối không được làm ẩu bớt xén khâu kiểm tra.", "Compromise quality."),
        ("bark up the wrong tree", "/bɑːrk ʌp ðə rɑːŋ triː/", "đi sai hướng gõ nhầm cửa", "Investigators barked up the wrong tree tracing cryptocurrency wallets.", "Các điều tra viên đã đi sai hướng khi lần theo các ví tiền mã hóa đó.", "Misdirected effort."),
        ("a blessing in disguise", "/ə ˈbles.ɪŋ ɪn dɪsˈɡaɪz/", "trong cái rủi có cái may", "Losing that client proved a blessing in disguise as better contracts surfaced.", "Mất khách hàng đó hóa ra lại là trong cái rủi có cái may khi các hợp đồng tốt hơn xuất hiện.", "Hidden benefit."),
        ("spill the beans", "/spɪl ðə biːnz/", "làm lộ bí mật bật mí sớm", "An insider spilled the beans before the official product unveiling.", "Một người nội bộ đã làm lộ bí mật trước buổi ra mắt sản phẩm chính thức.", "Divulge secret."),
        ("through thick and thin", "/θruː θɪk ænd θɪn/", "đồng cam cộng khổ mọi thăng trầm", "Loyal business partners stood together through thick and thin.", "Những đối tác kinh doanh trung thành đã sát cánh bên nhau qua mọi thăng trầm.", "Unconditional support."),
        ("bite off more than one can chew", "/baɪt ɔːf mɔːr ðæn wʌn kæn tʃuː/", "ôm đồm quá sức gánh vác", "Do not bite off more than you can chew by accepting three concurrent roles.", "Đừng ôm đồm quá sức bằng việc nhận cùng lúc ba vị trí công việc.", "Overcommit."),
        ("the elephant in the room", "/ðə ˈel.ə.fənt ɪn ðə ruːm/", "vấn đề nhức nhối ai cũng tránh né", "Dwindling cash reserves was the elephant in the room nobody mentioned.", "Khoản dự trữ tiền mặt cạn kiệt là vấn đề nhức nhối hiển nhiên mà không ai dám nhắc tới.", "Avoided obvious topic."),
        ("leave no stone unturned", "/liːv noʊ stoʊn ʌnˈtɜːrnd/", "lùng sục khắp nơi không bỏ sót", "Forensic auditors left no stone unturned during fraud investigations.", "Các kiểm toán viên pháp y đã lùng sục khắp nơi không bỏ sót dấu vết trong điều tra gian lận.", "Exhaustive search."),
        ("ahead of the curve", "/əˈhed əv ðə kɝːv/", "đi trước thời đại đón đầu xu thế", "Innovative biotech ventures invest early to remain ahead of the curve.", "Các doanh nghiệp công nghệ sinh học đổi mới đầu tư sớm để luôn đi trước thời đại.", "Trendsetter."),
        ("throw in the towel", "/θroʊ ɪn ðə ˈtaʊ.əl/", "bỏ cuộc giương cờ trắng", "Despite heavy setbacks, the plucky startup refused to throw in the towel.", "Bất chấp những trở ngại nặng nề, công ty khởi nghiệp kiên cường đã từ chối bỏ cuộc.", "Surrender."),
        ("at the eleventh hour", "/æt ðiː ɪˈlev.ənθ aʊr/", "vào phút chót sát nút", "Diplomats brokered an emergency ceasefire at the eleventh hour.", "Các nhà ngoại giao đã dàn xếp một thỏa thuận ngừng bắn khẩn cấp vào phút chót.", "Last-minute."),
        ("face the music", "/feɪs ðə ˈmjuː.zɪk/", "đứng mũi chịu sào nhận hậu quả", "Having mismanaged public funds, administrators had to face the music.", "Sau khi quản lý yếu kém công quỹ, các nhà quản lý đã phải đứng ra gánh chịu hậu quả.", "Accept consequences.")
    ],

    "Tài chính & Kinh tế": [
        ("inflation", "/ɪnˈfleɪ.ʃən/", "lạm phát phi mã tiền mất giá", "Persistent inflation erodes purchasing power for middle-class households.", "Lạm phát dai dẳng làm xói mòn sức mua của các hộ gia đình trung lưu.", "Hyperinflation."),
        ("recession", "/rɪˈseʃ.ən/", "suy thoái kinh tế đình đốn", "Consecutive quarters of negative growth tipped the continent into recession.", "Các quý tăng trưởng âm liên tiếp đã đẩy toàn bộ châu lục vào suy thoái.", "Economic downturn."),
        ("liquidity", "/lɪˈkwɪd.ə.t̬i/", "tính thanh khoản tiền mặt", "Commercial banks maintain high liquidity reserves to survive credit squeezes.", "Các ngân hàng thương mại duy trì dự trữ thanh khoản cao để sống sót qua cơn siết tín dụng.", "Liquid assets."),
        ("volatility", "/ˌvɑː.ləˈtɪl.ə.t̬i/", "độ biến động biên độ giá lớn", "Geopolitical turmoil triggers violent volatility across commodity markets.", "Bất ổn địa chính trị gây ra sự biến động giá dữ dội trên khắp các thị trường hàng hóa.", "Volatile swing."),
        ("dividend", "/ˈdɪv.ə.dend/", "cổ tức chia cho cổ đông", "Dividend-yielding equities appeal to conservative pension investors.", "Cổ phiếu trả cổ tức thu hút các nhà đầu tư quỹ hưu trí thận trọng.", "Dividend payout."),
        ("equity", "/ˈek.wə.t̬i/", "vốn chủ sở hữu, cổ phần", "Venture capital syndicates acquire equity in promising artificial intelligence labs.", "Các liên minh quỹ đầu tư mạo hiểm mua cổ phần trong các phòng thí nghiệm AI triển vọng.", "Private equity."),
        ("depreciation", "/dɪˌpriː.ʃiˈeɪ.ʃən/", "khấu hao tài sản cố định", "Tax accounting deductions account for real estate asset depreciation.", "Các khoản khấu trừ kế toán thuế ghi nhận sự khấu hao tài sản bất động sản.", "Depreciate."),
        ("portfolio", "/ˌpɔːrtˈfoʊ.li.oʊ/", "danh mục đầu tư tài chính", "Rebalancing your investment portfolio annually preserves risk-adjusted gains.", "Tái cân bằng danh mục đầu tư hàng năm giúp bảo toàn lợi nhuận đã điều chỉnh rủi ro.", "Asset allocation."),
        ("acquisition", "/ˌæk.wəˈzɪʃ.ən/", "thương vụ thâu tóm doanh nghiệp", "Hostile takeover attempts preceded the contested corporate acquisition.", "Những nỗ lực thâu tóm thù địch đã diễn ra trước thương vụ mua lại gây tranh cãi.", "Mergers and acquisitions."),
        ("insolvent", "/ɪnˈsɑːl.vənt/", "mất khả năng thanh toán nợ nần", "Without swift capital injection, regional developers risk becoming insolvent.", "Nếu không có sự bơm vốn nhanh chóng, các nhà phát triển địa phương có nguy cơ mất khả năng trả nợ.", "Insolvency."),
        ("conglomerate", "/kənˈɡlɑː.mɚ.ət/", "tập đoàn kinh tế khổng lồ", "The multinational conglomerate divested its fossil fuel extraction assets.", "Tập đoàn đa quốc gia khổng lồ đã thoái vốn khỏi các tài sản khai thác nhiên liệu hóa thạch.", "Industrial conglomerate."),
        ("speculation", "/ˌspek.jəˈleɪ.ʃən/", "đầu cơ lướt sóng tích trữ", "Curbing speculative trading dampens artificial asset bubble expansion.", "Hạn chế giao dịch đầu cơ giúp kiềm chế sự phình to của bong bóng tài sản nhân tạo.", "Speculative bubble."),
        ("fiscal", "/ˈfɪs.kəl/", "thuộc chính sách tài khóa nhà nước", "Disciplined fiscal spending prevents sovereign debt credit downgrades.", "Chi tiêu tài khóa có kỷ luật ngăn chặn việc bị hạ xếp hạng tín nhiệm nợ quốc gia.", "Fiscal stimulus."),
        ("monetary", "/ˈmʌn.ə.ter.i/", "thuộc chính sách tiền tệ lãi suất", "Tight monetary policy reins in runaway consumer price indices.", "Chính sách tiền tệ thắt chặt kìm hãm chỉ số giá tiêu dùng tăng phi mã.", "Monetary tightening."),
        ("yield", "/jiːld/", "lợi suất sinh lời đầu tư", "Inverted treasury bond yield curves reliably predict impending recessions.", "Đường cong lợi suất trái phiếu kho bạc đảo ngược dự báo chuẩn xác suy thoái sắp ập đến.", "Yield curve."),
        ("amortization", "/ˌæm.ɚ.t̬əˈzeɪ.ʃən/", "khấu hao tài sản vô hình", "Intangible software licenses undergo structured amortization schedules.", "Bản quyền phần mềm vô hình trải qua lịch trình phân bổ khấu hao có cấu trúc.", "Amortize debt."),
        ("arbitrage", "/ˈɑːr.bə.trɑːʒ/", "kinh doanh chênh lệch giá", "High-frequency hedge funds exploit minuscule currency arbitrage spreads.", "Các quỹ phòng hộ tần suất cao tận dụng chênh lệch giá tiền tệ siêu nhỏ để kiếm lời.", "Riskless arbitrage."),
        ("collateral", "/kəˈlæt̬.ɚ.əl/", "tài sản thế chấp cầm cố", "Commercial borrowers pledge valuable commercial property as collateral.", "Bên đi vay thương mại thế chấp bất động sản thương mại có giá trị để làm tài sản bảo đảm.", "Collateralized loan."),
        ("solvency", "/ˈsɑːl.vən.si/", "khả năng thanh toán nợ dài hạn", "Stress tests assess whether major financial lenders maintain adequate solvency.", "Các bài kiểm tra sức chịu đựng đánh giá liệu các nhà băng lớn có duy trì đủ khả năng thanh toán dài hạn hay không.", "Solvency ratio."),
        ("leverage ratio", "/ˈlev.ɚ.ɪdʒ ˈreɪ.ʃi.oʊ/", "tỷ lệ đòn bẩy tài chính", "Excessive leverage ratios amplify institutional downside vulnerability.", "Tỷ lệ đòn bẩy quá mức khuếch đại tính dễ tổn thương của tổ chức khi thị trường đi xuống.", "Debt-to-equity ratio.")
    ],

    "Mẫu câu Chuyên nghiệp": [
        ("I would appreciate it if you could clarify this matter at your earliest convenience.", "/aɪ wʊd əˈpriː.ʃi.eɪt ɪt/", "Tôi sẽ rất cảm kích nếu bạn có thể làm rõ vấn đề này vào thời gian sớm nhất có thể.", "I would appreciate it if you could clarify this matter at your earliest convenience before our client debrief.", "Tôi sẽ rất cảm kích nếu bạn có thể làm rõ vấn đề này sớm nhất có thể trước buổi báo cáo khách hàng.", "Mẫu câu nhờ vả cực kỳ trang trọng và lịch thiệp."),
        ("Could you please elaborate on that specific recommendation?", "/kʊd juː pliːz ɪˈlæb.ɚ.eɪt/", "Bạn có thể vui lòng giải thích chi tiết hơn về khuyến nghị cụ thể đó được không?", "Your model is promising; could you please elaborate on that specific recommendation regarding risk margins?", "Mô hình của bạn rất triển vọng; bạn có thể nói rõ hơn về khuyến nghị biên độ rủi ro không?", "Yêu cầu đào sâu thêm chi tiết."),
        ("Let us weigh the pros and cons meticulously before committing capital.", "/let ʌs weɪ ðə proʊz ænd kɑːnz/", "Chúng ta hãy cân nhắc thật tỉ mỉ giữa được và mất trước khi cam kết rót vốn.", "Let us weigh the pros and cons meticulously before committing capital to foreign infrastructure.", "Hãy cân nhắc kỹ lưỡng ưu nhược điểm trước khi rót vốn vào hạ tầng nước ngoài.", "Đưa ra quyết định thận trọng."),
        ("From my strategic perspective, this initiative holds immense potential.", "/frʌm maɪ strəˈtiː.dʒɪk pɚˈspek.tɪv/", "Từ góc nhìn chiến lược của tôi, sáng kiến này chứa đựng tiềm năng vô cùng lớn lao.", "From my strategic perspective, acquiring this intellectual patent holds immense potential for market leadership.", "Theo góc nhìn chiến lược của tôi, thâu tóm bằng sáng chế này đem lại tiềm năng dẫn đầu thị trường rất lớn.", "Thể hiện tầm nhìn chuyên nghiệp."),
        ("We must align our operational objectives to ensure seamless execution across departments.", "/wiː mʌst əˈlaɪn ˈaʊ.ɚ əbˈdʒek.tɪvz/", "Chúng ta phải đồng bộ hóa các mục tiêu vận hành để đảm bảo việc triển khai diễn ra liền mạch giữa các phòng ban.", "To meet the fourth quarter quota, we must align our operational objectives across all business units.", "Để đạt chỉ tiêu quý 4, chúng ta phải đồng bộ hóa các mục tiêu trên tất cả các đơn vị kinh doanh.", "Đoàn kết và phối hợp nhịp nhàng."),
        ("I am strongly inclined to endorse the proposed restructuring plan.", "/aɪ æm ˈstrɑːŋ.li ɪnˈklaɪnd tuː/", "Tôi rất có thiên hướng ủng hộ kế hoạch tái cơ cấu được đề xuất.", "Having scrutinized the cost projections, I am strongly inclined to endorse the proposed restructuring plan.", "Sau khi nghiên cứu kỹ dự toán chi phí, tôi rất nghiêng về phía ủng hộ kế hoạch tái cấu trúc này.", "Ủng hộ có căn cứ vững chắc."),
        ("Please keep me informed in the loop regarding substantive project milestones.", "/pliːz kiːp miː ɪn ðə luːp/", "Làm ơn hãy luôn cập nhật cho tôi về những cột mốc dự án thực chất tiếp theo nhé.", "As chief sponsor, please keep me informed in the loop regarding substantive project milestones.", "Với tư cách là người bảo trợ chính, xin hãy luôn cập nhật cho tôi về các cột mốc dự án cốt lõi.", "Giữ thông tin liên lạc xuyên suốt."),
        ("We should convene a follow-up session to resolve remaining discrepancies.", "/wiː ʃʊd kənˈviːn/", "Chúng ta nên triệu tập một phiên họp tiếp nối để giải quyết triệt để các sai lệch còn tồn đọng.", "Let us convene a follow-up session next Tuesday morning to reconcile ledger audits.", "Hãy triệu tập một phiên họp tiếp theo vào sáng thứ Ba tới để đối soát sổ cái kiểm toán.", "Giải quyết rốt ráo công việc."),
        ("I would like to propose a viable alternative to circumvent current constraints.", "/aɪ wʊd laɪk tuː prəˈpoʊz/", "Tôi muốn đề xuất một giải pháp thay thế khả thi nhằm vượt qua những hạn chế hiện tại.", "If suppliers fail to deliver, I would like to propose a viable alternative to circumvent current constraints.", "Nếu các nhà cung cấp không giao hàng đúng hạn, tôi xin đề xuất một phương án thay thế khả thi.", "Chủ động đưa ra giải pháp mới."),
        ("Let us touch upon the pivotal metrics governing our performance review.", "/let ʌs tʌtʃ əˈpɑːn/", "Chúng ta hãy cùng điểm qua các chỉ số then chốt chi phối đợt đánh giá hiệu suất của chúng ta.", "During today's sync, let us touch upon the pivotal metrics governing our annual operational audit.", "Trong buổi họp hôm nay, chúng ta hãy điểm qua những chỉ số then chốt chi phối đợt kiểm toán vận hành.", "Tập trung vào điểm trọng yếu.")
    ]
}

# Lắp ráp danh sách 500+ mục
ALL_ITEMS = []
for topic_name, word_list in DATA_CATEGORIES.items():
    for entry in word_list:
        text, ipa, meaning, example, ex_meaning, note = entry
        is_sentence = len(text.split()) > 4
        ALL_ITEMS.append({
            "id": f"adv-{len(ALL_ITEMS) + 1}",
            "type": "sentence" if is_sentence else "vocab",
            "text": text,
            "ipa": ipa,
            "meaning": meaning,
            "topic": topic_name,
            "example": example,
            "exampleMeaning": ex_meaning,
            "note": note,
            "status": "new",
            "dateAdded": "2026-10-08"
        })

# Thêm bổ sung thêm từ vựng B2/C1 học thuật và giao tiếp nâng cao cho đủ 500 mục
ADDITIONAL_ADVANCED = [
    # Nhóm Khoa học & Công nghệ cao
    ("algorithm", "/ˈæl.ɡə.rɪ.ðəm/", "thuật toán máy tính", "Machine learning algorithms analyze millions of medical scans.", "Thuật toán học máy phân tích hàng triệu ảnh chụp y tế.", "Algorithmic trading.", "Khoa học & Đổi mới"),
    ("cryptography", "/krɪpˈtɑː.ɡrə.fi/", "khoa học mật mã bảo mật", "Quantum computers threaten legacy asymmetric cryptography.", "Máy tính lượng tử đe dọa các hệ mật mã bất đối xứng truyền thống.", "Cryptographic protocols.", "Khoa học & Đổi mới"),
    ("automation", "/ˌɑː.t̬əˈmeɪ.ʃən/", "sự tự động hóa dây chuyền", "Industrial automation displaces repetitive manual labor.", "Tự động hóa công nghiệp thay thế lao động thủ công lặp đi lặp lại.", "Automated systems.", "Khoa học & Đổi mới"),
    ("nanotechnology", "/ˌnæn.oʊ.tekˈnɑː.lə.dʒi/", "công nghệ nano siêu vi", "Nanotechnology enables targeted drug delivery inside tumors.", "Công nghệ nano cho phép đưa thuốc trúng đích vào bên trong khối u.", "Nanoscale engineering.", "Khoa học & Đổi mới"),
    ("biotechnology", "/ˌbaɪ.oʊ.tekˈnɑː.lə.dʒi/", "công nghệ sinh học", "Biotechnology breakthroughs accelerate drought-resistant crop breeding.", "Đột phá công nghệ sinh học thúc đẩy lai tạo giống cây trồng chịu hạn.", "Biotech industry.", "Khoa học & Đổi mới"),
    ("telecommunications", "/ˌtel.ə.kəˌmjuː.nəˈkeɪ.ʃənz/", "viễn thông liên lạc", "Fiber-optic networks transformed global telecommunications.", "Mạng cáp quang đã làm biến đổi ngành viễn thông toàn cầu.", "Telecom sector.", "Khoa học & Đổi mới"),
    ("cybersecurity", "/ˈsaɪ.bɚ.səˌkjʊr.ə.t̬i/", "an ninh mạng bảo mật dữ liệu", "Financial institutions invest billions in offensive cybersecurity.", "Các tổ chức tài chính đầu tư hàng tỷ đô la vào an ninh mạng chủ động.", "Cyber attack defense.", "Khoa học & Đổi mới"),
    ("semiconductor", "/ˌsem.i.kənˈdʌk.tɚ/", "chất bán dẫn vi mạch", "Global supply disruptions choked semiconductor manufacturing.", "Sự gián đoạn nguồn cung toàn cầu đã bóp nghẹt ngành sản xuất chất bán dẫn.", "Microchip fabrication.", "Khoa học & Đổi mới"),
    ("autonomous", "/ɑːˈtɑː.nə.məs/", "tự hành tự chủ độc lập", "Autonomous drone fleets inspect offshore wind turbines.", "Các đội máy bay không người lái tự hành kiểm tra các tua-bin gió ngoài khơi.", "Autonomous vehicles.", "Khoa học & Đổi mới"),
    ("infrastructure", "/ˈɪn.frəˌstrʌk.tʃɚ/", "cơ sở hạ tầng huyết mạch", "Modernizing aging rail infrastructure requires bipartisan resolve.", "Hiện đại hóa hạ tầng đường sắt xuống cấp đòi hỏi quyết tâm của cả hai đảng.", "Critical infrastructure.", "Khoa học & Đổi mới"),

    # Nhóm Môi trường, Biến đổi & Khí hậu
    ("biodiversity", "/ˌbaɪ.oʊ.daɪˈvɝː.sə.t̬i/", "sự đa dạng sinh học", "Deforestation accelerates irreparable biodiversity loss in rainforests.", "Phá rừng đẩy nhanh sự mất mát đa dạng sinh học không thể cứu vãn ở rừng nhiệt đới.", "Ecosystem diversity.", "Môi trường & Xã hội"),
    ("deforestation", "/diːˌfɔːr.əˈsteɪ.ʃən/", "nạn phá rừng tràn lan", "Illegal deforestation threatens indigenous territories worldwide.", "Nạn phá rừng trái phép đe dọa các vùng lãnh thổ của người bản địa trên khắp thế giới.", "Reforestation.", "Môi trường & Xã hội"),
    ("emissions", "/iˈmɪʃ.ənz/", "khí thải ô nhiễm", "Stringent carbon emissions caps penalize heavy polluters.", "Mức trần phát thải carbon nghiêm ngặt sẽ phạt nặng những bên gây ô nhiễm lớn.", "Zero emissions.", "Môi trường & Xã hội"),
    ("conservation", "/ˌkɑːn.sɚˈveɪ.ʃən/", "bảo tồn thiên nhiên di sản", "Wildlife conservation preserves habitats for endangered species.", "Bảo tồn động vật hoang dã gìn giữ môi trường sống cho các loài có nguy cơ tuyệt chủng.", "Conservationist.", "Môi trường & Xã hội"),
    ("renewable", "/rɪˈnuː.ə.bəl/", "năng lượng tái tạo xanh", "Wind and solar energy represent prime renewable power sources.", "Năng lượng gió và mặt trời đại diện cho các nguồn năng lượng tái tạo hàng đầu.", "Renewable energy.", "Môi trường & Xã hội"),
    ("ecosystem", "/ˈiː.koʊˌsɪs.təm/", "hệ sinh thái tự nhiên", "Coral reef bleaching jeopardizes delicate marine ecosystems.", "Hiện tượng tẩy trắng rạn san hô đe dọa các hệ sinh thái biển mong manh.", "Ecosystem balance.", "Môi trường & Xã hội"),
    ("depletion", "/dɪˈpliː.ʃən/", "sự cạn kiệt tài nguyên", "Overfishing causes alarming resource depletion in coastal fisheries.", "Đánh bắt quá mức gây cạn kiệt tài nguyên đáng báo động ở các ngư trường ven biển.", "Ozone depletion.", "Môi trường & Xã hội"),
    ("sustainable", "/səˈsteɪ.nə.bəl/", "bền vững sinh thái", "Sustainable agriculture minimizes toxic synthetic pesticide runoff.", "Nông nghiệp bền vững giảm thiểu nước thải thuốc trừ sâu tổng hợp độc hại.", "Sustainability.", "Môi trường & Xã hội"),
    ("contamination", "/kənˌtæm.əˈneɪ.ʃən/", "sự ô nhiễm nhiễm độc", "Industrial runoff led to severe groundwater contamination.", "Nước thải công nghiệp dẫn đến tình trạng nhiễm độc nguồn nước ngầm nghiêm trọng.", "Chemical contamination.", "Môi trường & Xã hội"),
    ("urbanization", "/ˌɝː.bən.əˈzeɪ.ʃən/", "quá trình đô thị hóa", "Rapid urbanization strains public sanitation and housing supply.", "Đô thị hóa nhanh chóng gây căng thẳng cho hệ thống vệ sinh công cộng và nguồn cung nhà ở.", "Urban sprawl.", "Môi trường & Xã hội"),

    # Nhóm Pháp luật, Xã hội & Thể chế
    ("legislation", "/ˌledʒ.əˈsleɪ.ʃən/", "luật pháp cơ chế lập pháp", "Parliament drafted landmark legislation regulating artificial intelligence.", "Nghị viện đã soạn thảo đạo luật mang tính bước ngoặt nhằm quản lý trí tuệ nhân tạo.", "Pass legislation.", "Pháp luật & Xã hội"),
    ("jurisdiction", "/ˌdʒʊr.ɪsˈdɪk.ʃən/", "thẩm quyền tài phán pháp lý", "The international court lacks binding jurisdiction over sovereign military trials.", "Tòa án quốc tế thiếu thẩm quyền tài phán ràng buộc đối với các phiên tòa quân sự quốc gia.", "Legal jurisdiction.", "Pháp luật & Xã hội"),
    ("sovereignty", "/ˈsɑːv.rən.ti/", "chủ quyền quốc gia bất khả xâm phạm", "Territorial sovereignty must be respected under international law.", "Chủ quyền lãnh thổ phải được tôn trọng theo luật pháp quốc tế.", "National sovereignty.", "Pháp luật & Xã hội"),
    ("bureaucracy", "/bjʊˈrɑː.krə.si/", "bộ máy quan liêu rườm rà", "Red tape and cumbersome bureaucracy stifle entrepreneurial initiative.", "Thủ tục rườm rà và bộ máy quan liêu bóp nghẹt các sáng kiến kinh doanh.", "Bureaucratic delay.", "Pháp luật & Xã hội"),
    ("constitution", "/ˌkɑːn.stəˈtuː.ʃən/", "hiến pháp đạo luật tối cao", "The constitution enshrines fundamental civil rights and free speech.", "Hiến pháp tôn vinh các quyền công dân cơ bản và quyền tự do ngôn luận.", "Constitutional court.", "Pháp luật & Xã hội"),
    ("litigation", "/ˌlɪt̬.əˈɡeɪ.ʃən/", "vụ kiện tụng tranh chấp tòa án", "Costly corporate litigation dragged on for over eight years.", "Vụ kiện tụng doanh nghiệp tốn kém đã kéo dài hơn tám năm.", "Civil litigation.", "Pháp luật & Xã hội"),
    ("advocate", "/ˈæd.və.keɪt/", "biện hộ ủng hộ thúc đẩy", "Human rights groups advocate for equitable asylum policies.", "Các nhóm nhân quyền ủng hộ các chính sách tị nạn công bằng.", "Advocate for change.", "Pháp luật & Xã hội"),
    ("prosecute", "/ˈprɑː.sə.kjuːt/", "truy tố khởi tố trước vành móng ngựa", "Federal prosecutors indicted high-ranking cartel financiers.", "Các công tố viên liên bang đã truy tố những kẻ tài trợ cấp cao cho tập đoàn tội phạm.", "Prosecution.", "Pháp luật & Xã hội"),
    ("rehabilitation", "/ˌriː.həˌbɪl.əˈteɪ.ʃən/", "sự phục hồi hoàn lương cải tạo", "Penal systems should focus on juvenile rehabilitation over punishment.", "Hệ thống trại giam nên tập trung vào việc phục hồi hoàn lương cho người chưa thành niên hơn là trừng phạt.", "Rehab facility.", "Pháp luật & Xã hội"),
    ("sanction", "/ˈsæŋk.ʃən/", "lệnh trừng phạt kinh tế cấm vận", "Economic sanctions froze foreign currency assets of the regime.", "Các lệnh trừng phạt kinh tế đã phong tỏa tài sản ngoại tệ của chế độ.", "Impose sanctions.", "Pháp luật & Xã hội")
]

for item in ADDITIONAL_ADVANCED:
    text, ipa, meaning, example, ex_meaning, note, topic = item
    is_sentence = len(text.split()) > 4
    ALL_ITEMS.append({
        "id": f"adv-{len(ALL_ITEMS) + 1}",
        "type": "sentence" if is_sentence else "vocab",
        "text": text,
        "ipa": ipa,
        "meaning": meaning,
        "topic": topic,
        "example": example,
        "exampleMeaning": ex_meaning,
        "note": note,
        "status": "new",
        "dateAdded": "2026-10-08"
    })

# Đọc thêm từ vựng nâng cao từ điển chuẩn Oxford 3000/5000 B2-C1 nếu chưa đủ 500
EXTRA_WORDS = [
    ("abandon", "/əˈbæn.dən/", "từ bỏ ruồng bỏ", "He abandoned the damaged vessel to save crew members.", "Anh ấy đã từ bỏ con tàu bị hư hỏng để cứu các thuyền viên.", "Abandon hope / ship.", "Hành động & Biến chuyển"),
    ("abundant", "/əˈbʌn.dənt/", "dồi dào phong phú tràn trề", "Tropical rainforests shelter an abundant variety of rare flora.", "Rừng mưa nhiệt đới che chở cho một lượng phong phú các loài thực vật quý hiếm.", "Abundance.", "Tính cách & Phẩm chất"),
    ("accelerate", "/əkˈsel.ɚ.eɪt/", "tăng tốc đẩy nhanh tiến độ", "Technological advancements accelerate societal transformation.", "Những tiến bộ công nghệ đẩy nhanh sự biến đổi của xã hội.", "Acceleration.", "Hành động & Biến chuyển"),
    ("accumulate", "/əˈkjuː.mjə.leɪt/", "tích lũy dồn ứ lại theo thời gian", "Toxic contaminants accumulate in ocean food chains.", "Chất độc hại tích tụ dần trong chuỗi thức ăn đại dương.", "Accumulation of wealth.", "Hành động & Biến chuyển"),
    ("acknowledge", "/əkˈnɑː.lɪdʒ/", "thừa nhận công nhận thực tế", "The minister acknowledged systemic flaws within the department.", "Vị bộ trưởng đã thừa nhận những thiếu sót mang tính hệ thống trong bộ.", "Acknowledgment.", "Tư duy & Học thuật"),
    ("acquire", "/əˈkwaɪ.ɚ/", "tiếp thu đạt được thâu tóm", "Children acquire language proficiency naturally through immersion.", "Trẻ em tiếp thu sự thành thạo ngôn ngữ một cách tự nhiên thông qua môi trường sống.", "Language acquisition.", "Hành động & Biến chuyển"),
    ("adaptability", "/əˌdæp.təˈbɪl.ə.t̬i/", "khả năng thích ứng linh hoạt", "Adaptability is a vital trait in ever-shifting economies.", "Khả năng thích ứng là một phẩm chất sống còn trong các nền kinh tế luôn biến đổi.", "Adaptable mindset.", "Tính cách & Phẩm chất"),
    ("adequate", "/ˈæd.ə.kwət/", "đầy đủ tương xứng vừa đủ", "Ensure adequate ventilation when handling volatile chemicals.", "Đảm bảo thông gió đầy đủ khi xử lý các hóa chất dễ bay hơi.", "Trái nghĩa: inadequate.", "Tư duy & Học thuật"),
    ("administer", "/ədˈmɪn.ə.stɚ/", "quản lý điều hành phân phát thuốc", "Nurses administer intravenous antibiotics under doctor supervision.", "Y tá tiêm truyền kháng sinh tĩnh mạch dưới sự giám sát của bác sĩ.", "Administration.", "Công sở & Đàm phán"),
    ("advocate", "/ˈæd.və.keɪt/", "người chủ trương bênh vực", "She is a passionate advocate for equal education access.", "Cô ấy là một người ủng hộ nhiệt thành cho việc tiếp cận giáo dục bình đẳng.", "Patient advocate.", "Pháp luật & Xã hội"),
    ("aesthetic", "/esˈθet̬.ɪk/", "mang tính thẩm mỹ nghệ thuật", "The museum merges minimalist architecture with natural aesthetic harmony.", "Bảo tàng kết hợp kiến trúc tối giản với sự hài hòa thẩm mỹ tự nhiên.", "Aesthetics.", "Nghệ thuật & Triết học"),
    ("aggregate", "/ˈæɡ.rə.ɡət/", "tổng hợp gộp chung toàn thể", "Aggregate demand drives long-term macroeconomic output.", "Tổng cầu thúc đẩy sản lượng kinh tế vĩ mô dài hạn.", "In the aggregate.", "Tài chính & Kinh tế"),
    ("alleviate", "/əˈliː.vi.eɪt/", "làm vơi bớt xoa dịu áp lực", "Meditation alleviates mental fatigue during stressful seasons.", "Thiền định giúp làm vơi bớt sự mệt mỏi tinh thần trong những giai đoạn căng thẳng.", "Alleviation.", "Tư duy & Học thuật"),
    ("allocate", "/ˈæl.ə.keɪt/", "chia phần cấp phát ngân sách", "The government allocated grants to independent scientific research.", "Chính phủ đã cấp phát các khoản tài trợ cho nghiên cứu khoa học độc lập.", "Resource allocation.", "Công sở & Đàm phán"),
    ("alteration", "/ˌɑːl.təˈreɪ.ʃən/", "sự sửa đổi thay đổi cấu trúc", "Genetic alterations confer immunity against severe virus strains.", "Những biến đổi di truyền mang lại khả năng miễn dịch chống lại các chủng virus nghiêm trọng.", "Alter.", "Hành động & Biến chuyển"),
    ("ambiguity", "/ˌæm.bɪˈɡjuː.ə.t̬i/", "tính chất mơ hồ đa nghĩa", "Eliminate ambiguity from legal statutes to avoid misinterpretation.", "Loại bỏ sự mơ hồ khỏi các văn bản luật để tránh hiểu sai.", "Tolerate ambiguity.", "Tư duy & Học thuật"),
    ("amplify", "/ˈæm.plə.faɪ/", "khuếch đại mở rộng tầm ảnh hưởng", "Social media echo chambers amplify polarizing rhetoric.", "Các buồng vang thông tin trên mạng xã hội khuếch đại những luận điệu gây chia rẽ.", "Amplification.", "Hành động & Biến chuyển"),
    ("anticipate", "/ænˈtɪs.ə.peɪt/", "dự liệu đón trước tình thế", "Economists anticipate aggressive monetary adjustments by quarter end.", "Các nhà kinh tế dự liệu những đợt điều chỉnh tiền tệ mạnh tay vào cuối quý.", "Anticipation.", "Tư duy & Học thuật"),
    ("apparent", "/əˈper.ənt/", "rõ ràng hiển nhiên thấy ngay", "The discrepancy became apparent upon initial database reconciliation.", "Sự sai lệch trở nên hiển nhiên ngay sau đợt đối soát cơ sở dữ liệu ban đầu.", "Apparently.", "Tư duy & Học thuật"),
    ("appease", "/əˈpiːz/", "nhân nhượng làm nguôi giận", "Compromises were drafted to appease striking union delegates.", "Các thỏa hiệp được soạn thảo để làm nguôi giận các đại biểu công đoàn đang đình công.", "Appeasement policy.", "Công sở & Đàm phán"),
    ("arbitrary", "/ˈɑːr.bə.trer.i/", "tùy tiện độc đoán vô căn cứ", "Dictators impose arbitrary bans without constitutional justification.", "Các nhà độc tài áp đặt những lệnh cấm tùy tiện mà không có căn cứ hiến pháp.", "Arbitrary decision.", "Pháp luật & Xã hội"),
    ("articulation", "/ɑːrˌtɪk.jəˈleɪ.ʃən/", "sự phát biểu rõ ràng khúc chiết", "Precise articulation of strategic goals unites multinational workforces.", "Sự phát biểu khúc chiết các mục tiêu chiến lược giúp gắn kết lực lượng lao động đa quốc gia.", "Articulate.", "Công sở & Đàm phán"),
    ("ascertain", "/ˌæs.ɚˈteɪn/", "xác định chắc chắn tìm ra sự thật", "Detectives sought to ascertain the exact sequence of events.", "Các thám tử tìm cách xác định chắc chắn trình tự chính xác của các sự kiện.", "Ascertain the truth.", "Tư duy & Học thuật"),
    ("aspiration", "/ˌæs.pəˈreɪ.ʃən/", "nguyện vọng khát khao vươn lên", "Educational initiatives foster lofty career aspirations among youth.", "Các sáng kiến giáo dục nuôi dưỡng khát vọng nghề nghiệp cao đẹp trong giới trẻ.", "Aspire to.", "Tính cách & Phẩm chất"),
    ("assimilate", "/əˈsɪm.ə.leɪt/", "đồng hóa hòa nhập tiếp thu", "Immigrants assimilate into civic life while honoring native traditions.", "Người nhập cư hòa nhập vào đời sống công dân trong khi vẫn tôn vinh truyền thống cội nguồn.", "Cultural assimilation.", "Môi trường & Xã hội"),
    ("attain", "/əˈteɪn/", "đạt được mục tiêu sau nỗ lực", "Few athletes attain Olympic gold through talent alone.", "Hiếm có vận động viên nào đạt được huy chương vàng Olympic chỉ bằng tài năng đơn thuần.", "Attainable.", "Hành động & Biến chuyển"),
    ("authentic", "/ɑːˈθen.tɪk/", "đích thực chân chính nguyên bản", "Scholars verified the manuscript as an authentic medieval artifact.", "Các học giả đã xác minh bản thảo là một hiện vật thời Trung cổ đích thực.", "Authenticity.", "Tính cách & Phẩm chất"),
    ("authority", "/əˈθɔːr.ə.t̬i/", "uy quyền cơ quan chức năng", "Regulatory authorities issued directives halting dangerous clinical practices.", "Các cơ quan quản lý đã ban hành chỉ thị đình chỉ các hoạt động lâm sàng nguy hiểm.", "Authoritative.", "Pháp luật & Xã hội"),
    ("autonomous", "/ɑːˈtɑː.nə.məs/", "tự trị tự quản độc lập", "Universities maintain autonomous governance over academic curricula.", "Các trường đại học duy trì quyền quản trị tự chủ đối với chương trình học thuật.", "Autonomy.", "Pháp luật & Xã hội"),
    ("aversion", "/əˈvɝː.ʒən/", "ác cảm không thích ác cảm", "Conservative investors have an innate aversion to volatile equities.", "Các nhà đầu tư thận trọng có một ác cảm tự nhiên đối với cổ phiếu biến động mạnh.", "Risk aversion.", "Tâm lý & Nhận thức")
]

# Thêm từ vào danh sách cho tới khi vượt mốc 500
base_id = len(ALL_ITEMS) + 1
while len(ALL_ITEMS) < 520:
    for word_tuple in EXTRA_WORDS:
        if len(ALL_ITEMS) >= 520:
            break
        text, ipa, meaning, example, ex_meaning, note, topic = word_tuple
        ALL_ITEMS.append({
            "id": f"adv-{len(ALL_ITEMS) + 1}",
            "type": "sentence" if len(text.split()) > 4 else "vocab",
            "text": text if not any(x['text'] == text for x in ALL_ITEMS) else f"{text} (context {len(ALL_ITEMS)})",
            "ipa": ipa,
            "meaning": meaning,
            "topic": topic,
            "example": example,
            "exampleMeaning": ex_meaning,
            "note": note,
            "status": "new",
            "dateAdded": "2026-10-08"
        })

# Khử trùng lặp text
seen_texts = set()
UNIQUE_ITEMS = []
for item in ALL_ITEMS:
    clean_text = item["text"].split(" (context")[0]
    if clean_text not in seen_texts:
        seen_texts.add(clean_text)
        UNIQUE_ITEMS.append(item)

# Nếu còn thiếu để đủ 500, bổ sung từ điển học thuật
if len(UNIQUE_ITEMS) < 500:
    academic_list = [
        ("capitulate", "/kəˈpɪtʃ.ə.leɪt/", "đầu hàng nhượng bộ hoàn toàn", "The military capitulated after prolonged siege.", "Quân đội đã đầu hàng sau cuộc vây hãm kéo dài.", "Surrender.", "Lịch sử & Xã hội"),
        ("chastise", "/tʃæbˈstaɪz/", "trách phạt khiển trách gay gắt", "The manager chastised the team for reckless oversights.", "Quản lý đã khiển trách đội ngũ vì những sơ suất thiếu cẩn trọng.", "Scold severely.", "Công sở & Đàm phán"),
        ("coercion", "/koʊˈɝː.ʃən/", "sự ép buộc cưỡng bức áp đặt", "Confessions extracted under coercion are legally inadmissible.", "Lời thú tội bị ép buộc không được chấp nhận trước tòa.", "Coercive power.", "Pháp luật & Xã hội"),
        ("cognizant", "/ˈkɑːɡ.nɪ.zənt/", "nhận thức rõ ràng thấu hiểu", "Leaders must remain cognizant of grassroots grievances.", "Lãnh đạo phải nhận thức rõ những bất bình từ cơ sở.", "Cognizant of.", "Tâm lý & Nhận thức"),
        ("collusion", "/kəˈluː.ʒən/", "sự cấu kết ngầm thông đồng", "Cartels engaged in unlawful price-fixing collusion.", "Các tập đoàn đã cấu kết ngầm để ấn định giá phi pháp.", "Collusive behavior.", "Tài chính & Kinh tế"),
        ("commensurate", "/kəˈmen.ʃɚ.ət/", "tương xứng tương xứng với", "Salaries should be commensurate with experience and expertise.", "Tiền lương nên tương xứng với kinh nghiệm và chuyên môn.", "Commensurate with.", "Công sở & Đàm phán"),
        ("compelling", "/kəmˈpel.ɪŋ/", "đầy tính thuyết phục hấp dẫn", "The prosecution presented compelling forensic proofs.", "Bên công tố đã đưa ra các bằng chứng pháp y đầy thuyết phục.", "Compelling evidence.", "Tư duy & Học thuật"),
        ("conciliatory", "/kənˈsɪl.i.ə.tɔːr.i/", "mang tính hòa giải nhượng bộ", "The ambassador struck a conciliatory tone during talks.", "Vị đại sứ đã thể hiện một giọng điệu hòa giải trong các cuộc đàm phán.", "Conciliation.", "Công sở & Đàm phán"),
        ("concomitant", "/kənˈkɑː.mə.t̬ənt/", "đi kèm đồng thời xuất hiện", "Economic modernization brought concomitant social strains.", "Hiện đại hóa kinh tế kéo theo những căng thẳng xã hội đi kèm.", "Accompaniment.", "Tư duy & Học thuật"),
        ("concur", "/kənˈkɝː/", "đồng ý tán thành quan điểm", "The appellate judges concurred with the primary ruling.", "Các thẩm phán phúc thẩm đã tán thành phán quyết sơ thẩm.", "Concur with.", "Pháp luật & Xã hội"),
        ("condone", "/kənˈdoʊn/", "dung túng bao che cho sai trái", "School policies do not condone bullying behavior.", "Nội quy nhà trường không dung túng hành vi bắt nạt.", "Condone actions.", "Xã hội & Đạo đức"),
        ("confound", "/kənˈfaʊnd/", "làm bối rối làm rối trí", "Conflicting economic data confounded market analysts.", "Số liệu kinh tế mâu thuẫn làm rối trí các chuyên gia phân tích thị trường.", "Confounding variable.", "Tư duy & Học thuật"),
        ("conjecture", "/kənˈdʒek.tʃɚ/", "sự phỏng đoán vô căn cứ", "Historical claims must rest on artifacts, not mere conjecture.", "Các tuyên bố lịch sử phải dựa trên hiện vật, không thể chỉ là phỏng đoán.", "Speculation.", "Tư duy & Học thuật"),
        ("connoisseur", "/ˌkɑː.nəˈsɝː/", "người sành sỏi bậc thầy am hiểu", "A connoisseur of classical music detected subtle violin phrasing.", "Một người sành sỏi âm nhạc cổ điển nhận ra cách luyến ngắt vĩ cầm tinh tế.", "Art connoisseur.", "Nghệ thuật & Triết học"),
        ("consecrate", "/ˈkɑːn.sə.kreɪt/", "thánh hiến tôn sùng hiến dâng", "Monuments consecrate the memories of fallen soldiers.", "Các tượng đài hiến dâng ký ức cho những người lính đã ngã xuống.", "Dedicate solemnly.", "Văn hóa & Lịch sử"),
        ("contentious", "/kənˈten.ʃəs/", "gây tranh cãi nảy lửa", "Land rezoning remains a contentious local issue.", "Quy hoạch lại đất đai vẫn là một vấn đề địa phương gây tranh cãi nảy lửa.", "Contentious debate.", "Xã hội & Đạo đức"),
        ("contrite", "/kənˈtraɪt/", "ăn năn hối lỗi chân thành", "The defendant appeared genuinely contrite before sentencing.", "Bị cáo tỏ ra thực sự ăn năn hối lỗi trước khi tuyên án.", "Contrition.", "Tâm lý & Nhận thức"),
        ("conundrum", "/kəˈnʌn.drəm/", "bài toán hóc búa nan giải", "Balancing inflation control with employment is an economic conundrum.", "Cân bằng kiểm soát lạm phát với việc làm là bài toán kinh tế nan giải.", "Difficult puzzle.", "Tư duy & Học thuật"),
        ("converge", "/kənˈvɝːdʒ/", "hội tụ quy tụ về một mối", "Multiple technological trends converge on artificial intelligence.", "Nhiều xu hướng công nghệ cùng hội tụ vào trí tuệ nhân tạo.", "Convergence.", "Khoa học & Đổi mới"),
        ("copious", "/ˈkoʊ.pi.əs/", "dồi dào bạt ngàn nhiều vô kể", "She took copious handwritten notes throughout the seminar.", "Cô ấy đã ghi chép tay rất nhiều ghi chú trong suốt buổi hội thảo.", "Copious amounts.", "Tư duy & Học thuật"),
        ("corrosive", "/kəˈroʊ.sɪv/", "ăn mòn hủy hoại từ từ", "Cynicism exerts a corrosive effect on institutional trust.", "Sự hoài nghi yếm thế gây ra tác động ăn mòn đối với niềm tin vào thể chế.", "Corrosion.", "Môi trường & Xã hội"),
        ("counsel", "/ˈkaʊn.səl/", "lời khuyên cố vấn pháp lý", "Heed the wise counsel of seasoned financial advisers.", "Hãy lắng nghe lời khuyên khôn ngoan của những cố vấn tài chính dày dạn.", "Legal counsel.", "Công sở & Đàm phán"),
        ("credence", "/ˈkriː.dəns/", "lòng tin sự tín nhiệm", "Sensational rumors gained credence without solid evidence.", "Những tin đồn giật gân đã có được lòng tin dù thiếu bằng chứng vững chắc.", "Give credence to.", "Tư duy & Học thuật"),
        ("culpable", "/ˈkʌl.pə.bəl/", "đáng trách có tội phải chịu phạt", "Negligent supervisors were found culpable for site accidents.", "Các giám sát viên cẩu thả bị kết luận là có tội trong các tai nạn công trường.", "Culpability.", "Pháp luật & Xã hội"),
        ("cumbersome", "/ˈkʌm.bɚ.səm/", "cồng kềnh vướng víu nặng nề", "Outdated paper verification forms proved too cumbersome.", "Các biểu mẫu xác minh bằng giấy lỗi thời tỏ ra quá cồng kềnh.", "Cumbersome process.", "Công sở & Đàm phán"),
        ("curtail", "/kɚˈteɪl/", "cắt giảm thu hẹp hạn chế bớt", "Governments curtailed travel to contain infectious outbreaks.", "Chính phủ đã hạn chế đi lại để ngăn chặn dịch bệnh truyền nhiễm bùng phát.", "Curtail spending.", "Hành động & Biến chuyển"),
        ("dearth", "/dɝːθ/", "sự khan hiếm thiếu hụt trầm trọng", "A dearth of qualified engineers slows technological progress.", "Sự khan hiếm kỹ sư có trình độ làm chậm tiến bộ công nghệ.", "Dearth of resources.", "Kinh tế & Thị trường"),
        ("debilitate", "/dɪˈbɪl.ə.teɪt/", "làm suy nhược kiệt quệ sức lực", "Severe asthma can debilitate young athletes if untreated.", "Hen suyễn nặng có thể làm suy nhược các vận động viên trẻ nếu không điều trị.", "Debilitating illness.", "Sức khỏe & Tâm lý"),
        ("decipher", "/dɪˈsaɪ.fɚ/", "giải mã đọc ra ký tự cổ", "Linguists deciphered ancient hieroglyphs on royal tomb tablets.", "Các nhà ngôn ngữ học đã giải mã các chữ tượng hình cổ trên bia mộ hoàng gia.", "Decipher code.", "Khoa học & Đổi mới"),
        ("deference", "/ˈdef.ɚ.əns/", "sự tôn kính phục tùng nể trọng", "Subordinates treated the founding chairman with immense deference.", "Cấp dưới đối xử với vị chủ tịch sáng lập với sự tôn kính to lớn.", "In deference to.", "Văn hóa & Lịch sử")
    ]
    for item in academic_list:
        text, ipa, meaning, example, ex_meaning, note, topic = item
        if text not in seen_texts:
            seen_texts.add(text)
            UNIQUE_ITEMS.append({
                "id": f"adv-{len(UNIQUE_ITEMS) + 1}",
                "type": "vocab",
                "text": text,
                "ipa": ipa,
                "meaning": meaning,
                "topic": topic,
                "example": example,
                "exampleMeaning": ex_meaning,
                "note": note,
                "status": "new",
                "dateAdded": "2026-10-08"
            })

# Cập nhật ID
for idx, it in enumerate(UNIQUE_ITEMS):
    it["id"] = f"adv-{idx + 1}"

# Xuất ra file
output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\english-learning-app"
js_file = os.path.join(output_dir, "js", "data.js")
json_file = os.path.join(output_dir, "data_500_words.json")

unique_topics = []
for it in UNIQUE_ITEMS:
    if it["topic"] not in unique_topics:
        unique_topics.append(it["topic"])

js_code = f"""// Bộ dữ liệu {len(UNIQUE_ITEMS)} từ vựng & mẫu câu NÂNG CAO (B2 - C1 / Academic & Business)
const INITIAL_DATA = {json.dumps(UNIQUE_ITEMS, ensure_ascii=False, indent=4)};

const DEFAULT_TOPICS = {json.dumps(unique_topics, ensure_ascii=False, indent=4)};
"""

with open(js_file, "w", encoding="utf-8") as f:
    f.write(js_code)

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(UNIQUE_ITEMS, f, ensure_ascii=False, indent=2)

print(f"Total advanced items compiled: {len(UNIQUE_ITEMS)}")
