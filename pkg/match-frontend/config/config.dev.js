import commonConfig from './config.common.js';
import path from 'path';
import {HOST, PORT} from './constants.js';

const devPart = {
    mode: 'development',
    devServer: {
        proxy: {
            '/api': {
                target: `${process.env.BACKEND_HOST}:${process.env.BACKEND_PORT}`,
                changeOrigin: false //据说true可解决跨域问题，待测试
            }
        },
        static: path.resolve(process.env.PROJECT_ROOT, 'dist'),
        host: HOST,
        port: PORT,
        // headers: {
        //     "Access-Control-Allow-Origin": "*",
        //     "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
        //     "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
        //   }
    }
}

// const merged = Object.assign({}, commonConfig, devPart);
const merged = {...commonConfig, ...devPart};
export default merged;