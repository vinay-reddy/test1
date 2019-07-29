import lxml
import pandas as pd

pd.options.display.max_columns = 10
pd.options.display.width = 5000

a= pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

print(type(a))
b = a[0]

print(type(b))

print(b.head())




'''

>>>
>>>
>>> pd.options.display.
pd.options.display.chop_threshold      pd.options.display.encoding            pd.options.display.latex               pd.options.display.max_info_rows       pd.options.display.notebook_repr_html  pd.options.display.width
pd.options.display.colheader_justify   pd.options.display.expand_frame_repr   pd.options.display.max_categories      pd.options.display.max_rows            pd.options.display.pprint_nest_depth
pd.options.display.column_space        pd.options.display.float_format        pd.options.display.max_columns         pd.options.display.max_seq_items       pd.options.display.precision
pd.options.display.date_dayfirst       pd.options.display.html                pd.options.display.max_colwidth        pd.options.display.memory_usage        pd.options.display.show_dimensions
pd.options.display.date_yearfirst      pd.options.display.large_repr          pd.options.display.max_info_columns    pd.options.display.multi_sparse        pd.options.display.unicode
>>> pd.options.display.max_columns = 10
>>> pd.options.display.width = 5000

'''