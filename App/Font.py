import pygame, math

from App.Sprites import Sprites

class Font:
    def __init__(
            self,
            font: str = "fontlight",
            width: int = 7,
            height: int = 8,
            scale: int = 1,
            alphabet: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?",.+-=:;$%&'
        ):
        self.surf = pygame.display.get_surface()
        self.sprites = Sprites( "Fonts", f"{ font }.png" )
        self.sprites.cutBySpriteSize( width, height, scale )
        self.width = width
        self.height = height
        self.scale = scale
        self.alphabet = alphabet
    
    def getByWidth( self, message: str, width: int = 0 ):
        size = [ width, self.height * self.scale ]
        if size[ 0 ] == 0:
            size[ 0 ] = len( message ) * self.width * self.scale
        else:
            w = math.ceil( len( message ) * self.width * self.scale / width )
            size[ 1 ] = w * self.height * self.scale

        gridsX = width // ( self.height * self.scale )

        surf = pygame.Surface( size ).convert_alpha()
        surf.fill( 'black' )

        for i in range( len( message ) ):
            if message[ i ] != " ":
                ind = self.alphabet.index( message[ i ] )
                x = ( i % gridsX  if gridsX > 0 else i ) * self.width * self.scale
                y = ( i // gridsX if gridsX > 0 else 0 ) * self.width * self.scale
                surf.blit( self.sprites.get( ind ), ( x, y ) )
        
        surf.set_colorkey( 'black' )

        return surf

    def render( self, message: str, pos, align = ( -1, -1 ), width:int = 0 ):
        surf = self.getByWidth( message, width )
        rect = surf.get_rect( topleft = pos )

        match align[ 0 ]:
            case 0:
                rect.left -= rect[ 2 ] / 2
            case 1:
                rect.left -= rect[ 2 ]

        match align[ 1 ]:
            case 0:
                rect.top -= rect[ 3 ] / 2
            case 1:
                rect.top -= rect[ 3 ]
                
        self.surf.blit( surf, rect )
    
    def renderByGridsX( self, message: str, pos, align = ( -1, -1 ), gridsX:int = 0 ):
        self.render( message, pos, align, gridsX * self.width * self.scale )
