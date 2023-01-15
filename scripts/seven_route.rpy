#CHARACTER NAMES AND NAME COLOR
define ginanglazatin = Character("Ginang Lazatin", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")
define kuyamarvin = Character("Kuya Marvin", color = "#ff0000", ctc="ctc_blink", ctc_position="nestled")

define isko = Character("Isko", color = "#0000ff", ctc="ctc_blink", ctc_position="nestled")

define dexter = Character("Dexter", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")
define paul = Character("Paul", color = "#00ff00", ctc="ctc_blink", ctc_position="nestled")

#CHARACTER IMAGES AND EXPRESSION
image ginanglazatin one = "images/story7/char/ginanglazatin one.png"
image ginanglazatin two = "images/story7/char/ginanglazatin two.png"
image ginanglazatin tri = "images/story7/char/ginanglazatin tri.png"
image ginanglazatin close = "images/story7/char/ginanglazatin close.png"

image ginanglazatindagat one = "images/story7/char/ginanglazatindagat one.png"
image ginanglazatindagat two = "images/story7/char/ginanglazatindagat two.png"
image ginanglazatindagat tri = "images/story7/char/ginanglazatindagat tri.png"
image ginanglazatindagat close = "images/story7/char/ginanglazatindagat close.png"

image kuyamarvin one = "images/story7/char/kuyamarvin one.png"
image kuyamarvin two = "images/story7/char/kuyamarvin two.png"
image kuyamarvin tri = "images/story7/char/kuyamarvin tri.png"

image isko one = "images/story7/char/isko one.png"
image isko decision = "images/story7/char/isko decision.png"
image iskodagat one = "images/story7/char/iskodagat one.png"
image iskodagat tri = "images/story7/char/iskodagat tri.png"

image dexter two = "images/story7/char/dexter two.png"
image dexter tulong = "images/story7/char/dexter tulong.png"
image dexterdagat tri = "images/story7/char/dexterdagat tri.png"
image dexterdagat two = "images/story7/char/dexterdagat two.png"
image dexter tri = "images/story7/char/dexter tri.png"

image paul abot = "images/story7/char/paul abot.png"
image paul one = "images/story7/char/paul one.png"
image paul tulong = "images/story7/char/paul tulong.png"
image paul two = "images/story7/char/paul two.png"
image pauldagat tri = "images/story7/char/pauldagat tri.png"
image pauldagat two = "images/story7/char/pauldagat two.png"

#BACKGROUNDS
image bg dyip = "images/story7/bg dyip.png"
image bg beach = "images/story7/bg beach.png"
image bg beachnight = "images/story7/bg beachnight.png"
image bg beachresort = "images/story7/bg beachresort.png"

label seven_start:
    $ renpy.block_rollback()
    stop music

    scene black with dissolve
    centered "{size=50}PAMAGAT: ANG PASIYA NI ISKO{/size}" 

    $ renpy.block_rollback()
    play music "audio/bgm_fun.mp3"

    scene bg classroomtwo with fade
    "MASAYA ANG MGA MAG-AARAL NI GNG. LAZATIN. LAHAT AY MASIGLANG NAGSASALITA TUNGKOL SA OUTING NG KLASE."
    "DAHIL HINDI PA SILA NAKAPAGPASIYA KUNG SAAN PUPUNTA, NAG-BIGAY SILA NG ILANG MUNGKAHI."
    "LIMANG PANGKAT ANG BUMUBUO SA KLASE."
    show ginanglazatin tri at right with moveinright
    ginanglazatin "Mga bata dahil magtatapos na ang taon, magkakaroon tayo ng pagdiriwang. Saan niyo gusto ipagdiwang ang ating Christmas Party?"
    show ginanglazatin one
    show isko one at left with moveinleft
    isko "Ma'am, maganda po sana mag-camping tayo sa tabing-dagat."
    show dexter tri at slightleft with dissolve    
    dexter "Oo nga maganda yang naisip mo Isko tiyak na mag-eenjoy tayo."
    show paul one at slightright with dissolve                   
    paul "Ma'am, parang mas maganda po pumunta sa museo."
    show ginanglazatin close
    ginanglazatin "Dahil dalawa ang naisip ninyong puntahan magkakaroon tayo ng botohan."
    show ginanglazatin tri
    ginanglazatin "Kung alin ang may pinakamaraming boto doon tayo pupunta."

    scene black with dissolve
    "GAYUNPAMAN, BUMOTO AT SUMANG-AYON SILA NA SA TABING-DAGAT PUMUNTA."

    scene bg schoolgate with dissolve
    "NANG SUMUNOD NA ARAW, MAAGANG-MAAGA PA AY NASA PAARALAN NA ANG MGA MAG-AARAL. MAAGA RING DUMATING SI GNG. LAZATIN."
    "INIHANDA NILA ANG MGA BAGAY NA KAKAILANGANIN NILA. ISANG PANGKAT ANG NAATASANG MAGHANDA NG MGA PALARO PARA SA LAHAT."
    show ginanglazatin tri at right with moveinright
    ginanglazatin "Nakahanda na ba kayo mga bata. Dala niyo na ba ang mga kailangan dalhin."
    show ginanglazatin one
    show paul abot at left with moveinleft
    paul "Opo ma'am may dala po kaming mga bola, lubid, at sungka na gagamitin sa palaro."
    show ginanglazatin tri
    ginanglazatin "Sige umalis na tayo."

    scene bg dyip with dissolve
    "AT SUMAKAY NA NGA SILA SA JEEP PAPUNTA SA TABING-DAGAT."

    scene bg beachresort with dissolve
    "MAKALIPAS ANG ILANG ORAS AY DUMATING NA ANG MGA MAG-AARAL SA RESORT."
    show ginanglazatindagat tri with dissolve
    ginanglazatin "Mga bata, huwag kayo lumayo sa kubo at huwag kayong humiwalay sa inyong mga pangkat."

    scene bg beach with dissolve
    play sound "audio/beach.mp3" loop
    "NAGSIMULA NA ANG MASASAYANG GAWAIN. MAY NAGLALARO NG SUNGKA, VOLLEYBALL, AT HILAHAN (TUG-OF-WAR)."
    call screen interactive7 with dissolve

screen interactive7:
    add "images/story7/bg beachint.png"

    imagebutton:
        xpos 1030
        ypos 150
        idle "images/story7/arrowseven_idle.png"
        hover "images/story7/arrowseven_hover.png"
        action Jump("tuloy_7")

    imagebutton:
        xpos 100
        ypos 460
        idle "images/story7/tug_idle.png"
        hover "images/story7/tug_hover.png"
        action Jump("tug_7")

    imagebutton:
        xpos 570
        ypos 460
        idle "images/story7/volleyball_idle.png"
        hover "images/story7/volleyball_hover.png"
        action Jump("volley_7")
    
    imagebutton:
        xpos 800
        ypos 460
        idle "images/story7/sungka_idle.png"
        hover "images/story7/sungka_hover.png"
        action Jump("sungka_7")

label tug_7:
    show bg beach
    show tug_idle at truecenter
    with dissolve
    "Ang Hilahan o Tug of War ay isang isport na kinabibilangan ng dalawang kuponan na humihila sa magkabilang dulo ng isang lubid na may layuning hilahin ang kabilang koponan sa gitnang linya."
    "Maaaring laruin ang isport sa iba't ibang lugar, kabilang ang damo, dumi, o buhangin, at karaniwang nilalaro sa labas."
    "Ang bawat kuponan ay karaniwang binubuo ng anim hanggang walong manlalaro, bagama't ang mas malalaking kuponan ay hindi karaniwan."
    "Ang isport ay nangangailangan ng lakas, tibay, at diskarte, pati na rin ang kakayahang magtrabaho nang epektibo bilang isang grupo."
    "Ang Tug of war ay may mahabang kasaysayan at pinaniniwalaang nagmula sa mga sinaunang sibilisasyon, kung saan madalas itong ginagamit bilang pagsubok ng lakas at isang uri ng libangan."
    hide tug_idle
    call screen interactive7
label volley_7:
    show bg beach
    show volleyball_idle at truecenter
    with dissolve
    "Ang volleyball ay isang team isport na nilalaro ng dalawang kuponan ng anim na manlalaro sa isang court na hinahati ng net."
    "Ang layunin ng laro ay itama ang bola sa ibabaw ng net at papunta sa court ng kalabang kuponan, at upang pigilan ang ibang kuponan na ibalik ito."
    "Ang bawat kuponan ay pinapayagang tamaan ang bola ng maximum na tatlong beses bago ito dapat ibalik sa kabilang panig ng net."
    "Na-iiskor ang mga puntos kapag nabigo ang isang kuponan na ibalik ang bola sa kabilang panig ng net, o kapag tumama ang bola sa lupa sa gilid ng court ng kalaban."
    "Ang volleyball ay isang sikat na isport na nilalaro sa parehong baguhan at propesyonal na antas, at tinatangkilik ng mga tao sa lahat ng edad sa buong mundo."
    hide volleyball_idle
    call screen interactive7
label sungka_7:
    show bg beach
    show sungka_idle at truecenter
    with dissolve
    "Ang Sungka ay isang tradisyonal na larong tabla sa Pilipinas na nilalaro gamit ang mga shell o iba pang maliliit at bilog na bagay bilang mga piraso."
    "Ang laro ay nilalaro sa isang board na binubuo ng dalawang hanay ng pitong butas, o mga hukay, na nakaayos sa kalahating bilog."
    "Ang bawat manlalaro ay may isang hilera ng pitong hukay, at mayroong isang mas malaking hukay, na tinatawag na \"Kalaha\" sa bawat dulo ng board."
    "Ang layunin ng laro ay upang mangolekta ng maraming mga shell hangga't maaari sa pamamagitan ng pagkuha ng mga ito mula sa mga hukay ng kalaban."
    "Ang mga manlalaro ay humalili sa paghahasik ng mga shell mula sa isang hukay patungo sa isa pa, na may layuning makuha ang pinakamaraming shell ng kalaban hangga't maaari."
    hide sungka_idle
    call screen interactive7

label tuloy_7:
    scene bg beach with fade
    stop sound fadeout 1.0
    "MASAYANG-MASAYA ANG LAHAT NANG BIGLANG SUMIGAW ANG ILANG MAG-AARAL. NAPATINGIN SI ISKO SA GAWI NG DAGAT KUNG SAAN NAGMULA ANG SIGAW."
    "NAKITA NIYA ANG ILAN SA KANILANG MGA KAMAG-ARAL NA NAKASAKAY SA ISANG BANGKA NA DAHAN-DAHANG TINATANGAY NG ALON PALAYO SA PAMPANG."
    "ITO ANG MGA MAG-AARAL NA PALIHIM NA KINALAG SA PAGKAKATALI ANG BANGKA."

    show dexter tulong with dissolve
    dexter "Tulong! Tulong!"
    hide dexter
    show paul tulong with dissolve
    paul "Tulungan niyo kami!"
    hide paul
    show ginanglazatindagat tri at right with moveinright
    ginanglazatin "Mga bata humingi kayo ng tulong sa mga taong nakatira sa malapit."
    hide ginanglazatindagat with dissolve
    "SAMANTALA, NAISIP NI ISKO NA MAAARING BIGLANG ITABOY NG ALON ANG BANGKA PALAYO SA DALAMPASIGAN. MAAARI RING ITAOB IYON NG ALON."
    "NASA PANGANIB ANG BUHAY NG KANIYANG MGA KAMAG-ARAL."
    "NAALALA NIYA ANG NAPANSIN NIYANG KARATULA NA MAY NAKALAGAY NA KUNG KAILANGAN NG TULONG AY TAWAGAN LAMANG SI KUYA MARVIN."
    "NAPAISIP SI ISKO KUNG ANO ANG KANIYANG GAGAWIN."
    show isko decision with zoomin
    menu:
        
        isko "ANO ANG GAGAWIN KO?"
        "TULUNGAN ANG MGA KAKLASE":
            jump tumulong_7
        "HAYAAN NALANG NA IBA ANG TUMULONG":
            jump hayaan_7


label hayaan_7:
    scene black with dissolve
    "DAHIL HINDI AGAD NATULUNGAN NG MGA LIFEGUARD ANG MGA BATA AY TULUYAN NA SILANG NATANGAY NG ALON PAPALAYO SA PAMPANG."
    "NAPAHAMAK ANG MGA BATA AT NAUDLOT ANG KANILANG OUTING."

    "SA ORAS NG PANGANIB, KUNG MAYROON KANG KAKAYAHANG TUMULONG AY IYONG GAWIN UPANG MAIWASAN ANG MALALANG PANGYAYARI."
    
    centered "MORAL: PALAGING PILIIN ANG TUMULONG"
    jump quiz_7

label tumulong_7:
    hide isko
    "KAAGAD TINAWAG NI ISKO SI KUYA MARVIN, ANG LIFEGUARD SA NASABING RESORT."
    show iskodagat tri at left with moveinleft
    isko "Kuya Marvin, tulungan niyo po ang mga kaklase ko. Yung sinasakyan po kasi nilang bangka ay naaanod papalayo sa dalampasigan."
    show kuyamarvin tri at right with moveinright
    kuyamarvin "Sige. Tatawagin ko na rin ang iba pang lifeguard at dadalhin ko na rin ang mga life jacket."
    hide kuyamarvin
    hide iskodagat
    with dissolve
    "TINULUNGAN NIYANG ITALI ANG MGA LUBID NA GINAMIT NILA SA LARONG HILAHAN, TUMULONG DIN ANG IBA PA NIYANG KAMAG-ARAL."
    "ITINALI NILA ANG KABILANG DULO NG LUBID SA PUNO NG NIYOG. IYON ANG GINAMIT NI KUYA MARVIN SA PAGSAGIP SA MGA BATA."
    show kuyamarvin tri at center with dissolve
    kuyamarvin "Nasaan ang dulo ng tali na natanggal sa bangka?"
    hide kuyamarvin with dissolve
    "PINAGDUGTONG ANG ITINALI NILANG LUBID AT LUMANGOY PABALIK SA PAMPANG."
    show kuyamarvin tri at right with moveinright
    kuyamarvin "Mabuti na lang at naipagbigay-alam mo agad sa amin ang nangyari, baka naitaboy nang palayo ng alon sa gitna ng dagat ang iyong mga kaklase."
    show iskodagat tri at left with moveinleft
    isko "Salamat po kuya marvin sa mabilisang responde at naligtas ang aking mga kaklase."

    scene bg beach with dissolve
    pause 0.1
    show bg beachnight with dissolve
    "NANG MALIGTAS ANG MGA BATA AY KINAUSAP MUNA NI GNG. LAZATIN ANG KANIYANG MGA MAG-AARAL BAGO UMALIS."
    show ginanglazatindagat close at right with dissolve
    ginanglazatin "Mga bata hindi magandang pasiya ang sumakay sa bangka ng walang kasamang matanda."
    show ginanglazatindagat two
    show dexterdagat two at left with dissolve
    dexter "Pasensya na po ma'am sa aming nagawa."
    show pauldagat two at slightleft with dissolve
    paul "Hindi na po mauulit."
    show ginanglazatindagat one
    ginanglazatin "Sa katunayan, si Isko lamang ang nakagawa ng tamang pasiya ngayong araw."

    scene black with dissolve
    play sound "audio/clap.wav"
    "SUMANG-AYON ANG LAHAT NG MAG-AARAL AT NAGPALAKPAKAN. PINAGSABIHAN ANG LAHAT NA AYUSIN NA ANG KANILANG MGA GAMIT AT HUMANDA NA SA PAG-UWI."

    centered "MORAL: PALAGING PILIIN ANG TUMULONG"
    jump quiz_7

label quiz_7: 
    stop music
    play music [ "<silence 0.5>", "audio/quiz.mp3" ]
    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()
    default points_7 = 0 
    default percent_7 = "▒▒▒▒▒▒▒▒▒▒ 0%"
    default persistent.current_7 = 0 
    call screen question1_7 with pixellate #PIXELLATE PAGPASOK NG QUIZ

label correctanswer1_7: 
    $ points_7 += 1
    call screen question2_7 with circlewipe
label wronganswer1one_7:
    call screen question2_7 with circlewipe
label wronganswer1two_7:
    call screen question2_7 with circlewipe

label correctanswer2_7: 
    $ points_7 += 1
    call screen question3_7 with circlewipe
label wronganswer2two_7:
    call screen question3_7 with circlewipe
label wronganswer2one_7:
    call screen question3_7 with circlewipe

label correctanswer3_7: 
    $ points_7 += 1
    call screen question4_7 with circlewipe
label wronganswer3two_7:
    call screen question4_7 with circlewipe
label wronganswer3one_7:
    call screen question4_7 with circlewipe

label correctanswer4_7: 
    $ points_7 += 1
    call screen question5_7 with circlewipe
label wronganswer4_7:
    call screen question5_7 with circlewipe

label correctanswer5_7: 
    $ renpy.block_rollback()
    $ points_7 += 1
    $ persistent.current_7 = points_7
    $ renpy.choice_for_skipping()
    if points_7 == 4:
        $ persistent.seven = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_7 == 5:
        $ persistent.seven = True
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
    
label wronganswer5_7:
    $ renpy.block_rollback()
    $ persistent.current_7 = points_7
    $ renpy.choice_for_skipping()
    if points_7 == 4:
        $ persistent.seven = True
        play sound "audio/win.wav"
        scene bg four with dissolve
        centered ""
        scene bg bukas
        centered ""
        return
    elif points_7 == 5:
        $ persistent.seven = True
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


screen question1_7:
    add "images/story7/questions/bg question1.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story7/qc/a1_idle.png"
        hover "images/story7/qc/a1_hover.png"
        action Jump("correctanswer1_7")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story7/qc/b1_idle.png"
        hover "images/story7/qc/b1_hover.png"
        action Jump("wronganswer1one_7")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story7/qc/c1_idle.png"
        hover "images/story7/qc/c1_hover.png"
        action Jump("wronganswer1two_7")

screen question2_7:
    add "images/story7/questions/bg question2.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story7/qc/a2_idle.png"
        hover "images/story7/qc/a2_hover.png"
        action Jump("wronganswer2two_7")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story7/qc/b2_idle.png"
        hover "images/story7/qc/b2_hover.png"
        action Jump("correctanswer2_7")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story7/qc/c2_idle.png"
        hover "images/story7/qc/c2_hover.png"
        action Jump("wronganswer2one_7")

screen question3_7:
    add "images/story7/questions/bg question3.png"
    
    imagebutton:
        xpos 137
        ypos 234
        idle "images/story7/qc/a3_idle.png"
        hover "images/story7/qc/a3_hover.png"
        action Jump("wronganswer3one_7")

    imagebutton:
        xpos 485
        ypos 234
        idle "images/story7/qc/b3_idle.png"
        hover "images/story7/qc/b3_hover.png"
        action Jump("wronganswer3two_7")

    imagebutton:
        xpos 834
        ypos 234
        idle "images/story7/qc/c3_idle.png"
        hover "images/story7/qc/c3_hover.png"
        action Jump("correctanswer3_7")

screen question4_7:
    add "images/story7/questions/bg question4.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("correctanswer4_7")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("wronganswer4_7")

screen question5_7:
    add "images/story7/questions/bg question5.png"
    
    imagebutton:
        xpos 165
        ypos 208
        idle "truefalse_idle.png"
        hover "tama_hover.png"
        action Jump("wronganswer5_7")
        
    imagebutton:
        xpos 640
        ypos 208
        idle "truefalse_idle.png"
        hover "mali_hover.png"
        action Jump("correctanswer5_7")