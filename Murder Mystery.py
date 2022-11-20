import pygame

# Window Structure
screen_width, screen_height = 800, 800
WINDOW = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Murder Mystery')

# Program Icon
pygame_icon = pygame.image.load('Godly_Icon.png')
pygame.display.set_icon(pygame_icon)

# Start button
# start_button = pygame.image.load('Start_Btn.png')

# Sample Image
qr_code_img = pygame.image.load('qrcode.png')
qr_codeX, qr_codeY = 150, 150    

# Game Loop
def main():
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        WINDOW.blit(qr_code_img, (qr_codeX,qr_codeY))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()