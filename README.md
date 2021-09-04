### Introduction
This project is a war-game with 3-tier architecture, client, server, database.
* Client: the view of user, using mouse and keyboard to play this game.
* Server: is used to control and monitor each game, win-or-lose, whether the user lose the connection.
* Databas: store maps's information.
> player information.(id, name, and so on.)
> map information.(map size, headquater location, land, water, mountain, forest, and so on).
> army.(army type, movement range, vision, and so on.)

### Technique
In client, mainly use pygame module to draw our game window, and socket module to connect server.
In server, mainly use socket module to build server and listening, and use sqlite3 to read/write database.
In database, use sqlite to simplify the process to build a mySQL server(or others), and reduce the error occurrence rate in database.