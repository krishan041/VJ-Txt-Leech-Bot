import requests

def download_pdf(url, output_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded '{output_path}' successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    url = "https://appxcontent-mcdn.akamai.net.in/paid_course4/2024-08-14-0.7892268743301407.pdf"
    output_path = "downloaded_file.pdf"
    download_pdf(url, output_path)
