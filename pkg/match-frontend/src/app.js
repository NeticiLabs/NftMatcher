import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Alert, Form, Button, Card, FormGroup } from 'react-bootstrap';

function App(props) {
    return <div>
        <form id='form' >
            <FormGroup className="mb-5" controlId='formBasicEmail'>
                <Form.Label className="fs-2">选择你要上传的文件</Form.Label>
                <Form.Control className='fs-2' type='file' placeholder='文件上传' />
            </FormGroup>

            <FormGroup className=" mb-5" controlId='formBasicEmail'>
                <Form.Label className="fs-2">请输入合约地址</Form.Label>
                <Form.Control className='fs-2 ' type='text' placeholder='Enter contract address' />
            </FormGroup>

            <FormGroup className="mb-5" controlId='formBasicPassword'>
                <Form.Label className="fs-2">请输入token Id</Form.Label>
                <Form.Control className='fs-2' type="text" placeholder='TokenId'></Form.Control>
            </FormGroup>
        
            <Button id="button" className="mt-3" variant="primary" type="submit">
                相似度比较
            </Button>
        </form>
    </div>
}

// function App(props){
//     return (<div>
//             <div class='input'>
                
//                 <input type="file" class='textBox'></input>
//             </div>
//         <div id='main'>

//             <div class='input'>
//                 请输入合约地址：
//                 <input class='textBox' type="text">
//                 </input>
//             </div>
//             <div class='input'>
//                 请输入tokenId:
//                 <input  class='textBox' type="text" >
//                 </input>
//             </div>
//         </div>

//         <button id='submit'>提交</button>
//         <div id='result-area'>
//         </div>
//     </div>
//     );
// } 


export default App;