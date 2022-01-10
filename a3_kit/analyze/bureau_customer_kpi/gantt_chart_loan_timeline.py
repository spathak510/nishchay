import plotly.express as px
import plotly
import pandas as pd
import plotly.figure_factory as ff
from datetime import datetime

df=pd.read_excel(r".\ds.xlsx")
df=df.sort_values('Disbursed Amount')

start_dates=[i.date() for i in df['Start Date']]
end_dates=[i.date() for i in df['Current Date']]
amt=df['Disbursed Amount']
types=df['Loan Type']

df_chart=pd.DataFrame()
df_chart['Task']=amt
df_chart['Start']=start_dates
df_chart['Finish']=end_dates
df_chart['Resource']=types

fig = ff.create_gantt(df_chart,  index_col='Resource', 
                      showgrid_x=True, showgrid_y=False,title='Loan Timeline',
                      show_colorbar=True, bar_width=0.25)
fig.layout.xaxis.tickformat = '%b-%y'

plotly.offline.plot(fig,filename=r".\test.html")