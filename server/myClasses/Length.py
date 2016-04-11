#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Length'

__author__ = 'Sodablueblue'

from Rule import *

class Length(Restriction):

	def __init__(self, criteria):
		super(Length, self).__init__('String', criteria)

		if not 'minLength' in criteria or not 'maxLength' in criteria:
			raise BaseException('Length Restriction: Params error')
		
		self.minLength = criteria['minLength']
		self.maxLength = criteria['maxLength']

	def _checkCriteria(self, value):
		if len(value) < self.minLength or len(value) > self.maxLength:
			raise BaseException('Length Restriction: String out of range')

	def _toHtml(self):
		return 'minLength = ' + self.minLength + ', maxLength = ' + self.maxLength

if __name__ == '__main__':
	l = Length({'minLength' : 2, 'maxLength' : 5})
	l.check('abcde')