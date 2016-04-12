#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Pattern'

__author__ = 'Sodablueblue'

from Rule import *
import re

class Pattern(Restriction):

	def __init__(self, criteria):
		super(Pattern, self).__init__('String Pattern', criteria)

		if not 'pattern' in criteria:
			raise BaseException('Params error \'Element.' + value + '\'')
		
		self.pattern = criteria['pattern']

	def _checkCriteria(self, value):
		if not re.match(self.pattern, value):
			raise BaseException('Not match pattern \'Element.' + value + '\'')

	def _toHtml(self):
		return '(pattern=/' + self.pattern + '/)'

if __name__ == '__main__':
	try:
		p = Pattern({'pattern' : '^[a-zA-Z0-9]+$'})
		print(p.render())
		p.check('abccc---')	
	except BaseException as e:
		print(e)	
