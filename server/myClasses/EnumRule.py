#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of EnumRule'

__author__ = 'Sodablueblue'

from Rule import *

class EnumRule(Rule):
	def __init__(self, enums):
		self.enums = enums

	def check(self, value):
		if not value in self.enums:
			raise BaseException('String not in emuns')


if __name__ == '__main__':
	e = EnumRule(('red', 'blue', 'green'))
	e.check('yellow')