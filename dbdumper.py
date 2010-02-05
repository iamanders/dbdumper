#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class dumper:
	"""Class for dumping mysql databases"""
	
	def __init__(self, username, password, path):
		self.username = username
		self.password = password
		self.path = path


	def the_magic(self, dbname):
		os.system("mysqldump -u %s --password=%s %s > %s%s.sql" % (self.username, self.password, dbname, self.path, dbname))




if __name__ == '__main__':
	to_dump = ['db1', 'db2']
	to_path = '/path/for/dumps/'
	db_username = 'username'
	db_password = 'password'
	
	d = dumper(db_username, db_password, to_path)
	
	for db in to_dump:
		try:
			d.the_magic(db)
		except:
			print 'FAIL'