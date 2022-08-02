from output import OutputBlocs
from read import data_final
import numpy as np
from choos_columns_rows import CreateColumsRows

output = OutputBlocs(1,2,0,14,data_final).adding_col_and_row()
print(output[0:21])

column_selected = CreateColumsRows().select_periodes(0,np.array(data_final))
