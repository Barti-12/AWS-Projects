
![image](https://user-images.githubusercontent.com/60892908/132727620-98aff593-ffaa-4b9f-8b38-be7b7a9f09f5.png)


Steps:
1.	Creating DynamoDB table „Orders” with Partition key OrderId and Sort key date

 ![image](https://user-images.githubusercontent.com/60892908/132727667-20d5b13c-affb-4af6-9b67-f9588c872492.png)


2.	Creating IAM role to access to from API Gateway to DynamoDB

•	To create appropriate role we must choose policy called 

![image](https://user-images.githubusercontent.com/60892908/132727684-d279e2d7-7ee2-4dbe-8259-1b4ebb0afd0e.png)

 
•	Next we must change Trust relationships in our policy to this below

![image](https://user-images.githubusercontent.com/60892908/132727705-6c1ab221-b9df-4052-81ae-15bc32f3e69b.png)

 
•	Now policy is ready to be use


3.	Creating API GATEWAY

•	Create Resources “orders”

•	Next create POST method

•	In section “Execution role” put your role arn

•	Other configuration shoud be like on picture below

![image](https://user-images.githubusercontent.com/60892908/132727734-79d9c912-67ca-48e2-9171-4a3a680c1cdf.png)

 


To limit the amount of data entered by the client, I used Mapping Templates which look like:

![image](https://user-images.githubusercontent.com/60892908/132727769-41cbe644-52a5-4a45-b044-47d95425c086.png)




 
Results:
 






 



