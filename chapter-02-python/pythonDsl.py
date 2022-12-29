#!/usr/bin/env python

import sys
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Consumer, OFFSET_BEGINNING

conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }


if __name__ == '__main__':
    
    # Create the consumer object. 
    consumer = Consumer(conf)

    # Tell the consumer to look for the users topic.
    topic = "users"
    consumer.subscribe([topic])
    print(f"Beginning to listen for the {topic} topic.")
    try:
        # Run until the user hits CTRL+C
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            # If there is an error, print out the error.
            elif msg.error():
                print(f"ERROR: {msg.error()}")
            else:
                # Get the name of the user
                name = msg.value().decode('utf-8')
                # Get the partition topic.
                topic = msg.topic()
                print(f"TOPIC: {topic}\nHello, {name}!")
    # On exit...
    except KeyboardInterrupt:
        pass
    # Close the consumer.
    finally:
        consumer.close()
