### Introduction
This project is war-game with 3-tier architecture, client, server, database.
* Client: the view of user, using mouse and keyboard to play this game.
* Server: is used to control and monitor each game, win-or-lose, whether the user lose the connection.
* Databas: store maps's information.

### Technique
In client, mainly use pygame module to draw our game window, and socket module to connect server.  
In server, mainly use socket module to build server and listening, and use sqlite3 to read/write database.  
In database, use sqlite to simplify the process to build a mySQL server(or others), and reduce the error occurrence rate in database.  

### How to start?  
1. start the server  
> check ip config, and re-write ip address of config.py as yours  
> check the path is C:\......\War-Game\src (in the "src" directory)  
``` cli=
python Server.py  
```
  
2. start the client  
> check the path is C:\......\War-Game\src (in the "src" directory)  
``` cli=  
python GUI.py  
```  
  
3. client chooses user account  
> input user name or create a new account  
  
4. client chooses what to do in the next  
> * new game: to create/join a game room  
> * Back: to change other account  
> * Control: to see the rule of this game  
> * Ranking: to see your rank  
  
5. chose "new game", waiting another player join the room  
  
6. enjoy this game  
  
  
  
  
  
This project got the prize of "深碗專題競賽".  
Thanks for the contribution of each person in this project team.  