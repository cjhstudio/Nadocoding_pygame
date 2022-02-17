import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game') # 상단 창 이름에 들어가는 제목

# FPS
clock = pygame.time.Clock()


# 배경이미지 불러오기
background = pygame.image.load("background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기 - 사이즈의 첫번째
character_height = character_size[1] # 캐릭터의 세로 크기 - 사이즈의 두번째
character_x_pos = (screen_width / 2) - (character_width/2) # 화면의 가로 중앙
character_y_pos = screen_height - character_height # 화면 세로크기의 가장 아래쪽
# 좌표원점은 좌측 상단이 (0,0) - 좌표계를 고려하여 위치 계산해야 함

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기 - 사이즈의 첫번째
enemy_height = enemy_size[1] # 캐릭터의 세로 크기 - 사이즈의 두번째
enemy_x_pos = (screen_width / 2) - (enemy_width/2) # 화면의 가로 중앙
enemy_y_pos = (screen_height / 2) - (enemy_height/2) # 화면 세로 중앙

# 화면 텍스트의 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10
# 시작시작 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:

    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # 캐릭터가 1초 동안에 100 만큼 이동해야 함
    # 10 fps : 1초 동안 10번 동작 -> 한번에 10만큼 이동해야 함 10 * 10 = 100
    # 20 fps : 1초 동안 20번 동작 -> 한번에 5 만큼 이동해야 함 5 * 20 = 100

    for event in pygame.event.get(): # 이벤트 발생 체크. 항상 설정하는 세팅
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False # 게임이 진행중이 아님 - while 문 빠져나옴

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:# 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #떼기전에 좌우를 누르고 있었다면 to_x를 0으로 바꿔줌
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 #떼기전에 상하를 누르고 있었다면 to_y를 0으로 바꿔줌

    # 실제 캐릭터 위치정보에 반영
    character_x_pos += to_x * dt  # FPS가 달라져도 속도가 일정하게 유지되도록
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect() # 사각형상 정보를 가져옴
    character_rect.left = character_x_pos # 현재 위치로 좌측 상단 위치 업데이트
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background,(0,0)) # 배경에 파일 불러오기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 불러오기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # enemy 불러오기

    # 타이머 넣기
    # 경과시간 계산 - 현재 tick을 받아 시작 tick을 빼고, 1000을 나누어 초단위로 환산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # render(출력할 문자, True, 색상)
    screen.blit(timer, (10,10))
    # 만약 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0: # 만약 시간이 
        print('타임아웃')
        running = False

    pygame.display.update() # 화면 다시그리기 - 항상 포함되어야 하는 내용

# 종료 전 잠시대기
pygame.time.delay(2000)

# pygmae 종료
pygame.quit()