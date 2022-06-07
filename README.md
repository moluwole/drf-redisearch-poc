## Simple Django Project that uses Redisearch as a POC
### About the project

The project uses [Redisearch](https://oss.redislabs.com/redisearch/) which is a powerful search and indexing engine created by the Redis Team for caching and storing.We use 
celerybeat to schedule downloading of the CSV file from the provided URL. The workflow is for CeleryBeat to try and download the file by 12 midnight. If the CSV file 
exists, the contents are streamed and saved to Cache which is Redisearch.  

### Installation

- Make sure you have Docker and Docker Compose installed on your system. 
  For MacOS users, download from here [Docker for Mac](https://docs.docker.com/docker-for-mac/install/), For Windows users,
  download Docker desktop from here [Docker for Windows](https://docs.docker.com/docker-for-windows/install/). 
  
  You can choose also choose your operating system from [here](https://docs.docker.com/engine/install/) and download the corresponding Docker Engine/Desktop
  
- Run the following command to get the containers up and running
  ```sh
  $ docker-compose up --build -d
  ```
  
  Once the containers are up, it automatically runs the `download_cache` command which runs one time to setup the cache

- Navigate to [http:localhost:8000/api/items/](http:localhost:8000/api/items/) to see the first set of results. Do note 
  that results are paginated. To navigate, add number of results as `result_count` and page_number as `offset`
  
  **Example**
  
  Let's say the total number of items is 200 and I need 20 items per request, I'll just do
   - [http:localhost:8000/api/items/?result_count=20&offset=0](http:localhost:8000/api/items/?result_count=20&offset=0) for the 
        first page,
   - [http:localhost:8000/api/items/?result_count=20&offset=1](http:localhost:8000/api/items/?result_count=20&offset=1) for the next page
   
   and so on till page 9 which programmatically is the last page. We start counting from zero. 
   
   > Do note that the total number of items is returned as part of the response.
  
  Sample response dict is shown below
   
  ```json
    {
      "items": [{"id":  1, 
                  "title":  "Title here", 
                  "image": "http://image.com", 
                  "description":  "My Description"}
                ],
      "total": 20  
    } 
    ```
  - To get a single item, use [http:localhost:8000/api/items/{id}](http:localhost:8000/api/items/{id}). Replace {id} with
  the unique ID provided with each item
  
  Sample response dict is shown below
  
  ```json
    {
      "id": 5,
      "title": "Item 6, extra info",
      "description": "<b>Description 6</b>",
      "image": "http://fc01.deviantart.net/fs17/f/2007/129/7/4/Stock_032__by_enchanted_stock.jpg"
    }
  ```

- To view background tasks and their respective status, there's a flower dashboard available at [http://localhost:5555](http://localhost:5555)
- Documentation available at [http://localhost:8000/docs/](http://localhost:8000/docs/)
  
Made Changes to the CSV and need to update cache? Run
```sh
$   docker-compose exec api python manage.py download_cache
```

CSV URL has changed and need to be updated? Update the `CSV_URL` environment variable to your chosen url

#### Tech Stack
- Python Django
- Redisearch & Redis (for storage)
- Celery & CeleryBeat
- Flower Dashboard