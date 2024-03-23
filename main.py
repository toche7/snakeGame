import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
oldkey = 0
font = pygame.font.Font(None, 36)
sound_music = pygame.mixer.Sound("sounds/beattheme1-28954.mp3")
sound_score = pygame.mixer.Sound("sounds/score.mp3")
sound_end = pygame.mixer.Sound("sounds/buzzer.mp3")
def gen_start_pos():
    return (random.randint(0, 1280), random.randint(0, 720))

# function print you lose when the snake hit the wall or itself on the game screen
def you_lose():
    #show you lose on the screen
    text = font.render("You Lose", True, "red")
    screen.blit(text, (600, 360))
    sound_end.play()
    pygame.display.flip()
    pygame.time.delay(2000)


#ask for restart
def ask_for_restart():
    text = font.render("Press R to restart or Esc for Quit", True, "red")
    screen.blit(text, (470, 260))
    pygame.display.flip()
    # wait for user to press R to restart
    while True:
        event = pygame.event.wait()
        global running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                break
            elif event.key == pygame.K_ESCAPE:
                running = False
                break
        elif event.type == pygame.QUIT:
            running = False
            break

# restart the game
def restart():
    global running
    running = True
    global player_pos
    player_pos = pygame.Vector2(gen_start_pos())
    global snake_pixel
    snake_pixel.center = player_pos
    global old_pos
    old_pos = player_pos.copy()
    global snake_length
    snake_length = 1
    global snake
    snake = [snake_pixel.copy()]
    global food
    food.center = pygame.Vector2(gen_start_pos())
    global oldkey
    oldkey = 0

#playground
pixel_width = 50
snake_pixel = pygame.Rect(0, 0, pixel_width, pixel_width)
player_pos = pygame.Vector2(gen_start_pos())
snake_pixel.center = player_pos
old_pos = player_pos.copy()
snake_length = 1
snake = [snake_pixel.copy()]

food = pygame.Rect(0, 0, pixel_width, pixel_width)
food.center = pygame.Vector2(gen_start_pos())

sound_music.play(loops=-1)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
#    show score on screen

    score_text = font.render(f"Score: {snake_length-1}", True, "blue")
    screen.blit(score_text, (0, 0))


    # RENDER YOUR GAME HERE
    if old_pos != player_pos:
        old_pos = player_pos.copy()
        if snake_length > 1:    
            snake = snake[:snake_length-1]
            snake.insert(0, snake[0].copy())
        snake[0].center = player_pos
        #play sound when snake move


    # snake collision itself
    for segment in snake[1:]:
        if snake[0].colliderect(segment): 
             you_lose()
             ask_for_restart()

    # snake collision the wall
    if player_pos.x < 0 or player_pos.x > 1280 or player_pos.y < 0 or player_pos.y > 720:
         you_lose()
         ask_for_restart()

    for segment in snake:
        pygame.draw.rect(screen, "green", segment)

    pygame.draw.rect(screen, "red", food)

    if snake[0].colliderect(food):
        food.center = gen_start_pos()
        snake_length += 1
        snake.append(snake[-1].copy())
        print(snake_length)
        sound_score.play()
    
    if event.type == pygame.KEYDOWN:
        oldkey = event.key  
    if oldkey == pygame.K_UP:
            player_pos.y -= pixel_width
    elif oldkey == pygame.K_DOWN:
            player_pos.y += pixel_width
    elif oldkey == pygame.K_LEFT:
            player_pos.x -= pixel_width
    elif oldkey == pygame.K_RIGHT:
            player_pos.x += pixel_width
        
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(8)  # limits FPS to 60

pygame.quit()