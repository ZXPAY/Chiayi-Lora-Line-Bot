### Line-Bot 介紹
word_line_bot = '''\
    此line-bot為一互動式聊天機器人,將嘉義大學室內和室外的資料呈現給使用者,讓使用者能用習慣的手機app-line,\
去得知目前的溫度、濕度、二氧化碳、空氣微粒等等資料.\n\
Github：https://github.com/ZXPAY/Chiayi-Lora-Line-Bot\
'''
### 團隊簡介說明
word_team_instructions = '''\
    本團隊來自於嘉義大學的學生,目前研究物聯網的技術,期望以所學改變社會與生活。\n\
團隊成員:\n\
👉🏿鄧翔冠(Line-bot作者) zxpay73945788@gmail.com\n\
👉🏿林銘彥(指導學長) \n\
👉🏿湯昀翔(資料呈現)     auroral.13king518@gmail.com\n\
👉🏿黃富源(底層設計)\
'''
### Command Example:
word_command_example = '''\
室內擷取溫度資料範例如下:\n\
i1溫度\n溫度,>=,25\n溫度,<=,27\ntime,>=,2018-04-27 20:24:00\n\n\
室外擷取溫度資料範例如下:\n\
o1溫度\n溫度,>=,25\n溫度,<=,27\ntime,>=,2018-04-27 20:24:00\n\n\
i1 => indoor 12000008\n\
o1 => outdoor 12000006\
'''

### Bad response
word_into_bad = ['幹', '三小', '打架阿', '廢物', '垃圾', '操', '乾', '拉機', '拉基']
word_bad = ['乾你娘！你以為我很閒喔？！🖕🖕🖕']

### Good response
word_into_good = ['棒', 'great', 'awesome', '強', '猛']
word_good = ['哈哈 謝謝您的稱讚\n是您不嫌棄❤️❤️❤️', '哈哈 強吧？！\n要約嗎？ 嘿嘿 🙈💞']

### Hello response
word_into_hello = ['你好', '妳好','您好', 'hello', 'hi']
word_hello = ['您好 ! You are my dear！', '您好！\n我很好喔~~~❤️❤️❤️',
              'Hi ~~~~', 'Hello ~~~~~']

### Good morning response
word_into_morning = ['早安', '早', 'morning']
word_morning = ['早安~💋💋💋', '早安~寶貝💑', '早安~寶貝~祝您今日都順利👫', '早安💘💘💘',
                'Good morning, my dear！']

### Good afternoon response
word_into_afternoon = ['午安', 'good afternoon']
word_afternoon = ['午安~💋💋💋', '午安~寶貝💑', '寶貝~我要去午覺了喔👫', '午安💘💘💘',
                'Good afternoon, my dear！']

### Good night response
word_into_night = ['晚安', 'good evening', 'good night']
word_night = ['晚安~💋💋💋', '晚安~寶貝💑', '寶貝~祝您有個好夢👫', '晚安💘💘💘\nHave a nice dream ~❤️❤️❤️',
              'Good night, my dear！']

### 安安 response
word_into_ok = ['安', '安安', 'how are you']
word_ok = ['安安', "I'm fine,thank you！👍🏾 "]



def Word_in_or_not(word_list, Text_user_say):
    flag = False
    for word in word_list:
        flag = flag or (word in Text_user_say)
    return flag






