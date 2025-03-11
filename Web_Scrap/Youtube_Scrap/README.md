# YouTube Web Scraping Project  

This project focuses on web scraping YouTube channel pages and extracting video details using **Selenium** and **BeautifulSoup**.  

## Overview  

The project follows a two-step scraping process:  

1. **Scraping Video Links from a YouTube Channel Page**  
   - Open the YouTube channel's **videos** section.  
   - Extract details such as **title, views, upload date, video link, and thumbnail link**.  
   - Save the extracted data into a CSV file.  

2. **Scraping Detailed Information from Each Video Page**  
   - Read the CSV file containing video links.  
   - Open each video link using Selenium.  
   - Extract detailed information such as **title, views, upload date, likes, and description**.  
   - Save the extracted data into a structured format.  

## Technologies Used  

- **Python**  
- **Selenium** (for handling dynamic content)  
- **BeautifulSoup** (for parsing HTML)  
- **Pandas** (for data handling)  
- **NumPy**  
- **tqdm** (for progress tracking)  

## Setup & Execution  

1. Install required dependencies:  

   ```bash
   pip install selenium beautifulsoup4 pandas numpy tqdm
   ```

2. Ensure **ChromeDriver** is installed and properly configured.  

3. Run the scripts sequentially to scrape video links first and then extract detailed video information.  
