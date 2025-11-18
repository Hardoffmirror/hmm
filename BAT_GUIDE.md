# Руководство по BAT файлам / BAT Files Guide

## ⚠️ ВАЖНО / IMPORTANT

**Все .bat файлы должны запускаться ТОЛЬКО из корневой папки проекта `hmm`!**

**All .bat files must be run ONLY from the project root folder `hmm`!**

---

## 🚫 Типичная ошибка / Common Error

```
fatal: not a git repository (or any of the parent directories): .git
```

**Причина:** Вы запустили .bat файл не в той папке!

**Reason:** You ran the .bat file from wrong folder!

---

## ✅ Правильное использование / Correct Usage

### Шаг 1: Откройте командную строку
**Windows:**
- Нажмите `Win + R`
- Введите `cmd`
- Нажмите Enter

### Шаг 2: Перейдите в папку проекта
```cmd
cd C:\path\to\your\hmm
```

**Примеры:**
```cmd
cd C:\Users\YourName\Desktop\hmm
cd D:\Projects\hmm
cd %USERPROFILE%\Downloads\hmm
```

### Шаг 3: Проверьте что вы в правильной папке
```cmd
dir
```

Вы должны увидеть файлы:
- `tarot_analyzer.py`
- `web_app.py`
- `requirements.txt`
- `update.bat`
- `run.bat`
- и другие

### Шаг 4: Запустите нужный .bat файл
```cmd
update.bat
```

или

```cmd
run_web.bat
```

---

## 📁 Альтернативный способ / Alternative Method

1. Откройте папку `hmm` в проводнике Windows
2. Найдите адресную строку вверху окна (где путь к папке)
3. Кликните в адресную строку
4. Введите `cmd` и нажмите Enter
5. Командная строка откроется ПРЯМО в нужной папке!
6. Теперь можете запускать .bat файлы

---

## 📝 Список BAT файлов / BAT Files List

### `update.bat`
**Назначение:** Обновить проект из Git и зависимости

**Что делает:**
1. ✅ Проверяет что вы в правильной папке
2. 📥 Обновляет код из Git
3. 📦 Обновляет Python зависимости

**Использование:**
```cmd
cd C:\path\to\hmm
update.bat
```

---

### `update_and_run.bat`
**Назначение:** Обновить и сразу запустить CLI анализатор

**Что делает:**
1. ✅ Проверяет папку
2. 📥 Обновляет из Git
3. 📦 Обновляет зависимости
4. 🚀 Запускает CLI версию

**Использование:**
```cmd
cd C:\path\to\hmm
update_and_run.bat
```

---

### `run.bat`
**Назначение:** Быстро запустить CLI анализатор

**Что делает:**
1. ✅ Проверяет папку
2. 🚀 Запускает `tarot_analyzer.py`

**Использование:**
```cmd
cd C:\path\to\hmm
run.bat
```

**С параметрами:**
```cmd
run.bat --league "Settlers" --min-profit 10
```

---

### `run_web.bat`
**Назначение:** Запустить веб-интерфейс

**Что делает:**
1. ✅ Проверяет папку
2. 🌐 Запускает веб-сервер
3. 🌍 Открывает браузер автоматически

**Использование:**
```cmd
cd C:\path\to\hmm
run_web.bat
```

**Остановка:** Нажмите `Ctrl+C` в окне командной строки

---

### `install_and_run.bat`
**Назначение:** Первая установка и запуск

**Что делает:**
1. ✅ Проверяет папку
2. 🐍 Проверяет установку Python
3. 📦 Устанавливает зависимости
4. 🚀 Запускает анализатор

**Использование:**
```cmd
cd C:\path\to\hmm
install_and_run.bat
```

---

## 🐛 Устранение проблем / Troubleshooting

### Ошибка: "not a git repository"
**Решение:**
1. Убедитесь что вы в папке `hmm`
2. В папке должна быть скрытая папка `.git`
3. Проверьте командой: `dir /ah .git`

### Ошибка: "requirements.txt not found"
**Решение:**
1. Вы не в корневой папке проекта
2. Выполните: `cd C:\полный\путь\к\hmm`

### Ошибка: "Python not found"
**Решение:**
1. Установите Python с https://www.python.org/downloads/
2. **ВАЖНО:** При установке отметьте "Add Python to PATH"
3. Перезапустите командную строку

### Ошибка: "таrot_analyzer.py not found"
**Решение:**
1. Проверьте что вы в папке `hmm`
2. Выполните `dir` и найдите файл
3. Если файла нет - скачайте проект заново

---

## 💡 Полезные команды / Useful Commands

### Узнать текущую папку
```cmd
cd
```

### Посмотреть содержимое папки
```cmd
dir
```

### Перейти на диск D:
```cmd
d:
cd \Projects\hmm
```

### Перейти на рабочий стол
```cmd
cd %USERPROFILE%\Desktop\hmm
```

### Очистить экран
```cmd
cls
```

---

## 📚 Быстрый старт / Quick Start

**Если проект уже скачан:**
```cmd
cd C:\путь\к\hmm
run_web.bat
```

**Если нужно обновить:**
```cmd
cd C:\путь\к\hmm
update.bat
run_web.bat
```

**Если первый запуск:**
```cmd
cd C:\путь\к\hmm
install_and_run.bat
```

---

## ❓ Как узнать где находится папка hmm?

1. Откройте папку `hmm` в проводнике
2. Кликните правой кнопкой на `tarot_analyzer.py`
3. Выберите "Свойства" / "Properties"
4. Посмотрите "Расположение" / "Location"
5. Скопируйте путь
6. В cmd выполните: `cd "скопированный_путь"`

---

## 🎯 Рекомендуемый workflow

1. **Первый раз:**
   ```cmd
   cd C:\your\path\to\hmm
   install_and_run.bat
   ```

2. **Обновление (раз в день):**
   ```cmd
   cd C:\your\path\to\hmm
   update.bat
   ```

3. **Каждый запуск:**
   ```cmd
   cd C:\your\path\to\hmm
   run_web.bat
   ```

**Совет:** Создайте ярлык на `run_web.bat` на рабочем столе!
