import path from 'path';

console.log(process.env.SRC_ROOT, 'index.js');

const config = {
    entry: {
        welcome: path.resolve(process.env.SRC_ROOT, 'index.js')
    },
    output: {
        path: path.resolve(process.env.PROJECT_ROOT, 'dist'),
        filename: '[name].js'
    },
    module: {
        rules: [
            
        ]
    },
    plugin:[

    ]
}


export default config;