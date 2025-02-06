import random
from config import OPTIONS, EPISODES
from qlearning import choose_action, update_q_table
from data_handler import load_learning_data, save_learning_data

def determine_winner(player1, player2):
    """
    判斷勝負規則：
    - player1 贏：return -1
    - player2 贏：return 1
    - 平手：return 0
    """
    if player1 == player2:
        return 0
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return -1  # player2 輸
    else:
        return 1  # player2 贏
    
def play_game():
    """
    進行剪刀、石頭、布遊戲，並讓 AI 持續學習，並顯示學習成效
    """
    q_table = load_learning_data()

    ai_wins = 0
    human_wins = 0
    ties = 0

    for episode in range(EPISODES):
        player1_choice = random.choice(OPTIONS)  # 隨機選擇 Player 1 出拳
        player2_choice = choose_action(q_table, player1_choice, episode, EPISODES)  # AI 選擇 Player 2 出拳
        
        # 判斷輸贏
        reward = determine_winner(player1_choice, player2_choice)

        # 更新統計數據
        if reward == 1:
            ai_wins += 1
            result = "✅ AI 勝利"
        elif reward == -1:
            human_wins += 1
            result = "❌ AI 落敗"
        else:
            ties += 1
            result = "⚖️ 平手"

        # 輸出更直觀的結果
        print(f"回合 {episode + 1}: Player 1 出 {player1_choice} | Player 2 (AI) 出 {player2_choice} → {result}")

        # 更新 Q-table
        q_table = update_q_table(q_table, player1_choice, player2_choice, reward, player1_choice)

    # 儲存學習數據
    save_learning_data(q_table)

    # 顯示最終統計結果
    print("\n🔹 最終結果 🔹")
    print(f"✅ AI 獲勝次數: {ai_wins}")
    print(f"❌ AI 落敗次數: {human_wins}")
    print(f"⚖️ 平手次數: {ties}")
    print(f"AI 勝率: {ai_wins / EPISODES * 100:.2f}%")
    print("\n✅ 訓練完成，數據已更新！")
