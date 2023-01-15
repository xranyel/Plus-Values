label nextpage:
        $ renpy.block_rollback()
        call screen choose_route2 with dissolve

screen choose_route2:
    add "bg_choose.png"
    
    # This button will delete any persistent variable
    #button:
        #text "Clear Data": 
            #idle_color "#fff"
            #hover_color "#c0c0c0"
        #action Function(renpy.game.persistent._clear)

    #button:
     #   xpos 55
      #  ypos 650
       # text "MENU":
        #    idle_color "#fff"
         #   hover_color "#c0c0c0"
        #action ShowMenu("preferences") 
    
    imagebutton:
        xpos 40
        ypos 300
        idle "arrow2_idle.png"
        hover "arrow2_hover.png"
        action Jump("firstpage")

    # horizontal box
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30  
        spacing 20

        imagebutton:
            auto "choices/six_%s.png"
            action Jump("six_start")
            sensitive persistent.one == True and persistent.two == True and persistent.three == True and persistent.four == True and persistent.five == True

        imagebutton:
            auto "choices/seven_%s.png"
            action Jump("seven_start")
            sensitive persistent.one == True and persistent.two == True and persistent.three == True and persistent.four == True and persistent.five == True and persistent.six == True
        
        imagebutton:
            auto "choices/eight_%s.png"
            action Jump("eight_start")
            sensitive persistent.one == True and persistent.two == True and persistent.three == True and persistent.four == True and persistent.five == True and persistent.six == True and persistent.seven == True

        imagebutton:
            auto "choices/nine_%s.png"
            action Jump("nine_start")
            sensitive persistent.one == True and persistent.two == True and persistent.three == True and persistent.four == True and persistent.five == True and persistent.six == True and persistent.seven == True and persistent.eight == True