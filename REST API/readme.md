# REST API <h1> 

Project shows how to set up an API Gateway endpoint that directly interacts with DynamoDB

![image](https://user-images.githubusercontent.com/60892908/132727620-98aff593-ffaa-4b9f-8b38-be7b7a9f09f5.png)


Steps:
1.	Creating DynamoDB table "Orders" with Partition key OrderId and Sort key date

 ![image](https://user-images.githubusercontent.com/60892908/132727667-20d5b13c-affb-4af6-9b67-f9588c872492.png)


2.	Creating IAM role to access from API Gateway to DynamoDB

 •	To create appropriate role we must choose policy which is called 

 ![image](https://user-images.githubusercontent.com/60892908/132727684-d279e2d7-7ee2-4dbe-8259-1b4ebb0afd0e.png)

 
 •	Next we must change Trust Relationships in our policy to this below

 ![image](https://user-images.githubusercontent.com/60892908/132727705-6c1ab221-b9df-4052-81ae-15bc32f3e69b.png)

 
 •	Now policy is ready to be use


3.	Creating API GATEWAY

 •	Create Resources "orders"

 •	Next create "POST" method

 •	In section "Execution role" put your role arn

 •	Other configuration should be like on picture below

 ![image](https://user-images.githubusercontent.com/60892908/132727734-79d9c912-67ca-48e2-9171-4a3a680c1cdf.png)

 

 To limit the amount of data entered by the client, I used Mapping Templates which look like:

 ![image](https://user-images.githubusercontent.com/60892908/132727769-41cbe644-52a5-4a45-b044-47d95425c086.png)




 
Results:

![image](https://user-images.githubusercontent.com/60892908/132728415-ce3b17da-eeca-444c-9aef-86dbe5a5e903.png)

 


REST API are ready to be used to PUT some data to DynamoDB.


Output from database 
 
![image](https://user-images.githubusercontent.com/60892908/132944078-30538d6c-aa5f-405a-95a6-3c84fea8bc8f.png)

 



