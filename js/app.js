// ================= AI PRONUNCIATION EVALUATOR =================
class PronunciationEvaluator {
    levenshtein(a, b) {
        const matrix = [];
        for (let i = 0; i <= b.length; i++) matrix[i] = [i];
        for (let j = 0; j <= a.length; j++) matrix[0][j] = j;
        for (let i = 1; i <= b.length; i++) {
            for (let j = 1; j <= a.length; j++) {
                if (b.charAt(i - 1) === a.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(
                        matrix[i - 1][j - 1] + 1,
                        matrix[i][j - 1] + 1,
                        matrix[i - 1][j] + 1
                    );
                }
            }
        }
        return matrix[b.length][a.length];
    }

    wordSimilarity(w1, w2) {
        if (!w1 || !w2) return 0;
        if (w1 === w2) return 1.0;
        const maxLen = Math.max(w1.length, w2.length);
        if (maxLen === 0) return 1.0;
        const dist = this.levenshtein(w1, w2);
        return Math.max(0, 1 - dist / maxLen);
    }

    cleanWord(w) {
        return (w || '').toLowerCase().replace(/[.,/#!$%^&*;:{}=\-_`~()?'’"“”…–—]/g, '').trim();
    }

    evaluate(targetText, spokenText) {
        const rawTargetWords = (targetText || '').trim().split(/\s+/).filter(Boolean);
        const targetClean = rawTargetWords.map(w => this.cleanWord(w));
        const spokenClean = (spokenText || '').trim().split(/\s+/).map(w => this.cleanWord(w)).filter(Boolean);

        const n = targetClean.length;
        const m = spokenClean.length;
        if (n === 0) {
            return {
                overallScore: 0,
                verdict: 'Chưa có văn bản mẫu',
                feedback: 'Không tìm thấy câu hoặc từ cần phát âm.',
                badgeClass: 'bg-slate-100 text-slate-700 border-slate-300',
                scoreColorClass: 'text-slate-600',
                tokens: [],
                targetText,
                spokenText
            };
        }

        if (m === 0) {
            return {
                overallScore: 0,
                verdict: 'Chưa nghe thấy giọng nói 🔇',
                feedback: 'AI chưa thu được âm thanh rõ ràng. Hãy kiểm tra lại micro và thử nói to hơn nhé.',
                badgeClass: 'bg-rose-100 text-rose-800 border-rose-300',
                scoreColorClass: 'text-rose-600',
                tokens: rawTargetWords.map(rawW => ({
                    raw: rawW,
                    clean: this.cleanWord(rawW),
                    spoken: null,
                    similarity: 0,
                    status: 'missed',
                    score: 0
                })),
                targetText,
                spokenText: ''
            };
        }

        // Needleman-Wunsch sequence alignment
        const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));

        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= m; j++) {
                const sim = this.wordSimilarity(targetClean[i - 1], spokenClean[j - 1]);
                const matchScore = sim >= 0.5 ? (sim >= 0.85 ? 2.0 : sim * 1.5) : -0.5;
                dp[i][j] = Math.max(
                    dp[i - 1][j - 1] + matchScore,
                    dp[i - 1][j] - 0.2,
                    dp[i][j - 1] - 0.2
                );
            }
        }

        // Backtrack to find aligned pairs
        let i = n, j = m;
        const matches = new Map();
        while (i > 0 && j > 0) {
            const sim = this.wordSimilarity(targetClean[i - 1], spokenClean[j - 1]);
            const matchScore = sim >= 0.5 ? (sim >= 0.85 ? 2.0 : sim * 1.5) : -0.5;
            if (Math.abs(dp[i][j] - (dp[i - 1][j - 1] + matchScore)) < 0.001) {
                if (sim >= 0.5) {
                    matches.set(i - 1, { spokenIdx: j - 1, spokenWord: spokenClean[j - 1], sim });
                }
                i--; j--;
            } else if (dp[i][j] === dp[i - 1][j] - 0.2) {
                i--;
            } else {
                j--;
            }
        }

        let totalScore = 0;
        const tokens = targetClean.map((targetW, idx) => {
            const rawW = rawTargetWords[idx];
            const match = matches.get(idx);
            if (!match) {
                return {
                    raw: rawW,
                    clean: targetW,
                    spoken: null,
                    similarity: 0,
                    status: 'missed',
                    score: 0
                };
            }
            const sim = match.sim;
            let status = 'missed';
            let score = 0;
            if (sim >= 0.85) {
                status = 'correct';
                score = 100;
            } else if (sim >= 0.50) {
                status = 'close';
                score = Math.round(sim * 100);
            }
            totalScore += score;
            return {
                raw: rawW,
                clean: targetW,
                spoken: match.spokenWord,
                similarity: Math.round(sim * 100),
                status,
                score
            };
        });

        const overallScore = Math.min(100, Math.max(0, Math.round(totalScore / n)));

        let verdict = 'Cần luyện thêm 🔄';
        let feedback = 'Chưa nhận diện chính xác nhiều từ. Bạn hãy nghe mẫu vài lần, chú ý nhấn trọng âm và nói dứt khoát hơn nhé.';
        let badgeClass = 'bg-rose-100 text-rose-800 border-rose-300';
        let scoreColorClass = 'text-rose-600';

        if (overallScore >= 90) {
            verdict = 'Xuất sắc! 🎉';
            feedback = 'Phát âm rất chuẩn xác! Các âm tiết rõ ràng, ngữ điệu tự nhiên và chuẩn bản xứ.';
            badgeClass = 'bg-emerald-100 text-emerald-800 border-emerald-300';
            scoreColorClass = 'text-emerald-600';
        } else if (overallScore >= 75) {
            verdict = 'Rất tốt! ⭐';
            feedback = 'Phát âm khá tốt, người bản xứ nghe hiểu dễ dàng. Hãy bấm vào các từ màu cam để nghe lại và chuốt âm gió nhé.';
            badgeClass = 'bg-blue-100 text-blue-800 border-blue-300';
            scoreColorClass = 'text-blue-600';
        } else if (overallScore >= 50) {
            verdict = 'Cần cải thiện 💪';
            feedback = 'Có một số từ phát âm chưa chuẩn hoặc bị nuốt âm đuôi. Bấm vào nút "Nghe chậm" rồi bấm từng từ để sửa lỗi nhé.';
            badgeClass = 'bg-amber-100 text-amber-800 border-amber-300';
            scoreColorClass = 'text-amber-600';
        }

        return {
            overallScore,
            verdict,
            feedback,
            badgeClass,
            scoreColorClass,
            tokens,
            targetText,
            spokenText
        };
    }
}

// ================= SPEECH RECOGNITION MANAGER =================
class SpeechPracticeManager {
    constructor() {
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        this.SpeechRecClass = SpeechRec || null;
        this.recognition = null;
        this.isRecording = false;
        this.callbacks = null;
    }

    static isSupported() {
        return !!(window.SpeechRecognition || window.webkitSpeechRecognition);
    }

    start(callbacks = {}) {
        if (!SpeechPracticeManager.isSupported()) {
            if (callbacks.onError) {
                callbacks.onError({
                    error: 'not-supported',
                    message: 'Trình duyệt hiện tại chưa hỗ trợ Web Speech API. Bạn nên mở web bằng Google Chrome hoặc Microsoft Edge để nhận diện giọng nói mượt mà nhất!'
                });
            }
            return false;
        }

        // Cancel any active TTS playback to avoid audio echoing into mic
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
        }

        this.stop();

        this.callbacks = callbacks;
        this.recognition = new this.SpeechRecClass();
        this.recognition.lang = callbacks.lang || 'en-US';
        this.recognition.continuous = false;
        this.recognition.interimResults = true;
        this.recognition.maxAlternatives = 1;

        let finalTranscript = '';

        this.recognition.onstart = () => {
            this.isRecording = true;
            if (this.callbacks && this.callbacks.onStart) {
                this.callbacks.onStart();
            }
        };

        this.recognition.onresult = (event) => {
            let interim = '';
            for (let i = event.resultIndex; i < event.results.length; ++i) {
                const res = event.results[i];
                if (res.isFinal) {
                    finalTranscript += res[0].transcript + ' ';
                } else {
                    interim += res[0].transcript;
                }
            }

            if (this.callbacks && this.callbacks.onInterim) {
                this.callbacks.onInterim(interim || finalTranscript);
            }
        };

        this.recognition.onerror = (event) => {
            let userMsg = 'Đã xảy ra lỗi khi nhận diện giọng nói.';
            if (event.error === 'not-allowed') {
                userMsg = 'Quyền truy cập micro đã bị chặn. Vui lòng nhấn vào biểu tượng ổ khóa bên trái thanh địa chỉ trình duyệt để Cho phép Micro.';
            } else if (event.error === 'no-speech') {
                userMsg = 'Chưa nhận diện được giọng nói. Bạn hãy thử lại và nói to hơn vào micro nhé.';
            } else if (event.error === 'audio-capture') {
                userMsg = 'Không tìm thấy thiết bị micro. Hãy cắm tai nghe hoặc kiểm tra cài đặt âm thanh.';
            } else if (event.error === 'network') {
                userMsg = 'Lỗi kết nối mạng của dịch vụ nhận diện giọng nói.';
            }

            if (this.callbacks && this.callbacks.onError) {
                this.callbacks.onError({ error: event.error, message: userMsg });
            }
        };

        this.recognition.onend = () => {
            this.isRecording = false;
            const resText = finalTranscript.trim();
            if (this.callbacks && this.callbacks.onResult) {
                this.callbacks.onResult(resText);
            }
            if (this.callbacks && this.callbacks.onEnd) {
                this.callbacks.onEnd();
            }
        };

        try {
            this.recognition.start();
            return true;
        } catch (e) {
            console.error('SpeechRecognition start error:', e);
            if (callbacks.onError) {
                callbacks.onError({ error: 'start-failed', message: 'Không thể khởi động micro: ' + e.message });
            }
            return false;
        }
    }

    stop() {
        if (this.recognition && this.isRecording) {
            try {
                this.recognition.stop();
            } catch (e) {}
        }
        this.isRecording = false;
    }

    abort() {
        if (this.recognition) {
            try {
                this.recognition.abort();
            } catch (e) {}
        }
        this.isRecording = false;
    }
}

// App logic for English Learning Companion
class EnglishApp {
    constructor() {
        this.storageKey = 'english_learning_items_v3';
        this.topicsKey = 'english_learning_topics_v3';
        this.items = this.loadItems();
        this.topics = this.loadTopics();
        
        // Navigation & State
        this.currentTab = 'flashcard';
        this.currentFilter = 'all'; // all | vocab | sentence
        this.currentTopicFilter = 'all';
        this.searchQuery = '';
        this.libraryVisibleCount = 48; // Phân trang nhẹ nhàng
        
        // Flashcard State
        this.flashcardIndex = 0;
        this.isFlipped = false;
        this.flashcardList = [];

        // Speech Practice & Recognition State
        this.evaluator = new PronunciationEvaluator();
        this.speechManager = new SpeechPracticeManager();
        this.spMode = 'words'; // words | sentences | dialogues
        this.spIndex = 0;
        this.spTopic = 'all';
        this.spIsRecording = false;
        this.fcIsRecording = false;

        // Quiz State
        this.quizQuestions = [];
        this.quizIndex = 0;
        this.quizScore = 0;
        this.isQuizActive = false;

        // Reading & Dialogue State
        this.readingFilter = 'all'; // all | conversation | passage
        this.readingIndex = 0;
        this.showReadingTranslation = false;
        this.showReadingVocab = true;
        this.readingUserAnswers = {};
        this.readingQuizSubmitted = false;
        this.isReadingSpeaking = false;

        // TTS Speech Rate
        this.speechRate = 0.85; // Tốc độ chuẩn chậm cho người mới

        // Elements
        this.initDOMElements();
        this.initEvents();
        this.refreshAll();
    }

    loadItems() {
        const stored = localStorage.getItem(this.storageKey);
        if (stored) {
            try {
                const parsed = JSON.parse(stored);
                if (Array.isArray(parsed) && parsed.length >= INITIAL_DATA.length) {
                    return parsed;
                }
                // Nếu dữ liệu lưu ít hơn bộ mẫu 520 từ, gộp thêm các từ mới vào
                const existingIds = new Set(parsed.map(i => i.id));
                const merged = [...parsed];
                INITIAL_DATA.forEach(newItem => {
                    if (!existingIds.has(newItem.id)) {
                        merged.push(newItem);
                    }
                });
                return merged;
            } catch (e) {
                console.error("Lỗi đọc dữ liệu v2", e);
            }
        }

        // Tự động chuyển từ v1 sang nếu có từ tự thêm
        const storedV1 = localStorage.getItem('english_learning_items_v1');
        if (storedV1) {
            try {
                const oldList = JSON.parse(storedV1);
                const userCreated = oldList.filter(item => !INITIAL_DATA.some(init => init.id === item.id));
                return [...userCreated, ...INITIAL_DATA];
            } catch (e) {
                console.error("Lỗi đọc v1", e);
            }
        }

        return [...INITIAL_DATA];
    }

    saveItems() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.items));
        this.refreshStats();
    }

    loadTopics() {
        const stored = localStorage.getItem(this.topicsKey);
        if (stored) {
            try {
                return JSON.parse(stored);
            } catch (e) {
                console.error("Lỗi đọc chủ đề", e);
            }
        }
        return [...DEFAULT_TOPICS];
    }

    saveTopics() {
        localStorage.setItem(this.topicsKey, JSON.stringify(this.topics));
    }

    initDOMElements() {
        // Tab buttons & containers
        this.tabBtns = document.querySelectorAll('.tab-btn');
        this.tabContents = document.querySelectorAll('.tab-content');

        // Stats
        this.statTotal = document.getElementById('stat-total');
        this.statVocab = document.getElementById('stat-vocab');
        this.statSentences = document.getElementById('stat-sentences');
        this.statMastered = document.getElementById('stat-mastered');

        // Flashcard elements
        this.fcCard = document.getElementById('flashcard-element');
        this.fcFrontText = document.getElementById('fc-front-text');
        this.fcFrontIpa = document.getElementById('fc-front-ipa');
        this.fcFrontTopic = document.getElementById('fc-front-topic');
        this.fcBackMeaning = document.getElementById('fc-back-meaning');
        this.fcBackExample = document.getElementById('fc-back-example');
        this.fcBackExMeaning = document.getElementById('fc-back-ex-meaning');
        this.fcBackNote = document.getElementById('fc-back-note');
        this.fcProgress = document.getElementById('fc-progress');
        this.fcPrevBtn = document.getElementById('fc-prev-btn');
        this.fcNextBtn = document.getElementById('fc-next-btn');
        this.fcShuffleBtn = document.getElementById('fc-shuffle-btn');
        this.fcSpeakBtn = document.getElementById('fc-speak-btn');
        this.fcSpeakSlowBtn = document.getElementById('fc-speak-slow-btn');
        this.fcMasterBtn = document.getElementById('fc-master-btn');

        // Flashcard Speech elements
        this.fcMicBtn = document.getElementById('fc-mic-btn');
        this.fcSpeechBox = document.getElementById('fc-speech-box');
        this.fcSpeechCloseBtn = document.getElementById('fc-speech-close-btn');
        this.fcSpeechStatusText = document.getElementById('fc-speech-status-text');
        this.fcSpeechRecBtn = document.getElementById('fc-speech-rec-btn');
        this.fcSpeechRecText = document.getElementById('fc-speech-rec-text');
        this.fcSpeechMicDot = document.getElementById('fc-speech-mic-dot');
        this.fcSpeechInterimBox = document.getElementById('fc-speech-interim-box');
        this.fcSpeechInterimText = document.getElementById('fc-speech-interim-text');
        this.fcSpeechResultBox = document.getElementById('fc-speech-result-box');
        this.fcSpeechScore = document.getElementById('fc-speech-score');
        this.fcSpeechVerdict = document.getElementById('fc-speech-verdict');
        this.fcSpeechTokens = document.getElementById('fc-speech-tokens');
        this.fcSpeechSpoken = document.getElementById('fc-speech-spoken');

        // Library elements
        this.libraryContainer = document.getElementById('library-list');
        this.searchInput = document.getElementById('search-input');
        this.typeFilter = document.getElementById('type-filter');
        this.topicFilter = document.getElementById('topic-filter');

        // Modal elements
        this.modal = document.getElementById('item-modal');
        this.itemForm = document.getElementById('item-form');
        this.modalTitle = document.getElementById('modal-title');
        this.formId = document.getElementById('form-id');
        this.formType = document.getElementById('form-type');
        this.formText = document.getElementById('form-text');
        this.formIpa = document.getElementById('form-ipa');
        this.formMeaning = document.getElementById('form-meaning');
        this.formTopic = document.getElementById('form-topic');
        this.formCustomTopic = document.getElementById('form-custom-topic');
        this.formExample = document.getElementById('form-example');
        this.formExampleMeaning = document.getElementById('form-example-meaning');
        this.formNote = document.getElementById('form-note');
        this.openModalBtn = document.getElementById('open-add-modal-btn');
        this.closeModalBtn = document.getElementById('close-modal-btn');

        // Quiz elements
        this.quizStartBox = document.getElementById('quiz-start-box');
        this.quizPlayBox = document.getElementById('quiz-play-box');
        this.quizResultBox = document.getElementById('quiz-result-box');
        this.startQuizBtn = document.getElementById('start-quiz-btn');
        this.quizQuestionText = document.getElementById('quiz-question-text');
        this.quizQuestionSub = document.getElementById('quiz-question-sub');
        this.quizOptionsContainer = document.getElementById('quiz-options');
        this.quizProgress = document.getElementById('quiz-progress');
        this.quizScoreText = document.getElementById('quiz-score-text');
        this.quizFeedback = document.getElementById('quiz-feedback');
        this.quizNextBtn = document.getElementById('quiz-next-btn');

        // Backup elements
        this.exportBtn = document.getElementById('export-data-btn');
        this.importInput = document.getElementById('import-file-input');
        this.resetDataBtn = document.getElementById('reset-data-btn');

        // Reading elements
        this.readingFilterBtns = document.querySelectorAll('.reading-filter-btn');
        this.readingSelect = document.getElementById('reading-select');
        this.readingPrevBtn = document.getElementById('reading-prev-btn');
        this.readingNextBtn = document.getElementById('reading-next-btn');
        this.readingTypeBadge = document.getElementById('reading-type-badge');
        this.readingLevelBadge = document.getElementById('reading-level-badge');
        this.readingTopicBadge = document.getElementById('reading-topic-badge');
        this.readingTitle = document.getElementById('reading-title');
        this.readingSummary = document.getElementById('reading-summary');
        this.readingTtsBtn = document.getElementById('reading-tts-btn');
        this.readingTtsIcon = document.getElementById('reading-tts-icon');
        this.readingTtsText = document.getElementById('reading-tts-text');
        this.readingSpeechRate = document.getElementById('reading-speech-rate');
        this.readingToggleTransBtn = document.getElementById('reading-toggle-trans-btn');
        this.readingTransBtnText = document.getElementById('reading-trans-btn-text');
        this.readingToggleVocabBtn = document.getElementById('reading-toggle-vocab-btn');
        this.readingVocabPanel = document.getElementById('reading-vocab-panel');
        this.readingVocabChips = document.getElementById('reading-vocab-chips');
        this.readingBody = document.getElementById('reading-body');
        this.readingQuizCard = document.getElementById('reading-quiz-card');
        this.readingQuizContainer = document.getElementById('reading-quiz-container');
        this.readingQuizBadgeCount = document.getElementById('reading-quiz-badge-count');
        this.readingQuizScoreBanner = document.getElementById('reading-quiz-score-banner');
        this.readingSubmitQuizBtn = document.getElementById('reading-submit-quiz-btn');
        this.readingRetryQuizBtn = document.getElementById('reading-retry-quiz-btn');

        // Speaking Lab elements
        this.spModeBtns = document.querySelectorAll('.sp-mode-btn');
        this.spTopicSelect = document.getElementById('sp-topic-select');
        this.spRandomBtn = document.getElementById('sp-random-btn');
        this.spTargetBadge = document.getElementById('sp-target-badge');
        this.spTargetTopic = document.getElementById('sp-target-topic');
        this.spProgressText = document.getElementById('sp-progress-text');
        this.spTargetText = document.getElementById('sp-target-text');
        this.spTargetIpa = document.getElementById('sp-target-ipa');
        this.spTargetMeaning = document.getElementById('sp-target-meaning');
        this.spTargetExampleBox = document.getElementById('sp-target-example-box');
        this.spTargetExample = document.getElementById('sp-target-example');
        this.spListenStdBtn = document.getElementById('sp-listen-std-btn');
        this.spListenSlowBtn = document.getElementById('sp-listen-slow-btn');
        this.spRecordBtn = document.getElementById('sp-record-btn');
        this.spPulseRing = document.getElementById('sp-pulse-ring');
        this.spWaveBars = document.getElementById('sp-wave-bars');
        this.spRecordIcon = document.getElementById('sp-record-icon');
        this.spRecordSub = document.getElementById('sp-record-sub');
        this.spStatusText = document.getElementById('sp-status-text');
        this.spInterimBox = document.getElementById('sp-interim-box');
        this.spInterimText = document.getElementById('sp-interim-text');
        this.spToggleFallbackBtn = document.getElementById('sp-toggle-fallback-btn');
        this.spFallbackInputBox = document.getElementById('sp-fallback-input-box');
        this.spFallbackInput = document.getElementById('sp-fallback-input');
        this.spFallbackSubmitBtn = document.getElementById('sp-fallback-submit-btn');
        this.spResultCard = document.getElementById('sp-result-card');
        this.spResultScore = document.getElementById('sp-result-score');
        this.spResultBadge = document.getElementById('sp-result-badge');
        this.spResultFeedback = document.getElementById('sp-result-feedback');
        this.spCompTarget = document.getElementById('sp-comp-target');
        this.spCompSpoken = document.getElementById('sp-comp-spoken');
        this.spTokensContainer = document.getElementById('sp-tokens-container');
        this.spRetryBtn = document.getElementById('sp-retry-btn');
        this.spPrevBtn = document.getElementById('sp-prev-btn');
        this.spNextBtn = document.getElementById('sp-next-btn');
    }

    initEvents() {
        // Tab switching
        this.tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTab = btn.dataset.tab;
                this.switchTab(targetTab);
            });
        });

        // Flashcard events
        this.fcCard.addEventListener('click', (e) => {
            // Don't flip if clicking sound buttons
            if (e.target.closest('.audio-action-btn')) return;
            this.toggleFlip();
        });

        // Touch swipe gestures for mobile
        let touchStartX = 0;
        let touchStartY = 0;
        let touchStartTime = 0;

        this.fcCard.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].clientX;
            touchStartY = e.changedTouches[0].clientY;
            touchStartTime = Date.now();
        }, { passive: true });

        this.fcCard.addEventListener('touchend', (e) => {
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const diffX = touchEndX - touchStartX;
            const diffY = touchEndY - touchStartY;
            const timeDiff = Date.now() - touchStartTime;

            // Horizontal swipe detected
            if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY) * 1.4 && timeDiff < 600) {
                if (diffX < 0) {
                    this.nextFlashcard();
                } else {
                    this.prevFlashcard();
                }
            }
        }, { passive: true });

        this.fcPrevBtn.addEventListener('click', () => this.prevFlashcard());
        this.fcNextBtn.addEventListener('click', () => this.nextFlashcard());
        this.fcShuffleBtn.addEventListener('click', () => this.shuffleFlashcards());
        this.fcSpeakBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.speakCurrentFlashcard(1.0);
        });
        this.fcSpeakSlowBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.speakCurrentFlashcard(0.7);
        });
        this.fcMasterBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.toggleCurrentFlashcardMastery();
        });

        // Keyboard shortcuts for flashcard
        document.addEventListener('keydown', (e) => {
            if (this.currentTab === 'flashcard' && !this.modal.classList.contains('active')) {
                if (e.code === 'Space') {
                    e.preventDefault();
                    this.toggleFlip();
                } else if (e.code === 'ArrowRight') {
                    this.nextFlashcard();
                } else if (e.code === 'ArrowLeft') {
                    this.prevFlashcard();
                }
            }
        });

        // Search & Filters
        this.searchInput.addEventListener('input', (e) => {
            this.searchQuery = e.target.value.toLowerCase().trim();
            this.libraryVisibleCount = 48;
            this.renderLibrary();
        });

        this.typeFilter.addEventListener('change', (e) => {
            this.currentFilter = e.target.value;
            this.libraryVisibleCount = 48;
            this.renderLibrary();
            this.updateFlashcardList();
        });

        this.topicFilter.addEventListener('change', (e) => {
            this.currentTopicFilter = e.target.value;
            this.libraryVisibleCount = 48;
            this.renderLibrary();
            this.updateFlashcardList();
        });

        // Modal
        this.openModalBtn.addEventListener('click', () => this.openAddModal());
        this.closeModalBtn.addEventListener('click', () => this.closeModal());
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal) this.closeModal();
        });

        this.formTopic.addEventListener('change', (e) => {
            if (e.target.value === '__new__') {
                this.formCustomTopic.classList.remove('hidden');
                this.formCustomTopic.required = true;
                this.formCustomTopic.focus();
            } else {
                this.formCustomTopic.classList.add('hidden');
                this.formCustomTopic.required = false;
            }
        });

        this.itemForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleFormSubmit();
        });

        // Quiz
        this.startQuizBtn.addEventListener('click', () => this.startQuiz());
        this.quizNextBtn.addEventListener('click', () => this.nextQuizQuestion());
        document.getElementById('restart-quiz-btn').addEventListener('click', () => this.startQuiz());

        // Backup
        this.exportBtn.addEventListener('click', () => this.exportData());
        this.importInput.addEventListener('change', (e) => this.importData(e));
        this.resetDataBtn.addEventListener('click', () => this.resetData());

        // Reading events
        if (this.readingFilterBtns) {
            this.readingFilterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    this.setReadingFilter(btn.dataset.filter);
                });
            });
        }
        if (this.readingSelect) {
            this.readingSelect.addEventListener('change', (e) => {
                const filtered = this.getFilteredReadings();
                const idx = filtered.findIndex(r => r.id === e.target.value);
                if (idx !== -1) {
                    this.readingIndex = idx;
                    this.stopReadingTTS();
                    this.resetReadingQuizState();
                    this.renderCurrentReading();
                }
            });
        }
        if (this.readingPrevBtn) {
            this.readingPrevBtn.addEventListener('click', () => this.prevReading());
        }
        if (this.readingNextBtn) {
            this.readingNextBtn.addEventListener('click', () => this.nextReading());
        }
        if (this.readingTtsBtn) {
            this.readingTtsBtn.addEventListener('click', () => this.toggleReadingTTS());
        }
        if (this.readingToggleTransBtn) {
            this.readingToggleTransBtn.addEventListener('click', () => this.toggleReadingTranslation());
        }
        if (this.readingToggleVocabBtn) {
            this.readingToggleVocabBtn.addEventListener('click', () => this.toggleReadingVocabPanel());
        }
        if (this.readingSubmitQuizBtn) {
            this.readingSubmitQuizBtn.addEventListener('click', () => this.submitReadingQuiz());
        }
        if (this.readingRetryQuizBtn) {
            this.readingRetryQuizBtn.addEventListener('click', () => this.retryReadingQuiz());
        }

        // Flashcard Speech Events
        if (this.fcMicBtn) {
            this.fcMicBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleFlashcardSpeechBox();
            });
        }
        if (this.fcSpeechCloseBtn) {
            this.fcSpeechCloseBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.closeFlashcardSpeechBox();
            });
        }
        if (this.fcSpeechRecBtn) {
            this.fcSpeechRecBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleFlashcardRecording();
            });
        }

        // Speaking Lab Events
        if (this.spModeBtns) {
            this.spModeBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    this.setSpeakingMode(btn.dataset.mode);
                });
            });
        }
        if (this.spTopicSelect) {
            this.spTopicSelect.addEventListener('change', (e) => {
                this.spTopic = e.target.value;
                this.spIndex = 0;
                this.renderSpeakingLab();
            });
        }
        if (this.spRandomBtn) {
            this.spRandomBtn.addEventListener('click', () => this.randomSpeakingItem());
        }
        if (this.spListenStdBtn) {
            this.spListenStdBtn.addEventListener('click', () => this.listenCurrentSpeakingTarget(1.0));
        }
        if (this.spListenSlowBtn) {
            this.spListenSlowBtn.addEventListener('click', () => this.listenCurrentSpeakingTarget(0.7));
        }
        if (this.spRecordBtn) {
            this.spRecordBtn.addEventListener('click', () => this.toggleSpeakingLabRecording());
        }
        if (this.spToggleFallbackBtn) {
            this.spToggleFallbackBtn.addEventListener('click', () => {
                if (this.spFallbackInputBox) {
                    this.spFallbackInputBox.classList.toggle('hidden');
                    if (!this.spFallbackInputBox.classList.contains('hidden') && this.spFallbackInput) {
                        this.spFallbackInput.focus();
                    }
                }
            });
        }
        if (this.spFallbackSubmitBtn) {
            this.spFallbackSubmitBtn.addEventListener('click', () => {
                if (this.spFallbackInput) {
                    const text = this.spFallbackInput.value.trim();
                    if (text) {
                        this.evaluateSpeakingInput(text);
                        this.spFallbackInput.value = '';
                    }
                }
            });
        }
        if (this.spFallbackInput) {
            this.spFallbackInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    if (this.spFallbackSubmitBtn) this.spFallbackSubmitBtn.click();
                }
            });
        }
        if (this.spRetryBtn) {
            this.spRetryBtn.addEventListener('click', () => {
                this.toggleSpeakingLabRecording();
            });
        }
        if (this.spPrevBtn) {
            this.spPrevBtn.addEventListener('click', () => this.prevSpeakingItem());
        }
        if (this.spNextBtn) {
            this.spNextBtn.addEventListener('click', () => this.nextSpeakingItem());
        }
    }

    switchTab(tabId) {
        this.currentTab = tabId;
        this.tabBtns.forEach(btn => {
            if (btn.dataset.tab === tabId) {
                btn.classList.add('active', 'border-indigo-600', 'text-indigo-600', 'dark:text-indigo-400');
                btn.classList.remove('border-transparent', 'text-gray-500');
            } else {
                btn.classList.remove('active', 'border-indigo-600', 'text-indigo-600', 'dark:text-indigo-400');
                btn.classList.add('border-transparent', 'text-gray-500');
            }
        });

        this.tabContents.forEach(content => {
            if (content.id === `tab-${tabId}`) {
                content.classList.remove('hidden');
            } else {
                content.classList.add('hidden');
            }
        });

        if (tabId === 'flashcard') {
            this.updateFlashcardList();
        } else if (tabId === 'library') {
            this.renderLibrary();
        } else if (tabId === 'reading') {
            this.initReadingModule();
        } else if (tabId === 'speaking') {
            this.initSpeakingLab();
        }

        if (tabId !== 'reading') {
            this.stopReadingTTS();
        }
        if (tabId !== 'speaking') {
            this.stopSpeakingLabRecording();
        }
        if (tabId !== 'flashcard') {
            this.closeFlashcardSpeechBox();
        }
    }

    refreshAll() {
        this.updateTopicDropdowns();
        this.refreshStats();
        this.updateFlashcardList();
        this.renderLibrary();
        this.initReadingModule();
        this.initSpeakingLab();
    }

    refreshStats() {
        const total = this.items.length;
        const vocabs = this.items.filter(i => i.type === 'vocab').length;
        const sentences = this.items.filter(i => i.type === 'sentence').length;
        const mastered = this.items.filter(i => i.status === 'mastered').length;

        this.statTotal.textContent = total;
        this.statVocab.textContent = vocabs;
        this.statSentences.textContent = sentences;
        this.statMastered.textContent = mastered;
    }

    updateTopicDropdowns() {
        const uniqueTopics = Array.from(new Set([...this.topics, ...this.items.map(i => i.topic)])).filter(Boolean);
        
        // Filter topic dropdown
        let filterHtml = `<option value="all">Tất cả chủ đề (${uniqueTopics.length})</option>`;
        uniqueTopics.forEach(t => {
            filterHtml += `<option value="${t}">${t}</option>`;
        });
        this.topicFilter.innerHTML = filterHtml;

        // Modal topic select
        let modalHtml = `<option value="">-- Chọn chủ đề có sẵn --</option>`;
        uniqueTopics.forEach(t => {
            modalHtml += `<option value="${t}">${t}</option>`;
        });
        modalHtml += `<option value="__new__">+ Thêm chủ đề mới...</option>`;
        this.formTopic.innerHTML = modalHtml;
    }

    // ================= FLASHCARD LOGIC =================
    updateFlashcardList() {
        this.flashcardList = this.items.filter(item => {
            const matchType = this.currentFilter === 'all' || item.type === this.currentFilter;
            const matchTopic = this.currentTopicFilter === 'all' || item.topic === this.currentTopicFilter;
            return matchType && matchTopic;
        });

        if (this.flashcardIndex >= this.flashcardList.length) {
            this.flashcardIndex = 0;
        }

        this.renderFlashcard();
    }

    toggleFlip() {
        if (this.flashcardList.length === 0) return;
        this.isFlipped = !this.isFlipped;
        if (this.isFlipped) {
            this.fcCard.classList.add('flipped');
        } else {
            this.fcCard.classList.remove('flipped');
        }
    }

    renderFlashcard() {
        this.isFlipped = false;
        this.fcCard.classList.remove('flipped');

        if (this.flashcardList.length === 0) {
            this.fcFrontText.textContent = "Chưa có nội dung phù hợp";
            this.fcFrontIpa.textContent = "";
            this.fcFrontTopic.textContent = "Trống";
            this.fcBackMeaning.textContent = "Hãy thêm từ mới hoặc chọn bộ lọc khác!";
            this.fcBackExample.textContent = "";
            this.fcBackExMeaning.textContent = "";
            this.fcBackNote.textContent = "";
            this.fcProgress.textContent = "0 / 0";
            return;
        }

        const item = this.flashcardList[this.flashcardIndex];
        this.fcFrontText.textContent = item.text;
        this.fcFrontIpa.textContent = item.ipa || '';
        this.fcFrontTopic.textContent = `${item.type === 'vocab' ? 'Từ vựng' : 'Mẫu câu'} • ${item.topic}`;
        
        this.fcBackMeaning.textContent = item.meaning;
        this.fcBackExample.textContent = item.example ? `"${item.example}"` : 'Chưa có ví dụ';
        this.fcBackExMeaning.textContent = item.exampleMeaning ? `→ ${item.exampleMeaning}` : '';
        this.fcBackNote.textContent = item.note || 'Không có ghi chú ngữ pháp thêm.';

        // Master button style
        if (item.status === 'mastered') {
            this.fcMasterBtn.innerHTML = `⭐ Đã thuộc`;
            this.fcMasterBtn.className = "px-3 py-1.5 text-xs rounded-full font-medium bg-amber-100 text-amber-800 border border-amber-300 dark:bg-amber-900/50 dark:text-amber-200";
        } else {
            this.fcMasterBtn.innerHTML = `○ Đánh dấu đã thuộc`;
            this.fcMasterBtn.className = "px-3 py-1.5 text-xs rounded-full font-medium bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-300 dark:bg-gray-800 dark:text-gray-300";
        }

        this.fcProgress.textContent = `${this.flashcardIndex + 1} / ${this.flashcardList.length}`;
    }

    nextFlashcard() {
        if (this.flashcardList.length <= 1) return;
        this.flashcardIndex = (this.flashcardIndex + 1) % this.flashcardList.length;
        this.renderFlashcard();
    }

    prevFlashcard() {
        if (this.flashcardList.length <= 1) return;
        this.flashcardIndex = (this.flashcardIndex - 1 + this.flashcardList.length) % this.flashcardList.length;
        this.renderFlashcard();
    }

    shuffleFlashcards() {
        if (this.flashcardList.length <= 1) return;
        for (let i = this.flashcardList.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.flashcardList[i], this.flashcardList[j]] = [this.flashcardList[j], this.flashcardList[i]];
        }
        this.flashcardIndex = 0;
        this.renderFlashcard();
    }

    speakCurrentFlashcard(rate = 1.0) {
        if (this.flashcardList.length === 0) return;
        const text = this.flashcardList[this.flashcardIndex].text;
        this.speak(text, rate);
    }

    toggleCurrentFlashcardMastery() {
        if (this.flashcardList.length === 0) return;
        const currentItem = this.flashcardList[this.flashcardIndex];
        currentItem.status = currentItem.status === 'mastered' ? 'learning' : 'mastered';
        this.saveItems();
        this.renderFlashcard();
    }

    // ================= TTS AUDIO =================
    getVoiceForSpeaker(speakerText = '') {
        if (!('speechSynthesis' in window)) return { voice: null, pitch: 1.0 };
        const voices = window.speechSynthesis.getVoices() || [];
        const englishVoices = voices.filter(v => v.lang && v.lang.startsWith('en'));

        const lower = (speakerText || '').toLowerCase();
        const isFemale = lower.includes('female') || 
                         /\b(sarah|lin|chloe|olivia|victoria|sophia|emma|maya|clara|emily)\b/i.test(lower);
        const isMale = lower.includes('male') || 
                       /\b(david|marcus|richard|julian|alex|ethan|daniel|arthur|brandon|james|liam)\b/i.test(lower);

        if (isFemale) {
            const femaleKeywords = ['zira', 'jenny', 'samantha', 'victoria', 'karen', 'female', 'susan', 'hazel', 'aria', 'catherine'];
            const found = englishVoices.find(v => femaleKeywords.some(k => v.name.toLowerCase().includes(k)));
            return {
                voice: found || englishVoices.find(v => !v.name.toLowerCase().includes('david') && !v.name.toLowerCase().includes('male')) || englishVoices[0] || null,
                pitch: 1.15 // Nâng nhẹ cao độ cho giọng nữ
            };
        }

        if (isMale) {
            const maleKeywords = ['david', 'mark', 'george', 'guy', 'male', 'richard', 'daniel', 'james', 'brian'];
            const found = englishVoices.find(v => maleKeywords.some(k => v.name.toLowerCase().includes(k)));
            return {
                voice: found || englishVoices.find(v => v.name.toLowerCase().includes('david') || v.name.toLowerCase().includes('male')) || englishVoices[0] || null,
                pitch: 0.90 // Hạ nhẹ cao độ cho giọng nam trầm ấm
            };
        }

        const naturalVoice = englishVoices.find(v => v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha')) || englishVoices[0] || null;
        return { voice: naturalVoice, pitch: 1.0 };
    }

    speak(text, rate = 0.85, voiceConfig = null) {
        if (!('speechSynthesis' in window)) {
            alert('Trình duyệt của bạn không hỗ trợ tính năng phát âm trực tiếp.');
            return;
        }

        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = rate;

        const config = voiceConfig || this.getVoiceForSpeaker();
        if (config.voice) {
            utterance.voice = config.voice;
        }
        if (config.pitch) {
            utterance.pitch = config.pitch;
        }

        window.speechSynthesis.speak(utterance);
    }

    // ================= LIBRARY / MANAGER =================
    renderLibrary() {
        const filtered = this.items.filter(item => {
            const matchQuery = !this.searchQuery || 
                item.text.toLowerCase().includes(this.searchQuery) ||
                item.meaning.toLowerCase().includes(this.searchQuery) ||
                (item.topic && item.topic.toLowerCase().includes(this.searchQuery));
            
            const matchType = this.currentFilter === 'all' || item.type === this.currentFilter;
            const matchTopic = this.currentTopicFilter === 'all' || item.topic === this.currentTopicFilter;

            return matchQuery && matchType && matchTopic;
        });

        if (filtered.length === 0) {
            this.libraryContainer.innerHTML = `
                <div class="col-span-full text-center py-12 bg-white dark:bg-gray-800 rounded-xl border border-dashed border-gray-300 dark:border-gray-700">
                    <p class="text-gray-500 dark:text-gray-400">Không tìm thấy từ vựng hoặc mẫu câu nào phù hợp.</p>
                    <button class="mt-4 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-sm font-medium transition" onclick="app.openAddModal()">
                        + Thêm từ đầu tiên
                    </button>
                </div>
            `;
            return;
        }

        const visibleItems = filtered.slice(0, this.libraryVisibleCount);
        const hasMore = this.libraryVisibleCount < filtered.length;

        const cardsHtml = visibleItems.map(item => `
            <div class="bg-white dark:bg-gray-800 rounded-xl p-5 border border-gray-200 dark:border-gray-700 shadow-sm hover:shadow-md transition flex flex-col justify-between">
                <div>
                    <div class="flex items-start justify-between gap-2 mb-2">
                        <span class="inline-block px-2.5 py-0.5 text-xs font-semibold rounded-full ${item.type === 'vocab' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300' : 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-300'}">
                            ${item.type === 'vocab' ? 'Từ vựng' : 'Mẫu câu'}
                        </span>
                        <span class="text-xs text-gray-500 bg-gray-100 dark:bg-gray-700 px-2 py-0.5 rounded truncate max-w-[150px]" title="${item.topic || 'Chung'}">
                            ${item.topic || 'Chung'}
                        </span>
                    </div>

                    <div class="flex items-baseline gap-2 mb-1">
                        <h3 class="text-lg font-bold text-gray-900 dark:text-white leading-tight">${item.text}</h3>
                        <button onclick="app.speak('${item.text.replace(/'/g, "\\'")}', 0.85)" class="text-indigo-600 hover:text-indigo-800 dark:text-indigo-400 p-1" title="Nghe phát âm">
                            🔊
                        </button>
                    </div>

                    ${item.ipa ? `<p class="text-xs font-mono text-indigo-600 dark:text-indigo-300 mb-2">${item.ipa}</p>` : ''}
                    
                    <p class="text-sm font-medium text-gray-800 dark:text-gray-200 mb-3 bg-amber-50 dark:bg-amber-950/30 p-2 rounded border-l-2 border-amber-400">
                        ${item.meaning}
                    </p>

                    ${item.example ? `
                        <div class="text-xs text-gray-600 dark:text-gray-400 mb-2 bg-gray-50 dark:bg-gray-900/50 p-2.5 rounded">
                            <p class="font-medium text-gray-800 dark:text-gray-200">Ví dụ: ${item.example}</p>
                            ${item.exampleMeaning ? `<p class="text-gray-500 dark:text-gray-400 mt-0.5">Dịch: ${item.exampleMeaning}</p>` : ''}
                        </div>
                    ` : ''}

                    ${item.note ? `
                        <p class="text-xs text-gray-500 dark:text-gray-400 italic">💡 ${item.note}</p>
                    ` : ''}
                </div>

                <div class="mt-4 pt-3 border-t border-gray-100 dark:border-gray-700 flex items-center justify-between">
                    <button onclick="app.toggleMastery('${item.id}')" class="text-xs font-medium ${item.status === 'mastered' ? 'text-amber-600 font-semibold' : 'text-gray-400 hover:text-gray-600'}">
                        ${item.status === 'mastered' ? '⭐ Đã thuộc' : '○ Chưa thuộc'}
                    </button>
                    <div class="flex items-center gap-2">
                        <button onclick="app.editItem('${item.id}')" class="text-xs text-blue-600 hover:underline">Sửa</button>
                        <button onclick="app.deleteItem('${item.id}')" class="text-xs text-rose-500 hover:underline">Xóa</button>
                    </div>
                </div>
            </div>
        `).join('');

        const loadMoreHtml = hasMore ? `
            <div class="col-span-full text-center py-6">
                <button onclick="app.loadMoreLibrary()" class="px-6 py-2.5 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 rounded-xl font-semibold text-sm transition">
                    ⬇️ Hiển thị thêm (Đang xem ${visibleItems.length}/${filtered.length} mục)
                </button>
            </div>
        ` : (filtered.length > 48 ? `
            <div class="col-span-full text-center py-4 text-xs text-gray-400">
                Đã hiển thị toàn bộ ${filtered.length} mục.
            </div>
        ` : '');

        this.libraryContainer.innerHTML = cardsHtml + loadMoreHtml;
    }

    loadMoreLibrary() {
        this.libraryVisibleCount += 48;
        this.renderLibrary();
    }

    toggleMastery(id) {
        const item = this.items.find(i => i.id === id);
        if (item) {
            item.status = item.status === 'mastered' ? 'learning' : 'mastered';
            this.saveItems();
            this.renderLibrary();
            this.updateFlashcardList();
        }
    }

    // ================= MODAL & FORM =================
    openAddModal() {
        this.modalTitle.textContent = "Thêm từ vựng hoặc mẫu câu mới";
        this.itemForm.reset();
        this.formId.value = '';
        this.formCustomTopic.classList.add('hidden');
        this.modal.classList.add('active');
        this.formText.focus();
    }

    closeModal() {
        this.modal.classList.remove('active');
    }

    editItem(id) {
        const item = this.items.find(i => i.id === id);
        if (!item) return;

        this.modalTitle.textContent = "Chỉnh sửa mục học tập";
        this.formId.value = item.id;
        this.formType.value = item.type;
        this.formText.value = item.text;
        this.formIpa.value = item.ipa || '';
        this.formMeaning.value = item.meaning;
        
        // Topic selection
        const optionExists = Array.from(this.formTopic.options).some(o => o.value === item.topic);
        if (optionExists) {
            this.formTopic.value = item.topic;
            this.formCustomTopic.classList.add('hidden');
        } else {
            this.formTopic.value = '__new__';
            this.formCustomTopic.value = item.topic;
            this.formCustomTopic.classList.remove('hidden');
        }

        this.formExample.value = item.example || '';
        this.formExampleMeaning.value = item.exampleMeaning || '';
        this.formNote.value = item.note || '';

        this.modal.classList.add('active');
    }

    deleteItem(id) {
        const item = this.items.find(i => i.id === id);
        if (!item) return;
        if (confirm(`Bạn có chắc muốn xóa "${item.text}" không?`)) {
            this.items = this.items.filter(i => i.id !== id);
            this.saveItems();
            this.refreshAll();
        }
    }

    handleFormSubmit() {
        const id = this.formId.value || 'item-' + Date.now();
        let topic = this.formTopic.value;
        if (topic === '__new__') {
            topic = this.formCustomTopic.value.trim() || 'Chủ đề chung';
            if (!this.topics.includes(topic)) {
                this.topics.push(topic);
                this.saveTopics();
                this.updateTopicDropdowns();
            }
        }

        const newItem = {
            id: id,
            type: this.formType.value,
            text: this.formText.value.trim(),
            ipa: this.formIpa.value.trim(),
            meaning: this.formMeaning.value.trim(),
            topic: topic || 'Chủ đề chung',
            example: this.formExample.value.trim(),
            exampleMeaning: this.formExampleMeaning.value.trim(),
            note: this.formNote.value.trim(),
            status: 'new',
            dateAdded: new Date().toISOString().split('T')[0]
        };

        const existingIndex = this.items.findIndex(i => i.id === id);
        if (existingIndex >= 0) {
            newItem.status = this.items[existingIndex].status;
            this.items[existingIndex] = newItem;
        } else {
            this.items.unshift(newItem);
        }

        this.saveItems();
        this.closeModal();
        this.refreshAll();
    }

    // ================= QUIZ LOGIC =================
    startQuiz() {
        if (this.items.length < 4) {
            alert("Bạn cần ít nhất 4 từ hoặc mẫu câu để bắt đầu làm bài trắc nghiệm!");
            return;
        }

        // Tạo bộ 5-10 câu hỏi ngẫu nhiên từ kho từ vựng
        const shuffled = [...this.items].sort(() => 0.5 - Math.random());
        const selected = shuffled.slice(0, Math.min(10, shuffled.length));

        this.quizQuestions = selected.map(item => {
            // Lấy 3 lựa chọn sai ngẫu nhiên
            const wrongOptions = this.items
                .filter(i => i.id !== item.id)
                .sort(() => 0.5 - Math.random())
                .slice(0, 3)
                .map(i => i.meaning);

            const options = [...wrongOptions, item.meaning].sort(() => 0.5 - Math.random());
            return {
                target: item,
                options: options,
                correctAnswer: item.meaning
            };
        });

        this.quizIndex = 0;
        this.quizScore = 0;
        this.isQuizActive = true;

        this.quizStartBox.classList.add('hidden');
        this.quizResultBox.classList.add('hidden');
        this.quizPlayBox.classList.remove('hidden');

        this.renderQuizQuestion();
    }

    renderQuizQuestion() {
        const q = this.quizQuestions[this.quizIndex];
        this.quizProgress.textContent = `Câu ${this.quizIndex + 1} / ${this.quizQuestions.length}`;
        this.quizScoreText.textContent = `Điểm: ${this.quizScore}`;

        this.quizQuestionText.textContent = q.target.text;
        this.quizQuestionSub.textContent = q.target.ipa ? `${q.target.ipa} • ${q.target.topic}` : q.target.topic;
        this.quizFeedback.classList.add('hidden');
        this.quizNextBtn.classList.add('hidden');

        this.quizOptionsContainer.innerHTML = q.options.map((opt, idx) => `
            <button class="quiz-option-btn w-full text-left p-4 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-indigo-500 bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 font-medium transition" onclick="app.checkAnswer('${opt.replace(/'/g, "\\'")}', this)">
                <span class="inline-block w-7 h-7 text-center leading-7 rounded-full bg-gray-100 dark:bg-gray-700 text-sm font-bold mr-2">
                    ${String.fromCharCode(65 + idx)}
                </span>
                ${opt}
            </button>
        `).join('');

        // Phát âm câu hỏi
        this.speak(q.target.text, 0.85);
    }

    checkAnswer(selectedAnswer, buttonElement) {
        const q = this.quizQuestions[this.quizIndex];
        const allButtons = this.quizOptionsContainer.querySelectorAll('.quiz-option-btn');
        allButtons.forEach(btn => btn.disabled = true);

        if (selectedAnswer === q.correctAnswer) {
            buttonElement.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/30', 'text-emerald-800');
            this.quizScore += 10;
            this.quizFeedback.innerHTML = `
                <div class="p-3 bg-emerald-100 dark:bg-emerald-900/40 text-emerald-800 dark:text-emerald-200 rounded-lg text-sm font-medium">
                    🎉 Chính xác! <strong>"${q.target.text}"</strong> = ${q.correctAnswer}
                    ${q.target.note ? `<p class="text-xs mt-1 text-emerald-700 dark:text-emerald-300">💡 ${q.target.note}</p>` : ''}
                </div>
            `;
        } else {
            buttonElement.classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/30', 'text-rose-800');
            // Tô xanh đáp án đúng
            allButtons.forEach(btn => {
                if (btn.innerText.includes(q.correctAnswer)) {
                    btn.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/30', 'text-emerald-800');
                }
            });
            this.quizFeedback.innerHTML = `
                <div class="p-3 bg-rose-100 dark:bg-rose-900/40 text-rose-800 dark:text-rose-200 rounded-lg text-sm font-medium">
                    ❌ Chưa đúng rồi! Đáp án chính xác là: <strong>${q.correctAnswer}</strong>
                </div>
            `;
        }

        this.quizScoreText.textContent = `Điểm: ${this.quizScore}`;
        this.quizFeedback.classList.remove('hidden');
        this.quizNextBtn.classList.remove('hidden');
    }

    nextQuizQuestion() {
        this.quizIndex++;
        if (this.quizIndex < this.quizQuestions.length) {
            this.renderQuizQuestion();
        } else {
            this.finishQuiz();
        }
    }

    finishQuiz() {
        this.quizPlayBox.classList.add('hidden');
        this.quizResultBox.classList.remove('hidden');
        
        const finalScore = document.getElementById('final-score');
        const finalMsg = document.getElementById('final-msg');

        const totalPossible = this.quizQuestions.length * 10;
        finalScore.textContent = `${this.quizScore} / ${totalPossible}`;

        if (this.quizScore === totalPossible) {
            finalMsg.textContent = "Xuất sắc! Bạn đã nhớ toàn bộ từ vựng trong lượt này!";
        } else if (this.quizScore >= totalPossible * 0.7) {
            finalMsg.textContent = "Rất tốt! Bạn đang tiến bộ rất nhanh mỗi ngày.";
        } else {
            finalMsg.textContent = "Đừng nản lòng! Hãy ôn lại qua Flashcard một lần nữa nhé!";
        }
    }

    // ================= READING & DIALOGUE MODULE =================
    getFilteredReadings() {
        if (typeof READING_DATA === 'undefined' || !Array.isArray(READING_DATA)) {
            return [];
        }
        if (this.readingFilter === 'all') return READING_DATA;
        return READING_DATA.filter(item => item.type === this.readingFilter);
    }

    initReadingModule() {
        this.updateReadingFilterButtons();
        this.populateReadingSelect();
        this.renderCurrentReading();
    }

    setReadingFilter(filter) {
        this.readingFilter = filter;
        this.readingIndex = 0;
        this.stopReadingTTS();
        this.resetReadingQuizState();
        this.updateReadingFilterButtons();
        this.populateReadingSelect();
        this.renderCurrentReading();
    }

    updateReadingFilterButtons() {
        if (!this.readingFilterBtns) return;
        this.readingFilterBtns.forEach(btn => {
            if (btn.dataset.filter === this.readingFilter) {
                btn.className = 'reading-filter-btn px-3 py-1.5 rounded-xl text-xs font-semibold bg-indigo-600 text-white shadow-xs shrink-0 transition';
            } else {
                btn.className = 'reading-filter-btn px-3 py-1.5 rounded-xl text-xs font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0 transition';
            }
        });
    }

    populateReadingSelect() {
        if (!this.readingSelect) return;
        const filtered = this.getFilteredReadings();
        this.readingSelect.innerHTML = '';
        filtered.forEach(r => {
            const opt = document.createElement('option');
            opt.value = r.id;
            opt.textContent = `${r.type === 'conversation' ? '💬' : '📰'} ${r.title} (${r.level})`;
            this.readingSelect.appendChild(opt);
        });

        if (filtered[this.readingIndex]) {
            this.readingSelect.value = filtered[this.readingIndex].id;
        }
    }

    prevReading() {
        const filtered = this.getFilteredReadings();
        if (filtered.length <= 1) return;
        this.readingIndex = (this.readingIndex - 1 + filtered.length) % filtered.length;
        this.stopReadingTTS();
        this.resetReadingQuizState();
        this.populateReadingSelect();
        this.renderCurrentReading();
    }

    nextReading() {
        const filtered = this.getFilteredReadings();
        if (filtered.length <= 1) return;
        this.readingIndex = (this.readingIndex + 1) % filtered.length;
        this.stopReadingTTS();
        this.resetReadingQuizState();
        this.populateReadingSelect();
        this.renderCurrentReading();
    }

    toggleReadingTranslation() {
        this.showReadingTranslation = !this.showReadingTranslation;
        if (this.readingTransBtnText) {
            this.readingTransBtnText.textContent = this.showReadingTranslation ? 'Ẩn bản dịch TV' : 'Hiện bản dịch TV';
        }
        if (this.readingToggleTransBtn) {
            if (this.showReadingTranslation) {
                this.readingToggleTransBtn.classList.add('bg-indigo-50', 'text-indigo-700', 'border-indigo-300');
            } else {
                this.readingToggleTransBtn.classList.remove('bg-indigo-50', 'text-indigo-700', 'border-indigo-300');
            }
        }
        this.renderReadingBodyOnly();
    }

    toggleReadingVocabPanel() {
        this.showReadingVocab = !this.showReadingVocab;
        if (this.readingVocabPanel) {
            if (this.showReadingVocab) {
                this.readingVocabPanel.classList.remove('hidden');
            } else {
                this.readingVocabPanel.classList.add('hidden');
            }
        }
    }

    resetReadingQuizState() {
        this.readingUserAnswers = {};
        this.readingQuizSubmitted = false;
        if (this.readingQuizScoreBanner) {
            this.readingQuizScoreBanner.classList.add('hidden');
        }
        if (this.readingRetryQuizBtn) {
            this.readingRetryQuizBtn.classList.add('hidden');
        }
        if (this.readingSubmitQuizBtn) {
            this.readingSubmitQuizBtn.classList.remove('hidden');
        }
    }

    retryReadingQuiz() {
        this.resetReadingQuizState();
        this.renderReadingQuizOnly();
        if (this.readingQuizCard) {
            this.readingQuizCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    renderCurrentReading() {
        const filtered = this.getFilteredReadings();
        if (!filtered || filtered.length === 0) {
            if (this.readingTitle) this.readingTitle.textContent = 'Không có bài đọc nào phù hợp.';
            if (this.readingBody) this.readingBody.innerHTML = '';
            return;
        }

        if (this.readingIndex >= filtered.length) {
            this.readingIndex = 0;
        }

        const current = filtered[this.readingIndex];

        // Metadata badges
        if (this.readingTypeBadge) {
            this.readingTypeBadge.textContent = current.type === 'conversation' ? '💬 Hội thoại' : '📰 Đoạn văn';
            this.readingTypeBadge.className = current.type === 'conversation' 
                ? 'px-2.5 py-1 rounded-full text-xs font-bold bg-indigo-100 text-indigo-700'
                : 'px-2.5 py-1 rounded-full text-xs font-bold bg-purple-100 text-purple-700';
        }
        if (this.readingLevelBadge) this.readingLevelBadge.textContent = current.level;
        if (this.readingTopicBadge) this.readingTopicBadge.textContent = current.topic;
        if (this.readingTitle) this.readingTitle.textContent = current.title;
        if (this.readingSummary) this.readingSummary.textContent = current.summary;

        // Key Vocab Panel
        if (this.readingVocabChips) {
            this.readingVocabChips.innerHTML = current.keyVocab.map((v, vIdx) => `
                <div class="bg-white p-2.5 sm:p-3 rounded-xl border border-amber-200/80 shadow-2xs flex items-center justify-between gap-2">
                    <div class="min-w-0 flex-1">
                        <div class="flex items-center gap-1.5 flex-wrap">
                            <span class="font-bold text-slate-900 text-xs sm:text-sm">${v.word}</span>
                            <span class="text-[11px] text-indigo-600 font-mono">${v.ipa}</span>
                        </div>
                        <div class="text-xs text-slate-600 mt-0.5 truncate">${v.meaning}</div>
                    </div>
                    <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-indigo-600 hover:bg-indigo-50 shrink-0 transition" title="Nghe phát âm" onclick="app.speakReadingVocab(${vIdx})">
                        🔊
                    </button>
                </div>
            `).join('');
        }

        this.renderReadingBodyOnly();
        this.renderReadingQuizOnly();
    }

    renderReadingBodyOnly() {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const current = filtered[this.readingIndex];

        if (current.type === 'conversation') {
            const transLines = (current.vietnameseTranslation || '')
                .split('\n')
                .map(l => l.trim())
                .filter(l => l.startsWith('- **') || l.startsWith('-'));

            let speakerNames = [];
            current.content.forEach(turn => {
                if (!speakerNames.includes(turn.speaker)) speakerNames.push(turn.speaker);
            });

            this.readingBody.innerHTML = current.content.map((turn, idx) => {
                const speakerLower = turn.speaker.toLowerCase();
                const isFemale = speakerLower.includes('female');
                const isMale = speakerLower.includes('male');

                let lineTrans = '';
                if (transLines[idx]) {
                    lineTrans = transLines[idx].replace(/^-\s*\*\*[^*]+\*\*:\s*/, '').replace(/^-\s*/, '');
                }

                const cardBg = isFemale ? 'bg-rose-50/40 border-rose-200/80' : 'bg-slate-50 border-slate-200/90';
                const avatarBg = isFemale 
                    ? 'bg-gradient-to-tr from-pink-500 to-rose-600 text-white shadow-xs' 
                    : 'bg-gradient-to-tr from-blue-600 to-indigo-600 text-white shadow-xs';
                const avatarIcon = isFemale ? '👩' : (isMale ? '👨' : '👤');
                const genderBadge = isFemale 
                    ? '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-100 text-rose-700">👩 Giọng Nữ</span>' 
                    : '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-700">👨 Giọng Nam</span>';
                const nameColor = isFemale ? 'text-rose-950 font-bold' : 'text-slate-900 font-bold';

                return `
                    <div class="flex items-start gap-2.5 sm:gap-3.5 p-3.5 sm:p-4 rounded-2xl border ${cardBg}">
                        <div class="w-8 h-8 sm:w-9 sm:h-9 shrink-0 rounded-xl ${avatarBg} flex items-center justify-center font-bold text-sm sm:text-base">
                            ${avatarIcon}
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="flex items-center justify-between gap-2 mb-1 flex-wrap">
                                <div class="flex items-center gap-1.5 flex-wrap">
                                    <span class="text-xs ${nameColor}">${turn.speaker}</span>
                                    ${genderBadge}
                                </div>
                                <div class="flex items-center gap-1">
                                    <button type="button" class="inline-flex items-center gap-1 text-xs text-slate-400 hover:text-indigo-600 p-1 rounded-lg hover:bg-white transition" title="Nghe giọng này" onclick="app.speakReadingLine(${idx})">
                                        <span>🔊</span>
                                    </button>
                                    <button type="button" class="inline-flex items-center gap-1 text-xs text-slate-400 hover:text-indigo-600 p-1 rounded-lg hover:bg-white transition" title="Luyện đọc câu này cùng AI" onclick="app.practiceDialogueLine(${idx})">
                                        <span>🎙️</span>
                                    </button>
                                </div>
                            </div>
                            <p class="text-xs sm:text-sm text-slate-800 leading-relaxed font-normal">${turn.text}</p>
                            ${this.showReadingTranslation && lineTrans ? `
                                <div class="mt-2 pt-2 border-t border-slate-200/70 text-xs sm:text-sm text-slate-600 italic leading-relaxed">
                                    <span class="font-semibold text-slate-500 not-italic mr-1">Dịch:</span>${lineTrans}
                                </div>
                            ` : ''}
                        </div>
                    </div>
                `;
            }).join('');
        } else {
            const paragraphs = current.content.split('\n\n').map(p => p.trim()).filter(Boolean);
            const transParas = (current.vietnameseTranslation || '')
                .replace(/\*\*Bản dịch tiếng Việt:\*\*\n?/g, '')
                .split('\n\n')
                .map(p => p.trim())
                .filter(Boolean);

            this.readingBody.innerHTML = paragraphs.map((para, idx) => {
                const paraTrans = transParas[idx] || '';

                return `
                    <div class="p-4 sm:p-5 rounded-2xl bg-slate-50/70 border border-slate-200/90 hover:border-indigo-200 transition">
                        <div class="flex items-center justify-between gap-2 mb-2 pb-1.5 border-b border-slate-200/50">
                            <span class="text-[11px] sm:text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded-full">Đoạn ${idx + 1}</span>
                            <div class="flex items-center gap-1">
                                <button type="button" class="inline-flex items-center gap-1 text-xs text-slate-500 hover:text-indigo-600 px-2 py-1 rounded-lg hover:bg-white transition" onclick="app.speakReadingParagraph(${idx})">
                                    <span>🔊</span> <span class="hidden sm:inline">Nghe đoạn</span>
                                </button>
                                <button type="button" class="inline-flex items-center gap-1 text-xs text-slate-500 hover:text-indigo-600 px-2 py-1 rounded-lg hover:bg-white transition" title="Luyện đọc câu này cùng AI" onclick="app.practiceReadingParagraph(${idx})">
                                    <span>🎙️</span> <span class="hidden sm:inline">Luyện đọc</span>
                                </button>
                            </div>
                        </div>
                        <p class="text-xs sm:text-sm sm:leading-relaxed text-slate-800 font-normal leading-relaxed">${para}</p>
                        ${this.showReadingTranslation && paraTrans ? `
                            <div class="mt-3 p-3 rounded-xl bg-indigo-50/50 border-l-4 border-indigo-400 text-xs sm:text-sm text-slate-600 italic leading-relaxed">
                                <span class="font-semibold text-indigo-700 not-italic block mb-0.5">Bản dịch tiếng Việt:</span>
                                ${paraTrans}
                            </div>
                        ` : ''}
                    </div>
                `;
            }).join('');
        }
    }

    renderReadingQuizOnly() {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const current = filtered[this.readingIndex];

        if (this.readingQuizBadgeCount) {
            this.readingQuizBadgeCount.textContent = `${current.questions.length} câu hỏi`;
        }

        if (!this.readingQuizContainer) return;

        this.readingQuizContainer.innerHTML = current.questions.map((q, qIdx) => {
            const userChoice = this.readingUserAnswers[q.id];
            const isCorrect = userChoice === q.answerIndex;

            let cardBorder = 'border-slate-200 bg-white';
            if (this.readingQuizSubmitted) {
                cardBorder = isCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-rose-300 bg-rose-50/20';
            }

            return `
                <div class="quiz-question-card p-4 sm:p-5 rounded-2xl border ${cardBorder} shadow-2xs transition" data-qid="${q.id}">
                    <div class="flex items-start justify-between gap-3 mb-3.5">
                        <h4 class="text-xs sm:text-sm font-bold text-slate-900 leading-snug">
                            <span class="text-indigo-600 font-extrabold mr-1">Câu ${qIdx + 1}:</span> ${q.question}
                        </h4>
                        ${this.readingQuizSubmitted ? (
                            isCorrect 
                                ? '<span class="shrink-0 px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">✓ Đúng</span>' 
                                : '<span class="shrink-0 px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-100 text-rose-800">✗ Sai</span>'
                        ) : ''}
                    </div>

                    <div class="space-y-2">
                        ${q.options.map((optText, optIdx) => {
                            const isSelected = userChoice === optIdx;
                            let optClass = 'border-slate-200 hover:bg-slate-50 hover:border-slate-300 text-slate-700';

                            if (this.readingQuizSubmitted) {
                                if (optIdx === q.answerIndex) {
                                    optClass = 'border-emerald-500 bg-emerald-50 text-emerald-900 font-semibold ring-1 ring-emerald-500';
                                } else if (isSelected && !isCorrect) {
                                    optClass = 'border-rose-400 bg-rose-50 text-rose-900 ring-1 ring-rose-400';
                                } else {
                                    optClass = 'border-slate-200 opacity-60 text-slate-500';
                                }
                            } else if (isSelected) {
                                optClass = 'border-indigo-600 bg-indigo-50/70 text-indigo-900 font-semibold ring-1 ring-indigo-500';
                            }

                            const disabledAttr = this.readingQuizSubmitted ? 'disabled' : '';

                            return `
                                <label class="flex items-start gap-3 p-3 rounded-xl border text-xs sm:text-sm cursor-pointer transition select-none ${optClass}">
                                    <input type="radio" 
                                           name="q_${q.id}" 
                                           value="${optIdx}" 
                                           class="mt-0.5 text-indigo-600 focus:ring-indigo-500 shrink-0" 
                                           ${isSelected ? 'checked' : ''} 
                                           ${disabledAttr}
                                           onchange="app.handleReadingQuizSelect('${q.id}', ${optIdx})">
                                    <span class="flex-1 min-w-0">${optText}</span>
                                </label>
                            `;
                        }).join('')}
                    </div>

                    ${this.readingQuizSubmitted ? `
                        <div class="mt-3.5 p-3 sm:p-4 rounded-xl bg-indigo-50 border border-indigo-100 text-xs sm:text-sm text-slate-700 leading-relaxed">
                            <div class="font-bold text-indigo-900 mb-1 flex items-center gap-1.5">
                                <span>💡</span> <span>Bằng chứng & Giải thích chi tiết:</span>
                            </div>
                            <p class="text-slate-700">${q.explanation}</p>
                        </div>
                    ` : ''}
                </div>
            `;
        }).join('');
    }

    handleReadingQuizSelect(qId, optionIdx) {
        if (this.readingQuizSubmitted) return;
        this.readingUserAnswers[qId] = optionIdx;
        this.renderReadingQuizOnly();
    }

    submitReadingQuiz() {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const current = filtered[this.readingIndex];

        const unanswered = current.questions.filter(q => typeof this.readingUserAnswers[q.id] === 'undefined');
        if (unanswered.length > 0) {
            if (!confirm(`Bạn còn ${unanswered.length} câu chưa chọn đáp án. Bạn có chắc chắn muốn nộp bài ngay không?`)) {
                return;
            }
        }

        this.readingQuizSubmitted = true;

        let correctCount = 0;
        current.questions.forEach(q => {
            if (this.readingUserAnswers[q.id] === q.answerIndex) {
                correctCount++;
            }
        });

        const total = current.questions.length;
        const percent = Math.round((correctCount / total) * 100);

        if (this.readingQuizScoreBanner) {
            this.readingQuizScoreBanner.classList.remove('hidden');
            let bannerBg = '';
            let message = '';

            if (percent === 100) {
                bannerBg = 'bg-emerald-100 border border-emerald-300 text-emerald-900';
                message = `🎉 <strong>Điểm số: ${correctCount}/${total} (100%)</strong> — Hoàn hảo! Bạn đã nắm trọn vẹn toàn bộ ý đồ và chi tiết bài đọc.`;
            } else if (percent >= 75) {
                bannerBg = 'bg-blue-100 border border-blue-300 text-blue-900';
                message = `⭐ <strong>Điểm số: ${correctCount}/${total} (${percent}%)</strong> — Rất tốt! Hãy đối chiếu phần giải thích cho câu chưa đúng nhé.`;
            } else {
                bannerBg = 'bg-amber-100 border border-amber-300 text-amber-900';
                message = `📖 <strong>Điểm số: ${correctCount}/${total} (${percent}%)</strong> — Hãy bật bản dịch tiếng Việt, đọc kỹ lại văn bản và xem phần giải thích bên dưới nhé.`;
            }

            this.readingQuizScoreBanner.className = `w-full sm:w-auto p-3 sm:px-5 sm:py-2.5 rounded-xl text-xs sm:text-sm font-medium flex items-center gap-2 ${bannerBg}`;
            this.readingQuizScoreBanner.innerHTML = message;
        }

        if (this.readingSubmitQuizBtn) this.readingSubmitQuizBtn.classList.add('hidden');
        if (this.readingRetryQuizBtn) this.readingRetryQuizBtn.classList.remove('hidden');

        this.renderReadingQuizOnly();
    }

    speakReadingVocab(idx) {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const vocab = filtered[this.readingIndex].keyVocab[idx];
        if (vocab) {
            this.speak(vocab.word, 0.85);
        }
    }

    speakReadingLine(idx) {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const turn = filtered[this.readingIndex].content[idx];
        const speechRate = parseFloat(this.readingSpeechRate ? this.readingSpeechRate.value : 1.0) || 1.0;
        if (turn) {
            const voiceConfig = this.getVoiceForSpeaker(turn.speaker);
            this.speak(turn.text, speechRate, voiceConfig);
        }
    }

    speakReadingParagraph(idx) {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const paragraphs = filtered[this.readingIndex].content.split('\n\n').map(p => p.trim()).filter(Boolean);
        const speechRate = parseFloat(this.readingSpeechRate ? this.readingSpeechRate.value : 1.0) || 1.0;
        if (paragraphs[idx]) {
            this.speak(paragraphs[idx], speechRate);
        }
    }

    toggleReadingTTS() {
        if (!('speechSynthesis' in window)) {
            alert('Trình duyệt của bạn không hỗ trợ tính năng phát âm trực tiếp.');
            return;
        }

        if (this.isReadingSpeaking) {
            this.stopReadingTTS();
            return;
        }

        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const current = filtered[this.readingIndex];
        const speechRate = parseFloat(this.readingSpeechRate ? this.readingSpeechRate.value : 1.0) || 1.0;

        window.speechSynthesis.cancel();
        this.isReadingSpeaking = true;
        if (this.readingTtsIcon) this.readingTtsIcon.textContent = '⏹';
        if (this.readingTtsText) this.readingTtsText.textContent = 'Dừng đọc';
        if (this.readingTtsBtn) {
            this.readingTtsBtn.className = 'inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-rose-600 text-white transition active:scale-95 shadow-xs font-semibold text-xs';
        }

        if (current.type === 'conversation') {
            // Đọc đối thoại tự động chuyển đổi giữa giọng Nam và giọng Nữ
            const totalTurns = current.content.length;
            current.content.forEach((turn, idx) => {
                const utterance = new SpeechSynthesisUtterance(turn.text);
                utterance.lang = 'en-US';
                utterance.rate = speechRate;

                const voiceConfig = this.getVoiceForSpeaker(turn.speaker);
                if (voiceConfig.voice) utterance.voice = voiceConfig.voice;
                if (voiceConfig.pitch) utterance.pitch = voiceConfig.pitch;

                if (idx === totalTurns - 1) {
                    utterance.onend = () => this.stopReadingTTS();
                    utterance.onerror = () => this.stopReadingTTS();
                }

                window.speechSynthesis.speak(utterance);
            });
        } else {
            // Đọc bài văn học thuật
            const utterance = new SpeechSynthesisUtterance(current.content);
            utterance.lang = 'en-US';
            utterance.rate = speechRate;

            const voiceConfig = this.getVoiceForSpeaker();
            if (voiceConfig.voice) utterance.voice = voiceConfig.voice;

            utterance.onend = () => this.stopReadingTTS();
            utterance.onerror = () => this.stopReadingTTS();

            window.speechSynthesis.speak(utterance);
        }
    }

    stopReadingTTS() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }
        this.isReadingSpeaking = false;
        if (this.readingTtsIcon) this.readingTtsIcon.textContent = '🔊';
        if (this.readingTtsText) this.readingTtsText.textContent = 'Nghe đọc toàn bài';
        if (this.readingTtsBtn) {
            this.readingTtsBtn.className = 'inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-indigo-50 hover:bg-indigo-100 text-indigo-700 transition active:scale-95 text-xs font-semibold';
        }
    }

    // ================= EXPORT / IMPORT =================
    exportData() {
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.items, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute("href", dataStr);
        downloadAnchor.setAttribute("download", `tieng_anh_data_${new Date().toISOString().split('T')[0]}.json`);
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
    }

    importData(event) {
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const imported = JSON.parse(e.target.result);
                if (Array.isArray(imported)) {
                    if (confirm(`Tìm thấy ${imported.length} mục. Bạn có muốn nhập thêm vào danh sách hiện tại không?`)) {
                        // Trộn dữ liệu không trùng id
                        const existingIds = new Set(this.items.map(i => i.id));
                        imported.forEach(item => {
                            if (!existingIds.has(item.id)) {
                                this.items.push(item);
                            }
                        });
                        this.saveItems();
                        this.refreshAll();
                        alert("Nhập dữ liệu thành công!");
                    }
                } else {
                    alert("Tệp JSON không đúng định dạng danh sách.");
                }
            } catch (err) {
                alert("Lỗi khi đọc tệp JSON: " + err.message);
            }
        };
        reader.readAsText(file);
    }

    resetData() {
        if (confirm("Bạn có chắc muốn khôi phục danh sách từ vựng về mặc định ban đầu không? (Những từ bạn tự thêm sẽ bị xóa)")) {
            this.items = [...INITIAL_DATA];
            this.saveItems();
            this.refreshAll();
            alert("Đã khôi phục dữ liệu ban đầu!");
        }
    }

    // ================= FLASHCARD PRONUNCIATION METHODS =================
    toggleFlashcardSpeechBox() {
        if (!this.fcSpeechBox) return;
        const isHidden = this.fcSpeechBox.classList.contains('hidden');
        if (isHidden) {
            this.fcSpeechBox.classList.remove('hidden');
            if (this.fcSpeechResultBox) this.fcSpeechResultBox.classList.add('hidden');
            if (this.fcSpeechInterimBox) this.fcSpeechInterimBox.classList.add('hidden');
            if (this.fcSpeechStatusText) this.fcSpeechStatusText.textContent = 'Sẵn sàng. Chạm "Nói ngay" để bắt đầu.';
            this.toggleFlashcardRecording();
        } else {
            this.closeFlashcardSpeechBox();
        }
    }

    closeFlashcardSpeechBox() {
        if (!this.fcSpeechBox) return;
        this.fcSpeechBox.classList.add('hidden');
        if (this.fcIsRecording) {
            this.speechManager.stop();
            this.fcIsRecording = false;
        }
    }

    toggleFlashcardRecording() {
        if (this.flashcardList.length === 0) return;
        const currentItem = this.flashcardList[this.flashcardIndex];
        const targetText = currentItem.text;

        if (this.fcIsRecording) {
            this.speechManager.stop();
            this.fcIsRecording = false;
            if (this.fcSpeechRecText) this.fcSpeechRecText.textContent = 'Nói ngay';
            if (this.fcSpeechMicDot) this.fcSpeechMicDot.className = 'w-3 h-3 rounded-full bg-slate-300 shrink-0';
            return;
        }

        this.fcIsRecording = true;
        if (this.fcSpeechRecText) this.fcSpeechRecText.textContent = 'Dừng';
        if (this.fcSpeechMicDot) this.fcSpeechMicDot.className = 'w-3 h-3 rounded-full bg-rose-500 animate-ping shrink-0';
        if (this.fcSpeechStatusText) this.fcSpeechStatusText.textContent = '🔴 Đang nghe... Hãy nói to: "' + targetText + '"';
        if (this.fcSpeechInterimBox) this.fcSpeechInterimBox.classList.remove('hidden');
        if (this.fcSpeechInterimText) this.fcSpeechInterimText.textContent = '...';

        this.speechManager.start({
            lang: 'en-US',
            onStart: () => {
                if (this.fcSpeechStatusText) this.fcSpeechStatusText.textContent = '🔴 Đang nghe... Hãy đọc to: "' + targetText + '"';
            },
            onInterim: (interim) => {
                if (this.fcSpeechInterimText) this.fcSpeechInterimText.textContent = interim;
            },
            onResult: (spoken) => {
                this.evaluateFlashcardPronunciation(spoken);
            },
            onError: (err) => {
                if (this.fcSpeechStatusText) this.fcSpeechStatusText.textContent = '⚠️ ' + err.message;
                if (this.fcSpeechInterimBox) this.fcSpeechInterimBox.classList.add('hidden');
            },
            onEnd: () => {
                this.fcIsRecording = false;
                if (this.fcSpeechRecText) this.fcSpeechRecText.textContent = 'Nói ngay';
                if (this.fcSpeechMicDot) this.fcSpeechMicDot.className = 'w-3 h-3 rounded-full bg-slate-300 shrink-0';
            }
        });
    }

    evaluateFlashcardPronunciation(spokenText) {
        if (this.flashcardList.length === 0) return;
        const targetText = this.flashcardList[this.flashcardIndex].text;
        const evalResult = this.evaluator.evaluate(targetText, spokenText);

        if (this.fcSpeechInterimBox) this.fcSpeechInterimBox.classList.add('hidden');
        if (this.fcSpeechResultBox) this.fcSpeechResultBox.classList.remove('hidden');

        if (this.fcSpeechScore) {
            this.fcSpeechScore.textContent = `${evalResult.overallScore}%`;
            this.fcSpeechScore.className = `text-2xl font-black ${evalResult.scoreColorClass}`;
        }
        if (this.fcSpeechVerdict) {
            this.fcSpeechVerdict.textContent = evalResult.verdict;
            this.fcSpeechVerdict.className = `text-xs font-bold px-2.5 py-1 rounded-full ${evalResult.badgeClass}`;
        }
        if (this.fcSpeechSpoken) {
            this.fcSpeechSpoken.textContent = spokenText ? `"${spokenText}"` : '(Không nghe thấy)';
        }
        if (this.fcSpeechStatusText) {
            this.fcSpeechStatusText.textContent = `Đã chấm điểm: ${evalResult.overallScore}% - ${evalResult.verdict}`;
        }

        this.renderFlashcardTokens(evalResult.tokens);
    }

    renderFlashcardTokens(tokens) {
        if (!this.fcSpeechTokens) return;
        if (!tokens || tokens.length === 0) {
            this.fcSpeechTokens.innerHTML = '';
            return;
        }

        const colorClasses = {
            correct: 'bg-emerald-50 text-emerald-800 border-emerald-300 hover:bg-emerald-100',
            close: 'bg-amber-50 text-amber-800 border-amber-300 hover:bg-amber-100',
            missed: 'bg-rose-50 text-rose-800 border-rose-300 hover:bg-rose-100'
        };

        this.fcSpeechTokens.innerHTML = tokens.map(t => {
            const icon = t.status === 'correct' ? '✓' : (t.status === 'close' ? '⚠️' : '✗');
            const scoreLabel = t.status === 'missed' ? '0%' : `${t.score}%`;
            const cleanEscaped = t.clean.replace(/'/g, "\\'");
            return `
                <button type="button"
                        class="inline-flex items-center gap-1 px-2.5 py-1 rounded-xl border text-xs font-semibold transition cursor-pointer active:scale-95 ${colorClasses[t.status]}"
                        title="Nghe lại âm chuẩn từ: ${t.clean}"
                        onclick="app.speak('${cleanEscaped}', 0.8)">
                    <span>${icon}</span>
                    <span>${t.raw}</span>
                    <span class="text-[10px] opacity-75 font-mono">(${scoreLabel})</span>
                    <span class="text-[10px]">🔊</span>
                </button>
            `;
        }).join('');
    }

    // ================= SPEAKING LAB METHODS =================
    initSpeakingLab() {
        this.updateSpeakingModeButtons();
        this.updateSpeakingTopicDropdown();
        this.renderSpeakingLab();
    }

    setSpeakingMode(mode) {
        if (this.spMode === mode) return;
        this.spMode = mode;
        this.spIndex = 0;
        this.updateSpeakingModeButtons();
        this.updateSpeakingTopicDropdown();
        this.renderSpeakingLab();
    }

    updateSpeakingModeButtons() {
        if (!this.spModeBtns) return;
        this.spModeBtns.forEach(btn => {
            if (btn.dataset.mode === this.spMode) {
                btn.className = 'sp-mode-btn active px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-indigo-600 text-white transition shadow-xs';
            } else {
                btn.className = 'sp-mode-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200 transition';
            }
        });
    }

    updateSpeakingTopicDropdown() {
        if (!this.spTopicSelect) return;
        let topics = [];
        if (this.spMode === 'words') {
            topics = Array.from(new Set(this.items.filter(i => i.type === 'vocab').map(i => i.topic))).filter(Boolean);
        } else if (this.spMode === 'sentences') {
            topics = Array.from(new Set(this.items.filter(i => i.type === 'sentence').map(i => i.topic))).filter(Boolean);
        } else if (this.spMode === 'dialogues') {
            if (window.READING_DATA && Array.isArray(window.READING_DATA)) {
                topics = Array.from(new Set(window.READING_DATA.filter(r => r.type === 'conversation').map(r => r.topic))).filter(Boolean);
            }
        }

        let html = '<option value="all">Tất cả chủ đề</option>';
        topics.forEach(t => {
            html += `<option value="${t}" ${this.spTopic === t ? 'selected' : ''}>${t}</option>`;
        });
        this.spTopicSelect.innerHTML = html;
    }

    getSpeakingItems() {
        if (this.spMode === 'words') {
            const list = this.items.filter(i => i.type === 'vocab');
            return this.spTopic === 'all' ? list : list.filter(i => i.topic === this.spTopic);
        } else if (this.spMode === 'sentences') {
            const list = this.items.filter(i => i.type === 'sentence');
            return this.spTopic === 'all' ? list : list.filter(i => i.topic === this.spTopic);
        } else if (this.spMode === 'dialogues') {
            const list = [];
            if (window.READING_DATA && Array.isArray(window.READING_DATA)) {
                window.READING_DATA.forEach(r => {
                    if (r.type === 'conversation' && Array.isArray(r.content)) {
                        r.content.forEach((turn, idx) => {
                            list.push({
                                id: `dial_${r.id}_${idx}`,
                                text: turn.text,
                                ipa: '',
                                meaning: `[${turn.speaker}] ${r.title}`,
                                example: turn.vietnamese || '',
                                topic: r.topic || 'Hội thoại',
                                type: 'dialogue'
                            });
                        });
                    }
                });
            }
            return this.spTopic === 'all' ? list : list.filter(i => i.topic === this.spTopic);
        }
        return this.items;
    }

    renderSpeakingLab() {
        const items = this.getSpeakingItems();
        if (!items || items.length === 0) {
            if (this.spTargetText) this.spTargetText.textContent = 'Chưa có dữ liệu';
            if (this.spTargetIpa) this.spTargetIpa.textContent = '';
            if (this.spTargetMeaning) this.spTargetMeaning.textContent = 'Hãy chọn chủ đề hoặc chế độ khác.';
            if (this.spProgressText) this.spProgressText.textContent = '0 / 0';
            return;
        }

        if (this.spIndex >= items.length) {
            this.spIndex = 0;
        }

        const current = items[this.spIndex];

        if (this.spTargetBadge) {
            this.spTargetBadge.textContent = this.spMode === 'words' ? 'Từ vựng' : (this.spMode === 'sentences' ? 'Mẫu câu' : 'Hội thoại');
        }
        if (this.spTargetTopic) {
            this.spTargetTopic.textContent = current.topic || 'Chung';
        }
        if (this.spProgressText) {
            this.spProgressText.textContent = `Mục ${this.spIndex + 1} / ${items.length}`;
        }
        if (this.spTargetText) {
            this.spTargetText.textContent = current.text;
        }
        if (this.spTargetIpa) {
            this.spTargetIpa.textContent = current.ipa || '';
            this.spTargetIpa.classList.toggle('hidden', !current.ipa);
        }
        if (this.spTargetMeaning) {
            this.spTargetMeaning.textContent = current.meaning;
        }
        if (this.spTargetExampleBox && this.spTargetExample) {
            if (current.example) {
                this.spTargetExampleBox.classList.remove('hidden');
                this.spTargetExample.textContent = `"${current.example}"`;
            } else {
                this.spTargetExampleBox.classList.add('hidden');
            }
        }

        // Reset recognition & result card when changing phrase
        if (this.spResultCard) this.spResultCard.classList.add('hidden');
        if (this.spInterimBox) this.spInterimBox.classList.add('hidden');
        if (this.spStatusText) this.spStatusText.textContent = 'Chạm vào nút micro để bắt đầu nói tiếng Anh';
        this.stopSpeakingLabRecording();
    }

    prevSpeakingItem() {
        const items = this.getSpeakingItems();
        if (!items || items.length <= 1) return;
        this.spIndex = (this.spIndex - 1 + items.length) % items.length;
        this.renderSpeakingLab();
    }

    nextSpeakingItem() {
        const items = this.getSpeakingItems();
        if (!items || items.length <= 1) return;
        this.spIndex = (this.spIndex + 1) % items.length;
        this.renderSpeakingLab();
    }

    randomSpeakingItem() {
        const items = this.getSpeakingItems();
        if (!items || items.length <= 1) return;
        let nextIdx = Math.floor(Math.random() * items.length);
        if (nextIdx === this.spIndex && items.length > 1) {
            nextIdx = (nextIdx + 1) % items.length;
        }
        this.spIndex = nextIdx;
        this.renderSpeakingLab();
    }

    listenCurrentSpeakingTarget(rate = 1.0) {
        const items = this.getSpeakingItems();
        if (!items || !items[this.spIndex]) return;
        this.speak(items[this.spIndex].text, rate);
    }

    toggleSpeakingLabRecording() {
        const items = this.getSpeakingItems();
        if (!items || !items[this.spIndex]) return;
        const targetText = items[this.spIndex].text;

        if (this.spIsRecording) {
            this.speechManager.stop();
            this.spIsRecording = false;
            this.updateSpeakingRecordUI(false);
            return;
        }

        this.spIsRecording = true;
        this.updateSpeakingRecordUI(true);

        if (this.spStatusText) {
            this.spStatusText.textContent = '🔴 Đang nghe... Hãy nói to: "' + targetText + '"';
        }
        if (this.spInterimBox) {
            this.spInterimBox.classList.remove('hidden');
        }
        if (this.spInterimText) {
            this.spInterimText.textContent = '...';
        }

        this.speechManager.start({
            lang: 'en-US',
            onStart: () => {
                this.updateSpeakingRecordUI(true);
            },
            onInterim: (interim) => {
                if (this.spInterimText) this.spInterimText.textContent = interim;
            },
            onResult: (spoken) => {
                this.evaluateSpeakingInput(spoken);
            },
            onError: (err) => {
                if (this.spStatusText) this.spStatusText.textContent = '⚠️ ' + err.message;
                if (this.spInterimBox) this.spInterimBox.classList.add('hidden');
                this.updateSpeakingRecordUI(false);
            },
            onEnd: () => {
                this.spIsRecording = false;
                this.updateSpeakingRecordUI(false);
            }
        });
    }

    stopSpeakingLabRecording() {
        if (this.spIsRecording) {
            this.speechManager.stop();
            this.spIsRecording = false;
            this.updateSpeakingRecordUI(false);
        }
    }

    updateSpeakingRecordUI(isRecording) {
        if (this.spPulseRing) {
            this.spPulseRing.classList.toggle('hidden', !isRecording);
        }
        if (this.spWaveBars) {
            this.spWaveBars.classList.toggle('hidden', !isRecording);
        }
        if (this.spRecordBtn) {
            if (isRecording) {
                this.spRecordBtn.className = 'relative z-10 w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-rose-600 hover:bg-rose-700 text-white shadow-xl shadow-rose-200 flex flex-col items-center justify-center transition active:scale-90 focus:outline-none';
            } else {
                this.spRecordBtn.className = 'relative z-10 w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-indigo-600 hover:bg-indigo-700 text-white shadow-xl shadow-indigo-200 flex flex-col items-center justify-center transition active:scale-90 focus:outline-none';
            }
        }
        if (this.spRecordIcon) {
            this.spRecordIcon.textContent = isRecording ? '⏹️' : '🎙️';
        }
        if (this.spRecordSub) {
            this.spRecordSub.textContent = isRecording ? 'Dừng' : 'Nói ngay';
        }
    }

    evaluateSpeakingInput(spokenText) {
        const items = this.getSpeakingItems();
        if (!items || !items[this.spIndex]) return;
        const targetText = items[this.spIndex].text;

        const evalResult = this.evaluator.evaluate(targetText, spokenText);
        this.renderSpeakingAssessment(evalResult);
    }

    renderSpeakingAssessment(evalResult) {
        if (this.spInterimBox) this.spInterimBox.classList.add('hidden');
        if (!this.spResultCard) return;

        this.spResultCard.classList.remove('hidden');

        if (this.spResultScore) {
            this.spResultScore.textContent = `${evalResult.overallScore}%`;
            this.spResultScore.className = `text-4xl sm:text-5xl font-black ${evalResult.scoreColorClass}`;
        }
        if (this.spResultBadge) {
            this.spResultBadge.textContent = evalResult.verdict;
            this.spResultBadge.className = `inline-block mt-2 px-3 py-1 rounded-full text-xs font-bold ${evalResult.badgeClass}`;
        }
        if (this.spResultFeedback) {
            this.spResultFeedback.textContent = evalResult.feedback;
        }
        if (this.spCompTarget) {
            this.spCompTarget.textContent = evalResult.targetText;
        }
        if (this.spCompSpoken) {
            this.spCompSpoken.textContent = evalResult.spokenText ? `"${evalResult.spokenText}"` : '(Không thu được âm thanh)';
        }
        if (this.spStatusText) {
            this.spStatusText.textContent = `Hoàn thành đánh giá: ${evalResult.overallScore}% - ${evalResult.verdict}`;
        }

        this.renderSpeakingTokens(evalResult.tokens);

        // Smooth scroll into result card
        this.spResultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    renderSpeakingTokens(tokens) {
        if (!this.spTokensContainer) return;
        if (!tokens || tokens.length === 0) {
            this.spTokensContainer.innerHTML = '<span class="text-xs text-slate-400">Không có dữ liệu từ.</span>';
            return;
        }

        const colorClasses = {
            correct: 'bg-emerald-100 text-emerald-900 border-emerald-300 hover:bg-emerald-200',
            close: 'bg-amber-100 text-amber-900 border-amber-300 hover:bg-amber-200',
            missed: 'bg-rose-100 text-rose-900 border-rose-300 hover:bg-rose-200'
        };

        this.spTokensContainer.innerHTML = tokens.map(t => {
            const icon = t.status === 'correct' ? '✓' : (t.status === 'close' ? '⚠️' : '✗');
            const scoreLabel = t.status === 'missed' ? 'Chưa đạt' : `${t.score}%`;
            const tip = t.spoken && t.spoken !== t.clean ? ` (Bạn nói: "${t.spoken}")` : '';
            const cleanEscaped = t.clean.replace(/'/g, "\\'");

            return `
                <button type="button"
                        class="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl border text-xs sm:text-sm font-semibold transition cursor-pointer active:scale-95 shadow-2xs ${colorClasses[t.status]}"
                        title="Bấm để nghe âm chuẩn từ này${tip}"
                        onclick="app.speak('${cleanEscaped}', 0.8)">
                    <span>${icon}</span>
                    <span>${t.raw}</span>
                    <span class="text-[11px] opacity-75 font-mono">(${scoreLabel})</span>
                    <span class="text-xs ml-0.5">🔊</span>
                </button>
            `;
        }).join('');
    }

    // ================= READING PRACTICE INTEGRATION =================
    practiceDialogueLine(turnIdx) {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const item = filtered[this.readingIndex];
        if (item.type !== 'conversation' || !item.content[turnIdx]) return;
        const turn = item.content[turnIdx];

        this.spMode = 'dialogues';
        this.updateSpeakingModeButtons();
        this.spTopic = 'all';
        this.updateSpeakingTopicDropdown();

        const items = this.getSpeakingItems();
        const foundIdx = items.findIndex(i => i.text === turn.text);
        if (foundIdx !== -1) {
            this.spIndex = foundIdx;
        } else {
            items.unshift({
                id: `dial_jump_${Date.now()}`,
                text: turn.text,
                ipa: '',
                meaning: `[${turn.speaker}] ${item.title}`,
                example: turn.vietnamese || '',
                topic: item.topic || 'Hội thoại',
                type: 'dialogue'
            });
            this.spIndex = 0;
        }

        this.switchTab('speaking');
        this.renderSpeakingLab();

        const targetEl = document.getElementById('sp-target-text');
        if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    practiceReadingParagraph(paraIdx) {
        const filtered = this.getFilteredReadings();
        if (!filtered || !filtered[this.readingIndex]) return;
        const item = filtered[this.readingIndex];
        const paras = item.content.split('\n\n').map(p => p.trim()).filter(Boolean);
        const paraText = paras[paraIdx];
        if (!paraText) return;

        // Choose first sentence of the paragraph for comfortable pronunciation practice
        const firstSentence = paraText.split(/(?<=[.?!])\s+/)[0] || paraText;

        this.spMode = 'sentences';
        this.updateSpeakingModeButtons();
        this.spTopic = 'all';
        this.updateSpeakingTopicDropdown();

        const items = this.getSpeakingItems();
        items.unshift({
            id: `para_jump_${Date.now()}`,
            text: firstSentence,
            ipa: '',
            meaning: `Trích từ: ${item.title}`,
            example: paraText,
            topic: item.topic || 'Bài đọc',
            type: 'sentence'
        });
        this.spIndex = 0;

        this.switchTab('speaking');
        this.renderSpeakingLab();

        const targetEl = document.getElementById('sp-target-text');
        if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

// Global instance
let app;
window.addEventListener('DOMContentLoaded', () => {
    app = new EnglishApp();
});
