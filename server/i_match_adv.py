#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("54.153.4.14", "linkedinterest", "capstone2018", "li", charset='utf8' )
cursor = db.cursor()

#Get the first/last index
cursor.execute("SELECT user_id FROM user_info ORDER BY user_id LIMIT 1;")
id_min = cursor.fetchone()
cursor.execute("SELECT user_id FROM user_info ORDER BY user_id DESC LIMIT 1;")
id_max = cursor.fetchone()

id_min = int(id_min[0])
id_max = int(id_max[0])

for i in range(id_min, id_max+1):
	user_a_id = i
	for j in range(id_min+i, id_max+1):
		#Initialization
		i_score=0
		user_rec_gender='NULL'
		user_rec_food='NULL'
		user_rec_travel='NULL'

		user_b_id = j
		cursor.execute("SELECT user_name FROM user_info WHERE user_id = %s;" %user_a_id)
		user_a_name = cursor.fetchone()
		user_a_name = user_a_name[0]
		cursor.execute("SELECT user_name FROM user_info WHERE user_id = %s;" %user_b_id)
		user_b_name = cursor.fetchone()
		user_b_name = user_b_name[0]
		cursor.execute("SELECT user_gender FROM user_info WHERE user_id = %s;" %user_a_id)
		user_a_gender = cursor.fetchone()
		user_a_gender = user_a_gender[0]
		cursor.execute("SELECT user_gender FROM user_info WHERE user_id = %s;" %user_b_id)
		user_b_gender = cursor.fetchone()
		user_b_gender = user_b_gender[0]
		cursor.execute("SELECT user_i_gender FROM user_info WHERE user_id = %s;" %user_a_id)
		user_a_i_gender = cursor.fetchone()
		user_a_i_gender = user_a_i_gender[0]
		cursor.execute("SELECT user_i_gender FROM user_info WHERE user_id = %s;" %user_b_id)
		user_b_i_gender = cursor.fetchone()
		user_b_i_gender = user_b_i_gender[0]
		cursor.execute("SELECT user_i_food FROM user_info WHERE user_id = %s;" %user_a_id)
		user_a_i_food = cursor.fetchone()
		user_a_i_food = user_a_i_food[0]
		cursor.execute("SELECT user_i_food FROM user_info WHERE user_id = %s;" %user_b_id)
		user_b_i_food = cursor.fetchone()
		user_b_i_food = user_b_i_food[0]
		cursor.execute("SELECT user_i_travel FROM user_info WHERE user_id = %s;" %user_a_id)
		user_a_i_travel = cursor.fetchone()
		user_a_i_travel = user_a_i_travel[0]
		cursor.execute("SELECT user_i_travel FROM user_info WHERE user_id = %s;" %user_b_id)
		user_b_i_travel = cursor.fetchone()
		user_b_i_travel = user_b_i_travel[0]


		if user_a_gender == user_b_i_gender and user_b_gender == user_a_i_gender:
			i_score+=1
			user_rec_gender = 'Date'

		if user_a_i_food==user_b_i_food:
			i_score+=1
			user_rec_food = user_a_i_food

		if user_a_i_travel==user_b_i_travel:
			i_score+=1
			user_rec_travel = user_a_i_travel

		#Save data into DB
		sql = "INSERT INTO i_score (user_id_a, user_id_b, user_name_a, user_name_b, rec_gender, rec_food, rec_travel, i_user_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
		val = (user_a_id, user_b_id, user_a_name, user_b_name, user_rec_gender, user_rec_food, user_rec_travel, i_score)
		cursor.execute(sql, val)
		print user_a_id, user_b_id, user_a_name, user_b_name, user_rec_gender, user_rec_food, user_rec_travel, i_score


# Close DB connection
db.commit()
db.close()