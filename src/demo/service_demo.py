from src.ai_linkage.conversational_ai import conv_ai
from src.server_db.get_user_db import get_user_info


def main() -> None:
    """
    @rtype: None
    @return: 0 if successful
    """
    conversation_history = ""
    print("Welcome to the demo!")
    user_name = input("What is your full name? ")
    account_details, _ = get_user_info(user_name)

    while (True):
        user_response = input("What would you like to know about your account? ")

        soteria_response = conv_ai(
            user_request=user_response,
            user_account_details=account_details,
            conversation_history=conversation_history,
        )

        print(soteria_response)
        conversation_history += soteria_response

    return


if __name__ == "__main__":
    main()