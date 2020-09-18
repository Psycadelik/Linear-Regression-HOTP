cd ~/personal/linear-regression/

# make generate_csv.py executable
#chmod +x generate_csv.py

# generate csv file
python generate_csv.py >> houses_data.csv || exit 1
