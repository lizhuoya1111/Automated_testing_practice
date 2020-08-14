
import paramiko
import os
import sys
import subprocess
import re
import datetime
from time import sleep


def local_shell(cmds):
	"""
		cmds         要执行的命令字符串或者列表或元组
	"""
	shell = False
	if isinstance(cmds,(list, tuple)):
		shell = True
	cmds = isinstance(cmds, (list, tuple)) and '&&'.join(cmds) or cmds
	res = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=shell)
	sout ,serr = res.communicate()
	if serr:
		return serr
	return sout


class SSH(object):
	def __init__(self,server_ip=None,server_user=None,server_passwd=None,server_port=22,timeout=120):
		self.ssh = None

		if not all([server_ip,server_user,server_passwd]):
			raise '请给定IP,用户名,密码'

		self.timeout = timeout
		self.server_ip = server_ip
		self.server_user = server_user
		self.server_passwd = server_passwd
		self.server_port = server_port

	def connect(self):
		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(self.server_ip, self.server_port,self.server_user, self.server_passwd, timeout=self.timeout)
			self.ssh = ssh
		except:
			print('连接%s失败' % self.server_ip)
			exit(1)
		
	def close(self) -> object:
		if self.ssh:
			self.ssh.close()
		
	def execute(self, command) -> object:
		'''
		windows客户端远程执行linux服务器上命令
		command   执行的命令为字符串或列表、元组
		:rtype: object
		'''
		command = isinstance(command, (list, tuple)) and '&&'.join(command) or command
		stdin, stdout, stderr = self.ssh.exec_command(command)
		
		err = stderr.read()

		global out
		out = stdout.read().decode('utf-8')
		return out
		"""
		if "" != err:
			print("command: " + str(command) + " exec failed!\nERROR :" + str(err))
			return  err
		else:
			return out
		"""

	def ping_resault(self):

		if '100% packet loss' in out:
			return False
		elif "ttl" in out:
			return True
		else:
			return False


	def win_to_linux(self,localpath, remotepath,upload_type='file'):
		'''
		windows向linux服务器上传文件,上传目录下的文件夹远程自动创建﻿﻿
		localpath  为本地文件的绝对路径。如：D:\\test.py,上传目录如：D:\\test\\
		remotepath 为服务器端存放上传文件的绝对路径。如：/tmp/my_file.txt,上传目录，如：/tmp/aaa/
		upload_type  指定上传类型'file'为上传文件，'dir为上传文件夹'
		'''
		try:
			client = None
			if not localpath and not remotepath:
				raise '路径不能为空'
			client = paramiko.Transport((self.server_ip, self.server_port))
			client.connect(username = self.server_user, password = self.server_passwd)
			sftp = paramiko.SFTPClient.from_transport(client)

			print('upload file start %s ' % datetime.datetime.now())
			if upload_type == 'file':
				if ('.' not in localpath.split('\\')[-1]) or ('.' not in remotepath.split('/')[-1]):
					print('请指定正确的路径,且远程路径必须有路径中的文件夹')
					raise '请指定正确的路径,且远程路径必须有路径中的文件夹'
				sftp.put(localpath, remotepath)
			elif upload_type == 'dir':
				for root,dirs,files in os.walk(localpath):
					print('[%s][%s][%s]' % (root,dirs,files))
					for filespath in files:  
						local_file = os.path.join(root,filespath)  
						print(11,'[%s][%s][%s][%s]' % (root,filespath,local_file,localpath))
						a = local_file.replace(localpath,'').replace('\\','/').lstrip('/')  
						print(a,'[%s]' % remotepath)
						remote_file = os.path.join(remotepath,a)  
						print(remote_file) 
						try:  
							sftp.put(local_file,remote_file)  
						except Exception as e:  
							sftp.mkdir(os.path.split(remote_file)[0])  
							sftp.put(local_file,remote_file)  
							print("upload %s to remote %s" % (local_file,remote_file))
					for name in dirs:  
						local_path = os.path.join(root,name)  
						print(local_path,localpath)  
						a = local_path.replace(localpath,'').replace('\\','')  
						print(a)  
						print(remotepath)  
						remote_path = os.path.join(remotepath,a)  
						print(remote_path)  
						try:  
							sftp.mkdir(remote_path)  
							print("mkdir path %s" % remote_path)
						except Exception as e:  
							print(e)
			print('upload file %s ' % datetime.datetime.now())
		except Exception as e:
			print(e)
		finally:
			if client:
				client.close()

		
	def linux_to_win(self,localpath, remotepath):
		'''
		从linux服务器下载文件到本地
		localpath  为本地文件的绝对路径。如：D:\test.py
		remotepath 为服务器端存放上传文件的绝对路径,而不是一个目录。如：/tmp/my_file.txt
		'''
		try:
			client = None
			client = paramiko.Transport((self.server_ip, self.server_port))
			client.connect(username = self.server_user, password = self.server_passwd)
			sftp = paramiko.SFTPClient.from_transport(client)
		 
			sftp.get(remotepath, localpath)
		except Exception as e:
			print(e)
		finally:
			if client:
				client.close()


class DeviceSSH(object):
	# 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
	def __init__(self, ip, username, password, port=22,timeout=120):
		self.ip = ip
		self.username = username
		self.password = password
		self.timeout = timeout
		self.port = port
		self.client = None
		self.chan = None

		# 初始化连接
		self.connect()


	def connect(self):
		try:
			self.client = paramiko.Transport(sock=(self.ip, self.port))
			self.client.connect(username=self.username, password=self.password,timeout=self.timeout)
		except:
			print('连接%s失败' % self.ip)
			if not self.client:
				exit(1)

	# 调用该方法连接远程主机
	def session(self):
		"""
			连接回话
		"""
		try:
			self.chan = self.client.open_session()
			self.chan.settimeout(self.timeout)
			self.chan.get_pty()
			self.chan.invoke_shell()
		except Exception as err:
			print('%s会话建立失败' % self.ip)
			if self.chan:
				self.chan.close()

	# 断开连接
	def close(self):
		if self.client:
			self.client.close()


	# 发送要执行的命令
	def execute(self, cmd ,waitTime=2):
		u"""远程连接到客户端设备执行 shell 命令

		参数列表：
			cmd 要执行的命令字符串或者列表或元组

		返回：
			返回命令执行结果字符串

		实例：
			result = self.execute('en')
			result = self.execute(['en', 'show ver'])

		"""
		# 建立回话,如果连接成功，会话建立失败，则重新连接并建立会话
		if self.client and not self.chan:
			print('正在重新连接%s'%self.ip)
			self.connect()
		self.session()

		# 发送要执行的命令
		if isinstance(cmd, (list, tuple)):
			for m in cmd:
				m += '\n'
				self.chan.send(m)
		else:
			cmd += '\n'
			self.chan.send(cmd)
		# 回显很长的命令可能执行较久，睡眠取回回显
		sleep(waitTime)
		ret = self.chan.recv(65535)
		try:
			ret = ret
		except:
			try:
				ret = ret.decode('utf-8')
			except:
				ret = ret.decode('gbk')
		finally:
			self.chan.close()
		return ret


class Shell_SSH(object):

	def connect(self, hostip, name="admin", passwd="admin@139", po=22):
		ssh = paramiko.SSHClient()
		self.ssh_1 = ssh
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=str(hostip), port=int(po), username=str(name), password=str(passwd))
		self.ssh_con = ssh.invoke_shell()

		#return self.ssh_con

	def execute(self, cmd):

		self.ssh_con.send(cmd+"\n")

	def output(self):
		sleep(3)
		out = self.ssh_con.recv(3000)
		#print(out.decode('utf-8'))
		return out.decode('utf-8')

	def close(self):
		if self.ssh_1:
			sleep(1)
			self.ssh_1.close()

	# 默认0.1S一次，一共ping15次,用于linux
	def ping(self, ipadd, i=0.1, c=15):
		self.ssh_con.send("ping "+str(ipadd)+" -i "+str(i)+" -c "+str(c)+"\n")

	# 设备命令行的ping，默认ping5个
	def ping_cmd(self, ipadd, c=5):
		self.ssh_con.send("en" + "\n")
		self.ssh_con.send("ping "+str(ipadd)+" count "+str(c)+"\n")

"""---------------------------------------------------------"""

"""
# 远程linux/windows执行命令
# 连接主机
ssh = SSH('192.168.80.112','baomu','wyf@bm.',22) 
# ssh = SSH('192.168.80.112','baomu','wyf@bm.',22,timeout=5) # 设置连接超时时间
ssh.connect()
# 执行命令,单个命令用字符串,多个关联的命令通过列表或元组形式。执行一次execute相当于重新开一个终端
# result = ssh.execute('ls')#单条命令可直接采用字符串
result = ssh.execute(['cd Pherkad','ls','cd self_manage','ls'])
print result
# 关闭连接
ssh.close()
"""

"""
# windows向linux/windows服务器上传文件,传一个文件
ssh = SSH('192.168.80.111','baomu','wyf@bm.',22)
# 第一个为本地路径且必须为绝对路径且必须是文件名结尾，
# 第二个为远程路径，且必须为绝对路径，并且路径中的文件夹必须在远程上有此文件夹
ssh.win_to_linux('C:\\Users\\Administrator\\Desktop\\test\\demo.txt','/home/baomu/test/demo.txt')
"""

"""
# windows向linux/windows服务器上传文件,传一个目录
ssh = SSH('192.168.80.111','baomu','wyf@bm.',22)
# 第一个为本地路径且必须为绝对路径且必须是'\\'结尾，
# 第二个为远程路径，且必须为绝对路径，需以'/'结尾,upload_type指定为dir
ssh.win_to_linux('C:\\Users\\Administrator\\Desktop\\test\\','/home/baomu/test2/',upload_type='dir')
"""

"""
从linux/windwos服务器下载文件到本地
ssh = SSH('192.168.80.111','baomu','wyf@bm.',22)
ssh.linux_to_win('C:\\Users\\Administrator\\Desktop\\test\\demo.txt','/home/baomu/demo.txt')
"""


"""
# 执行本地命令
# 字符串执行一个命令，列表执行多个命令,local_shell
# 
result = local_shell(['cd test','ping 192.168.80.3'])
result = local_shell('ping 192.168.80.3')
print(result.decode('gbk'))

"""
'''
# 连接设备如使用SSH类不成功，就使用DeviceSSh,执行命令
host = DeviceSSH('10.2.2.81', 'admin', 'admin@139')
# host = DeviceSSH('10.2.2.51', 'admin', 'admin@139',timeout=5) # 设置连接超时时间
# 执行命令,执行单个直接用字符串，多个命令用列表。执行一次execute相当于重新开一个终端
result = host.execute(['en','show ver'])
print(result)
host.close()
'''

'''
ssh = SSH('10.1.1.212', 'root', 'root', 22)
ssh1 = SSH('10.1.1.212', 'root', 'root', 22)
ssh.connect()
ssh1.connect()

result21 = ssh.execute('tcpdump -i eth3')
print(result21)
result1 = ssh.execute('ping 21.1.1.3 -c 5')
print(result1)
result2 = ssh.execute('ls')
print(result2)
print(result21)

#ssh.close()
'''
'''
# SCG命令行连接，敲命令的方法
a = Shell_SSH()

a.connect("10.2.2.81")

a.execute("en")

a.execute("show ver")

a.execute("show ip add")

a.output()
'''