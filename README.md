## INITIALIZATION

Create folder named ".config".
```
mkdir .config
``` 
Inside it put your google Sheet json service account and txt file named "password" with postgres user password inside.

Then run next command: 
```
python models.py
```
Now you are ready to start main part.

## Parsing

To get data from link, run command:
```
python main.py
```
Received information will be stored in the database.

## Google Sheet

To write stored in db data, at first you need to change google_sheet_name and worksheet_name in models.py to your names.
After that, run next:

```
python google_sheet.py
```

There is a limit on the number of requests on Google Sheet API, so first row will n`t be filled automatically.
