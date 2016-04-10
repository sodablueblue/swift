#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of LengthRule'

__author__ = 'Sodablueblue'

from Rule import *

class LengthRule(Rule):

	def __init__(self, minLength, maxLength):
		self.minLength = minLength
		self.maxLength = maxLength

	def check(self, value):
		if len(value) < self.minLength or len(value) > self.maxLength:
			raise BaseException('String out of range')


if __name__ == '__main__':
	l = LengthRule(2, 5)
	l.check('abcdef')