import json

# Nạp 465 từ hiện có
path = r"C:\Users\Admin\.gemini\antigravity\scratch\english-learning-app\data_500_words.json"
with open(path, "r", encoding="utf-8") as f:
    items = json.load(f)

MORE_40 = [
    ("oblivious", "/əˈblɪv.i.əs/", "không để ý không hay biết gì", "He walked into oncoming traffic, oblivious to danger.", "Anh ấy bước vào luồng xe cộ, hoàn toàn không hay biết gì về nguy hiểm.", "Oblivious of/to.", "Tâm lý & Nhận thức"),
    ("obscure", "/əbˈskjʊr/", "tối nghĩa khó hiểu ít người biết", "The reference is to an obscure nineteenth-century poet.", "Điển tích này nhắc đến một nhà thơ thế kỷ 19 ít người biết đến.", "Obscurity.", "Nghệ thuật & Triết học"),
    ("ominous", "/ˈɑː.mə.nəs/", "điềm gở đe dọa báo trước điềm xấu", "Dark thunderclouds cast an ominous shadow across the valley.", "Những đám mây giông đen kịt phủ bóng đen điềm gở khắp thung lũng.", "Ominous silence.", "Tư duy & Học thuật"),
    ("opaque", "/oʊˈpeɪk/", "mờ đục không trong suốt khó hiểu", "The ministry provided opaque explanations regarding state spending.", "Bộ này đã đưa ra những lời giải thích mờ đục khó hiểu về chi tiêu công.", "Opacity.", "Tư duy & Học thuật"),
    ("opportunistic", "/ˌɑː.pɚ.tuːˈnɪs.tɪk/", "cơ hội trục lợi cơ hội chủ nghĩa", "Opportunistic investors bought depreciated real estate assets cheaply.", "Các nhà đầu tư cơ hội đã mua tài sản bất động sản bị mất giá với giá rẻ mạt.", "Opportunism.", "Tài chính & Kinh tế"),
    ("optimal", "/ˈɑːp.tə.məl/", "tối ưu hoàn hảo nhất", "The algorithm calculated the optimal route to bypass gridlocks.", "Thuật toán đã tính toán lộ trình tối ưu để tránh các điểm nghẽn giao thông.", "Optimum.", "Khoa học & Đổi mới"),
    ("orthodox", "/ˈɔːr.θə.dɑːks/", "chính thống theo truyền thống lâu đời", "He abandoned orthodox economic theories to study decentralized finance.", "Ông đã từ bỏ các lý thuyết kinh tế chính thống để nghiên cứu tài chính phi tập trung.", "Trái nghĩa: unorthodox.", "Nghệ thuật & Triết học"),
    ("oscillate", "/ˈɑː.səl.eɪt/", "dao động đung đưa bất định", "Consumer sentiment oscillated between optimism and acute inflation fears.", "Tâm lý người tiêu dùng dao động giữa sự lạc quan và nỗi sợ lạm phát gay gắt.", "Oscillation.", "Khoa học & Đổi mới"),
    ("ostentatious", "/ˌɑː.stənˈteɪ.ʃəs/", "phô trương khoe khoang hào nhoáng", "The billionaire's ostentatious superyacht drew public outrage.", "Chiếc du thuyền siêu sang phô trương khoe của tỷ phú đã thu hút sự phẫn nộ của công chúng.", "Ostentation.", "Tính cách & Phẩm chất"),
    ("outsource", "/ˈaʊt.sɔːrs/", "thuê ngoài gia công bên ngoài", "Technology firms outsource customer support to cut operational overhead.", "Các công ty công nghệ thuê ngoài dịch vụ chăm sóc khách hàng để cắt giảm chi phí vận hành.", "Outsourcing.", "Công sở & Đàm phán"),
    ("pacify", "/ˈpæs.ə.faɪ/", "xoa dịu bình định làm nguôi giận", "Diplomats attempted to pacify warring factions through trade pacts.", "Các nhà ngoại giao đã cố gắng xoa dịu các phe phái tham chiến thông qua các hiệp ước thương mại.", "Pacification.", "Công sở & Đàm phán"),
    ("painstaking", "/ˈpeɪnzˌteɪ.kɪŋ/", "công phu cực nhọc tỉ mỉ chu đáo", "Restoring ancient frescoes requires painstaking, delicate craftsmanship.", "Việc phục hồi các bức bích họa cổ đòi hỏi tay nghề công phu, tỉ mỉ và tinh tế.", "Painstaking effort.", "Tính cách & Phẩm chất"),
    ("palatable", "/ˈpæl.ə.t̬ə.bəl/", "dễ chấp nhận hợp khẩu vị", "The compromise was politically palatable to both legislative factions.", "Thỏa hiệp này là có thể chấp nhận được về mặt chính trị đối với cả hai phe lập pháp.", "Trái nghĩa: unpalatable.", "Công sở & Đàm phán"),
    ("paradox", "/ˈper.ə.dɑːks/", "nghịch lý điều ngược đời có lý", "The paradox of thrift shows saving can reduce aggregate economic demand.", "Nghịch lý của sự tiết kiệm cho thấy việc tiết kiệm có thể làm giảm tổng cầu kinh tế.", "Paradoxical.", "Tư duy & Học thuật"),
    ("paramount", "/ˈper.ə.maʊnt/", "tối quan trọng hàng đầu", "Protecting digital intellectual property is of paramount concern.", "Bảo vệ sở hữu trí tuệ số là mối quan tâm hàng đầu tối quan trọng.", "Paramount importance.", "Tư duy & Học thuật"),
    ("partisan", "/ˈpɑːr.t̬ə.zən/", "mang tính đảng phái phiến diện", "Partisan media coverage deepens societal division and distrust.", "Sự đưa tin mang tính đảng phái phiến diện làm sâu sắc thêm sự chia rẽ và ngờ vực xã hội.", "Bipartisan.", "Pháp luật & Xã hội"),
    ("patronize", "/ˈpeɪ.trə.naɪz/", "lên mặt trịch thượng, lui tới quán", "Never patronize junior associates during technical brainstorming sessions.", "Đừng bao giờ lên mặt trịch thượng với các cộng sự cấp dưới trong các buổi động não kỹ thuật.", "Patronizing tone.", "Tính cách & Phẩm chất"),
    ("paucity", "/ˈpɑː.sə.t̬i/", "sự khan hiếm nghèo nàn số lượng ít", "A paucity of empirical evidence weakened the bold academic thesis.", "Sự khan hiếm bằng chứng thực nghiệm đã làm suy yếu luận văn học thuật táo bạo này.", "Paucity of data.", "Tư duy & Học thuật"),
    ("pedantic", "/pəˈdæn.tɪk/", "mọt sách vụn vặt câu nệ chi tiết", "Critics dismissed the reviewer as overly pedantic about minor grammatical slips.", "Các nhà phê bình đã gạt bỏ người đánh giá vì quá câu nệ mọt sách về những lỗi ngữ pháp nhỏ nhặt.", "Pedantry.", "Tính cách & Phẩm chất"),
    ("peerless", "/ˈpɪr.ləs/", "vô song không ai sánh bằng", "Her peerless vocal technique captivated opera audiences worldwide.", "Kỹ thuật thanh nhạc vô song của cô ấy đã chinh phục khán giả opera trên toàn thế giới.", "Peerless quality.", "Nghệ thuật & Triết học"),
    ("penchant", "/ˈpen.tʃənt/", "thiên hướng sở thích đặc biệt", "He has a lifelong penchant for high-risk speculative venture investments.", "Ông có một sở thích thiên hướng suốt đời đối với các khoản đầu tư mạo hiểm rủi ro cao.", "Penchant for.", "Tính cách & Phẩm chất"),
    ("perceive", "/pɚˈsiːv/", "nhận thức lĩnh hội nhìn nhận", "Investors perceive political instability as a severe sovereign risk factor.", "Các nhà đầu tư nhìn nhận sự bất ổn chính trị là một yếu tố rủi ro quốc gia nghiêm trọng.", "Perception.", "Tâm lý & Nhận thức"),
    ("perceptive", "/pɚˈsep.tɪv/", "nhạy bén sâu sắc tinh ý", "Her perceptive observations identified bottlenecks before project failure.", "Những quan sát nhạy bén tinh tế của cô ấy đã nhận diện các điểm nghẽn trước khi dự án thất bại.", "Perceptive insight.", "Tính cách & Phẩm chất"),
    ("perennial", "/pəˈren.i.əl/", "bất diệt vĩnh viễn tồn tại mãi", "Water scarcity remains a perennial challenge for arid farming basins.", "Sự khan hiếm nước vẫn là một thách thức lâu dài thường trực đối với các lưu vực canh tác khô cằn.", "Perennial problem.", "Môi trường & Xã hội"),
    ("peripheral", "/pəˈrɪf.ɚ.əl/", "ngoại vi thứ yếu bên lề", "Do not lose focus on peripheral issues during critical negotiations.", "Đừng mất tập trung vào các vấn đề thứ yếu bên lề trong các cuộc đàm phán mang tính quyết định.", "Peripheral vision.", "Tư duy & Học thuật"),
    ("permeate", "/ˈpɝː.mi.eɪt/", "thấm nhuần lan tỏa ngấm vào", "Digital surveillance technologies permeate every aspect of urban civil life.", "Các công nghệ giám sát kỹ thuật số thấm nhuần len lỏi vào mọi khía cạnh của đời sống dân sự đô thị.", "Permeate society.", "Khoa học & Đổi mới"),
    ("perpetual", "/pɚˈpetʃ.u.əl/", "vĩnh viễn liên tục không dứt", "The region endured perpetual territorial skirmishes for three decades.", "Khu vực này đã phải chịu đựng những cuộc giao tranh lãnh thổ liên tục không dứt trong suốt ba thập kỷ.", "Perpetual motion.", "Lịch sử & Xã hội"),
    ("perplex", "/pɚˈpleks/", "làm bối rối làm lúng túng", "Bizarre quantum physics anomalies continue to perplex seasoned researchers.", "Những dị thường vật lý lượng tử kỳ quặc tiếp tục làm bối rối các nhà nghiên cứu dày dạn kinh nghiệm.", "Perplexing puzzle.", "Tư duy & Học thuật"),
    ("persevere", "/ˌpɝː.səˈvɪr/", "kiên trì bền bỉ vượt gian khó", "Startups that persevere through early funding droughts frequently succeed.", "Các công ty khởi nghiệp kiên trì bền bỉ vượt qua giai đoạn cạn kiệt vốn ban đầu thường sẽ thành công.", "Perseverance.", "Tính cách & Phẩm chất"),
    ("persist", "/pɚˈsɪst/", "khăng khăng dai dẳng tồn tại tiếp", "If high fever symptoms persist beyond forty-eight hours, consult doctors.", "Nếu các triệu chứng sốt cao kéo dài dai dẳng quá 48 giờ, hãy tham khảo ý kiến bác sĩ.", "Persistent effort.", "Sức khỏe & Tâm lý"),
    ("perspective", "/pɚˈspek.tɪv/", "góc nhìn quan điểm viễn cảnh", "Living overseas offers a transformative perspective on domestic culture.", "Sống ở nước ngoài mang lại một góc nhìn biến đổi sâu sắc về văn hóa quê nhà.", "Broaden perspective.", "Tư duy & Học thuật"),
    ("pervasive", "/pɚˈveɪ.sɪv/", "lan tỏa thâm nhập rộng khắp", "Cyber risks pose a pervasive threat to interconnected financial institutions.", "Rủi ro mạng đặt ra một mối đe dọa lan tỏa sâu rộng đối với các tổ chức tài chính liên kết.", "Pervasiveness.", "Khoa học & Đổi mới"),
    ("pessimism", "/ˈpes.ə.mɪz.əm/", "thuyết bi quan cái nhìn tiêu cực", "Unwarranted economic pessimism suppresses productive corporate capital outlay.", "Sự bi quan kinh tế vô căn cứ kìm hãm các khoản chi tiêu vốn hiệu quả của doanh nghiệp.", "Trái nghĩa: optimism.", "Tâm lý & Nhận thức"),
    ("philanthropist", "/fɪˈlæn.θrə.pɪst/", "nhà từ thiện nhà hảo tâm lớn", "The billionaire philanthropist endowed universities with cancer research trusts.", "Nhà từ thiện tỷ phú đã quyên tặng các trường đại học những quỹ tín thác nghiên cứu ung thư.", "Philanthropy.", "Xã hội & Đạo đức"),
    ("pioneer", "/ˌpaɪ.əˈnɪr/", "người tiên phong mở đường", "Marie Curie was a fearless pioneer in experimental nuclear radiation science.", "Marie Curie là người tiên phong dũng cảm không biết sợ trong khoa học bức xạ hạt nhân thực nghiệm.", "Pioneering work.", "Khoa học & Đổi mới"),
    ("pique", "/piːk/", "kích thích khơi gợi sự tò mò", "The cryptographic puzzle piqued the mathematical genius's curiosity.", "Câu đố mật mã đã kích thích sự tò mò của thiên tài toán học.", "Pique one's interest.", "Tâm lý & Nhận thức"),
    ("pitfall", "/ˈpɪt.fɑːl/", "cạm bẫy cạm bẫy tiềm ẩn", "Auditing teams highlighted critical regulatory pitfalls in cross-border deals.", "Các đội kiểm toán đã nêu bật những cạm bẫy quy định quan trọng trong các thỏa thuận xuyên biên giới.", "Avoid pitfalls.", "Công sở & Đàm phán"),
    ("plausible", "/ˈplɑː.zə.bəl/", "đáng tin cậy nghe có vẻ hợp lý", "She provided a plausible hypothesis for unexpected atmospheric temperature fluctuations.", "Cô ấy đã đưa ra một giả thuyết hợp lý đáng tin cho những biến động nhiệt độ khí quyển bất ngờ.", "Plausibility.", "Tư duy & Học thuật"),
    ("poignant", "/ˈpɔɪ.njənt/", "thấm thía chua xót ngậm ngùi", "The war documentary ended with a poignant testament to peace.", "Bộ phim tài liệu chiến tranh kết thúc bằng một lời chứng thấm thía chua xót cho hòa bình.", "Poignant memory.", "Nghệ thuật & Triết học"),
    ("polarize", "/ˈpoʊ.lɚ.aɪz/", "phân cực gây chia rẽ sâu sắc", "Heated constitutional debates polarize electorates along demographic fault lines.", "Những cuộc tranh luận hiến pháp nảy lửa gây phân cực cử tri sâu sắc theo các ranh giới nhân khẩu học.", "Polarization.", "Pháp luật & Xã hội")
]

existing_texts = {it["text"] for it in items}
for w in MORE_40:
    text, ipa, meaning, example, ex_meaning, note, topic = w
    if text not in existing_texts:
        items.append({
            "id": f"adv-{len(items) + 1}",
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
        existing_texts.add(text)

# Đánh số ID
for idx, it in enumerate(items):
    it["id"] = f"adv-{idx + 1}"

topics = []
for it in items:
    if it["topic"] not in topics:
        topics.append(it["topic"])

js_file = r"C:\Users\Admin\.gemini\antigravity\scratch\english-learning-app\js\data.js"
json_file = r"C:\Users\Admin\.gemini\antigravity\scratch\english-learning-app\data_500_words.json"

js_code = f"""// Bộ dữ liệu {len(items)} từ vựng & mẫu câu TIẾNG ANH NÂNG CAO (B2 - C1 / Academic, Business & IELTS 7.0+)
const INITIAL_DATA = {json.dumps(items, ensure_ascii=False, indent=4)};

const DEFAULT_TOPICS = {json.dumps(topics, ensure_ascii=False, indent=4)};
"""

with open(js_file, "w", encoding="utf-8") as f:
    f.write(js_code)

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Final Count: {len(items)} advanced items written successfully across {len(topics)} topics!")
