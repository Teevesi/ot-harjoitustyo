"""Game state management - pure game logic without rendering.

This module contains the GameState class which manages all game entities
and logic without pygame rendering concerns. It can be unit tested and
used independently of the visual layer.
"""

from settings import MAP_NAME, MAX_HEALTH, TILE_SIZE
from enemies.enemy_path import EnemyPath
from enemies.enemy_timing import Timer
from enemies.enemy_manager import EnemyManager
from player_stats import HealthBar, Currency
from defences.tower1 import Tower1
from defences.tower2 import Tower2


class GameState:
    """Manages game entities and logic without rendering.
    
    Attributes:
        towers: List of all towers in the game
        enemies: List of all enemies (via enemy_manager)
        projectiles: List of all projectiles
        hp_bar: Player health bar
        currency: Player currency
        timer: Game timer
        running: Whether the game is active
    """

    def __init__(self):
        """Initialize game state with default values."""
        self.timer = Timer()
        self.hp_bar = HealthBar(MAX_HEALTH)
        self.currency = Currency(100)
        self.enemy_path = EnemyPath(MAP_NAME, TILE_SIZE)
        self.projectiles = []
        self.towers = []
        self.running = False
        
        # Enemy manager (logic-only)
        self.enemy_manager = EnemyManager(
            self.timer,
            self.enemy_path,
            self.hp_bar
        )
        
        # Selected tower for placement
        self.selected_tower_type = None

    def start_game(self):
        """Start the game and initialize enemy path."""
        self.running = True
        self.enemy_path.get_path(self.enemy_path.map_data)

    def is_game_over(self):
        """Check if game is over (player health <= 0).
        
        Returns:
            bool: True if game is over
        """
        return self.hp_bar.current_health() <= 0

    def update(self):
        """Update all game entities (enemies, towers, projectiles, collisions)."""
        if self.enemy_manager:
            self.enemy_manager.add_enemies()
            self.enemy_manager.update_enemies()

        self._update_towers()
        self._update_projectiles()
        self._check_collisions()
        self.timer.update()

    def _update_towers(self):
        """Update all towers and handle shooting."""
        for tower in self.towers:
            new_projectiles = []
            if tower.can_shoot(self.timer.get_real_timer()):
                if tower.__class__.__name__ == "Tower1":
                    new_projectiles = tower.shoot("left", self.timer.get_real_timer())
                elif tower.__class__.__name__ == "Tower2":
                    new_projectiles = tower.shoot(self.timer.get_real_timer())
                if new_projectiles:
                    self.projectiles.extend(new_projectiles)
            tower.update(self.timer.get_real_timer())

    def _update_projectiles(self):
        """Update projectile positions and remove expired ones."""
        # Remove projectiles that exceeded range
        self.projectiles[:] = [
            p for p in self.projectiles 
            if p and not p.has_exceeded_range()
        ]
        
        # Update remaining projectiles
        for projectile in self.projectiles:
            if projectile:
                projectile.update()

    def _check_collisions(self):
        """Check and handle projectile-enemy collisions."""
        to_remove = []
        
        if not self.enemy_manager:
            return
            
        for projectile in self.projectiles:
            for enemy in self.enemy_manager.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    self.enemy_manager.remove(enemy)
                    to_remove.append(projectile)
                    self.currency.increase(1)
                    break
        
        # Remove collided projectiles
        for projectile in to_remove:
            if projectile in self.projectiles:
                self.projectiles.remove(projectile)

    def add_tower(self, tower_type, position):
        """Add a tower at the specified position if player has enough currency.
        
        Args:
            tower_type: String identifier for tower type ("Tower1", "Tower2")
            position: Tuple (x, y) in pixel coordinates
            
        Returns:
            bool: True if tower was successfully placed
        """
        # Create the tower instance
        new_tower = None
        if tower_type == "Tower1":
            new_tower = Tower1(position)
        elif tower_type == "Tower2":
            new_tower = Tower2(position)
        
        if not new_tower:
            return False
        
        # Check if player can afford it
        if self.currency.current_amount() >= new_tower.stats.price:
            self.currency.decrease(new_tower.stats.price)
            self.towers.append(new_tower)
            return True
        
        return False

    def can_place_tower_at(self, tile_x, tile_y, tilemap):
        """Check if a tower can be placed at the given tile coordinates.
        
        Args:
            tile_x: Tile x coordinate
            tile_y: Tile y coordinate
            tilemap: TileMap instance to check tile availability
            
        Returns:
            bool: True if tower can be placed
        """
        # Check if tile is free (not blocked)
        if not tilemap.tile_is_free(tile_x, tile_y):
            return False
        
        # Check if another tower is already at this position
        grid_x = tile_x * TILE_SIZE + TILE_SIZE // 2
        grid_y = tile_y * TILE_SIZE + TILE_SIZE // 2
        
        for tower in self.towers:
            if tower.position == (grid_x, grid_y):
                return False
        
        return True

    def select_tower(self, tower_type):
        """Select a tower type for placement.
        
        Args:
            tower_type: String identifier for tower type
        """
        self.selected_tower_type = tower_type

    def clear_tower_selection(self):
        """Clear the currently selected tower."""
        self.selected_tower_type = None

    def get_tower_count(self):
        """Get the number of towers placed.
        
        Returns:
            int: Number of towers
        """
        return len(self.towers)

    def get_enemy_count(self):
        """Get the number of active enemies.
        
        Returns:
            int: Number of enemies
        """
        if self.enemy_manager:
            return len(self.enemy_manager.enemies)
        return 0

    def get_projectile_count(self):
        """Get the number of active projectiles.
        
        Returns:
            int: Number of projectiles
        """
        return len(self.projectiles)
