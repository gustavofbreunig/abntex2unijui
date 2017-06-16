#script que limpa todos arquivos gerados na compilação do pdflatex, deixando apenas o pdf

import os
import pathlib

dir = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(dir)
extensions = [".aux", ".bbl", ".blg", ".idx", ".log", ".gz", ".toc", ".lof", ".lot"]

for file in files:
	extensao = pathlib.Path(os.path.join(dir,file)).suffix
	if extensao in extensions:
		os.remove(file)