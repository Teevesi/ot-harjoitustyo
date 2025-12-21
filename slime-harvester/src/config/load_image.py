import os
import pygame

dirname = os.path.dirname(__file__)

def load_image(filename):
    """ Helper function to load an image from the assets folder. """
    return pygame.image.load(
        os.path.join(dirname, "..", "assets", filename)
    )
