# Spritesheet Font
Generowanie tekstu na podstawie czicionki w pliku z duszkami.
![Aplikacja](screen.png)

## Technologie
- Python
- PyGame

## Duszki
Znaki wchodzące w skład czcionki należy zapisać w pliku w formacie `*.png` w katalogu `Assets/Fonts`. Znaki w pliku znajdują się w siatce, gdzie w każdym pojedynczym polu siatki znajduje się jeden znak.

<figure>
  <figcaption>fontmain.png</figcaption>
  <img src="Assets/Fonts/fontmain.png" alt="fontmain.png">
</figure>

<figure>
  <figcaption>fontlight.png</figcaption>
  <img src="Assets/Fonts/fontlight.png" alt="fontlight.png">
</figure>

## Klasa `Font`

### Konstruktor

```python
__init__(
    self,
    font: str = "fontlight",
    width: int = 7,
    height: int = 8,
    scale: int = 1,
    alphabet: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?",.+-=:;$%&'
):
```

argumenty":
- `font` - nazwa pliku z czcionką ( bez formatu pliku ), domyślna czcionka `fontlight`
- `width` - szerokość znaku w pliku z czionką, domyślnie `7`
- `height` - wysokość znaku w pliku z czionką, domyślnie `8`
- `scale` - skala czionki, domyślnie `1` - oryginalny rozmiar
- `alphabet` - ciąg znakowy z domyślnym alfabetem, kolejność znakó musi odpowiadać kolejnośći znaków w pliku graficznym od lewej do prawej, wiersz po wierszu, domyślny alfabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?",.+-=:;$%&`

## Jak użyć
Skrypt korzysta z klas `Asset` oraz `Sprites`. Klasa `Asset` wczytuje pliki z katalogu `Assets`, klasa `Sprites` tnie plik graficzny na pojedyczne duszki i umieszcza je w tablicy.

### Import klasy `Font`
```python
from App.Font import Font
```

### Utworzenie obiektu `Font`
```python
font
