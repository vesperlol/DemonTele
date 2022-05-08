import os,requests
from pystyle import *
from time import sleep
os.system("mode con cols=88 lines=50")
os.system("title " + "DemonTele || vesper#0003")
logo = """
                        ▄▄▄██████████████████████▄▄▄
                    ▄▄███████████████████████████████████▌▄▄
               ▀█████▌ ██████████████████████████████████ ██████▌
               ▄█████▌  ████████████████████████████████  ▐█████▌
               ▐█████    ▀████████████████████████████▀   ▐█████
                ▀████▌     █████████████████████████▀     ▐████▀
                ██████       ▀████████████████████▀       ██████
                ██████▌         ▀██████████████▀         ███████
                 ███████        ▄██████████████▄        ███████
                ▐████████▄   ▄▄██████████████████▄▄   ▄████████▌
                 ████████████   ▀▀████████████▀▀   ████████████
                  ██████████████▄▄   ▀▀▐▌▀▀   ▄▄██████████████
                  ▀█████████████████▄▄▄██▄▄▄█████████████████▌ 
               ███████████           ▄████▄           ███████████
               ███████████▄        ▄████████▄        ▄███████████
               ▐█████████████▄▄▄████████████████▄▄▄██████████████
                ████████████████████████████████████████████████
                 ██████████████████████████████████████████████
                   ██████▄▀▀▀▀███████▄▀▀▀▀▄████████▀▀▀▄██████▀
                   ▐██████████▄▄      ▀██▀      ▄▄ █████████
                    █████████   ▀▀▀▀▀  ▀▀  ▀▀▀▀▀   ████████▌
                     █████████                    ████████▀
                      ▀████████▄                ▄████████
                        ▀██████████▄▄▄▄▄▄▄▄▄▄██████████▀
                          ▀██████████████████████████▀
                           ▀████████████████████████
                             █████████████████████▀
                              ▀██████████████████
                                 ▀████████████▀
                                   ▀▀██████▀
                                       ▀▀
"""
while True:
    os.system("cls")
    API = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Insert Telegram Bot API >> ")
    try:
        r = requests.get(f"https://api.telegram.org/bot{API}/getMe")
        if r.status_code ==200:
            a = r.json()['result']['username'];break
        else:print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Invalid Bot API");sleep(2)
    except:print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Invalid Bot API");sleep(2)
class DemonTele:
    def __init__(self):
        os.system("cls")
        try:
            choice = int(input(f"""
           \t\t\t\t\t\t\t{Col.blue}{logo}

       \t\t\t{Col.white}\t#{Col.blue} Made by vesper{Col.white}#0003

\t\t\t{Col.white}! {Col.blue}Connected To {Col.white}{a} {Col.blue}BOT {Col.white}!
────────────────────────────────────────────────────────────────────────────────────────
\t\t{Col.white}[{Col.blue}1{Col.white}]{Col.blue} Info             \t{Col.white}[{Col.blue}6{Col.white}]{Col.blue} Leave Chat
\t\t{Col.white}[{Col.blue}2{Col.white}]{Col.blue} Get Chat ID      \t{Col.white}[{Col.blue}7{Col.white}]{Col.blue} Delete Bot Commands
\t\t{Col.white}[{Col.blue}3{Col.white}]{Col.blue} Get Members ID   \t{Col.white}[{Col.blue}8{Col.white}]{Col.blue} Delete Chat Photo
\t\t{Col.white}[{Col.blue}4{Col.white}]{Col.blue} Set Chat Title   \t{Col.white}[{Col.blue}9{Col.white}]{Col.blue} Create Invite Link
\t\t{Col.white}[{Col.blue}5{Col.white}]{Col.blue} Message Spammer  \t{Col.white}[{Col.blue}10{Col.white}]{Col.blue} Unpin Messages
{Col.white}────────────────────────────────────────────────────────────────────────────────────────
                                                     
>> """))
            if choice==1:self.info()
            elif choice==2:self.update()
            elif choice==3:self.members()
            elif choice==4:self.setTitle()
            elif choice==5:self.spammer()
            elif choice==6:self.leavechat()
            elif choice==7:self.delcommands()
            elif choice==8:self.delchatphoto()
            elif choice==9:self.createinvlink()
            elif choice==10:self.unpinMessage()
            else:print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Invalid Choice..");sleep(2);self.__init__()
        except:print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Invalid Choice..");sleep(2);self.__init__()
    def info(self):
        try:
            r = requests.get(f"https://api.telegram.org/bot{API}/getMe")
            if r.status_code==200:
                id = r.json()['result']['id']
                isbot = r.json()['result']['is_bot']
                firstname = r.json()['result']['first_name']
                username = r.json()['result']['username']
                print(f"""\n
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} BOT ID : {Col.white}{id}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Is Bot : {Col.white}{isbot}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} First Name : {Col.white}{firstname}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Username : {Col.white}{username}
                """)
                input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        except:self.__init__()
    def update(self):
            r = requests.get(f"https://api.telegram.org/bot{API}/getUpdates")
            if r.status_code==200:
                id = r.json()['result']
                chats = []
                for i in id:
                    try:
                        chatid = i['message']['chat']['id']
                        if chatid in chats:
                            pass
                        else:
                            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID Found : {Col.white}{chatid}")
                            chats.append(chatid)
                    except:pass
                    try:
                        chatid2 = i['my_chat_member']['chat']['id']
                        if chatid2 in chats:
                            pass
                        else:
                            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID Found : {Col.white}{chatid2}")
                            chats.append(chatid2)
                    except:pass
                input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def createinvlink(self):
        chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
        r = requests.get(f"https://api.telegram.org/bot{API}/createChatInviteLink?chat_id={chat_id}")
        if r.status_code==200:
            link = r.json()['result']['invite_link']
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Created Link : {Col.white}{link}")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        else:
            print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} No permissions OR private chat..")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def delchatphoto(self):
        chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
        r = requests.get(f"https://api.telegram.org/bot{API}/deleteChatPhoto?chat_id={chat_id}")
        if r.status_code==200:
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Successfully Deleted Chat Photo")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        else:
            print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} No permissions OR private chat..")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def delcommands(self):
        r = requests.get(f"https://api.telegram.org/bot{API}/deleteMyCommands")
        if r.status_code==200:
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Successfully Deleted Commands")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        else:
            print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Couldn't delete Commands")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def leavechat(self):
        chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
        r = requests.get(f"https://api.telegram.org/bot{API}/leaveChat?chat_id={chat_id}")
        if r.status_code==200:
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Successfully Left Chat")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        else:
            print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Can't leave a private chat.")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def unpinMessage(self):
        chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
        r = requests.get(f"https://api.telegram.org/bot{API}/unpinAllChatMessages?chat_id={chat_id}")
        if r.status_code==200:
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Successfully Unpinned All Messages.")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        else:
            print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} No permissions.")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def setTitle(self):
        chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
        title = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Set New Title >> ")
        r = requests.get(f"https://api.telegram.org/bot{API}/setChatTitle?chat_id={chat_id}&title={title}")
        if r.status_code==200:
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Set Title to : {Col.white}{title}")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        else:
            print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} No permissions.")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
    def members(self):
        chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
        try:
            r = requests.get(f"https://api.telegram.org/bot{API}/getChat?chat_id={chat_id}")
            if r.status_code==200:
                chattype = r.json()['result']['type']
                if chattype == 'private':
                    id = r.json()['result']['id']
                    first_name = r.json()['result']['first_name']
                    last_name = r.json()['result']['last_name']
                    print(f"""
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} PRIVATE CHAT WITH : {Col.white}{id}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} First Name : {Col.white}{first_name}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Last Name : {Col.white}{last_name}
                    """)
                    input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
                else:
                    id = r.json()["result"]['id']
                    type = r.json()['result']['type']
                    title = r.json()['result']['title']
                    cansendmessages = r.json()['result']['permissions']['can_send_messages']
                    cansendmedia = r.json()['result']['permissions']['can_send_media_messages']
                    cansendpolls = r.json()['result']['permissions']['can_send_polls']
                    cansendothermessages = r.json()['result']['permissions']['can_send_other_messages']
                    addwebpage = r.json()['result']['permissions']['can_add_web_page_previews']
                    canchangeinfo = r.json()['result']['permissions']['can_change_info']
                    caninviteusers = r.json()['result']['permissions']['can_invite_users']
                    canpingmessages = r.json()['result']['permissions']['can_pin_messages']
                    print(f"""
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} GROUP CHAT : {Col.white}{id}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Title : {Col.white}{title}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Type : {Col.white}{type}
                    """)
                    r = requests.get(f"https://api.telegram.org/bot{API}/getChatAdministrators?chat_id={chat_id}")
                    if r.status_code==200:
                        for i in r.json()['result']:
                            try:
                                adminid = i['user']['id']
                                adminname = i['user']['first_name']
                                adminname2 = i['user']['last_name']
                                print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Admin Found : {Col.white}{adminname} {adminname2} {Col.blue}({Col.white}{adminid}{Col.blue})")
                            except:pass
                    r = requests.get(f"https://api.telegram.org/bot{API}/getChatMemberCount?chat_id={chat_id}")
                    if r.status_code==200:
                        membercount = r.json()['result']
                        print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Membercount : {Col.white}{membercount}")
                    print(f"""
{Col.white}──────────── Bot Permissions ─────────────────
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Send Messages : {Col.white}{cansendmessages}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Send Media Messages : {Col.white}{cansendmedia}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Send Polls : {Col.white}{cansendpolls}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Send Other Messages : {Col.white}{cansendothermessages}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Add Web Page Previews : {Col.white}{addwebpage}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Change Info : {Col.white}{canchangeinfo}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Invite Users : {Col.white}{caninviteusers}
{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Can Pin Messages : {Col.white}{canpingmessages}
                    """)
                    input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
        except:pass
    def spammer(self):
        valid = 0
        while True:
            try:
                chat_id = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Chat ID >> ")
                message = input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Message >> ")
                amount = int(input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Amount >> "))
                message = message.replace(" ","+");break
            except:pass
        while True:
            r = requests.get(f"https://api.telegram.org/bot{API}/sendMessage?chat_id={chat_id}&text={message}")
            if r.status_code==200:
                valid +=1
                print(f"{Col.white}[{Col.green}+{Col.white}]{Col.green} Sent Message ! ({Col.white}{valid}{Col.green}) ")
            elif r.json()['error_code']==429:
                print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Rate Limited : ({Col.white}{r.json()['parameters']['retry_after']}{Col.pink}ms)")
                sleep(r.json()['parameters']['retry_after'] / 1000)
            elif r.status_code==404:
                print(f"{Col.white}[{Col.pink}!{Col.white}]{Col.pink} Error Occured ! Chat ID Invalid or Bot API Invalid");break
            if valid == amount:break
        if valid != amount:
            self.__init__()
        else:
            print(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Finished Process.. ")
            input(f"{Col.white}[{Col.blue}+{Col.white}]{Col.blue} Press Enter to continue..");self.__init__()
                  
DemonTele()