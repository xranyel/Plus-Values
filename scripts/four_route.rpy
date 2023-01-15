#CHARACTER NAMES AND NAME COLOR
define alingemily = Character("Aling Emily", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define marisa = Character("Marisa", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define cherry = Character("Ninang Cherry", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define reporter = Character("Reporter", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define alex = Character("Alexander", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image alex one = "images/story4/char/alex one.png"
image alex two = "images/story4/char/alex two.png"
image alex tri = "images/story4/char/alex tri.png"
image alex decision = "images/story4/char/alex decision.png"

image alingemily one = "images/story4/char/alingemily one.png"
image alingemily two = "images/story4/char/alingemily two.png"
image alingemily tri = "images/story4/char/alingemily tri.png"
image alingemily close = "images/story4/char/alingemily close.png"
#EMILYLEFT
image alingemily oneleft = Transform("images/story4/char/alingemily one.png", xzoom=-1)
image alingemily twoleft = Transform("images/story4/char/alingemily two.png", xzoom=-1)
image alingemily trileft = Transform("images/story4/char/alingemily tri.png", xzoom=-1)
image alingemily closeleft = Transform("images/story4/char/alingemily close.png", xzoom=-1)

image cherry one = "images/story4/char/cherry one.png"
image cherry tri = "images/story4/char/cherry tri.png"

image marisa one = "images/story4/char/marisa one.png"
image marisa tri = "images/story4/char/marisa tri.png"

image reporter one = "images/story4/char/reporter one.png"
image reporter tri = "images/story4/char/reporter tri.png"

image alexemily decision = "images/story4/char/alexemily decision.png"

#BACKGROUNDS
image bg kalyefour = "images/story4/bg kalyefour.jpg"
image bg livingroomfour = "images/story4/bg livingroomfour.jpg"
image bg livingroommarisa = "images/story4/bg livingroommarisa.jpg"
image bg livingbaha = "images/story4/bg livingbaha.png"
image bg reporterbg = "images/story4/bg reporterbg.png"
image bg marisabaha = "images/story4/bg marisabaha.png"

image rain:
        "images/story4/rain1.png"
        0.2
        "images/story4/rain3.png"
        0.2
        "images/story4/rain2.png"
        0.2
        repeat

label four_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: BAGYO{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg livingroomfour with fade
    "NAGING GAWI NG KARAMIHAN NA SA BAWAT PAGGISING AY MAGHANAP NG BAGONG BALITA MULA SA DIYARYO, RADYO, O TELEBISYON. PARA SA KANILA,"
    "HINDI KOMPLETO ANG UMAGA KUNG WALANG BAGONG BALITA."
    "ISA RIN ITO SA MGA PARAAN NG MGA MAG-AARAL NA TULAD MO UPANG MAPALAWAK AT MADAGDAGAN ANG IYONG KAALAMAN AT KAMALAYAN,"
    "HINDI LAMANG UKOL SA MGA PANGKARANIWANG PANGYAYARI, KUNDI SA MGA BAGO AT KAGILAGILALAS NA MGA TUKLAS SA SIYENSIYA AT TEKNOLOHIYA."
    "BUKOD SA MGA BAGONG KAALAMAN, NARIYAN DIN ANG MGA KAHINDIK-HINDIK NA BALITA TULAD NG MGA TRAHEDYA,"
    "AT MGA KALAMIDAD TULAD NG LINDOL AT BAGYO NA BUMIBIKTIMA SA MGA TAO." 

    show alex one at slightleft
    show alingemily one at slightright
    "NANONOOD ANG PAMILYA NI ALEXANDER NG BALITA SA TELEBISYON TUNGKOL SA PAPARATING NA BAGYO."
    hide alex
    hide alingemily
    show bg reporterbg
    show reporter tri at center
    with dissolve
    reporter "Ayon sa PAG-ASA may namataang may namumuong bagyo sa bahagi ng luzon,"
    show reporter one
    reporter "inaasahang magiging isang super typhoon na darating sa huwebes kung kayat pinag-iingat ang bawat isa lalo na sa mga nasa bahagi ng luzon,"
    show reporter tri
    reporter "kung maaari ay lumikas na at lumayo sa mga puno na maaring bumagsak at humanap ng ligtas na lugar na maaring pansamantalang masisilungan."
    hide reporter
    show bg livingroomfour
    show alexemily decision with zoomin
    menu:
        
        "MANINIWALA KAYA SILA SA BALITA?"
        "OO":
            jump oo_4
        "HINDI":
            jump hindi_4   

label oo_4:
    hide alexemily
    show alex tri at left
    show alingemily one at right
    alex "Nay! Kailangan na pala nating humanap ng maari nating puntahan bago dumating ang bagyo."
    show alex one
    alex "Mas Maigi nang maging handa bago pa ito mangyari."
    show alingemily tri
    alingemily "Sige anak pupunta tayo sa iyong tiya Marisa magpapaalam tayo kung maari muna tayong sumilong sa kanila bago dumating ang bagyo."

    scene bg kalyefour with fade
    "AT NAGPUNTA NA ANG MAG-INA SA KANILANG TIYA MARISA."
    "SA KANILANG PAGLALAKAD NAKASALUBONG NILA ANG NINANG NI ALEXANDER."

    show alex tri at left
    show alingemily oneleft at slightleft 
    show cherry one at right
    with dissolve
    alex "Magandang umaga po ninang."
    show alex one
    show cherry tri
    cherry "Huy! Kumare saan kayo pupunta?"
    show alingemily trileft
    alingemily "Dito kumare kina ate Marisa, magpapaalam sana kami kung maari kaming makisilong sa kanilang bahay bago pa man dumating ang bagyo."
    show cherry one
    cherry "Nako! kumare huwag kang mangamba. Huwag kang maniwala sa balita dahil hindi naman tayo maaapektuhan ng bagyo na yan."
    show alingemily oneleft
    alingemily "Nako! kumare baka kung kailan kasagsagan ay saka pa kami lilipat, mas maigi nang maging handa."
    show cherry tri
    cherry "Osige kumare mag-ingat kayo basta kami ay dito nalang sa amin hindi naman tayo maaapektuhan ng bagyo."
    
    # INTERACTIVE DRAG MAG-INA SA BAHAY.
init python:

    def detective_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True

screen interactive4:

    # A map as background.
    add "images/story4/bg kalyefourfeature.png"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "alexemilydrag"
            child "images/story4/alexemilydrag.png"
            droppable False
            dragged detective_dragged
            xpos 950 ypos 450
        

        # The cities they can go to.
        drag:
            drag_name "gate"
            child "images/story4/gate.png"
            draggable False
            xpos 263 ypos 391

label tuloy_4:
    call screen interactive4 with dissolve
    scene bg livingroommarisa 
    "AT NANG NAKARATING NA SILA SA BAHAY NI MARISA."

    show alex one at left
    show alingemily trileft at slightleft 
    show marisa one at right
    with dissolve
    alingemily "Ate magandang umaga sayo, nabalitaan mo na ba ang paparating na bagyo?"
    show marisa tri
    marisa "Hindi pa pero may napakinggan akong usap-usapan tungkol diyan, ngunit hindi naman daw tayo maaapektuhan nito."
    show alingemily oneleft
    alingemily "Pero ate ayon sa balita ay pinapalikas na ang mga tao."
    show alingemily trileft
    alingemily "kung kaya't napagdesisyonan namin na makikisilong muna sana kami dito sa inyo bago pa man dumating ang nalalapit na bagyong ito"
    show alingemily oneleft
    alingemily "dahil ito daw ay napakalakas."
    show marisa one
    marisa "Sige maigi na din ang maging ligtas."

    scene bg bagyo 
    show rain
    with fade
    play sound "audio/rain.mp3" loop
    "NUNG DUMATING NA ANG MALAKAS NA BAGYO."
    stop sound fadeout 0.5
    scene bg marisabaha
    show alex one at left
    show alingemily tri at right
    with dissolve
    alingemily "Buti nalang anak lumikas agad tayo, kung hindi mangangamba sana tayo kung paano tayo makakaligtas."
    show alex tri
    alex "Oo nga po nay, mabuti talagang maging handa bago dumating ang bagyo."
    
    scene black with fade
    "AT NATAPOS ANG BAGYO NA LIGTAS ANG PAMILYA NI ALEXANDER AT ALING EMILY."

    centered "MORAL: PAHALAGAHAN ANG KATOTOHANAN"
    jump quiz_4

label hindi_4:
    hide alexemily
    show alex one at left
    show alingemily tri at right
    alingemily "Anak, kailangan na pala natin maghanda para sa darating na bagyo."
    show alex tri
    alex "Nako nay! wag kayo magpapaniwala diyan, hindi tayo maaapektuhan niyan."
    show alingemily one
    alingemily "Anak mahirap ang hindi maging handa."
    show alex one
    alex "Nay, huwag po kayong mabahala."    
    
    scene bg bagyo 
    show rain
    with fade
    play sound "audio/rain.mp3" loop
    "AT DUMATING NA NGA ANG MALAKAS BAGYO."
    "NAGSIMULA NA ANG MALAKAS NA HANGIN AT LUMALAKAS NA RIN ANG ULAN NA NAGDUDULOT NG PAGTAAS NG TUBIG."
    
    stop sound fadeout 0.5
    scene bg livingbaha with dissolve
    pause 0.5
    "PUMASOK NA SA LOOB NG BAHAY ANG TUBIG NA NAGDULOT NG PANGAMBA SA PAMILYA NINA ALEXANDER."

    show alex tri at left with moveinleft
    alex "Nay! tumataas na ang tubig."
    show alingemily tri at right with moveinright
    alingemily "Ayan na nga ba ang sinasabi ko sayo. Kung lumipat na sana tayo kahapon pa hindi tayo magkakaproblema."
    show alex two
    alex "Hindi ko naman po kasi inaasahan na papasukin tayo ng tubig."
    
    scene black with fade
    "AT TULUYAN NANG NAPASOK NG TUBIG ANG LOOB NG BAHAY NILA NA NAGDULOT NG PAGKASIRA NG ILANG KAGAMITAN."

    centered "MORAL: PAHALAGAHAN ANG KATOTOHANAN"
    jump quiz_4

label quiz_4: 
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_4 = 0 
    default percent_4 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_4 = 0 
    call screen question1_4 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_4: 
    $ points_4 += 1
    call screen question2_4 with circlewipe
label wronganswer1one_4:
    call screen question2_4 with circlewipe
label wronganswer1two_4:
    call screen question2_4 with circlewipe

label correctanswer2_4: 
    $ points_4 += 1
    call screen question3_4 with circlewipe
label wronganswer2two_4:
    call screen question3_4 with circlewipe
label wronganswer2one_4:
    call screen question3_4 with circlewipe

label correctanswer3_4: 
    $ points_4 += 1
    call screen question4_4 with circlewipe
label wronganswer3two_4:
    call screen question4_4 with circlewipe
label wronganswer3one_4:
    call screen question4_4 with circlewipe

label correctanswer4_4: 
    $ points_4 += 1
    call screen question5_4 with circlewipe
label wronganswer4_4:
    call screen question5_4 with circlewipe

label correctanswer5_4: 
    $ renpy.block_rollback()
    $ points_4 += 1
    $ persistent.current_4 = points_4
    $ renpy.choice_for_skipping()
    if points_4 == 4:
        $ persistent.four = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_4 == 5:
        $ persistent.four = True
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
    
label wronganswer5_4:
    $ renpy.block_rollback()
    $ persistent.current_4 = points_4
    $ renpy.choice_for_skipping()
    if points_4 == 4:
        $ persistent.four = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_4 == 5:
        $ persistent.four = True
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


screen question1_4:
    add "images/story4/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story4/qc/a1_idle.png"
        hover "images/story4/qc/a1_hover.png"
        action Jump("correctanswer1_4")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story4/qc/b1_idle.png"
        hover "images/story4/qc/b1_hover.png"
        action Jump("wronganswer1two_4")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story4/qc/c1_idle.png"
        hover "images/story4/qc/c1_hover.png"
        action Jump("wronganswer1one_4")

screen question2_4:
    add "images/story4/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story4/qc/a2_idle.png"
        hover "images/story4/qc/a2_hover.png"
        action Jump("wronganswer2one_4")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story4/qc/b2_idle.png"
        hover "images/story4/qc/b2_hover.png"
        action Jump("wronganswer2two_4")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story4/qc/c2_idle.png"
        hover "images/story4/qc/c2_hover.png"
        action Jump("correctanswer2_4")

screen question3_4:
    add "images/story4/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story4/qc/a3_idle.png"
        hover "images/story4/qc/a3_hover.png"
        action Jump("wronganswer3two_4")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story4/qc/b3_idle.png"
        hover "images/story4/qc/b3_hover.png"
        action Jump("wronganswer3one_4")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story4/qc/c3_idle.png"
        hover "images/story4/qc/c3_hover.png"
        action Jump("correctanswer3_4")

screen question4_4:
    add "images/story4/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer4_4")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer4_4")

screen question5_4:
    add "images/story4/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer5_4")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer5_4")