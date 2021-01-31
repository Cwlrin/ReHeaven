define lxl = Character(' 林小鲤 ',image="xiaoli")
define xj = Character(' 筱久 ',image="xiaojiu",who_color="#2894FF")
define sc = Character(' 苏纯 ',image="sucun")
define manA = Character(' 男研究员A ')
define womanA = Character(' 女研究员A ')
define manB = Character(' 男研究员B ')

define narrator_adv = Character(None,kind=adv,ctc_position="nestled")
define config.voice_filename_format = "{filename}"

image black = "#000"
image white = "#ffffff"

transform why_alt_xiaojiu(x=640,y=0):
    xcenter x - 95 ycenter y + 150 zoom 0.70 alpha 0.00 subpixel True
    easein 0.3 xcenter x - 115 ycenter y + 110 alpha 1.00
    easein 0.4 xcenter x - 95 ycenter y + 150
    easein 0.5
    easein 1.0 xcenter x - 75 ycenter y + 190 alpha 0.00
transform sub_xiaoli(x = 640,y= 0):
    xcenter x ycenter y + 75 zoom 0.8 alpha 0.00 subpixel True
    parallel:
        linear 0.5 ycenter y + 150
    parallel:
        linear 0.2 alpha 1.0
        linear 1.0
        linear 0.3 alpha 0.0

image why1:
    "liluo_common/common/facial/why.png"
    why_alt_xiaojiu(x = 740, y = 108)
image sub2:
    "liluo_common/common/facial/sub.png"
    sub_xiaoli(x = 950 , y=100)

image side xiaoli_banter="side/side_xiaoli_banter.png"
image side xiaoli_forcedsmile="side/side_xiaoli_forcedsmile.png"
image side xiaoli_happy="side/side_xiaoli_happy.png"
image side xiaoli_helpless="side/side_xiaoli_helpless.png"
image side xiaoli_left="side/side_xiaoli_left.png"
image side xiaoli_slack="side/side_xiaoli_slack.png"
image side xiaoli_slack_oneeye="side/side_xiaoli_slack_oneeye.png"
image side xiaoli_sleep_closeeye="side/side_xiaoli_sleep_closeeye.png"
image side xiaoli_smile="side/side_xiaoli_smile.png"
image side xiaoli_smile_oneeye="side/side_xiaoli_smile_oneeye.png"
image side xiaoli_stare="side/side_xiaoli_stare.png"
image side xiaoli_withsmile="side/side_xiaoli_withsmile.png"
image side xiaoli_worry="side/side_xiaoli_worry.png"
image side xiaoli_xd="side/side_xiaoli_xd.png"

image side xiaojiu_amaze="side/side_xiaojiu_amaze.png"
image side xiaojiu_amaze_oneeye="side/side_xiaojiu_amaze_oneeye.png"
image side xiaojiu_anxious="side/side_xiaojiu_anxious.png"
image side xiaojiu_dededo="side/side_xiaojiu_dededo.png"
image side xiaojiu_disappointment="side/side_xiaojiu_disappointment.png"
image side xiaojiu_forcedsmile="side/side_xiaojiu_forcedsmile.png"
image side xiaojiu_glance="side/side_xiaojiu_glance.png"
image side xiaojiu_hum="side/side_xiaojiu_hum.png"
image side xiaojiu_hum_closeeye="side/side_xiaojiu_hum_closeeye.png"
image side xiaojiu_pleased="side/side_xiaojiu_pleased.png"
image side xiaojiu_smile="side/side_xiaojiu_smile.png"
image side xiaojiu_worry="side/side_xiaojiu_worry.png"

transform re_left:
    xcenter 0.3
    ypos 0.1
transform re_right:
    xcenter 0.7
    ypos 0.1
transform re_center:
    xcenter 0.5
    ypos 0.1

label first:
    #play music "audio/colorful dream.mp3"
    scene black
    narrator_adv "又做了那个梦。"
    scene black with Fade(0.1, 0.0, 0.5, color="#fff")
    narrator_adv "意识陷于深沉的黑暗中，恍然如同白昼，密密麻麻的线条无序地交织在空中，越来越多。越来越多。"
    scene white with ImageDissolve("transition/television.jpg",0.2)
    scene black with ImageDissolve("transition/television.jpg",0.2)
    narrator_adv "坠落感向我袭来，世界颠倒过来，失去了时间、空间、概念以及概念本身。"
    scene black with vpunch
    scene black with hpunch
    narrator_adv "失落感在蔓延，血、黑暗、堕落、乱性和虫卵，那是一片荒漠。"
    narrator_adv "稍微……有了一点脚踏实地的感觉。"
    narrator_adv "今年是几几年？"
    voice da1
    lxl xiaoli_stare "「我是……谁」？"
    scene black_white_dream_light with ImageDissolve("transition/noise.png",0.2)
    narrator_adv "天空中紊乱的线条越来越多，越来越多。"
    scene white_biack_dream_light with ImageDissolve("transition/wrangle.jpg",0.2)
    scene black_white_dream_light with ImageDissolve("transition/noise.png",0.2)
    narrator_adv "一切本就无序，线条常常断开，重连，错位，没有一根线条准确地相交。"
    scene black_white_dream_highlights with vpunch
    scene black_white_dream_highlights with hpunch
    scene black_white_dream_highlights with ImageDissolve("transition/crazy.png",0.2)
    narrator_adv "渐渐地，天空被漆黑的巨幕所掩盖。"
    narrator_adv "但这真的称得上是“有序”吗？"
    scene black with Fade(0.1, 0.0, 0.5, color="#fff")
    scene black_white_dream_highlights with ImageDissolve("transition/top.png",0.2)
    narrator_adv "一片荒漠。一望无际，几千米前有一颗枯树，便没有了其他物体。"
    show xiao_li with ImageDissolve("transition/noise.png",0.2):
        xcenter 0.5
        ycenter 0.5
    narrator_adv "既熟悉，又陌生，那是一片荒漠。"
    voice da2
    lxl xiaoli_stare "「我忘记了……但是，很讨厌。有生命，却没有生气。」"
    scene black with Fade(0.1, 0.0, 0.5, color="#fff")
    narrator_adv "咔嚓！眼前一黑，放映的电影被人关掉了。整个世界都宁静了。远处慢慢拉开帷幕，是一条走廊，是一只张着嘴等着猎物送上门的巨兽。"
    scene black_white_dream_light with Dissolve(1)
    narrator_adv "“快进来！快进来！”"
    scene black_white_dream_highlights with Dissolve(1)
    show xiao_li with fade
    narrator_adv "我恍然而迷茫，我向前走去。"
    scene color_dream_light with Dissolve(1)
    narrator_adv "走廊被逐渐照亮，这里像是儿童的天堂。墙上挂着色彩各异的画，八音盒演奏着名叫林小鲤的人从未听过的音乐。"
    show xiao_li with fade
    voice da3
    lxl xiaoli_worry "「我……」"
    narrator_adv "“快来！快来！”"
    narrator_adv "我走到走廊深处，向上望去，上面挂着一只机器人玩具和养在笼子里的猫咪，猫咪眨巴着灵动的眼睛，喵喵地朝着我叫。"
    narrator_adv "我抬起头，笑了。"
    narrator_adv "猫咪也笑了。它舔了舔嘴唇，张开它的小嘴，露出了裂开的红色唇瓣、鲜血和滴落的脓液。"
    narrator_adv "音乐演奏越来越快，逐渐达到了高潮。{w}机器人的眼睛变成了红色，头部翻转掉落，燃起了火。窗帘燃烧起来了，走廊燃烧起来了，全世界燃烧起来了，到处都是浓烟。"
    narrator_adv "我望向身后，望向四周，所有的猫咪一瞬间衰老了，皮肤变得干枯，毛发一根根掉下，变成一具具毫无生机的尸体。"
    narrator_adv "快跑啊！快跑啊！"
    hide xiao_li
    show xiao_li :
        xcenter 0.5
        ycenter 0.5
        easein_bounce 0.1 xcenter 0.3 ypos 0.4
        easeout_bounce 0.1 xcenter 0.7 ypos 0.6
        easeout_bounce 0.1 xcenter 0.7 ypos 0.4
        easein_bounce 0.1 xcenter 0.3 ypos 0.6
        ease_quint 0.1 xcenter 0.5 ycenter 0.5
    narrator_adv "我飞快的向外跑去，但出口在哪？被火焰烧得残破的死机了的八音盒只剩下了一句歌词，在循环播放着。"
    narrator_adv "“罪恶本在，人性无奈……”"
    narrator_adv "“罪恶本在，人性无奈……”"
    scene black with Fade(0.1, 0.0, 0.5, color="#fff")
    narrator_adv "世界突然再次黑暗。"
    narrator_adv "我感觉脊椎中有一团火，无数根针正扎向我的背脊，就好像密集恐惧症患者猛然之间看到蜂巢，或是害怕黑暗的人被吞噬在无光的房间中。身体内好像有无数的虫子翻涌着，肌肉被搅动的生疼。"
    narrator_adv "好难受。好痛苦。"
    scene black_white_dream_light with ImageDissolve("transition/noise.png",0.2)
    narrator_adv "很快，世界再次变成了那个荒漠。"
    scene white_biack_dream_light with ImageDissolve("transition/wrangle.jpg",0.2)
    scene black_white_dream_light with ImageDissolve("transition/noise.png",0.2)
    narrator_adv "无数的线条交织在天空上，混乱无序。"
    narrator_adv "我讨厌这种感觉。"

label second:
    voice da4
    lxl xiaoli_xd "「……」"
    voice db1
    scene black with fade
    xj xiaojiu_amaze "「醒醒，醒醒……小鲤！」"
    scene xiao_li_home with ImageDissolve("transition/dizzy.jpg",0.2)
    show xiaojiu_amaze_onehand :
        xcenter 1.0
        ypos 0.1
        linear 0.2 xcenter 0.3
    voice db2
    xj xiaojiu_amaze "「你没事吧？吾辈看你脸色很差，做梦了吗。」"
    show xiaoli_forcedsmile_onehand :
        xcenter 1.0
        ypos 0.1
        linear 0.2 xcenter 0.9 ypos 0.2
        linear 0.2 xcenter 0.8 ypos 0.0
        linear 0.2 xcenter 0.7 ypos 0.1
    voice da5
    lxl xiaoli_forcedsmile "「我没事。又做了……那个梦。」"
    #play music "audio/A_Lazy_Day.mp3"
    hide xiaojiu_amaze_onehand
    show xiaojiu_worry at re_left
    show xiaoli_stare at re_right
    voice db3_1
    xj xiaojiu_worry "「梦是大脑皮层处理冗余信息和图像数据时发出的神经脉冲，其中包含了你意识和潜意识中所曾经感触到的事物。」"
    voice db3_2
    hide xiaojiu_worry
    show xiaojiu_worry_onehand at re_left
    xj xiaojiu_worry "「如果反复做同一个噩梦，吾辈建议咨询心理医生进行一定程度上的治疗哦。」"
    narrator_adv "林小鲤开始感到有些头疼了。"
    hide xiaoli_forcedsmile_onehand
    hide xiaoli_stare
    show xiaoli_stare:
        re_right
        linear 0.2 xcenter 0.65 ypos 0.1
        linear 0.2 xcenter 0.75 ypos 0.1
        linear 0.1 xcenter 0.7 ypos 0.1
    narrator_adv "晃了晃脑袋，眼前是熟悉的房间，她已经在这里居住了两年。"
    hide xiaojiu_worry_onehand
    show xiaojiu_hum_closeeye at re_left
    voice db4_1
    xj xiaojiu_hum_closeeye"「顺带一提，“没事”的用词只是中国人遇到问题却又不好表露出软弱心理时的习惯用词。」"
    hide xiaojiu_hum_closeeye
    show xiaojiu_hum at re_left
    voice db4_2
    xj xiaojiu_hum "「吾辈经过观察你的神态，觉得你有76.9\%的概率依然在对这个梦耿耿于怀。」"
    show xiaoli_smile at re_right
    voice da6_1
    lxl  xiaoli_smile "「哎呀……不要太在意这些啦。」"
    hide xiaoli_smile
    show xiaoli_slack_oneeye_onehand at re_right
    voice da6_2
    lxl xiaoli_slack_oneeye "「我只是稍微有那么一点点，就那么一点点哦。」"
    hide xiaoli_stare
    hide xiaoli_slack_oneeye_onehand
    show xiaoli_sleep_closeeye_onehand :
        re_right
        linear 0.2 xcenter 0.45 ypos 0.1
        linear 0.1 xcenter 0.5 ypos 0.1
    narrator_adv "林小鲤扑到筱久怀里，用力摸着筱久的小脑袋。"
    hide xiaojiu_hum
    hide xiaojiu_smile_onehead
    show xiaojiu_hum_closeeye_onehand :
        re_left
        linear 0.1 xcenter 0.4 ypos 0.1
    narrator_adv "筱久轻轻反抱住女孩柔软的身体，就这样待了一会。"
    hide xiaojiu_amaze
    hide xiaojiu_hum_closeeye_onehand
    hide xiaoli_xd_onehand
    show xiaojiu_smile :
        xcenter 0.4 
        ypos 0.1
        linear 0.1 re_left
    show why1
    voice db5
    xj xiaojiu_smile "「怎么样的一点点？」"
    hide xiaoli_xd_smile
    hide xiaoli_sleep_closeeye_onehand
    show xiaojiu_smile at re_left
    show xiaoli_sleep_closeeye_onehand at re_center
    voice da7
    lxl xiaoli_sleep_closeeye "「小学生回到家里，爸爸问他考得怎么样，他说：“就考差了一点点。”」"
    hide xiaojiu_smile
    show xiaojiu_amaze at re_left
    narrator_adv "筱久莫名其妙地看着林小鲤。"
    hide xiaoli_sleep_closeeye_onehand
    show xiaoli_banter at re_center
    voice da8_1
    lxl xiaoli_banter"「那我换一个。有个屌丝一直追不到女神，然后跑去问她：“我还差多远？」"
    hide xiaoli_banter
    show xiaoli_banter_onehand at re_center
    voice da8_2
    lxl xiaoli_banter"「女神拍着宝马告诉他：“还差一点点。”」"
    hide xiaojiu_amaze
    show xiaojiu_amaze_onehand at re_left
    xj xiaojiu_amaze_onehand "「……」"
    hide xiaojiu_amaze_onehand
    show xiaojiu_amaze at re_left
    hide xiaoli_banter_onehand
    show xiaoli_slack at re_center
    voice da9
    lxl xiaoli_slack"「哎，算了。你说啊……这些都是我曾经经历过的事吗？」"
    hide xiaojiu_amaze
    show xiaojiu_hum at re_left
    voice db6
    xj xiaojiu_hum "「不要想太多，没准这只是你看过的恐怖片而已。」"
    hide xiaoli_slack
    show xiaoli_think_onehand at re_center
    voice da10
    lxl xiaoli_think"「总觉得这个梦很熟悉，但又好像哪里不太一样。」"
    hide xiaojiu_hum
    show xiaojiu_hum_onehand at re_left
    voice db7
    xj xiaojiu_hum "「别多想，兴许是你记错了。」"
    hide xiaoli_think_onehand
    show xiaoli_sleep_closeeye :
        re_center
        linear 0.1 xcenter 0.45 ypos 0.1
        linear 0.1 xcenter 0.5 ypos 0.1
        linear 0.1 xcenter 0.45 ypos 0.1
        linear 0.1 xcenter 0.5 ypos 0.1
    narrator_adv "筱久的衣服沾满了阳光的味道，暖融融的，散发着一种让人安心的清香。林小鲤惬意的在筱久的臂弯内钻了几下。"
    narrator_adv "筱久用手指绕着林小鲤的发梢，让林小鲤把头依偎在她的肩上，就这样过去了好久好久……"
    narrator_adv "这时候，窗外响起救护车的声音，打破了这份美好的宁静。"
    narrator_adv "越来越近，随后又越来越远。"
    hide xiaoli_sleep_closeeye
    show xiaoli_left at re_center
    show sub2
    voice da11
    lxl xiaoli_left "「发生什么了吗？」"
    hide xiaojiu_hum_onehand
    show xiaojiu_pleased_onehand at re_left
    voice db8
    xj xiaojiu_pleased "「不知道。」"
    return

label start:

    jump first
