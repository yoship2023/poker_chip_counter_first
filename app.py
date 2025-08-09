import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# 前回の入力値を保存するためのキー
prev_input_key = "previous_input"

# 前回の入力値を取得する関数
def get_previous_input():
    return st.session_state.get(prev_input_key, "")

# 現在の入力値を保存する関数
def save_current_input(input_value):
    st.session_state[prev_input_key] = input_value

def poker_chip_counter():
    st.title("チップかぞえチャオ ver1")

    selected_item = st.radio(
        'カウントするチップの種類を選択して下さい',
        ['JOPT用', '一般的なリング用', 'カスタム用']
    )

    st.write("チップ数を直接入力 or 末尾-+ボタンで設定後、計算ボタンを押下")

    #初期値
    chips_01_value = 100
    chips_01_cnt = 0
    chips_02_value = 500
    chips_02_cnt = 0
    chips_11_value = 1000
    chips_11_cnt = 0
    chips_12_value = 5000
    chips_12_cnt = 0
    chips_21_value = 25000
    chips_21_cnt = 0
    chips_22_value = 100000
    chips_22_cnt = 0
    chips_31_value = 1000000
    chips_31_cnt = 0
    bb_value = 200

    if selected_item == 'JOPT用' or selected_item == '一般的なリング用':
        col_01, col_02 = st.columns(2)
        col_11, col_12 = st.columns(2)
        col_21, col_22 = st.columns(2)
        col_31, col_32 = st.columns(2)
        col_98, col_99 = st.columns([1, 6])

        if selected_item == 'JOPT用':
            # 旧ロジック
            chips_01_cnt = col_01.number_input("100点（⚫️黒いチップ）の数", min_value=0, value=0)
            chips_02_cnt = col_02.number_input("500点（🟣紫色チップ）の数", min_value=0, value=0)
            chips_11_cnt = col_11.number_input("1,000点（🔵青いチップ）の数", min_value=0, value=0)
            chips_12_cnt = col_12.number_input("5,000点（🟡黄色チップ）の数", min_value=0, value=0)
            chips_21_cnt = col_21.number_input("25,000点（🔴赤いチップ）の数", min_value=0, value=0)
            chips_22_cnt = col_22.number_input("100,000点（⚪️赤いチップ）の数", min_value=0, value=0)
            chips_31_cnt = col_31.number_input("1,000,000点（薄紫チップ）の数", min_value=0, value=0)
        else:
            chips_01_cnt = col_01.number_input("100点の数", min_value=0, value=0)
            chips_02_cnt = col_02.number_input("500点の数", min_value=0, value=0)
            chips_11_cnt = col_11.number_input("1,000点の数", min_value=0, value=0)
            chips_12_cnt = col_12.number_input("5,000点の数", min_value=0, value=0)
            chips_21_cnt = col_21.number_input("2,5000点の数", min_value=0, value=0)
            chips_22_cnt = col_22.number_input("100,000点の数", min_value=0, value=0)
            chips_31_cnt = col_31.number_input("1,000,000点の数", min_value=0, value=0)

        # BBの入力フィールド
        # 旧ロジック
        bb_value = col_32.number_input("1BBの点数", min_value=0, value=200, step=100)
    else:
        col_01, col_02 = st.columns(2)
        col_11, col_12 = st.columns(2)
        col_21, col_22 = st.columns(2)
        col_31, col_32 = st.columns(2)
        col_41, col_42 = st.columns(2)
        col_51, col_52 = st.columns(2)
        col_61, col_62 = st.columns(2)
        col_71, col_72 = st.columns(2)
        col_98, col_99 = st.columns([1, 6])

        # チップの数とBBの入力フィールド
        chips_01_value = col_01.number_input("チップ1の点数", min_value=0, value=0)
        chips_01_cnt = col_02.number_input("チップ1の枚数", min_value=0, value=0)

        chips_02_value = col_11.number_input("チップ2の点数", min_value=0, value=0)
        chips_02_cnt = col_12.number_input("チップ2の枚数", min_value=0, value=0)

        chips_11_value = col_21.number_input("チップ3の点数", min_value=0, value=0)
        chips_11_cnt = col_22.number_input("チップ3の枚数", min_value=0, value=0)

        chips_12_value = col_31.number_input("チップ4の点数", min_value=0, value=0)
        chips_12_cnt = col_32.number_input("チップ4の枚数", min_value=0, value=0)

        chips_21_value = col_41.number_input("チップ5の点数", min_value=0, value=0)
        chips_21_cnt = col_42.number_input("チップ5の枚数", min_value=0, value=0)

        chips_22_value = col_51.number_input("チップ6の点数", min_value=0, value=0)
        chips_22_cnt = col_52.number_input("チップ6の枚数", min_value=0, value=0)

        chips_31_value = col_61.number_input("チップ7の点数", min_value=0, value=0)
        chips_31_cnt = col_62.number_input("チップ7の枚数", min_value=0, value=0)

        bb_value = col_71.number_input("1BBの点数", min_value=1, value=1)

    # 計算ボタン
    if col_98.button("計算"):
        # 合計計算
        total_chips = chips_01_cnt * chips_01_value + chips_02_cnt * chips_02_value \
            + chips_11_cnt * chips_11_value + chips_12_cnt * chips_12_value \
            + chips_21_cnt * chips_21_value + chips_22_cnt * chips_22_value \
            + chips_31_cnt * chips_31_value
        # BB表記への変換
        total_bb = total_chips / bb_value
        col_99.subheader(f"合計点数： {total_chips:,} 点 ({total_bb:,.2f} BB)")

    # 現在時刻の表示
    current_time = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    # メモ欄
    memo_title = "メモ4 現在時刻（JST）：" + current_time
    memo = st.text_input(memo_title, get_previous_input())
    # memo = st.text_area(memo_title, "")
    # print(memo)
    # print("a")
    # 前回の入力値を表示
    # st.write("前回の入力値:", memo)
    # 入力値を保存
    # save_current_input(memo)
    # 前回の入力値を表示
    # st.write("前回の入力値:", get_previous_input())

    # 入力保持 表示確認
    #st.write("現在のchips_01_cnt：", st.session_state.chips_01_cnt)
    #st.write("現在のchips_01_cnt：", st.session_state["chips_01_cnt"])

    # 画面の下部にTwitterリンクを追加
    st.markdown(
    """
    ---
    Produced by Yoship.
    Follow me on X: [yoship](https://twitter.com/yoship2023)
    """,
    unsafe_allow_html=True,
    )

if __name__ == "__main__":
    poker_chip_counter()