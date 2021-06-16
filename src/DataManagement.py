import pandas as pd

data = pd.read_csv('./sa_data_out.csv')
data_case = pd.read_csv('./sa_data_cases_out.csv')

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
    def get_sum_country(country):
        return data[country].sum()
        
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
    def get_data_case_contry(country):
        '''return a list of years by country name'''
        if country in data_case:
            return data_case[country].tolist();
        else:
            return [];
    def get_data_case_contry_by_year(country, year):
        '''return a list by country and by year'''
        if year in data_case.Year.values:
            return data_case.loc[data["Year"] == year][country];
        else:
            return [];
    def global_case_values():
        '''return max and min global, but min general is 0'''
        tmp = [data_case.Argentina.sum(), data_case.Bolivia.sum(), data_case.Brazil.sum(), data_case.Chile.sum(), data_case.Colombia.sum(), data_case.Ecuador.sum(), data_case.Guyana.sum(), data_case.Paraguay.sum(), data_case.Peru.sum(), data_case.Suriname.sum(), data_case.Uruguay.sum(), data_case.Venezuela.sum()]
        return max(tmp), min(tmp);
    
    def get_case_sum_country(country):
        return data_case[country].sum()
    
    def max_min_case_by_country(country):
        '''return max and min value by country'''
        if country in data_case:
            return data_case[country].max(), data_case[country].min()
        else:
            return []
    def max_min_case_by_country_by_year(country,year):
        '''return max and min value by country'''
        if year in data_case.Year.values:
            return data_case.loc[data_case["Year"] == year][country].max(), data_case.loc[data_case["Year"] == year][country].min()
        else:
            return []



'''DataManagement.get_data_contry('Peru')
DataManagement.get_data_contry('aeru')
DataManagement.get_data_contry('Brazil')
DataManagement.get_data_contry('Colombia')
print(DataManagement.max_min_by_country_by_year('Colombia', 2020))
#print(DataManagement.global_values())
print(DataManagement.max_min_by_country('Peru'))'''