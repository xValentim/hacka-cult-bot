from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq

load_dotenv()

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)

system_prompt = """

Flávio Cerqueira
São Paulo Brasil [Brazil], 1983

Amnésia [Amnesia], 2015
Látex sobre bronze, prova de artista 2/2
Coleção do artista, em empréstimo de longa
duração ao MASP 

O paulistano Flávio Cerqueira aborda em seus
trabalhos a temática racial. Em Amnésia,
Cerqueira representa uma criança negra de braços
erguidos, segurando um balde de tinta branca que
ela despeja sobre sua cabeça; a tinta escorre sobre
seu corpo, contudo, não se impregna nele. A obra
faz referência ao branqueamento das populações
negras no Brasil, uma história em que as imigrações
europeias a partir do século 19 tinham também a
perversa função de tornar menos negra a população.
Um dos focos da obra é a lata de tinta que se apresenta
quase vazia. Seria possível interpretá -la, portanto,
como uma espécie de esgotamento de tal processo
de embranquecimento. A escultura em bronze —
um dos mais nobres e robustos dos materiais,
associado de fato à escultura tradicional e hoje pouco
utilizado na arte contemporânea, sobretudo com
conteúdos mais políticos — parece ter sido feita como
um antídoto contra o esquecimento dessas histórias
para as quais devemos estar sempre atentos, daí seu
caráter simbólico e materialmente indestrutível.

"""

system_datails = """

Flávio Cerqueira
Amnésia, 2015
Autor:Flávio Cerqueira
Dados biográficos:São Paulo, Brasil, 1983
Título:Amnésia
Data da obra:2015
Técnica:Látex sobre bronze
Dimensões:129 x 42 x 41 cm
Aquisição:Doação do artista, no contexto da exposição Histórias Afro-atlânticas, 2018
Designação:Escultura
Número de inventário:MASP.10800
Créditos da fotografia:MASP

"""

system_extra_content = """

Por Adriano Pedrosa e Tomás Toledo, 2020

O paulistano Flávio Cerqueira aborda em seus trabalhos a temática racial. Em Amnésia, Cerqueira representa uma criança negra de braços erguidos, segurando um balde de tinta branca que ela despeja sobre sua cabeça; a tinta escorre sobre seu corpo, contudo, não se impregna nele. A obra faz referência ao branqueamento das populações negras no Brasil, uma história em que as imigrações europeias a partir do século 19 tinham também a perversa função de tornar menos negra a população. Um dos focos da obra é a lata de tinta que se apresenta quase vazia. Seria possível interpretá­‐la, portanto, como uma espécie de esgotamento de tal processo de embranquecimento. A escultura em bronze — um dos mais nobres e robustos dos materiais, associado de fato à escultura tradicional e hoje pouco utilizado na arte contemporânea, sobretudo com conteúdos mais políticos — parece ter sido feita como um antídoto contra o esquecimento dessas histórias para as quais devemos estar sempre atentos, daí seu caráter simbólico e materialmente indestrutível.

— Adriano Pedrosa, diretor artístico, e Tomás Toledo, curador-chefe, MASP, 2020

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
