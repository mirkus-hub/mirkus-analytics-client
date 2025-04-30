#%%
import pandas as pd
from  MirKusAnalytics.db import DBConnection
import MirKusAnalytics.dataModels as dm
from os import environ
from dotenv import load_dotenv
#%%
# CONNECT TO MIRKUS ANALYTICS
load_dotenv()
server = environ.get('SERVER')
password = environ.get('PASSWORD')
username = environ.get('USERNAME')
mirkus = DBConnection(username, password, server)
#%%
# LOAD INFORMATION
project: dm.Project = mirkus.getMirKusData('Project')
strategies: dm.Strategy = mirkus.get('Select * from [da_view].[Strategy]')
print(project.project)
print(strategies)

#%%

