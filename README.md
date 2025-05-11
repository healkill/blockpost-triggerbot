### 🇷🇺 Полная инструкция по установке и использованию TriggerBot для BlockPost

---

#### 🔧 **1. Установка необходимых компонентов**

1. **Скачайте и установите Python**:
   - Перейдите на [официальный сайт Python](https://www.python.org/downloads/)
   - Скачайте последнюю версию (3.7 или выше)
   - **ВАЖНО**: При установке отметьте галочки:
     - ☑ `Add Python to PATH`
     - ☑ `Install pip`

2. **Скачайте файлы бота**:
   - На странице GitHub нажмите `Code` → `Download ZIP`
   - Распакуйте архив в удобное место (например, `C:\blockpost-bot`)

---

#### 💻 **2. Установка зависимостей через CMD**

1. Откройте **Командную строку**:
   - Нажмите `Win + R`
   - Введите `cmd`
   - Нажмите `Enter`

2. Перейдите в папку с ботом:
   ```cmd
   cd C:\blockpost-bot
   ```
   (замените путь на свой)

3. Установите зависимости:
   ```cmd
   pip install pyautogui pillow keyboard
   ```

---

#### ⚙ **3. Настройка конфигурации**

1. Откройте файл `config.json` в блокноте
2. Настройте параметры:
   ```json
   {
       "threshold": 15,
       "trigger_key": "x",
       "exit_key": "end",
       "crosshair_offset": 2,
       "shot_delay": 50,
       "cooldown_ms": 100
   }
   ```
   - `threshold`: Чувствительность (10-30)
   - `crosshair_offset`: Смещение от центра прицела

---

#### 🎮 **4. Запуск и использование**

1. В командной строке (уже в папке с ботом):
   ```cmd
   python main.py
   ```

2. **В игре**:
   - Наведите прицел на врага
   - **Зажмите** клавишу `x` для активации
   - Бот будет стрелять при обнаружении цели
   - **Отпустите** `x` для двойного выстрела и остановки
   - Для выхода нажмите `End`

---

#### ❓ **Частые проблемы и решения**

| Проблема | Решение |
|----------|---------|
| "Python не найден" | Переустановите Python с галочкой "Add to PATH" |
| Ошибки при установке | Попробуйте `python -m pip install ...` |
| Бот не реагирует | Уменьшите `threshold` в config.json |
| Зависания | Закройте лишние программы |

---

### 🇬🇧 Complete TriggerBot Setup Guide for BlockPost

---

#### 🔧 **1. Install Requirements**

1. **Install Python**:
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation check:
     - ☑ `Add Python to PATH`
     - ☑ `Install pip`

2. **Download Bot Files**:
   - Click `Code` → `Download ZIP` on GitHub
   - Extract to folder (e.g. `C:\blockpost-bot`)

---

#### 💻 **2. Install Dependencies via CMD**

1. Open **Command Prompt**:
   - Press `Win + R`
   - Type `cmd`
   - Press `Enter`

2. Navigate to bot folder:
   ```cmd
   cd C:\blockpost-bot
   ```
   (replace with your path)

3. Install packages:
   ```cmd
   pip install pyautogui pillow keyboard
   ```

---

#### ⚙ **3. Configuration**

1. Edit `config.json`:
   ```json
   {
       "threshold": 15,
       "trigger_key": "x",
       "exit_key": "end",
       "crosshair_offset": 2,
       "shot_delay": 50,
       "cooldown_ms": 100
   }
   ```
   - `threshold`: Sensitivity (10-30)
   - `crosshair_offset`: Crosshair offset

---

#### 🎮 **4. Launch & Usage**

1. In Command Prompt (in bot folder):
   ```cmd
   python main.py
   ```

2. **In-Game**:
   - Aim at enemy
   - **Hold** `x` to activate
   - Bot will auto-shoot when target detected
   - **Release** `x` for double-shot
   - Press `End` to exit

---

#### ❓ **Troubleshooting**

| Issue | Solution |
|-------|----------|
| "Python not found" | Reinstall Python with PATH option |
| Installation errors | Try `python -m pip install ...` |
| No reaction | Decrease `threshold` value |
| Freezes | Close background programs |

---

### 🔥 **Pro Tips**
- Для быстрого пути в CMD: перетащите папку в окно командной строки после `cd `
- For quick path in CMD: drag folder into CMD window after `cd `
- Оптимальные настройки для BlockPost: `threshold=15`, `offset=2`
