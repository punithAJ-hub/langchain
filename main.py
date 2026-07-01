from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

def main():
    print("Hello from langchain!")
    information = """ Elon Musk (born June 28, 1971) is a South African-born American technology entrepreneur and billionaire businessman. He is the CEO and largest shareholder of Tesla and SpaceX. With a net worth exceeding $950 billion, he is one of the wealthiest individuals in the world.Core BackgroundBirth: June 28, 1971, in Pretoria, South Africa.Nationality: South African-born, naturalized as a Canadian and later a U.S. citizen.Education: Attended Queen's University in Canada, then transferred to the University of Pennsylvania, where he earned degrees in physics and economics.Major Companies & VenturesSpaceX: Founder, CEO, and Chief Engineer (founded in 2002), aiming to revolutionize space technology and enable human life on Mars.Tesla: CEO and product architect. He oversees the company's mission to accelerate the world's transition to sustainable energy.xAI: Founder of the artificial intelligence company behind the Grok chatbot.The Boring Company: Founder, focused on infrastructure and tunnel construction.Other Notable ProjectsX (formerly Twitter): Purchased the social media platform in 2022 to promote his vision of "free speech" and transform it into an "everything app."Neuralink: Co-founder, developing implantable brain-computer interfaces.OpenAI: Co-founder, though he later stepped down from the board.PayPal: Founded X.com in 1999, which merged with Confinity in 2000 to become PayPal (later acquired by eBay)."""

    summary_template = """
    given information {information}, summarize the information into short intro and  2 interesting  facts
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(f"Summary: {response.content}")
if __name__ == "__main__":
    main()
