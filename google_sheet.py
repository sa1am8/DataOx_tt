import gspread

google_sheet_name = "dataOx_tt"
worksheet_name = "Apartment"
json_file = ".config/google_sheet.json"


sa = gspread.service_account(filename=json_file)
sh = sa.open(google_sheet_name)

wks = sh.worksheet(worksheet_name)


from sqlalchemy.orm import sessionmaker
from postgress import engine
from models import Apartment

Session = sessionmaker(bind=engine)
session = Session()

aparts = session.query(Apartment).all()

amount = 100
for i, each in enumerate(aparts[1:amount]):
    n = i + 2
    wks.update(f'A{n}', each.id)
    wks.update(f'B{n}', each.title)
    wks.update(f'C{n}', each.img_source)
    wks.update(f'D{n}', each.bedrooms)
    wks.update(f'E{n}', each.location)
    wks.update(f'F{n}', each.description)
    wks.update(f'G{n}', each.cost)
    wks.update(f'H{n}', each.currency)
    wks.update(f'I{n}', str(each.date)[:-8])
    #print('updated')
