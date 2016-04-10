#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of DatetimeRule'

__author__ = 'Sodablueblue'

from Rule import *
import re

class DatetimeRule(Rule):

	def __init__(self):
		self.pattern = '^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}$'

	def check(self, value):
		if not re.match(self.pattern, str(value).strip()):
			raise BaseException('Date time format error')


if __name__ == '__main__':
	d = DatetimeRule()
	d.check('2015-2-4 10:03:23')