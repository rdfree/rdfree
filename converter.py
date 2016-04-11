#!/usr/bin/env python
# -*- coding: utf-8 -*-

from templates.gephi import Gephi

def converter(nodes,ties):

  # Conversão para gexf
  print u'Iniciando conversão para formato gexf'
  gephi = Gephi()
  gephi.convert(nodes, ties)

  # Acrescentar aqui as chamadas para os templates de cada formato que pode ser escolhido
  