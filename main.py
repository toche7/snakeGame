import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def gen_start_pos():
    return (random.randint(0, 1280), random.randint(0, 720))


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




# print(snake_pixel)
# print(snake_pixel.center)
# input("Press enter to continue")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
#    show score on screen
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {snake_length-1}", True, "white")
    screen.blit(score_text, (0, 0))
    
    # RENDER YOUR GAME HERE
    if old_pos != player_pos:
        old_pos = player_pos.copy()
        if snake_length > 1:    
            snake = snake[:snake_length-1]
            snake.insert(0, snake[0].copy())
        snake[0].center = player_pos

    for segment in snake:
        pygame.draw.rect(screen, "green", segment)

    pygame.draw.rect(screen, "red", food)

    if snake[0].colliderect(food):
        food.center = gen_start_pos()
        snake_length += 1
        snake.append(snake[-1].copy())
        print(snake_length)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= pixel_width
    if keys[pygame.K_s]:
        player_pos.y += pixel_width
    if keys[pygame.K_a]:
        player_pos.x -= pixel_width
    if keys[pygame.K_d]:
        player_pos.x += pixel_width
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(15)  # limits FPS to 60

pygame.quit()