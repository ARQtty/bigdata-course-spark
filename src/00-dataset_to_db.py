import pandas as pd
from sqlalchemy import create_engine


if __name__ == '__main__':
    user = 'root'
    password = 'secret'
    db = 'db'
    host = 'database'
    engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{db}")

    df = pd.read_csv('data/subset.csv')
    df.to_sql('data', engine)
    print('done')
