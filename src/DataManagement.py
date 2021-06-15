import pandas as pd

data = pd.read_csv('./sa_data_out.csv')

class DataManagement:
    '''Class DataManagement receive query and send data'''
    def get_data_contry(country):
        '''return a list of years by country name'''
        if country in data:
            return data[country].tolist();
        else:
            return [];
    def get_data_contry_by_year(country, year):
        '''return a list by country and by year'''
        if year in data.Year.values:
            return data.loc[data["Year"] == year][country];
        else:
            return [];
    def global_values():
        '''return max and min global, but min general is 0'''
        tmp = [data.Argentina.sum(), data.Bolivia.sum(), data.Brazil.sum(), data.Chile.sum(), data.Colombia.sum(), data.Ecuador.sum(), data.Guyana.sum(), data.Paraguay.sum(), data.Peru.sum(), data.Suriname.sum(), data.Uruguay.sum(), data.Venezuela.sum()]
        return max(tmp), min(tmp);
    def max_min_by_country(country):
        '''return max and min value by country'''
        if country in data:
            return data[country].max(), data[country].min()
        else:
            return []
    def max_min_by_country_by_year(country,year):
        '''return max and min value by country by year'''
        if year in data.Year.values:
            return data.loc[data["Year"] == year][country].max(), data.loc[data["Year"] == year][country].min()
        else:
            return []



'''DataManagement.get_data_contry('Peru')
DataManagement.get_data_contry('aeru')
DataManagement.get_data_contry('Brazil')
DataManagement.get_data_contry('Colombia')
print(DataManagement.max_min_by_country_by_year('Colombia', 2020))
#print(DataManagement.global_values())
print(DataManagement.max_min_by_country('Peru'))'''