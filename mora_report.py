import os
import time
import random
import numpy as np
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
