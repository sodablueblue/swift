#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of SequenceRule'

__author__ = 'Sodablueblue'

from Rule import *

class SequenceRule(Rule):

	def __init__(self, elements):
		self.elements = elements

	def check(self, elements):
		if not self.elements.equal(elements):
			raise BaseException('Sequence not equal')