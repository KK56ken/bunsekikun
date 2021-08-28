var http = require('http');

var server = http.createServer();
server.on('request', doRequest);
server.listen(1234);
console.log('Server running!');

// リクエストの処理
async function doRequest(req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    //呼び出し結果出力
    // res.write("Hello World")
    var {PythonShell} = require('python-shell')
    let options = {
        scriptPath: '/home/ken/github/bunsekikun/bunseki',
        args: ['https://www.apple.com/', '1']
    };
    const { success, err = '', results } = await new Promise((resolve, reject) =>{
        PythonShell.run('main.py', options, function (err, results) {
        if (err) {
            logger.error(err, '[ config - runManufacturingTest() ]');
            reject({ success: false, err });
        }
            // results is an array consisting of messages collected during execution
            // console.log('results: %j', results);
            // console.log(a)
            console.log("分析結果出力完了🤣");

            resolve({ success: true, results })
        });
    })
    console.log(typeof(results))
    // console.log(results)
    
    // results = results["'tag'"]

    // console.dir(results)
    let buffer = Buffer.from(JSON.stringify(results))

    res.write(buffer)
    console.log('Hello World😇');

    res.end();
}