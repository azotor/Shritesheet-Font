import pygame

from App.Asset import Asset

class Sprites:
    def __init__( self, type: str, file: str ):
        self.asset = Asset( type, file )
        self.sprites = []

    def cutBySpriteSize( self, width: int, height: int , scale: int = 1 ):
        gridsX = self.asset.image.get_width() // width
        for i in range( width * height ):
            surf = pygame.Surface( ( width, height ) )
            surf.fill( ( 0, 0, 0 ) )
            surf.blit( self.asset.image, ( 0, 0 ), ( i % gridsX * width, i // gridsX * height, width, height ) )
            if scale != 1:
                surf = pygame.transform.scale( surf, ( width * scale, height * scale ) )
            surf.set_colorkey( ( 0, 0, 0 ) )
            self.sprites.append( surf )

    def get( self, id: int ):
        return self.sprites[ id ]