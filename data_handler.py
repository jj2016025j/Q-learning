import os
import pandas as pd
import numpy as np
from config import OPTIONS, DATA_FILE

def load_learning_data():
    """
    讀取學習數據，如果檔案不存在，則建立新的 3x3 Q-table
    """
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE, index_col=0)
    else:
        q_table = pd.DataFrame(np.zeros((3, 3)), index=OPTIONS, columns=OPTIONS)
        q_table.to_csv(DATA_FILE)
        return q_table

def save_learning_data(q_table):
    """
    儲存學習數據到 CSV 檔案
    """
    q_table.to_csv(DATA_FILE)
    print(f"✅ 學習數據已更新，存入 {DATA_FILE}")
