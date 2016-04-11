#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Pattern'

__author__ = 'Sodablueblue'

from Rule import *
import re

class Pattern(Restriction):

	def __init__(self, criteria):
		super(Pattern, self).__init__('String', criteria)

		if not 'pattern' in criteria:
			raise BaseException('Pattern Restriction: Params error')
		
		self.pattern = criteria['pattern']

	def _checkCriteria(self, value):
		if not re.match(self.pattern, value):
			raise BaseException('Pattern Restriction: String not match pattern')

	def _toHtml(self):
		return 'pattern = ' + self.pattern

if __name__ == '__main__':
	p = Pattern({'pattern' : '^[a-zA-Z0-9]+$'})
	p.check('abc')	
