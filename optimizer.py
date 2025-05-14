# 🔧 Main script: Reads data, runs knapsack, plots results.
import argparse

def main():
    parser = argparse.ArgumentParser(description="Portfolio Optimizer")

    parser.add_argument('--capital',type=int, required=True, help='Amount of capital available for investment')
    parser.add_argument('--risk', type=int, required=True, help='Risk tolerance (0-100)')
    parser.add_argument('--assets', type=str, help='Path to the assets CSV file')
    parser.add_argument('--prices', type=str, help='Path to the prices CSV file')

    args = parser.parse_args()

    capital = args.capital
    risk = args.risk
    assets_file = args.assets
    prices_file = args.prices

    if not (assets_file or prices_file):
        print("You must provide either --assets or --prices CSV file.")
        return
    else:
        if assets_file:
            pass
        elif prices_file:
            pass
    

if __name__ ==  "__main__":
    main()