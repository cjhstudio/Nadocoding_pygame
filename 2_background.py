import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game') # 상단 창 이름에 들어가는 제목

# 배경이미지 불러오기
background = pygame.image.load("background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 이벤트 발생 체크. 항상 설정하는 세팅
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False # 게임이 진행중이 아님 - while 문 빠져나옴
    
    #screen.fill((0,0,255)) # 화면을 RGB 컬러로 채우기만 할 때
    screen.blit(background,(0,0)) # 배경에 파일 불러오기

    pygame.display.update() # 화면 다시그리기 - 항상 포함되어야 하는 내용

# pygmae 종료
pygame.quit()