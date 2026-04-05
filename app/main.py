from db import get_connection
from generator import generate_log

def insert_log():
	conn = get_connection()
	cur = conn.cursor()

	log = generate_log()

	query = """
	INSERT INTO logs (user_id, page)
	VALUES (%s, %s)
	"""

	cur.execute(query, (log["user_id"], log["page"]))

	conn.commit()
	cur.close()
	conn.close()

if __name__ == "__main__":
	for _ in range(10):
		insert_log()