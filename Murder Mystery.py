import pygame
pygame.init()

# Window Structure
window_width, window_height = 800, 800
WINDOW = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Murder Mystery')
fps = 60
timer = pygame.time.Clock()
main_menu = False
menu_command = 0
font = pygame.font.Font('freesansbold.ttf', 25)

# Program Icon
pygame_icon = pygame.image.load('Godly_Icon.png')
pygame.display.set_icon(pygame_icon)

# Rick Roll QR Code for easter egg
qr_code_img = pygame.image.load('qrcode.png')
qr_codeX, qr_codeY = 150, 150    

# Button Class
class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(WINDOW, 'light gray', self.button, 0, 5)
        pygame.draw.rect(WINDOW, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        WINDOW.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

# Main Draw Menu
def draw_menu():
    command = -1
    pygame.draw.rect(WINDOW, 'black', [100, 100, 300, 300])
    pygame.draw.rect(WINDOW, 'green', [100, 100, 300, 300], 5)
    pygame.draw.rect(WINDOW, 'white', [120, 120, 260, 40], 0, 5)
    pygame.draw.rect(WINDOW, 'gray', [120, 120, 260, 40], 5, 5)
    txt = font.render('Main Menu', True, 'black')
    WINDOW.blit(txt, (135, 127))
    menu = Button('Exit Menu', (120, 350))
    menu.draw()
    button1 = Button('Play', (120, 180))
    button1.draw()
    button2 = Button('Settings', (120, 240))
    button2.draw()
    button3 = Button('Highscores', (120, 300))
    button3.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command

# Starting Screen - WIP
def draw_game():
    menu_btn = Button('Main Menu', (230, 450))
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    return menu

# Game Loop
run = True
while run:
    WINDOW.fill('light blue')
    timer.tick(fps)
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command > 0:
            text = font.render(f'{menu_command} was selected!', True, 'black')
            WINDOW.blit(text, (150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()