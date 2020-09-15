# Run the script to generate the houses.csv file

cd ~/personal/linear_regression || exit 1

# make generate_csv.py executable
chmod +x generate_csv.py

# generate csv file
houses.csv << ./generate_csv.py || exit 1

chmod +x regression_model.py

# Run the regression model with the above  csv file as argument
./regression_model.py --csv_file "$houses.csv" || exit 1




