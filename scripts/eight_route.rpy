#CHARACTER NAMES AND NAME COLOR
define christine = Character("Christine", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define nathan = Character("Nathan", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define jerry = Character("Jerry", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define mateo = Character("Mateo", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define hannah = Character("Hannah", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

define ginangramos = Character("Ginang Ramos", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image christine one = "images/story8/char/christine one.png"
image christine two = "images/story8/char/christine two.png"
image christine tri = "images/story8/char/christine tri.png"

image ginangramos one = "images/story8/char/ginangramos one.png"
image ginangramos two = "images/story8/char/ginangramos two.png"
image ginangramos tri = "images/story8/char/ginangramos tri.png"

image hannah one = "images/story8/char/hannah one.png"
image hannah two = "images/story8/char/hannah two.png"
image hannah tri = "images/story8/char/hannah tri.png"

image jerry one = "images/story8/char/jerry one.png"
image jerry two = "images/story8/char/jerry two.png"
image jerry tri = "images/story8/char/jerry tri.png"

image mateo one = "images/story8/char/mateo one.png"
image mateo two = "images/story8/char/mateo two.png"
image mateo tri = "images/story8/char/mateo tri.png"

image nathan one = "images/story8/char/nathan one.png"
image nathan two = "images/story8/char/nathan two.png"
image nathan tri = "images/story8/char/nathan tri.png"

image nathan oneflip = Transform("images/story8/char/nathan one.png", xzoom=-1)
image nathan triflip = Transform("images/story8/char/nathan tri.png", xzoom=-1)
image mateo oneflip = Transform("images/story8/char/mateo one.png", xzoom=-1)
image mateo triflip = Transform("images/story8/char/mateo tri.png", xzoom=-1)

label eight_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: GALING NG PILIPINO{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg hallway with fade
    "NAIPAKIKITA ANG KAHUSAYAN SA PAGLIKHA NG ILANG MGA PILIPINO SA KANILANG MAHUSAY NA PAGGAWA SA LARANGAN NG NEGOSYO, SINING, PAMUMUNO, AT PANANALIKSIK?"
    "SA PAMAMAGITAN NG ANGKING GALING, MAY MGA NATATANGING PILIPINO NA KAYANG MAGING ISANG MAHUSAY NA PINTOR O DI KAYA'Y MAGALING NA MUSIKERO."
    "TUNAY NA KATANGI-TANGI ANG MARAMING PILIPINO AT DAPAT LANG NA SILA AY ATING HANGAAN AT GAWING MODELO NG KUNG ANO ANG GUSTO NATING MARATING SA ATING BUHAY."

    scene bg classroomtwo with dissolve
    "ANG GURO NA SI GNG. RAMOS AT KANIYANG KLASE AY NAG-UUSAP USAP TUNGKOL SA MAGALING AT MATAGUMPAY NA MGA PILIPINO SA IBA'T IBANG LARANGAN."
    "KAGAYA SA LARANGAN NG MUSIKA NA SI LEA SALONGA."
    "AT SA LARANGAN NG SINING AT PAGSAYAW NA GRUPO NG EL GAMMA PENUMBRA."
    show ginangramos tri at center with dissolve
    ginangramos "Mga bata sino sa inyo ang may kilala kay Lea Salonga?"
    hide ginangramos with dissolve
    "MARAMING BATA ANG TUMAAS NG KAMAY NA GUSTO SUMAGOT."
    show ginangramos tri at right with moveinright
    ginangramos "Sige, Christine sino si Lea Salonga?"
    hide ginangramos with moveoutright
    show christine tri at left with moveinleft
    christine "Si Maria Lea Carmen Imutan Salonga ay mas kilala bilang Lea Salonga."
    show christine one
    christine "Ipinanganak po siya noong Pebrero 22, 1971. Una po siyang nakilala sa The King and I ng Repertory Philippines noong siya'y pitong taong gulang pa lamang."
    show christine tri
    christine "Sa edad na sampung taon, inirekord ni Lea ang awiting Small Voice. Iyon ang naging simula ng kaniyang karera bilang isa sa mga sikat na aktres at mang-aawit sa Pilipinas."
    hide christine with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Salamat Christine. Sino pa ang nais magdagdag?"
    hide ginangramos with moveoutright
    show jerry tri at left with moveinleft
    jerry "Nagsimula po ang kaniyang katanyagan sa ibang bansa noong siya ay napiling gumanap bilang Kim sa tagumpay na musikal na Miss Saigon noong 1989."
    show jerry one
    jerry "Noong 1993, si Lea ay gumanap bilang Eponine, isang batang ulila sa Broadway production na Les Miserables."
    show jerry tri
    jerry "Ang tagumpay ni Lea sa Pilipinas at sa iba pang mga bansa,"
    show jerry one
    jerry "Ang siyang nagbukas ng oportunidad sa iba pang Pilipino entertainers upang makilala at kinalaunan ay nag-alay din ng karangalan sa ating bansa."
    hide jerry with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Salamat Jerry. Ano naman ang mga award na natanggap niya?"
    hide ginangramos with moveoutright
    show mateo tri at left with moveinleft
    mateo "Nagtamo siya ng mga gantimpala mula sa pinakarespetadong tagapaggawad ng parangal, at itinanghal bilang kauna-unahang Pilipina na,"
    show mateo one
    mateo "Nagkamit ng Laurence Olivier Award, Tony Award, Drama Desk, Outer Critics Circle at ang Theatre World Award para sa natatangi niyang pagganap bilang Kim."
    hide mateo with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Magaling mga bata. Natutuwa ako dahil kilala niyo talaga si Lea Salonga."
    show ginangramos one
    ginangramos "Sumunod naman ay ating pag-uusapan ang grupo ng El Gamma Penumbra, ang kampeon sa Asia's Got Talent."
    show ginangramos tri
    ginangramos "Sino naman ang may kilala sa kanila?"
    hide ginangramos with moveoutright
    show hannah tri at left with moveinleft
    hannah "Ang El Gamma Penumbra ay bahagi po ng kampanya ng turismo ng Pilipinas, ang \"Choose Philippines\"."
    show hannah one
    hannah "Mula sa bayan ng Tanauan sa Batangas, nabuo ang grupo noong 2010 upang sumayaw ng shadow play."
    show hannah tri
    hannah "Ang kanilang mga mensahe ay patungkol sa kaguluhan, kalikasan, pagmamalaki bilang Pilipino at iba pa ay ibinabahagi nila sa bawat palabas na ginagawa nila."
    show hannah one
    hannah "Hindi naging madali sa grupo na makamit ang kanilang tagumpay. Ang kanilang kahusayan at kasipagan sa napili nilang larangan ang naging daan sa kanilang pangarap."
    show hannah tri
    hannah "May mga pagkakataon din na hindi sila nananalo ngunit sa kabila ng lahat, buo ang kanilang paniniwala sa kanilang ginagawa."
    hide hannah with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Salamat Hannah. Kailan naman ang pinakamahalagang araw sa grupo ng mga kalahok sa Asia's Got Talent."
    hide ginangramos with moveoutright
    show nathan tri at left with moveinleft
    nathan "Mayo 7, 2015 po ang pinakamahalagang araw sa grupo ng mga kalahok sa patimpalak."
    show nathan one
    nathan "Ibinida ng mga Pilipino ang galing ng mga Pinoy nang tanghaling kampeon ang El Gamma Penumbra."
    hide nathan with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Salamat Nathan. Idagdag ko na rin,"
    show ginangramos one
    ginangramos "Tunay nga na matagumpay at kilala na ang kanilang grupo, subalit sa kabila nito, hindi nila nakakalimutang magpasalamat sa pamamagitan ng pagbibigay ng mga donasyon."

    scene black with dissolve
    "NATAPOS NA ANG KLASE SA UNANG SUBJECT AT SUMUNOD NAMAN AY ANG ARALING PANLIPUNAN."

    scene bg classroomtwo with dissolve
    show ginangramos tri at center with dissolve
    ginangramos "Ngayon naman ay magtutungo na tayo sa susunod na subject na Araling Panlipunan."
    show ginangramos one
    ginangramos "Pag-aaralan natin ang Kalikasan, mga batas sa pangangalaga nito at mga pinagkukunang-yaman para sa kabuhayan."
    show ginangramos tri at right with moveinright
    ginangramos "Bilang panimula, ano para sa inyo ang kahulugan ng Kalikasan?"
    hide ginangramos with moveoutright
    show hannah tri at left with moveinleft
    hannah "Ang kalikasan po ay tumutukoy sa lahat ng nakapaligid sa atin na maaaring may buhay o wala."
    show hannah one
    hannah "Ito ay kinabibilangan ng mga puno't halaman at lahat ng iba't ibang uri ng hayop mula sa maliit hanggang sa malaki."
    show hannah tri
    hannah "Ang tao at kalikasan ay magkaugnay. Ang kalikasan ang nagkakaloob sa tao ng kaniyang pangangailangan para mabuhay."
    show hannah one
    hannah "Ang tao naman ang nangangalaga sa kalikasan upang mapanatili ito. Kailangan ng tao ang kalikasan. Kailangan naman ng kalikasan ang tao."
    hide hannah with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Salamat Hannah. Tama ang sagot mo."
    show ginangramos one
    ginangramos "Sunod naman ay ang mga batas pambansa at pandaigdig tungkol sa pangangalaga sa Kalikasan."
    show ginangramos tri
    ginangramos "Ang una ay Batas Pambansa 7638 (Department of Energy Act of 1992). Pagtatatag sa Department of Energy (DOE)."
    show ginangramos one
    ginangramos "Layunin nitong isaayos, subaybayan, at isakatuparan ang mga plano at programa ng pamahalaan sa eksplorasyon, pagpapaunlad at konserbasyon ng enerhiya."
    show ginangramos tri
    ginangramos "Ano pa ang mga batas na may kinalaman sa pangangalaga sa kalikasan?"
    hide ginangramos with moveoutright
    show christine tri at left with moveinleft
    christine "Isa po ay ang RA 8749 o \"Philippine Clean Air Act\" ang batas na ito ay naglalayong panatilihing malinis at ligtas ang hanging nilalanghap ng mga mamamayan."
    hide christine with moveoutleft
    show jerry tri at left with moveinleft
    jerry "Sunod naman po ay RA 9275 o \"Philippine Clean Water Act\" ang batas na ito ay bilang pagkilala sa kalinisan ng tubig para sa mamamayan."
    hide jerry with moveoutleft
    show nathan tri at left with moveinleft
    nathan "Sunod naman po ay RA 7586 o \"National Integrated Protected Areas System Act of 1992\""
    show nathan one
    nathan "Ang batas na ito ay naglalayong protektahan ang mga lugar na kinikilalang luklukan ng mga uri ng hayop at halaman na may kaunting bilang na lamang at nanganganib na mapuksa."
    hide nathan with moveoutleft
    show mateo tri at left with moveinleft
    mateo "Sunod naman po ay RA 9147 o \"Wildlife Resources Convervation and Protection Act\""
    show mateo one
    mateo "Ang layunin ng batas na ito ay konserbasyon at pagbibigay proteksyon sa mga maiilap na hayop at kanilang habitas upang mapanatili ang ecological diversity."
    hide mateo with moveoutleft
    show christine tri at left with moveinleft
    christine "Ang panghuli ay RA 9003 o \"Ecological Solid Waste Management Act of 2000\""
    show christine one
    christine "Ang layunin ng batas na ito ay tungkol sa tamang paraan ng pangongolekta at pagbubukod-bukod ng mga solid waste sa mga barangay."
    hide christine with moveoutleft
    show ginangramos tri at right with moveinright
    ginangramos "Tama ang inyong mga sagot. Ngayon ay maaari na kayong magrecess."

    scene bg hallway with dissolve
    show jerry one with dissolve
    "HABANG NAGRERECESS NAKATANGGAP NG TEXT SI JERRY MULA SA KANIYANG KAIBIGAN."
    scene bg textone with dissolve
    centered ""
    show bg texttwo
    play sound "audio/sent.mp3"
    centered ""
    show bg textthree
    play sound "audio/sent.mp3"
    centered ""
    show bg textfour
    play sound "audio/sent.mp3"
    centered ""
    show bg textfive
    play sound "audio/sent.mp3"
    centered ""

    scene bg hallway
    show jerry two with zoomin
    menu:
        jerry "ANO ANG GAGAWIN KO?"
        "SUMAMA SA KAIBIGAN":
            jump sumama_8
        "PUMASOK SA KLASE":
            jump pumasok_8

label sumama_8:
    scene black with dissolve
    "NAGPUNTA SINA JERRY SA COMPUTERSHOP MALAPIT SA KANILANG PAARALAN."
    "MAYA-MAYA NAPADAAN ANG KANIYANG NANAY. NAPANSIN SILA NITO AT KINAUSAP."
    "NUNG NALAMAN NG KANIYANG NANAY ANG KATOTOHANAN, PINAGALITAN SIYA NITO AT PINAUWI NA SA KANILANG BAHAY."
    
    "SAMANTALA, SA PAARALAN."


label pumasok_8:
    scene bg classroomtwo with dissolve
    "MATAPOS ANG RECESS AY NAGPATULOY NA ULIT ANG KLASE."
    show ginangramos tri at right with dissolve
    ginangramos "Bilang pagpapatuloy sa ating natalakay kanina. Ngayon naman ay pagaaralan natin ang patungkol sa pinagkukunang-yaman para sa kabuhayan."
    show ginangramos one
    ginangramos "Ang pinagkukunang-yaman ay mga bagay na ginagamit ng tao upang tugunan ang kaniyang pangangailangan at kagustuhan."
    show ginangramos tri
    ginangramos "Ang halimbawa ng yamang lupa ay Palayan kung saan maaaring magtanim at mag-ani."
    show ginangramos one
    ginangramos "Ang halimbawa naman ng yamang tubig ay Dagat kung saan maaaring mangisda ang mga mamamayan."

    scene black with dissolve
    "AT NAGPATULOY ANG KLASE PATUNGKOL SA MGA PINAGKUKUNANG-YAMAN."

    scene bg classroomtwo with dissolve
    "MATAPOS ANG KLASE AY MAY INANUNSYO ANG GURO SA KLASE."
    show ginangramos tri at right with moveinright
    ginangramos "Mga bata magkakaroon ng paligsahan ang bawat seksyon sa paggawa ng parol dahil ngayon ay buwan ng disyembre."
    show ginangramos one
    ginangramos "Nais kong gamitin ninyo ang oras na ito upang pagplanuhan ang magiging disenyo ng inyong parol na gagawin."
    show christine tri at left with moveinleft
    christine "Sige po ma'am."

    scene black with dissolve
    "NAGPULONG PULONG ANG MGA BATA TUNGKOL SA DISENYO NA NAIS NILANG GAWIN."

    scene bg classroomtwo 
    show christine tri at left
    show hannah one at slightleft
    show mateo oneflip at right
    show nathan oneflip at slightright
    with dissolve
    christine "Ano ang gusto ninyong disenyo para sa ating parol?"
    show christine one
    show nathan triflip
    nathan "Dapat makulay para maganda tingnan!"
    show nathan oneflip
    show mateo triflip
    mateo "Oo nga dapat matingkad ang kulay na pula at berde."
    show mateo oneflip
    show hannah tri
    hannah "Gumamit tayo ng mga recycled materials."
    show hannah one
    show nathan triflip
    nathan "Sakto marami sa aming mga bote, magasin at dyaryo."

    scene black with dissolve
    "MATAPOS ANG PAGPUPULONG NG MGA BATA AY BUMALIK NA SI GNG. RAMOS."

    scene bg classroomtwo with dissolve
    show ginangramos tri at right with moveinright
    ginangramos "Ano ang mga napag-usapan ninyo?"
    show ginangramos one
    show christine tri at left with moveinleft
    christine "Maganda po ang idea ng bawat isa. Pagsasama-samahin namin ito upang mabuo ang parol ng maganda at maayos."

    scene black with dissolve
    "NATUWA SI GNG. RAMOS SA NARINIG. NGAYON PA LANG AY NARARAMDAMAN NA NIYA ANG TAGUMPAY NG MGA BATA."
    
    "AT BILANG PAGTATAPOS NG PULONG, ITO ANG SINABI NIYA SA MGA MAG-AARAL:"

    "LAHAT NG PUNA O OPINYON AY NAGBIBIGAY NG PAGSUBOK UPANG LALO PANG MAGSUMIKAP ANG BAWAT ISA. ANG PAGGALANG SA OPINYON AY IKABUBUTI NG BAWAT GAWAIN AT PAGSASAMA."

    centered "MORAL: PAGKILALA SA TALENTO NG IBA, PINAGKUKUNANG-YAMAN AT PAGGALANG SA OPINYON NG KAPWA."
    jump quiz_8

label quiz_8: 
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_8 = 0 
    default percent_8 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_8 = 0 
    call screen question1_8 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_8: 
    $ points_8 += 1
    call screen question2_8 with circlewipe
label wronganswer1one_8:
    call screen question2_8 with circlewipe
label wronganswer1two_8:
    call screen question2_8 with circlewipe

label correctanswer2_8: 
    $ points_8 += 1
    call screen question3_8 with circlewipe
label wronganswer2two_8:
    call screen question3_8 with circlewipe
label wronganswer2one_8:
    call screen question3_8 with circlewipe

label correctanswer3_8: 
    $ points_8 += 1
    call screen question4_8 with circlewipe
label wronganswer3two_8:
    call screen question4_8 with circlewipe
label wronganswer3one_8:
    call screen question4_8 with circlewipe

label correctanswer4_8: 
    $ points_8 += 1
    call screen question5_8 with circlewipe
label wronganswer4_8:
    call screen question5_8 with circlewipe

label correctanswer5_8: 
    $ renpy.block_rollback()
    $ points_8 += 1
    $ persistent.current_8 = points_8
    $ renpy.choice_for_skipping()
    if points_8 == 4:
        $ persistent.eight = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_8 == 5:
        $ persistent.eight = True
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
    
label wronganswer5_8:
    $ renpy.block_rollback()
    $ persistent.current_8 = points_8
    $ renpy.choice_for_skipping()
    if points_8 == 4:
        $ persistent.eight = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_8 == 5:
        $ persistent.eight = True
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


screen question1_8:
    add "images/story8/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story8/qc/a1_idle.png"
        hover "images/story8/qc/a1_hover.png"
        action Jump("wronganswer1two_8")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story8/qc/b1_idle.png"
        hover "images/story8/qc/b1_hover.png"
        action Jump("wronganswer1one_8")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story8/qc/c1_idle.png"
        hover "images/story8/qc/c1_hover.png"
        action Jump("correctanswer1_8")

screen question2_8:
    add "images/story8/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story8/qc/a2_idle.png"
        hover "images/story8/qc/a2_hover.png"
        action Jump("correctanswer2_8")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story8/qc/b2_idle.png"
        hover "images/story8/qc/b2_hover.png"
        action Jump("wronganswer2two_8")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story8/qc/c2_idle.png"
        hover "images/story8/qc/c2_hover.png"
        action Jump("wronganswer2one_8")

screen question3_8:
    add "images/story8/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story8/qc/a3_idle.png"
        hover "images/story8/qc/a3_hover.png"
        action Jump("wronganswer3one_8")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story8/qc/b3_idle.png"
        hover "images/story8/qc/b3_hover.png"
        action Jump("wronganswer3two_8")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story8/qc/c3_idle.png"
        hover "images/story8/qc/c3_hover.png"
        action Jump("correctanswer3_8")

screen question4_8:
    add "images/story8/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer4_8")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer4_8")

screen question5_8:
    add "images/story8/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer5_8")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer5_8")





