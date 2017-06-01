# product-service

Api's

Auth API:

1. Login

   URL: http://localhost:8000/auth/login
   Request Method : POST
   Data Sample: {"username":"Usernaame", "password":"Password"}
   Response: 
          {
            "token": "69647b612f876035ae3df73975e06d5f37783e60e54187d5470a847e639b9f8b",
            "user": {
            "username": "pranav",
            "first_name": "",
            "last_name": ""
            }
          }
          
2. Logout
URL: https://product-services.herokuapp.com/auth/logout
Request Method : POST
headers: {"Authorization":"Token 83d4c101fbe5bd29c72e4d75a0dc9053e75d996cb7b8ddaeac0c88476ebbd156"} // token returned in response of login api

3. Product List:
URL: https://product-services.herokuapp.com/product/
Request Method : GET

4. Product Detail:
URL: https://product-services.herokuapp.com/product/id
Request Method : GET

5. Product Create:
URL: https://product-services.herokuapp.com/product/
Request Method : POST
headers: {"Authorization":"Token 83d4c101fbe5bd29c72e4d75a0dc9053e75d996cb7b8ddaeac0c88476ebbd156"}
data:{
            "id": 1,
            "sku_number": "12345",
            "brand": "Adidas",
            "category": 1,
            "name": "herbal",
            "condition": "new",
            "description": "sdgsd",
            "price": "10.00",
            "parent": null
        }
6. Product Update:

URL: https://product-services.herokuapp.com/product/
Request Method : POST
headers: {"Authorization":"Token 83d4c101fbe5bd29c72e4d75a0dc9053e75d996cb7b8ddaeac0c88476ebbd156"}
data:{}

7. Category List:
URL: https://product-services.herokuapp.com/category/
Request Method : GET
8. Category Detail:
URL: https://product-services.herokuapp.com/category/id
Request Method : GET

9. Category Create:
URL: https://product-services.herokuapp.com/category/
Request Method : POST
headers: {"Authorization":"Token 83d4c101fbe5bd29c72e4d75a0dc9053e75d996cb7b8ddaeac0c88476ebbd156"}
data:{
        "name": "Beauty",
        "parent": null 
    }

Note: Parent should be the id of another category of which it should be sub category

10. Category Wise product list
URL: https://product-services.herokuapp.com/category/id/products
Request Method : GET

11. Sub category of Category
URL: https://product-services.herokuapp.com/category/id/sub-category
Request Method : GET

