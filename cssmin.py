#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# based on Simple CSS Minifier by Rafał Jońca.
# http://blog.rafaljonca.org/2007/11/simple-css-minifier.html
# The (original) code is available on double license: GPL and MIT.

import re
import sys

RULES = [
  (r'\/\*.*?\*\/', ''),           # remove comments
  (r"\n", ""),                    # remove all newlines
  (r'[\t ]+', " "),               # change spaces and tabs to one space
  (r'\s?([;:{},+>])\s?', r"\1"),  # remove unneeded space
  (r';}', "}"),                   # remove final semicolon
]

def minimalize(css):
  css = css.replace("\r\n", "\n")
  for rule in RULES:
    css = re.compile(rule[0], re.MULTILINE|re.UNICODE|re.DOTALL).sub(rule[1], css)
  return css

if len(sys.argv) > 1:
  filename = sys.argv[1]
else:
  print "usage: cssmin.py [file]"
  sys.exit(1)

print minimalize(open(filename, 'r').read())
