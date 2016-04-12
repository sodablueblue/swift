#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Sequence'

__author__ = 'Sodablueblue'

from Rule import *

class Sequence(Combination):

	def __init__(self, criteria):
		super(Sequence, self).__init__('Sequence', criteria)

	def _checkCriteria(self, values):
		length, listVal = len(values), list()
		for index, val in enumerate(values):
			name = val.name
			count = 1

			if index < length - 1 and val.name == values[index + 1].name:
				count += 1
				continue
			else:
				listVal.append({'name': name, 'occurs': count})

		if len(listVal) > len(self.criteria):
			raise BaseException('Invalid data \'Element.' + listVal[len(listVal) - 1]['name'] + '\'')

		for index, cri in enumerate(self.criteria):
			if listVal[index]['name'] != cri['name']:
				raise BaseException('Invalid data \'Element.' + listVal[index]['name'] + '\'')
			if listVal[index]['occurs'] < (cri['minOccurs'] if 'minOccurs' in cri else 1) or listVal[index]['occurs'] > (cri['maxOccurs'] if 'maxOccurs' in cri else 1):
				raise BaseException('Invalid data \'Element.' + listVal[i]['name'] + '\'')
				
	def _toHtml(self):
		resVal = '('
		for cri in self.criteria:
			max = cri['maxOccurs'] if 'maxOccurs' in cri else 1
			min = cri['minOccurs'] if 'minOccurs' in cri else 1
			resVal += cri['name'] + '{' + str(max) + '~' + str(min) + '}, '
		return resVal[:-2:] + ')'


if __name__ == '__main__':
	from Element import *
	from Type import *

	try:
		c = Sequence(
			[
				{'name': "AnyBIC", 'type':"AnyBICIdentifier", 'maxOccurs' : 2, 'minOccurs': 1},
	            {'name':"PrtryId",'type':"GenericIdentification29", 'minOccurs': 0},
	            {'name':"NmAndAdr", 'type':"NameAndAddress6", 'maxOccurs': 2, 'minOccurs' : 0}
	        ])
		print(c.render())

		c.check(
			[ 
				Element('AnyBIC', Type('test', c)),
				# Element('AnyBIC', Type('test', c)),
				Element('PrtryId', Type('test', c)),
				Element('NmAndAdr', Type('test', c)),
				Element('NmAndAdr', Type('test', c)),
				Element('AnyBIC', Type('test', c))
			])
	except BaseException as e:
		print(e)