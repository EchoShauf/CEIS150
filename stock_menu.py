import matplotlib.pyplot as plt
from stock_class import DailyData, Stock
from datetime import datetime


def main():
    stock_list = []
    option = ""
    while option != "0":
        print("\nStock Menu")
        print("1 - Add Stock")
        print("2 - List Stocks")
        print("3 - Delete Stock")
        print("4 - Add Daily Stock Data")
        print("5 - Display Stock Chart")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            list_stocks(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            add_stock_data(stock_list)
        elif option == "5":
            display_chart(stock_list)
        elif option != "0":
            print("Invalid Option. Please try again.")


def add_stock(stock_list):
    option = ""
    while option != "0":
        print("----- Add Stock -----")
        symbol = input("Enter Ticker Symbol: ").upper()
        name = input("Enter Company Name: ")
        shares = float(input("Enter Number of Shares: "))
        new_stock = Stock(symbol, name, shares)  # Assuming you have a Stock class
        stock_list.append(new_stock)
        option = input("Press Enter to add another stock or 0 to stop: ")

def list_stocks(stock_list):
    print("----- Stock List -----")
    print("Symbol       Name          1      Shares")
    print("-" * 40)
    for stock in stock_list:
        print(f"{stock.symbol:<14}{stock.name:<20}{stock.shares:.2f}")
    _ = input("Press Enter to continue ***")

def delete_stock(stock_list):
    print("----- Delete Stock -----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol + " ", end="")
    print("]")
    symbol = input("Enter Symbol to Delete: ").upper()
    found = False
    for i, stock in enumerate(stock_list):
        if stock.symbol == symbol:
            stock_list.pop(i)
            found = True
            print("Deleted", symbol)
            break
    if not found:
        print("Symbol Not Found ***")
    _ = input("Press Enter to continue ***")

def add_stock_data(stock_list):
    print("----- Add Daily Stock Data -----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
            break
    if found:
        print("Ready to add data for:", symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date(mm/dd/yy),Price,Volume")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(datetime.strptime(date, "%m/%d/%y"), float(price), float(volume))
            current_stock.add_data(daily_data)  # Assuming your Stock class has an add_data method
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")
    

def display_stock_chart(stock_list, symbol):
       date = []
       price = []
       volume = []
       company = ""

       for stock in stock_list:
           if stock.symbol == symbol:
               company = stock.name
               for dailyData in stock.DataList:
                   date.append(dailyData.date)
                   price.append(dailyData.close)
                   volume.append(dailyData.volume)

       plt.plot(date, price)
       plt.xlabel('Date')
       plt.ylabel('Price')
       plt.title(company)
       plt.plot(date, price, marker='o', linestyle='-', color='blue')
       plt.show()

def display_chart(stock_list):
       print("Stock List: [", end="")
       for stock in stock_list:
           print(stock.symbol + " ", end="")
       print("]")

       symbol = input("Enter stock symbol: ").upper()
       found = False

       for stock in stock_list:
           if stock.symbol == symbol:
               found = True
               current_stock = stock

       if found:
           display_stock_chart(stock_list, symbol)
       else:
           print("Error: Symbol not found.")

       input("Press Enter to continue...")

if __name__ == "__main__":
    main()




