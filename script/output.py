import numpy as np
from choos_columns_rows import CreateColumsRows
from chaines import TransposingBlocs

class OutputBlocs:
    def __init__(self, col_nb, first_col_of_row, step, dt):
        self.col_nb = col_nb
        self.first_col_of_row = first_col_of_row
        self.step = step
        self.dt = dt

    last = []
    def adding_titles(self):
        last_row_of_col = self.step+1
        return np.append("Chaines",CreateColumsRows().select_row_from_col(self.col_nb,last_row_of_col,np.array(self.dt)))

    def adding_col_and_row(self):
        x = TransposingBlocs(self.step,np.array(self.dt)).transpos_fc()
        y = CreateColumsRows().select_column_from_row(self.first_col_of_row,np.array(self.dt))

        for i in range(len(x)):
            for j in range(len(y)):
                self.last.append(np.append(y[j],x[i][j]))
        return np.array(np.vstack([self.adding_titles(), self.last]))
