# 🤖 剪刀、石頭、布 AI（Q-learning）

本專案使用 **Q-learning** 讓 AI 學習剪刀、石頭、布，並根據學習數據來決定最佳策略。
已經可以讓AI勝率平均超過**70%**

---

## 📌 如何運行？

### 1. 安裝必要套件
```bash
pip install pandas numpy
```
### 2. 執行 AI 訓練
```bash
python main.py
系統將自動進行 100 次對戰，並更新 learning_data.csv 學習數據。
```
### 📂 專案架構
```bash
rock-paper-scissors-ai/
│── main.py               # 啟動遊戲
│── qlearning.py          # Q-learning 核心算法
│── game.py               # 遊戲邏輯
│── data_handler.py       # CSV 數據處理
│── config.py             # 參數設定
│── README.md             # 使用說明
│── learning_data.csv     # 學習數據（第一次執行會自動建立）
```
### 🎯 Q-learning 機制
我們使用 Q-learning 來更新學習數據：
```bash
java
Q(s, a) = Q(s, a) + α × [r + γ × max(Q(s', a')) - Q(s, a)]
s (state)： 目前狀態（player1 出的拳）
a (action)： AI 決定出的拳
r (reward)： 獎勵值（輸 -1、贏 +1、平手 0）
α (learning rate)： 0.1（學習率）
γ (discount factor)： 0.9（獎勵折扣因子）
這樣 AI 會逐步學習哪些出拳方式最容易獲勝！💡
```
### 🏆 結果
隨著 AI 進行越多場比賽，它會根據數據學習到：

玩家 最常 出什麼拳
什麼拳最有可能贏過玩家
最終 AI 會越來越強，變得幾乎無法擊敗！🚀

### 📞 聯絡方式
如果有任何問題，請聯繫 [jj2016025j@gmail.com] 或開啟 GitHub Issue。