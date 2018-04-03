#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__='Jay Gu'


station_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'az', 'ca'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
final_station = set()

while station_needed:
	best_station = None
	states_covered = set()
	for station, states_for_stations in stations.items():
		covered = states_for_stations & station_needed
		if len(covered) > len(states_covered):
			states_covered = covered
			best_station = station
	final_station.add(best_station)
	station_needed -= states_covered
	
print(final_station)
