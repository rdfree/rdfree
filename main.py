#!/usr/bin/env python
# -*- coding: utf-8 -*-

from extractor import extractor
from normalizer import normalizer
from converter import converter

if __name__ == "__main__":

  results = extractor()
  nodes, ties = normalizer(results)
  converter(nodes, ties)