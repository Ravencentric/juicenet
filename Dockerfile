FROM nikolaik/python-nodejs:python3.12-nodejs20

ENV LANG=C.UTF-8 \
    # See: https://github.com/Ravencentric/juicenet-cli/issues/75
    GYP_DEFINES="enable_native_tuning=0"

WORKDIR /node

RUN npm install -g yencode
RUN npm install -g git+https://github.com/animetosho/Nyuu.git --production --unsafe-perm
RUN npm install -g @animetosho/parpar

WORKDIR /app

COPY . .
COPY ./config/juicenet.docker.yaml /config/juicenet.docker.yaml

RUN pip install .

WORKDIR /media

ENTRYPOINT ["python", "-m", "juicenet", "--config", "/config/juicenet.docker.yaml"]
