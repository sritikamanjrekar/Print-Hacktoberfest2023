import boto3
import os
import threading

AWS_ACCESS_KEY = ""
AWS_SECRET_ACCESS_KEY = ""
BUCKET_NAME = ""
SAVE_FOLDER = "./aws_data"
THREAD_COUNT = 5

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY ,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
s3_resource = session.resource('s3')
bucket = s3_resource.Bucket(BUCKET_NAME)


def download_file(obj):
    file_path = os.path.join(SAVE_FOLDER, os.path.basename(os.path.dirname(obj.key)), os.path.basename(obj.key))
    if file_path.endswith(".json"):
        os.makedirs(os.path.join(SAVE_FOLDER, os.path.basename(os.path.dirname(obj.key))), exist_ok=True)
        bucket.download_file(obj.key, file_path)
        print(f"Downloaded: {obj.key}")


def main():
    threads = []
    for obj in bucket.objects.filter(Prefix="public"):
        thread = threading.Thread(target=download_file, args=(obj,))
        threads.append(thread)
        if len(threads) >= THREAD_COUNT:
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            threads = []

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
