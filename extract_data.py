import pandas as pd
import sqlalchemy as sa


def get_sa_engine(database_name: str, server_name: str) -> sa.engine:
    """
    Create sql-alchemy engine object to connect to databases

    :param database_name: database name
    :param server_name: domain of server
    :return engine: sql-alchemy engine object
    """
    conn_string = f"mssql+pyodbc://@{server_name}/{database_name}?trusted_connection=yes&driver=SQL+Server"
    engine = sa.create_engine(conn_string)

    return engine


def get_data_extract(engine: sa.engine,
                     query: str) -> pd.DataFrame:
                    # dtype_dict:dict,
                    # dates_to_parse:list=None) -> pd.DataFrame:

    df = pd.read_sql(sql=query,
                     con=engine)
                     #dtype=dtype_dict,
                     #parse_dates=dates_to_parse)

    return df
