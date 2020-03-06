closing_price_sum = 0 

with open('data/SPY.csv') as f:
    content = f.readlines()[-200:]
    for line in content:
        print(line)
        tokens = line.split(",")
        close = tokens[4]

        closing_price_sum += float(close)

print("200 MA: ", (closing_price_sum / 200))