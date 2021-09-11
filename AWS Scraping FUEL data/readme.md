# AWS Scraping FUEL data <h1> 

![image](https://user-images.githubusercontent.com/60892908/132874696-7661e6c9-394a-4720-a2b6-9b77bc634568.png)

# Project shows how to scrape date from webiste and store them in RDS MySql database <h3>
  
Configuration stuff
 1) Import nessesary library. 
  
  For this I used solution called 'Layers'. I install localy libraries in specyfic location. Next step was to zipped all files and upload them to 'Layers'.
  
![image](https://user-images.githubusercontent.com/60892908/132942955-b251649f-292d-467f-81fa-0b4b98db5df0.png)

 2) Automation download data.
  
  For this task I used AWS EventBridge (CloudWatch Events) which allow me to create Cron Schedule expression (data are downloaded once a day at 10.00 am)
  
  ![image](https://user-images.githubusercontent.com/60892908/132943789-59a7ed28-78db-4f14-b1fb-c89c7aa60efd.png)

  
  

