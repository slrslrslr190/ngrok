try:
	import os, wget, requests
except:
	os.system("pkg install wget -y ;pkg install figlet -y ;pkg install json -y ;pip2 install wget")
	pass
##
os.system("rm -rf ngrok.py ;rm -rf kali-binds ;rm -rf kali-fs ;rm -rf kali.sh ;rm -rf start-kali.sh")
##
wget.download("https://github.com/968hacker/ngrok/raw/main/ngrok")
##
os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
##
os.system("mv ngrok $HOME ;mv kali-binds $HOME ;mv kali-fs $HOME ;mv start-kali.sh $HOME ;cd $HOME ;chmod 777 ngrok ;chmod +x * ;./ngrok authtoken 1tYDfq1AlTEsMoyp5SMqFYtbU46_7w8vfHyH4rTxV7NdaotZe ;mv ngrok kali-fs ;cd kali-fs ;mv ngrok root ;cd $HOME")
##
os.system("clear ;clear ;clear ;figlet Ngrok")
print("==By===Lawa====Working==To===Root==&&==No=Root==\nType > ./ngrok http <port>\nOr\n./ngrok tcp <port>\n==============================================")
os.system("cd $HOME ;./start-kali.sh")

