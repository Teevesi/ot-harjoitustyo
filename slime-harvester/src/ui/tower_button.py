import pygame

class TowerButton:
    """
    Represents a button in the UI for selecting and placing a tower.
    """
    def __init__(self, image, position, tower_type):
        self.image = image
        self.position = position
        self.tower_type = tower_type
        self.size = 56
        self.rect = pygame.Rect(position[0], position[1], self.size, self.size)
        self.background = pygame.Surface((self.size, self.size))
        self.background.set_alpha(180)
        self.background.fill((0, 0, 0))

    def draw(self, surface):
        """ Draws the tower button. """
        mouse_pos = pygame.mouse.get_pos()

        if self.is_hovering(mouse_pos):
            highlight = pygame.Surface((self.size, self.size))
            highlight.set_alpha(180)
            highlight.fill((255, 255, 255))
            surface.blit(highlight, self.position)

        surface.blit(self.background, self.position)
        scaled_image = pygame.transform.scale(self.image, (self.size, self.size))
        surface.blit(scaled_image, self.position)

    def is_hovering(self, mouse_pos):
        """ checks if mouse is hovering the tower button. """
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event, start_dragging):
        """ handles mouse events for the tower button. """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # pylint: disable=no-member
            if self.is_hovering(event.pos):
                start_dragging(self.tower_type)
