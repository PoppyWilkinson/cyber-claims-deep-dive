from extract_data import get_data_extract, get_sa_engine
import yaml

if __name__ == '__main__':
    with open('secret_config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    engine = get_sa_engine(database_name=config['secret_database_name'],
                           server_name=config['secret_server_name'])
    extract_query = config['secret_query']

    #dates_to_parse = ['add_date', 'modify_date']

    df = get_data_extract(engine=engine,
                                  query=extract_query)
                                  #dtype_dict=dtype_dict,
                                  #dates_to_parse=dates_to_parse)

    # Temp export to use whilst testing
    df.to_csv('test_output_policies.csv', index=False)
    print(df.describe())
