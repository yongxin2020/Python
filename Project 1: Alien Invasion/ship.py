import pygame

# ship类
class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.x += 1
            self.x += self.settings.ship_speed
        # 用if不用elif的原因：使同时按下左右两键的时候位置保持不动而不是右箭头键始终处于优先地位
        if self.moving_left and self.rect.left > 0:
            #self.rect.x -= 1
            self.x -= self.settings.ship_speed
        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)