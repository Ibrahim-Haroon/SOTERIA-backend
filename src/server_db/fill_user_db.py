import psycopg2
from tqdm import tqdm
from src.server_db.aws_sdk_auth import get_secret
from src.server_db.aws_database_auth import connection_string


def fill_products_table(
        data: list[dict]
) -> bool:
    """

    @rtype: bool
    @param data: all the menu items which have to be embedded and inserted in DB
    @return: true if successfully created and filled table
    """

    get_secret()
    db_connection = psycopg2.connect(connection_string())
    db_connection.set_session(autocommit=True)

    cur = db_connection.cursor()

    cur.execute("DROP TABLE IF EXISTS users;")

    cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                full_name text,
                checking_balance double precision,
                savings_balance double precision,
                current_credit_balance double precision,
                current_debit_balance double precision,
                credit_limit double precision,
                cash_back_balance double precision,
                credit_score int
            );
    """)

    for item in tqdm(data):
        cur.execute("""
            INSERT INTO users (
            full_name, checking_balance, savings_balance, current_credit_balance,
             current_debit_balance, credit_limit, cash_back_balance, credit_score
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (item['full_name'],
              item['checking_balance'],
              item['savings_balance'],
              item['current_credit_balance'],
              item['current_debit_balance'],
              item['credit_limit'],
              item['cash_back_balance'],
              item['credit_score']
              ))

    cur.execute("VACUUM ANALYZE users;")

    cur.close()
    db_connection.close()

    return True


def main(

) -> int:  # pragma: no cover
    """
    @rtype: int
    @return: 0 if successfully filled table
    """
    data = [
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
    ]

    fill_products_table(data)
    return 0


if __name__ == "__main__":
    main()
