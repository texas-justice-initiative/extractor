FROM python:3.11.2

# install ubuntu basics
RUN apt-get update && apt-get install -y \
    python3 python3-pip --no-install-recommends && rm -rf /var/lib/apt/lists/*


WORKDIR /tmp/tracker/

# install poetry + dependencies & set working directory
RUN pip install --upgrade pip && pip install poetry
COPY poetry.lock pyproject.toml /tmp/tracker/
RUN poetry install --no-root --no-dev

# move over rest of code
COPY . /tmp/tracker/
