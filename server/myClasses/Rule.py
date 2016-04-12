#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Rule'

__author__ = 'Sodablueblue'

Rules = (
	'Choice',
	'Sequence',
	'SimpleContent',
	'Decimal',
	'Enum',
	'Pattern',
	'Length',
	'Date',
	'Datetime')

class Rule(object):
	def __init__(self, type, criteria):
		self.criteria = criteria
		self.type = type

	def render(self):
		return self.type + self._toHtml()

	'''
	@param res in (Choice, Sequence, SimpleContent, Decimal, Enum,
		Pattern, Length, Date, Datetime)
	'''
	@staticmethod
	def factory(res, criteria):
		res = str(res).title()

		if not res in Rules:
			raise BaseException('Rule: No rule named ' + res)

		module = __import__(res)
		cls = getattr(module, res)
		return cls(criteria)

class Restriction(Rule):
	def __init__(self, type, criteria):
		super(Restriction, self).__init__(type, criteria)

	def _checkCriteria(self, value):
		pass

	def _toHtml(self):
		pass

	def check(self, values):
		try:
			self._checkCriteria(values)
		except BaseException as e:
			raise BaseException('Restriction ' + self.__class__.__name__ + ': ' + str(e))

class Combination(Rule):
	def __init__(self, type, criteria):
		super(Combination, self).__init__(type, criteria)

	def _checkCriteria(self, value):
		pass

	def _toHtml(self):
		pass

	def check(self, values):
		try:
			self._checkCriteria(values)
		except BaseException as e:
			raise BaseException('Combination ' + self.__class__.__name__ + ': ' + str(e))

if __name__ == '__main__':
	try:
		r = Rule.factory('decimal', {'fractionDigits': 1, 'totalDigits': 3, 'minInclusive': -9})

		c = Rule.factory('Sequence', [
				{'name': "AnyBIC", 'type':"AnyBICIdentifier", 'maxOccurs' : 2, 'minOccurs': 1},
	            {'name':"PrtryId",'type':"GenericIdentification29", 'minOccurs': 0},
	            {'name':"NmAndAdr", 'type':"NameAndAddress6", 'maxOccurs': 2, 'minOccurs' : 0}
	        ])
		print(r.render())
		print(c.render())
	except BaseException as e:
		print(e)