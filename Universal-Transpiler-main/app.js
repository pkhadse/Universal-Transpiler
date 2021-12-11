const http = require('http')
const express = require('express')
const upload = require('express-fileupload')
const fs = require('fs')
const app = express()

app.use(upload())








app.get('/download', function(req, res){
    res.download('./out.c')
    })
app.get('/download1', (req, res) => res.download('./out.cpp'))
app.get('/download2', (req, res) => res.download('./out.java'))




app.get('/',(req,res) => {
    res.sendFile(__dirname + '/index.html')

})

app.post('/', (req,res)=> {
    if(req.files){
        console.log(req.files)
        var file = req.files.file
        var filename = file.name
        console.log(filename)

        file.mv(filename,function (err){
            if (err){
                res.send(err)}
            // }else{
            //     res.send("file uploaded")
                // const { exec } = require('child_process');
                // var yourscript = exec('sc.py',
                // (error, stdout, stderr) => {
                //     console.log(stdout);
                //     console.log(stderr);
                //     if (error !== null) {
                //         console.log(`exec error: ${error}`);
                //     }
                // });
            // }
        })
    }
})

const { spawn } = require('child_process')
app.get('/foo', function(req, res) {
    // Call your python script here.
    // I prefer using spawn from the child process module instead of the Python shell
    const scriptPath = 'sc.py'
    const process = spawn('python', ['sc.py'])
    process.stdout.on('data', (myData) => {
        // res.send("helllllooo")
        // res.redirect('/download')
        res.sendFile(__dirname + '/temp.html')
        
    })
    process.stderr.on('data', (myErr) => {
        // If anything gets written to stderr, it'll be in the myErr variable
    })
})

const { spawn1 } = require('child_process')
app.get('/foo1', function(req, res) {
    // Call your python script here.
    // I prefer using spawn from the child process module instead of the Python shell
    const scriptPath = 'sc1.py'
    const process = spawn('python', ['sc1.py'])
    process.stdout.on('data', (myData) => {
        // res.send("helllllooo")
        // res.redirect('/download1')
        res.sendFile(__dirname + '/temp1.html')
    })
    process.stderr.on('data', (myErr) => {
        // If anything gets written to stderr, it'll be in the myErr variable
    })
})

const { spawn2 } = require('child_process')
app.get('/foo2', function(req, res) {
    // Call your python script here.
    // I prefer using spawn from the child process module instead of the Python shell
    const scriptPath = 'sc2.py'
    const process = spawn('python', ['sc2.py'])
    process.stdout.on('data', (myData) => {
        // res.send("helllllooo")
        // res.redirect('/download2')
        res.sendFile(__dirname + '/temp2.html')
    })
    process.stderr.on('data', (myErr) => {
        // If anything gets written to stderr, it'll be in the myErr variable
    })
})

app.listen(5000)