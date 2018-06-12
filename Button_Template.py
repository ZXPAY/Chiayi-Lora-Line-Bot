from linebot.models import*
from words import *
### Button templates to define in this file

### 隨機輸入數字時產生的 button template, 功能簡介與輸入
function_template = TemplateSendMessage(alt_text='目錄 template',
                                      template=(ButtonsTemplate(
                                          title='嘉義大學生物機電工程學系  整合空氣感測應用服務',
                                          text='歡迎使用',
                                          thumbnail_image_url='https://i.imgur.com/w10BJAF.jpg',
                                          actions=[
                                                  MessageTemplateAction(
                                                          label='Line-Bot介紹',
                                                          text='Line-Bot介紹'
                                                          ),
                                                  MessageTemplateAction(
                                                          label='索引資料功能',
                                                          text='索引資料功能'
                                                          ),
                                                  MessageTemplateAction(
                                                          label='團隊簡介與聯絡',
                                                          text='團隊簡介與聯絡'
                                                          ),
                                                  MessageTemplateAction(
                                                          label='指令範例',
                                                          text='指令範例'
                                                          )
                                                  ])
                                            )
                                        )


### 索引資料功能
index_template = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='選擇資料庫',
                                  text='請選擇以下資料庫\n',
                                  thumbnail_image_url='https://i.imgur.com/ZHguCZH.png',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='室內資料庫 12000008',
                                                  text='indoor database1'
                                                  ),
                                          MessageTemplateAction(
                                                  label='室內資料庫 12000009',
                                                  text='indoor database2'
                                                  ),
                                          MessageTemplateAction(
                                                  label='室外資料庫 12000006',
                                                  text='outdoor database1'
                                                  ),
                                          MessageTemplateAction(
                                                  label='室外資料庫 12000007',
                                                  text='outdoor database2'
                                                  ),
                                          ])
                                    )
                                )

### 索引資料於室內資料庫
index_indoor_template1 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000008',
                                  text='請選擇您要搜索的資料',
                                  thumbnail_image_url='https://i.imgur.com/PrTZjLa.jpg',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度,濕度,一氧化碳',
                                                  text='indoor1$_First'
                                                  ),
                                          MessageTemplateAction(
                                                  label='二氧化碳,瓦斯,空氣微粒',
                                                  text='indoor1$_Second'
                                                  ),
                                          MessageTemplateAction(
                                                  label='火焰,風速,下雨',
                                                  text='indoor1$_Third'
                                                  ),
                                          MessageTemplateAction(
                                                  label='最新室內資料',
                                                  text='recent indoor data1'
                                                  ),
                                          ])
                                    )
                                )

index_indoor_template1_1 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000008',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度 Temperature',
                                                  text='indoor1$_TS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='濕度 Humidity',
                                                  text='indoor1$_HS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='一氧化碳 CO',
                                                  text='indoor1$_CS'
                                                  ),
                                          ])
                                    )
                                )

index_indoor_template1_2 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000008',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='二氧化碳 CO2',
                                                  text='indoor1$_IS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='液化石油氣 LPG',
                                                  text='indoor1$_LS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='空氣微粒 PM',
                                                  text='indoor1$_MS'
                                                  ),

                                          ])
                                    )
                                )
index_indoor_template1_3 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000008',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='火焰感測 Fire Detect',
                                                  text='indoor1$_FS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='風速 Wind Velocity',
                                                  text='indoor1$_WS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='雨量感測 Rain Detect',
                                                  text='indoor1$_RS'
                                                  ),
                                          ])
                                    )
                                )

index_indoor_template2 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000009',
                                  text='請選擇您要搜索的資料',
                                  thumbnail_image_url='https://i.imgur.com/PrTZjLa.jpg',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度,濕度,一氧化碳',
                                                  text='indoor2$_First'
                                                  ),
                                          MessageTemplateAction(
                                                  label='二氧化碳,瓦斯,空氣微粒',
                                                  text='indoor2$_Second'
                                                  ),
                                          MessageTemplateAction(
                                                  label='火焰,風速,下雨',
                                                  text='indoor2$_Third'
                                                  ),
                                          MessageTemplateAction(
                                                  label='最新室內資料',
                                                  text='recent indoor data2'
                                                  ),
                                          ])
                                    )
                                )
index_indoor_template2_1 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000009',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度 Temperature',
                                                  text='indoor2$_TS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='濕度 Humidity',
                                                  text='indoor2$_HS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='一氧化碳 CO',
                                                  text='indoor2$_CS'
                                                  ),
                                          ])
                                    )
                                )

index_indoor_template2_2 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000009',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='二氧化碳 CO2',
                                                  text='indoor2$_IS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='液化石油氣 LPG',
                                                  text='indoor2$_LS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='空氣微粒 PM',
                                                  text='indoor2$_MS'
                                                  ),

                                          ])
                                    )
                                )
index_indoor_template2_3 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室內資料庫 12000009',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='火焰感測 Fire Detect',
                                                  text='indoor2$_FS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='風速 Wind Velocity',
                                                  text='indoor2$_WS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='雨量感測 Rain Detect',
                                                  text='indoor2$_RS'
                                                  ),
                                          ])
                                    )
                                )

### 索引資料於室外資料庫
index_outdoor_template1 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000006',
                                  text='請選擇您要搜索的資料',
                                  thumbnail_image_url='https://i.imgur.com/PrTZjLa.jpg',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度,濕度,二氧化碳',
                                                  text='outdoor1$_First'
                                                  ),
                                          MessageTemplateAction(
                                                  label='空氣微粒,風速,雨量',
                                                  text='outdoor1$_Second'
                                                  ),
                                          MessageTemplateAction(
                                                  label='大氣壓力,緯度,經度',
                                                  text='outdoor1$_Third'
                                                  ),
                                          MessageTemplateAction(
                                                  label='最新室外資料',
                                                  text='recent outdoor data1'
                                                  ),
                                          ])
                                    )
                                )

index_outdoor_template1_1 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000006',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度 Temperature',
                                                  text='outdoor1$_TS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='濕度 Humidity',
                                                  text='outdoor1$_HS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='二氧化碳 CO2',
                                                  text='outdoor1$_IS'
                                                  ),
                                          ])
                                    )
                                )
index_outdoor_template1_2 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000006',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='空氣微粒 PM',
                                                  text='outdoor1$_MS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='風速 Wind Velocity',
                                                  text='outdoor1$_WS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='雨量感測 Rain Detect',
                                                  text='outdoor1$_RS'
                                                  ),
                                          ])
                                    )
                                )
index_outdoor_template1_3 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000006',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                           MessageTemplateAction(
                                                  label='大氣氣壓 Pressure',
                                                  text='outdoor1$_AS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='緯度 Latitude',
                                                  text='outdoor1$_DS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='經度 Longitude',
                                                  text='outdoor1$_NS'
                                                  ),
                                          ])
                                    )
                                )
index_outdoor_template2 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000007',
                                  text='請選擇您要搜索的資料',
                                  thumbnail_image_url='https://i.imgur.com/PrTZjLa.jpg',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度,濕度,二氧化碳',
                                                  text='outdoor2$_First'
                                                  ),
                                          MessageTemplateAction(
                                                  label='空氣微粒,風速,雨量',
                                                  text='outdoor2$_Second'
                                                  ),
                                          MessageTemplateAction(
                                                  label='大氣壓力,緯度,經度',
                                                  text='outdoor2$_Third'
                                                  ),
                                          MessageTemplateAction(
                                                  label='最新室外資料',
                                                  text='recent outdoor data2'
                                                  ),
                                          ])
                                    )
                                )

index_outdoor_template2_1 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000007',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='溫度 Temperature',
                                                  text='outdoor2$_TS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='濕度 Humidity',
                                                  text='outdoor2$_HS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='二氧化碳 CO2',
                                                  text='outdoor2$_IS'
                                                  ),
                                          ])
                                    )
                                )
index_outdoor_template2_2 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000007',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                          MessageTemplateAction(
                                                  label='空氣微粒 PM',
                                                  text='outdoor2$_MS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='風速 Wind Velocity',
                                                  text='outdoor2$_WS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='雨量感測 Rain Detect',
                                                  text='outdoor2$_RS'
                                                  ),
                                          ])
                                    )
                                )
index_outdoor_template2_3 = TemplateSendMessage(alt_text='索引資料 template',
                              template=(ButtonsTemplate(
                                  title='室外資料庫 12000007',
                                  text='請選擇您要搜索的資料',
                                  actions=[
                                           MessageTemplateAction(
                                                  label='大氣氣壓 Pressure',
                                                  text='outdoor2$_AS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='緯度 Latitude',
                                                  text='outdoor2$_DS'
                                                  ),
                                          MessageTemplateAction(
                                                  label='經度 Longitude',
                                                  text='outdoor2$_NS'
                                                  ),
                                          ])
                                    )
                                )
