#CHARACTER NAMES AND NAME COLOR
define lily = Character("Lily", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define blessy = Character("Blessy", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define vicente = Character("Vicente", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define simon = Character("Simon", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")
define LnB = Character("Lily at Blessy", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

define lola = Character("Lola", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define pari = Character("Pari", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define ggonzales = Character("Ginang Gonzales", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image ggonzales one = "images/story9/char/ggonzales one.png"
image ggonzales two = "images/story9/char/ggonzales two.png"
image ggonzales tri = "images/story9/char/ggonzales tri.png"

image lily one = "images/story9/char/lily one.png"
image lily two = "images/story9/char/lily two.png"
image lily tri = "images/story9/char/lily tri.png"
image lilys one = "images/story9/char/lilys one.png"
image lilys two = "images/story9/char/lilys two.png"
image lilys tri = "images/story9/char/lilys tri.png"

image blessy one = "images/story9/char/blessy one.png"
image blessy two = "images/story9/char/blessy two.png"
image blessy tri = "images/story9/char/blessy tri.png"
image blessys one = "images/story9/char/blessys one.png"
image blessys two = "images/story9/char/blessys two.png"
image blessys tri = "images/story9/char/blessys tri.png"

image lola one = "images/story9/char/lola one.png"
image lola two = "images/story9/char/lola two.png"
image lola tri = "images/story9/char/lola tri.png"

image pari one = "images/story9/char/pari one.png"
image pari tri = "images/story9/char/pari tri.png"

image simon one = "images/story9/char/simon one.png"
image simon two = "images/story9/char/simon two.png"
image simon tri = "images/story9/char/simon tri.png"

image vicente one = "images/story9/char/vicente one.png"
image vicente two = "images/story9/char/vicente two.png"
image vicente tri = "images/story9/char/vicente tri.png"
image vicente decision = "images/story9/char/vicente decision.png"
image vicente yosi = "images/story9/char/vicente yosi.png"

image vicentes one = "images/story9/char/vicentes one.png"
image vicentes two = "images/story9/char/vicentes two.png"
image vicentes tri = "images/story9/char/vicentes tri.png"

image blessy oneflip = Transform("images/story9/char/blessy one.png", xzoom=-1)
image blessy triflip = Transform("images/story9/char/blessy tri.png", xzoom=-1)

#BACKGROUNDS
image bg church = "images/story9/bg church.jpg"
image bg kalsadatwo = "images/story9/bg kalsadatwo.jpg"

label nine_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: ANG PANANALIG AY ANG PAGTITIWALA SA DIYOS{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg condooutside with fade
    "NANINIWALA TAYO NA MAY DIYOS NA PUMAPATNUBAY SA LAHAT NG ATING MGA GAWAIN. ANG PANANALIG SA DIYOS AY HINDI TAGLAY NG ISANG INDIBIDWAL LAMANG."
    "LAHAT TAYO AY MAY IBAT-IBANG ANTAS NG PANANAMPALATAYA SA DIYOS. MAAARING MAS MALALIM ANG PANINIWALA NG ISA KAYSA SA ISA, NGUNIT PAREHO SILANG MAYROON NITO."
    "MAHALAGA ITO DAHIL GAANO MAN KALIIT ANG PANINIWALA NG ISANG TAO TAGLAY PARIN NITO,"
    "ANG PAG-ASANG SIYA AY MATUTULUNGAN AT MAPAPATAWAD NG DIYOS SA KANIYANG NAGAWANG KASALANAN GAANO MAN ITO KALIIT O KALAKI."

    scene bg condoone with dissolve
    "MAHALAGA ANG PAGMAMAHAL AT PANANAMPALATAYA SA DIYOS PARA SA PAMILYA NI GNG. GONZALES."
    "SINISIKAP NILANG ARAW-ARAW NA MAKAGAWA NG MABUBUTING BAGAY SA IBANG TAO AT MAGING MAKATARUNGAN AT WALANG KINIKILINGAN."

    show bg condotwo
    show lily tri at left
    show blessy tri at slightleft 
    with dissolve
    LnB "Mama, papasok na po kami."
    show lily one
    show blessy one
    show ggonzales tri at right with dissolve
    ggonzales "Sige mga anak, mag-ingat kayo. Maging mabuti kayo palagi at huwag gumawa ng kahit na anong magdudulot ng kahihiyan at panghihinayang."
    show ggonzales one
    show blessy one at slightright with moveinright
    show lily one at slightright with moveinright
    "NIYAKAP AT HINALIKAN SIYA NG KANILANG MGA ANAK."
    show blessy one at slightleft with moveinleft
    show lily tri at left with moveinleft
    lily "Halika na at baka mahuli tayo, istrikto pa naman ang guwardiya."

    scene bg schoolgate with fade
    "BINILISAN NG MAGKAPATID ANG PAGLAKAD UPANG MAKAABOT SA FLAG CEREMONY."
    show vicente yosi at right with dissolve
    "AT HABANG NAGLALAKAD AY NAPANSIN NILA ANG ISA NILANG KAKLASE NA SI VINCENTE NA NANINIGARILYO SA MAY TAPAT NG SCHOOL HINDI MUNA NILA ITO KINAUSAP,"
    "DAHIL NARINIG NA NILA KAAGAD ANG TUNOG NG BELL AT TAHIMIK NA SILANG PUMILA KASAMA ANG KANILANG MGA KAMAG-ARAL."

    scene bg classroom with dissolve
    "PAGKATAPOS NG FLAG CEREMONY AY NAGPUNTAHAN NA ANG MAG-AARAL SA KANI-KANILANG MGA SILID KABILANG NA SINA LILY AT BLESSY."
    "NAPANSIN NILA SI VICENTE AT NAALALA NILA ANG KANILANG NAKITA SA LABAS NG PAARALAN."
    show lily tri at left
    show blessy oneflip at right
    with dissolve
    lily "Blessy diba siya yung napansin natin sa labas ng paaralan?"
    show blessy triflip
    show lily one
    blessy "Oo siya nga yun. Hindi ba bawal ang manigarilyo lalo na ang mga bata pa at ayon din sa batas?"
    show lily tri
    show blessy oneflip
    lily "Oo Blessy masama yun sa kalusugan lalo na at mga bata pa tayo at higit sa lahat hindi iyon nakakalugod sa paningin ng diyos."
    show blessy triflip
    show lily one
    blessy "Ano kaya kung sabihan natin siya na masama iyon? Para itigil na niya ang ganoong gawain."
    show lily tri
    show blessy oneflip
    lily "Oo nga tama ang naisip mo, pagkatapos ng klase ay agad natin siyang lapitan upang kausapin."

    scene black with dissolve
    "AT NAGSIMULA NA ANG KLASE."
    "PAGKALIPAS NG ILANG ORAS AY NATAPOS NA ANG KANILANG KLASE AT NILAPITAN NA NILA ANG KANILANG KAKLASE NA SI VICENTE."

    scene bg hallwaytwo with dissolve
    show lily tri at left
    show blessy one at slightleft
    show vicente two at right
    with dissolve
    lily "Vicente, nakita ka namin kanina na naninigarilyo ka."
    show vicente tri 
    show lily one
    vicente "Oh! ano namang masama don? isusumbong niyo ako?"
    show vicente one
    show blessy tri
    blessy "Hindi ba at masama iyon sa kalusugan."
    show vicente tri
    show blessy one
    vicente "Eh ano naman, minsan lang naman."

    scene black with dissolve
    "AT HINAYAAN NA LAMANG NILA SI VICENTE."

    scene bg classroom with dissolve
    "MAKALIPAS ANG ILANG ARAW NAPANSIN NILA NA HINDI PUMAPASOK NG KLASE SI VICENTE."
    show lily tri at left
    show blessy oneflip at right
    with dissolve
    lily "Blessy parang may napapansin ako."
    show blessy triflip
    show lily one
    blessy "Ano yun Lily."
    show lily tri
    show blessy oneflip
    lily "Parang ilang araw nang hindi pumapasok si vicente simula nung nakausap natin."
    show lily one
    show blessy one at slightleft with moveinleft
    show simon one at right with moveinright
    "AT BIGLANG DUMATING ANG KAIBIGAN NI VICENTE NA SI SIMON AT NAKISALI SA USAPAN NG MAGKAPATID."
    show simon tri
    simon "Alam ko kung bakit ilang araw nang wala si Vicente."
    show simon one
    show blessy tri
    blessy "Bakit, ano ang nangyari sa kaniya?"
    show blessy one
    show simon tri
    simon "Ilang araw na siyang may sakit. Pinuntahan ko siya kahapon kaya aking nalaman."
    show simon one
    show blessy tri
    blessy "Kawawa naman siya."
    scene black with dissolve
    "MAKALIPAS ANG ILANG ARAW AY PUMASOK NA MULI SI VICENTE."
    scene bg classroom with dissolve
    show lily one at left
    show blessy tri at slightleft
    show vicente one at right
    with dissolve
    blessy "Vicente kamusta ka? Balita ko nagkasakit ka daw?"
    show blessy one
    show vicente tri
    vicente "Oo nagkaroon ako ng Asthma dahil daw sa paninigarilyo ko."
    show vicente one
    show blessy tri
    blessy "Naku sabi sayo eh, Dapat matagal mo nang itinigil para hindi ka nagkaroon ng ganang sakit."
    show blessy one
    show lily tri
    lily "Oo nga Vicente mas pangalagaan mo ang iyong kalusugan lalo na at mga bata pa tayo."
    show lily one
    show vicente tri
    vicente "Maraming salamat sa inyong paala sa akin tunay nga na kayo ay mabuti sa inyong kapwa."
    scene black with dissolve
    "AT SIMULA NOON AY NAGING MAGKAKAIBIGAN NA SILA."
    scene bg hallwaytwo with dissolve
    show lily tri at left
    show blessy one at slightleft
    show vicente one at right
    with dissolve
    lily "Vicente may event na gaganapin sa aming simbahan baka nais mong dumalo. Tiyak na mag-eenjoy ka at marami kang makikilala."
    show lily one
    show vicente tri
    vicente "Sige pag-iisipan ko pa."
    show vicente one
    show blessy tri
    blessy "Sige magsabi ka lang sa amin kapag dadalo ka."
    hide blessy
    hide lily
    hide vicente
    show vicente decision at center with zoomin
    menu:
        vicente "SASAMA BA AKO?"
        "OO":
            jump oo_9
        "HINDI":
            jump hindi_9

label oo_9:
    scene bg condoone with dissolve
    "NANG MAKAUWI NA SILA SA KANI-KANILANG TAHANAN NAGBUKAS SI LILY NG KANIYANG LAPTOP PARA MAGGAWA NG TAKDANG ARALIN,"
    "AT BIGLANG NAKATANGGAP SIYA NG MENSAHE MULA KAY VICENTE."
    "SINABI NI VICENTE NA NAIS DAW NIYANG DUMALO SA SIMBAHAN AT SASABAY DAW SIYA SA MAGKAPATID KINABUKASAN."
    #vicente "Lily nais kong dumalo sa inyong simbahan na tinutukoy."
    #lily "Sige aasahan namin ang iyong pagdalo bukas sa simbahan."
    #vicente "Sige Lily sasabay ako sainyo bukas papunta doon."

    scene bg kalsadatwo with fade
    "KINABUKASAN MAGKAKASAMA NA SILANG PAPUNTA SA SIMBAHAN."
    show lola one at left with dissolve
    "HABANG NAGLALAKAD SILA AY NAPANSIN NI LILY AT BLESSY NA MAY LILIBAN NA MATANDA SA KANILANG HARAPAN."
    "TILA ITO AY MALABO NA ANG MGA MATA AT MAY KABAGALAN NA DIN SA PAGLAKAD."
    hide lola
    show lilys one at left
    show blessys tri at slightleft
    show vicentes one at right
    with dissolve
    blessy "Tulungan natin si Lola na makaliban sa kabilang kalsada."
    show blessys one
    show lilys tri
    lily "Sige tulungan natin si lola."
    show lilys one
    show blessys tri
    blessy "Vicente, ikaw sasama ka ba?"
    show blessys one
    show vicentes tri
    vicente "Hindi dito na lang ako hihintayin ko nalang kayo."

    #interactive9 drag drop lola
screen interactive9:

    # A map as background.
    add "images/story9/bg kalsadatwofeature.png"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "liliban"
            child "images/story9/liliban.png"
            droppable False
            dragged detective_dragged
            xpos 300 ypos 543
        

        # The cities they can go to.
        drag:
            drag_name "libanan"
            child "images/story9/libanan.png"
            draggable False
            xpos 891 ypos 336

label tuloy_9:
    call screen interactive9 with dissolve
    scene bg kalsadatwo 
    "AT NAILIBAN NA NGA NILA ANG MATANDA."
    show lola two at right
    show lilys one at left
    show blessys one at slightleft
    with dissolve
    lola "Salamat mga apo pagpalain kayo ng diyos sa inyong kabutihan."
    show blessys tri
    show lilys tri
    LnB "Walang anuman po lola. Ingat po kayo palagi."
    scene black with dissolve
    "NAGPATULOY NA MULING NAGLAKAD ANG TATLONG MAGKAKAIBIGAN."
    scene bg sakayan 
    show lilys one at left
    show blessys one at slightleft
    show vicentes tri at right
    with dissolve
    vicente "Bakit niyo tinulungan yung matandang iyon eh kaya naman niyang maglakad."
    show vicentes one
    show blessys tri
    blessy "Kasi nakakaawa siya at malabo na ang kaniyang mata at may kabagalan na ang paglakad."
    show blessys one
    show lilys tri
    lily "Mapanganib kung siya ay liliban na mag-isa at itinuro din sa amin na palaging gumawa ng kabutihan sa kapwa."
    show lilys one
    show vicentes tri
    vicente "Ah ganun ba ang babait naman ng inyong buong pamilya."

    scene bg church with fade
    play sound [ "<silence 0.5>", "audio/bell.mp3" ]
    "NANG MAKARATING NA SILA SA SIMBAHAN AY PINAKILALA NG MAGKAPATID SI VICENTE SA LAHAT NG MIYEMBRO NG SIMBAHAN."
    "NATUWA SI VICENTE SA MGA BAGO NIYANG MGA NAKILALA AT TUNAY NGANG MABABAIT ANG MGA TAO DOON."

    "HABANG NAGMEMENSAHE ANG PARI AY NASAKTUHAN NA KATUGMA NG MENSAHE ANG LAHAT NG KANIYANG PINAGDARAANAN SA BUHAY."
    
    show pari tri at center with dissolve
    pari "Palagi kayong gumawa ng mabuti sa inyong kapwa dahil ito ay nakakalugod sa ating panginoon."
    hide pari
    show vicentes two at center with dissolve
    "NAALALA NI VICENTE ANG MGA NAGAWA NIYANG KASALANAN SA KANIYANG SARILI AT SA KANIYANG KAPWA."
    "NAPAGTANTO NIYA NA ITO AY MASAMA KAYA NAMAN MAAGA PA AY MAITUTUWID NIYA ANG LAHAT NG KANIYANG NAGAWANG KASALANAN."
    hide vicentes with dissolve
    "AT NATAPOS NA ANG KANILANG GAWAIN SA SIMBAHAN."
    show lilys one at left
    show blessys tri at slightleft
    show vicentes one at right
    with dissolve
    blessy "Kamusta naman ang iyong karanasan sa iyong pagdalo?"
    show blessys one
    show vicentes tri
    vicente "Tunay ngang nakakagalak at magaan sa kalooban ang pagdalo sa ganitong gawain patungkol sa diyos."
    show vicentes one
    show blessys tri
    blessy "Mabuti naman at nasiyahan ka sa aming paanyaya sayo."
    show blessys one
    show lilys tri
    lily "Nawa ay makasama kapa ulit namin kapag may ganitong pagsimba."

    scene black with dissolve
    "MULA NOON PALAGI NANG SUMASAMA SI VICENTE SA SIMBAHAN. MAS NAGKAROON SIYA NG KAPAYAPAAN SA KANIYANG BUHAY."
    "MAS LUMALIM PA ANG KANIYANG PANANAMPALATAYA SA DIYOS AT NAGAMIT DIN SIYA UPANG MAGING DAAN PARA MAKATULONG DIN SA IBA."
    centered "MORAL: PAGMAMAHAL SA SARILI, KAPWA AT PANANAMPALATAYA SA DIYOS."
    jump quiz_9


label hindi_9:
    scene bg classroom with dissolve
    "KINABUKASAN SA PAARALAN AY NAGKAUSAP MULI ANG MAGKAKAIBIGAN."
    show lily tri at left
    show blessy one at slightleft
    show vicente one at right
    with dissolve
    lily "Vicente, sayang hindi ka nakadalo kahapon ang saya pa naman."
    show lily one
    show vicente tri
    vicente "Oo nga dapat pala dumalo ako ang lungkot ko pa naman kahapon."
    show vicente one
    show blessy tri
    blessy "Okay lang yun sa susunod sumama ka na sa amin."
    show blessy one
    show vicente tri
    vicente "Babawi ako sa susunod."
    show vicente one
    show lily tri
    lily "Sige aasahan namin yan."
    scene black with dissolve
    "MAKALIPAS ANG ILANG ARAW INANYAYAHAN MULI NG MAGKAPATID SI VICENTE PARA SA ISANG PROGRAMA NG KANILANG SIMBAHAN."
    "PATUNGKOL SA PAGBABAWAL NG PANINIGARILYO AT MAY KASAMANG MENSAHE PATUNGKOL SA DIYOS."
    "SUMAMA SI VICENTE SA MAGKAPATID."

    scene bg auditorium with fade
    "DITO NALAMAN NI VICENTE NA MASAMA PALA ANG KANIYANG GINAGAWANG KASALANAN NA PANINIGARILYO."
    "AT MASAMA ANG EPEKTO NITO SA KALUSUGAN."
    "DITO UNTI-UNTI NIYANG NAKILALA ANG DIYOS SA KANIYANG BUHAY."
    show lily one at left
    show blessy one at slightleft
    show vicente tri at right
    with dissolve
    vicente "Maraming salamat sa inyong magkapatid dahil sainyo mas napalapit ako sa diyos at nalinawan ako sa mga kasalanan na aking nagawa."
    show vicente one
    show blessy tri
    blessy "Walang anuman iyon ang mahalaga ay nakatulong kami sayo."
    show blessy one
    show lily tri
    lily "Mas nagagalak ang diyos dahil nakilala mo siya."

    scene black with dissolve
    "AT MAS TUMIBAY PA ANG PAGKAKAIBIGAN NILA DAHIL SA NANGYARI AT KAHIT ANONG PAGSUBOK NA DUMATING SA KANILANG BUHAY AY PATULOY SILANG MANANALIG SA DIYOS."
    centered "MORAL: PAGMAMAHAL SA SARILI, KAPWA AT PANANAMPALATAYA SA DIYOS."
    jump quiz_9
    

label quiz_9: 
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_9 = 0 
    default percent_9 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_9 = 0 
    call screen question1_9 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_9: 
    $ points_9 += 1
    call screen question2_9 with circlewipe
label wronganswer1one_9:
    call screen question2_9 with circlewipe
label wronganswer1two_9:
    call screen question2_9 with circlewipe

label correctanswer2_9: 
    $ points_9 += 1
    call screen question3_9 with circlewipe
label wronganswer2two_9:
    call screen question3_9 with circlewipe
label wronganswer2one_9:
    call screen question3_9 with circlewipe

label correctanswer3_9: 
    $ points_9 += 1
    call screen question4_9 with circlewipe
label wronganswer3two_9:
    call screen question4_9 with circlewipe
label wronganswer3one_9:
    call screen question4_9 with circlewipe

label correctanswer4_9: 
    $ points_9 += 1
    call screen question5_9 with circlewipe
label wronganswer4_9:
    call screen question5_9 with circlewipe

label correctanswer5_9: 
    $ renpy.block_rollback()
    $ points_9 += 1
    $ persistent.current_9 = points_9
    $ renpy.choice_for_skipping()
    if points_9 == 4:
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        
        return
    elif points_9 == 5:
        play sound "audio/win.wav"
        scene bg five with dissolve
        centered ""
        
        return
    else:
        play sound "audio/lose.mp3"
        scene bg bagsak with dissolve
        centered ""
        scene bg ulit
        centered ""
        return
    
label wronganswer5_9:
    $ renpy.block_rollback()
    $ persistent.current_9 = points_9
    $ renpy.choice_for_skipping()
    if points_9 == 4:
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        
        return
    elif points_9 == 5:
        play sound "audio/win.wav"
        scene bg five with dissolve
        centered ""
        
        return
    else:
        play sound "audio/lose.mp3"
        scene bg bagsak with dissolve
        centered ""
        scene bg ulit
        centered ""
        return


screen question1_9:
    add "images/story9/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story9/qc/a1_idle.png"
        hover "images/story9/qc/a1_hover.png"
        action Jump("wronganswer1two_9")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story9/qc/b1_idle.png"
        hover "images/story9/qc/b1_hover.png"
        action Jump("correctanswer1_9")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story9/qc/c1_idle.png"
        hover "images/story9/qc/c1_hover.png"
        action Jump("wronganswer1one_9")

screen question2_9:
    add "images/story9/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story9/qc/a2_idle.png"
        hover "images/story9/qc/a2_hover.png"
        action Jump("wronganswer2one_9")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story9/qc/b2_idle.png"
        hover "images/story9/qc/b2_hover.png"
        action Jump("wronganswer2two_9")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story9/qc/c2_idle.png"
        hover "images/story9/qc/c2_hover.png"
        action Jump("correctanswer2_9")

screen question3_9:
    add "images/story9/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story9/qc/a3_idle.png"
        hover "images/story9/qc/a3_hover.png"
        action Jump("wronganswer3one_9")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story9/qc/b3_idle.png"
        hover "images/story9/qc/b3_hover.png"
        action Jump("wronganswer3two_9")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story9/qc/c3_idle.png"
        hover "images/story9/qc/c3_hover.png"
        action Jump("correctanswer3_9")

screen question4_9:
    add "images/story9/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer4_9")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer4_9")

screen question5_9:
    add "images/story9/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer5_9")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer5_9")
