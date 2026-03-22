create database influencer_db;
use influencer_db;
create table influencer(
    
    influencer_id INT PRIMARY KEY,
    influencer_name VARCHAR(100),
    platform VARCHAR(50),
    followers INT,
    engagement_rate FLOAT,
    likes INT,
    comments INT,
    campaign_cost FLOAT,
    revenue_generated FLOAT,
    category VARCHAR(50),
    predicted_roi FLOAT
);
select * from influencer;


 
