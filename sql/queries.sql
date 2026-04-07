CREATE TABLE youtube_comments (
    comment VARCHAR(65535),
    original_sentiment VARCHAR(50),
    predicted_sentiment VARCHAR(50)
);
COPY youtube_comments
FROM 's3://aws-project-divya/processed/youtube_output.csv'
IAM_ROLE 'PASTE_YOUR_ROLE_ARN'
CSV
IGNOREHEADER 1;
SELECT * FROM youtube_comments LIMIT 10;
SELECT predicted_sentiment, COUNT(*) 
FROM youtube_comments
GROUP BY predicted_sentiment;