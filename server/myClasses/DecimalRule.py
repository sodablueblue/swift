#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for DecimalRule'

__author__ = 'Sodablueblue'

from Rule import *

class DecimalRule(Rule):
	def __init__(self, fractionDigits, totalDigits, minInclusive = -float('Inf')):
		self.fractionDigits = fractionDigits
		self.totalDigits = totalDigits
		self.minInclusive = minInclusive

	def check(self, value):
		if value < self.minInclusive:
			raise BaseException('Decimal less than minInclusive')

		else:
			strVal = str(value)
			if '-' in strVal:
				strVal = strVal.replace('-', '')

			if '.' in strVal:
				if self.totalDigits != len(strVal) - 1 or self.fractionDigits != len(strVal[strVal.index('.')]):
					raise BaseException('Deciaml not corret digits')
			else:
				if self.fractionDigits != 0 or self.totalDigits != len(strVal):
					raise BaseException('Decial not correct digits')


if __name__ == '__main__':
	try:
		# d = DecimalRule(1, 4)
		# d.check(123.4)
		# d.check(12)
		# d.check(12.4)

		e = DecimalRule(1, 3, -9)
		# e.check(-10)
	except BaseException as e:
		print(e)