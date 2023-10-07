import pandas
import pandas as pd
from suds.client import Client
import json
import datetime
from datetime import datetime
from datetime import timedelta

stations_lst = ['916:MT:SNTL', '307:MT:SNTL', '311:MT:SNTL', '313:MT:SNTL', '315:MT:SNTL', '1190:MT:SNTL',
                '318:MT:SNTL', '328:MT:SNTL', '346:MT:SNTL', '347:MT:SNTL',
                '349:MT:SNTL', '1144:MT:SNTL', '355:MT:SNTL', '360:MT:SNTL', '363:MT:SNTL', '365:MT:SNTL',
                '981:MT:SNTL', '381:MT:SNTL', '385:MT:SNTL', '1312:MT:SNTL',
                '403:MT:SNTL', '407:MT:SNTL', '410:MT:SNTL', '413:MT:SNTL', '414:MT:SNTL', '427:MT:SNTL', '919:MT:SNTL',
                '433:MT:SNTL', '436:MT:SNTL', '437:MT:SNTL',
                '448:MT:SNTL', '458:MT:SNTL', '1105:MT:SNTL', '1106:MT:SNTL', '469:MT:SNTL', '480:MT:SNTL',
                '482:MT:SNTL', '487:MT:SNTL', '918:MT:SNTL', '500:MT:SNTL',
                '510:MT:SNTL', '516:MT:SNTL', '530:MT:SNTL', '1287:MT:SNTL', '562:MT:SNTL', '568:MT:SNTL',
                '576:MT:SNTL', '578:MT:SNTL', '590:MT:SNTL', '603:MT:SNTL',
                '604:MT:SNTL', '609:MT:SNTL', '613:MT:SNTL', '635:MT:SNTL', '646:MT:SNTL', '649:MT:SNTL', '656:MT:SNTL',
                '657:MT:SNTL', '903:MT:SNTL', '662:MT:SNTL',
                '664:MT:SNTL', '667:MT:SNTL', '670:MT:SNTL', '1008:MT:SNTL', '930:MT:SNTL', '690:MT:SNTL',
                '693:MT:SNTL', '696:MT:SNTL', '932:MT:SNTL', '700:MT:SNTL',
                '722:MT:SNTL', '917:MT:SNTL', '725:MT:SNTL', '929:MT:SNTL', '727:MT:SNTL', '753:MT:SNTL', '754:MT:SNTL',
                '760:MT:SNTL', '1286:MT:SNTL', '783:MT:SNTL',
                '781:MT:SNTL', '787:MT:SNTL', '1009:MT:SNTL', '1311:MT:SNTL', '901:MT:SNTL', '813:MT:SNTL',
                '893:MT:SNTL', '835:MT:SNTL', '836:MT:SNTL', '847:MT:SNTL',
                '850:MT:SNTL', '924:MT:SNTL', '858:MT:SNTL', '862:MT:SNTL']


def get_data(element):
    # collects data from 2020-2021 season
    url = "https://wcc.sc.egov.usda.gov/awdbWebService/services?WSDL"
    client = Client(url)
    result = client.service.getData(stationTriplets=['754:MT:SNTL', '307:MT:SNTL', '311:MT:SNTL'], elementCd=element,
                                    ordinal=1, duration="DAILY", getFlags=False, beginDate='1980-01-28',
                                    endDate='2021-03-10', alwaysReturnDailyFeb29=False)

    return result


# data = get_data("TMAX")


# 24 hour snowfall totals from every MT site saved in pd data frame site name: snowfall amount:

def daily_snwd():
    url = "https://wcc.sc.egov.usda.gov/awdbWebService/services?WSDL"
    client = Client(url)
    result = client.service.getHourlyData(stationTriplets= '578:MT:SNTL', elementCd="SNWD",
                                                         # 2010-01-01 22:00
                                    ordinal=1, beginDate=(datetime.now() - timedelta(hours=40)).strftime('%Y-%m-%d %H:%M'),
                                    endDate=datetime.now().strftime('%Y-%m-%d %H:%M'))

    return result

#snowfall = daily_snwd()



def daily_swe():
    url = "https://wcc.sc.egov.usda.gov/awdbWebService/services?WSDL"
    client = Client(url)
    result = client.service.getHourlyData(stationTriplets= '727:MT:SNTL', elementCd="WTEQ",
                                                         # 2010-01-01 22:00
                                    ordinal=1, beginDate=(datetime.now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M'),
                                    endDate=datetime.now().strftime('%Y-%m-%d %H:%M'))

    return result

swe = daily_swe()


for data in swe:
    start_date = data[0]
    end_date = data[1]
    time = []
    values = []
    for value in data[3]:
        time.append(value[0])
        values.append(float(value[2]))


df = pd.DataFrame(list(zip(time, values)),
               columns =['time', 'swe'])

print(df)
print((values[-1]-values[0]).__round__(3))




