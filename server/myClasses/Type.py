#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Type'

__author__ = 'Sodablueblue'

from Rule import Restriction
from Rule import Combination
from common import _SIMPLE, _COMPLEX

class Type(object):
	def __init__(self, name, rule):
		self.name = name
		self.rule = rule
		if isinstance(self.rule, Restriction):
			self.simOrCom = _SIMPLE
		elif isinstance(self.rule, Combination):
			self.simOrCom = _COMPLEX
		else:
			raise BaseException('Type ' + self.name + ': rule isn\'t a instance of Type. It\'s ' + self.rule.__class__.__name__)

	def inflat(self):
		if self.simOrCom == _COMPLEX and len(self.children) > 0:
			resArr = list()
			for child in self.rule.criteria:
				maxv = 'maxOccurs' in child if child.maxOccurs else 1
				minv = 'minOccurs' in child if child.minOccurs else 1
				try:
					resArr.append = Element(child.name, child.type, maxv, minv)
				except BaseException as e:
					raise BaseException('Type ', self.name, ' -> ', str(e))
			self.children = resArr
			return self.children
		else:
			return None


	def render(self):
		return '<tr><td>' + self.name + '</td><td>' + self.rule.name + '</td><td>' + self.rule.render + '</td></tr>'

	def check(self, values):
		try:
			self.rule.check(values, children)

		except BaseException as e:
			raise BaseException('Type ', self.name, ' -> ', str(e))

	def encode(self):
		pass

# if __name__ == '__main__':
# 	t = Type('name', Restriction())
# 	print(t.simOrCom)