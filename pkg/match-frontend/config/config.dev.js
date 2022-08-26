import commonConfig from './config.common.js';
import path from 'path';

const devPart = {
    mode: 'development',
    devServer: {
        static: path.resolve(process.env.PROJECT_ROOT, 'dist'),
        port: 8000
    }
}

const merged = Object.assign({}, commonConfig, devPart);

export default merged;