# cointracking-to-turbotax-online
Python script to transform cointracking.info tax reports into a format that TurboTax Online accepts

## Instructions
1. Create your cointracking.info Tax-Report
2. From cointracking.info, view your report and click `CSV Download` and save your CSV locally
3. Run `python3 cointracking-to-turbotax path/to/downloaded_file.csv` to generate a new file, `turbotax_online_2018_crypto_report.csv` alongisde the original
4. In Turbotax Online 2018, under Wages & Income -> Cryptocurrency, select `Bitcoin.tax` as your crypto platform, and upload the `turbotax_online_2018_crypto_report.csv` file
5. Verify all of the entries look correct

## Known Limitations
* Turbotax Online 2018 only supports 250 transactions. If the output from cointracking.info has too many rows, Turbotax may reject it.
