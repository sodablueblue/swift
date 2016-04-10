#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of DateRule'

__author__ = 'Sodablueblue'

from Rule import *
import re

class DateRule(Rule):

	def __init__(self):
		self.pattern = '^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$'

	def check(self, value):
		if not re.match(self.pattern, str(value)):
			raise BaseException('Date format error')


if __name__ == '__main__':
	d = DateRule()
	d.check('2013/12-1')