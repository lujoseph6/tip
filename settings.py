from win32api import GetSystemMetrics

class Settings():

    def __init__(self):
        self.screen_width = GetSystemMetrics(0)
        self.screen_height = GetSystemMetrics(1) - 60
        self.bg_color = (230, 230, 230)
        self.ship_limit = 2
        self.bullet_width = 10
        self.bullet_height = 250
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10
        self.fleet_drop_speed = 5
        self.speedup_scale = 1.1
        self.score_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 0.5
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)