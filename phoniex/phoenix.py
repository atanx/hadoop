#!/usr/bin/env python
#coding=utf-8

import phoenixdb
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

database_url = 'http://localhost:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)
cursor = conn.cursor()


def get_cmd_type(cmd):
	if len(cmd.strip()) == 0 or cmd.startswith('!'):
		return 'invalid_cmd'
	kw = cmd.split()[0].upper()
	if kw in ('SELECT','SHOW'):
		return "data_cmd"
	else:
		return "no_data_cmd"


def execute_sql(cmd):
	cmd_type= get_cmd_type(cmd)
	if cmd_type == "data_cmd":
		cursor.execute(cmd)
		data = cursor.fetchall()
		for row in data:
			for idx, item in enumerate(row):
				sys.stdout.write(str(item))
				if idx < len(row)-1:
					sys.stdout.write('\t')
			sys.stdout.write('\n')
	elif cmd_type == "no_data_cmd":
		cursor.execute(cmd)
	else:
		pass


def execute_sqlfile(sqlfile):
	content = open(sqlfile).read()
	cmds = [ i.strip() for i in content.split(';')]
	for cmd in cmds:
		execute_sql(cmd)


if __name__ == '__main__':
	
	if len(sys.argv)==2:
		if os.path.exists(sys.argv[1]):
			execute_sqlfile(sys.argv[1])
		else:
			cmd = sys.argv[1]
			execute_sql(cmd)
	else:
		raise SyntaxError(u"语法错误，未指定SQL文件")
	
