#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Rule'

__author__ = 'Sodablueblue'

class Rule(object):
	pass

class Restriction(Rule):
	def __init__(self, type, criteria):
		self.criteria = criteria
		self.type = type

	def _checkCriteria(self, value):
		pass

	def check(self, values, bench = None):
		try:
			self._checkCriteria(values)
		except BaseException(e):
			raise BaseException('Restriction ', self.__class__.__name__, ': ', e)

class Combination(Rule):
	def __init__(self, type, criteria):
		self.criteria = criteria
		self.type = type

	def _checkCriteria(self, value):
		pass

	def _checkbench(self, value, bench):
		pass

	def check(self, values, bench):
		try:
			self._checkCriteria(values)
			self._checkBench(values, bench)
		except BaseException(e):
			raise BaseException('Combination ', self.__class__.name__.': ', e)
