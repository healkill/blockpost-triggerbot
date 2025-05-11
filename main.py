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
        
    def load_config(self):
        with open('config.json') as f:
            config = json.load(f)
            self.threshold = config["threshold"]
            self.trigger_key = config["trigger_key"]
            self.exit_key = config["exit_key"]
            self.offset = config["crosshair_offset"]
            self.shot_delay = config["shot_delay"]
    
    def get_pixel_color(self, x, y):
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        return screenshot.getpixel((0, 0))
    
    def run(self):
        print(f"TriggerBot запущен! Удерживайте {self.trigger_key} для активации")
        print(f"Выход: {self.exit_key}")
        
        try:
            while True:
                if keyboard.is_pressed(self.exit_key):
                    print("Выход...")
                    break
                    
                if keyboard.is_pressed(self.trigger_key):
                    if not self.active:
                        x, y = pyautogui.position()
                        x += self.offset
                        y += self.offset
                        self.target_color = self.get_pixel_color(x, y)
                        self.active = True
                        print(f"Цель: {self.target_color} | Позиция: ({x}, {y})")
                    
                    x, y = pyautogui.position()
                    x += self.offset
                    y += self.offset
                    current_color = self.get_pixel_color(x, y)
                    
                    diff = sum(abs(c - t) for c, t in zip(current_color, self.target_color))
                    if diff > self.threshold:
                        pyautogui.click(button='left')
                        time.sleep(self.shot_delay)
                else:
                    self.active = False
                    
                time.sleep(0.01)
                
        except KeyboardInterrupt:
            print("\nРабота завершена")

if __name__ == "__main__":
    bot = TriggerBot()
    bot.run()
