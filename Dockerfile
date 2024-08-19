FROM alpine:3

# Poetry para gerenciamento de dependencias do python. 
# Já existe pacote pro alpine, então nem precisamos instalar via PIP.
# Pinado na versão 1.8.X para não quebrar a build caso a interface do poetry mude.
# https://pkgs.alpinelinux.org/packages?name=poetry&branch=edge
# https://superuser.com/questions/1055060/how-to-install-a-specific-package-version-in-alpine
RUN apk add --no-cache "poetry=~1.8"

# Mesmo dockerizando, vamos instalar o projeto em um virtualenv gerenciado pelo poetry.
# Especificamos o cache_dir pois posteriormente iremos instalar as dependencias e limpar
# o cache, tudo em um único comando, para ajudar a manter a imagem do docker pequena.   
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \ 
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Cria o virtualenv com as dependencias, mas ainda não copia o fonte.
# Faço isso pra poder carregar o fonte em uma layer diferente do docker. 
# Isso permite cachear a layer das dependencias, aumentando a velocidade da 
# build
# https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0
COPY pyproject.toml poetry.lock ./
RUN touch README.md
RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR

COPY tool ./tool
RUN poetry install --without dev 

ENTRYPOINT ["poetry", "run", "tool"]
CMD ["--help"]