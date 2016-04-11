#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Datetime'

__author__ = 'Sodablueblue'

from Rule import *
import re

class Datetime(Restriction):

	def __init__(self, criteria = None):
		super(Datetime, self).__init__('Datetime', criteria)
		self.pattern = '^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}$'

	def _checkCriteria(self, value):
		if not re.match(self.pattern, str(value).strip()):
			raise BaseException('Datetime Restriction: Datetime format error')


if __name__ == '__main__':
	d = Datetime()
	d.check('2015-2-4 10:03:23')