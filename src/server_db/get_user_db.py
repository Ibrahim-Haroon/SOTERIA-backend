import psycopg2
from src.server_db.aws_sdk_auth import get_secret
from src.server_db.aws_database_auth import connection_string


def get_user_info(
        user_full_name: str
) -> str and bool:
    """

    @rtype: str + bool
    @param user_full_name: prompt from user
    @return: user information along with a boolean flag to mark successful retrieval
    """
    if not user_full_name:
        return None, False

    db_connection = psycopg2.connect(connection_string())
    db_connection.set_session(autocommit=True)

    cur = db_connection.cursor()

    cur.execute(""" SELECT id, full_name, checking_balance, savings_balance, current_credit_balance, 
                           current_debit_balance, credit_limit, cash_back_balance, credit_score
                    FROM users
                    WHERE full_name = %s;
                """,
                (user_full_name,))

    result = cur.fetchall()

    cur.close()

    db_connection.close()

    return result, True


def main(

) -> int:
    """
    @rtype: int
    @return: 0 if successful
    """
    get_secret()

    res = get_user_info(
        user_full_name="John Doe",
    )

    print(res)

    return 0


if __name__ == "__main__":
    main()
