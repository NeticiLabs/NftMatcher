import commonConfig from './config.common.js';


const devPart = {

}

const merged = Object.assign({}, commonConfig, devPart);

export default merged;