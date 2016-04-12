#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Choice'

__author__ = 'Sodablueblue'

from Rule import *

class Choice(Combination):

	def __init__(self, criteria):
		super(Choice, self).__init__('Choice', criteria)

	def _checkCriteria(self, values):
		if len(values) > 1:
			raise BaseException('Data more than one')

		if not values[0].name in tuple(v['name'] for v in self.criteria):
			raise BaseException('Invalid data \'Element.' + values[0].name + '\'')

	def _toHtml(self):
		resVal = '('
		for cri in self.criteria:
			resVal += cri['name'] + ', '
		return resVal[:-2:] + ')'



if __name__ == '__main__':
	from Element import *
	from Type import *

	try:
		c = Choice(
			[
				{'name': "AnyBIC", 'type':"AnyBICIdentifier"},
	            {'name':"PrtryId",'type':"GenericIdentification29"},
	            {'name':"NmAndAdr", 'type':"NameAndAddress6"}
	        ])
		print(c.render())

		c.check(
			[ 
				Element('AnyBIC', Type('test', c))
			])
	except BaseException as e:
		print(e)