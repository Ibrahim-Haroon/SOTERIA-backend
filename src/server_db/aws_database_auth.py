from os import getenv as env
from dotenv import load_dotenv

load_dotenv()


def connection_string(
) -> str:
    """
    @rtype: str
    @return: connection string for AWS RDS
    """

    if (env('RDS_DB_NAME') and
        env('RDS_USERNAME') and
        env('RDS_PASSWORD') and
        env('RDS_HOSTNAME') and
        env('RDS_PORT')
    ):
        dsn = (f"dbname={env('RDS_DB_NAME')} "
               f"user={env('RDS_USERNAME')} "
               f"password={env('RDS_PASSWORD')} "
               f"host={env('RDS_HOSTNAME')} "
               f"port={env('RDS_PORT')}")
    else:
        raise SystemExit(f"Error in connection_string()")

    return dsn


if __name__ == "__main__":
    print(connection_string())
