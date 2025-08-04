
count = 0
total_investment = 0
total_profit = 0
total_loss = 0
highest_profit = None
lowest_profit = None



user_name = input('Please enter your name:')
print('Welcome',user_name+ ", let's track your trades today!")

while True:
    coin_name = str(input('Enter coin name (e.g., BTC, ETH, SHIBA):'))
    if coin_name == 'done':
        break
    if coin_name.isdigit():
        print('Invalid, please enter a name not a digit!')
        continue
    try:
        buy_price = float(input('Enter buy price (Dollars):'))
        buy_quantity = float(input('Enter buy quantity (e.g., 0.5, 10, 100, 1000):'))
        sell_price = float(input('Enter sell price (Dollars):'))

        count = count + 1

        investment = (buy_price*buy_quantity)
        total_investment += investment

        profit = (sell_price - buy_price)* buy_quantity
        total_profit += profit

        if investment > 0:
            ROI = ((profit/investment)*100)
        else:
            print('ROI cannot be calculated due to zero investment! , Please enter correct value!')
            continue

        if sell_price < buy_price:
            loss = abs(profit)
            total_loss += loss
            print('Trade',count,'\n' 'Coin:',coin_name,'\n''Invested amount:','$',investment,'\n''Loss is','$'+str(loss),'\n' 'ROI is',round(ROI, 2),'%')
        else:
            print('Trade',count,'\n''Coin:',coin_name,'\n''Invested amount:','$',investment,'\n''Profit is','$'+str(profit),'\n' 'ROI is',round(ROI, 2),'%')

        if highest_profit is None or profit > highest_profit:
            highest_profit = profit
            highest_profit_coin = coin_name

        if lowest_profit is None or profit < lowest_profit:
            lowest_profit = profit
            lowest_profit_coin = coin_name
    except:
        print('Please, enter a valid value')


#Summary of Trades

if count > 0:
    print('\n''Summary')
    print('Total trades:',count)
    print('Total investment:','$',(total_investment))
    print('Total pnl:','$',(total_profit))
    print('Avg profit:','$',(total_profit/count))
    print('Highest profit trade:',highest_profit_coin,'$',(highest_profit))
    print('Lowest profit trade:',lowest_profit_coin,'$',(lowest_profit))
    print('Total ROI:',(total_profit/total_investment)*100,'%')