from jsonschema import draft4_format_checker
import pandas as PD
from vb2csv import read_vbo

file = 'file.txt'

df4 = read_vbo(file)


df4.to_csv(f'folder//subfolder//{file}.csv')
