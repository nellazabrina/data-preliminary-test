# data-preliminary-test

### Prekondisi
- sudah import sql

### Spesifikasi
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

### Status Code:
- 200 : ok
- 201 : created
- 400 : bad request
- 404 : not found
- 405 : method not allowed
- 410 : resource is no longer available at the server

### Installation:
- flask-restful
- peewee
- pymysql

### Cara Penggunaan

#### create:
- menggunakan method post
- contoh http://localhost:5000/api/usr-review/
dengan body
{
    "order_id" : 3,
    "product_id" : 1,
    "user_id" : "user",
    "rating" : 3,
    "review" : "test content review"
}

#### read:
- menggunakan method get
- contoh http://localhost:5000/api/usr-review/<integer:id>

#### update:
- menggunakan method put
- contoh http://localhost:5000/api/usr-review/<integer:id>
dengan body
{
    "order_id" : 3,
    "product_id" : 1,
    "user_id" : "user",
    "rating" : 3,
    "review" : "change content review"
}

#### delete:
- menggunakan method delete
- contoh http://localhost:5000/api/usr-review/<integer:id>


#### Nella Zabrina Pramata