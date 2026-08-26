@namespace
class SpriteKind:
    Ground = SpriteKind.create()
    P = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.P, SpriteKind.food, on_on_overlap)

def on_a_pressed():
    global X
    if X == 80 or X == 10:
        X = X + 70
        Cell.set_position(X, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    global X
    if X == 150 or X == 80:
        X = X - 70
        Cell.set_position(X, 100)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

X2 = 0
Laser_beam: Sprite = None
T = 0
X = 0
Cell: Sprite = None
Laser1 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 9 9 9 8 8 8 6 6 6 8 8 8 9 9 9
        . . 8 6 1 6 1 8 9 8 1 6 1 6 8 .
        . . . 9 6 1 6 9 8 9 6 1 6 9 . .
        . . . 6 9 6 9 1 9 1 9 6 9 6 . .
        . . . 9 6 9 6 8 8 8 6 9 6 9 . .
        . . . 6 9 6 9 9 9 9 9 6 9 6 . .
        . . . 8 6 9 6 8 6 8 6 9 6 8 . .
        . . . . 9 6 9 6 8 6 9 6 9 . . .
        . . . . . 8 6 9 9 9 6 8 . . . .
        . . . . . . 9 6 8 6 9 . . . . .
        . . . . . . . 8 9 8 . . . . . .
        . . . . . . . . 8 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.projectile)
Laser1.set_position(10, 7)
Laser2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 9 9 9 8 8 8 6 6 6 8 8 8 9 9 9
        . . 8 6 1 6 1 8 9 8 1 6 1 6 8 .
        . . . 9 6 1 6 9 8 9 6 1 6 9 . .
        . . . 6 9 6 9 1 9 1 9 6 9 6 . .
        . . . 9 6 9 6 8 8 8 6 9 6 9 . .
        . . . 6 9 6 9 9 9 9 9 6 9 6 . .
        . . . 8 6 9 6 8 6 8 6 9 6 8 . .
        . . . . 9 6 9 6 8 6 9 6 9 . . .
        . . . . . 8 6 9 9 9 6 8 . . . .
        . . . . . . 9 6 8 6 9 . . . . .
        . . . . . . . 8 9 8 . . . . . .
        . . . . . . . . 8 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.projectile)
Laser2.set_position(80, 7)
Laser3 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        . 9 9 9 8 8 8 6 6 6 8 8 8 9 9 9
        . . 8 6 1 6 1 8 9 8 1 6 1 6 8 .
        . . . 9 6 1 6 9 8 9 6 1 6 9 . .
        . . . 6 9 6 9 1 9 1 9 6 9 6 . .
        . . . 9 6 9 6 8 8 8 6 9 6 9 . .
        . . . 6 9 6 9 9 9 9 9 6 9 6 . .
        . . . 8 6 9 6 8 6 8 6 9 6 8 . .
        . . . . 9 6 9 6 8 6 9 6 9 . . .
        . . . . . 8 6 9 9 9 6 8 . . . .
        . . . . . . 9 6 8 6 9 . . . . .
        . . . . . . . 8 9 8 . . . . . .
        . . . . . . . . 8 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.projectile)
Laser3.set_position(150, 7)
Cell = sprites.create(img("""
        . . a d d d a c a d d d a . . .
        . . d 1 c b c a c b c 1 d . . .
        . . d c b d b b b d b c d . . .
        . . d b d c d d d c d b d . . .
        . . a c b d b 1 b d b c a . . .
        . . c a b d 1 c 1 d b a c . . .
        . . a c b d b 1 b d b c a . . .
        . . d b d c d d d c d b d . . .
        . . d c b d b b b d b c d . . .
        . . d 1 c b c a c b c 1 d . . .
        . . a d d d a c a d d d a . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
X = 80
Cell.set_position(X, 100)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.food)
mySprite.set_position(80, 100)
a = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.food)
a.set_position(10, 100)
b = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.food)
b.set_position(150, 100)

def on_on_update():
    global T
    T = 0
game.on_update(on_on_update)

def on_update_interval():
    global Laser_beam, X2, T
    Laser_beam = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . 8 . . . . . . . . . 8 . .
            . . . 8 9 . . . . . . . 9 8 . .
            . . . 8 9 6 . . . . . 6 9 8 . .
            . . . 8 9 6 9 . . . 9 6 9 8 . .
            . . . 8 9 6 9 9 . 9 9 6 9 8 . .
            . . . 8 9 6 9 9 8 9 9 6 9 8 . .
            . . . 8 9 6 9 9 8 9 9 6 9 8 . .
            . . . 8 9 6 9 9 8 9 9 6 9 8 . .
            . . . . 8 6 9 9 8 9 9 6 8 . . .
            . . . . . 8 9 9 8 9 9 8 . . . .
            . . . . . . 8 8 8 8 8 . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.P)
    X2 = randint(0, 3)
    if T <= 2:
        if X2 == 1:
            Laser_beam.set_position(10, 13)
        elif X2 == 2:
            Laser_beam.set_position(80, 13)
        else:
            Laser_beam.set_position(150, 13)
        Laser_beam.set_velocity(0, 50)
        T = T + 1
    if T >= 5:
        if T <= 3:
            if X2 == 1:
                Laser_beam.set_position(10, 13)
            elif X2 == 2:
                Laser_beam.set_position(80, 13)
            else:
                Laser_beam.set_position(150, 13)
            Laser_beam.set_velocity(0, 75)
        T = T + 1
    if T < 5:
        Laser_beam.set_velocity(0, 100)
        if X2 == 1:
            Laser_beam.set_position(10, 13)
        elif X2 == 2:
            Laser_beam.set_position(80, 13)
        else:
            Laser_beam.set_position(150, 13)
        T = T + 1
game.on_update_interval(500, on_update_interval)
