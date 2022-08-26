import axios from 'axios';
import {HOST,PORT} from '../../config/constants.js';

async function computeSimilarity(data) {
    const formData = new FormData();
    formData.append('file', data.file);
    formData.append('contract', data.contract);
    formData.append('token_id', data.tokenId);
    
    try{
        resp = await axios({
            method: "post",
            url: `http://${HOST}:${PORT}/api/v1/similarity`,
            data: formData,
            headers: { "Content-Type": "multipart/form-data"},
        });
    }catch(err){
        console.log('has error');
    }

    return {
        code: 200,
        message: null,
        data: {
            similarity: "0.9787878"
        }
    }
}


export default {
    computeSimilarity
}