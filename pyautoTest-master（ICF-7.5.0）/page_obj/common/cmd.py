import subprocess
import time


class CMD(object):

	def ping(self, ip, parm1="-l", size="32"):

		windows_cmd = subprocess.Popen(["ping.exe", str(parm1), str(size), str(ip)],
		                     stdin=subprocess.PIPE,
		                     stdout=subprocess.PIPE,
		                     stderr=subprocess.PIPE,
		                     shell=True)

		out = windows_cmd.stdout.read()
		sss = out.decode('gbk')
		return sss



	def input(self,input1):

		windows_cmd = subprocess.Popen([str(input1)],
		                               stdin=subprocess.PIPE,
		                               stdout=subprocess.PIPE,
		                               stderr=subprocess.PIPE,
		                               shell=True)
		time.sleep(3)
		out = windows_cmd.stdout.read()
		sss = out.decode('gbk')

		err = windows_cmd.stderr.read()

		err1 = err.decode('gbk')
		print(err)
		print(err1)
		return sss
