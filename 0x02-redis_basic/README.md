# 0x02. Redis basic

## Learning Objectives

1. Learn how to use redis for basic operations
2. Learn how to use redis as a simple cache

## Install Redis on Ubuntu 18.04
	sudo apt-get -y install redis-server
	pip3 install redis
	sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
