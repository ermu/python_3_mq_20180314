#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jianglin on 2018/3/12
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.2.4'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
print " [x] Sent 'Hello World'"
connection.close()