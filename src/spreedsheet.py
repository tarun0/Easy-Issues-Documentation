import pygsheets
import sched, time
import terminal_print
import user_data
from oauth2client.service_account import ServiceAccountCredentials

class Sheet():

  def __init__(self, list_of_records):
    self.config = user_data.Config()
    self.list_of_records = list_of_records
    self.sheet = self.get_sheet()
    self.s = sched.scheduler(time.time, time.sleep)

  def create_table(self):
    print("\nCreating a table")
    self.create_header()
    self.insert_rows_into_sheet()
    if self.config.get('sheet', 'status', 'colorize'):
      try:
        self.try_to_colorize_status_cells()
      except Exception as e:
        print('--Error: couldn\'t colorize cells. Code:', e)

  def create_header(self):
    print("-Creating a header")
    self.sheet.clear()
    row_data = self.config.get('sheet', 'header_rows')
    self.sheet.update_cells('A1:D1', row_data)

  def insert_rows_into_sheet(self):
    print("-Inserting rows of data into sheet")
    self.sheet.update_cells('A2', self.list_of_records)

  def try_to_colorize_status_cells(self):
    print('-Colorizing status cells')
    status_col = 'C{}'
    data_starting_index = 2
    for n in range(len(self.list_of_records)):
      col_coord = status_col.format(n + data_starting_index)

      while True:
        try:
          self.s.enter(0, 0, self.colorize_cell_by_its_status, (col_coord, col_coord))
          self.s.run()
          break
        except Exception as e:
           print('--Error: couldn\'t colorize cell - api exhausted. Trying to send request again')
      
  def colorize_cell_by_its_status(self, col_coord, cell_coord):
    value = self.sheet.get_value(cell_coord)
    if 'error' not in value:
      cell = self.sheet.cell(col_coord)
      bgr_color = self.config.get('sheet', 'status', value, 'background_color')
      cell.color = (float(bgr_color[0]),
        float(bgr_color[1]),
        float(bgr_color[2]),
        float(bgr_color[3]))
      cell.update()

  def get_sheet(self):
    c = pygsheets.authorize(outh_file='./user_data/client_secret.json')
    sheet_name = self.config.get('sheet', 'name')
    sh = c.open(sheet_name)
    return sh.sheet1