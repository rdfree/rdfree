#!/usr/bin/env python
# -*- coding: utf-8 -*-

OUTPUT_FILE = 'output.gexf'
ENDPOINT = "http://dbpedia.org/sparql"
QUERY = '''
prefix dbpedia: <http://dbpedia.org/ontology/> 
prefix dbprop: <http://dbpedia.org/property/> 
prefix dbsource: <http://dbpedia.org/resource/> 
SELECT DISTINCT
 ?bandaA, ?bandaB, ?genero
WHERE {
?bandA dbprop:background "group_or_band"@en.
?bandB dbprop:background "group_or_band"@en.
?bandA dbprop:genre ?genre.
?bandB dbprop:genre ?genre.
?bandA dbprop:origin ?country.
?bandB dbprop:origin ?country.
?country a dbpedia:Country.
?bandA rdfs:label ?bandaA.
?bandB rdfs:label ?bandaB.
?genre rdfs:label ?genero.
FILTER(?bandA != ?bandB && 
	   ?country = dbsource:Brazil && 
	   langMatches(lang(?bandaA), "pt") && 
	   langMatches(lang(?bandaB), "pt") &&
           langMatches(lang(?genero), "pt") )
}
'''

# GEXF
CREATOR = 'RDFree'
DESCRIPTION = 'A tool for transform linked data into networks formats'
DEFAULTEDGETYPE = 'undirected'
MODE = 'static'
LABEL = 'Relacionamento entre bandas'

