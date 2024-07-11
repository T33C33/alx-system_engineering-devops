# Debugging Apache in Docker Container

In this project, you will debug Apache running in a Docker container to return a page containing "Hello Holberton" when querying the root of it.

To get started, make sure to read the Docker concept page to familiarize yourself with Docker.

Follow these steps to debug Apache in the Docker container:

1. Start the Docker container with the following command:
    ```
    docker run -p 8080:80 -d -it holbertonschool/265-0
    ```

2. Check the status of the Docker container using the command:
    ```
    docker ps
    ```

3. Curl the port 8080 mapped to the Docker container port 80 using the command:
    ```
    curl 0:8080
    ```

    If you receive the error message "curl: (52) Empty reply from server," proceed to the next step.

4. Connect to the Docker container using the command:
    ```
    docker exec -it <container_id> /bin/bash
    ```

5. Inside the container, fix whatever needs to be fixed to make Apache return the desired page. Once fixed, exit the container.

6. Curl the port 8080 again using the command:
    ```
    curl 0:8080
    ```

    You should now see the page containing "Hello Holberton."

Remember to include the command(s) you used to fix the issue in your answer file.
