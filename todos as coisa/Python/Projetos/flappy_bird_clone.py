import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Definindo constantes
WIDTH, HEIGHT = 400, 600
FPS = 50 
GRAVITY = 0.5
FLAP_STRENGTH = 10
BIRD_WIDTH, BIRD_HEIGHT = 30, 30
OBSTACLE_WIDTH = 70

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializando a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')

# Inicializando fontes
font = pygame.font.SysFont('Arial', 30)

# Função para exibir o menu de dificuldade
def show_difficulty_menu():
    """Exibe o menu de seleção de dificuldade e retorna a dificuldade escolhida."""
    while True:
        screen.fill(BLACK)
        title_surface = font.render('Selecione a Dificuldade:', True, WHITE)
        easy_surface = font.render('1. Fácil', True, WHITE)
        medium_surface = font.render('2. Médio', True, WHITE)
        hard_surface = font.render('3. Difícil', True, WHITE)

        screen.blit(title_surface, (50, 100))
        screen.blit(easy_surface, (50, 200))
        screen.blit(medium_surface, (50, 250))
        screen.blit(hard_surface, (50, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 3  # Velocidade dos obstáculos e gravidade para dificuldade fácil
                elif event.key == pygame.K_2:
                    return 5  # Dificuldade média
                elif event.key == pygame.K_3:
                    return 7  # Dificuldade difícil

# Função para exibir contagem regressiva
def countdown(seconds):
    """Exibe uma contagem regressiva de segundos no início do jogo."""
    for second in range(seconds, 0, -1):
        screen.fill(BLACK)
        countdown_surface = font.render(f'Iniciando em: {second}', True, WHITE)
        screen.blit(countdown_surface, (50, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(1000)  # Espera 1 segundo

# Classe do Pássaro
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.vel_y = 0

    def flap(self):
        """Faz o pássaro voar para cima."""
        self.vel_y = -FLAP_STRENGTH

    def update(self):
        """Atualiza a posição do pássaro considerando a gravidade."""
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def draw(self):
        """Desenha o pássaro na tela."""
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Classe do Obstáculo
class Obstacle:
    def __init__(self, speed):
        self.width = OBSTACLE_WIDTH
        self.gap = 150
        self.x = WIDTH
        self.height_top = random.randint(50, HEIGHT - self.gap - 50)
        self.height_bottom = HEIGHT - self.height_top - self.gap
        self.speed = speed
        self.color = (0, 255, 0)  # Cor inicial

    def update(self):
        """Atualiza a posição do obstáculo."""
        self.x -= self.speed

    def draw(self):
        """Desenha o obstáculo na tela."""
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.height_top))
        pygame.draw.rect(screen, self.color, (self.x, HEIGHT - self.height_bottom, self.width, self.height_bottom))

# Função para mostrar a pontuação
def draw_score(score):
    """Desenha a pontuação na tela."""
    score_surface = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surface, (10, 10))

# Função para verificar colisões
def check_collision(bird, obstacles):
    """Verifica se o pássaro colidiu com algum obstáculo."""
    for obstacle in obstacles:
        if (bird.x + bird.width > obstacle.x and bird.x < obstacle.x + obstacle.width):
            if (bird.y < obstacle.height_top or bird.y + bird.height > HEIGHT - obstacle.height_bottom):
                return True
    return False

# Função principal
def main():
    clock = pygame.time.Clock()
    speed = show_difficulty_menu()  # Obter a dificuldade selecionada
    bird = Bird()
    obstacles = []
    score = 0
    frame_count = 0
    obstacle_speed = 5 + speed  # Obtenha a velocidade inicial com base na dificuldade

    # Contagem regressiva antes de começar o jogo
    countdown(5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()

        bird.update()

        # Adiciona um novo obstáculo a cada 90 quadros
        if frame_count % 90 == 0:
            obstacles.append(Obstacle(obstacle_speed))

        # Atualiza obstáculos e verifica a pontuação
        obstacles = [obstacle for obstacle in obstacles if obstacle.x >= 0]  # Remove obstáculos que saem da tela
        for obstacle in obstacles:
            obstacle.update()
            if obstacle.x < 0:
                score += 1

            # Variação de cores para cada 100 pontos
            if score % 100 == 0 and score != 0:
                obstacle.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Verifica colisões
        if check_collision(bird, obstacles):
            print("Game Over! Score:", score)
            pygame.quit()
            sys.exit()

        # Limpeza da tela
        screen.fill(BLACK)
        bird.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # Desenhar a pontuação
        draw_score(score)

        pygame.display.flip()
        frame_count += 1
        clock.tick(FPS)

if __name__ == "__main__":
    main()