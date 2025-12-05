import re

# ファイルを読み込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修正するコード
old_code = '''        // ========== Initialize Application ==========
        let app;
        window.addEventListener('DOMContentLoaded', () => {
            app = new RouletteApp();
        });'''

new_code = '''        // ========== Initialize Application ==========
        window.addEventListener('DOMContentLoaded', () => {
            window.app = new RouletteApp();
        });'''

# 置換
content = content.replace(old_code, new_code)

# ファイルに書き込む
with open(r'c:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("app変数をグローバルに修正完了!")
