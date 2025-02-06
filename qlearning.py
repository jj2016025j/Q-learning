import random
import numpy as np
from config import OPTIONS, EPSILON, ALPHA, GAMMA

def choose_action(q_table, state, episode, max_episodes):
    """
    AI 根據 Q-table 選擇出拳:
    - 以 ε-greedy 策略決定是否隨機探索 (EPSILON 初始高，隨時間遞減)
    - 若非探索模式，則選擇目前 Q 值最高的出拳
    """
    # 計算當前 ε-greedy 值，隨著訓練回合數降低探索機率
    epsilon = max(0.1, 0.9 - (episode / max_episodes))  # 逐步降低隨機探索

    if random.uniform(0, 1) < epsilon:
        return random.choice(OPTIONS)  # 隨機探索
    else:
        return q_table.loc[state].idxmax()  # 根據學習數據選擇最佳動作

def update_q_table(q_table, state, action, reward, next_state):
    """
    使用 Q-learning 公式更新 Q-table:
    Q(s, a) = Q(s, a) + α * (r + γ * max(Q(s', a')) - Q(s, a))
    """
    q_value = q_table.loc[state, action]
    max_next_q = q_table.loc[next_state].max()

    # 增強獎勵強度，讓 AI 更快學習
    if reward == 1:
        reward = 5  # 獎勵勝利更多分
    elif reward == -1:
        reward = -5  # 懲罰失敗更多分

    new_q_value = q_value + ALPHA * (reward + GAMMA * max_next_q - q_value)

    # 更新 Q-table
    q_table.loc[state, action] = new_q_value
    return q_table
