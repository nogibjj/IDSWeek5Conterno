"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work
 well

food dataset
"""
import requests
urlTemp = "https://gist.githubusercontent.com/tiangechen/"
urlTemp+="b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv"
def extract(url=urlTemp, 
            file_path="data/movies.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



