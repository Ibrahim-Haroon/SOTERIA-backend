"""
script to get conversational ai response from gpt model
"""
from os import getenv as env
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

ROLE = """
        You are an agent at Bank of America. Your name is Soteria. Response should be formed solely based on
        on user details and conversation history. Don't add extra information to response.
       """

PROMPT = """
        Give a response (ex. "I just checked your account and it looks like you have a balance of $1000.
        Is there anything else I can help you with today?"
        but make your own and somewhat personalize per order to sound normal) given transcription
        and order details gathered from the database:
        """


def conv_ai(
        user_request: str, user_account_details: str, conversation_history: str
) -> str:
    """
    @rtype: str
    @param user_request: complete transcription of the users request
    @param user_account_details: customers account details
    @param conversation_history: all previous conversation history
    @param api_key: openi api key
    """
    api_key = env('OPENAI_API_KEY')

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role": "system",
                "content": (f"{ROLE} and all previous conversation history: "
                            f"{conversation_history}."
                            )
            },
            {
                "role": "user",
                "content": f"{PROMPT}\n"
                           f"transcription: {user_request}"
                           f" + order details: {user_account_details}"
            }
        ],
        stream=True
    )

    for chunk in response:
        yield chunk.choices[0].delta.content


def main(

) -> None:
    """
    @rtype: None
    @return: 0 if successful
    """
    for _ in conv_ai(
            user_request="How much money do I have in my checking account?",
            user_account_details=
            """
            (
                [
                    {
                        "full_name": "John Doe",
                        "checking_balance": 1000.0,
                        "savings_balance": 5000.0,
                        "current_credit_balance": 0.0,
                        "current_debit_balance": 0.0,
                        "credit_limit": 10000.0,
                        "cash_back_balance": 0.0,
                        "credit_score": 750
                    }
                ],
             '')
            """,
            conversation_history=""
    ):
        print(_)


if __name__ == "__main__":
    main()
