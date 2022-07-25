import numpy as np

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
