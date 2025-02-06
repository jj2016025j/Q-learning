# 剪刀、石頭、布選項
OPTIONS = ["rock", "paper", "scissors"]

# Q-learning 參數
EPSILON = 0.9  # 貪婪度 (探索 vs. 利用)
ALPHA = 0.3    # 學習率
GAMMA = 0.9    # 折扣因子 (未來獎勵的影響力)
EPISODES = 100  # 迭代回合數
DATA_FILE = "learning_data.csv"  # 學習數據儲存檔案
