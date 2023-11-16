#Objetivo: fazer um script que puxa automaticamente os dados disponíveis e colaca-los em um formato que poderão ser analisados. Fazer alguns gráficos e gerar um relatório (em PDF) que deve conter o conteúdo da análise e o resultado
from fpdf import FPDF

# #Criar uma variável para guardar os dados da planilha
# arquivo = pd.read_csv("Dados.csv")

#gerando o gráfico com os dados da planilha
#class
class PDF(FPDF):
#configurando o titulo
    def doc_title(self, Label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, Label, 0, 1, 'L')
        self.ln()
#configurando o texto
    def doc_text(self, text):
        self.set_font('helvetica', '', size=13)    
        self.multi_cell(0, 8, text)
        self.ln()
#configurando a imagem
    def doc_img(self, img, x, y, w, h):
        self.image(img, x, y, w, h)

#Criando o PDF
pdf = PDF()
pdf.add_page()

pdf.doc_title("A Persistência na Desigualdade Educacional Brasileira")

pdf.doc_text("A presente pesquisa tem como objetivo primordial analisar a persistência da desigualdade educacional no Brasil, abrangendo diferenças entre grupos raciais, de gênero, pessoas com deficiência e níveis socioeconômicos. A disparidade no acesso e na qualidade da educação reflete uma teia complexa de fatores interconectados, sendo este um fenômeno profundamente enraizado na estrutura socioeconômica do país.")

pdf.doc_text("A concentração de recursos e oportunidades em estratos sociais específicos cria um ambiente propício para a continuidade dessa disparidade educacional. Comunidades de baixa renda frequentemente se deparam com obstáculos tanto físicos, como a falta de proximidade de instituições de ensino, quanto financeiros, como a incapacidade de arcar com despesas relacionadas à educação, como materiais escolares e transporte.")

pdf.doc_text("Mesmo quando o acesso é viável, a qualidade da educação oferecida varia significativamente. Escolas localizadas em áreas economicamente desfavorecidas tendem a contar com menos recursos, professores menos capacitados e uma infraestrutura precária. Isso gera um ciclo de desvantagem para os alunos dessas comunidades.")

pdf.doc_text("A escassez de oportunidades se torna particularmente preocupante ao examinarmos o setor público. Isso complica ainda mais a entrada nas instituições de ensino públicas, dada a significativa demanda em relação à oferta limitada de vagas. A intensificação da competição resulta em critérios de seleção mais rigorosos, exigindo dos candidatos uma preparação ainda mais aprimorada, dado o grande número de concorrentes para um número restrito de posições disponíveis.")

pdf.add_page()

pdf.doc_img("grafico-01.png", 30, 10, 150, 135)

pdf.ln(130) 

pdf.doc_text("Ao analisar o gráfico, torna-se evidente a disparidade na disponibilidade de vagas entre Instituições Privadas e Públicas. Em números aproximados, mais de 90% das vagas pertencem a instituições privadas com fins lucrativos, enquanto 2% são de instituições privadas sem fins lucrativos. Por outro lado, menos de 1% é composto por instituições públicas municipais e também estaduais. Essa distribuição reflete a ampla gama de tipos de instituições educacionais presentes no Brasil.")

pdf.doc_text("Essa variedade nas categorias administrativas das instituições de ensino ressalta a relevância da colaboração dos setores público-privada na oferta de cursos, proporcionando aos estudantes uma diversidade de opções. Esse fenômeno é um reflexo da persistente da desigualdade social enraizada no Brasil, que tem impactado cada vez mais a população.")

pdf.doc_text("Existem diversos fatores que contribuem para a desigualdade no acesso à educação, porém, por si só, não explicam completamente a persistência dessas disparidades. É notável que a Educação tenha se solidificado como um dos pilares fundamentais da estrutura social atual, tornando-se, infelizmente, um elemento que sustenta a desigualdade social. Isso se manifesta em práticas discriminatórias e na perenização de estereótipos que ganham espaço tanto dentro das escolas quanto nos sistemas educacionais.")

pdf.doc_title("Análise da distribuição de vagas por grau de ensino na região Sudeste: ")

pdf.doc_text("A seleção do tipo de formação acadêmica, como Bacharelado, Licenciatura, Tecnológico, entre outros, desempenha um papel crucial na decisão educacional. Optar por um curso universitário marca o início de uma jornada profissional. Durante a faculdade, os estudantes adquirem os conhecimentos essenciais para adentrar o cenário profissional por meio de estágios. Em muitas situações, os estagiários conseguem se destacar, resultando na sua efetivação por parte das empresas.")

pdf.doc_text("Para que esse processo seja bem-sucedido, é crucial que o aluno demonstre um elevado grau de dedicação ao longo da graduação, visto que é necessário adquirir competências técnicas que serão aplicadas no ambiente corporativo. Isso se torna mais acessível quando se opta por uma instituição de ensino superior que conta com professores altamente qualificados e uma infraestrutura de excelência.")

pdf.doc_text("Quando uma instituição de ensino superior proporciona aos estudantes condições adequadas para assimilar o conteúdo programático, as chances de os alunos se destacarem nos testes direcionados à contratação de estagiários e trainees promovidos pelo setor privado são significativamente ampliadas.")

pdf.add_page()

pdf.doc_img("grafico-02.png", 30, 10, 150, 135)

pdf.ln(140)

pdf.doc_text(" Ao analisar o gráfico fornecido, notamos que a maioria dos cursos é categorizada como Tecnológico, seguido por Bacharelado e Licenciatura. Essa distribuição reflete as preferências dos alunos e as demandas do mercado de trabalho. A predominância de cursos de Bacharelado sugere uma inclinação para formações mais abrangentes, enquanto os cursos Tecnológicos atendem a necessidades específicas do mercado de trabalho.")

pdf.doc_text("A busca pelos cursos tecnólogos experimentou um aumento significativo nos últimos anos. Conforme indicado pelo Censo de Educação Superior, no período de 2006 a 2016, as inscrições nesse formato de graduação quase triplicaram. Essa alternativa se revela excelente para aqueles que almejam obter um diploma, adquirir qualificação, e desejam evitar a espera de 4 anos (ou mais) para a conclusão do curso.")

pdf.doc_text("Embora as modalidades de bacharelado e licenciatura permaneçam como as mais populares, aqueles que optam pelos cursos tecnólogos têm a oportunidade de aprofundar-se em áreas específicas de conhecimento, tornando-se, assim, especialistas.")

pdf.doc_text("Indiscutivelmente, o custo representa uma das vantagens primárias dos cursos tecnológicos. Aqueles que estão inseridos no mercado de trabalho, em busca de uma posição sólida, frequentemente se deparam com limitações financeiras que dificultam o investimento em uma graduação convencional. ")

pdf.doc_text("A ausência de um diploma também restringe as oportunidades de acesso a melhores colocações profissionais. Diante desse cenário, os cursos tecnológicos emergem como uma alternativa atrativa. ")

pdf.doc_text("Além disso, as opções disponíveis são bastante abrangentes, proporcionando ao aluno a capacidade de escolher a área de especialização desejada. Conforme registrado no Catálogo Nacional de Cursos Superiores de Tecnologia pelo Ministério da Educação (MEC), há um total de 112 variedades de graduações tecnológicas.")

pdf.doc_title("Análise da distribuição de vagas por modalidade na região Sudeste:")

pdf.doc_img("grafico-03.png", 30, 144, 150, 135)

pdf.add_page()

pdf.doc_text("A alocação de cursos em diferentes modalidades, seja presencial ou a distância, é um elemento crucial no panorama da educação superior. Ao analisar o gráfico, torna-se evidente que a maioria dos cursos pertence à modalidade a distância (Educação a Distância). Esse padrão pode indicar uma crescente preferência por cursos online, destacando a flexibilidade que essa modalidade proporciona aos estudantes.")

pdf.doc_text("O ensino a distância oferece uma flexibilidade superior em comparação com os cursos presenciais. Os estudantes não necessitam deslocar-se diariamente de suas residências, nem passar longas horas em salas de aula, uma vez que a maioria das aulas ocorre online. Nesse formato, os alunos acompanham as aulas utilizando um computador e uma conexão com a internet. O material educacional é disponibilizado nos websites das instituições, em áreas restritas, e os alunos registrados têm acesso irrestrito a esses recursos.")

pdf.doc_text("Os horários para estudo e execução de atividades são determinados pelo próprio estudante. Se ele optar por estudar durante a madrugada, por exemplo, isso não é um problema, pois o acesso ao site está disponível 24 horas por dia. Os alunos têm a liberdade de estudar a qualquer momento e em qualquer lugar, seja em suas residências, bibliotecas, casas de amigos ou até mesmo em locais que ofereçam serviços de internet.")

pdf.doc_title("Conclusão")

pdf.doc_text("Em resumo, a análise do panorama educacional abarcou uma ampla gama de aspectos, desde a desigualdade social até a variedade de cursos e modalidades disponíveis. Essas informações representam um recurso valioso para estudantes, educadores e formuladores de políticas educacionais, capacitando-os a tomar decisões esclarecidas acerca do futuro do ensino superior no Brasil.")

pdf.doc_text("Dessa análise, deduz-se que os estudantes enfrentam desafios financeiros e obstáculos significativos no acesso à educação. Mesmo quando o acesso é possível, deparam-se com questões relativas à qualidade do ensino. Num contexto pós-pandêmico, observa-se uma preferência dos estudantes por cursos tecnológicos e a distância. Isso se justifica pela facilidade de estudar no conforto do ambiente escolhido, aspectos financeiros mais acessíveis e uma redução no período de absorção de conhecimento.")

pdf.output("Script.pdf") 
