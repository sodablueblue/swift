#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Element'

__author__ = 'Sodablueblue'

from Type import *
from common import _SIMPLE, _COMPLEX

class Element(object):

	def __init__(self, name, type, maxOccurs = 1, minOccurs = 1):
		self.name = name
		self.type = type
		self.maxOccurs = maxOccurs
		self.minOccurs = minOccurs
		self.inflatReady = False
		self.valueReady = False

		if not isinstance(self.type, Type):
			raise BaseException('Element ', self.name, ': type isn\'t an instance of Type')

	def inflat(self):
		try:
			self.values = self.type.inflat()
			self.inflatReady = True
		except BaseException(e):
			self.inflatReady = False
			raise BaseException('Element ', self.name, ' -> ' + e)

	def setValue(self, values):
		if not self.inflatReady:
			self.inflat()

		if self.type.simOrCom == _SIMPLE:
			self.values = values
		else:
			for index, value in enumerate(self.values):
				value.setValue(values[index])
		
		self.valueReady = True

	def render(self):
		if self.maxOccurs == self.minOccurs:
			occurs = str(self.maxOccurs)
		else:
			occurs = str(self.minOccurs) + ' ~ ' + str(self.maxOccurs)
		return '<tr><td>' + self.name + '</td><td>' + occurs + '</td><td>' + self.type + '</td></tr>'

	def encode(self):
		pass

	def check(self, values):
		if not self.inflatReady:
			self.inflat()

		try:
			self.type.check(values)
		except BaseException(e):
			raise 'Element name=' + self.name + ' -> ' + e

	def rule(self, value):
		return {'name': self.name, 'maxOccurs': self.maxOccurs, 'minOccurs': self.minOccurs}

# if __name__ == '__main__':
# 	a = Element('test', 'baseType')
# 	print(a.render())