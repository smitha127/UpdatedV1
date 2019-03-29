import requests
from bs4 import BeautifulSoup
import json
import simple.config3
import sys
import simple.Cards_test_2


class Scrapy():

    def __init__(self):
        self.head = simple.config3.obj.Headers()
        self.cred = simple.config3.obj.Credentials()
        self.url1 = simple.config3.obj.url_store()

    def Login(self):

        with requests.session() as s:
            url_1 = self.url1[0]
            header = json.loads(self.head.replace("'", "\""))
            credentials = self.cred
            r = s.get(url_1, headers=header)
            # r = s.post(url_1, data=self.cred, headers=header)
            url_2 = self.url1[1]
            r = s.get(url_2)
            # print(type(r1))
            # obj1.Boards()
            Scrapy.Boards(self, r)

    def Boards(self, r):

        with requests.session() as s:
            url_1 = self.url1[0]
            header = json.loads(self.head.replace("'", "\""))
            r = s.post(url_1, data=self.cred, headers=header)
            #board_no = ["123457855", "111137067", "106606106", "107600350"]
            board_no=["111137067"]
            for i in board_no:
                r = s.get("https://rolls-royce.leankit.com/io/board/" + i + "/card?limit=200&id=" + i + "")
                soup1 = BeautifulSoup(r.content, 'lxml')
                cards1 = soup1.find("p")
                cards2 = cards1.text
                listofcards = []
                card_Nos = {}
                card_Nos = json.loads(cards2)
                asd = card_Nos['cards']
               # print(type(asd))
                # simple.Cards_test_2.Scrapy1.Cards(asd)
                for i in range(len(asd)):
                    listofcards.append(card_Nos['cards'][i]['id'])
                print(listofcards)
                # return listofcards
                Scrapy.Cards(self, listofcards)
                # print(listofcards)
                # simple.Cards_test_2.Scrapy1.Cards(self)





    def Cards(self, li):

        # print(li)
        with requests.session() as s:
            url_1 = self.url1[0]
            header = json.loads(self.head.replace("'", "\""))
            r = s.post(url_1, data=self.cred, headers=header)
            # board_no = ["123457855", "111137067", "106606106", "107600350"]
            # for i in board_no:
            # r = s.get("https://rolls-royce.leankit.com/io/board/" + i + "/card?limit=200&id=" + i + "")
            # soup1 = BeautifulSoup(r.content, 'lxml')
            # cards1 = soup1.find("p")
            # cards2 = cards1.text
            # listofcards = []
            # card_Nos = {}
            # card_Nos = json.loads(cards2)
            # asd = card_Nos['cards']
            # #print(asd)
            # for i in range(len(asd)):
            #     listofcards.append(card_Nos['cards'][i]['id'])
            # #print(listofcards)
            listofcards = li
            for i in listofcards:
                try:
                    r = s.get("https://rolls-royce.leankit.com/io/card/" + i + "?id=" + i + "")
                    soup = BeautifulSoup(r.content, 'lxml')
                    card = soup.findAll(text=True)
                    if len(card) > 1:
                        card = card[0] + card[len(card) - 1]
                    elif len(card) == 1:
                        card = card[0]
                    card_Details = json.loads(card)
                    card_body = soup.find('body')
                    # actualFinish = card_Details["actualFinish"]
                    # actualStart = card_Details['actualStart']
                    # blockedStatus = card_Details['blockedStatus']['isBlocked']
                    # blockedStatus_reason = card_Details['blockedStatus']['reason']
                    # blockedStatus_reason = card_Details['blockedStatus']['date']
                    # board_ID = card_Details['board']['id']
                    # board_Title = card_Details['board']['title']
                    # createdOn = card_Details['createdOn']
                    plannedFinish = card_Details['plannedFinish']
                    externalLinks = card_Details['externalLinks']
                    customId_ConsessionNo = card_Details['customId']['value']
                    if (externalLinks != []):
                        externalLinks = card_Details['externalLinks'][0]['url']
                    elif (externalLinks == None):
                        externalLinks = card_Details['externalLinks'][0]['label']
                    elif (externalLinks == []):
                        externalLinks = soup.findAll(text=True)[1]
                    card_ID = card_Details['id']
                    lane_ID = card_Details['lane']['id']
                    lane_ClassType = card_Details['lane']['laneClassType']
                    lane_title = card_Details['lane']['title']
                    # updatedOn = card_Details['updatedOn']
                    # movedOn = card_Details['movedOn']
                    priority = card_Details['priority']
                    card_size = card_Details['size']
                    card_title = card_Details['title']
                    card_title1 = card_title.split(" ")
                    engieneNo = card_title1[0]
                    engpartNo = str(card_title1[1:])
                    card_type = card_Details['type']['title']
                    if (lane_ClassType == "backlog"):
                        card_Details_data = {"card_title": card_title, "engieneNo": engieneNo, "partNo": engpartNo,
                                             "customId_ConsessionNo": customId_ConsessionNo,
                                             "plannedFinish": plannedFinish, "externalLinks": externalLinks,
                                             "card_ID": card_ID,
                                             "lane_ID": lane_ID, "lane_ClassType": lane_ClassType,
                                             "priority": priority,
                                             "card_size": card_size, "card_type": card_type}
                        print(card_Details_data)

                except:
                    pass

        # except Exception as e:
        # print(e)
        # line = sys.exc_info()[-1].tb_lineno
        # print(line)


obj1 = Scrapy()
obj1.Login()
# var = obj1.Login()
# print(var)

# print(var)
# obj1.Boards()
# print(li)
# obj1.Cards(li)
