import pandas as pd

data = pd.read_csv('./sa_data_out.csv')

class DataManagement:
    '''Class DataManagement receive query and send data'''
    def get_data_contry(country):
        '''return a list of years by country name'''
        if country in data:
            return data[country].tolist()
        else:
            return []
    def get_data_contry_by_year(country, year):
        if year in data.Year.values:
            return data.loc[data["Year"] == year][country]
        else:
            return []





DataManagement.get_data_contry('Peru')
DataManagement.get_data_contry('aeru')
DataManagement.get_data_contry('Brazil')
DataManagement.get_data_contry('Colombia')
DataManagement.get_data_contry_by_year('Colombia', 2020)