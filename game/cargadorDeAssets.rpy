#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Rutas
define backgrounds = "images/bg/"
define extras = "images/interactuables/"
define sprites = "images/sprites/"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Sprites

image seguridad:
    sprites + "NPC_SEGURIDAD.png"
    xzoom 1.0 yzoom 1.0
    xalign 0.5 yalign 1.9

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fondos

image bg vagon = backgrounds + "bg vagon1.jpg"
image bg cabina = backgrounds + "bg vagon2.jpg"
image bg anden centro = backgrounds + "bg anden.jpg"
image bg anden derecho = backgrounds + "bg anden2.jpg"
image bg anden final derecho = backgrounds + "bg final del anden.jpg"
image bg tunel cerrado = backgrounds + "bg puerta cerrada.jpg"
image bg tunel = backgrounds + "bg tunel.jpg"
image bg escalera = backgrounds + "bg escalera.jpg"
image bg despertar = backgrounds + "bg despertar.jpg"
image bg salida cerrado = backgrounds + "bg puerta cerrada.jpg"

image bg ojos cerrados = Movie(play = backgrounds + "ojos_cerrados.webm")

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Extras

define exCigarrillos = extras + "cigarrillos_%s.png"
define exCigarrillosCerca = extras + "cigarrillos_ui.png"
define exCigarrillosInventario = extras + "cigarrillos_ui.png"

define exCartel = extras + "cartel_%s.png"
define exCartelCerca = extras + "cartel.png"


