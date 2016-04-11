#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Rule'

__author__ = 'Sodablueblue'

class Rule(object):
	def __init__(self, type, criteria):
		self.criteria = criteria
		self.type = type

	def render(self):
		return self.type + ' ' + self._toHtml()

class Restriction(Rule):
	def __init__(self, type, criteria):
		super(Restriction, self).__init__(type, criteria)

	def _checkCriteria(self, value):
		pass

	def _toHtml(self):
		pass

	def check(self, values, bench = None):
		try:
			self._checkCriteria(values)
		except BaseException as e:
			raise BaseException('Restriction ', self.__class__.__name__, ': ', str(e))

class Combination(Rule):
	def __init__(self, type, criteria):
		super(Combination, self).__init__(type, criteria)

	def _checkbench(self, value, bench):
		pass

	def _toHtml(self):
		pass

	def check(self, values, bench):
		try:
			self._checkBench(values, bench)
		except BaseException as e:
			raise BaseException('Combination ', self.__class__.name__,': ', str(e))
