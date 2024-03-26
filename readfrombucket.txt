import requests

def read_octet_stream_file(file_url):
    try:
        # Fetch the octet stream content
        response = requests.get(file_url)

        if response.status_code == 200:
            # Assuming the content is in UTF-8 encoding
            return response.content.decode("utf-8")
        else:
            print(f"Error fetching the file. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error reading octet stream file: {e}")
        return None

if __name__ == "__main__":
    # Define the URL of your octet stream SQL file in cloud storage
    sql_file_url = "https://example.com/path/to/your/file.sql"

    # Read the SQL query from the octet stream file
    sql_query = read_octet_stream_file(sql_file_url)

    if sql_query:
        print("SQL query from the file:")
        print(sql_query)
    else:
        print("Error reading SQL query from the octet stream file.")
