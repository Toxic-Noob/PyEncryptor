# -*- coding: utf-8 -*-

# PyEncryptor
# Tool: A Python2 and Python3 Code Encoder
#Author: ToxicNoob
# Coder: HunterSl4d3

import os
import sys
import time
import marshal
import zlib
import base64
import compileall
import shutil

#Setting Up Logo#
try:
	columns = shutil.get_terminal_size().columns
	column1 = columns + 15
	column2 = columns + 5
	column3 = columns + 20
except:
	rows, columns = os.popen('stty size', 'r').read().split()
	column1 = 0
	column2 = 0
	column3 = 0

#Logo
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(column2))
    print("\033[94m│    \033[92m▛▀▖   ▛▀▘               ▐    \033[94m       │".center(column1))
    print("\033[94m│    \033[92m▙▄▘▌ ▌▙▄ ▛▀▖▞▀▖▙▀▖▌ ▌▛▀▖▜▀ ▞▀▖▙▀▖\033[94m   │".center(column1))
    print("\033[94m│    \033[92m▌  ▚▄▌▌  ▌ ▌▌ ▖▌  ▚▄▌▙▄▘▐ ▖▌ ▌▌  \033[94m   │".center(column1))
    print("\033[94m│    \033[92m▘  ▗▄▘▀▀▘▘ ▘▝▀ ▘  ▗▄▘▌   ▀ ▝▀ ▘  \033[94m   │".center(column1))
    print("\033[94m│                                        │".center(column2))
    print("\033[94m│ \033[95mAuthor : ToxicNoob                     \033[94m│".center(column1))
    print("\033[94m│ \033[95mTool   : Encode Python2 and Python3    \033[94m│".center(column1))
    print("\033[94m│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(column1))
    print("\033[94m│ \033[95mCoder  : HunterSl4d3              \033[37mV2.0 \033[94m│".center(column3))
    print("\033[94m└────────────────────────────────────────┘".center(column2))

#Exit Tool Massage
def logout():
    psb("\n    \033[94m[\033[92m*\033[94m]\033[92m Thanks For Using Our Tool")
    psb("    \033[94m[\033[92m*\033[94m]\033[92m For More Tools, Visit: \n")
    print("\033[93m[ \033[92mhttps://github.com/Toxic-Noob/ \033[93m]\033[37m\n".center(column3))
    sys.exit()

#Python Version Banner
def banner():
    version = str(sys.version_info[:3][0]) + "." + str(sys.version_info[:3][1]) + "." + str(sys.version_info[:3][2])
    
    print("\033[93m-" * int(columns))
    if (sys.version_info[:3][0] < 3):
        print("\033[92m\t\tPython Version : \033[37m"+version)
    else:
        print(("\033[92mPython Version : \033[37m"+version).center(columns + 10))
    print("\033[93m-" * int(columns))

#Flush Print
def psb(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

#Taking Input Depending on Python Version
def verInput(data):
    version = sys.version_info[:2]
    if (version < (3, 0)):
        dataInput = raw_input(data)
    else:
        dataInput = input(data)
    return dataInput

#Marshal_Code_Executor#
marshalHead = "# Encoded By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport marshal\n\nexec(marshal.loads("

marshalTail = "))"

#Base64_Code_Executor#
b64Head = "# Encoded By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport base64\n\nexec(base64.b64decode("

b64Tail = "))"

#Zlib_Code_Executor#
zlibHead = "# Encoded By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport zlib\n\nexec(zlib.decompress("

zlibTail = "))"

#Zlib+B64+Mar_Code_Executor#
allHead = "# Encoded By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport marshal, base64, zlib\n\nexec(marshal.loads(zlib.decompress(base64.b64decode("

allTail = "))))"

#Encode Marshal
def encodeMarshal(data):
    code = compile(data, "ToxicNoob", 'exec')
    dump = marshal.dumps(code)
    encData = marshalHead +repr(dump) + marshalTail
    
    return encData

#Encode Zlib
def encodeZlib(data):
    code = data.encode()
    dump = zlib.compress(code, 2)
    encData = zlibHead + repr(dump) + zlibTail
    
    return encData

#Encode Base64
def encodeBase64(data):
    code = data.encode()
    dump = base64.b64encode(code)
    encData = b64Head + repr(dump) + b64Tail
    
    return encData

#Python Bytecode Encode
def encodePyc(data):
    tmp = open("temp.py", "w")
    tmp.write(data)
    tmp.close()
    if (sys.version_info[:2] < (3, 0)):
        compileall.compile_file("temp.py")
    else:
        compileall.compile_file("temp.py", legacy=True)
    
    return True

#Marshal + Zlib + Base64
def encodeAll(data):
    data = compile(data, "ToxicNoob", "exec")
    data = marshal.dumps(data)
    data = zlib.compress(data)
    dump = base64.b64encode(data)
    encData = allHead + repr(dump) + allTail
    
    return encData

#Hard Encode
def encodeHard(data):
    power = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Hard Power Amount (\033[37mMAX: 15\033[92m):> \033[37m")
    
    try:
        power = int(power)
    except:
        psb("\n\033[92m    [\033[91m*\033[92m] Your Power Amount Must Be a Number!")
        power = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Hard Power Amount (\033[37mMAX: 15\033[92m):> \033[37m")
        power = int(power)
    
    while (power > 15):
        psb("\n\033[92m    [\033[91m*\033[92m] Max Hard Amount Is \033[37m15!")
        power = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Hard Power Amount (\033[37mMAX: 15\033[92m):> \033[37m")
        power = int(power)
    
    psb("\n\033[92m    [\033[37m*\033[92m] Encoding Your File...\033[30m")
    
    powerData = data
    
    for i in range(power):
        powerData = encodeAll(powerData)
    
    encodePyc(powerData)
    
    return True


#Get File Data
def getFile():
    path = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Your File Path:> \033[37m")
    
    while not os.path.exists(path):
        psb("\n\033[92m    [\033[91m!\033[92m] File Does Not Exists!")
        time.sleep(0.4)
        path = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Your File Path:> \033[37m")
    
    fileData = open(path, "r").read()
    
    global fileName
    if ("/" in path):
        fileName = path.split("/")[-1:]
    else:
        fileName = path
    
    return fileData

#Save File Data
def saveFile(encData):
    if (".py" in fileName):
        savefileName = fileName.replace(".py", "_enc.py")
    else:
        savefileName = fileName + "_enc.py"
    
    savePath = "/sdcard/PyEncryptor/" + savefileName
    
    file = open(savePath, "w")
    file.write(encData)
    file.close()

#PYC Move File
def moveFile():
    if (".py" in fileName):
        savefileName = fileName.replace(".py", "_enc.py")
    else:
        savefileName = fileName + "_enc.py"
    
    savePath = "/sdcard/PyEncryptor/" + savefileName
    
    os.system("mv temp.pyc " + savePath + " >/dev/null 2>&1")
    os.system("rm temp.py > /dev/null 2>&1")
    


#Encoding Process
def encode(type):
    fileData = getFile()
    
    
    if not (type == "hard"):
        psb("\n\033[92m    [\033[37m*\033[92m] Encoding Your File...\033[30m")
    
    if (type == "marshal"):
        encData = encodeMarshal(fileData)
        saveFile(encData)
        
    elif (type == "zlib"):
        encData = encodeZlib(fileData)
        saveFile(encData)
        
    elif (type == "base64"):
        encData = encodeBase64(fileData)
        saveFile(encData)
        
    elif (type == "pyc"):
        encData = encodePyc(fileData)
        moveFile()
        
    elif (type == "all"):
        encData = encodeAll(fileData)
        saveFile(encData)
        
    elif (type == "hard"):
        encData = encodeHard(fileData)
        moveFile()
    
    
    time.sleep(1)
    psb("\n\033[92m    [\033[37m*\033[92m] Encoding Complete!")
    psb("\n\033[92m    [\033[37m*\033[92m] File Saved In \033[37m/sdcard/PyEncryptor \033[92m Directory, as \033[37m " + fileName.replace(".py", "_enc.py") + "\033[92m....\033[37m\n")


#Update Tool
def update():
    logo()
    psb("\n\033[92m    [\033[37m*\033[92m] Please Wait!")
    psb("\033[92m    [\033[37m*\033[92m] Checking Update...")
    import requests
    try:
        toolVersion = open(".version", "r").read()
    except:
        toolVersion = "ToxicNoob"
    try:
        mainVersion = requests.get("https://raw.githubusercontent.com/Toxic-Noob/PyEncryptor/main/.version").text
    except:
        psb("\n\033[92m    [\033[91m!\033[92m] Please Turn On Internet Connection!")
        l = verInput("\n\033[92m    [\033[37m*\033[92m] Press Enter To Continue....")
        update()
    if (toolVersion == mainVersion):
        psb("\n\033[92m    [\033[37m*\033[92m] You are Using the Latest Version of PyEncryptor!")
        l = verInput("\033[92m    [\033[37m*\033[92m] Press Enter To Go Back....")
        logo()
        main()
    else:
        psb("\n\033[92m    [\033[37m!\033[92m] Tool Update Found!!")
        psb("\033[92m    [\033[37m*\033[92m] Updating Tool...")
        os.system("cd .. && rm -rf PyEncryptor && git clone https://github.com/Toxic-Noob/PyEncryptor > /dev/null 2>&1")
        psb("\n\033[92m    [\033[37m*\033[92m] Tool Updated Successfully!")
        psb("\033[92m    [\033[37m*\033[92m] Starting Latest Version of PyEncryptor...")
        time.sleep(1)
        os.system("cd .. && cd PyEncryptor && python PyEnc.py")



#Main Menu
def main():
    psb("\n\033[92m    [\033[37m*\033[92m] Choose Your Option:")
    
    print("\n\033[92m    [\033[37m01\033[92m] Marshal")
    print("\033[92m    [\033[37m02\033[92m] Zlib")
    print("\033[92m    [\033[37m03\033[92m] Base64")
    print("\033[92m    [\033[37m04\033[92m] Python Bytecode (\033[37m.pyc\033[92m)")
    print("\033[92m    [\033[37m05\033[92m] Marshal + Zlib + Base64")
    print("\033[92m    [\033[37m06\033[92m] Hard Encrypt")
    print("\033[92m    [\033[37m07\033[92m] Update Tool")
    print("\033[92m    [\033[37m08\033[92m] Exit")
    
    op = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "")
    
    while not (op in ["1", "2", "3", "4", "5", "6", "7", "8"]):
        psb("\n\033[92m    [\033[91m!\033[92m] Please Enter a Correct Option!")
        op = verInput("\n\033[92m    [\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "")
    
    if (op == "1"):
        encode("marshal")
    elif (op == "2"):
        encode("zlib")
    elif (op == "3"):
        encode("base64")
    elif (op == "4"):
        encode("pyc")
    elif (op == "5"):
        encode("all")
    elif (op == "6"):
        encode("hard")
    elif (op == "7"):
        update()
    elif (op == "8"):
        logout()



if (__name__ == "__main__"):
    logo()
    banner()
    main()

