#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class for Type'

__author__ = 'Sodablueblue'

from Base import *

class Type(Base):
	def __init__(self, name, rule):
		super(Type, self).__init__(name)
		self.rule = rule
		self.values = None

	def setValue(self, values):
		self.values = values

	def render(self):
		return '<tr><td>' + self.name + '</td><td>' + self.condition.name + '</td><td>' + self.condition.rules + '</td></tr>'

	def check(self):
		rules = [
		
		for value in self.values:
			rules = rules + value.rule

		try:
			for rule in self.rules:
				rule.check(self.value)
		except BaseException as e:
			print('except: ', self.__class__._name__, 'check error. ', e) 
		finally:
			pass
