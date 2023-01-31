import pandas as pd
import numpy as np
import random

# 出拳選項
options = ["rock", "paper", "scissors"]

# Q-learning參數
Max_Episodes = 100   #回合數

#勝率
Win_time=0

#產生矩陣檔案
# 檢查檔案是否存在
try:
    # 讀取csv檔案並轉換為pandas矩陣
    weights = pd.read_csv("learning_Data.csv",index_col=0)
    learning_Data = pd.DataFrame(weights, index=options, columns=options)

except FileNotFoundError:
    # 生成矩陣並建立新檔案
    weights = [[0,0,0],[0,0,0],[0,0,0]]
    """[
    [random.randint(1,100), random.randint(1,100), random.randint(1,100)],
    [random.randint(1,100), random.randint(1,100), random.randint(1,100)],
    [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    ]"""
    #weights = np.zeros((3,3))
    learning_Data = pd.DataFrame(weights, index=options, columns=options)
    learning_Data.to_csv("learning_Data.csv", index=True)#true
    weights = pd.read_csv("learning_Data.csv",index_col=0)
    print(learning_Data)

for int in range(Max_Episodes):

    # 先出方隨機出拳
    first_hand = random.choice(options)
    print("先出方出拳: ", first_hand)

    # 後出方根據先出方出拳加上先前學習的經驗矩陣機率隨機選擇出拳
    try:
        second_hand = random.choices(options, weights[first_hand])
        second_hand = random.choice(second_hand)    
    except:
        second_hand = random.choice(options)    
    print("後出方出拳: ", second_hand)

    # 將每次猜拳結果輸入矩陣
    if first_hand == second_hand:
        result = "tie"
        weights.loc[first_hand, second_hand] += 1
        #print("Result is "+result)

    elif (first_hand == "rock" and second_hand == "scissors") or (first_hand == "scissors" and second_hand == "paper") or (first_hand == "paper" and second_hand == "rock"):
        weights.loc[first_hand, second_hand] += 1
        #print("Winner is player1")

    elif(first_hand == "scissors" and second_hand == "rock") or (first_hand == "paper" and second_hand == "scissors") or (first_hand == "rock" and second_hand == "paper"):
        weights.loc[first_hand, second_hand] += 100
        Win_time += 1
        #print("Winner is player2")

    else:
        print("格式錯誤")
        #weights.loc[first_hand, second_hand] += 1

#如果矩陣內元素大於1000則全部除以10
'''for i in weights:
    for j in i:
        if(i>1000):
            weights=round(weights/10)'''

#輸出結果
print( "勝率 : " + str(Win_time/Max_Episodes*100) + "%" )

# 將矩陣輸出至csv文件內
learning_Data = pd.DataFrame(weights, index=options, columns=options)
learning_Data.to_csv('learning_Data.csv', index=True)


