# Subscription-Management-API
#  Subscription Management API

A professional RESTful API built using Flask and SQLite to manage subscriptions.

Users can create, view, and delelt

## Technologies Used

- Python 3
- Flask
- SQLite3
- REST API
- JSON

---

##  Project Structure

```text
subscription-management-api/
│
├── app.py
├── subscription.db
├── README.md
└── requirements.txt
```
---

Install dependencies:

```bash
pip install flask
```

Run application:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```


## Add Subscription

Request

```json
{
 "service_name":"Netflix",
 "monthly_price":2500
}
```

Response

```json
{
 "message":"Subscription added",
 "subscription_id":1
}
```

Status

```text
201 Created
```

---

## View Subscriptions

Request

```http
GET /subscriptions
```

Response

```json
[
 {
  "id":1,
  "service_name":"Netflix",
  "monthly_price":2500
 }
]
```

---

##  Get Subscription By ID

Request

```http
GET /subscriptions/1
```

Response

```json
{
 "id":1,
 "service_name":"Netflix",
 "monthly_price":2500
}
```

---

## Delete Subscription

Request

```http
DELETE /subscriptions/1
```

Response

```json
{
 "message":"Subscription deleted"
}
```

---

##  Author

**Maheen Asad**

Flask • SQLite • REST API

---

 Give this project a star on GitHub
