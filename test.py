import pandas as pd
import time
import datetime

# 団体についての情報があDBを読み込む
csv_file_path = 'DB.csv'

# テスト用の関数。(職人、金さんのプログラムに変更する予定)
def pass_db_to_next_program(db_data):
   
    # ここではデモのため、単にデータベースが渡されたことを出力
    print("Database passed to the next program.")

# メインプログラム
def main():
    while True:
        
        # 現在時刻を取得(実際に運用する際、一週目は運用を始める時刻を手入力する。一週目と二週目で条件分岐させる必要がある)
        current_time = datetime.datetime.now()
        print("curent_time",current_time)
        # 次の実行予定時刻を計算（現在時刻から12時間後。）
        #next_run_time = current_time + datetime.timedelta(hours=12)
        next_run_time = current_time + datetime.timedelta(minutes=1)
        print("next_run_time",next_run_time)
        # DBを読み込む
        db_data = pd.read_csv(csv_file_path)

    
        # 次の実行予定時刻まで待機
        while datetime.datetime.now() < next_run_time:
            # 10秒スリープ。テスト用で10秒にしているが、運用時は5分とかでよさそう。
            time.sleep(10)
        
        # DBを次のプログラムに渡す。(ここを職人、金さんのプログラムにすればいい)
        pass_db_to_next_program(db_data)

if __name__ == "__main__":
    main()