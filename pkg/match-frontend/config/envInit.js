import path from 'path'

//Preset path infomations
function init() {
    process.env.PROJECT_ROOT=process.cwd()
    process.env.SRC_ROOT = path.resolve(process.env.PROJECT_ROOT, "src");
}


export default init;