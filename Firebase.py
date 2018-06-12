# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

### Command format below
'''
temperature
time,<=,2018-04-24 07:12:00
time,>=,2018-04-24 07:00:00
'''
#    Indoor:
#    Temperature         (TS)
#    Humidity            (HS)
#    CO                  (CS)
#    CO2                 (IS)
#    LPG                 (LS)
#    PM                  (MS)
#    Fire                (FS)
#    Wind Velocity       (WS)
#    Rain                (RS)
#
#    Outdoor:
#    Temperature         (TS)
#    Humidity            (HS)
#    CO2                 (IS)
#    PM                  (MS)
#    Wind Velocity       (WS)
#    Rain                (RS)
#    Atmospheric Press   (AS)
#    Latitude            (DS)
#    Longitude           (NS)
#    DNList = [DS,NS]

Data_Name_English = {
        'TS':'Temperature', 'HS':'Humidity', 'CS':'CO',
        'IS':'CO2', 'LS':'C3H8', 'MS':'PM', 'FS':'Fire',
        'WS':'Wind Velocity', 'RS':'Rain', 'Atmosphere':'Pressure',
        'DS':'Latitude', 'NS':'Longitude', 'AS':'Atmosphere'
        }
Data_Unit_English = {
        'TS':'\u00b0'+'C', 'HS':'%', 'CS':'ppm',
        'IS':'ppm', 'LS':'ppm', 'MS':'\u00b5'+'g/m'+'\u00b3', 'FS':'',
        'WS':'m/s', 'RS':'cm', 'AS':'pa',
        'DS':'', 'NS':''
        }
Data_English_Name = {
        'Temperature':'TS', 'Humidity':'HS', 'CO':'CS', 'CO2':'IS',
        'LPG':'LS', 'PM':'MS', 'Fire':'FS', 'Wind':'WS', 'Rain':'RS', 'Atmosphere':'AS',
        'Latitude':'DS', 'longitude':'NS', 'time':'time', 'rssi':'rssi'
        }

class myFirebase:
    def __init__(self, json_file):
        self.cred = credentials.Certificate(json_file)
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.all_ref = {}

        ### define the name we usually call for the sensor detect data
        self.temperature_name = ['溫度', '攝氏', 'temperature', 'temp', 'ts']
        self.humidity_name = ['濕度', 'humidity', '相對溼度', 'hum', 'hs']
        self.CO_name = ['co', '一氧化碳', 'cs']
        self.CO2_name = ['co2', '二氧化碳', 'is']
        self.LPG_name = ['液化石油氣', '瓦斯', '丙烷', 'lpg', 'ls']
        self.PM_name = ['空氣微粒', 'pm2.5', 'pm', 'ms', '空氣品質']
        self.fire_name = ['火焰感測', '火焰', 'fire', 'fs']
        self.wind_name = ['風速感測', '風速', 'wind', 'wind velocity', 'ws']
        self.rain_name = ['雨滴感測', '下雨', 'rain', 'rs']
        self.pressure_name = ['氣壓', '海拔', 'as', '大氣壓力', '壓力', 'pressure', 'atmosphere']
        self.latitude = ['緯度', 'latitude', 'ds']
        self.longitude = ['經度', 'longitule', 'ns']
        self.time_name = ['time', '時間', 'date']
        self.rssi_name = ['rssi']


    def Create_Ref(self, collection, document, tag):
        new_ref = self.db.collection(collection).document(document)
        self.all_ref[tag] = new_ref

    def GrabData(self, tag, collection):
        data_collect = []
        ref = self.all_ref[tag].collection(collection)
        docs = ref.get()
        for data in docs:
            data_collect.append('{} => {}'.format(data.id, data.to_dict()))
        return data_collect

    def Which_Collection(self, str_name):
        if str_name in self.temperature_name:
            return 'Temperature'
        elif str_name in self.humidity_name:
            return 'Humidity'
        elif str_name in self.CO_name:
            return 'CO'
        elif str_name in self.CO2_name:
            return 'CO2'
        elif str_name in self.LPG_name:
            return 'LPG'
        elif str_name in self.PM_name:
            return 'PM'
        elif str_name in self.fire_name:
            return 'Fire'
        elif str_name in self.wind_name:
            return 'Wind'
        elif str_name in self.rain_name:
            return 'Rain'
        elif str_name in self.pressure_name:
            return 'Atmosphere'
        elif str_name in self.latitude:
            return 'Latitude'
        elif str_name in self.longitude:
            return 'longitude'
        elif str_name in self.time_name:
            return 'time'
        elif str_name in self.rssi_name:
            return 'rssi'
        else:
            return None

    def Remove_space(self, string_cmd):
        new_cmd_without_space = ''
        for data in string_cmd:
            if ' ' != data:
                new_cmd_without_space += data
        return new_cmd_without_space

    def Query(self, cmd, sort='ASCENDING', limit_number=20):
        query_data_dict = {}
        collection = None
        cmd_list = cmd.split('\n')
        if cmd_list[0].lower()[0:2] == 'i1':
            tag = 'indoor1'
        elif cmd_list[0].lower()[0:2] == 'i2':
            tag = 'indoor2'
        elif cmd_list[0].lower()[0:2] == 'o1':
            tag = 'outdoor1'
        elif cmd_list[0].lower()[0:2] == 'o2':
            tag = 'outdoor2'
        else:
            error

        collection = self.Which_Collection(cmd_list[0].lower()[2:])

        if collection is not None:
            if self.Which_Collection(collection.lower()) == 'time':
                return 'Sorry, we cannot query time.'
            query_name = Data_English_Name[self.Which_Collection(collection.lower())]
            ref = self.all_ref[tag].collection(collection)
            msg = ''
            name_remember = ''
            flag = False
            flag_correct_query = False
            cnt = 0  # 計數，compound query need it.
            for cmd in cmd_list:
                cnt += 1
                if flag:
                    name, operator, item = cmd.split(',')
                    name = self.Remove_space(name)
                    operator = self.Remove_space(operator)
                    if item[0:2] == '  ':
                        item = item[2:]
                    elif item[0] == ' ':
                        item = item[1:]
                    elif name.lower() in self.time_name:
                        pass
                    else:
                        item = self.Remove_space(item)
                    if flag_correct_query:
                        if name != name_remember:
                            return 'Sorry, can not query muti-parameters.'
                    name_remember = name
                    flag_correct_query = True
                    code_name = Data_English_Name[self.Which_Collection(name.lower())]
                    #print(query_name, name, operator, item)
                    if self.Which_Collection(name.lower()) is not None:
                        if sort == 'ASCENDING':
                            if cnt == len(cmd_list):  # Last Query
                                ref = ref.where(code_name, operator, item).order_by(code_name ,firestore.Query.ASCENDING).limit(limit_number)
                            else:
                                ref = ref.where(code_name, operator, item)
                        elif sort == 'DESCENDING':
                            if cnt == len(cmd_list):  # Last Query
                                ref = ref.where(code_name, operator, item).order_by(code_name ,firestore.Query.DESCENDING).limit(limit_number)
                            else:
                                ref = ref.where(code_name, operator, item)
                        print(query_name, collection, tag, code_name, operator, item)
                    else:
                        return 'Command Error.PLease Check the data.Below is the example.\n\
itemperature\n時間,>=,2018-04-27 12:00:00\n時間,<=,2018-04-27 20:15:00'
                flag = True
            results = ref.get()
            flag_empty_query_data = True
            for rs in results:
                if(len(msg)<1000):
                    query_data_dict = rs.to_dict()
                    #if ((float(query_data_dict[code_name]) != 0) and (code_name.lower() != 'time')):
                    msg += query_data_dict['time'] + '👉🏻\n' + Data_Name_English[query_name] \
                            + ':' + query_data_dict[query_name] + ' ' + Data_Unit_English[query_name]
                    msg += '\n'
                    print(query_data_dict)
                    flag_empty_query_data = False
            if flag_empty_query_data:
                return 'Sorry, data ' + Data_Name_English[query_name]  + ' you queried is empty or your query format is not coorect.\n'
            return msg
        else:
            return 'Command Error.PLease Check the data.Below is the example.\n\
itemperature\ntime,>= ,2018-04-27 12:00:00\ntime ,<= ,2018-04-27 20:15:00'
#            print('No collection found')


if __name__ == '__main__':
    json_dir = 'aquarium-iot.json'
    #Test_cmd = 'itemperature\ntime,>=,2018-04-27 12:00:00\ntime,<=,2018-04-27 20:15:00'
    #Test_cmd = 'itemperature\n時間,>=,2018-05-08 18:00:00\n時間,<=,2018-05-08 18:15:00'
    #Test_cmd = 'i溫度\n溫度,>,25\n溫度,<,30\ntime,>=,2018-05-08 8:00:00'
    #Test_cmd = 'itemp\n溫度,>,28.1\n溫度,<,28.5\ntime,>=,2018-05-10 8:00:00'
    #Test_cmd = 'i溫度\ntime,>=,2018-04-27 12:00:00\ntime,<=,2018-04-27 20:00:00'
    #Test_cmd = 'oas\ntime,>=,2018-04-00 00:00:00'
    #Test_cmd = 'its\ntime,>=, 2018-05-10 16:00:00'
    #Test_cmd = 'o2is\nis,<=,1000'
    Test_cmd = 'o2溫度\n時間,<,2018-06-11 22:42:30'

    myFirebase = myFirebase(json_dir)
    myFirebase.Create_Ref(collection='InDoor', document='0000000012000008', tag='indoor1')
    myFirebase.Create_Ref(collection='InDoor', document='0000000012000009', tag='indoor2')
    myFirebase.Create_Ref(collection='OutDoor', document='0000000012000006', tag='outdoor1')
    myFirebase.Create_Ref(collection='OutDoor', document='0000000012000007', tag='outdoor2')
    #print(myFirebase.GrabData('indoor', 'Temperature'))
    #myFirebase.Query(Test_cmd)
    print(myFirebase.Query(Test_cmd, sort='DESCENDING', limit_number=10))

##    a = doc.to_dict()
##    print(a)

##QUERY DATA
##query = collection_ref.where(u'Time', u'<=', u'2018-04-24T07:15:45')
##query = collection_ref.where(u'Time', u'>=', u'2018-04-24T07:15:45')
##
##results = query.get()
##
##for rs in results:
##    print(rs.to_dict())

#cred = credentials.Certificate("/home/pi/Desktop/FirebaseTest/smartcitytestproject-fb938-firebase-adminsdk-775p2-a9961fa11a.json")
#firebase_admin.initialize_app(cred)
#
#db = firestore.client()

#
#collection_ref = db.collection(u'InDoor').document(u'InNode01').collection(u'Temerpature')
#
###collection_ref.add(doc)
#
#
#
#docs =collection_ref.get()

#for doc in docs:
#    print(u'{} => {}'.format(doc.id, doc.to_dict()))







