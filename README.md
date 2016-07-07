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
