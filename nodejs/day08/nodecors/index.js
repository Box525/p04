const Express = require('express')
const Path = require('path')

const app = Express()
app.use(Express.static(Path.join(__dirname,'public')))


app.get('/',(req,res)=>{
    res.redirect('index.html')
})

app.listen(8080)