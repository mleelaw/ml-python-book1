import sqlite3
import json


def update_metal(pk, new_price):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    price = ?
            WHERE id = ?
            """,
            (new_price["price"], pk),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False
