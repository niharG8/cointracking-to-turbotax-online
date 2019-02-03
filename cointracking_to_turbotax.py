import pandas as pd
import argparse
from pathlib import Path


def convert_to_ttax(ct_csv_path:Path) -> None:
    # Load in the CSV
    dateparse = lambda x: pd.datetime.strptime(x, '%d.%m.%Y')
    df = pd.read_csv(ct_csv_path, parse_dates=['Date Sold', 'Purchase Date'], date_parser=dateparse)

    # Create the new columns
    asset_name = df['Amount'].apply(str) + ' ' + df['Currency Name']
    DATE_FMT = '%m/%d/%Y'
    received_date = df['Purchase Date'].dt.strftime(DATE_FMT)
    date_sold = df['Date Sold'].dt.strftime(DATE_FMT)
    strip_commas = lambda x: x.replace(',', '')
    cost_basis_usd = pd.to_numeric(df['Cost Basis'].apply(strip_commas))
    proceeds = pd.to_numeric(df['Proceeds'].apply(strip_commas))

    # Assemble the output dataframe
    df_out = pd.DataFrame({'Asset name': asset_name, 'Received Date': received_date, 'Cost Basis (USD)': cost_basis_usd,
                           'Date sold': date_sold, 'Proceeds': proceeds})
    df_out = df_out[['Asset name', 'Received Date', 'Cost Basis (USD)', 'Date sold', 'Proceeds']]  # reorder columns
    df_out.set_index('Asset name', inplace=True)  # eliminates the default numeric index

    # Output to CSV
    out_path = ct_csv_path.parent / 'turbotax_online_2018_crypto_report.csv'
    df_out.to_csv(out_path, float_format='%.2f')
    print('Succesfully converted to TurboTax Online 2018 format')


def parse_cli() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    return Path(parser.parse_args().input_path)

if __name__ == '__main__':
    convert_to_ttax(parse_cli())
