// DepartmentManagerクラスの修正版メソッド
// 以下のコードをindex.htmlの行813-878に置き換えてください

editDepartment(oldName, newName) {
    const trimmedName = newName.trim();

    if (!trimmedName) {
        alert('部門名を入力してください');
        return false;
    }

    if (trimmedName.length > this.MAX_NAME_LENGTH) {
        alert(`部門名は${this.MAX_NAME_LENGTH}文字以内で入力してください`);
        return false;
    }

    const data = this.storage.loadData();
    const lowerCaseName = trimmedName.toLowerCase();
    const oldLowerCaseName = oldName.toLowerCase();

    // 同じ名前の場合は変更なし
    if (oldLowerCaseName === lowerCaseName) {
        return true;
    }

    // 重複チェック
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
