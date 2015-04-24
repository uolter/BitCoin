__author__ = 'uolter'


from datetime import datetime, timedelta
from pandas.io.data import DataReader
import sys

FIN_SERVICE_PROVIDER = 'yahoo'
PAST_DAYS = 60


def main(symbol):

    t1 = datetime.now()
    t2 = t1 - timedelta(days=PAST_DAYS)

    df  = DataReader(symbol,  FIN_SERVICE_PROVIDER , t2, t1)
    print df.head()
    print '...' * 20
    print df.tail()

    return df


if __name__ == '__main__':

    symbol = sys.argv[1]

    main(symbol)
