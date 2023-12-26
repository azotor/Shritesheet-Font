import pygame, os

class Asset:

    def __init__( self, type: str, file: str ):
        self.image = pygame.image.load( os.path.join( "Assets", type, file ) ).convert_alpha()