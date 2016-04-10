#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Extension'

__author__ = 'Sodablueblue'

from Attribute import *

class Extension(object):

	def __init__(self, attribute, base):
		self.attribute = attribute
		self.base = base

	def check():
		self.base.check()
		if not self.attribute isinstance Attribute:
			raise BaseException('Extension doesn\'t has attribute') 