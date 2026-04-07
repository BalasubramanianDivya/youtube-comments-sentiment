import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

bucket = 'aws-project-divya'
key = 'data/YoutubeComments.csv'

obj = s3.get_object(Bucket=bucket, Key=key)
data = obj['Body'].read().decode('utf-8')

df = pd.read_csv(StringIO(data))

print(df.columns)

df = df.dropna()

def get_sentiment(text):
    text = str(text).lower()
    if "good" in text or "love" in text:
        return "positive"
    elif "bad" in text or "hate" in text:
        return "negative"
    else:
        return "neutral"
    
df["predicted_sentiment"] = df["Comment"].apply(get_sentiment)

csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

s3.put_object(
    Bucket=bucket,
    Key='processed/youtube_output.csv',
    Body=csv_buffer.getvalue()
)

print("ETL Job Completed Successfully!")