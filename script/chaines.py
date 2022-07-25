import read
from read import data_final
from choos_columns_rows import CreateColumnsRows
import numpy as np


class Chaine:
    def __init__(self,tf1,france_2,france_3,canal_plus,arte):
        self.tf1 = tf1
        self.france_2 = france_2
        self.france_3 = france_3
        self.canal_plus = canal_plus
        self.arte = arte


class TransposingBlocs:
    def __init__(self,step,data):
        self.step = step
        self.data = data
        self.transposed_dt = []
        self.fix_list = []

    def transpos_fc(self):
        length_list = len(self.data) - self.step
        for i in range(1,length_list,self.step):
            down_part_block = i
            up_part_block = i + 14
            self.transposed_dt.append(self.data[down_part_block:up_part_block, 2:].T)
        return np.array(self.transposed_dt)

    def fixing_dt(self):
        for i in self.transpos_fc():
            for j in range(len(i)):
                self.fix_list.append(i[j])
        return np.array(self.fix_list)

class OutputBlocs:
    last = []
    def adding_titles(self,dt):
        return np.append("Chaines",CreateColumnsRows().creating_rw(1,1,15,np.array(dt)))

    def adding_col(self,dt):
        x = TransposingBlocs(14,np.array(dt)).transpos_fc()
        y = CreateColumnsRows().creating_cl(0,2,7,np.array(dt))

        for i in range(len(x)):
            for j in range(len(y)):
                self.last.append(np.append(y[j],x[i][j]))
        return np.array(np.vstack([self.adding_titles(dt), self.last]))



#print(TransposingBlocs(14,np.array(data_final)).fixing_dt())

#print(CreateColumnsRows().creating_cl(0,2,7,np.array(data_final)))

#print(CreateColumnsRows().creating_rw(1,1,15,np.array(data_final)))

print(OutputBlocs().adding_col(data_final)[0:25])
(OutputBlocs().adding_titles(data_final))




