import yfinance as yf


def get_ticker_details(ticker):
    return yf.Ticker(ticker)


def get_lowest_price(stock):
    # function shall return with
    # the lowest price (:float) of the stock and
    # the corresponding day (:date) from the last 21 days
    pass


def get_highest_price(stock):
    # function shall return with
    # the highest price (:float) of the stock and
    # the corresponding day (:date) from the last 21 days
    pass


def main():
    otp = get_ticker_details("OTP.F")


if __name__ == "__main__":
    main()

