from flask import Flask, request, abort
from Firebase import *
import json
import random
import datetime

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from Button_Template import *
from words import *

CHANNEL_TOKEN_KEY = '{Your line-bot token key}'
CHANNEL_SECRET = '{Your line-bot chennel secret key}'


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_TOKEN_KEY)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)

### Create firebase object
json_dir = 'aquarium-iot.json'
myfirebase = myFirebase(json_dir)
myfirebase.Create_Ref(collection='InDoor', document='0000000012000003', tag='indoor1')
myfirebase.Create_Ref(collection='InDoor', document='0000000012000008', tag='indoor2')
myfirebase.Create_Ref(collection='InDoor', document='0000000012000009', tag='indoor3')
myfirebase.Create_Ref(collection='OutDoor', document='0000000012000006', tag='outdoor1')
myfirebase.Create_Ref(collection='OutDoor', document='0000000012000007', tag='outdoor2')

def Check_date_format(num):
    if len(str(num)) < 2:
        return '0'+str(num)
    else:
        return str(num)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_data = 'Nothing to share ...'
    if event.message.text == 'recent indoor data1':
        msg = 'Indoor 12000003 Below :\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)
        cmd_tail = '\n' + 'time,<=,' + day

        msg += myfirebase.Query('i1'+'ts'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i1'+'hs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i1'+'cs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i1'+'is'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i1'+'ls'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i1'+'ms'+cmd_tail, sort='DESCENDING', limit_number=1)

        message = TextSendMessage(text=msg)
        #message = TextSendMessage(text=event.message.text)
        #message = TextSendMessage(text='Hello world !!!')
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == 'recent indoor data2':
        msg = 'Indoor 12000008 Below :\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)
        cmd_tail = '\n' + 'time,<=,' + day
        msg += myfirebase.Query('i2'+'ts'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i2'+'hs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i2'+'cs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i2'+'is'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i2'+'ls'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i2'+'ms'+cmd_tail, sort='DESCENDING', limit_number=1)

        message = TextSendMessage(text=msg)
        #message = TextSendMessage(text=event.message.text)
        #message = TextSendMessage(text='Hello world !!!')
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == 'recent indoor data3':
        msg = 'Indoor 12000009 Below :\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)
        cmd_tail = '\n' + 'time,<=,' + day
        msg += myfirebase.Query('i3'+'ts'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i3'+'hs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i3'+'cs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i3'+'is'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i3'+'ls'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('i3'+'ms'+cmd_tail, sort='DESCENDING', limit_number=1)

        message = TextSendMessage(text=msg)
        #message = TextSendMessage(text=event.message.text)
        #message = TextSendMessage(text='Hello world !!!')
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == 'recent outdoor data1':
        msg = 'Outdoor 12000006 Below :\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)
        cmd_tail = '\n' + 'time,<=,' + day

        msg += myfirebase.Query('o1'+'ts'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o1'+'hs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o1'+'is'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o1'+'ms'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o1'+'as'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o1'+'dns'+cmd_tail, sort='DESCENDING', limit_number=1)
        #msg += myfirebase.Query('o1'+'ns'+cmd_tail, sort='DESCENDING', limit_number=1)

        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == 'recent outdoor data2':
        msg = 'Outdoor 12000007 Below :\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)
        cmd_tail = '\n' + 'time,<=,' + day

        #cmd_tail = '\ntime,<,2018-06-11 22:10:00'
        msg += myfirebase.Query('o2'+'ts'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o2'+'hs'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o2'+'is'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o2'+'ms'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o2'+'as'+cmd_tail, sort='DESCENDING', limit_number=1)
        msg += myfirebase.Query('o2'+'dns'+cmd_tail, sort='DESCENDING', limit_number=1)
#        msg += myfirebase.Query('o2'+'ds'+cmd_tail, sort='DESCENDING', limit_number=1)
#        msg += myfirebase.Query('o2'+'ns'+cmd_tail, sort='DESCENDING', limit_number=1)

        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == '索引資料功能':
        line_bot_api.reply_message(event.reply_token, index_template)
        return 0
    elif event.message.text == 'IndoorDatabase':
        line_bot_api.reply_message(event.reply_token, indexIndoor_template)
    elif event.message.text == 'OutdoorDatabase':
        line_bot_api.reply_message(event.reply_token, indexOutdoor_template)

    ### Indoor database index ###
    elif event.message.text == 'indoor database1':
        line_bot_api.reply_message(event.reply_token, index_indoor_template1)
        return 0
    elif event.message.text == 'indoor1$_First':
        line_bot_api.reply_message(event.reply_token, index_indoor_template1_1)
        return 0
    elif event.message.text == 'indoor1$_Second':
        line_bot_api.reply_message(event.reply_token, index_indoor_template1_2)
        return 0
    elif event.message.text == 'indoor database2':
        line_bot_api.reply_message(event.reply_token, index_indoor_template2)
        return 0
    elif event.message.text == 'indoor2$_First':
        line_bot_api.reply_message(event.reply_token, index_indoor_template2_1)
        return 0
    elif event.message.text == 'indoor2$_Second':
        line_bot_api.reply_message(event.reply_token, index_indoor_template2_2)
        return 0
    elif event.message.text == 'indoor database3':
        line_bot_api.reply_message(event.reply_token, index_indoor_template3)
        return 0
    elif event.message.text == 'indoor3$_First':
        line_bot_api.reply_message(event.reply_token, index_indoor_template3_1)
        return 0
    elif event.message.text == 'indoor3$_Second':
        line_bot_api.reply_message(event.reply_token, index_indoor_template3_2)
        return 0
    ### Deal with the indoor data
    elif 'indoor1$_' in event.message.text:
        sensor_key = event.message.text[9:11]
        msg = 'Newest Indoor 12000003\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)
        cmd = 'i1' + sensor_key.lower() + '\n' + 'time,<=,' + day
        msg += myfirebase.Query(cmd, sort='DESCENDING')
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'indoor2$_' in event.message.text:
        sensor_key = event.message.text[9:]
        msg = 'Newest Indoor 12000008\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)

        cmd = 'i2' + sensor_key.lower() + '\n' + 'time,<=,' + day
        msg += myfirebase.Query(cmd, sort='DESCENDING')
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'indoor3$_' in event.message.text:
        sensor_key = event.message.text[9:]
        msg = 'Newest Indoor 12000009\n'

        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)

        cmd = 'i3' + sensor_key.lower() + '\n' + 'time,<=,' + day
        msg += myfirebase.Query(cmd, sort='DESCENDING')
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

    ### Outdoor database index ###
    elif event.message.text == 'outdoor database1':
        line_bot_api.reply_message(event.reply_token, index_outdoor_template1)
        return 0
    elif event.message.text == 'outdoor1$_First':
        line_bot_api.reply_message(event.reply_token, index_outdoor_template1_1)
        return 0
    elif event.message.text == 'outdoor1$_Second':
        line_bot_api.reply_message(event.reply_token, index_outdoor_template1_2)
        return 0
    elif event.message.text == 'outdoor database2':
        line_bot_api.reply_message(event.reply_token, index_outdoor_template2)
        return 0
    elif event.message.text == 'outdoor2$_First':
        line_bot_api.reply_message(event.reply_token, index_outdoor_template2_1)
        return 0
    elif event.message.text == 'outdoor2$_Second':
        line_bot_api.reply_message(event.reply_token, index_outdoor_template2_2)
        return 0
    ### Deal with the outdoor data
    elif 'outdoor1$_' in event.message.text:
        sensor_key = event.message.text[10:]
        msg = 'Newest Outdoor 12000006\n'
        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)

        cmd = 'o1' + sensor_key.lower() + '\n' + 'time,<=,' + day
        msg += myfirebase.Query(cmd, sort='DESCENDING')

        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

    elif 'outdoor2$_' in event.message.text:
        sensor_key = event.message.text[10:]
        msg = 'Newest Outdoor 12000007\n'
        today_datetime = datetime.datetime.today()
        day = str(today_datetime.year) + '-' + Check_date_format(today_datetime.month) + '-' + Check_date_format(today_datetime.day) + ' ' +\
                Check_date_format(today_datetime.hour) + ':' + Check_date_format(today_datetime.minute) + ':' + Check_date_format(today_datetime.second)

        cmd = 'o2' + sensor_key.lower() + '\n' + 'time,<=,' + day
        msg += myfirebase.Query(cmd, sort='DESCENDING')

        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == 'Line-Bot介紹':
        message = TextSendMessage(text=word_line_bot)
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif event.message.text == '團隊簡介與聯絡':
        message = TextSendMessage(text=word_team_instructions)
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif event.message.text == '指令範例':
        image_image = ImageSendMessage(
                    original_content_url='https://i.imgur.com/VWkCx1L.png',
                    preview_image_url='https://i.imgur.com/VWkCx1L.png'
                )
        line_bot_api.reply_message(event.reply_token, image_image)
        return 0

    ### 稱讚的回覆
    elif Word_in_or_not(word_into_good, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_good))
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif event.message.text.lower() == 'good':
        message = TextSendMessage(text=random.choice(word_good))
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    ### 問好的回覆
    elif Word_in_or_not(word_into_hello, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_hello))
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    ### 說早安的回覆
    elif Word_in_or_not(word_into_morning, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_morning))
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    ### 說午安的回覆
    elif Word_in_or_not(word_into_afternoon, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_afternoon))
        line_bot_api.reply_message(event.reply_token, message)

    ### 說晚安的回覆
    elif Word_in_or_not(word_into_night, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_night))
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    ### 說安安的回覆
    elif Word_in_or_not(word_into_ok, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_ok))
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    ### 說安安的回覆
    elif Word_in_or_not(word_into_bad, event.message.text.lower()):
        message = TextSendMessage(text=random.choice(word_bad))
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    try:
        msg = myfirebase.Query(event.message.text)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    except:
        line_bot_api.reply_message(event.reply_token, function_template)

    line_bot_api.reply_message(event.reply_token, function_template)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
