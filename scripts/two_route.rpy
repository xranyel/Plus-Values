#CHARACTER NAMES AND NAME COLOR
define celia = Character("Celia", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define jenny = Character("Jenny", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define ana = Character("Ana", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image celia abot = "images/story2/char/celia abot.png"
image celia close = "images/story2/char/celia close.png"
image celia decision = "images/story2/char/celia decision.png"
image celia one = "images/story2/char/celia one.png"
image celia two = "images/story2/char/celia two.png"
image celia tri = "images/story2/char/celia tri.png"

image jenny close = "images/story2/char/jenny close.png"
image jenny decision = "images/story2/char/jenny decision.png"
image jenny one = "images/story2/char/jenny one.png"
image jenny two = "images/story2/char/jenny two.png"
image jenny tri = "images/story2/char/jenny tri.png"

image ana one = "images/story2/char/ana one.png"
image ana two = "images/story2/char/ana two.png"
image ana tri = "images/story2/char/ana tri.png"

#BACKGROUNDS
image bg school = "images/story2/bg school.jpg"
image bg sakayan = "images/story2/bg sakayan.jpg"
image bg classroom = "images/story2/bg classroom.jpg"
image bg bayan = "images/story2/bg bayan.png"
image bg bus = "images/story2/bg bus.jpg"

label two_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: LIBRE{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg school with fade
    "LAGING HANDA SA PAGTULONG SI CELIA SA KAIBIGAN NIYANG SI JENNY. LAGI NIYANG BINIBIGYAN NG PAGKAIN TUWING RISES AT MADALAS DIN NIYANG INILILIBRE NG PAMASAHE SA PAGUWI."
    "NAAAWA KASI SI CELIA KAY JENNY DAHIL WALANG TRABAHO ANG TATAY NIYA."

    show bg sakayan with dissolve 
    play sound "audio/cars.mp3" loop fadein 0.5
    "MINSAN SILA AY PAUWI AT NAG-AANTAY NG MASASAKYAN, WALANG BARYA PARA SA PAMASAHE SI CELIA."
    stop sound fadeout 1.0
    show celia one at left with dissolve
    celia "Jenny may barya ka ba dyan?"
    hide celia with moveoutleft
    show jenny tri at right with moveinright
    "SINILIP NAMAN NI JENNY ANG KANYANG PITAKA AT NAKITA NIYANG SIYA AY MAY SAPAT NA BARYA PARA SA PAMASAHE NILANG DALAWA."
    hide jenny
    show jenny decision with zoomin
    menu:
        
        "ANO ANG DAPAT GAWIN NI JENNY?"
        "SABIHIN NA MAYRON SIYANG BARYA":
            jump sabihin_2
        "ILIHIM ITO KAY CELIA":
            jump ilihim_2

label sabihin_2:
    show celia one at left
    show jenny tri at right
    jenny "Heto na lang Celia, sapat ang aking barya para sa pamasahe nating dalawa."

    show jenny one at slightleft with moveinleft
    show bg bus with dissolve
    "AT NANG MAKASAKAY NA SILA SA BUS, IBINAYAD NA NI JENNY ANG KANILANG PAMASAHE."

    show celia tri
    show jenny one
    celia "Maraming salamat Jenny, napakabuti mong kaibigan."
    show celia one 
    celia "Bayadan ko nalang yung pamasahe natin kapag nasa bayan na tayo."
    show jenny tri with dissolve
    jenny "Huwag na maliit na bagay lamang iyon."
    show celia two
    celia "Hala babayadan ko na, idagdag mo nalang sa ipon mo."

    scene bg bayan with fade
    "AT NANG MAKARATING NA SILA SA BAYAN. NAGHANAP MUNA SILA NG MAKAKAIN."

    show celia tri at left 
    show jenny one at right
    with dissolve
    celia "Jenny, gutom ka na ba? Maghanap muna tayo ng makakain?"
    show jenny two
    jenny "Nako Celia wala na akong pera sa susunod na lang ako."
    show celia one
    celia "Sige ililibre na kita, alam kong nagugutom ka na rin."
    call screen interactive2 with dissolve

screen interactive2:
    add "images/story2/bg foodchoice.png"

    imagebutton:
        xpos 120
        ypos 243
        idle "images/story2/burger_idle.png"
        hover "images/story2/burger_hover.png"
        action Jump("burger_2")

    imagebutton:
        xpos 682
        ypos 270
        idle "images/story2/pizza_idle.png"
        hover "images/story2/pizza_hover.png"
        action Jump("pizza_2")

label burger_2:
    show jenny one
    jenny "Wow! sarap naman ng burger, maraming salamat dito Celia."
    show celia tri
    celia "Walang anuman."
    jump end_2

label pizza_2:
    jenny "Wow! sarap naman ng pizza, maraming salamat dito Celia."
    show celia tri
    celia "Walang anuman."
    jump end_2

label end_2:
    show celia abot at left with dissolve #try palitan tong image
    celia "Jenny ito na nga pala yung hiniram ko sayo kanina."
    show celia one with dissolve
    show jenny tri
    jenny "Huwag na Celia ayos na yun."

    "AT TULUYAN NA NGANG HINDI PINABAYADAN NI JENNY ANG PAMASAHE NILA KANINA."
    
    show jenny one
    show celia tri
    celia "Sige Jenny salamat, magkita na lamang tayo ulit bukas sa eskwelahan."
    show celia one
    celia "Mag-ingat ka sa paguwi."

    scene black with dissolve
    "AT UMUWI NA ANG DALAWANG MAGKAIBIGAN SA KANI-KANILANG TAHANAN."
    "DAHIL DITO AY NAGING MAS MATALIK SILANG MAGKAIBIGAN AT NAG TUTULUNGAN SA LAHAT NG BAGAY."
    "KAPAG MAY PAG KUKULANG ANG ISA AY AGAD NA PINUPUNAN NG ISA, GANITO ANG KANILANG PAGKAKAIBIGAN."
    centered "MORAL: HUWAG MAGING MAPANG-ABUSO SA KAPWA"
    jump quiz_2

label ilihim_2:
    hide jenny
    "DAHIL DITO NAPILITAN SI CELIA NA BUMILI SA MALAPIT NA TINDAHAN PARA MABARYAHAN ANG PERA NIYA." 
    
    show celia tri at left
    show jenny one 
    with dissolve
    celia "Jenny saglit lamang, bibili na lang ako ng biskwit para mabaryahan ang pamasahe."
    jenny "Sige hintayin nalang kita dito."
    hide celia with moveoutright

    scene black with dissolve
    "BINIGYAN NIYA NG BISKUWIT SI JENNY AT SIYA ANG NAGBAYAD NG PAMASAHE NILA."
    "NALAMAN ITO NG ISA NILANG KAKLASE NA SI ANA KAYA ISANG ARAW AY KINAUSAP NIYA SI CELIA."

    scene bg classroom with dissolve
    show celia decision at left
    show ana two at right
    with dissolve
    celia "Ana, ano ba ang iyong sasabihin? Hinaan mo ang iyong boses dahil nag-aaral ang ating mga kaklase."
    show ana tri
    ana "Celia, huwag kang masyadong mabait. Inaabuso na ni Jenny ang kabaitan mo."
    show celia close 
    celia "Paano mo naman nasabi Ana?"
    show ana two
    ana "Sinabi ni Jenny sa akin na inuuto ka lang niya para ilibre mo siya."
    hide ana
    hide celia
    show celia decision with zoomin
    menu:
        
        celia "ANO ANG DAPAT KONG GAWIN?"
        "HINDI MANIWALA KAY ANA":
            jump mainis_2
        "MAGPASALAMAT SA PAALALA NI ANA":
            jump magpasalamat_2

label mainis_2:
    show celia close at left
    show ana two at right
    celia "Grabe ka naman Ana, napakasama mo sa kaibigan ko. Hindi kita mapapatawad."
    show ana tri
    ana "Nagsasabi lang naman ako Celia."

    scene black with dissolve
    "ISANG ARAW AY NASUBOK ANG PAGKAKAIBIGAN NI CELIA AT JENNY"

    show bg classroom with dissolve
    show celia tri at left
    show jenny two at right
    with dissolve
    celia "Alam mo ba Jenny sinabi sa akin ni Ana na inaabuso mo lang ang aking pagiging mabuting kaibigan sayo."
    show jenny tri
    jenny "Bakit naman niya iyon nasabi?"
    show celia two
    celia "Noong isang araw daw ay sakto ang barya mo para sa pamasahe naten pero pinilit mo pa din akong magpabarya sa tindahan."
    show jenny close with dissolve
    jenny "Paumanhin Celia, kung hindi ko agad sinabi sayo ang totoo at sa iba mo pa nalaman."

    scene black with fade
    "DAHIL DITO AY NAGKAROON NG TAMPO SI CELIA KAY JENNY."
    "MAKALIPAS ANG ILANG ARAW NG PAGHINGI NG TAWAD NI JENNY KAY CELIA AY NAPATAWAD NA SIYA NITO."

    "MAARING MAWALA ANG PINAPAHALAGAHAN MONG KAIBIGAN KUNG HINDI KA MAGIGING MAHINAHON AT KUNG MAGIGING MAPANG-ABUSO KA."
    centered "MORAL: HUWAG MAGING MAPANG-ABUSO SA KAPWA"
    jump quiz_2


label magpasalamat_2:
    show celia tri at left
    show ana one at right
    celia "Salamat sa paalala mo Ana. Inaamin ko na inaabuso na ako ni Jenny." 
    show ana tri
    ana "Bakit hindi mo siya sinasabihan?"
    show celia close
    celia "Ayoko kasi na sa akin magmula, alam ko naman na alam niya ang kanyang ginawa."
    show celia one
    celia "Pero umaasa ako na darating ang araw na hindi na siya mang-aabuso at magsusumikap na siya."

    scene black with fade
    centered "MORAL: HUWAG MAGING MAPANG-ABUSO SA KAPWA"
    jump quiz_2

label quiz_2: #change _2 to _3 to copy for next quiz
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_2 = 0 
    default percent_2 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_2 = 0 
    call screen question1_2 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_2: 
    $ points_2 += 1
    call screen question2_2 with circlewipe
label wronganswer1one_2:
    call screen question2_2 with circlewipe
label wronganswer1two_2:
    call screen question2_2 with circlewipe

label correctanswer2_2: 
    $ points_2 += 1
    call screen question3_2 with circlewipe
label wronganswer2two_2:
    call screen question3_2 with circlewipe
label wronganswer2one_2:
    call screen question3_2 with circlewipe

label correctanswer3_2: 
    $ points_2 += 1
    call screen question4_2 with circlewipe
label wronganswer3two_2:
    call screen question4_2 with circlewipe
label wronganswer3one_2:
    call screen question4_2 with circlewipe

label correctanswer4_2: 
    $ points_2 += 1
    call screen question5_2 with circlewipe
label wronganswer4_2:
    call screen question5_2 with circlewipe

label correctanswer5_2:
    $ renpy.block_rollback()
    $ points_2 += 1
    $ persistent.current_2 = points_2
    $ renpy.choice_for_skipping()
    if points_2 == 4:
        $ persistent.two = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_2 == 5:
        $ persistent.two = True
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
    
label wronganswer5_2:
    $ renpy.block_rollback()
    $ persistent.current_2 = points_2
    $ renpy.choice_for_skipping()
    if points_2 == 4:
        $ persistent.two = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_2 == 5:
        $ persistent.two = True
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


screen question1_2:
    add "images/story2/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story2/qc/a1_idle.png"
        hover "images/story2/qc/a1_hover.png"
        action Jump("wronganswer1two_2")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story2/qc/b1_idle.png"
        hover "images/story2/qc/b1_hover.png"
        action Jump("wronganswer1one_2")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story2/qc/c1_idle.png"
        hover "images/story2/qc/c1_hover.png"
        action Jump("correctanswer1_2")

screen question2_2:
    add "images/story2/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story2/qc/a2_idle.png"
        hover "images/story2/qc/a2_hover.png"
        action Jump("wronganswer2two_2")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story2/qc/b2_idle.png"
        hover "images/story2/qc/b2_hover.png"
        action Jump("correctanswer2_2")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story2/qc/c2_idle.png"
        hover "images/story2/qc/c2_hover.png"
        action Jump("wronganswer2one_2")

screen question3_2:
    add "images/story2/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story2/qc/a3_idle.png"
        hover "images/story2/qc/a3_hover.png"
        action Jump("correctanswer3_2")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story2/qc/b3_idle.png"
        hover "images/story2/qc/b3_hover.png"
        action Jump("wronganswer3one_2")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story2/qc/c3_idle.png"
        hover "images/story2/qc/c3_hover.png"
        action Jump("wronganswer3two_2")

screen question4_2:
    add "images/story2/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer4_2")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer4_2")

screen question5_2:
    add "images/story2/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer5_2")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer5_2")