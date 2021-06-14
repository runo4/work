from stopwatch import measure_time2


# 数独問題を表す2次元配列を定義（空欄を0に設定）
TABLE1 = [[9, 0, 6, 7, 0, 5, 4, 0, 2],
          [0, 0, 0, 6, 9, 4, 0, 0, 0],
          [4, 0, 7, 0, 3, 0, 5, 0, 9],
          [2, 5, 0, 3, 7, 1, 0, 8, 6],
          [0, 7, 3, 5, 6, 9, 1, 2, 0],
          [1, 6, 0, 4, 8, 2, 0, 5, 7],
          [7, 0, 1, 0, 2, 0, 6, 0, 5],
          [0, 0, 0, 1, 4, 6, 0, 0, 0],
          [6, 0, 8, 9, 0, 7, 2, 0, 1]]

# 高難度版テーブル
TABLE2 = [[0, 0, 0, 0, 1, 0, 9, 2, 0],
          [0, 6, 0, 0, 5, 0, 0, 0, 0],
          [0, 7, 1, 0, 0, 0, 0, 5, 0],
          [0, 2, 0, 0, 0, 6, 3, 1, 0],
          [0, 0, 0, 7, 0, 0, 0, 0, 9],
          [9, 3, 0, 4, 0, 0, 0, 0, 5],
          [3, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 5, 0, 0, 7],
          [1, 0, 0, 3, 6, 2, 0, 0, 0]]

# 全部埋まった想定のテーブル
TABLE_COMP = [[1 for i in range(9)] for j in range(9)]


# m行n列のセルに数値kを入れたとき、そのkが条件を満たすか判定する関数
def check_cell(t, m, n):
    n_set1, n_set2, n_set3 = set(), set(), set()
    # 行に対してのチェック
    for cell in t[m]:
        if cell != 0:
            n_set1.add(cell)
    # 列に対してのチェック
    for r in t:
        if r[n] != 0:
            n_set2.add(r[n])
    # エリアに対してのチェック
    for a in range(3 * (m // 3), 3 * (m // 3) + 3):
        for b in range(3 * (n // 3), 3 * (n // 3) + 3):
            if t[a][b] != 0:
                n_set3.add(t[a][b])
    # これら3つのsetの和集合を取る
    n_union = n_set1.union(n_set2, n_set3)
    # 差集合をとり、まだ使われていない数字を取得
    n_not_used = {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(n_union)
    # m, nに入りうる数字の集合を返す
    return n_not_used


# 一番左上の空欄を取得する関数
def find_next_blank(t):
    for i, items in enumerate(t):
        for j, item in enumerate(items):
            if item == 0:
                # 順にマス目を調べ、0が初めてあった座標を返す
                return i, j
    # 81マスの中に一度も0がなければ(-1, -1)を返す
    return -1, -1


# 数独を解く関数
def do(t):
    r, c = find_next_blank(t)
    # rに-1が格納されていれば、数独完成済み
    if r == -1:
        return True
    # 1 ~ 9の数字を順番にcheck_cell()関数で判定
    for num in range(1, 10):
        # 条件を満たしていればnumを格納
        if num in check_cell(t, r, c):
            t[r][c] = num
            # do()関数自身を呼び出し
            if do(t):
                return True
            t[r][c] = 0
    # 1 ~ 9まで一つも条件を満たさなければ戻るためFalseを返す
    return False


# 完成したTABLEが実際に正しいかどうかを判定する関数
def check_table(t):
    status = True
    for r in range(9):
        for c in range(9):
            # この関数は第4引数の数値が使われていない数字かどうかを判定するため
            # 一度でもTrue -> 完成済みTABLEのどこかに重複が発生している
            if t[r][c] in check_cell(t, r, c):
                status = False
    return status


# 数独テーブルを表示する関数
def display_table(t):
    for _ in t:
        print(_)


# 実行部分
# 未完成状態の数独の表示
display_table(TABLE1)
# 数独を解く
print("↓")
print("処理時間 : " + measure_time2(do, TABLE1))
# 完成後の数独の表示
display_table(TABLE1)
# check_table()関数で完成後の数独が適切な状態かチェック
w = "この解答は正しいです。" if check_table(TABLE1) else "この解答は正しくありません"
print(w)
