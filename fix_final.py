import re

# ファイルを読み込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 修正1: 1113行目付近の animate(); を追加
# animate関数定義の終わりを探して、その後にanimate();を追加
for i in range(len(lines)):
    if i > 1090 and '};' in lines[i] and 'return new Promise' in ''.join(lines[max(0,i-20):i]):
        # この};の直前にanimate();を追加
        if 'animate();' not in lines[i-1]:
            lines.insert(i, '                    animate();\n')
            break

# 修正2: 不適切なイベントリスナーコードを削除（1115-1140行目付近）
# "// 部門追加" から "}" までを削除
start_idx = None
end_idx = None
for i in range(len(lines)):
    if '// 部門追加' in lines[i] and 'document.getElementById(\'addButton\')' in lines[i+1]:
        start_idx = i
    if start_idx is not None and i > start_idx and lines[i].strip() == '}' and 'this.updateUI' in ''.join(lines[max(0,i-5):i]):
        end_idx = i + 1
        break

if start_idx and end_idx:
    del lines[start_idx:end_idx]

# 修正3: RouletteAppクラスを追加
# addDepartment() メソッドの前に挿入
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

'''

for i in range(len(lines)):
    if 'addDepartment()' in lines[i] and 'const input' in lines[i+1]:
        lines.insert(i, roulette_app_class)
        break

# ファイルに書き込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("完全な修正が完了しました!")
print("1. animate()呼び出しを追加")
print("2. 不適切なイベントリスナーを削除")
print("3. RouletteAppクラスを追加")
