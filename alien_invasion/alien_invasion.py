import sys
#玩家退出的时候，使用sys模块退出游戏
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()#初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
        
    #创建一个显示窗口，实参是一个元组
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船
    ship = Ship(Screen)
    
    #设置背景色
    bg_color = (230, 230, 230)#一种浅灰色
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events()
        # for event in pygame.event.get():#侦听事件
            # if event.type == pygame.QUIT:
                # sys.exit()
        
        gf.update_screen(ai_settings, screen, ship)
        # #每次循环的时候都重绘屏幕，用背景色填充屏幕
        # #但是这个时候的屏幕没有被更新
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
                 
        # #更新
        # #屏幕，显示元素的新位置，从而构成平滑移动的效果
        # pygame.display.flip()
    
run_game()