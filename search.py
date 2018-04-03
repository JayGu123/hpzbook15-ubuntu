#! /usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        func(*args, **kwargs)
        time2 = time.time()
        print('the runtime is:', time2-time1)
        return func
    return wrapper
############################################二分查找#########################################
@cal_time
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid+1
        else:
            high = mid-1
    return None


@cal_time
def stupid_search(list, item):
    index = 0
    for i in range(len(list)-1):
        if list[i] == item:
            index = i
    print(index)
########################################广度优先搜索#########################################
from collections import deque
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
def bf_search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print('this %s is mango seller' % person)
				return True
			else:
				searched.append(person)
				search_queue += graph([erson]
	return False

########################################
























