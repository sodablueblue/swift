#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Enum'

__author__ = 'Sodablueblue'

from Rule import *

class Enum(Restriction):
	def __init__(self, criteria):
		super(Enum, self).__init__('String Enum', criteria)

		if not 'enums' in criteria:
			raise BaseException('Params error')
		
		self.enums = criteria['enums']

	def _checkCriteria(self, value):
		if not value in self.enums:
			raise BaseException('Not in emuns \'Elment.' + value + '\'')

	def _toHtml(self):
		resVal = '('
		for enum in self.enums:
			resVal += enum + ', '
		resVal = resVal[: -2:] + ')'
		return resVal


if __name__ == '__main__':
	try:
		e = Enum({'enums': ('red', 'blue', 'green')})
		print(e.render())
		e.check('r')
	except BaseException as e:
		print(e)