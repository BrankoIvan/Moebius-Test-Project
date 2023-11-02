#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Iniciaciones

define Protagonista = Character("", color = "#ff9100", what_prefix = "{k=3}", what_suffix = "{/k}")
define Narrador = Character("", color = "#008cff",what_color="#bdbcfb", what_prefix = "{k=3}{i}", what_suffix = "{/k}{/i}")
define Conductor = Character("Conductor", color = "#0aff1e8c",what_prefix = "{cps=80}", what_suffix = "{/cps}")

define karma = 0
define capitulo = 1

define opcionElegida = 0

label start:
    scene black
    show inventario    
    jump intro
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Definicion de Items e Interactuables

define cartel = Interactuable(exCartel, (111,47), exCartelCerca, "descripcionCartel")

define cigarrillos = Item(exCigarrillos, (151,826), exCigarrillosCerca, "descripcionCigarrillos", exCigarrillosInventario)

label descripcionCartel:

    Narrador " -REEMPLAZAR POR FAVOR- El cartel esta en blanco"

    return

label descripcionCigarrillos:

    "agarrar"

    menu:
        "si":
            $ cigarrillos.agregarAlInvetario()
        
        "no":
            pass

    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Mapa

label vagon:
    scene bg vagon
    
    show screen nombreDeHabitacion("Vagon") 

    if capitulo in [1]:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1
    
    call screen flechasDeNavegacion("cabina","","","andenCentro")

label cabina:
    scene bg cabina

    if capitulo in [2]:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    $ cigarrillos.mostrar()
    call screen flechasDeNavegacion("","","vagon","")

label andenCentro:
    scene bg anden centro
    if capitulo in [3]:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1
    
    $ cartel.mostrar()
    call screen flechasDeNavegacion("andenDerecha","vagon","","tunel2")

label tunel2:
    scene bg tunel2
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1
    
    $ cartel.mostrar()
    call screen flechasDeNavegacion("tunelCerrado","","andenCentro","")

label andenDerecha:
    scene bg anden derecho
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    call screen flechasDeNavegacion("andenFinalDerecho","","andenCentro","tunel")

label andenFinalDerecho:
    scene bg anden final derecho
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    call screen flechasDeNavegacion("","vias","andenDerecha","")

label baño:
    scene bg baño
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    call screen flechasDeNavegacion("","","andenFinalDerecho","")

label vias:
    scene black

    "esta demasiado oscuro"

    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    jump andenFinalDerecho

label tunelCerrado:
    scene bg tunel cerrado

    "TEXTO"

    label .navegacion:

        if capitulo in []:
            $ renpy.call("escena" + str(capitulo))
            $ capitulo += 1

        call screen flechasDeNavegacion("","","andenCentro","")

label tunel:
    scene bg tunel
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1
    
    call screen flechasDeNavegacion("escalera","","andenDerecha","")

label escalera:
    scene bg escalera
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    show seguridad

    "dame cigarrillos"

    menu:
        "dar" if cigarrillos.estaEnInventario():
            $ cigarrillos.sacarDelInvetario()
        
        "...":
            pass

    call screen flechasDeNavegacion("salidaCerrada","","tunel","")

label salidaCerrada:
    scene bg salida cerrada
    if capitulo in []:
        $ renpy.call("escena" + str(capitulo))
        $ capitulo += 1

    call screen flechasDeNavegacion("","","escalera","")

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Historia

label intro:
    scene bg ojos cerrados
    # $ renpy.notify("intro")
    
    scene bg despertar

    menu:

        Narrador " -REEMPLAZAR POR FAVOR- Sentis el vagon frenar levemente"

        "Ponerse de pie":
            jump vagon
        
        "Seguir durmiendo":
            pass
        
    Narrador " -REEMPLAZAR POR FAVOR- Estas muy cansado, decidis dormir un poco mas"
    Narrador " -REEMPLAZAR POR FAVOR- Describir el nivel de cansancio"

    menu:
        
        Narrador " -REEMPLAZAR POR FAVOR- Sentis el vagon frenar levemente"

        "Ponerse de pie":
            jump vagon
        
        "Seguir durmiendo":
            pass
    
    Narrador " -REEMPLAZAR POR FAVOR- Estas demasiado cansado, decidis dormir un poco mas"

    menu:
        
        Narrador " -REEMPLAZAR POR FAVOR- Sentis el vagon frenar levemente"
        
        "Seguir durmiendo":
            pass
    
    scene black

    Narrador " -REEMPLAZAR POR FAVOR- Seguiste durmiendo"

    return

label escena1:
    Narrador " -REEMPLAZAR POR FAVOR- Te lavantas"
    Narrador " -REEMPLAZAR POR FAVOR- Notas que las puertas estan cerradas"
    Narrador " -REEMPLAZAR POR FAVOR- Te acercas a la cabina"
    
    return

label escena2:
    Protagonista " -REEMPLAZAR POR FAVOR- Le haces una pregunta al conductor"
    Conductor " -REEMPLAZAR POR FAVOR- CARAMELOS"
    Protagonista " -REEMPLAZAR POR FAVOR- Le haces una pregunta al conductor"
    Conductor " -REEMPLAZAR POR FAVOR- CARAMELOS"
    Protagonista " -REEMPLAZAR POR FAVOR- Le haces una pregunta al conductor"
    Conductor " -REEMPLAZAR POR FAVOR- CARAMELOS"

    Protagonista " -REEMPLAZAR POR FAVOR- Caramelos?"
    
    Narrador " -REEMPLAZAR POR FAVOR- Sonido de puerta abriendose"
    
    return

label escena3:
    Narrador " -REEMPLAZAR POR FAVOR- La puerta esta abierta"
    return

label escena4:
    Narrador " -REEMPLAZAR POR FAVOR- La puerta esta abierta"
    return

# Implementar que cada escena te diga cuanto capitulos se tiene que avanzar