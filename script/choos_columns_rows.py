
class CreateColumsRows:
    def select_column_from_row(self,first_col_of_row, dt):
        return dt[0,first_col_of_row:]

    def select_row_from_col(self,col_nb,last_row_of_cl,dt):
        return (dt[1:last_row_of_cl,col_nb])
