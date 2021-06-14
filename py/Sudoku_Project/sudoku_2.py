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


# m行n列のセルに格納することが可能な数字を列挙する関数
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


# 空欄を入りうる数字が少ない順にソートし、その空欄の座標と候補の集合を返す関数
def sort_blank_cell(t):
    if not find_all_blank(t):
        return -1, -1
    # 空欄に入る数字の候補リストと、空欄の座標リスト
    n_list = []
    blank_cell_list = []
    # 2つのリストに値を追加
    for blank_cell in find_all_blank(t):
        blank_cell_list.append((blank_cell[0], blank_cell[1]))
        n_list.append(check_cell(t, blank_cell[0], blank_cell[1]))
    # 数字の候補リストを、集合の要素数昇順にソートするための要素番号リストを作成
    indices = [*range(len(n_list))]
    # 要素番号リストを、n_list要素数昇順にソート
    sorted_indices = sorted(indices, key=lambda i: len(n_list[i]))
    # ソートされた要素番号をもとに、n_list, blank_cell_listもソート
    n_list_sorted = [n_list[i] for i in sorted_indices]
    blank_cell_list_sorted = [blank_cell_list[i] for i in sorted_indices]

    return blank_cell_list_sorted, n_list_sorted


# 空欄をすべて取得し、2次元配列で返す関数
def find_all_blank(t):
    blank_list = []
    for i, items in enumerate(t):
        for j, item in enumerate(items):
            if item == 0:
                blank_list.append((i, j))
    return blank_list


# 数独を解く関数、候補が少ないマス目から候補を一つずつ格納
def do_v2(t):
    blank_cell_list, n_list = sort_blank_cell(t)
    # blank_cell_listに-1が格納されていれば、数独完成済み
    if blank_cell_list == -1:
        return True
    r = blank_cell_list[0][0]
    c = blank_cell_list[0][1]
    # numを格納
    for num in n_list[0]:
        t[r][c] = num
        # do_v2()関数自身を呼び出し
        if do_v2(t):
            return True
        t[r][c] = 0
    # 一つも条件を満たさなければ戻るためFalseを返す
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
display_table(TABLE2)
# 数独を解く
print("↓")
print("処理時間 : " + measure_time2(do_v2, TABLE2))
# 完成後の数独の表示
display_table(TABLE2)
# check_table()関数で完成後の数独が適切な状態かチェック
w = "この解答は正しいです。" if check_table(TABLE2) else "この解答は正しくありません"
print(w)
