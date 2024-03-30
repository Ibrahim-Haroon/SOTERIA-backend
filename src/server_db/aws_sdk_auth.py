"""
This file is used to get the AWS secret from the AWS Secrets Manager.
"""
from os import getenv as env
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

load_dotenv()


def get_secret(
) -> dict:
    """
    @purpose: SDK for AWS
    @rtype: dict
    @return: ex. {
                    "username":"username",
                    "password":"pass",
                    "host":"host",
                    "port":5432,
                    "dbname":"name",
                    "dbInstanceIdentifier":"db-id"
                }
    """

    if (env('AWS_ACCESS_KEY_ID') and
        env('AWS_SECRET_ACCESS_KEY') and
        env('AWS_DEFAULT_REGION') and
        env('SECRET_NAME')
    ):
        secret_name = env('SECRET_NAME')
        region_name = env('AWS_DEFAULT_REGION')
        aws_access_key_id = env('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = env('AWS_SECRET_ACCESS_KEY')

    else:
        raise SystemExit(f"Error in get_secret()")

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    return get_secret_value_response['SecretString']


if __name__ == "__main__":
    get_secret()
