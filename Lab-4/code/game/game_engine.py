import pygame
from game.maze import generate_maze, CELL
from game.entities import Player, Enemy

COLS, ROWS = 13, 11
WIDTH = COLS * CELL
HEIGHT = ROWS * CELL + 50
FPS = 60

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Chase")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 22)
        self.big_font = pygame.font.SysFont("monospace", 38, bold=True)
        self.reset()

    def reset(self):
        self.walls = generate_maze(COLS, ROWS)
        self.player = Player(0, 0)
        # Task 1: 3 independent enemies starting at different maze corners
        self.enemies = [
            Enemy(ROWS - 1, COLS - 1, color=(220, 60, 60)),  # Bottom-right
            Enemy(0, COLS - 1, color=(240, 100, 40)),        # Top-right
            Enemy(ROWS - 1, 0, color=(190, 40, 140))         # Bottom-left
        ]
        self.enemy = self.enemies[0]
        self.exit_rect = pygame.Rect((COLS//2)*CELL+5, (ROWS//2)*CELL+5, CELL-10, CELL-10)
        self.caught = False
        self.won = False
        self.start_ticks = pygame.time.get_ticks()
        self.speed_tier = 1
        # Task 3: Power Pellet placed in central maze area
        pellet_c, pellet_r = COLS // 2, 1
        self.pellet_rect = pygame.Rect(pellet_c * CELL + CELL//4, pellet_r * CELL + CELL//4, CELL//2, CELL//2)
        self.pellet_active = True
        # Task 4: Survival score
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r: self.reset()
        return True

    def update(self):
        if self.caught or self.won: return
        # Task 4: Increment survival score each frame alive
        self.score += 1
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.walls, ROWS, COLS)

        # Task 2: Difficulty ramp - increase speed every 15 seconds
        elapsed_sec = (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.speed_tier = 1 + (elapsed_sec // 15)
        new_interval = max(5, 20 - (self.speed_tier - 1) * 2)

        for enemy in self.enemies:
            enemy.move_interval = new_interval
            enemy.update(self.walls, self.player, ROWS, COLS)
            if self.player.rect.colliderect(enemy.rect):
                self.caught = True
                break
        # Task 3: Check power pellet collision (freeze enemies for 300 frames)
        if self.pellet_active and self.player.rect.colliderect(self.pellet_rect):
            self.pellet_active = False
            for enemy in self.enemies:
                enemy.frozen = True
                enemy.freeze_timer = 300

        if self.player.rect.colliderect(self.exit_rect):
            self.won = True

    def draw(self):
        self.screen.fill((230, 220, 210))
        wc=(50,40,60)
        for r in range(ROWS):
            for c in range(COLS):
                x,y=c*CELL,r*CELL
                w=self.walls[r][c]
                if w[0]: pygame.draw.line(self.screen,wc,(x,y),(x+CELL,y),3)
                if w[1]: pygame.draw.line(self.screen,wc,(x,y+CELL),(x+CELL,y+CELL),3)
                if w[2]: pygame.draw.line(self.screen,wc,(x+CELL,y),(x+CELL,y+CELL),3)
                if w[3]: pygame.draw.line(self.screen,wc,(x,y),(x,y+CELL),3)
        pygame.draw.rect(self.screen,(80,200,80),self.exit_rect,border_radius=4)
        lbl=self.font.render("EXIT",True,(20,80,20))
        self.screen.blit(lbl,(self.exit_rect.x+2,self.exit_rect.y+6))
        # Task 3: Draw power pellet if active
        if self.pellet_active:
            pygame.draw.circle(self.screen, (255, 215, 0), self.pellet_rect.center, CELL//4)
            pygame.draw.circle(self.screen, (255, 255, 200), self.pellet_rect.center, CELL//6)
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        hud=pygame.Rect(0,ROWS*CELL,WIDTH,50)
        pygame.draw.rect(self.screen,(30,30,50),hud)
        survived_sec = self.score // 60
        info=self.font.render(f"Survived: {survived_sec}s | Score: {self.score}",True,(255,255,255))
        tier_info=self.font.render(f"Tier {self.speed_tier}",True,(255,180,60))
        self.screen.blit(info,(8,ROWS*CELL+14))
        self.screen.blit(tier_info,(WIDTH - tier_info.get_width() - 8, ROWS*CELL+14))
        if self.caught:
            self._overlay("CAUGHT!", (220,60,60))
        if self.won:
            self._overlay("ESCAPED!", (80,220,80))
        pygame.display.flip()

    def _overlay(self, text, color):
        surf=pygame.Surface((WIDTH,ROWS*CELL),pygame.SRCALPHA)
        surf.fill((0,0,0,140))
        self.screen.blit(surf,(0,0))
        msg=self.big_font.render(text,True,color)
        score_txt=self.font.render(f"Survived: {self.score // 60}s  |  Final Score: {self.score}",True,(255,230,100))
        sub=self.font.render("Press R to Restart",True,(200,200,200))
        self.screen.blit(msg,(WIDTH//2-msg.get_width()//2,ROWS*CELL//2-45))
        self.screen.blit(score_txt,(WIDTH//2-score_txt.get_width()//2,ROWS*CELL//2+5))
        self.screen.blit(sub,(WIDTH//2-sub.get_width()//2,ROWS*CELL//2+40))

    def run(self):
        running=True
        while running:
            running=self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
