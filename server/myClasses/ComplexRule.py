#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of ComplexRule'

__author__ = 'Sodablueblue'

from Rule import *

class ComplexRule(Rule):

	def __init__(self, elements):
		self.elements = elements

	def check(self, element):
		if not element in self.elements:
			raise BaseException('Choice not cover element')