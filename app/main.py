from db import get_connection
from generator import generate_user, generate_log
from dml import get_all_user_ids
from psycopg2.extras import execute_values

def insert_user(count=1000):
    conn = get_connection()
    cur = conn.cursor()

    data = []
    for _ in range(count):
        user = generate_user()
        data.append((user['name'], user['age'], user['country']))

    query = """
    INSERT INTO users (name, age, country)
    VALUES (%s, %s, %s)
    """
    
    print(f"{count}개 데이터 삽입 시작 (executemany)...")
    cur.executemany(query, data)
    print("데이터 삽입 완료!")

    conn.commit()
    cur.close()
    conn.close()
	

def insert_log(count=1000000):
    # 1. DB에서 ID 가져오기
    existing_ids = get_all_user_ids()
    if not existing_ids:
        print("유저가 없습니다! 먼저 유저부터 생성하세요.")
        return
    
    # 2. 로그 생성
    logs = []
    for _ in range(count):
        log = generate_log(existing_ids)
        logs.append((log['user_id'], log['page']))

    # 3. DB 연결 및 execute_values 실행
    conn = get_connection()
    cur = conn.cursor()
    
    query = "INSERT INTO logs (user_id, page) VALUES %s"
    
    print(f"{count}개 로그 삽입 시작...")
    execute_values(cur, query, logs)
    
    conn.commit()
    cur.close()
    conn.close()
    print("로그 저장 완료!")

if __name__ == "__main__":
	insert_user()
	insert_log()