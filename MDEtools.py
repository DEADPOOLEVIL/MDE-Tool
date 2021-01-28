import os
import time
import sys

def menu():
    os.system('clear')

    print("#" * 80)
    print(" Welcome ".center(80, '#'))
    print(" This Script Made By MDE ".center(80, '#'))
    print(" For Contact https://github.com/DEADPOOLEVIL ".center(80, '#'))
    print("#" * 80)
    print("\n")
    print("Loading..")

    animation = ("|/-\\")

    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("Loading Complete!")
    
    time.sleep(2)
    os.system('clear')

    print("#" * 80)
    print("01- For Install All Command ")
    print("02- For Famous Tools (Soon)")
    print("03- For Help")
    print("99- For Exit")
    print("#" * 80)

loop = True
while  loop:
    menu()
    
    mdechoseone = int(input("MDE:---#> ")).strip()

    if mdechoseone == 1 or mdechoseone == "01" :
        print("Ok!")
        print("Loading..")
        
        animation = ("|/-\\")
        
        for i in range(100):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("Loading Complete!")
        time.sleep(2)
        os.system('clear')
        yesorno = input("Do You Wanna Contino Y/N").lower().strip()

        if yesorno == 'y' or yesorno == 'yes':
            os.system("termux-setup-storage -y")
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install python -y")
            os.system("apt-get install python2 -y")
            os.system("apt-get install python3 -y")
            os.system("apt-get install ruby -y")
            os.system("apt-get install git -y")
            os.system("apt-get install php -y")
            os.system("apt-get install nano -y")
            os.system("apt-get install nmap -y")
            os.system("apt-get install perl -y")
            os.system("apt-get install golang -y")
            os.system("apt-get install host -y")
            os.system("apt-get install havij -y")
            os.system("apt-get install hydra -y")
            os.system("apt install wireshark -y")
            os.system("apt-get install cmatrix -y")
            os.system("apr-get install figlet -y")
            os.system("apt-get install wget -y")
            os.system("apt-get install wget -y")
            os.system("apt-get install python2 -y")
            os.system("apt-geg install python2-dev -y")
            os.system("apt install wireshark -y")
            os.system("apt-get install cowsay -y")
            os.system("apt-get install toilet -y")
            os.system("apt-get install curlinstall wgetrc -y")
            os.system("apt-get install ruby -y")
            os.system("apt-get install help -y")
            os.system("apt-get install net-tools -y")
            os.system("apt-get install w3m -y")
            os.system("apt-get install unrar -y ")
            os.system("apt-get install curl -y ")
            os.system("pkg install curl -y ")
            os.system("apt-get install clang -y")
            os.system("apt-get install openssh -y")
            os.system("apt-get install tor -y")
            os.system("apt-get install tar -y")
            os.system("apt-get install zip -y")
            os.system("apt-get install proot -y")
            os.system("pip2 install wget -y")
            os.system("pip2 install requests -y")
            os.system("gem install lolcat -y")
            os.system("pip install bundle -y ")
            os.system("apt-get install gcc -y ")        
            os.system("apt update -y && apt upgrade -y")

            print("Complite.!!")
            print("See You Next Time")
            time.sleep(3)
            os.system('clear')

        elif yesorno == 'n' or yesorno == 'no':
            print("Ok Try Again")
            menu()

    elif mdechoseone == 2 or mdechoseone == '02' :
        os.system('clear')
        print("#" * 80)
        print("Its Comeing Soon")
        print("99- Back To Menu")
        print("#" * 80)

        mdechoseonethree = int(input("MDE:---#> ").strip())
        
        if mdechoseonetwo == "99":
            menu()
            
        else:
            menu()

    elif mdechoseone == 3 or mdechoseone == "03" :
        os.system('clear')
        print("#" * 80)
        print("01- For Install All Command ")
        print("02- For Famous Tools (Soon)")
        print("03- For Help")
        print("99- For Exit")
        print("#" * 80)

        mdechoseonetwo = int(input("MDE:---#> ").strip())
        
        if mdechoseonetwo == "99":
            menu()
            
        else:
            menu()
            
    elif mdechoseone == 4 or mdechoseone == "04" :

        yesornotwo = input("Do You Wanna Contino Y/N").lower().strip()

        if yesornotwo == 'y' or yesornotwo == 'yes' :
            os.system('clear')
            os.system('pkg install git')
            os.system('git clone https://github.com/DEADPOOLEVIL/MDE-Tool.git')

        elif yesornotwo == 'n' or yesornotwo == 'no' :
            print("Ok Try Again")
            time.sleep(2)
            menu()

    elif mdechoseone == 99 :
        os.system('clear')
        print("Dont Forget Us:>")
        print("Bye")
        time.sleep(2)
        break
