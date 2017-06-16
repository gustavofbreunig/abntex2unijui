# unijuiabntex2

Pacote de customização do abntex2 para atender as normas ABNT específicas da Universidade Regional do Noroeste do Estado do Rio Grande do Sul (UNIJUI).

O documento oficial pode ser acessado [através da biblioteca digital](http://bibliodigital.unijui.edu.br:8080/xmlui/handle/123456789/2905) (ou [link alternativo](https://github.com/gustavofbreunig/abntex2unijui/files/1081810/TRABALHOS.ACADEMICOS.85-2016-UNIJUI.pdf) ) e serve como base em trabalhos, teses e dissertações da universidade.

## Requisitos

- Qualquer ambiente de desenvolvimento LaTeX, recomendo o uso do [TeXstudio](http://www.texstudio.org/) por ter um ambiente completo e multiplataforma.
- [getnonfreefonts](https://www.tug.org/fonts/getnonfreefonts/) para habilitar a fonte Arial, o download será feito automaticamente caso estiver usando o TeXstudio.

## Como utilizar

Baixe o arquivo `unijui.sty` para a pasta do seu projeto e inclua a linha no preambulo:

```tex
\usepackage{unijui}
```

Obs: O arquivo ` exemplo.tex` já possui a estrutura básica de um trabalho com:

- Capa
- Folha de Rosto
- Folha de Aprovação
- Dedicatória
- Agradecimentos
- Epígrafe
- Resumo
- Abstract
- Lista de Ilustrações
- Lista de Tabelas
- Lista de Abreviaturas e Siglas
- Lista de Símbolos
- Sumário
- Introdução
- Desenvolvimento
- Conclusão
- Referências (linkado ao arquivo bibliografia.bib)
- Anexos

Você pode utilizar este arquivo como base para o desenvolvimento do seu trabalho.

## Créditos

### Essa customização

[Gustavo Freddo Breunig](mailto:gustavofbreunig@gmail.com): 

- Espaçamentos da capa e folha de rosto de acordo com o documento oficial;
- Fonte Arial;
- Tamanho das fontes;
- Folha de Aprovação;
- Título das referências em negrito.

### Customização original

[Cristiano Politowski](https://github.com/polako/unijui_latex_template):

- Customização de capa, folha de rosto.

