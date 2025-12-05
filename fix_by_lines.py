#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ファイルを読み込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 行834-878を置き換える (0-indexed なので 833-877)
new_lines = [
    "                // 重複チェック\r\n",
    "                if (data.departments.some(dept => dept.toLowerCase() === lowerCaseName)) {\r\n",
    "                    alert('この部門名は既に登録されています');\r\n",
    "                    return false;\r\n",
    "                }\r\n",
    "\r\n",
    "                // 部門名を更新\r\n",
    "                const index = data.departments.findIndex(dept => dept === oldName);\r\n",
    "                if (index !== -1) {\r\n",
    "                    data.departments[index] = trimmedName;\r\n",
    "                    \r\n",
    "                    // 履歴も更新\r\n",
    "                    data.history = data.history.map(h => h === oldName ? trimmedName : h);\r\n",
    "                    \r\n",
    "                    this.storage.saveData(data);\r\n",
    "                    this.onUpdate();\r\n",
    "                    return true;\r\n",
    "                }\r\n",
    "                return false;\r\n",
    "            }\r\n",
    "\r\n",
    "            deleteDepartment(name) {\r\n",
    "                const data = this.storage.loadData();\r\n",
    "                \r\n",
    "                if (data.departments.length <= this.MIN_DEPARTMENTS) {\r\n",
    "                    alert(`部門は最低${this.MIN_DEPARTMENTS}つ必要です`);\r\n",
    "                    return;\r\n",
    "                }\r\n",
    "\r\n",
    "                // カスタム確認モーダルを表示\r\n",
    "                const modal = document.getElementById('deleteConfirmModal');\r\n",
    "                const text = document.getElementById('deleteConfirmText');\r\n",
    "                const confirmBtn = document.getElementById('confirmDeleteButton');\r\n",
    "                const cancelBtn = document.getElementById('cancelDeleteButton');\r\n",
    "\r\n",
    "                text.textContent = `「${name}」を削除しますか?`;\r\n",
    "                modal.classList.add('show');\r\n",
    "\r\n",
    "                const cleanup = () => {\r\n",
    "                    confirmBtn.removeEventListener('click', handleConfirm);\r\n",
    "                    cancelBtn.removeEventListener('click', handleCancel);\r\n",
    "                };\r\n",
    "\r\n",
    "                const handleConfirm = () => {\r\n",
    "                    const data = this.storage.loadData();\r\n",
    "                    data.departments = data.departments.filter(dept => dept !== name);\r\n",
    "                    data.history = data.history.filter(h => h !== name);\r\n",
    "                    \r\n",
    "                    this.storage.saveData(data);\r\n",
    "                    this.onUpdate();\r\n",
    "                    modal.classList.remove('show');\r\n",
    "                    cleanup();\r\n",
    "                };\r\n",
    "\r\n",
    "                const handleCancel = () => {\r\n",
    "                    modal.classList.remove('show');\r\n",
    "                    cleanup();\r\n",
    "                };\r\n",
    "\r\n",
    "                confirmBtn.addEventListener('click', handleConfirm);\r\n",
    "                cancelBtn.addEventListener('click', handleCancel);\r\n",
    "            }\r\n",
    "        }\r\n",
]

# 行834-878を置き換え (0-indexed: 833-877)
lines[833:878] = new_lines

# 行1276-1279を修正 (0-indexed: 1275-1278)
# 現在の行を確認
for i in range(1275, 1280):
    if i < len(lines):
        print(f"Line {i+1}: {lines[i].rstrip()}")

# let app; を削除し、window.app = に変更
for i in range(1275, 1280):
    if i < len(lines):
        if 'let app;' in lines[i]:
            # この行を削除
            lines[i] = ''
        elif 'app = new RouletteApp();' in lines[i]:
            # window.app に変更
            lines[i] = lines[i].replace('app = new RouletteApp();', 'window.app = new RouletteApp();')

# ファイルに書き込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("\n修正完了!")
print("1. editDepartmentメソッドを修正 (行834-848)")
print("2. deleteDepartmentメソッドを追加 (行849-895)")
print("3. appをグローバル変数に変更 (行1276-1279)")
