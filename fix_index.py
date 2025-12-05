import re

# ファイルを読み込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修正するコード
old_code = '''                // 重複チェック
                if (data.departments.some(dept => dept.toLowerCase() === lowerCaseName)) {
                    return;
                }

                // カスタム確認モーダルを表示
                this.showDeleteConfirmation(name, (confirmed) => {
                    if (confirmed) {
                        data.departments = data.departments.filter(dept => dept !== name);
                        this.storage.saveData(data);
                        this.onUpdate();
                    }
                    if (callback) callback(confirmed);
                });
            }

            showDeleteConfirmation(name, callback) {
                const modal = document.getElementById('deleteConfirmModal');
                const text = document.getElementById('deleteConfirmText');
                const confirmBtn = document.getElementById('confirmDeleteButton');
                const cancelBtn = document.getElementById('cancelDeleteButton');

                text.textContent = `「${name}」を削除しますか?`;
                modal.classList.add('show');

                const handleConfirm = () => {
                    modal.classList.remove('show');
                    cleanup();
                    callback(true);
                };

                const handleCancel = () => {
                    modal.classList.remove('show');
                    cleanup();
                    callback(false);
                };

                const cleanup = () => {
                    confirmBtn.removeEventListener('click', handleConfirm);
                    cancelBtn.removeEventListener('click', handleCancel);
                };

                confirmBtn.addEventListener('click', handleConfirm);
                cancelBtn.addEventListener('click', handleCancel);
            }
        }'''

new_code = '''                // 重複チェック
                if (data.departments.some(dept => dept.toLowerCase() === lowerCaseName)) {
                    alert('この部門名は既に登録されています');
                    return false;
                }

                // 部門名を更新
                const index = data.departments.findIndex(dept => dept === oldName);
                if (index !== -1) {
                    data.departments[index] = trimmedName;
                    
                    // 履歴も更新
                    data.history = data.history.map(h => h === oldName ? trimmedName : h);
                    
                    this.storage.saveData(data);
                    this.onUpdate();
                    return true;
                }
                return false;
            }

            deleteDepartment(name) {
                const data = this.storage.loadData();
                
                if (data.departments.length <= this.MIN_DEPARTMENTS) {
                    alert(`部門は最低${this.MIN_DEPARTMENTS}つ必要です`);
                    return;
                }

                // カスタム確認モーダルを表示
                const modal = document.getElementById('deleteConfirmModal');
                const text = document.getElementById('deleteConfirmText');
                const confirmBtn = document.getElementById('confirmDeleteButton');
                const cancelBtn = document.getElementById('cancelDeleteButton');

                text.textContent = `「${name}」を削除しますか?`;
                modal.classList.add('show');

                const cleanup = () => {
                    confirmBtn.removeEventListener('click', handleConfirm);
                    cancelBtn.removeEventListener('click', handleCancel);
                };

                const handleConfirm = () => {
                    const data = this.storage.loadData();
                    data.departments = data.departments.filter(dept => dept !== name);
                    data.history = data.history.filter(h => h !== name);
                    
                    this.storage.saveData(data);
                    this.onUpdate();
                    modal.classList.remove('show');
                    cleanup();
                };

                const handleCancel = () => {
                    modal.classList.remove('show');
                    cleanup();
                };

                confirmBtn.addEventListener('click', handleConfirm);
                cancelBtn.addEventListener('click', handleCancel);
            }
        }'''

# 置換
content = content.replace(old_code, new_code)

# ファイルに書き込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("修正完了!")
