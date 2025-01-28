## Project X

### Functionality
This program allows the user to interact with our dataset that contains data about natural disasters in the United States for the past ? years.

### Using CLI
You may use the program to obtain National Risk Index data about a particular disaster in a particular county in the U.S. by running the following command, where `<disaster_name>` is the name of the disaster and `<county_name>` is the name of the county
```
python3 command_line.py --disaster --<disaster_name> --county <county_name> 
```
You can also run the following command which will retrieve the top 5 disasters that a particular county in the U.S. is most at risk of experiencing

python3 command_line.py --top5 '<county_name>'

