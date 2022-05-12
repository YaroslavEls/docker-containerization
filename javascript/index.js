require('dotenv').config()
const express = require('express');
const colors = require('colors');
const app = express();
const port = process.env.PORT ?? 3000;

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(port, () => {
    console.log('Wake up samurai'.rainbow);
    console.log(`Example app listening on port ${port}`);
});