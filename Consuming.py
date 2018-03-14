#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jianglin on 2018/3/12
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.2.4'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
channel.start_consuming()

