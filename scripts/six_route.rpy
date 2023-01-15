#CHARACTER NAMES AND NAME COLOR
define alingabi = Character("Aling Abi", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define mangben = Character("Mang Ben", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")

define marta = Character("Marta", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")

define princess = Character("Princess", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define chloe = Character("Chloe", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define mark = Character("Mark", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

define host = Character("Host", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define tawastudents = Character("Mga Bata", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define mayari = Character("May-ari ng Cellphone", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image tawastudents one = "images/story6/char/tawastudents one.png"

image alingabi one = "images/story6/char/alingabi one.png"
image alingabi two = "images/story6/char/alingabi two.png"
image alingabi tri = "images/story6/char/alingabi tri.png"
image alingabi pray = "images/story6/char/alingabi pray.png"

image mangben one = "images/story6/char/mangben one.png"
image mangben tri = "images/story6/char/mangben tri.png"
image mangben pray = "images/story6/char/mangben pray.png"

image princess one = "images/story6/char/princess one.png"
image princess two = "images/story6/char/princess two.png"
image princess tri = "images/story6/char/princess tri.png"
image princess pray = "images/story6/char/princess pray.png"

image marta one = "images/story6/char/marta one.png"
image marta two = "images/story6/char/marta two.png"
image marta tri = "images/story6/char/marta tri.png"

image chloe one = "images/story6/char/chloe one.png"
image chloe two = "images/story6/char/chloe two.png"
image chloe tri = "images/story6/char/chloe tri.png"
image chloe bigaycp = "images/story6/char/chloe bigaycp.png"
image chloe pulotcp = "images/story6/char/chloe pulotcp.png"

image mrcheng one = "images/story6/char/mrcheng one.png"
image mrcampbell one = "images/story6/char/mrcampbell one.png"
image msbelsky one = "images/story6/char/msbelsky one.png"
image host one = "images/story6/char/host one.png"
image host two = "images/story6/char/host two.png"

image mayari one = "images/story6/char/mayari one.png"
image mayari two = "images/story6/char/mayari two.png"
image mayari tri = "images/story6/char/mayari tri.png"
image mayari kuhacp = "images/story6/char/mayari kuhacp.png"

#BACKGROUNDS
image bg condoone = "images/story6/bg condoone.jpg"
image bg condotwo = "images/story6/bg condotwo.jpg"
image bg condooutside = "images/story6/bg condooutside.jpg"
image bg schoolgate = "images/story6/bg schoolgate.jpg"
image bg hallwaytwo = "images/story6/bg hallwaytwo.jpg"
image bg audikalat = "images/story6/bg audikalat.png"
image bg auditorium = "images/story6/bg auditorium.png"
image bg auditwo = "images/story6/bg auditwo.png"

image chloe twoflip = Transform("images/story6/char/chloe two.png", xzoom=-1)

label six_start:                      
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: PATIMPALAK SA PAARALAN{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg condooutside with fade
    "ANG PAGMAMAHAL SA BANSA AY ISANG KATANGIAN NA NASUSUKAT SA MARAMING BAGAY."
    "HINDI KAILANGANG PALAGI MONG SINASABI NA MAHAL MO ANG PILIPINAS UPANG MAITURING NA MAHAL MO ANG IYONG BAYAN."
    "MAAARI DIN KASI NA MAIPAKITA ITO SA PAGSASABUHAY NG MGA KATANGIAN, KULTURA, AT KAUGALIANG KUMAKATAWAN SA ISANG TUNAY NA PILIPINO."
    "MGA KAUGALIAN NA SARILING ATIN."

    scene bg condoone with fade
    "KAUGALIAN NA NG PAMILYA GOMEZ ANG SABAY SABAY NA PAGKAIN AT PAGDARASAL BAGO MAGSIMULA."
    "MAAGANG KUMAIN ANG KANILANG PAMILYA DAHIL SILA AY PUPUNTA SA PATIMPALAK NG PAARALAN."
    "ISA ANG ANAK NILANG SI PRINCESS SA NAIMBITAHAN UPANG MAGPAKITA NG TALENTO SA PAGSASAYAW."
    show alingabi tri at slightright
    show mangben one at right
    show princess one at slightleft
    with dissolve
    alingabi "Anak pangunahan mo ang pagdarasal upang tayo ay makapagsimulang kumain."
    show alingabi one
    show princess tri
    princess "Sige po mama."
    show alingabi pray 
    show mangben pray
    show princess pray
    with dissolve
    "AT NAGSIMULA NANG MAGDASAL ANG PAMILYA."

    show alingabi one
    show princess one
    show mangben one with dissolve
    mangben "Kumain na tayo."

    show bg condotwo
    hide alingabi
    hide princess
    hide mangben
    play sound "audio/knock.wav"
    "HABANG SILA AY KUMAKAIN NAKARINIG SILA NG KATOK MULA SA PINTO."
    show bg condoone
    show princess one at slightleft
    show alingabi one at slightright
    show mangben one at right
    with dissolve
    show marta tri at left with moveinleft
    marta "Mare may ibibigay akong ulam, niluto ko ito kanina."
    show marta one
    show alingabi tri
    alingabi "Maraming salamat Marta. Kumain ka muna."
    show marta tri
    show alingabi one
    marta "Sige salamat aalis na din ako."

    scene bg schoolgate with fade
    "PAGKATAPOS KUMAIN AY NAGPUNTA NA SI PRINCESS SA PAARALAN. NAKASALUBONG NIYA ANG KANIYANG KAKLASE NA SI MARK."
    show princess tri at left
    show mark one at right
    with dissolve
    princess "Mark kasali ka ba sa patimpalak?"
    show princess one
    show mark tri
    mark "Hindi ako magpeperform pero nagvolunteer ako sa pagaayos ng sound system."
    show mark one
    mark "Ikaw ba?"
    show princess tri
    princess "Isa ako sa mga magbabahagi ng talento mamaya."
    show mark tri
    show princess one
    mark "Sige galingan mo mamaya."

    show bg hallwaytwo 
    hide mark
    show chloe one at right
    with dissolve
    "NAGPATULOY NA SI PRINCESS SA PAGLALAKAD AT NAKITA NIYA ANG KAIBIGAN NA SI CHLOE NA ISA SA MGA TUMUTULONG SA PAG-AAYOS NG PATIMPALAK."
    show princess tri
    princess "Chloe dumating na ba ang ating mga special guest na galing sa iba't ibang bansa?"
    show princess one
    show chloe tri
    chloe "Nako hindi pa pero papunta na daw sila."
    show princess tri
    show chloe one
    princess "Sige maghanda na tayo ng pagkain nila."

    scene black with dissolve
    "INIHANDA NA NILA ANG MGA PAGKAING PINOY NA PARA SA MGA DAYUHAN."
    scene bg auditorium with dissolve
    "DUMATING ANG MGA DAYUHAN AT PINAKAIN NA NILA ITO. PAGKATAPOS AY NAGSIMULA NA ANG PATIMPALAK."
    show host one at right with moveinright
    host "Ngayon ay ipapakilala ko sa inyo ang ating mga special guest na nagmula pa sa iba't ibang bansa."
    play sound "audio/clap.wav"
    pause 0.5
    show mrcheng one at left with moveinleft
    host "Let's all welcome Mr. Cheng from China"
    play sound "audio/clap.wav"
    pause 0.5
    show mrcampbell one at slightleft with moveinleft
    host "Mr. Campbell from America"
    play sound "audio/clap.wav"
    pause 0.5
    show msbelsky one at slightright with moveinleft
    host "Ms. Belsky from Russia"
    
    scene bg auditwo with fade
    "NAGSIMULA NA ANG PAGPAPAKITA NG TALENTO SA PATIMPALAK."
    "UNANG NAGBAHAGI NG TALENTO SI PRINCESS SA PAGSAYAW."
    scene bg pdanceone with dissolve
    centered ""
    show bg pdancetwo
    centered ""
    show bg pdancethree
    centered ""
    show bg pdancefour
    centered ""
    show bg pdanceone
    centered ""
    show bg pdancetwo
    centered ""
    show bg pdancethree
    centered ""
    show bg pdancefour
    centered ""
    show bg pdanceone
    centered ""
    show bg pdancetwo
    centered ""
    show bg pdancethree
    centered ""
    show bg pdancefour
    play sound "audio/clap.wav"
    centered ""

    scene bg auditorium with fade
    "ANG SUNOD NA NAGBAHAGI AY ANG GRUPO NG MGA KATUTUBONG SAYAW."
    show tawastudents one at left
    show chloe two at right
    with dissolve
    "HABANG NAGSASAYAW AY NAPANSIN NI CHLOE ANG ISANG GRUPO NG KABATAAN NA NAGTATAWANAN."
    hide tawastudents
    hide chloe
    show chloe twoflip with zoomin
    menu:
        
        chloe "ANO ANG GAGAWIN KO?"
        "PAGSASABIHAN AT ISUSUMBONG":
            jump sabisumbong_6
        "HINDI NALANG PAPANSININ":
            jump hindipansin_6


label sabisumbong_6:
    show chloe tri at right
    show tawastudents one at left
    chloe "Bakit kayo nagtatawanan?"
    tawastudents "Kasi ang pangit ng sayaw nila at nakakatawa."
    show chloe two
    chloe "Hindi dapat ganyan ang iyong sabihin dahil isa yan sa mga katutubong sayaw na dapat nating pahalagahan at igalang."
    show chloe tri
    chloe "Ipapa-alam ko sa inyong guro ang inyong ginawa."
    jump next_6

label hindipansin_6:
    hide chloe
    show tawastudents one at center with dissolve
    play sound "audio/laugh.mp3"
    "NAGPATULOY SA PAGTATAWANAN ANG MGA BATA SA KATUTUBONG SAYAW. AT GUMAYA NA RIN ANG IBANG MGA BATA."
    hide tawastudents
    show chloe twoflip at center
    with dissolve
    chloe "Dapat pala ay pinagsabihan ko na agad ang grupo ng mga batang iyon para hindi na ito lumala."

    chloe "Nalaman rin sana nila ang kahalagahan ng ipinapakitang katutubong sayaw."
    jump next_6

label next_6:
    scene bg audikalat with fade
    "MATAPOS ANG ILANG ORAS AY NATAPOS NA ANG PATIMPALAK AT NAGSIMULA NA RIN SILA MAGLINIS NG MGA KALAT."
    show host two at center with dissolve
    host "Bago po tayo umalis ay pulutin po natin ang ating mga kalat na makikita."
    show host one with dissolve
    host "Mahalaga po na mapanatili natin ang kalinisan ng ating paaralan dahil para rin ito sa ating kaligtasan at kalusugan."
    hide host
    show chloe pulotcp with dissolve
    "HABANG NAGLILINIS AY NAPANSIN NI CHLOE NA MAY NAKAIWAN NG CELLPHONE SA ISANG UPUAN."
    show chloe twoflip with dissolve
    chloe "Kailangan ko itong maibalik dahil masama ang magnakaw."
    hide chloe with dissolve
    "ITINAGO MUNA NI CHLOE ANG CELLPHONE AT BIGLANG DUMATING ANG MAY-ARI NITO."
    show chloe one at right
    show mayari tri at left with moveinleft
    mayari "May nakita po ba kayong cellphone? Naiwan ko kasi dito sa upuan kanina."
    show mayari one
    mayari "Mahalaga iyon sa akin dahil ginagamit ko iyon palagi."
    show chloe bigaycp
    show mayari kuhacp
    with dissolve
    chloe "Eto yung cellphone na hinahanap mo itinago ko muna baka kasi may maghanap."
    show mayari tri
    mayari "Maraming Salamat."

    scene black with fade

    "AT NATAPOS NA ANG PAGLILINIS AT UMUWI NA SILA UPANG MAKAPAGPAHINGA."

    centered "MORAL: PAGPAPAHALAGA SA DAYUHAN AT KAPWA"
    jump quiz_6


label quiz_6: 
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_6 = 0 
    default percent_6 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_6 = 0 
    call screen question1_6 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_6: 
    $ points_6 += 1
    call screen question2_6 with circlewipe
label wronganswer1one_6:
    call screen question2_6 with circlewipe
label wronganswer1two_6:
    call screen question2_6 with circlewipe

label correctanswer2_6: 
    $ points_6 += 1
    call screen question3_6 with circlewipe
label wronganswer2two_6:
    call screen question3_6 with circlewipe
label wronganswer2one_6:
    call screen question3_6 with circlewipe

label correctanswer3_6: 
    $ points_6 += 1
    call screen question4_6 with circlewipe
label wronganswer3two_6:
    call screen question4_6 with circlewipe
label wronganswer3one_6:
    call screen question4_6 with circlewipe

label correctanswer4_6: 
    $ points_6 += 1
    call screen question5_6 with circlewipe
label wronganswer4_6:
    call screen question5_6 with circlewipe

label correctanswer5_6: 
    $ renpy.block_rollback()
    $ points_6 += 1
    $ persistent.current_6 = points_6
    $ renpy.choice_for_skipping()
    if points_6 == 4:
        $ persistent.six = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_6 == 5:
        $ persistent.six = True
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
    
label wronganswer5_6:
    $ renpy.block_rollback()
    $ persistent.current_6 = points_6
    $ renpy.choice_for_skipping()
    if points_6 == 4:
        $ persistent.six = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_6 == 5:
        $ persistent.six = True
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


screen question1_6:
    add "images/story6/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story6/qc/a1_idle.png"
        hover "images/story6/qc/a1_hover.png"
        action Jump("wronganswer1two_6")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story6/qc/b1_idle.png"
        hover "images/story6/qc/b1_hover.png"
        action Jump("wronganswer1one_6")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story6/qc/c1_idle.png"
        hover "images/story6/qc/c1_hover.png"
        action Jump("correctanswer1_6")

screen question2_6:
    add "images/story6/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story6/qc/a2_idle.png"
        hover "images/story6/qc/a2_hover.png"
        action Jump("wronganswer2two_6")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story6/qc/b2_idle.png"
        hover "images/story6/qc/b2_hover.png"
        action Jump("correctanswer2_6")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story6/qc/c2_idle.png"
        hover "images/story6/qc/c2_hover.png"
        action Jump("wronganswer2one_6")

screen question3_6:
    add "images/story6/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story6/qc/a3_idle.png"
        hover "images/story6/qc/a3_hover.png"
        action Jump("wronganswer3one_6")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story6/qc/b3_idle.png"
        hover "images/story6/qc/b3_hover.png"
        action Jump("correctanswer3_6")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story6/qc/c3_idle.png"
        hover "images/story6/qc/c3_hover.png"
        action Jump("wronganswer3two_6")

screen question4_6:
    add "images/story6/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer4_6")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer4_6")

screen question5_6:
    add "images/story6/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer5_6")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer5_6")