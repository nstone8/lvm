import pandas as pd
import io
def parse_lvm(path:str)->pd.DataFrame:
    with open(path,'rt') as lvm:
        buf=io.StringIO()
        for line in lvm:
            buf.write(line)
            if line[0:3]=='***':
                #Everything before was a header, make a new buffer
                buf.close()
                buf=io.StringIO()

    buf.seek(0)
    return pd.read_csv(buf,sep='\t')
