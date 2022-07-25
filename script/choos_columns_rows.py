

class CreateColumnsRows:
    def creating_cl(self,row_nb,first_col, last_col,dt):
        return dt[row_nb,first_col:last_col]

    def creating_rw(self,col_nb,first_row,last_row,dt):
        return (dt[first_row:last_row,col_nb])