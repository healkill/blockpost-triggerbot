import pyautogui
import time
import json
import keyboard
from PIL import ImageGrab

class TriggerBot:
    def __init__(self):
        self.load_config()
        self.active = False
        self.target_color = None
        self.last_shot_time = 0
        
    def load_config(self):
        with open('config.json') as f:
            config = json.load(f)
            self.threshold = config["threshold"]
            self.trigger_key = config["trigger_key"]
            self.exit_key = config["exit_key"]
            self.offset = config["crosshair_offset"]
            self.shot_delay = config["shot_delay"]
            self.cooldown = config["cooldown_ms"] / 1000
    
    def get_pixel_color(self, x, y):
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        return screenshot.getpixel((0, 0))
    
    def run(self):
        print(f"TriggerBot | Активация: {self.trigger_key} | Выход: {self.exit_key}")
        print("Бот будет стрелять ТОЛЬКО при зажатии клавиши и обнаружении цели")
        
        try:
            while True:
                if keyboard.is_pressed(self.exit_key):
                    print("Завершение работы...")
                    break
                    
                current_time = time.time()
                
                if keyboard.is_pressed(self.trigger_key):
                    if not self.active:
                        # Первичная активация
                        x, y = pyautogui.position()
                        x += self.offset
                        y += self.offset
                        self.target_color = self.get_pixel_color(x, y)
                        self.active = True
                        print("АКТИВИРОВАН | Слежение за целью...")
                    
                    # Проверка цвета
                    x, y = pyautogui.position()
                    x += self.offset
                    y += self.offset
                    current_color = self.get_pixel_color(x, y)
                    
                    diff = sum(abs(c - t) for c, t in zip(current_color, self.target_color))
                    
                    if diff > self.threshold and current_time - self.last_shot_time > self.cooldown:
                        pyautogui.click(button='left')
                        self.last_shot_time = current_time
                        print("ВЫСТРЕЛ!")
                else:
                    if self.active:
                        # Деактивация
                        self.active = False
                        print("ОСТАНОВЛЕН | Ожидание активации...")
                
                time.sleep(0.005)  # Ультра-быстрая проверка
                
        except KeyboardInterrupt:
            print("\nРабота завершена")

if __name__ == "__main__":
    bot = TriggerBot()
    bot.run()
