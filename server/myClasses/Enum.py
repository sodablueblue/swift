#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Enum'

__author__ = 'Sodablueblue'

from Rule import *

class Enum(Restriction):
	def __init__(self, criteria):
		super(Enum, self).__init__('String', criteria)

		if not 'enums' in criteria:
			raise BaseException('Enum Restriction: Params error')
		
		self.enums = criteria['enums']

	def _checkCriteria(self, value):
		if not value in self.enums:
			raise BaseException('Enum Restriction: String not in emuns')

	def _toHtml(self):
		resVal = 'enums: ('
		for enum in self.enums:
			resVal += enum + ', '
		resVal = resVal[: -2:] + ')'
		return resVal

if __name__ == '__main__':
	e = Enum({'enums': ('red', 'blue', 'green')})
	e.check('red')
	print(e._toHtml())