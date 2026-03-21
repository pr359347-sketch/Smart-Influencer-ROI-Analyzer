create database influencer_db;
use influencer_db;
create table influencer(
    influencer_name VARCHAR(255),
    platform VARCHAR(50),
    followers INT,
    likes INT,
    comments INT,
    shares INT,
    impressions INT,
    clicks INT,
    conversions INT,
    campaign_cost FLOAT,
    revenue FLOAT,
    content_type VARCHAR(50),
    campaign_date DATE,
    engagement_rate FLOAT,
    roi FLOAT,
    conversion_rate FLOAT,
    influencer_score FLOAT,
    influencer_type VARCHAR(50)
);
select * from influencer;


 