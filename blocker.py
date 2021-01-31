from pathlib import Path
from shutil import copy
import sys
try:
	from win10toast import ToastNotifier
	toaster = ToastNotifier()
except:
	toaster = False

APP_NAME = 'Website Blocker'
REDIRECT = '127.0.0.1'
WIN_PATH = r'C:\Windows\System32\drivers\etc'
ICON_PATH = 'icon.ico'

host_path = Path(WIN_PATH)
host_file = host_path/'hosts'
host_file_copy = host_path/'hosts.original'
host_file_blocked = host_path/'hosts.blocked'

class Blocker():
	def __init__(self, redirect=REDIRECT):
		self.redirect = redirect
		with open('blocklist.txt') as file:
			self.blocked = [line.rstrip() for line in file]
		if not host_file_copy.exists():
			self._setup()
		self._create_blocked_list()

	def _setup(self):
		# Create copy of hosts file
		try:
			copy(host_file, host_file_copy)
			print("Copy of hosts file created")
		except PermissionError:
			self._raise_permission_error()

	def _create_blocked_list(self):
		try:
			copy(host_file_copy, host_file_blocked)
			with open(host_file_blocked, "a") as blocked_file:
				for url in self.blocked:
					# TODO: refine, add www only if not in url
					blocked_file.write(f"{self.redirect} {url}\n")
					blocked_file.write(f"{self.redirect} www.{url}\n")
				print("hosts.blocked created")
		except PermissionError:
			self._raise_permission_error()

	def block(self):
		try:
			copy(host_file_blocked, host_file)
			print("Hosts file replaced with hosts.blocked")
			return True
		except PermissionError:
			self._raise_permission_error()
			return False

	def unblock(self):
		try:
			copy(host_file_copy, host_file)
			print("Hosts file replaced with hosts.original")
			return True
		except PermissionError:
			self._raise_permission_error()
			return False

	def notify(self, message, title=APP_NAME):
		print(message)
		if toaster:
			toaster.show_toast(title, message, duration=5) # icon_path=ICON_PATH, 

	def _raise_permission_error(self):
		self.notify("Permission Error. Please run the command line tool as ADMINISTRATOR.")

if __name__=='__main__':
	blocker = Blocker()
	try: mode = sys.argv[1]
	except: mode = 'block' 

	if mode == 'unblock':
		if blocker.unblock():
			blocker.notify("Websites unblocked, have fun")
	else:
		if blocker.block():
			blocker.notify("Websites blocked, enjoy your work")

