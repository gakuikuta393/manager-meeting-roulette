import re

# ファイルを読み込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修正1: 897行目の余分な閉じ括弧を削除
# DepartmentManagerクラスの最後の余分な閉じ括弧を削除
content = re.sub(
    r'(                confirmBtn\.addEventListener\(\'click\', handleConfirm\);\r?\n                cancelBtn\.addEventListener\(\'click\', handleCancel\);\r?\n            }\r?\n        })\r?\n        }',
    r'\1',
    content
)

# 修正2: AnimationControllerクラスのspin()メソッドにanimate()呼び出しを追加
content = re.sub(
    r'(                return new Promise\(\(resolve\) => \{\r?\n                    const animate = \(\) => \{\r?\n                        const elapsed = Date\.now\(\) - startTime;\r?\n                        const progress = Math\.min\(elapsed / duration, 1\);\r?\n\r?\n                        // イージング関数（cubic-bezier）\r?\n                        const easeOut = 1 - Math\.pow\(1 - progress, 3\);\r?\n                        const currentRotation = finalRotation \* easeOut;\r?\n\r?\n                        this\.renderer\.draw\(currentRotation\);\r?\n\r?\n                        if \(progress < 1\) \{\r?\n                            requestAnimationFrame\(animate\);\r?\n                        } else \{\r?\n                            this\.isAnimating = false;\r?\n                            resolve\(\);\r?\n                        }\r?\n                    };\r?\n\r?\n                )\}\);',
    r'\1\n                    animate();\n                });',
    content
)

# 修正3: 不適切なイベントリスナーコードを削除（1116-1140行目付近）
# spin()メソッドの後に誤って配置されているイベントリスナーを削除
content = re.sub(
    r'\n\n                // 部門追加\r?\n                document\.getElementById\(\'addButton\'\)\.addEventListener\(\'click\', \(\) => \{\r?\n                    this\.addDepartment\(\);\r?\n                \}\);\r?\n\r?\n                document\.getElementById\(\'departmentInput\'\)\.addEventListener\(\'keypress\', \(e\) => \{\r?\n                \}\);\r?\n\r?\n                // 履歴変更（前々回）\r?\n                document\.getElementById\(\'secondLastResultSelect\'\)\.addEventListener\(\'change\', \(e\) => \{\r?\n                    this\.storage\.updateHistory\(1, e\.target\.value\);\r?\n                    this\.updateUI\(\);\r?\n                \}\);\r?\n\r?\n                // 結果モーダルを閉じる\r?\n                document\.getElementById\(\'closeResultButton\'\)\.addEventListener\(\'click\', \(\) => \{\r?\n                    document\.getElementById\(\'resultModal\'\)\.classList\.remove\(\'show\'\);\r?\n                \}\);\r?\n\r?\n                // ウィンドウリサイズ\r?\n                window\.addEventListener\(\'resize\', \(\) => \{\r?\n                    this\.renderer\.setupCanvas\(\);\r?\n                    this\.updateUI\(\);\r?\n                \}\);\r?\n            }',
    '',
    content
)

# 修正4: RouletteAppクラスを追加（AnimationControllerクラスの後）
roulette_app_class = '''
        // ========== Roulette App ==========
        class RouletteApp {
            constructor() {
                this.showError = this.showError.bind(this);
                this.storage = new StorageManager(this.showError);
                this.departmentManager = new DepartmentManager(this.storage, () => this.updateUI());
                this.lotteryEngine = new LotteryEngine(this.storage);
                
                const canvas = document.getElementById('rouletteCanvas');
                const departments = this.departmentManager.getDepartments();
                const eligible = this.lotteryEngine.getEligibleDepartments();
                const excludedDepts = departments.filter(dept => !eligible.includes(dept));
                
                this.renderer = new RouletteRenderer(canvas, departments, excludedDepts);
                this.animation = new AnimationController(this.renderer);
                
                this.setupEventListeners();
                this.updateUI();
            }

            showError(message) {
                const toast = document.getElementById('errorToast');
                toast.textContent = message;
                toast.style.display = 'block';
                setTimeout(() => {
                    toast.style.opacity = '0';
                    setTimeout(() => {
                        toast.style.display = 'none';
                        toast.style.opacity = '1';
                    }, 300);
                }, 3000);
            }

            setupEventListeners() {
                // ルーレット開始
                document.getElementById('centerStartButton').addEventListener('click', () => {
                    this.startLottery();
                });

                // 部門追加
                document.getElementById('addButton').addEventListener('click', () => {
                    this.addDepartment();
                });

                document.getElementById('departmentInput').addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        this.addDepartment();
                    }
                });

                // 履歴変更（前回）
                document.getElementById('lastResultSelect').addEventListener('change', (e) => {
                    this.storage.updateHistory(0, e.target.value);
                    this.updateUI();
                });

                // 履歴変更（前々回）
                document.getElementById('secondLastResultSelect').addEventListener('change', (e) => {
                    this.storage.updateHistory(1, e.target.value);
                    this.updateUI();
                });

                // 履歴リセット
                document.getElementById('resetHistoryButton').addEventListener('click', () => {
                    const modal = document.getElementById('historyResetModal');
                    modal.classList.add('show');
                });

                document.getElementById('confirmResetButton').addEventListener('click', () => {
                    this.storage.resetHistory();
                    this.updateUI();
                    document.getElementById('historyResetModal').classList.remove('show');
                });

                document.getElementById('cancelResetButton').addEventListener('click', () => {
                    document.getElementById('historyResetModal').classList.remove('show');
                });

                // 結果モーダルを閉じる
                document.getElementById('closeResultButton').addEventListener('click', () => {
                    document.getElementById('resultModal').classList.remove('show');
                });

                // ウィンドウリサイズ
                window.addEventListener('resize', () => {
                    this.renderer.setupCanvas();
                    this.updateUI();
                });
            }

            addDepartment() {
                const input = document.getElementById('departmentInput');
                const name = input.value;

                if (this.departmentManager.addDepartment(name)) {
                    input.value = '';
                }
            }

            async startLottery() {
                const departments = this.departmentManager.getDepartments();

                if (departments.length === 0) {
                    alert('部門を登録してください');
                    return;
                }

                const eligible = this.lotteryEngine.getEligibleDepartments();

                if (eligible.length === 0) {
                    alert('抽選可能な部門がありません');
                    return;
                }

                // ボタンを無効化
                const centerButton = document.getElementById('centerStartButton');
                centerButton.classList.add('disabled');
                centerButton.textContent = '回転中...';

                // 抽選実行
                const selected = this.lotteryEngine.performLottery();

                // アニメーション
                await this.animation.spin(selected, departments);

                // 結果表示
                document.getElementById('resultDepartment').textContent = selected;
                document.getElementById('resultModal').classList.add('show');

                // UI更新
                this.updateUI();

                // ボタンを有効化
                centerButton.classList.remove('disabled');
                centerButton.textContent = 'START';
            }

            updateUI() {
                const departments = this.departmentManager.getDepartments();
                const history = this.lotteryEngine.getHistory();
                const eligible = this.lotteryEngine.getEligibleDepartments();
                const excludedDepts = departments.filter(dept => !eligible.includes(dept));

                // ルーレット更新
                this.renderer.updateDepartments(departments, excludedDepts);

                // 履歴表示更新
                this.updateHistorySelects(departments, history);

                // 部門リスト更新
                this.renderDepartmentsList(departments, excludedDepts);
            }

            updateHistorySelects(departments, history) {
                const lastSelect = document.getElementById('lastResultSelect');
                const secondLastSelect = document.getElementById('secondLastResultSelect');

                const createOptions = (selectedValue) => {
                    let html = '<option value="">なし</option>';
                    departments.forEach(dept => {
                        const isSelected = dept === selectedValue;
                        html += `<option value="${dept}" ${isSelected ? 'selected' : ''}>${dept}</option>`;
                    });
                    return html;
                };

                lastSelect.innerHTML = createOptions(history[0]);
                secondLastSelect.innerHTML = createOptions(history[1]);
                
                // 明示的に値を設定（ブラウザの表示状態を確実に更新）
                lastSelect.value = history[0] || '';
                secondLastSelect.value = history[1] || '';
            }

            renderDepartmentsList(departments, excludedDepts) {
                const listContainer = document.getElementById('departmentsList');

                if (departments.length === 0) {
                    listContainer.innerHTML = `
                        <div class="empty-state">
                            <div class="empty-state-icon">📋</div>
                            <div>部門が登録されていません</div>
                        </div>
                    `;
                    return;
                }

                listContainer.innerHTML = departments.map((dept, index) => {
                    const isExcluded = excludedDepts.includes(dept);
                    const escapedDept = dept.replace(/'/g, "\\\\'");
                    return `
                        <div class="department-item ${isExcluded ? 'excluded' : ''}" id="dept-item-${index}">
                            <span class="department-name" id="dept-name-${index}">${dept}</span>
                            ${isExcluded ? '<span class="excluded-badge">除外中</span>' : ''}
                            <button class="edit-button" onclick="app.startEditDepartment(${index}, '${escapedDept}')">編集</button>
                            <button class="delete-button" onclick="app.departmentManager.deleteDepartment('${escapedDept}')">削除</button>
                        </div>
                    `;
                }).join('');
            }

            startEditDepartment(index, oldName) {
                const itemEl = document.getElementById(`dept-item-${index}`);
                
                const currentName = oldName;
                
                itemEl.innerHTML = `
                    <input type="text" class="department-edit-input" id="edit-input-${index}" value="${currentName}" maxlength="50" />
                    <button class="save-button" id="save-btn-${index}">保存</button>
                    <button class="cancel-button" onclick="app.cancelEditDepartment()">キャンセル</button>
                `;
                
                const input = document.getElementById(`edit-input-${index}`);
                input.focus();
                input.select();
                
                // 保存ボタンのイベントリスナー設定
                document.getElementById(`save-btn-${index}`).addEventListener('click', () => {
                    this.saveEditDepartment(index, currentName);
                });
                
                input.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        this.saveEditDepartment(index, currentName);
                    } else if (e.key === 'Escape') {
                        this.cancelEditDepartment();
                    }
                });
            }

            saveEditDepartment(index, oldName) {
                const input = document.getElementById(`edit-input-${index}`);
                const newName = input.value;
                
                if (this.departmentManager.editDepartment(oldName, newName)) {
                    this.updateUI();
                } else {
                    this.updateUI();
                }
            }

            cancelEditDepartment() {
                this.updateUI();
            }
        }
'''

# RouletteAppクラスを挿入（既存のメソッド定義の前に）
content = re.sub(
    r'(\n            addDepartment\(\) \{)',
    roulette_app_class + r'\1',
    content
)

# 修正5: 初期化コードを修正（appをグローバルに）
content = re.sub(
    r'        // ========== Initialize Application ==========\r?\n        let app;\r?\n        window\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\r?\n            app = new RouletteApp\(\);\r?\n        \}\);',
    r'        // ========== Initialize Application ==========\n        window.addEventListener(\'DOMContentLoaded\', () => {\n            window.app = new RouletteApp();\n        });',
    content
)

# ファイルに書き込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("修正が完了しました!")
print("1. 余分な閉じ括弧を削除")
print("2. animate()呼び出しを追加")
print("3. 不適切なイベントリスナーを削除")
print("4. RouletteAppクラスを追加")
print("5. appをグローバル変数に変更")
