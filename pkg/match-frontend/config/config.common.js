import path from 'path';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import initer from './envInit.js';
initer();

const config = {
    entry: {
        welcome: path.resolve(process.env.SRC_ROOT, 'welcome')
    },
    output: {
        path: path.resolve(process.env.PROJECT_ROOT, 'dist'),
        filename: '[name].js'
    },
    devServer: {
        static: path.resolve(process.env.PROJECT_ROOT, 'dist'),
        port: 8000
    },
    plugins:[
        new HtmlWebpackPlugin({
            template: path.resolve(process.env.SRC_ROOT, 'welcome', 'index.html'),
            chunks: ['welcome'],
            filename: 'index.html'
        })
    ]
    // module: {
    //     rules: [
            
    //     ]
    // },
    // plugins:[

    // ]
}


export default config;