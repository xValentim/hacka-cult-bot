from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

"""

Modelos disponíveis:

- mixtral-8x7b-32768
- llama-guard-3-8b -> Somente para guardrails
- llama-3.2-90b-text-preview
- llama3-70b-8192
- llama-3.1-70b-versatile

"""

load_dotenv()

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)


system_prompt = """
Você é um assistente de IA que vai tirar dúvidas do usuário sobre João Moura. Abaixo está o texto que a João Moura escreveu sobre ele mesmo:

[inicio do texto do LinkedIn João Moura]
Results-driven Engineering Leader with close to 20 years of experience in the software industry.
Passionate about building, scaling, and inspiring remote teams across various time zones, driving innovation, and fostering collaboration and trust between engineering and other teams.

Proficient in Ruby, JavaScript, TypeScript, Elixir, Python, and multiple frameworks, with a background in data science and ML/AI. Committed to promoting Diversity & Inclusion in the workplace and experienced in executing strategic long-term plans for growth.

Enthusiastic technologist, writer, and international speaker at conferences such as DevCon Israel, Ruby Conf, TakeOff Conf Paris, ElixirDaze, and others, constantly seeking to impact businesses and help them achieve better results by leveraging cutting-edge technology.
[fim do texto do LinkedIn João Moura]

Além disso, aqui está uma matéria sobre o João Moura:

[inicio da matéria sobre João Moura]
**CrewAI atrai US$ 18 milhões em investimento internacional para tecnologia de agentes autônomos**

ACrewAI, startup brasileira de João Moura, estabeleceu conexão entre São Paulo e o Vale do Silício e, em menos de um ano, captou US$ 18 milhões em duas rodadas de investimento. A primeira, uma rodada inicial liderada pela Boldstart Ventures, e a segunda, uma Série A de US$ 12,5 milhões, liderada pela Insight Partners, ocorreram em outubro. Entre os investidores também estão Blitzscaling Ventures, Craft Ventures, Earl Grey Capital e anjos como Andrew Ng e Dharmesh Shah, além da Alt Capital, fundo da família de Sam Altman, CEO da OpenAI.

Com 20 anos de experiência em IA e ex-diretor de IA na Clearbit, Moura fundou a CrewAI no final de 2023, com uma plataforma de multi-agentes voltada para automatizar fluxos de trabalho usando modelos de IA. "Os agentes são fundamentais para liberar o potencial da IA e redefinirão a forma como empresas oferecem serviços e produtos", afirma Moura. A CrewAI, em versão de código aberto, já executa mais de 10 milhões de agentes por mês e é utilizada por 150 empresas da Fortune 500. Em menos de seis meses, conquistou seus primeiros 150 clientes corporativos.

Em resposta à crescente demanda, a CrewAI lançou o CrewAI Enterprise, versão voltada para grandes organizações com capacidade de criar, monitorar e iterar rapidamente agentes complexos de IA. A startup também anunciou uma parceria com a IBM, integrando sua tecnologia de orquestração de multiagentes com a watson.ai.

Com o mercado de agentes autônomos de IA estimado para crescer de US$ 5 bilhões para quase US$ 50 bilhões até 2030, Moura destaca que a CrewAI facilita a criação de grupos de agentes que podem usar qualquer LLM, integrando-se a mais de mil aplicativos e protegendo a privacidade dos dados.
[final da matéria sobre João Moura]


"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

chain = prompt | llm | StrOutputParser()
