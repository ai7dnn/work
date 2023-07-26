import pygame
import random

# 게임 화면 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 블록 크기
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20

# 패들 크기
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10

# 공 크기
BALL_RADIUS = 8

# 게임 속도 설정
FPS = 60

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker")

# 시계 설정
clock = pygame.time.Clock()

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

def draw_paddle():
    pygame.draw.rect(screen, GREEN, paddle)

def draw_ball():
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), BALL_RADIUS)

def check_collision():
    global ball_speed_x, ball_speed_y, score

    # 패들과 충돌 체크
    if ball_y >= SCREEN_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS and \
       paddle.left <= ball_x <= paddle.right:
        ball_speed_y = -ball_speed_y

    # 벽돌과 충돌 체크
    for block in blocks[:]:
        if block.collidepoint(ball_x, ball_y):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y
            score += 10

    # 벽과 충돌 체크
    if ball_x <= BALL_RADIUS or ball_x >= SCREEN_WIDTH - BALL_RADIUS:
        ball_speed_x = -ball_speed_x

    if ball_y <= BALL_RADIUS:
        ball_speed_y = -ball_speed_y

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over - Score: {}".format(score), True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)

# 벽돌 초기화
blocks = []
for row in range(5):
    for col in range(10):
        block = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

# 패들 초기화
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 초기화
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = random.choice([-5, 5])
ball_speed_y = -5

# 점수 초기화
score = 0

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.left -= 5
    if keys[pygame.K_RIGHT]:
        paddle.left += 5

    # 화면 초기화
    screen.fill(WHITE)

    # 블록 그리기
    draw_blocks()

    # 패들 그리기
    draw_paddle()

    # 공 그리기
    draw_ball()

    # 충돌 체크
    check_collision()

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 화면 업데이트
    pygame.display.update()

    # 게임 속도 설정
    clock.tick(FPS)

    # 게임 오버 체크
    if ball_y >= SCREEN_HEIGHT:
        game_over()
        running = False

# 게임 종료
pygame.quit()
