import pandas
import pandas as pd
from suds.client import Client
import json
import datetime as dt

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
                                    ordinal=1, duration="DAILY", getFlags=False, beginDate='2021-01-28',
                                    endDate='2021-03-10', alwaysReturnDailyFeb29=False)

    return result


data = get_data("TMAX")
print(data)
master_lst = []

for site in data:
    start_date = site[0]
    station_id = site[3]
    c = 1
    dates = []
    values = []
    for value in site[4]:
        days = dt.timedelta(c)
        date = dt.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") + days
        dates.append(date)
        values.append(value)
        c += 1
    master_lst.append({
        'station': station_id,
        'dates': dates,
        'values': values
    })

#print(pandas.DataFrame(master_lst[0]))

