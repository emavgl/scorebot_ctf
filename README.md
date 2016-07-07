#scorebot_ctf
This is a simple sketch of a scorebot for Attack-Defense CTF in python.
It has been tested using two services (textfilestore, tweety_bird) from iCTF 2015.

##Configuration
```python
if __name__ == '__main__':
	teams = {'team1': Team('team1', "192.168.56.101"), 'team2': ... }
	services = {'tweety_bird': Service('tweety_bird', '20118'), 'textfilestore': Service('textfilestore', '20093')}
	game = Game(teams, services)
	...
```
The configuration has to be set in the main function.
You have to initialize the dictionary *teams* which contains for each team an object of type *Team(name, ip)*.
Every team has a name and an IP that the scorebot use to test the services.
Then you have to initialize the dictionary *service* with objects of type *Service(name, port)*.

###Services
Each service must have a directory inside the directory **./services** that contains the file **setflag.py** and **getflag.py** used by the scorebot to set a new flag into the service and gets it back. The set_flag script returns to the main script a *flag_id* and a *token*. The get_flag script returns a flag given a flag_id and a token.

##Flask server
There is also a simple HTTP server that lets the teams submit flags, get flagIDs and view the scores.

```python
@app.route("/")
def hello():
	res = ""
	for team_name, team in teams.iteritems():
		res += "Name: {0}</br>Def Pnt: {1}</br>Att Pnt: {2}</br></br>".format(team_name, team.def_score, team.att_score)
	return res

@app.route('/submit', methods=['POST'])
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
```
