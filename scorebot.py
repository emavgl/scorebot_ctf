import sys
import os
import subprocess
import ast
import time, threading
import random, string

from flask import Flask
from flask import request

app = Flask(__name__)

class Game:
	def __init__(self, teams, services):
		self.teams = teams
		self.services = services

	def getFlags(self):
		for service_name, service in services.iteritems():
			for team_name, team in teams.iteritems():
				tmp_flag = service.getFlag(team.host, team_name)
				if tmp_flag == service.flags[team.name]:
					print 'punto difesa per ' + team_name + " serice_name " + service_name
					team.updateDefScore()
					
	def setFlags(self):
		for service_name, service in services.iteritems():
			for team_name, team in teams.iteritems():
				service.setFlag(team.host, team_name)

	def getFlagID(self, service_name, evil_team):
		return self.services[service_name].args[evil_team].get('flag_id')
		
	
	def submitFlags(self, team_name, service_name, flag):
		teamx = self.teams[team_name]
		dic_flags = self.services[service_name].flags
		for user, user_flag in dic_flags.iteritems():
			if flag == user_flag: #and user != teamx.name:
				print 'punto attacco per ' + team_name
				teamx.updateAttScore()
				self.services[service_name].flags[user] = ""
				return "valid"
		return "invalid"

class Team:
	def __init__(self, name, host):
		self.name = name
		self.host = host
		self.att_score = 0
		self.def_score = 0

	def updateAttScore(self):
		self.att_score += 2

	def updateDefScore(self):
		self.def_score += 1

class Service:
   def __init__(self, name, port):
      self.name = name
      self.port = port
      self.path = "./services/" + name
      self.flags = {} #flag una per team
      self.args = {}

   def getFlagID(self, team_name):
   	  return (args[team_name]).get("flag_id", None)

   def setFlag(self, host, team_name):
   	  flag = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
   	  query = "{0}/set_flag.py".format(self.path)
   	  args = "{0} {1} {2}".format(host, self.port, flag)
	  proc = subprocess.Popen(['python', query,  args], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	  out, err = proc.communicate()
	  out = out.split('\n')
	  size = len(out)
	  out = out[size-2]
	  self.args[team_name] = ast.literal_eval(out)
   	  self.flags[team_name] = flag
 
   def getFlag(self, host, team_name):
   	  query = "{0}/get_flag.py".format(self.path)
   	  args = "{0} {1} {2} {3}".format(host, self.port, self.args[team_name]["flag_id"], self.args[team_name]["token"])
	  proc = subprocess.Popen(['python', query,  args], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	  out, err = proc.communicate()
	  out = out.split('\n')
	  size = len(out)
	  out = out[size-2]
	  print 'flag ottenuta: ' + str(out)
	  return str(out)

def routine():
	game.setFlags()
	game.getFlags()
	threading.Timer(10, routine).start()

@app.route("/")
def hello():
	res = ""
	for team_name, team in teams.iteritems():
		res += "Name: {0}</br>Def Pnt: {1}</br>Att Pnt: {2}</br></br>".format(team_name, team.def_score, team.att_score)
	return res

@app.route('/submit/', methods=['POST'])
def submitFlag():
	flag = request.form.get('flag', None)
	team_name = request.form.get('team', None)
	service_name = request.form.get('service', None)
	status = game.submitFlags(team_name, service_name, flag)
	return status

@app.route('/flagid', methods=['GET'])
def getFlagID():
	username = request.args.get('enemy_name')
	service_name = request.args.get('service')
	flagid = game.getFlagID(service_name, username)
	return str(flagid)

if __name__ == '__main__':
	teams = {'fried': Team('fried', "192.168.56.101") }
	services = {'tweety_bird': Service('tweety_bird', '20118'), 'textfilestore': Service('textfilestore', '20093')}
	game = Game(teams, services)
	routine()
	app.run()

