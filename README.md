# Discord Ping bot
This is a server-client solution for a client to send a message to the server
to ping/dm a user. this can be used to get messages when a user is inside the game
after standing in a queue.

## Client
Requirements:
 - Python 3.9
 - https://github.com/drov0/python-imagesearch

How to run:
 - choose a picture of the queue. example picture in repository.
 - change server ip, port.
 - `python client.py`

## Server
Requirements:
 - Python 3.9
 - Flask

How to run:
 - create a `.env` file.
 - add environment variables HOST_NAME, PORT_NUMBER, CHANNEL_ID, BOT_TOKEN
 - `python server.py`