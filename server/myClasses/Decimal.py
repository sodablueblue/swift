#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Decimal'

__author__ = 'Sodablueblue'

from Rule import *

class Decimal(Restriction):
	def __init__(self, criteria):
		super(Decimal, self).__init__('Decimal', criteria)

		if not 'fractionDigits' in criteria or not 'totalDigits' in criteria:
			raise BaseException('Decimal Restriction: Params error')
		
		self.fractionDigits = criteria['fractionDigits']
		self.totalDigits = criteria['totalDigits']
		self.minInclusive = 'minInclusive' in criteria if criteria['minInclusive'] else -float('Inf')

	def _checkCriteria(self, value):
		if value < self.minInclusive:
			raise BaseException('Decimal Restriction: Less than minInclusive')

		else:
			strVal = str(value)
			if '-' in strVal:
				strVal = strVal.replace('-', '')

			if '.' in strVal:
				if self.totalDigits != len(strVal) - 1 or self.fractionDigits != len(strVal[strVal.index('.')]):
					raise BaseException('Decimal Restriction: Incorret total digits')
			else:
				if self.fractionDigits != 0 or self.totalDigits != len(strVal):
					raise BaseException('Decimal Restriction: Incorrect fraction digits')

	def _toHtml(self):
		return 'fractionDigits = ' + self.fractionDigits + ', totalDigits = ' + self.totalDigits + ', minInclusive = ' + self.minInclusive


if __name__ == '__main__':
	try:
		# d = DecimalRule(1, 4)
		# d.check(123.4)
		# d.check(12)
		# d.check(12.4)

		d = Decimal({'fractionDigits': 1, 'totalDigits': 3, 'minInclusive': -9})
		d.check(-10)
	except BaseException as e:
		print(str(e))