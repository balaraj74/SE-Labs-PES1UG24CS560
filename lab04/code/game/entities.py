import pygame
from game.maze import CELL

SPEED = 2

class Player:
    def __init__(self, r, c):
        self.r, self.c = r, c
        cx, cy = c*CELL+CELL//2, r*CELL+CELL//2
        self.rect = pygame.Rect(cx-10, cy-10, 20, 20)
        self.color = (60, 120, 220)

    def move(self, keys, walls, rows, cols):
        dx=dy=0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx=-SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx=SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy=-SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy=SPEED
        nr = self.rect.move(dx,0)
        if self._valid(nr, walls, rows, cols): self.rect=nr
        nr = self.rect.move(0,dy)
        if self._valid(nr, walls, rows, cols): self.rect=nr

    def _valid(self, rect, walls, rows, cols):
        # Outer boundary check
        if rect.left < 2 or rect.right > cols * CELL - 2 or rect.top < 2 or rect.bottom > rows * CELL - 2:
            return False
        
        # Check wall collisions for cells covered by rect
        r_start = max(0, rect.top // CELL)
        r_end = min(rows - 1, (rect.bottom - 1) // CELL)
        c_start = max(0, rect.left // CELL)
        c_end = min(cols - 1, (rect.right - 1) // CELL)
        
        for r in range(r_start, r_end + 1):
            for c in range(c_start, c_end + 1):
                # Top wall
                if walls[r][c][0] and rect.top < r * CELL + 2:
                    return False
                # Bottom wall
                if walls[r][c][1] and rect.bottom > (r + 1) * CELL - 2:
                    return False
                # Right wall
                if walls[r][c][2] and rect.right > (c + 1) * CELL - 2:
                    return False
                # Left wall
                if walls[r][c][3] and rect.left < c * CELL + 2:
                    return False
        return True

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

class Enemy:
    def __init__(self, r, c, color=(220, 60, 60)):
        self.r, self.c = r, c
        cx, cy = c*CELL+CELL//2, r*CELL+CELL//2
        self.rect = pygame.Rect(cx-12, cy-12, 24, 24)
        self.color = color
        self.base_color = color
        self.timer = 0
        self.move_interval = 20  # frames between cell moves
        self.frozen = False
        self.freeze_timer = 0

    def update(self, walls, player, rows, cols):
        from game.maze import bfs
        # Task 3: While frozen, enemy update does nothing
        if self.frozen:
            self.freeze_timer -= 1
            if self.freeze_timer <= 0:
                self.frozen = False
            return

        self.timer += 1
        if self.timer >= self.move_interval:
            self.timer = 0
            pr, pc = player.rect.centery//CELL, player.rect.centerx//CELL
            step = bfs(walls, (self.r, self.c), (pr, pc), rows, cols)
            if step:
                dr, dc = step
                self.r += dr; self.c += dc
                cx, cy = self.c*CELL+CELL//2, self.r*CELL+CELL//2
                self.rect.center = (cx, cy)

    def draw(self, screen):
        # Task 3: Show frozen indicator and ice-blue tint
        draw_color = (100, 200, 255) if self.frozen else self.color
        pygame.draw.rect(screen, draw_color, self.rect, border_radius=5)
        # eyes
        for ex in [self.rect.x+4, self.rect.x+14]:
            pygame.draw.circle(screen, (255,255,255), (ex, self.rect.y+8), 4)
            eye_pupil = (0, 100, 200) if self.frozen else (0, 0, 0)
            pygame.draw.circle(screen, eye_pupil, (ex+1, self.rect.y+8), 2)
        if self.frozen:
            # Draw snowflake/ice symbol on enemy
            pygame.draw.circle(screen, (255, 255, 255), self.rect.center, 3)
            pygame.draw.circle(screen, (120, 220, 255), self.rect.center, 7, 1)
