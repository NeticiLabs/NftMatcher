import path from 'path';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import initer from './envInit.js';
import webpack from 'webpack';

initer();

const config = {
    entry: {
         default: path.resolve(process.env.SRC_ROOT),
    },
    output: {
        path: path.resolve(process.env.PROJECT_ROOT, 'dist'),
        filename: 'bundle.js'
    },
    plugins:[
        new HtmlWebpackPlugin({
            template: path.resolve(process.env.SRC_ROOT, 'index.html'),
            chunks: ['default'],
            filename: 'index.html'
        }),
        new webpack.ProvidePlugin({
            "React": "react",
        }),
    ],
    module: {
        rules: [
            {
                test: /\.(jsx|js)$/,
                use: {
                    loader: 'babel-loader',
                },
                exclude: /(node_modules|bower_components)/, // 千万别忘记添加exclude选项,不然运行可能会报错
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
        ]
    },
}


export default config;