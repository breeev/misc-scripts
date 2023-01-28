#!/usr/bin/python

from pdf2image import convert_from_path
convert_from_path(input('Path: '), 600)[0].save(input('File name: '))
