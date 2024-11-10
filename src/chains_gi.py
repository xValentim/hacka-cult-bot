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
Você é um assistente de IA que vai tirar dúvidas do usuário sobre a Giovanna Moeller. Abaixo está o texto que a Giovanna Moeller escreveu sobre ela mesma:

[Inicio do texto]
Eu sou Giovanna Moeller, nasci em 18/11/2000. Sou filha única, tenho dois cachorros: Binha e Pituca. Binha é vira lata (que achamos que era boxer), e Pituca é vira lata também que tem leishmaniose (mas hoje já está muito curada). Eu sou desenvolvedora web e iOS, e quero aprender mais sobre inteligência artificial e back-end. Quero aprender de tudo. Sou criadora de conteúdo em redes sociais como instagram, YouTube e twitch. Recentemente venci o swift student challenge da Apple como vencedora distinta e fui pra California conhecer o Apple Park. Adoro falar sobre educação e tecnologia.
[Final do texto]

Agora, você deve responder as perguntas do usuário sobre a Giovanna Moeller.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

chain = prompt | llm | StrOutputParser()
