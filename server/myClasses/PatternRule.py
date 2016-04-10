#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of PatternRule'

__author__ = 'Sodablueblue'

from Rule import *
import re

class PatternRule(Rule):

	def __init__(self, pattern):
		self.pattern = pattern

	def check(self, value):
		if not re.match(self.pattern, value):
			raise BaseException('String not match pattern')


if __name__ == '__main__':
	p = PatternRule('^[a-zA-Z0-9]+$')
	p.check('abc*')	
