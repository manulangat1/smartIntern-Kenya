import express from 'express';
import colors from 'colors';
import dotenv from 'dotenv';
import morgan from 'morgan';
import bodyParser from 'body-parser';

dotenv.config()
const app = express()

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
 
// parse application/json
app.use(bodyParser.json());


if (process.env.NODE_ENV === "development"){
    app.use(morgan('dev'));
}

const PORT=process.env.PORT;

app.listen(PORT, console.log(`SMART INTERN RUNNING IN ${process.env.NODE_ENV} MODE ON PORT ${PORT}`.yellow.underline));