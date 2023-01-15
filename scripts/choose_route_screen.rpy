label firstpage:
        $ renpy.block_rollback()
        call screen choose_route with dissolve

screen choose_route:
    add "bg_choose.png"
    
    # This button will delete any persistent variable
    #button:
    #    text "Clear Data": 
    #        idle_color "#fff"
    #        hover_color "#c0c0c0"
    #    action Function(renpy.game.persistent._clear)

    #button:
     #   xpos 55
      #  ypos 650
       # text "MENU":
        #    idle_color "#fff"
         #   hover_color "#c0c0c0"
        #action ShowMenu("preferences") 

    imagebutton:
        xpos 1200
        ypos 300
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("nextpage")

    # horizontal box
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30  
        spacing 20

        imagebutton:
            auto "choices/one_%s.png"
            action Jump("one_start")

        imagebutton:
            auto "choices/two_%s.png"
            action Jump("two_start")
            # The imagebutton will be enabled if blue is true and disabled when at least one is false.
            sensitive persistent.one == True
       
        imagebutton:
            auto "choices/three_%s.png"
            action Jump("three_start")
            # The imagebutton will be enabled if blue, red and yellow are true and disabled when at least one is false.
            sensitive persistent.one == True and persistent.two == True 

        imagebutton:
            auto "choices/four_%s.png"
            action Jump("four_start")
            # The imagebutton will be enabled if blue, red, yellow and silver are true and disabled when at least one is false.
            sensitive persistent.one == True and persistent.two == True and persistent.three == True 

        imagebutton:
            auto "choices/five_%s.png"
            action Jump("five_start")
            sensitive persistent.one == True and persistent.two == True and persistent.three == True and persistent.four == True 