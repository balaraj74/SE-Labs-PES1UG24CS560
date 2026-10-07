# PES UNIVERSITY — DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
## Software Engineering Lab (UE24CS242) — Lab 4: VibeCoding
**Student Name:** Balaraj R  
**SRN:** PES1UG24CS560  
**Semester & Branch:** 4th Semester, B.Tech CSE (AI & ML)  
**Assigned Repository:** `https://github.com/SETAPESU26/11_maze_chase`  
**Date:** October 7, 2026  

---

### Prompt 1: Bug Fix — Player Wall Collision Enforcement
**Goal:** Fix defect where player passes through solid maze walls.  
**Prompt:**
```text
In game/entities.py, the Player._valid method only checks outer grid boundaries and completely ignores walls, allowing the player to walk through solid maze walls. Refactor _valid to inspect the 4-bit wall bitmask (top, bottom, right, left) for all cells overlapping the player bounding box and block invalid wall crossings.
```
**Outcome:** Updated `Player._valid` with boundary checks and 4-way wall collision detection.  
**Git Commit:** `5de6c0c fix: enforce wall collision boundaries for player movement`

---

### Prompt 2: Task 1 — Multiple Enemies with Independent BFS
**Goal:** Spawn 2 additional enemies at corners that chase player independently.  
**Prompt:**
```text
In my maze-chase pygame game, I have one Enemy that uses BFS to chase the player. Add two more Enemy instances starting at different maze corners. Each should independently call bfs() on every update. List them in a self.enemies list and loop over them.
```
**Outcome:** Created `self.enemies` list in `GameEngine` spawning at `(ROWS-1, COLS-1)`, `(0, COLS-1)`, and `(ROWS-1, 0)` with distinctive colors.  
**Git Commit:** `90e75a3 feat: add multiple independent BFS enemies at maze corners`

---

### Prompt 3: Task 2 — Speed Up Over Time (Difficulty Ramp)
**Goal:** Dynamically scale enemy speed every 15 seconds and show speed tier in HUD.  
**Prompt:**
```text
Add a difficulty ramp to my maze-chase game. Track elapsed time with pygame.time.get_ticks(). Every 15 seconds, reduce enemy.move_interval by 2 (minimum 5). Show current enemy speed tier in the HUD.
```
**Outcome:** Monitored elapsed ticks, computed `self.speed_tier = 1 + (elapsed_sec // 15)`, reduced interval down to 5 frames, and updated bottom HUD.  
**Git Commit:** `cec76bf feat: implement 15-second dynamic enemy speed ramp and HUD tier display`

---

### Prompt 4: Task 3 — Power Pellet (Freeze Enemies)
**Goal:** Spawn golden power pellet that freezes enemies for 5 seconds (300 frames).  
**Prompt:**
```text
Add a power pellet to my maze-chase game — a yellow circle somewhere in the maze. When the player rect collides with it, set enemy.frozen = True and start a 300-frame countdown. While frozen, enemy.update() does nothing. Show a frozen indicator on the enemy.
```
**Outcome:** Added collectible pellet at `(COLS//2, 1)`. When collected, freezes enemies for 300 frames, turns them icy-blue, and renders a freeze symbol.  
**Git Commit:** `d1e4f40 feat: add power pellet item with 5-second enemy freeze effect`

---

### Prompt 5: Task 4 — Survival Scoring & Game Over Overlay
**Goal:** Increment score per frame alive, display in HUD, and report on game over.  
**Prompt:**
```text
Add a survival score to maze-chase. Increment self.score by 1 each frame the player is alive. Display it in the HUD as "Survived: Xs" where X is score // 60. On game over, show the final score on the overlay.
```
**Outcome:** Added frame scoring (`self.score += 1`), rendered `Survived: Xs | Score: N` in HUD, and added final score stats to overlay screen.  
**Git Commit:** `2e3c2c1 feat: add survival score tracking and game over overlay metrics`
