import axios from 'axios';
import {HOST,PORT} from '../../config/constants.js';
async function computeSimilarity(form) {
    const formData = new FormData(form);
    await new Promise((resolve, reject)=>{
        setTimeout( ()=>{resolve()}, 3000);
    })
    try{
        let resp = await axios.post(
            `http://${HOST}:${PORT}/api/v1/similarity`,
            formData,
            { headers:{"Content-Type": "multipart/form-data"}},
        );
        return resp.data;
    }catch(err){
        console.log('has error:', err.message);
    }
}


export default {
    computeSimilarity
}