import socket
import time

UDP_IP = "192.168.0.4"
UDP_Port = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main_title():
    print('\033[96m')
    print(" ____      ____      _                                         _                         __        ____    ")
    print("|_  _|    |_  _|    / |_                                      / |_                      /  |     .'    '.  ")
    print("  \ \  /\  / /,--. `| |-'.---.  _ .--.  .--.    _   __  .--. `| |-'.---.  _ .--..--.    `| |    |  .--.  | ")
    print("   \ \/  \/ /`'_\ : | | / /__ \[ `/'`\]( (`\]  [ \ [  ]( (`\] | | / /__ \[ `.-. .-. |    | |    | |    | |  ")
    print("    \  /\  / // | |,| |,| \__., | |     `'.'.   \ '/ /  `'.'. | |,| \__., | | | | | |   _| |_  _|  `--'  |  ")
    print("     \/  \/_ _'-;__/\__/ '.__.'[___]   [\__) )[\_:  /  [\__) )\__/ '.__.'[___||__||__] |_____|(_)'.____.'   ") 
    print('===========================================================================================================  ')
    print("                                                                                         Light for terminal beta"+'\033[0m')

def help_cmd():
   
    print("help commands    : ")
    print("water            : waters plant manually")
    print("changemode1      : change to auto mode")
    print("changemode2      : change to manual mode")
    print("changemode3      : change to testmode")
    print("status           : update humidity level")
    print('============================================================================================================  ')

def check_valid_commands(value):
    cmd_arr= ["water", "changemode1","changemode2","changemode3","status"]
    for x in cmd_arr:
        if f"{value}".lower()== x:
            return True
    return False

def main():
    connected=True
    main_title()
    help_cmd()
    while(connected):
        print(">")
        value= input().encode()
        print(f"input was: {value.decode()}")
        
        if check_valid_commands(value.decode()):
            sock.sendto(value, (UDP_IP,UDP_Port))
            time.sleep(1)
            data, addr = sock.recvfrom(1024)
            print(f"Humidity {data.decode()} %")
        else:
            print("command doesn't exist")
            help_cmd()
            
        print("continue? n/y")
    
        connected= True if input().lower()=="y" else False
if __name__== "__main__":
    main()
    
    