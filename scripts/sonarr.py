import os
import sqlite3

file_name = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+"/file.txt"

f = open(file_name, 'w')
f.write(str(os.environ.get('sonarr_episodefile_path')))