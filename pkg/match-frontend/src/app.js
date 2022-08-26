import { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Alert, Form, Button, Card, FormGroup } from 'react-bootstrap';
import api from './utils/api.js';
import { useEffect } from 'react';

function App(props) {
    const [inputs, setInputs] = useState({});
    const [visible, setVisible] = useState(false);
    const [data, setData] = useState({});
    const [loading, setLoading] = useState(false);
    useEffect(()=>{
        console.log('渲染');
        setVisible(false);//渲染的时候初始化
    },[]);
    
    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]:value}));
    }
    const handleSubmit = async (event) => {
        event.preventDefault();
        setVisible(false);
        setLoading(true);
        const resp = await api.computeSimilarity(inputs);
        setData(resp.data);
        setLoading(false);
        setVisible(true);
    }
    const loadingComponent = loading?loadingArea():(<div></div>);
    const resultComponent = visible?resultArea(data):(<div></div>)
    return <div id='main' className='w-75'>
        <form id='form' onSubmit={handleSubmit}>
            <FormGroup className="mb-5 mt-5" controlId='formBasicEmail'>
                <Form.Label className="fs-2">选择你要上传的文件</Form.Label>
                <Form.Control className='fs-2' type='file' placeholder='文件上传' 
                name='file' onChange={handleChange}/>
            </FormGroup>

            <FormGroup className=" mb-5" controlId='formBasicEmail'>
                <Form.Label className="fs-2">请输入合约地址</Form.Label>
                <Form.Control className='fs-2 ' type='text' placeholder='Enter contract address' 
                name="contract" onChange={handleChange}/>
            </FormGroup>

            <FormGroup className="mb-5" controlId='formBasicPassword'>
                <Form.Label className="fs-2">请输入token Id</Form.Label>
                <Form.Control className='fs-2' type="text" placeholder='Enter token Id'
                name="tokenId" onChange={handleChange}
                ></Form.Control>
            </FormGroup>
        
            <Button id="button" 
                className="mt-3 " 
                variant="primary" 
                type="submit" 
                disabled={loading}
                >
                进行比较!
            </Button>
        </form>
        {loadingComponent}
        {resultComponent}
    </div>
}

function resultArea(data) {
    return (
        <div id='result-area' className='mb-5'>


            <div id='img-area'>
                <div className='img'>
                </div>

                <div id='similarity-area' >
                    <Card style={{ textAlign:'center', margin:'auto'} } >
                        <Card.Body>
                            <Card.Title className='fs-3'>相似度:</Card.Title>
                            <Card.Text  style={ {fontSize: '40pt'}} >
                                {data.similarity}
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </div>

                <div className='img '>
                </div>
            </div>
        </div>

    )
}

function loadingArea() {
    return (
        <div id='loading-area' 
        className='mb-5 spinner-border text-primary' 
        style={{margin:'auto', display:'block', width:'50px', height:'50px'}}>

        </div>
    )
}

//TODO: 1 设计结果区的样式
//TODO: 2 让结果区可以隐藏
//TODO: 3 form data怎么上传文件，特别是文件流怎么读取
//TODO: 4 添加“计算中，请稍后”旋转提示
//Demo
// function App(props) {
//     const [inputs, setInputs] = useState({});
//     const handleChange = (event) => {
//         const name = event.target.name;//Form.Control的name属性
//         const value = event.target.value;
//         setInputs(values => ({...values, [name]:value}));
//         //inputs = {xxxx} 不能通过这种形式，因为inputs是只读的。
//     }
//     const handleSubmit = (event) => {
//         event.preventDefault();
//         alert(JSON.stringify(inputs));
//     }

//     return <div>
//         <form id='form' onSubmit={handleSubmit}>
//             <FormGroup  controlId='formBasicEmail'>
//                 <Form.Label >请输入合约地址</Form.Label>
//                 <Form.Control  type='text'
//                     name="address"
//                     onChange={handleChange}/>
//             </FormGroup>
        
//             <Button id="button" variant="primary" 
//                 type="submit" 
//                 >
//                 相似度比较
//             </Button>
//         </form>
//     </div>
// }


export default App;