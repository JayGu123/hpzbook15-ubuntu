#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__='Jay Gu'
import random
###########################################quick sort##############################################
def quick_sort(list):
	if len(list) > 2:
		pivot = list[0]
		less = []
		greater = []
		for i in list[1:]:
			print(i)
			if list[i] <= pivot:
				less.append(list[i])
			else:
				greater.append(list[i])
		return quick_sort(less)+pivot+quick_sort(greater)
	else:
		return list
		
def quick_sort1(list, low, high):
	if low < high:
		pivot = partition(list, low, high)
		quick_sort1(list, low, pivot)
		quick_sort1(list, pivot+1, high)
		
def partition(list, low, high):
	pivot = list[low]
	while low < high:
		while low < high and list[high] >= pivot:
			high += 1
		while low < high and list[high] < pivot:
			list[low] = list[high]
			low += 1
			list[high] = list[low]
	list[low] = pivot
	return low
########################################select sort###############################################
def find_smallest(list):
	smallest = list[0]
	smallest_index = 0
	for i in range(1, len(list)):
		if list(i) < smallest:
			smallest = list(i)
			smallest_index = i
	return smallest_index
	
def select_sort(list):
	new_list = []
	for i in list:
		index = find_smallest(list)
		new_list.append(list.pop(index))
	return new_list
list = [6,3,5,4,2,1]
print(select_sort(list))
#####################################狄克斯特拉算法###############################################
graph = {} #第一个散列表存储所有节点的关系以及他们的开销
costs = {} #第二个散列表存储所有从起点到其他节点的开销（若不是一层父->子的关系，那么均设置为无穷大）
parents = {} #第三个散列表存储素有的父子关系
processed = [] #这个数组存储所有的已经被处理过的节点
def find_lowest_cost_node(costs): #定义一个函数来找到整个开销中最小的节点
	lowest_node = None #初始化一个最小节点为空
	lowest_cost = float("inf") #初始化一个最小开销为无穷大
	for node in costs: #循环所有开销中的节点
		cost = costs[node] #取得这些节点的开销
		if cost < lowest_cost and lowest_node not in processed: #如果开销小于最小节点开销并且最小节点不在已处理过的数组中
			lowest_node = node #那么设置最小节点为该节点
			lowest_cost = cost #同时设置最小节点开销为该节点开销
	return lowest_node #返回一个最小节点

node = find_lowest_cost_node(costs) #首先取得一个最小开销节点
while node is not None: #循环直到节点不存在
	neighbors = graph[node]
	cost = costs[node]
	for n in neighbors.key():
		new_cost = cost + neighbors[n]
		if new_cost < costs[n]
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
