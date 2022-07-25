from output import OutputBlocs
from read import data_final

output = OutputBlocs(1,2,14,data_final).adding_col_and_row()
print(output[0:21])
