def main():
    market_file = open("intro project/market.csv", "r")
    returns_file = open("intro project/returns.csv", "w")
    with market_file, returns_file:
        market_prices = market_file.readlines()
        monthly_prices = [yearly_outlook.split(",") for yearly_outlook in market_prices]
        returns_file.write("Period,^GSPC,NVDA,AAPL,KO,MCD,MS\n") # Exchange header
        for index, exchanges in enumerate(monthly_prices[1:-1]):
            returns_line = [monthly_prices[index+2][0]] # the title of the next month
            for return_index, current_return in enumerate(exchanges[1:]):
                next_month_return = monthly_prices[index+2][return_index+1]
                returns_line.append( str(float(next_month_return)/float(current_return)-1) )
            returns_file.write(",".join(returns_line)+"\n")
            
            
                
                
            
        

if __name__ == "main":
    main()
