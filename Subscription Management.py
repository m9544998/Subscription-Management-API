from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
DATABASE = "subscription.db"
def get_db():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn
def init_db():

    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_name TEXT NOT NULL,
        monthly_price INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()
init_db()
@app.route("/subscriptions", methods=["POST"])
def add_subscription():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Data required"
        }), 400

    service = data.get("service_name")
    price = data.get("monthly_price")

    if not service or price is None:

        return jsonify({
            "error":
            "service_name and monthly_price required"
        }), 400

    try:

        conn = get_db()

        cursor = conn.execute(
            """
            INSERT INTO subscriptions(
            service_name,
            monthly_price
            )
            VALUES(?,?)
            """,
            (service, price)
        )

        conn.commit()

        sub_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "message":
            "Subscription added",
            "subscription_id":
            sub_id
        }), 201

    except sqlite3.Error as e:

        return jsonify({
            "error":
            str(e)
        }), 500
@app.route("/subscriptions", methods=["GET"])
def get_subscriptions():

    try:

        conn = get_db()

        rows = conn.execute(
            "SELECT * FROM subscriptions"
        ).fetchall()

        conn.close()

        return jsonify([
            dict(row)
            for row in rows
        ])

    except sqlite3.Error as e:

        return jsonify({
            "error":
            str(e)
        }), 500
@app.route("/subscriptions/<int:id>", methods=["GET"])
def get_subscription(id):

    try:

        conn = get_db()

        row = conn.execute(
            """
            SELECT *
            FROM subscriptions
            WHERE id=?
            """,
            (id,)
        ).fetchone()

        conn.close()

        if row is None:

            return jsonify({
                "error":
                "Subscription not found"
            }), 404

        return jsonify(
            dict(row)
        )

    except sqlite3.Error as e:

        return jsonify({
            "error":
            str(e)
        }), 500

@app.route("/subscriptions/<int:id>", methods=["DELETE"])
def delete_subscription(id):

    try:

        conn = get_db()

        conn.execute(
            """
            DELETE FROM subscriptions
            WHERE id=?
            """,
            (id,)
        )

        conn.commit()

        conn.close()

        return jsonify({
            "message":
            "Subscription deleted"
        })

    except sqlite3.Error as e:

        return jsonify({
            "error":
            str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)