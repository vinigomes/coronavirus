import pandas as pd
import plotly.express as px
from datetime import date


def show_confirmed_coronavirus_cases_in_brazil(covid):
    # Filter to Cases in Brazil
    brazil = covid.loc[(covid['Country_Region']) == 'Brazil']
    # Filter to present just cases confirmed
    brazil = brazil.loc[(brazil['Case_Type']) == 'Confirmed']
    # Convert date field to datetime
    brazil['Date'] = pd.to_datetime(brazil.Date)
    # Filter to present just data after first confirmed case
    brazil = brazil.loc[(brazil['Date']) >= pd.Timestamp(date(2020, 2, 25))]
    # Sort to present in a timeline view
    brazil = brazil.sort_values(by='Date')
    # Convert again de date field to String to be present in scatter_geo
    brazil['Date'] = brazil['Date'].apply(lambda x: x.strftime('%d/%m/%Y'))
    # Create the graphic
    fig = px.scatter_geo(brazil,
                         locations="Country_Region",
                         locationmode="country names",
                         lat='Lat',
                         lon='Long',
                         color="Country_Region",
                         hover_name="Country_Region",
                         text="Cases",
                         size="Cases",
                         animation_frame="Date",
                         projection="natural earth")
    return fig


def show_confirmed_coronavirus_cases_in_world(covid):
    # Filter to present just cases confirmed
    covid = covid.loc[(covid['Case_Type']) == 'Confirmed']
    # Convert date field to datetime and sort to present in a timeline view
    covid['Date'] = pd.to_datetime(covid.Date)
    covid = covid.sort_values(by='Date')
    # Convert again de date field to String to be present in scatter_geo
    covid['Date'] = covid['Date'].apply(lambda x: x.strftime('%d/%m/%Y'))
    # Create the graphic
    fig = px.scatter_geo(covid,
                         locations="Country_Region",
                         locationmode="country names",
                         lat='Lat',
                         lon='Long',
                         color="Country_Region",
                         hover_name="Country_Region",
                         size="Cases",
                         animation_frame="Date",
                         projection="natural earth")
    return fig
