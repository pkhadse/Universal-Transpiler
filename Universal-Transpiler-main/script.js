// const shell = require('shelljs')
// // var shell = require('shelljs')
// shell.exec('./spt.txt')

const { exec } = require('child_process');
var yourscript = exec('sc.py',
        (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
        });