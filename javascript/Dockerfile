FROM node:18.1-buster

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm install

COPY . /app

CMD ["node", "index.js"]