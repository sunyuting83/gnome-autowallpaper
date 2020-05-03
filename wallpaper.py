# -*- coding: utf-8 -*-
import os
import sys
import time

class SetWallpaper:
	"""docstring for ClassName"""
	def __init__(self, rootdir, sleep):
		self.rootdir = rootdir
		self.sleep = sleep
		self.start()

	def getWallpaper(self):
		rootdir = self.rootdir
		lists = os.listdir(rootdir) #列出文件夹下所有的目录与文件
		pypath = os.path.split( os.path.realpath( sys.argv[0] ) )[0] # .py程序所在目录
		self.lastpath = os.path.join(pypath,'last') # 检测最后一张
		last = 0
		with open(self.lastpath, "r") as fo:
			last = int(fo.read())

		# print(len(lists))
		if last == len(lists) - 1:
			last = 0
		lists.sort()
		for i in range(int(last),len(lists)):
		# for i in range(0,3):
			path = os.path.join(rootdir,lists[i])
			root, ext = os.path.splitext(path)
			if os.path.isfile(path) and ext.lower() == '.jpg' or '.png' or '.jpep':
				self.index = i
				yield path

	def start(self):
		wals = self.getWallpaper()
		sleep = self.sleep
		while True:
			try:
				os.system('gsettings set org.gnome.desktop.background picture-uri "%s"' % ( next(wals) ) )
				with open(self.lastpath, "w+") as fo:
					fo.write(str(self.index))
				time.sleep(sleep)
			except StopIteration:
				SetWallpaper(self.rootdir, self.sleep)
			except Exception as e:
				print(e)
				pass
				sys.close()


if __name__ == '__main__':
	SetWallpaper('/home/sun/图片/wallpaper',300)
