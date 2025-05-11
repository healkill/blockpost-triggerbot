import pyautogui
import time
import json
import keyboard
from PIL import ImageGrab

class TriggerBot:
    def __init__(self):
        self.load_config()
        self.active = False
        self.was_active = False
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
    
    def double_click(self):
        pyautogui.click(button='left')
        time.sleep(0.05)
        pyautogui.click(button='left')
    
    def run(self):
        print(f"TriggerBot | Активация: {self.trigger_key} | Выход: {self.exit_key}")
        print("Двойной выстрел при отпускании клавиши")
        
        try:
            while True:
                if keyboard.is_pressed(self.exit_key):
                    print("Завершение работы...")
                    break
                    
                current_time = time.time()
                
                if keyboard.is_pressed(self.trigger_key):
                    if not self.active:
                        # Активация
                        x, y = pyautogui.position()
                        x += self.offset
                        y += self.offset
                        self.target_color = self.get_pixel_color(x, y)
                        self.active = True
                        self.was_active = True
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
                else:
                    if self.was_active:
                        # Двойной выстрел при отпускании
                        self.double_click()
                        self.active = False
                        self.was_active = False
                        print("ДВОЙНОЙ ВЫСТРЕЛ | Остановка")
                
                time.sleep(0.005)
                
        except KeyboardInterrupt:
            print("\nРабота завершена")

if __name__ == "__main__":
    bot = TriggerBot()
    bot.run()
