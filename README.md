# data-preliminary-test

endpoint REST sederhana (accept json) untuk tabel berikut :
Nama tabel : user_review
Fields :
- id (auto increment)
- order_id
- product_id
- user_id
- rating (float, min:1, max 5)
- review
- created_at (auto_generated)
- updated_at (auto_generated)

status code:
- 200 : ok
- 201 : created
- 400 : bad request
- 404 : not found
- 405 : method not allowed
- 410 : resource is no longer available at the server

installation:
- flask-restful
- peewee
- pymysql

Nella Zabrina Pramata