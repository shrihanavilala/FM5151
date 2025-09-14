from intermediate.solutions import utils

def main():
    """Your implementation"""
    metrics_file = open("intro_project/metrics.csv", "w")
    returns_file = open("intro_project/returns.csv", "r")
    with metrics_file, returns_file:
        returns = returns_file.readlines()
        monthly_returns = [yearly_outlook.split(",") for yearly_outlook in returns] #split and ignore header title
        
        metrics_file.write("ticker,avg_return,volatility,alpha,beta\n")
        gspc_returns = [float(line[1]) for line in monthly_returns[1:]] #baseline for market returns
        returns_by_stock = [list(row) for row in zip(*monthly_returns[1:])]
        for stock_title, stock in enumerate(returns_by_stock[1:]):
            numbered = [float(return_) for return_ in stock]
            avg_return = sum(numbered)/len(numbered)
            volatility = utils.stddev(numbered)
            beta = utils.covariance(gspc_returns, numbered)/utils.variance(gspc_returns)
            alpha = avg_return - beta*(sum(gspc_returns)/len(gspc_returns))
            metrics_file.write(f"{monthly_returns[0][stock_title]},{avg_return:0.4f},{volatility:0.4f},{alpha:0.4f},{beta:0.4f}\n")
            
        
        
        
            
        
        
        


if __name__ == "__main__":
    main()
