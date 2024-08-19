
Blazing fast Python Docker builds with Poetry
https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0
https://medium.com/swlh/dockerize-your-python-command-line-program-6a273f5c5544


# Install and use:
```
docker build -t tool --rm .
docker run --rm -it --name tool tool
```

# Dev
```
docker run --rm -it -v $(pwd)/tool:/app/tool --name tool tool --help
```

## 

- Package Management via Poetry: https://python-poetry.org/docs/basic-usage/
- Cli: https://typer.tiangolo.com/tutorial/