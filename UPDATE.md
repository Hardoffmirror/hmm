# Команды для обновления / Update Commands

## 🔄 Обновить проект из Git

### Windows (Command Prompt / PowerShell)
```cmd
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS && pip install -r requirements.txt --upgrade
```

### Linux / macOS
```bash
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS && pip install -r requirements.txt --upgrade
```

---

## 📥 Первая установка (если репозиторий ещё не скачан)

### Windows
```cmd
git clone <URL_репозитория>
cd hmm
git checkout claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
pip install -r requirements.txt
```

### Linux / macOS
```bash
git clone <URL_репозитория>
cd hmm
git checkout claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
pip install -r requirements.txt
```

---

## ⚡ Быстрые команды

### Обновить и запустить
**Windows:**
```cmd
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS && pip install -r requirements.txt --upgrade && python tarot_analyzer.py
```

**Linux / macOS:**
```bash
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS && pip install -r requirements.txt --upgrade && python tarot_analyzer.py
```

### Только запуск (без обновления)
```cmd
python tarot_analyzer.py
```
