from extract_data import get_data_extract, get_sa_engine
import yaml

if __name__ == '__main__':
    with open('example_config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    engine = get_sa_engine(database_name=config['database_name'],
                           server_name=config['server_name'])
    extract_query = config['query']


    df = get_data_extract(engine=engine, query=extract_query)


    # Temp export to use whilst testing
    df.to_csv('test_output_policies.csv', index=False)
    print(df.describe())
