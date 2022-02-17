import pygame
import random
#######################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('똥피하기')

# FPS
clock = pygame.time.Clock()
#######################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표정의, 속도, 폰트 등)

# 배경화면
background = pygame.image.load('background.png')

# 캐릭터
character = pygame.image.load('character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_position = screen_width/2 - character_width/2
character_y_position = screen_height - character_height
character_to_x = 0
character_speed = 0.6

# 에너미
enemy = pygame.image.load('enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_position = 0
enemy_y_position = 0
enemy_to_y = 0
enemy_speed = 0.7

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 좌우키를 눌렀을 때 x 방향 이용
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
        # 키를 놓았을 때 
        if event.type == pygame.KEYUP:
            character_to_x = 0
        
    # 3. 게임 캐릭터 위치 정의

    # 캐릭터 위치
    character_x_position += character_to_x * dt

    # 캐릭터 경계 처리
    if character_x_position <= 0:
        character_x_position = 0
    elif character_x_position + character_width >= screen_width:
        character_x_position = screen_width - character_width

    # 에너미 위치
    enemy_y_position += enemy_speed * dt

    # 에너미 시작위치 및 경계처리
    if enemy_y_position > screen_height:
        enemy_y_position = 0
        enemy_x_position = int((random.random()) * (screen_width-enemy_width))

    # 4. 충돌 처리

    # 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect() # 사각형상 정보를 가져옴
    character_rect.left = character_x_position # 현재 위치로 좌측 상단 위치 업데이트
    character_rect.top = character_y_position

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_position,character_y_position))
    screen.blit(enemy, (enemy_x_position,enemy_y_position))

    pygame.display.update()

pygame.quit()