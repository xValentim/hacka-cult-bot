from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq

load_dotenv()


content_venus = """

Pierre-Auguste Renoir

Limoges, França [France], 1841 – Cagnes-surMer, França [France], 1919

A partir da década de 1890, Pierre-Auguste Renoir
começou a desenvolver artrite reumatóide, o que
impactou severamente sua forma de trabalhar.
Mesmo com as mãos debilitadas, produziu uma
enorme quantidade de pinturas até sua morte.
São também desse período quase todas as suas
esculturas, produzidas, a partir de 1913, com o auxílio
do jovem artista Richard Guino (1890-1973), que
havia trabalhado com Aristide Maillol (1861-1944),
escultor próximo ao pintor. Renoir rascunhava os
esboços e Guino os traduzia em modelagem, ajustada
conforme o artista apontava os pontos a serem
modificados. Durante os cinco anos de parceria,
foram criadas catorze esculturas. Tal como Vênus
Vitoriosa, grande parte desse conjunto partiu da
pintura O julgamento de Páris, feita por Renoir alguns
anos antes. Refere-se ao episódio da mitologia grega
conhecido como “Pomo da Discórdia”, a disputa entre
Juno (Hera), Minerva (Atenas) e Vênus (Afrodite)
pela maçã de ouro destinada à mais bela. Páris, um
jovem mortal convocado para resolver o impasse,
foi conquistado por Vênus, que lhe ofereceu em
troca o amor verdadeiro, prometendo-lhe Helena
(posteriormente conhecida como Helena de Tróia).
A Vênus Vitoriosa segura em sua mão direita a maçã
recebida como reconhecimento de sua beleza. O
rosto da deusa assemelha-se ao de Gabrielle Renard
(1878-1959), prima da esposa do artista, que cuidava
dos filhos do casal e foi sua principal modelo
no período tardio. Entre as peças desse período,
lavadeiras e figuras femininas lembram as banhistas
de suas pinturas. O MASP também possui doze
pinturas de Renoir, cobrindo toda a sua carreira.

"""


# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)

system_prompt = """

Você é um guia de museu que irá tirar dúvidas sobre a obra Venus Victrix (Vênus Vitoriosa) de Pierre-Auguste Renoir.

O contexto da obra você pode encontrar aqui:

Pierre-Auguste Renoir

Limoges, França [France], 1841 – Cagnes-surMer, França [France], 1919

A partir da década de 1890, Pierre-Auguste Renoir
começou a desenvolver artrite reumatóide, o que
impactou severamente sua forma de trabalhar.
Mesmo com as mãos debilitadas, produziu uma
enorme quantidade de pinturas até sua morte.
São também desse período quase todas as suas
esculturas, produzidas, a partir de 1913, com o auxílio
do jovem artista Richard Guino (1890-1973), que
havia trabalhado com Aristide Maillol (1861-1944),
escultor próximo ao pintor. Renoir rascunhava os
esboços e Guino os traduzia em modelagem, ajustada
conforme o artista apontava os pontos a serem
modificados. Durante os cinco anos de parceria,
foram criadas catorze esculturas. Tal como Vênus
Vitoriosa, grande parte desse conjunto partiu da
pintura O julgamento de Páris, feita por Renoir alguns
anos antes. Refere-se ao episódio da mitologia grega
conhecido como “Pomo da Discórdia”, a disputa entre
Juno (Hera), Minerva (Atenas) e Vênus (Afrodite)
pela maçã de ouro destinada à mais bela. Páris, um
jovem mortal convocado para resolver o impasse,
foi conquistado por Vênus, que lhe ofereceu em
troca o amor verdadeiro, prometendo-lhe Helena
(posteriormente conhecida como Helena de Tróia).
A Vênus Vitoriosa segura em sua mão direita a maçã
recebida como reconhecimento de sua beleza. O
rosto da deusa assemelha-se ao de Gabrielle Renard
(1878-1959), prima da esposa do artista, que cuidava
dos filhos do casal e foi sua principal modelo
no período tardio. Entre as peças desse período,
lavadeiras e figuras femininas lembram as banhistas
de suas pinturas. O MASP também possui doze
pinturas de Renoir, cobrindo toda a sua carreira.

"""

system_datails = """

Título: Venus Vitoriosa (Venus Victrix)
Criador: Pierre Auguste Renoir
Vida do criador: 1841 - 1919
Local de nascimento do criador: Limoges, França
Local da morte do criador: Cagnes-sur-Mer, França
Data: 1916 - 1916
Dimensões físicas: L128 x A180 x D80 cm
Crédito de imagem: João Musa
Linha de crédito: João Musa
Procedência: Doação Maria Helena Morganti, 1951
Tipo: Escultura
Meio: Bronze

"""

system_extra_content = """

Contexto a mais:

Por Luciano Migliaccio
A obra Vênus Vitoriosa procede da Petite Venus (altura, 60 cm), primeira escultura de Richard Guino, realizada em 1913 sob a supervisão de Renoir, impedido de trabalhar por causa da artrite, e tem como modelo a Vênus do Julgamento de Páris, criada naquele mesmo ano. A versão em bronze do Masp foi fundida por volta de 1915-1916 pela Fundição Rudier, que fez três exemplares. O exemplar do Masp tem o número 2. O número 1 encontra-se no Petit Palais de Paris, e o número 3 no Museum Boymans-Van Beuningen de Roterdã. Outras fusões existentes em outros museus e coleções particulares seriam surmoulages realizados a partir destas (Camesasca 1979, p. 88). Para P. Haesaerts (1947, p. 18), essa é a mais acabada e a mais complexa das esculturas idealizadas por Renoir.

— Luciano Migliaccio, 1998


Fonte: Luiz Marques (org.), Catálogo do Museu de Arte de São Paulo Assis Chateaubriand, São Paulo: MASP, 1998. (reedição, 2008).

"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("system", system_datails),
        ("system", system_extra_content),
        ("human", "{input}"),
    ]
)

chain = prompt | llm | StrOutputParser()
