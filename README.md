# EcoLogic DemoApp

Demo App for EcoLogic

## structure

```structure
.README
├── python
    ├── app
        ├── templates
            ├── index.html
            └── success.html
        ├── Dockerfile
        ├── requirements.txt
        └── app.py
    └── compose.yaml
├── .....
```

## Python

- switch to python folder
- use uv pip install requirements.txt to install all required dependencies
- run the app:

```sh
python3 app.py
```

- Open Browser and use url http://localhost:8080

### Docker and Docker compose

#### Docker Compose File

[_compose.yaml_](compose.yaml)

```yaml
services: 
  web: 
    build:
     context: app
     target: builder
    ports: 
      - '8080:8080'
```

#### Build and Deploy with docker compose

##### Build and run

```sh
    docker build -t ecologic .
    docker run -p 8080:8080 ecologic
```


```sh
$ docker compose up -d
[+] Building 1.1s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                       0.0s
    ...                                                                                                                                         0.0s
 => => naming to docker.io/library/flask_web                                                                                                                                                                                               0.0s
[+] Running 2/2
 ⠿ Network flask_default  Created                                                                                                                                                                                                          0.0s
 ⠿ Container flask-web-1  Started
```

## Expected result

Listing containers must show one container running and the port mapping as below:

```sh
$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
flask-web-1         "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp
```

After the application starts, navigate to `http://localhost:8080` in your web browser or run:

```sh
$ curl localhost:8080
Welcome to Eco and Logic!
```

Stop and remove the containers

```sh
docker compose down
```
