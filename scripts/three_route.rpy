#CHARACTER NAMES AND NAME COLOR
define reyes = Character("Binibining Reyes", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define mangjose = Character("Mang Jose", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")

define eden = Character("Eden", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define gloren = Character("Gloren", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define john = Character("John", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define gemma = Character("Gemma", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define ezekiel = Character("Ezekiel", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

define luz = Character("Luz", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define allan = Character("Allan", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image allan mano = "images/story3/char/allan mano.png"
image allan one = "images/story3/char/allan one.png"
image allan tri = "images/story3/char/allan tri.png"
image eden one = "images/story3/char/eden one.png"
image eden tri = "images/story3/char/eden tri.png"
image ezekiel one = "images/story3/char/ezekiel one.png"
image ezekiel tri = "images/story3/char/ezekiel tri.png"
image gemma one = "images/story3/char/gemma one.png"
image gemma taas = "images/story3/char/gemma taas.png"
image gemma tri = "images/story3/char/gemma tri.png"
image gloren one = "images/story3/char/gloren one.png"
image gloren tri = "images/story3/char/gloren tri.png"
image john one = "images/story3/char/john one.png"
image john tri = "images/story3/char/john tri.png"
image luz decision = "images/story3/char/luz decision.png"
image luz mano = "images/story3/char/luz mano.png"
image luz one = "images/story3/char/luz one.png"
image luz two = "images/story3/char/luz two.png"
image luz tri = "images/story3/char/luz tri.png"
image luz taas = "images/story3/char/luz taas.png"

image mangjose one = "images/story3/char/mangjose one.png"
image mangjose tri = "images/story3/char/mangjose tri.png"
image reyes bitbit = "images/story3/char/reyes bitbit.png"
image reyes close = "images/story3/char/reyes close.png"
image reyes one = "images/story3/char/reyes one.png"
image reyes tri = "images/story3/char/reyes tri.png"

image luz oneflip = Transform("images/story3/char/luz one.png", xzoom=-1)
image luz triflip = Transform("images/story3/char/luz tri.png", xzoom=-1)

#BACKGROUNDS
image bg hallway = "images/story3/bg hallway.jpg"
image bg streetmorning = "images/story3/bg streetmorning.jpg"
image bg classroomtwo = "images/story3/bg classroomtwo.jpg"

label three_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: KLASE{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg streetmorning with fade
    "LUNES NG UMAGA, MAAGANG UMALIS ANG MAGPINSAN NA SI LUZ AT ALLAN PAPASOK SA PAARALAN."
    "NAGLALAKAD LAMANG SILA PATUNGO SA PAARALAN DAHIL MALAPIT LAMANG ITO SA KANILANG BARANGGAY."
    "HABANG SILA AY NAGLALAKAD AY NAKASALUBONG NILA SI MANG JOSE, ANG KANILANG LOLO AT KINAUSAP SILA NITO."

    show luz mano at left 
    show allan one at slightleft
    show mangjose one at right
    with dissolve
    luz "Magandang umaga po lolo Jose, mano po."
    show allan mano with dissolve
    allan "Mano po."
    show mangjose tri with dissolve
    mangjose "Ang aaga talaga magsipasok ng aking mga apo nakakatuwa naman at talagang kay sisipag ninyo magsipasok sa eskwela."
    show allan one
    allan "Opo lolo, payo po kasi sa amin nina mama at papa na sikapin na maging maaga pumasok upang hindi mahuli sa klase."
    show luz tri
    luz "Nakakatuwa rin po kasi pag maagang pumapasok sa eskwela at hindi po namin kailangan magmadali bago magbell."
    show mangjose one
    mangjose "Tama yan mga apo. Oh sya sige lumakad na kayo."
    show mangjose tri
    mangjose "Mag ingat kayo at palaging tumingin muna sa kaliwa at kanan bago tumawid."
    show luz one
    luz "Opo lolo, kayo rin po mag ingat po kayo."

    scene bg hallway with fade
    "AT NAGPATULOY NA MULI SA PAGLAKAKAD ANG MAGPINSAN PATUNGO SA PAARALAN."
    "NANG NAGLALAKAD NA SILA SA HALLWAY AY NAKITA NILA ANG KANILANG GURO NA SI BINIBINING REYES."

    show luz one at left
    show allan one at slightleft
    show reyes bitbit at right
    with dissolve
    luz "Magandang umaga po Binibining Reyes."
    show allan mano 
    show reyes one
    with dissolve
    allan "Magandang umaga po Ma'am. Kami na po ang magbibitbit ng inyong mga dala."
    show allan one
    show reyes tri
    reyes "Magandang umaga rin sa inyo, nakakatuwa naman at ang aga ninyo palagi pumasok magpinsan."
    show reyes one
    reyes "Salamat rin dahil nagboluntaryo kayo sa pagbibitbit ng aking mga dala."
    allan "Walang anuman po Ma'am."

    hide allan
    hide luz
    hide reyes
    with dissolve
    "AT KINUHA NA NILA ANG MGA GAMIT NI BINIBINING REYES AT NAGLAKAD NA SILA PAPUNTA SA KANILANG SILID-ARALAN."

    scene bg classroomtwo with fade
    "NAG-UUSAP ANG GURO AT ANG MGA MAG-AARAL TUNGKOL SA MAGAGANDANG KAUGALIAN AT KULTURA NG IBA'T IBANG PANGKAT ETNIKO SA ATING BANSA."
    show reyes tri at right with dissolve
    reyes "Pag-uusapan natin ngayong umaga ang mga kultura at kaugalian ng iba't ibang pangkat etniko sa ating bansa"
    show reyes one
    reyes "Anong pangkat etniko ang kinabibilangan ninyo?"
    show eden tri at left with moveinleft
    eden "Ako po ay nabibilang sa pangkat ng Mangyan"
    hide eden with moveoutleft
    reyes "Ano-ano ang mga kabilang sa pangkat Mangyan?"

    show luz decision with zoomin
    menu:
        
        luz "ANO ANG DAPAT KONG GAWIN KAHIT ALAM KO ANG SAGOT?"
        "TUMAAS NG KAMAY":
            jump taas_3
        "HINDI NALANG SUMAGOT":
            jump hindi_3

label taas_3:
    show luz taas at left
    luz "Ma'am ako po. Ang mga pangkat ng mangyan ay"
    show luz tri
    luz "Alangan, Hanunoo, Batangan, Tadyawan, Iraya, Ratagnon, Buhid, Manguianes, Tiron,"
    show luz one
    luz "Lactan, Buquit, Barangan, Tagaydan, Pula, Nauhan, at Buid."
    show reyes tri
    reyes "Magaling Luz tama ang sagot mo."
    hide luz with moveoutleft
    jump choice_3

label hindi_3:
    show gemma taas at left
    hide luz
    gemma "Ma'am ako po, alam ko po ang sagot. Ang mga pangkat po ng mangyan ay"
    show gemma one
    gemma "Alangan, Hanunoo, Batangan, Tadyawan, Iraya, Ratagnon, Buhid, Manguianes, Tiron,"
    show gemma tri
    gemma "Lactan, Buquit, Barangan, Tagaydan, Pula, Nauhan, at Buid."
    show reyes tri
    reyes "Magaling Gemma tama ang sagot mo."
    hide gemma
    hide reyes
    show luz two at center with dissolve
    luz "Sayang sana pala ako yung sumagot tama pala ang naiisip ko na sagot."
    hide luz
    jump choice_3

label choice_3:
    show reyes one at right
    reyes "Sunod naman mayaman tayo sa iba't ibang laro. Ano ang alam ninyong tradisyunal na mga laro ng iba't ibang pangkat etniko?"
    show allan tri at left with moveinleft
    allan "Ilan po sa mga nalalaman kong laro ay ang patintero, taguan, pagbubuno ng mga paa o feet wresting, at tatsing."
    show allan one
    allan "Ngunit, isa sa pinakakilalang laro ay ang mga taguan, o tinatawag din ng ibang pangkat etniko bilang tinnabunan."
    show allan tri
    allan "Ito po ay nilalaro ng mga bata at pati na rin ng mga matatanda. At alam niyo po ba na hindi lamang ito nilalaro sa Pilipinas,"
    show allan one
    allan "kung hindi pati na rin sa ibang mga bansa sa Timog-Silangang Asya tulad ng Indonesia at Thailand."
    hide allan with moveoutleft
    show reyes tri
    reyes "Ano-ano naman ang mga tradisyunal na instrumentong pang-musika ang inyong nalalaman?"
    show gloren tri at left with moveinleft
    gloren "Ang gangsa, abellao at awedeng ay ilan lamang sa mga tradisyunal na instrumentong pangmusika sa bansa."
    show gloren one
    gloren "Sa iloilo po ay kilala ang tulali, isang instrumento pong anyong plawta."
    show gloren tri
    gloren "Ang kudyapi po ay karaniwang ginagamit at makikita sa maraming lugar sa bansa,"
    show gloren one
    gloren "tulad ng Palawan at Cotabato. Ito po ay katutubong gitara."
    hide gloren with moveoutleft
    show reyes one
    reyes "Ano naman ang alam ninyong mayamang kultura ng mga pangkat etniko sa Mindanao?"
    show john tri at left with moveinleft
    john "Ma'am, ang tribong T'boli ay humahabi ng tnalak."
    hide john with moveoutleft
    show gemma tri at left with moveinleft
    gemma "Tradisyunal na tela na galing sa abaka na hinabi sa kamay," 
    show gemma one
    gemma "pangunahing kulay ng mga ito ang pula, itim at orihinal na kulay ang dahon ng abaka."
    hide gemma with moveoutleft
    show ezekiel tri at left with moveinleft
    ezekiel "Sinasabi raw po na kumukuha ng inspirasyon ang mga T'boli sa kanilang panaginip kaya malikhain ang mga disenyo ng mga tnalak."
    hide ezekiel with moveoutleft
    show reyes tri
    reyes "Bukas, pag-uusapan naman natin ang kultura ng mga Kankanaey at iba pang pangkat etniko."
    show reyes close
    reyes "Basahin ninyo sa inyong aklat sa Araling Panlipunan ang tungkol sa kanila."
    show reyes tri
    reyes "Tapos na ang klase ngunit maiwan ang mga nakatakdang maglinis ng silid-aralan ngayong araw."
    show reyes one
    reyes "Para mapanatili ang kalinisan ng ating kapaligiran."
    hide reyes with dissolve
    "AT NAIWAN NA SINA LUZ AT ALLAN PARA MAGLINIS NG SILID-ARALAN."
    show allan one at left
    show luz oneflip at right
    with dissolve
    allan "Sige Luz ako ang magaayos ng upuan at ikaw naman ang magwalis."
    show luz triflip
    luz "Sige, ngunit nasaan ang walis?"
    show allan tri
    allan "Hanapin mo ang walis sa bodega."
    call screen interactive3 with dissolve

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

screen interactive3:
    add "images/story3/bg hanapwalis.png"

    imagebutton:
        xpos 600
        ypos 300
        idle "images/story3/walis_idle.png"
        hover "images/story3/walis_hover.png"
        action Jump("foundwalis")

    draggroup:
        drag:
            drag_name "box"
            child "images/story3/box.png"
            xpos 600
            ypos 310
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "shovel"
            child "images/story3/shovel.png"
            xpos 400
            ypos 290
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "box2"
            child "images/story3/box.png"
            xpos 400
            ypos 300
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "rake"
            child "images/story3/rake.png"
            xpos 540
            ypos 220
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "box3"
            child "images/story3/box.png"
            xpos 500
            ypos 250
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "gloves"
            child "images/story3/gloves.png"
            xpos 650
            ypos 400
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

label foundwalis:
    scene black
    "MATAPOS MAKITA ANG WALIS AY NAGSIMULA NA SILANG MAGLINIS AT PAGKATAPOS AY UMUWI NA SILA SA KANILANG TAHANAN."
    centered "MORAL: PAGPAPAHALAGA SA KULTURA AT KAPALIGIRAN."
    jump quiz_3

label quiz_3: #change _3 to _4 to copy for next quiz
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_3 = 0 
    default percent_3 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_3 = 0 
    call screen question1_3 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_3: 
    $ points_3 += 1
    call screen question2_3 with circlewipe
label wronganswer1one_3:
    call screen question2_3 with circlewipe
label wronganswer1two_3:
    call screen question2_3 with circlewipe

label correctanswer2_3: 
    $ points_3 += 1
    call screen question3_3 with circlewipe
label wronganswer2two_3:
    call screen question3_3 with circlewipe
label wronganswer2one_3:
    call screen question3_3 with circlewipe

label correctanswer3_3: 
    $ points_3 += 1
    call screen question4_3 with circlewipe
label wronganswer3two_3:
    call screen question4_3 with circlewipe
label wronganswer3one_3:
    call screen question4_3 with circlewipe

label correctanswer4_3: 
    $ points_3 += 1
    call screen question5_3 with circlewipe
label wronganswer4_3:
    call screen question5_3 with circlewipe

label correctanswer5_3: 
    $ renpy.block_rollback()
    $ points_3 += 1
    $ persistent.current_3 = points_3
    $ renpy.choice_for_skipping()
    if points_3 == 4:
        $ persistent.three = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_3 == 5:
        $ persistent.three = True
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
    
label wronganswer5_3:
    $ renpy.block_rollback()
    $ persistent.current_3 = points_3
    $ renpy.choice_for_skipping()
    if points_3 == 4:
        $ persistent.three = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_3 == 5:
        $ persistent.three = True
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


screen question1_3:
    add "images/story3/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story3/qc/a1_idle.png"
        hover "images/story3/qc/a1_hover.png"
        action Jump("wronganswer1two_3")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story3/qc/b1_idle.png"
        hover "images/story3/qc/b1_hover.png"
        action Jump("correctanswer1_3")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story3/qc/c1_idle.png"
        hover "images/story3/qc/c1_hover.png"
        action Jump("wronganswer1one_3")

screen question2_3:
    add "images/story3/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story3/qc/a2_idle.png"
        hover "images/story3/qc/a2_hover.png"
        action Jump("correctanswer2_3")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story3/qc/b2_idle.png"
        hover "images/story3/qc/b2_hover.png"
        action Jump("wronganswer2two_3")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story3/qc/c2_idle.png"
        hover "images/story3/qc/c2_hover.png"
        action Jump("wronganswer2one_3")

screen question3_3:
    add "images/story3/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story3/qc/a3_idle.png"
        hover "images/story3/qc/a3_hover.png"
        action Jump("correctanswer3_3")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story3/qc/b3_idle.png"
        hover "images/story3/qc/b3_hover.png"
        action Jump("wronganswer3one_3")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story3/qc/c3_idle.png"
        hover "images/story3/qc/c3_hover.png"
        action Jump("wronganswer3two_3")

screen question4_3:
    add "images/story3/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer4_3")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer4_3")

screen question5_3:
    add "images/story3/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer5_3")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer5_3")