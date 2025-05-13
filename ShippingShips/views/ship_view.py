import sqlite3
import json


def update_ship(id, ship_data):
    with sqlite3.connect("./shipping.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Ship
                SET
                    name = ?,
                    hauler_id = ?
            WHERE id = ?
            """,
            (ship_data["name"], ship_data["hauler_id"], id),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False


def delete_ship(pk):
    with sqlite3.connect("./shipping.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        DELETE FROM Ship WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False


def list_ships(url):
    print(f"URL received: {url}")
    print(f"Query params: {url.get('query_params', {})}")
    # Open a connection to the database
    with sqlite3.connect("./shipping.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Check if _expand parameter exists and contains 'hauler'
        expand_param = url.get("query_params", {}).get("_expand", [])
        print(f"expand_param: {expand_param}, type: {type(expand_param)}")
        should_expand = False

        # Handle both cases: when _expand is a list or a string
        if isinstance(expand_param, list) and "hauler" in expand_param:
            should_expand = True
        elif expand_param == "hauler":
            should_expand = True

        print(f"Should expand: {should_expand}")

        # Write the SQL query to get the information you want
        if should_expand:
            db_cursor.execute(
                """
                SELECT
                    s.id,
                    s.name,
                    s.hauler_id,
                    h.id as haulerId,
                    h.name as haulerName,
                    h.dock_id
                FROM Ship s
                JOIN Hauler h
                    ON h.id = s.hauler_id
                """
            )
            query_results = db_cursor.fetchall()
            print(f"Query returned {len(query_results)} rows with expansion")

            ships = []
            for row in query_results:
                hauler = {
                    "id": row["haulerId"],
                    "name": row["haulerName"],
                    "dock_id": row["dock_id"],
                }
                ship = {
                    "id": row["id"],
                    "name": row["name"],
                    "hauler_id": row["hauler_id"],
                    "hauler": hauler,
                }
                ships.append(ship)

        else:
            db_cursor.execute(
                """
                SELECT id, name, hauler_id FROM Ship
            """
            )
            query_results = db_cursor.fetchall()
            ships = [dict(row) for row in query_results]

        serialized_ships = json.dumps(ships)
        return serialized_ships


def retrieve_ship(pk, url=None):
    try:
        with sqlite3.connect("./shipping.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            expand_param = url.get("query_params", {}).get("_expand", []) if url else []
            should_expand = False

            if isinstance(expand_param, list) and "hauler" in expand_param:
                should_expand = True
            elif expand_param == "hauler":
                should_expand = True

            if should_expand:
                db_cursor.execute(
                    """
                    SELECT
                        s.id,
                        s.name,
                        s.hauler_id,
                        h.id as haulerId,
                        h.name as haulerName,
                        h.dock_id
                    FROM Ship s
                    JOIN Hauler h
                        ON h.id = s.hauler_id
                    WHERE s.id = ?
                    """,
                    (pk,),
                )
                row = db_cursor.fetchone()

                if row:
                    # Create the hauler dictionary
                    hauler = {
                        "id": row["haulerId"],
                        "name": row["haulerName"],
                        "dock_id": row["dock_id"],
                    }

                    # Create the ship dictionary with nested hauler
                    ship = {
                        "id": row["id"],
                        "name": row["name"],
                        "hauler_id": row["hauler_id"],
                        "hauler": hauler,
                    }

                    serialized_ship = json.dumps(ship)
                else:
                    return json.dumps({"error": "Ship not found"})
            else:
                db_cursor.execute(
                    """
                    SELECT id, name, hauler_id 
                    
                    FROM Ship
                    WHERE id = ?
                    """,
                    (pk,),
                )
                row = db_cursor.fetchone()

                if row:
                    ship = dict(row)
                    serialized_ship = json.dumps(ship)
                else:
                    return json.dumps({"error": "Ship not found"})

            return serialized_ship

    except Exception as e:
        print(f"Error in retrieve_ship: {str(e)}")
        return json.dumps({"error": str(e)})


def add_ship(ship_data):

    # Connect to the database
    with sqlite3.connect("./shipping.db") as conn:
        # Create a cursor to execute SQL
        cursor = conn.cursor()

        # Insert the new ship record
        cursor.execute(
            "INSERT INTO Ship (name, hauler_id) VALUES (?, ?)",
            (ship_data["name"], ship_data["hauler_id"]),
        )

        # Save the changes
        conn.commit()

        # Return True to indicate success
        return True
