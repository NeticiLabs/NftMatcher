import path from 'path'
import dotenv from 'dotenv';
//Preset path infomations
function init() {
    process.env.PROJECT_ROOT=process.cwd()
    process.env.SRC_ROOT = path.resolve(process.env.PROJECT_ROOT, "src");
    process.env.PUBLIC_ROOT = path.resolve(process.env.PROJECT_ROOT, "public");
    process.env.CONFIG_ROOT = path.resolve(process.env.PROJECT_ROOT, "config");

    let configPath = path.resolve(process.env.CONFIG_ROOT, `.env.${process.env.NODE_ENV}`);
    dotenv.config({
        path: configPath
    });
}


export default init;