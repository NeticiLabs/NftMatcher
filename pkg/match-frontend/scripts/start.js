import webpack from 'webpack'
import devConfig from '../config/config.dev.js'
import DevServer from 'webpack-dev-server';

async function main(){
    const compiler = webpack(devConfig);
    const devServer = new DevServer(compiler, devConfig.devServer);
    console.log('Starting dev server at ', devConfig.devServer.port);
    await devServer.start();
}

try{
    main();
}catch(err){
    console.log(err);
}

// console.log(compiler);
