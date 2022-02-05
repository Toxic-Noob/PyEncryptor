#####################################
# Coded By HunterSl4d3
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob/
# You Are Welcomed To Take Knowledge From This Script
# But You Have No Permission To Copy Codes!!
#####################################



import sys, time, os
import marshal, base64, zlib
import compileall

#Marshal_Code_Executor#
mar_code = "# Encrypted By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport marshal\nexec(marshal.loads("

last = "))"

#Base64_Code_Executor#
b64_code = "# Encrypted By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport base64\nexec(base64.b64decode("
b64_code_last = "))"

#Zlib_Code_Executor#
zlib_code = "# Encrypted By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport zlib\nexec(zlib.decompress("

last = "))"

#Zlib+B64+Mar_Code_Executor#
zlib_b64_mar_code = "# Encrypted By PyEncryptor\n# A Product Of ToxicNoob\n# https://github.com/Toxic-Noob\n\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode("

zlib_b64_mar_last = "))))"

#Needed_Functions#
def path_to_name(path):
    sp = path.split("/")
    name = sp[-1]
    return name

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)

def ver_in(data):
    ver_py = sys.version_info[:2]
    if (ver_py < (3, 0)):
        data_in = raw_input(data)
    else:
        data_in = input(data)
    return data_in
    
rows, columns = os.popen('stty size', 'r').read().split()

def ver_in_path():
    path_data = ver_in("\033[92m\n    [*] Enter File Path:> \033[37m")
    while not os.path.exists(path_data):
        psb("\n    \033[91m[!] File Path Not Exists!!\033[92m")
        time.sleep(0.8)
        path_data = ver_in("\033[92m\n    [*] Enter File Path:> \033[37m")
    return path_data

def logout():
    time.sleep(0.5)
    love = b'\xf0\x9f\x92\x93'
    if not (sys.version_info[:2] < (3, 0)):
        love = love.decode()
    psb("\n\033[92m    ["+love+"] Thanks For Using Our Tool..")
    psb("    ["+love+"] For More Tools, Visit:")
    print("\n\t\033[33m[\033[92m https://github.com/Toxic-Noob/ \033[33m]\033[37m\n")
    time.sleep(0.4)
    sys.exit()

def logo():
	os.system("clear")
	time.sleep(0.5)
	logopsb("\033[0;92m ____        _____                             _   \n|  _ \ _   _| ____|_ __   ___ _ __ _   _ _ __ | |_ \n| |_) | | | |  _| | '_ \ / __| '__| | | | '_ \| __|\n|  __/| |_| | |___| | | | (__| |  | |_| | |_) | |_ \n|_|    \__, |_____|_| |_|\___|_|   \__, | .__/ \__|\n       |___/                       |___/|_|        ")
	logopsb("\033[3;90m		  	A Product Of ToxicNoob\033[0;92m")
	time.sleep(0.6)
	logopsb("\033[34m\n|****************************************************|\n|\033[3m Author   : HunterSl4d3                             \033[0;34m|\n|\033[3m Tool     : Python Encryptor                        \033[0;34m|\n|\033[3m Version  : 1.4                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : HunterSl4d3      		     	     \033[0;34m|\n******************************************************")
	time.sleep(0.8)

##Code_Encrypting_Functions##

#Marshal#
def mar_enc():
    path = ver_in_path()
    psb("\033[92m\n    [*] Please Wait, Encoding Your File...")
    time.sleep(1)
    file_name = path_to_name(path)
    out_name = file_name.replace(".py", "")
    out = "/sdcard/PyEncryptor/"+out_name+"_enc.py"
    file = open(path, "r").read()
    code = compile(file, '', 'exec')
    data = marshal.dumps(code)
    code_out = open(out, "w")
    code_out.write(mar_code+repr(data)+last)
    code_out.close()
    psb("\n    [*] Your File Saved In /sdcard/PyEncryptor Directory as "+out_name+"_enc.py...\033[37;40;0m\n")
    logout()
    
#Base64#
def b64_enc():
    path = ver_in_path()
    psb("\033[92m\n    [*] Please Wait, Encrypting Your File...")
    time.sleep(1)
    file_name = path_to_name(path)
    out_name = file_name.replace(".py", "")
    out = "/sdcard/PyEncryptor/"+out_name+"_enc.py"
    file = open(path, "r").read()
    code = file.encode("ascii")
    code = base64.b64encode(code)
    data = code.decode("ascii")
    code_out = open(out, "w")
    code_out.write(b64_code+repr(data)+b64_code_last)
    code_out.close()
    psb("\n    [*] Your File Saved In /sdcard/PyEncryptor Directory as "+out_name+"_enc.py...\033[37;40;0m\n")
    logout()

#Zlib#
def zlib_enc():
    path = ver_in_path()
    psb("\033[92m\n    [*] Please Wait, Encrypting Your File...")
    time.sleep(1)
    file_name = path_to_name(path)
    out_name = file_name.replace(".py", "")
    out = "/sdcard/PyEncryptor/"+out_name+"_enc.py"
    file = open(path, "r").read()
    code = file.encode()
    data = zlib.compress(code, 2)
    code_out = open(out, "w")
    code_out.write(zlib_code+repr(data)+last)
    psb("\n    [*] Your File Saved In /sdcard/PyEncryptor Directory as "+out_name+"_enc.py...\033[37;40;0m\n")
    logout()

#Base64+Marshal+Zlib#
def b64_mar_zlib():
    path = ver_in_path()
    psb("\033[92m\n    [*] Please Wait, Encrypting Your File...")
    time.sleep(1)
    file_name = path_to_name(path)
    out_name = file_name.replace(".py", "")
    out = "/sdcard/PyEncryptor/"+out_name+"_enc.py"
    file = open(path, "r").read()
    code = compile(file, '', 'exec')
    mar_data = marshal.dumps(code)
    zlib_data = zlib.compress(mar_data, 2)
    data = base64.b64encode(zlib_data)
    code_out = open(out, "w")
    code_out.write(zlib_b64_mar_code+repr(data)+zlib_b64_mar_last)
    psb("\n    [*] Your File Saved In /sdcard/PyEncryptor Directory as "+out_name+"_enc.py...\033[37;40;0m\n")
    logout()

#PyCompile#
def py_to_pyc():
    path = ver_in_path()
    psb("\033[92m\n    [*] Please Wait, Encrypting Your File...\033[30m")
    time.sleep(1)
    file_name = path_to_name(path)
    out_name = file_name.replace(".py", "")
    out = "/sdcard/PyEncryptor/"+out_name+"_enc.py"
    file = open(path, "r").read()
    code = compile(file, '', 'exec')
    data = marshal.dumps(file)
    f_w = open(out_name+"_tmp.py", "w")
    f_w.write(mar_code+repr(data)+last)
    f_w.close()
    if (sys.version_info[:2] < (3, 0)):
        compileall.compile_file(out_name+"_tmp.py")
    else:
        compileall.compile_file(out_name+"_tmp.py", legacy=True)
    os.system("mv "+out_name+"_tmp.pyc "+out)
    os.system("rm "+out_name+"_tmp.py")
    psb("\033[92m    [*] Your File Saved In /sdcard/PyEncryptor Directory as "+out_name+"_enc.py...\033[37;40;0m\n")
    logout()
    
#Tool_Version_Updates#
def version():
    psb("\033[92m\n    [*] Please Wait, Checking Version...")
    import requests
    ver = open(".version", "r").read()
    mainver = requests.get("https://raw.githubusercontent.com/Toxic-Noob/PyEncryptor/main/.version")
    mainver = mainver.text
    if (ver==mainver):
        psb("\n    [*] You are using the latest Version of PyEncryptor...")
        psb("\n    [*] Thanks For Using Our Tool...")
        time.sleep(1.5)
        logo()
        options()
    else:
        psb("\n    [*] Tool Update Found!!")
        psb("    [*] Updating Tool...")
        os.system("cd .. && rm -rf PyEncryptor && git clone https://github.com/Toxic-Noob/PyEncryptor > /dev/null 2>&1")
        psb("    [*] Tool Updated Successfully..!")
        psb("    [*] Starting Latest Version of PyEncryptor...")
        psb("    [*] Thanks For Using Our Tool...")
        time.sleep(1.5)
        os.system("cd .. && cd PyEncryptor && python PyEnc.py")

#Options#
def options():
    ver_print = str(sys.version_info[:3]).replace("(", "").replace(")", "").replace(",", ".")
    print("\033[33m-"*int(columns))
    print("\033[92m\t\tPython Version : "+ver_print)
    print("\033[33m-"*int(columns))
    psb("\n\033[92m    [*] Choose Your Encrypting Method...")
    print("\n\033[92m    [01] Marshal")
    print("    [02] Base64")
    print("    [03] Zlib")
    print("    [04] Marshal, Zlib, Base64")
    print("    [05] Python Binary File (.pyc)")
    print("    [06] Update Tool")
    print("    [##] Exit")
    
    op = ver_in("\033[92m\n    [*] Enter Your Encoding Choice:> \033[37m").replace("0", "").replace("##", "#")
    while not (op in ["1", "2", "3", "4", "5", "6", "#"]):
        psb("\n\033[91m    [!] Please Choose an Option From Above...")
        op = ver_in("\033[92m\n    [*] Enter Your Encoding Choice:> \033[37m").replace("0", "").replace("##", "#")
    if(op=="1"):
        mar_enc()
    elif(op=="2"):
        b64_enc()
    elif(op=="3"):
        zlib_enc()
    elif(op=="4"):
        b64_mar_zlib()
    elif(op=="5"):
        py_to_pyc()
    elif(op=="6"):
        version()
    elif(op=="7"):
        logout()


if __name__ == '__main__':
    if not os.path.exists("/sdcard/PyEncryptor"):
        os.mkdir("/sdcard/PyEncryptor")
    logo()
    options()

