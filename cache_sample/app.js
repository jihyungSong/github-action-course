const express = require('express')
const app = express()
const port = 3000

var humancat = require('humancat')

var hc = new humancat.Humancat(human_name='ryan', cat_name='haku')

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})