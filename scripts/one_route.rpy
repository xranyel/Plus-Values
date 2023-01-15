#DEFAULT CONFIGS
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 0.7


#REMOVE KEYMAPS
init:
    $ _game_menu_screen = "preferences"
    
    #DISABLE ARROW KEYS
    $ config.keymap["focus_left"].remove('K_LEFT')
    $ config.keymap["focus_right"].remove('K_RIGHT')
    $ config.keymap["focus_up"].remove('K_UP')
    $ config.keymap["focus_down"].remove('K_DOWN') 

    $ config.keymap["focus_left"].remove('repeat_K_LEFT')
    $ config.keymap["focus_right"].remove('repeat_K_RIGHT')
    $ config.keymap["focus_up"].remove('repeat_K_UP')
    $ config.keymap["focus_down"].remove('repeat_K_DOWN') 

    #DISABLES
    $ config.keymap["screenshot"].remove('s')
    $ config.keymap["screenshot"].remove('alt_K_s')
    $ config.keymap["screenshot"].remove('alt_shift_K_s')
    $ config.keymap["screenshot"].remove('noshift_K_s')

    $ config.keymap["self_voicing"].remove('v')
    $ config.keymap["self_voicing"].remove('V')
    $ config.keymap["self_voicing"].remove('alt_K_v')
    $ config.keymap["self_voicing"].remove('K_v')


    $ config.keymap["accessibility"].remove('K_a')
    $ config.keymap["clipboard_voicing"].remove('C')

    $ config.keymap["hide_windows"].remove('mouseup_2') #middle click

    $ config.keymap["skip"].remove('K_LCTRL')
    $ config.keymap["skip"].remove('K_RCTRL')
    

#ADDITIONAL POSITIONS
define slightleft = Position(xpos=0.25, xanchor='left')
define slightright = Position(xpos=0.75, xanchor='right')

#CHARACTER NAMES AND NAME COLOR
define liza = Character("Liza", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define alingida = Character("Aling Ida", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define luis = Character("Luis", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
#BAWAL ANG MAY NUMBER SA IMAGE NAME             #ONE TWO TRI
image liza one = "images/story1/char/liza one.png"
image liza two = "images/story1/char/liza two.png"
image liza tri = "images/story1/char/liza tri.png"
image liza close = "images/story1/char/liza close.png"
image liza scared = "images/story1/char/liza scared.png"
image liza decision = "images/story1/char/liza decision.png"

image alingida one = "images/story1/char/alingida one.png"
image alingida two = "images/story1/char/alingida two.png"
image alingida tri = "images/story1/char/alingida tri.png"
image alingida close = "images/story1/char/alingida close.png"
image alingida angry = "images/story1/char/alingida angry.png"
image alingida nako = "images/story1/char/alingida nako.png"

image luis one = "images/story1/char/luis one.png"

#BACKGROUNDS
image bg inhouse = "images/story1/bg inhouse.jpg"
image bg outhouse = "images/story1/bg outhouse.jpg"

#CTC (Click to Continue) AND NARRATOR
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
image ctc_blink:
       "ctc.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 

label splashscreen:
    scene black
    with Pause(0.7)
    
    show text "{font=fonts/bryndan_write.ttf}{size=40}Team {color=#FF0000}E{/color}{color=#00FF00}C{/color}{color=#0000FF}M{/color}{color=#FF0000}C{/color} presents...{/size}{/font}" with dissolve
    with Pause(1.2)
    
    hide text with dissolve
    with Pause(0.7)

    return

label one_start:                                              
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: SASABIHIN KO BA{/size}" 
    #centered "{color=#0000ffff}{size=50}PAMAGAT: SASABIHIN KO BA{/size}{/color}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    show bg inhouse with fade
    "SI LIZA AY INUTUSAN NG KANIYANG NANAY NA SI ALING IDA NA MAGLINIS NG KANILANG SALA. MASAYA NIYANG SINUNOD ANG UTOS NG INA. PINUNASAN MUNA NIYA ANG MGA SILYA AT UPUAN."
    #play sound [ "<silence 1.5>", "audio/glass.mp3" ]
    play sound "audio/glass.mp3"
    "NANG PINUPUNASAN NA NIYA ANG CABINET NA MAY LARAWAN, AKSIDENTE NIYA ITONG NATABIG. NAHULOG AT NABASAG ANG MAGANDANG SALAMIN NG PICTURE FRAME."
    show liza scared at center
    liza "Naku! tiyak na pagagalitan ako ni nanay."
    hide liza with dissolve
    "INAYOS NIYA ANG NABASAG NA SALAMIN NG PICTURE FRAME AT ITINABI MUNA. TINAPOS NIYA ANG PAGWAWALIS."
    "NANG DUMATING NA ANG KANIYANG NANAY AGAD NIYANG NAPANSIN NA WALA ANG PICTURE FRAME SA CABINET."
    show alingida nako at right
    alingida "Liza! nasaan ang picture frame?"
    hide alingida
    show liza decision with zoomin
    menu:
        
        liza "SASABIHIN KO KAYA SA AKING NANAY?"
        "OO":
            jump oo_1
        "HINDI":
            jump hindi_1
        
label oo_1:
    show liza two at left
    show alingida two at right 
    liza "Paumanhin po, nanay. Hindi ko po sinasadyang matabig ko ito habang nagpupunas po ako ng cabinet."
    liza "Heto po ang nabasag na salamin ng picture frame."
    show alingida close
    alingida "Naku! bata ka. Sa susunod ay mag-iingat ka ha." 
    show alingida two
    alingida "Delikado pa naman ang mga babasagin." 
    show liza two
    liza "Pasensya na po nay, magiingat po ako sa susunod."
    show alingida one
    alingida "Sige anak ikaw ay aking patatawarin basta palagi kang makikinig sa akin."
    show alingida tri 
    show liza tri with dissolve
    alingida "At dahil umamin ka sa iyong kasalanan, kakain tayo sa labas."
    show alingida one
    alingida "Kunin mo ang aking pitaka sa kwarto."
    call screen interactive1 with dissolve

screen interactive1:
    add "images/story1/bg kwarto.png"

    imagebutton:
        xpos 80
        ypos 460
        idle "images/story1/wallet_idle.png"
        hover "images/story1/wallet_hover.png"
        action Jump("jump_1")

label jump_1:
    scene black
    liza "Mabuti na lamang at sinabi ko ang totoo. Tama ang aming napag-aralan sa eskwela na mahalaga ang pagsasabi ng katotohanan kahit anuman ang maging bunga nito" 
    "NAPANGITI SI LIZA SA SARILI AT MASAYANG KUMAIN ANG KANILANG PAMILYA SA KANILANG PABORITONG RESTAURANT"
    centered "MORAL: SABIHIN ANG KATOTOHANAN"
    jump quiz_1

label hindi_1:
    show liza two at left
    show alingida two at right
    liza "Nay, hindi ko po napansin ang picture frame na binabanggit nyo."
    show alingida close
    alingida "Sigurado ka ba sa iyong sinasabi? Napakamahal at maganda pa naman iyon."

    scene bg outhouse with fade
    "ILANG ARAW ANG NAKALIPAS HABANG NAG LILINIS NG BAHAY SI ALING IDA, NAPANSIN NIYA ANG SALAMIN NG PICTURE FRAME."

    scene bg inhouse with fade
    show alingida two at right
    alingida "Liza, pumunta ka rito."
    show liza two at left with moveinleft
    liza "Bakit po Nay?"
    show alingida close
    alingida "Bakit nakatago ang salamin ng picture frame dito? Sino ang nakabasag nito?"
    hide alingida
    hide liza
    show liza decision with zoomin
    menu:

        liza "ANO ANG DAPAT KONG GAWIN?"
        "UMAMIN SA KASALANAN":
            jump umamin_1
        "MANISI NG KAPATID":
            jump manisi_1

label umamin_1:
    show liza two at left
    show alingida two at right
    liza "Paumanhin po, nanay. Hindi ko po sinasadyang matabig ko ito habang nagpupunas po ako ng cabinet."
    show liza close
    liza "Pasensiya na po at hindi ko sinabi agad."
    show alingida close
    alingida "Ikaw na bata ka, alam mo bang masama ang magsinungaling?"
    show liza two
    liza "Pasensya na po nay, hindi ko na po uulitin."
    show alingida one
    alingida "Sige, magpahinga ka na."
    show alingida two
    alingida "Ikaw ay aking patatawarin basta palagi kang makikinig sa akin."

    scene black with fade 
    liza "Mabuti na lamang at sinabi ko ang totoo. Tama ang aming napag-aralan sa eskwela na mahalaga ang pagsasabi ng katotohanan kahit anuman ang maging bunga nito" 
    "NAPANGITI SI LIZA SA SARILI AT HINABOL ANG PAPATALIKOD NA INA PARA YAKAPIN."
    centered "MORAL: SABIHIN ANG KATOTOHANAN"
    jump quiz_1

label manisi_1:
    show liza two at left
    show alingida two at right
    liza "Siguro 'nay si Luis"
    show alingida nako
    alingida "Luis! Ikaw ba ang nakabasag ng picture frame na ito?"
    show luis one at slightleft with dissolve
    luis "'Nay hindi ako ang nakabasag nyan."
    luis "Nakita ko si ate na itinatago ang picture frame dyan."
    show alingida angry
    show liza scared with dissolve
    alingida "Liza, ikaw talagang bata ka!"
    scene black with fade 
    "AT DAHIL DITO NAPAGALITAN SI LIZA NG KANIYANG INA DAHIL SA KASINUNGALINGAN NITO."
    centered "MORAL: SABIHIN ANG KATOTOHANAN"
    jump quiz_1
    
label quiz_1:
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points = 0 
    default percent_1 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_1 = 0 
    call screen question1 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1: 
    $ points += 1
    call screen question2 with circlewipe
label wronganswer1one:
    call screen question2 with circlewipe
label wronganswer1two:
    call screen question2 with circlewipe

label correctanswer2: 
    $ points += 1
    call screen question3 with circlewipe
label wronganswer2two:
    call screen question3 with circlewipe
label wronganswer2one:
    call screen question3 with circlewipe

label correctanswer3: 
    $ points += 1
    call screen question4 with circlewipe
label wronganswer3two:
    call screen question4 with circlewipe
label wronganswer3one:
    call screen question4 with circlewipe

label correctanswer4: 
    $ points += 1
    call screen question5 with circlewipe
label wronganswer4:
    call screen question5 with circlewipe

label correctanswer5: 
    $ renpy.block_rollback()
    $ points += 1
    $ persistent.current_1 = points
    $ renpy.choice_for_skipping()
    if points == 4:
        $ persistent.one = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points == 5:
        $ persistent.one = True
        play sound "audio/win.wav"
        scene bg five with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    else:
        play sound "audio/lose.mp3"
        scene bg bagsak with dissolve
        centered ""
        scene bg ulit
        centered ""
        return
    
label wronganswer5:
    $ renpy.block_rollback()
    $ persistent.current_1 = points 
    $ renpy.choice_for_skipping()
    if points == 4:
        $ persistent.one = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points == 5:
        $ persistent.one = True
        play sound "audio/win.wav"
        scene bg five with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    else:
        play sound "audio/lose.mp3"
        scene bg bagsak with dissolve
        centered ""
        scene bg ulit
        centered ""
        return


screen question1:
    add "images/story1/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story1/qc/a1_idle.png"
        hover "images/story1/qc/a1_hover.png"
        action Jump("correctanswer1")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story1/qc/b1_idle.png"
        hover "images/story1/qc/b1_hover.png"
        action Jump("wronganswer1one")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story1/qc/c1_idle.png"
        hover "images/story1/qc/c1_hover.png"
        action Jump("wronganswer1two")

screen question2:
    add "images/story1/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story1/qc/a2_idle.png"
        hover "images/story1/qc/a2_hover.png"
        action Jump("wronganswer2two")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story1/qc/b2_idle.png"
        hover "images/story1/qc/b2_hover.png"
        action Jump("wronganswer2one")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story1/qc/c2_idle.png"
        hover "images/story1/qc/c2_hover.png"
        action Jump("correctanswer2")

screen question3:
    add "images/story1/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story1/qc/a3_idle.png"
        hover "images/story1/qc/a3_hover.png"
        action Jump("wronganswer3one")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story1/qc/b3_idle.png"
        hover "images/story1/qc/b3_hover.png"
        action Jump("correctanswer3")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story1/qc/c3_idle.png"
        hover "images/story1/qc/c3_hover.png"
        action Jump("wronganswer3two")

screen question4:
    add "images/story1/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer4")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer4")

screen question5:
    add "images/story1/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer5")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer5")