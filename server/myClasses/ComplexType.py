#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of ComplexType'

__author__ = 'Sodablueblue'

from Type import *

class ComplexType(Type):

	def __init__(self, name, rules):
		supe(ComplexType, self).__init__(name, rules)

	