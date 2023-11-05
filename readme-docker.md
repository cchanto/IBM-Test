-Container Image Base: The first script uses Ubuntu 20.04 as the base image, which is a well-established and widely used version. The second script uses Ubuntu 23.04, which might not be as widely adopted or tested.

-Labeling and Maintainer Information: The first script includes a label indicating the maintainer's email address. This provides useful metadata for anyone using or maintaining the image.

-Setting Timezone Non-interactively: The first script sets the timezone non-interactively, which can be important in automated or non-interactive environments.

-Combining RUN Commands: The first script combines multiple RUN commands into one, which helps reduce the number of layers in the image. Each RUN command creates a new layer, and minimizing the number of layers can make the image smaller and more efficient.

-Fetching Files Using curl: The first script uses curl to fetch files, which is a common and versatile tool for downloading resources from the web. The second script uses ADD to directly add files, which can be less flexible and more limited in its capabilities.

-Directory Structure: The first script creates a necessary directory structure explicitly using mkdir, ensuring that the required directories exist. The second script assumes the directories already exist, which may not always be the case.

-Nginx Configuration: The first script doesn't override the default nginx configuration, which can be a good practice as it allows for easier maintenance and updates of the image. The second script replaces the nginx configuration with a specific one from a URL.

-Git Installation: The second script installs Git after updating the package list, but it's not clear if it's being used. If Git is not necessary for the image's functionality, it's better not to include it.




Steps to run locally 
docker build -t my_nginx_image .


docker run -d -p 80:80 my_nginx_image


Troubleshooting steps 
docker exec -it <container_id> service nginx restart
docker exec -it <container_id> cat /var/log/nginx/error.log


Please validate any other issue that you can face during this build using the dockerhub documentation.



Index, about the running process 
![Screenshot 2023-11-05 at 4 22 10 PM](https://github.com/cchanto/IBM-Test/assets/35463225/60d43da8-6054-4c18-86ab-ab885c84c8d8)


![Screenshot 2023-11-05 at 4 22 24 PM](https://github.com/cchanto/IBM-Test/assets/35463225/9e018012-eedb-4051-ade3-f9647534f8d9)

![Screenshot 2023-11-05 at 4 22 46 PM](https://github.com/cchanto/IBM-Test/assets/35463225/72384fdf-0405-4e09-a188-3b6fdfa94d63)








