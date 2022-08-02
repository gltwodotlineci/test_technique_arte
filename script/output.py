import numpy as np
from choos_columns_rows import CreateColumsRows
from chaines import TransposingBlocs
from itertools import repeat

class OutputBlocs:
    def __init__(self, col_nb, first_col_of_row, col_periode, step, dt):
        self.col_nb = col_nb
        self.first_col_of_row = first_col_of_row
        self.col_periode = col_periode
        self.step = step
        self.dt = dt

    last = []
    new_list=[]
    def adding_titles(self):
        last_row_of_col = self.step+1
        return np.append( ["Mois","Chaines"],CreateColumsRows().select_row_from_col(self.col_nb,last_row_of_col,np.array(self.dt)))

    def adding_col_and_row(self):
        x = TransposingBlocs(self.step,np.array(self.dt)).transpos_fc()
        y = CreateColumsRows().select_column_from_row(self.first_col_of_row,np.array(self.dt))
        z = CreateColumsRows().select_periodes(self.col_periode,np.array(self.dt))[1:]

        for k in range(len(z)):
            self.new_list.append([z[k] for l in range(len(y))])
        print(self.new_list)

        for i in range(len(x)):
            for j in range(len(y)):
                self.last.append(np.append(x[j],x[i][j]))

        return np.array(np.vstack([self.adding_titles(), self.last]))
