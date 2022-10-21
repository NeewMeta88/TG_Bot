import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    

    def add_user(self,user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
    
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            if result.fetchone() is None:
                return 0
            else:
                return  1

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET nickname = ? WHERE user_id = ?", (nickname, user_id,))

    def get_nickname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT nickname FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                nickname = str(row[0])
            return nickname

    def set_signup(self, user_id, signup):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_city(self, user_id, city):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET city = ? WHERE user_id = ?", (city, user_id,))

    def get_city(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT city FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                city = str(row[0])
            return city

    def set_inst(self, user_id, inst):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET inst = ? WHERE user_id = ?", (inst, user_id,))

    def get_inst(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT inst FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                inst = str(row[0])
            return inst

    def set_status(self, user_id, status):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET status = ? WHERE user_id = ?", (status, user_id,))

    def get_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT status FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                status = str(row[0])
            return status
    
    def set_gender(self, user_id, gender):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id,))

    def get_gender(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT gender FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                gender = str(row[0])
            return gender

    def set_year(self, user_id, year):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET year = ? WHERE user_id = ?", (year, user_id,))

    def get_year(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT year FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                year = str(row[0])
            return year

    def set_goro(self, user_id, goro):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET goro = ? WHERE user_id = ?", (goro, user_id,))

    def get_goro(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT goro FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                goro = str(row[0])
            return goro

    def find_user(self):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users ORDER BY RANDOM()").fetchone()
            for row in result:
                x = (str(row))
            return x

    
    # def find_user2(self, user_id):
    #     with self.connection:
    #         first_id = self.cursor.execute("SELECT user_id FROM users WHERE id = 1").fetchone()
    #         for row in first_id:
    #                 find_id = str(row[0])
    #                 print("first_id: " + find_id + "\n")
    #                 print("user_id: " + str(user_id) + "\n")
    #         if (find_id == str(user_id)):
    #             other_id = self.cursor.execute("SELECT user_id FROM users WHERE id = ?")
    #         return other_id

    def set_test(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET test = 1 WHERE user_id = ?", (user_id,))

    def clear_test(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET test = 0 WHERE user_id = ?", (user_id,))

    def get_test(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT test FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                test = str(row[0])
            return test

    def set_question(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET question = question +1 WHERE user_id = ?", (user_id,))

    def clear_question(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET question = 0 WHERE user_id = ?", (user_id,))

    def get_question(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT question FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                question = str(row[0])
            return question

    def set_test_score(self, user_id, test_score):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET test_score = test_score + ? WHERE user_id = ?", (test_score, user_id,))

    def clear_test_score(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET test_score = 0 WHERE user_id = ?", (user_id,))

    def get_test_score(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT test_score FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                test_score = str(row[0])
            return test_score

    def set_test_bool(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET test_bool = 1 WHERE user_id = ?", (user_id,))

    def clear_test_bool(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET test_bool = 0 WHERE user_id = ?", (user_id,))

    def get_test_bool(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT test_bool FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                test_bool = str(row[0])
            return test_bool

    def set_find_id(self, user_id, find_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET find_id = ? WHERE user_id = ?", (find_id, user_id,))

    def clear_find_id(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET find_id = NULL WHERE user_id = ?", (user_id,))

    def get_find_id(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT find_id FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                find_id = str(row[0])
            return find_id

    def set_alert(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT alert FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                    alert = str(row[0])
            if (alert == '1'):
                pass
            else:
                return  self.cursor.execute("UPDATE users SET alert = 1 WHERE user_id = ?", (user_id,))

    def clear_alert(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET alert = 0 WHERE user_id = ?", (user_id,))

    def get_alert(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT alert FROM users WHERE user_id = ?", (user_id,)).fetchall()
            if (result == 1):
                pass
            else:
                for row in result:
                    alert = str(row[0])
                return alert
    
    def set_sovm(self, user_id, sovm):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET sovm = ? WHERE user_id = ?", (sovm, user_id,))

    def clear_sovm(self, user_id):
        with self.connection:
            return  self.cursor.execute("UPDATE users SET sovm = 0 WHERE user_id = ?", (user_id,))

    def get_sovm(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT sovm FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                sovm = str(row[0])
            return sovm

    # def set_temp(self, user_id):
    #     with self.connection:
    #         return  self.cursor.execute("UPDATE users SET temp = temp + 1 WHERE user_id = ?", (user_id,))

    # def clear_temp(self, user_id):
    #     with self.connection:
    #         return  self.cursor.execute("UPDATE users SET temp = 0 WHERE user_id = ?", (user_id,))

    # def get_temp(self, user_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT temp FROM users WHERE user_id = ?", (user_id,)).fetchall()
    #         for row in result:
    #             temp = str(row[0])
    #         return temp



            # ТАБЛИЦА SAVE
    # def add_save(self,user_id):
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO saves (user_id) VALUES (?)", (user_id,))
