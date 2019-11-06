# postgres-12

This image will forward port 5432 (default postgres port) from localhost
to the container port so you can use an postgres client to connect to the
container.

```sh
docker-compose up
```

Then visit http://localhost:8080 to access the postgres web client.

Make sure to change the dropdown in adminer to PostgreSQL. You can use these credentials:

![Adminer](https://user-images.githubusercontent.com/3826772/68314563-5df14f00-0084-11ea-81e7-2a3b63c44f41.png)


You can also access the database with a GUI client such as Postico with these credentials.

![Postico](https://user-images.githubusercontent.com/3826772/68314906-fa1b5600-0084-11ea-9c75-b8c552b3844f.png)

## Container Info

DockerHub:
https://hub.docker.com/_/postgres

Github Dockerfile:
https://github.com/docker-library/postgres/blob/a8613f4cda3e932245f09c4d0f6733462b14b582/12/Dockerfile
