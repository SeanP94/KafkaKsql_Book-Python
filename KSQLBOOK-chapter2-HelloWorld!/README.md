Initialize the Kafka instance by
docker compose up -d

----------------------------------------------------------------------------
Producer:

Once launched, access the terminal, and you can start creating users by:
kafka-console-producer --boostrap-server localhost:9092 --topic users

And you can type in names.
----------------------------------------------------------------------------
Consumer:

In a seperate console, you need to make the python file runnable:
chmod u+v pythonDsl.py
Then,

./pythonDsl.py
Then this will begin to listen for the users.
----------------------------------------------------------------------------
Inside the Kafka instance, just type in names. Inside the python as you type in names, like Seanep94
You'll see
TOPIC: Users
Hello, Seanep94!