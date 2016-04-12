#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Length'

__author__ = 'Sodablueblue'

from Rule import *

class Length(Restriction):

	def __init__(self, criteria):
		super(Length, self).__init__('String Length', criteria)

		if not 'minLength' in criteria or not 'maxLength' in criteria:
			raise BaseException('Params error')
		
		self.minLength = criteria['minLength']
		self.maxLength = criteria['maxLength']

	def _checkCriteria(self, value):
		if len(value) < self.minLength or len(value) > self.maxLength:
			raise BaseException('Out of range \'Element.' + value + '\'')

	def _toHtml(self):
		return '(minLength=' + str(self.minLength) + ', maxLength=' + str(self.maxLength) + ')'

if __name__ == '__main__':
	try:
		l = Length({'minLength' : 2, 'maxLength' : 5})
		print(l.render())
		l.check('abccccde')
	except BaseException as e:
		print(e)