from api.ai.llms import get_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_message(query: str) -> EmailMessageSchema:
    llm_base = get_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional AI assistant who writes clear, polite, and well-structured emails. "
                "When given a scenario, respond with two fields: 'subject' for the email's subject line, and "
                "'content' for the full email body text. Use natural language, proper grammar, and punctuation. "
                "Do not include markdown or any formatting symbols."
            )
        },
        {
            "role": "user",
            "content": (
                f"Write a professional email based on this scenario:\n{query}\n\n"
                "Please respond only with the two fields 'subject' and 'content'."
            )
        }
    ]

    return llm.invoke(messages)


