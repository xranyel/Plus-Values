#CHARACTER NAMES AND NAME COLOR
define alingluming = Character("Aling Luming", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define mangrobert = Character("Mang Robert", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define wally = Character("Wally", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define miguel = Character("Miguel", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define marlo = Character("Marlo", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define nori = Character("Nori", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image alingluming one = "images/story5/char/alingluming one.png"
image alingluming tri = "images/story5/char/alingluming tri.png"

image mangrobert one = "images/story5/char/mangrobert one.png"
image mangrobert two = "images/story5/char/mangrobert two.png"
image mangrobert tri = "images/story5/char/mangrobert tri.png"

image marlo one = "images/story5/char/marlo one.png"
image marlo two = "images/story5/char/marlo two.png"
image marlo tri = "images/story5/char/marlo tri.png"

image miguel one = "images/story5/char/miguel one.png"
image miguel two = "images/story5/char/miguel two.png"
image miguel tri = "images/story5/char/miguel tri.png"

image nori one = "images/story5/char/nori one.png"
image nori two = "images/story5/char/nori two.png"
image nori tri = "images/story5/char/nori tri.png"

image wally one = "images/story5/char/wally one.png"
image wally two = "images/story5/char/wally two.png"
image wally tri = "images/story5/char/wally tri.png"

image nori oneflip = Transform("images/story5/char/nori one.png", xzoom=-1)
image miguel oneflip = Transform("images/story5/char/miguel one.png", xzoom=-1)

image nori triflip = Transform("images/story5/char/nori tri.png", xzoom=-1)
image miguel triflip = Transform("images/story5/char/miguel tri.png", xzoom=-1)

#BACKGROUNDS
image bg salafive = "images/story5/bg salafive.png"
image bg baranggayloob = "images/story5/bg baranggayloob.png"

label five_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: PAGKAKAISA SA PAGGAWA{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg salafive with fade
    "ANG TAGUMPAY NG ISANG PROYEKTO AY NAKASALALAY SA MARAMING BAGAY. ANG ILAN SA MGA BAGAY NA ITO AY ANG PAGKAKAROON NG KAKAILANGANING GAMIT,"
    "PAGKAKAROON NG MAAYOS NA PLANO, PAGKAKAROON NG MAHUSAY NA PINUNO, AT ILAN PANG MGA BAGAY."
    "NGUNIT ANG PINAKAMAHALAGANG PANGANGAILANGAN AY ANG PAGKAKAISA NG BAWAT MIYEMBRO NG PANGKAT AT PAGTUTULUNGAN NG BAWAT ISA."

    "MAY ILANG BATANG LALAKI NA NAGLALARO NG CHESS SA GARAHE NG BAHAY NI MANG ROBERT."
    "TUMAYO AT NAGSALITA SI MARLO, LIDER NG YOUTH CLUB AT ANAK NI MANG ROBERT."

    show marlo tri at left with moveinleft
    marlo "Halina! Ituloy natin ang trabahong nasimulan natin."
    hide marlo with moveoutleft
    "DAHIL MABABAIT AT MASUNURIN NAMAN ANG MGA BATA, HINDI NA NAGTANONG SI MANG ROBERT KUNG ANO ANG GAGAWIN NILA."

    scene bg streetmorning with fade
    show wally tri at slightleft with moveinleft
    show nori one at left with moveinleft
    wally "Mauuna na po kami, Tito Robert mayroon lang po kaming kukunin sa kabilang kalye."
    show mangrobert tri at slightright with moveinright
    show wally one
    mangrobert "Sasama ka rin ba sa kanila Nori?"
    show mangrobert one
    show nori tri
    nori "Hindi po, Tito Robert. Sasama po ako sa pangkat ni ate Mylene. Magtuturo po kami sa ilang bata ng pagbilang at pagsulat."
    show nori one
    show alingluming tri at right with moveinright
    alingluming "Mga batang guro sila nagtuturo sila sa mga bata tuwing sabado at linggo sa barangay hall."

    scene black with fade
    "NANG MAKAALIS ANG MGA BATA. PINAG-IISIPAN NILA KUNG DAPAT BANG IPAGPATULOY ANG LAYUNIN NG YOUTH CLUB NG KANILANG PAARALAN NA GAGAWIN SA BARANGGAY."

    show bg salafive
    pause 0.1
    show wally one at left
    show marlo one at slightleft
    show nori oneflip at slightright
    show miguel oneflip at right
    with zoomin
    menu:
        
        "IPAGPAPATULOY PA BA NAMIN ANG LAYUNIN NG YOUTH CLUB NG AMING PAARALAN NA GAGAWIN SA BARANGGAY?"
        "OO":
            jump oo_5
        "HINDI":
            jump hindi_5 

label oo_5:
    scene bg baranggayloob with fade
    "NAPAGDESISYONAN NG KANILANG GRUPO NA IPAGPATULOY ANG NASABING LAYUNIN."
    "SI NORI AY NASA BARANGGAY PARA TURUAN ANG MGA BATA."
    show nori one at left with dissolve
    nori "Ngayon mga bata ay tuturuan namin kayo ng pagbilang at pagsulat."
    show nori tri
    nori "Kunin ang inyong mga kwaderno at lapis para makapagsimula sa pagsulat."

    scene bg sulatzero with fade
    centered ""
    show bg sulatone
    centered ""
    show bg sulattwo
    centered ""
    show bg sulatthree
    centered ""
    show bg sulatfour
    centered ""

    scene bg baranggayloob with fade
    show nori tri at left with dissolve
    nori "Ngayon naman tuturuan namin kayo kung paano magbilang."

    scene bg bilangzero with fade
    centered ""
    show bg bilangone
    centered ""
    show bg bilangtwo
    centered ""
    show bg bilangthree
    centered ""
    show bg bilangfour
    centered ""
    show bg bilangfive
    centered ""

    scene bg baranggayloob with fade
    show nori one at left with dissolve
    nori "Ang galing niyo."
    show nori tri
    nori "Bukas ay iba naman ang pag-aaralan natin."
    
    scene bg salafive with fade
    "SA BAHAY NI MANG ROBERT KAUSAP NIYA ANG ANAK NA SI MARLO AT ANG KAIBIGAN NITONG SI MIGUEL."
    show marlo tri at slightleft
    show miguel one at left
    show mangrobert one at right
    with dissolve
    marlo "Itay, ipagpapatuloy po ng Youth Club namin sa paaralan ang gawain namin sa barangay."
    
    scene black with dissolve
    "PAGKALIPAS NG ILANG ORAS, BUMALIK SILA SAKAY NG ISANG DYIP. PUNO ANG DYIP NG MGA DIYARYO, BASYO NG BOTE, AT PIRA-PIRASONG BAKAL."

    scene bg salafive
    show marlo tri at slightleft
    show miguel one at left
    show mangrobert one at right
    with dissolve
    marlo "Itay, humingi po kami ng tulong kay Mang david at ibinigay niya po ang hiningi namin!"
    show marlo one
    marlo "narito ang nahingi namin: mga diyaryo, basyo ng bote, at pira-pirasong bakal."
    show mangrobert tri
    mangrobert "Bakal? paano nagkaroon si Mang David ng napakaraming diyaryo, bote, at pira-pirasong bakal?"
    show miguel tri
    miguel "Inutusan po niya ang kaniyang mga kasambahay na kunin ang mga iyon sa kanilang bodega. Sinabihan din niya ang kaniyang mga kaibigan na magbigay."
    show miguel one
    show mangrobert one
    mangrobert "At ano naman ang gagawin ninyo sa mga bagay na iyan?"
    show marlo tri
    marlo "Ipagbibili po namin ang mga iyan."
    show marlo one
    marlo "Pagkatapos, gagamitin po namin ang pera upang bumili ng mga kailangang bagay para sa basketball at volleyball at makapagbigay ng uniporme para sa liga."
    show marlo tri
    marlo "Kapag hindi pa ito sapat, binabalak namin na manghingi sa iba na maaaring magbigay. Isa roon si Mang David. Sabi niya, nais niyang sumuporta sa aming layunin." 
    show mangrobert tri
    show marlo one
    mangrobert "Sinong gumawa ng mga tuntunin ninyo sa inyong samahan? lahat ba iyon idea ni Marlo?"
    show miguel tri
    show mangrobert one
    miguel "Pasiya po ng lahat ng miyembro. Tinitiyak po namin na bilang mga miyembro,"
    show miguel one
    miguel "ginagampanan namin ang aming mga pananagutan sa samahan. Lahat kami ay nag-lisip ng mga proyekto at kung paano ipatutupad ang mga ito."
    show mangrobert one
    mangrobert "Ipinagmamalaki ko kayo! napakagaling ng mga ginagawa ninyo para sa pamayanan. Mga batang bayani kayo."
    show mangrobert tri
    mangrobert "Sa ganiyan, inilalayo ninyo ang mga bata sa paggawa ng masama. Natitiyak kong lahat kayo ay magiging mabubuting lider sa hinaharap."

    scene black with dissolve
    "ANG PAKIKIISA SA PROGRAMA NG PAARALAN NA MAKAKATULONG SA IBANG TAO AY NAKAKAGAAN NG KALOOBAN."

    centered "MORAL: MAKIISA SA MGA GAWAIN NA MAY LAYUNIN NA TUMULONG SA KAPWA."
    jump quiz_5

label hindi_5:
    scene bg salafive with fade
    "NAPAGDESISYONAN NG KANILANG GRUPO NA HUWAG NA LAMANG MUNA IPAGPATULOY ANG NASABING LAYUNIN."
    show wally one at left
    show marlo tri at slightleft
    show nori oneflip at slightright
    show miguel oneflip at right
    with dissolve
    marlo "Siguro ay huwag na muna natin ipagpatuloy ang plano nating gawin na pagtulong sa baranggay."
    show marlo one
    show nori triflip
    nori "Ano ang dahilan? hindi natin ipagpapatuloy ang ating layunin."
    show nori oneflip
    show miguel triflip
    miguel "Hindi sapat ang oras para maisagawa ang layunin dahil madami din tayong ginagawa sa paaralan."
    show miguel oneflip
    show wally tri
    wally "Saka nalang natin ipagpatuloy kapag kailangan na itong masolusyonan."

    scene black with dissolve
    "AT NAGDAAN ANG MGA ARAW NAPANSIN NG GRUPO NA MARAMING BATA ANG KAILANGAN MATUTO NG PAGBILANG AT PAGSULAT."
    "AT WALANG BADYET ANG BARANGGAY PARA SA LIGA."
    jump oo_5


label quiz_5: 
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_5 = 0 
    default percent_5 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_5 = 0 
    call screen question1_5 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_5: 
    $ points_5 += 1
    call screen question2_5 with circlewipe
label wronganswer1one_5:
    call screen question2_5 with circlewipe
label wronganswer1two_5:
    call screen question2_5 with circlewipe

label correctanswer2_5: 
    $ points_5 += 1
    call screen question3_5 with circlewipe
label wronganswer2two_5:
    call screen question3_5 with circlewipe
label wronganswer2one_5:
    call screen question3_5 with circlewipe

label correctanswer3_5: 
    $ points_5 += 1
    call screen question4_5 with circlewipe
label wronganswer3two_5:
    call screen question4_5 with circlewipe
label wronganswer3one_5:
    call screen question4_5 with circlewipe

label correctanswer4_5: 
    $ points_5 += 1
    call screen question5_5 with circlewipe
label wronganswer4_5:
    call screen question5_5 with circlewipe

label correctanswer5_5: 
    $ renpy.block_rollback()
    $ points_5 += 1
    $ persistent.current_5 = points_5
    $ renpy.choice_for_skipping()
    if points_5 == 4:
        $ persistent.five = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_5 == 5:
        $ persistent.five = True
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
    
label wronganswer5_5:
    $ renpy.block_rollback()
    $ persistent.current_5 = points_5
    $ renpy.choice_for_skipping()
    if points_5 == 4:
        $ persistent.five = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_5 == 5:
        $ persistent.five = True
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


screen question1_5:
    add "images/story5/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story5/qc/a1_idle.png"
        hover "images/story5/qc/a1_hover.png"
        action Jump("wronganswer1two_5")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story5/qc/b1_idle.png"
        hover "images/story5/qc/b1_hover.png"
        action Jump("correctanswer1_5")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story5/qc/c1_idle.png"
        hover "images/story5/qc/c1_hover.png"
        action Jump("wronganswer1one_5")

screen question2_5:
    add "images/story5/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story5/qc/a2_idle.png"
        hover "images/story5/qc/a2_hover.png"
        action Jump("correctanswer2_5")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story5/qc/b2_idle.png"
        hover "images/story5/qc/b2_hover.png"
        action Jump("wronganswer2two_5")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story5/qc/c2_idle.png"
        hover "images/story5/qc/c2_hover.png"
        action Jump("wronganswer2one_5")

screen question3_5:
    add "images/story5/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story5/qc/a3_idle.png"
        hover "images/story5/qc/a3_hover.png"
        action Jump("wronganswer3one_5")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story5/qc/b3_idle.png"
        hover "images/story5/qc/b3_hover.png"
        action Jump("correctanswer3_5")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story5/qc/c3_idle.png"
        hover "images/story5/qc/c3_hover.png"
        action Jump("wronganswer3two_5")

screen question4_5:
    add "images/story5/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer4_5")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer4_5")

screen question5_5:
    add "images/story5/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer5_5")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer5_5")