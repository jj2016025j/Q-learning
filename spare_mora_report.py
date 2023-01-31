import os
import random
import pandas as np
import pandas as pd

# 出拳选项
gestures = ["rock", "paper", "scissors"]
epsilon=0.9 #貪婪度 greedy
alpha=0.1   #學習率
gamma=0.9   #獎勵遞減值
Max_Episodes = 10   #回合數

#建立列表或讀取檔案
def build(player1_gesture,player2_gesture):
    #确认数据文件是否存在，如果不存在，则创建一个
    if not os.path.exists("learning_data.csv"):
        #learning_data = pd.DataFrame(columns=['player1_gesture', 'player2_gesture', 'result', 'timestamp'])
        #learning_data = pd.DataFrame(np.zeros(3,3))
        learning_data = pd.DataFrame(np.zeros(player1_gesture,player2_gesture),player1_gesture=player1_gesture)
        learning_data.to_csv("learning_data.csv", index=False)
    else:
        learning_data = pd.read_csv("learning_data.csv")
    return learning_data

    rock_rock = 100   
    rock_paper = 100
    rock_scissors = 100

    paper_rock = 100   
    paper_paper = 100
    paper_scissors = 100

    scissors_rock = 100   
    scissors_paper = 100
    scissors_scissors = 100

#後者出拳
def player2_gesture_Deside(player1_gesture):
    player2_gesture  = random.choice(gestures)
    learning_data = pd.read_csv('learning_data.csv')
    grouped = learning_data.groupby(["player1_gesture","player2_gesture"])
    print(grouped)
    #counts = grouped.size().reset_index(name="counts")
    #win_prob = counts.pivot_table(values="counts", index="player1_gesture", columns="result", aggfunc="sum")
    #weights = learning_data[learning_data["player1_gesture"] == player1_gesture]["player2_gesture"].value_counts(normalize=True)
    #player2_gesture = random.choices(gestures, weights,k=1)[0]

    # 根据学习数据随机出拳
    #导入学习数据
    weights = [0.1, 0.1, 0.1]
    player2_gesture = random.choices(gestures,weights,k=1)[0]
    return player2_gesture

#判斷結果
def determine_result(player1_gesture, player2_gesture):
    if player1_gesture == player2_gesture:
        result = "tie"
        print("Result is "+result)
    elif (player1_gesture == "rock" and player2_gesture == "scissors") or (player1_gesture == "scissors" and player2_gesture == "paper") or (player1_gesture == "paper" and player2_gesture == "rock"):
        result = "player1"
        print("Winner is "+result)
    else:
        result = "player2"
        print("Winner is "+result)
    return result

#連續猜拳
def Gesture(learning_data):
    for int in range(Max_Episodes):
        # 随机出拳
        player1_gesture  = random.choice(gestures)
        player2_gesture = player2_gesture_Deside(player1_gesture)

        # 判断结果
        result = None
        print("Player 1 chose " + player1_gesture + " and Player 2 chose " + player2_gesture)
        result = determine_result(player1_gesture, player2_gesture)

        # 创建一个空的 DataFrame 用来存储学习经验数据
        # 将学习经验数据添加到 DataFrame 中
        # 导出学习经验数据到 csv 文件
        learning_data = learning_data.append({'player1_gesture': player1_gesture, 'player2_gesture': player2_gesture, 'result': result, 'timestamp': pd.datetime.now()}, ignore_index=True)
    return learning_data

#主架構
def main():
    #建立列表或讀取檔案
    learning_data=build(gestures,gestures)
    #連續猜拳
    learning_data=Gesture(learning_data)
    learning_data.to_csv("learning_data.csv", index=False)

    print(learning_data)

main()
"""
將每次猜拳結果輸入csv文件內

根據三種結果
分別算出三種輸出獲勝的機率
並取根據獲勝機率分配權重

    wins = df[df["result"] == "player1"].shape[0]
    losses = df[df["result"] == "player2"].shape[0]
    ties = df[df["result"] == "tie"].shape[0]

    if (wins + losses + ties) > 0:
        win_rate = wins / (wins + losses + ties)
        print("Player 1 win rate: " + str(win_rate))
    else:
        print("Not enough data to calculate win rate")


#player_gesture = input("请出拳(rock/paper/scissors): ")

try:
except:
    grouped


"""

import os
import time
import random
import numpy as np
import pandas as pd

# 出拳选项
gestures = ["rock", "paper", "scissors"]
# Q-learning參數
epsilon=0.9 #貪婪度 greedy
alpha=0.1   #學習率
gamma=0.9   #獎勵遞減值
Max_Episodes = 10   #回合數

#建立列表或讀取檔案
def build(player1_gesture,player2_gesture):
    #确认数据文件是否存在，如果不存在，则创建一个
    if not os.path.exists("learning_data.csv"):
        learning_data = pd.DataFrame(columns=[player1_gesture],index=[player2_gesture])
        learning_data.to_csv("learning_data.csv", index=True)
    else:
        learning_data = pd.read_csv("learning_data.csv")
    print(learning_data)
    return learning_data

#後者出拳
def player2_gesture_Deside(player1_gesture,learning_data):
    State_Actions = learning_data.loc[0]
    State_Actions = learning_data.iloc[player1_gesture,:]
    if(np.randomuniform()>epsilon) or (State_Actions.all == 0):
        player2_gesture = np.random.choice(gestures)
    else:
        player2_gesture = State_Actions.argmax()
    return player2_gesture

#判斷結果
def determine_result(player1_gesture, player2_gesture):
    if player1_gesture == player2_gesture:
        result = "tie"
        print("Result is "+result)
    elif (player1_gesture == "rock" and player2_gesture == "scissors") or (player1_gesture == "scissors" and player2_gesture == "paper") or (player1_gesture == "paper" and player2_gesture == "rock"):
        result = "player1"
        print("Winner is "+result)
    else:
        result = "player2"
        print("Winner is "+result)
    return result

#連續猜拳
def Gesture(learning_data):
    for int in range(Max_Episodes):
        # 随机出拳
        player1_gesture  = random.choice(gestures)
        player2_gesture = player2_gesture_Deside(player1_gesture,learning_data)

        # 判断结果
        result = None
        print("Player 1 chose " + player1_gesture + " and Player 2 chose " + player2_gesture)
        result = determine_result(player1_gesture, player2_gesture)

        # 创建一个空的 DataFrame 用来存储学习经验数据
        # 将学习经验数据添加到 DataFrame 中
        # 导出学习经验数据到 csv 文件
        #learning_data = learning_data.append({'player1_gesture': player1_gesture, 'player2_gesture': player2_gesture, 'result': result, 'timestamp': pd.datetime.now()}, ignore_index=True)
    return learning_data

#主架構
def main():
    #建立列表或讀取檔案
    learning_data=build(gestures,gestures)
    print(learning_data)

    #連續猜拳
    learning_data=Gesture(learning_data)
    learning_data.to_csv("learning_data.csv", index=False)

    print(learning_data)

main()
"""

若無文件則生成文件
若有文件則讀取文件

宣告猜拳選項
建立猜拳產生矩陣檔案

先出方隨機出拳
後出方根據先出方出拳加上先前學習的經驗矩陣機率隨機選擇出拳

將每次猜拳結果輸入矩陣
再將矩陣輸出至csv文件內

根據三種結果
分別算出三種輸出獲勝的機率
並取根據獲勝機率分配權重

    wins = df[df["result"] == "player1"].shape[0]
    losses = df[df["result"] == "player2"].shape[0]
    ties = df[df["result"] == "tie"].shape[0]

    if (wins + losses + ties) > 0:
        win_rate = wins / (wins + losses + ties)
        print("Player 1 win rate: " + str(win_rate))
    else:
        print("Not enough data to calculate win rate")


#player_gesture = input("请出拳(rock/paper/scissors): ")

try:
except:
    grouped

    # Q-learning function
def q_learning(state, action):
    # Q-value
    q = matrix[state[0], state[1], action]
    # 取得下一個狀態
    next_state = get_next_state(state, action)
    # 取得reward
    reward = get_reward(state, action)
    # 更新Q-value
    matrix[state[0], state[1], action] = q + alpha * (reward + gamma * np.max(matrix[next_state[0], next_state[1]]) - q)
    return next_state
# 根据当前状态获取概率分布
def get_probabilities(state):
    row, col = state
    return matrix[row][col]

# 随机选择动作
def choose_action(state):
    probabilities = get_probabilities(state)
    actions = ['A', 'B', 'C']
    return np.random.choice(actions, p=probabilities)
# Example
current_state = (1, 0)
action = choose_action(current_state)
print(action)

# 隨機選擇動作
def choose_action(weights):
    # 計算總權重
    total_weight = np.sum(weights)
    # 隨機選取一個權重
    random_weight = random.uniform(0, total_weight)
    # 根據權重選擇動作
    for i, weight in enumerate(weights):
        random_weight -= weight
        if random_weight <= 0:
            return i

# 選擇一個動作
action = choose_action(weights[0])
print("選擇的動作:", action)

# 選擇動作的函數
def choose_action(state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        # 隨機選擇動作

# 修改矩陣中的元素
weights[first_hand][second_hand] += 1

# 猜拳遊戲迴圈
for i in range(1000):
    # 隨機選擇當前狀態
    current_state = (random.randint(0, 2), random.randint(0, 2))

    # 隨機選擇動作
    if random.uniform(0, 1) < epsilon:
        action = random.choice(options)
    else:
        action = options[np.argmax(q_table[current_state[0], current_state[1], :])]

    # 模擬對手出拳
    opponent_action = random.choice(options)

    # 根據勝負決定下一個狀態
    if action == opponent_action:
        next_state = current_state
    elif (action

# 猜拳遊戲
def play_game():
    q_matrix = load_q_matrix()
    while True:
        # 先出方隨機出拳
        first_player_choice = random.choice(options)
        print(f"first_player_choice: {first_player_choice}")
        
        # 後出方根據先出方出拳加上先前學習的經驗矩陣機率隨機選擇出拳
        second_player_choice = random.choices(options, weights=q_matrix[first_player_choice])[0]
        print(f"second_player_choice: {second_player_choice}")
        
        # 判斷遊戲結果
        if first_player_choice == second_player_choice:
            result = 'tie'
        elif (first_player_choice == 'rock' and second_player_choice == 'scissors') or \
             (first_player_choice == 'sc

#再將矩陣輸出至csv文件內
# 修改数据
learning_Data.loc[1, 'B'] = 0.5

# 更新矩陣
df.loc[len(df)] = [new_value1, new_value2, new_value3]

# 儲存至csv檔案
df.to_csv("q_table.csv", index=False)

# 將修改後的矩陣存回 CSV 檔案中
data = pd.DataFrame(weights)
data.to_csv('weights.csv', index=False)

    #learning_Data = pd.DataFrame(np.zeros(len(options),len(options)),index=options,columns=options)
    #or
    #learning_data = pd.DataFrame(columns=[options],index=[options])
    #learning_data.to_csv("learning_Data.csv", index=False)#true

    #or

    #learning_Data = pd.DataFrame(0, index=options, columns=options)
    #learning_Data.to_csv("learning_Data.csv", index=False)#true
    #or
    #weights = np.zeros((3, 3))
    #learning_Data = pd.DataFrame(weights, index=options, columns=options)
    #learning_Data.to_csv("learning_Data.csv", index=False)#true
    #or
"""
# 初始化矩阵
"""matrix = np.array([[0.1, 0.2, 0.7],
                   [0.4, 0.3, 0.3],
                   [0.6, 0.1, 0.3]])"""

