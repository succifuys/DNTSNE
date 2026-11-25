import random

gold = 100
army = 10
enemy = 30
turn = 1

print("=== ミニ戦略ゲーム ===")
print("敵の軍隊を倒してください！")

while army > 0 and enemy > 0:
    print("\n---", turn, "ターン ---")
    print("お金:", gold)
    print("自分の兵士:", army)
    print("敵の兵士:", enemy)
    
    print("\n1. 兵士を5人雇う（50円）")
    print("2. 税金を集める（+30円）")
    print("3. 敵を攻撃する")
    print("4. 何もしない")

    choice = input("行動を選んでください: ")

    if choice == "1":
        if gold >= 50:
            gold -= 50
            army += 5
            print("兵士を5人雇いました！")
        else:
            print("お金が足りません！")

    elif choice == "2":
        gold += 30
        print("税金を集めました！")

    elif choice == "3":
        attack = random.randint(1, army)
        defense = random.randint(1, enemy)

        enemy -= attack
        army -= defense

        print("敵を", attack, "人倒しました！")
        print("自分の兵士を", defense, "人失いました。")

    elif choice == "4":
        print("何もしませんでした。")

    else:
        print("正しい番号を入力してください！")
        continue

    # 敵は毎ターン兵士を増やす
    if enemy > 0:
        enemy += 2
        print("敵の兵士が2人増えました！")

    turn += 1

if enemy <= 0:
    print("\n勝利！おめでとうございます！")
else:
    print("\n敗北！ゲームオーバー！")