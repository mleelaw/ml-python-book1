import sqlite3
import json


def list_orders():

    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            o.id,
            o.quantity,
            o.order_date,
            o.metal_id,      -- Add this
            o.customer_id,   -- Add this
            o.size_id,       -- Add this
            o.style_id, 
            m.metal,
            m.price,
            c.name as customer_name,
            c.email,
            s.size,
            st.style
        FROM Orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Customers c ON c.id = o.customer_id
        JOIN Sizes s ON s.id = o.size_id  -- Fixed: was sizes_id
        JOIN Styles st ON st.id = o.style_id
        """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:

            order = {
                "id": row["id"],
                "quantity": row["quantity"],
                "order_date": row["order_date"],
                "metal_id": row["metal_id"],
                "customer_id": row["customer_id"],
                "size_id": row["size_id"],
                "style_id": row["style_id"],
            }

        size = {"size": row["size"]}

        style = {"style": row["style"]}

        metal = {"metal": row["metal"], "price": row["price"]}

        order["size"] = size
        order["style"] = style
        order["metal"] = metal

        orders.append(order)

        serialized_orders = json.dumps(orders)

    return serialized_orders


def retrieve_order(pk):

    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                    SELECT id, quantity, order_date
                    
                    FROM Orders
                    WHERE id = ?
                    """,
            (pk,),
        )
        row = db_cursor.fetchone()

        if row:
            order = dict(row)
            serialized_order = json.dumps(order)
        else:
            return json.dumps({"error": "Order not found"})

    return serialized_order


def add_order(new_order_data):
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            "INSERT INTO Orders (customer_id, style_id, size_id, quantity, order_date, metal_id) VALUES (?, ?, ?, ?, ?, ?)",
            (
                new_order_data["customer_id"],
                new_order_data["style_id"],
                new_order_data["size_id"],
                new_order_data["quantity"],
                new_order_data["order_date"],
                new_order_data["metal_id"],
            ),
        )

        conn.commit()

        return True


def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM Orders WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

        return True if number_of_rows_deleted > 0 else False
