#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Element'

__author__ = 'Sodablueblue'

from Base import *

class Element(Base):

	def __init__(self, name, type, maxOccurs = 1, minOccurs = 1):
		super(Element, self).__init__(name)
		self.type = type
		self.maxOccurs = maxOccurs
		self.minOccurs = minOccurs
		self.valueReady = False

	def setValue(self, value):
		self.type.setValue()
		self.valueReady = True

	def render(self):
		if self.maxOccurs == self.minOccurs:
			return '<tr><td>' + self.name + '</td><td>' + str(self.maxOccurs) + '</td><td>' + self.type + '</td></tr>'
		else:
			return '<tr><td>' + self.name + '</td><td>' + str(self.minOccurs) + ' ~ ' + str(self.maxOccurs) + '</td><td>' + self.type + '</td></tr>'

	def encode(self):
		if not self.valueReady:
			raise BaseElement(self.name + '\'s value not set')
		return '<' + self.name + '>' + self.type.encode() + '</' + self.name + '>'

	def check(self):
		return (int(self.maxOccurs), int(self.minOccurs))


if __name__ == '__main__':
	a = Element('test', 'baseType')
	print(a.render())