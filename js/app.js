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

        // Quiz State
        this.quizQuestions = [];
        this.quizIndex = 0;
        this.quizScore = 0;
        this.isQuizActive = false;

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
        }
    }

    refreshAll() {
        this.updateTopicDropdowns();
        this.refreshStats();
        this.updateFlashcardList();
        this.renderLibrary();
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
    speak(text, rate = 0.85) {
        if (!('speechSynthesis' in window)) {
            alert('Trình duyệt của bạn không hỗ trợ tính năng phát âm trực tiếp.');
            return;
        }

        window.speechSynthesis.cancel(); // Dừng câu đang phát trước đó
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = rate; // 0.7 cho người mới, 1.0 tốc độ bình thường

        // Cố gắng chọn voice chuẩn tiếng Anh nếu có
        const voices = window.speechSynthesis.getVoices();
        const englishVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha')));
        if (englishVoice) {
            utterance.voice = englishVoice;
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
}

// Global instance
let app;
window.addEventListener('DOMContentLoaded', () => {
    app = new EnglishApp();
});
