FROM node:alpine

WORKDIR /react-app

COPY ./package.json /react-app

RUN npm config set legacy-peer-deps true
RUN npm install

COPY ./ ./

CMD [ "npm", "start"]