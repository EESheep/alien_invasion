import sys
#玩家退出的时候，使用sys模块退出游戏
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()#初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
        
    #创建一个显示窗口，实参是一个元组
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #设置背景色
    bg_color = (230, 230, 230)#一种浅灰色
    
    #
    alien = Alien(ai_settings, screen)
    
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
