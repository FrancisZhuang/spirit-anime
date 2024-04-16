"""db set up"""
import sqlite3
import os
from typing import List


class Storage:
    """db class"""
    def __init__(self):
        self.current_path = os.getcwd()
        self.__db_file = os.path.join(self.current_path, 'user.db')

    def has_user_id(self, user_id: int) -> bool:
        """Check if user id exist"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('SELECT COUNT(*) FROM USER WHERE user_id = :user_id', {'user_id': user_id})
                return cursor.fetchone()[0]
        finally:
            conn.close()

    def has_user_name_dob(self, full_name: str, dob: str) -> bool:
        """Check if user's name and dob exist"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('SELECT COUNT(*) FROM USER WHERE full_name = :full_name AND '
                               'dob = :dob', {'full_name': full_name, 'dob': dob})
                return cursor.fetchone()[0]
        finally:
            conn.close()

    def add_anime_data(self, user_id, full_name, dob, char, quote, food) -> None:
        """Add user's data"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('INSERT INTO USER VALUES (:user_id, :full_name, :dob, :char, :quote, :food);',
                               {'user_id': user_id,
                                'full_name': full_name,
                                'dob': dob,
                                'char': char,
                                'quote': quote,
                                'food': food})
        finally:
            conn.close()

    def get_all_id_name(self) -> List[tuple]:
        """Get all user's id and name"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('SELECT user_id, full_name FROM USER')
                return cursor.fetchall()
        finally:
            conn.close()

    def get_info_by_id(self, user_id) -> tuple:
        """Get user's data by id"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('SELECT * FROM USER WHERE user_id = :user_id;', {'user_id': user_id})
                return cursor.fetchall()[0]
        finally:
            conn.close()

    def update_full_name(self, full_name, user_id) -> None:
        """Update user's name by id"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('UPDATE USER SET full_name = :full_name WHERE user_id = :user_id',
                               {'full_name': full_name, 'user_id': user_id})
        finally:
            conn.close()

    def update_dob(self, dob, user_id) -> None:
        """Update user's dob by id"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('UPDATE USER SET dob = :dob WHERE user_id = :user_id',
                               {'dob': dob, 'user_id': user_id})
        finally:
            conn.close()

    def update_full_name_dob(self, full_name, dob, user_id) -> None:
        """Update user's name and dob by id"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('UPDATE USER SET full_name = :full_name, dob = :dob WHERE user_id = :user_id',
                               {'full_name': full_name, 'dob': dob, 'user_id': user_id})
                return cursor.fetchall()[0]
        finally:
            conn.close()

    def delete_user(self, user_id) -> None:
        """Delete user's data by id"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('DELETE FROM USER WHERE user_id = :user_id', {'user_id': user_id})
        finally:
            conn.close()

    def delete_user_name_dob(self, full_name, dob) -> None:
        """Delete user's data by id"""
        conn = sqlite3.connect(self.__db_file)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute('DELETE FROM USER WHERE full_name = :full_name AND dob = :dob',
                               {'full_name': full_name, 'dob': dob})
        finally:
            conn.close()
