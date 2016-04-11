#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of SimpleContent'

__author__ = 'Sodablueblue'

from Rule import *

class SimpleContent(Combination):

	def __init__(self, criteria):
		super(Sequence, self).__init__('Sequence', criteria)

	#TODO: