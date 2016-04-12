#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Date'

__author__ = 'Sodablueblue'

from Rule import *
import re

class Date(Restriction):

	def __init__(self, criteria = None):
		super(Date, self).__init__('Date', criteria)
		self.pattern = '^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$'

	def _checkCriteria(self, value):
		if not re.match(self.pattern, str(value)):
			raise BaseException('Format error \'Element.' + value + '\'')

	def _toHtml(self):
		return ''

if __name__ == '__main__':
	try:
		d = Date()

		print(d.render())
		
		d.check('2013.12-1')
	except BaseException as e:
		print(e)