import React, {useEffect,useState} from "react";



function index(){
  const [message,setMessage]  = useState<string>("loading..");
  const [inputValue,setInputValue] = useState<string>();
  useEffect(()=>{
    fetch("http://localhost:8080/api/home")
    .then((reponse)=>reponse.json())
    .then((data)=>{
      setMessage(data.message)
    });
  },[]);

const send = () =>{
fetch("http://localhost:8080/api/get",{

    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({value: inputValue}),
  }).then((response)=>{response.json()})
  .then((data)=>{
    console.log("response: ",data)
  })
}

return (
<div>
  <div>{message}</div>
<input type = "text" value = {inputValue} onChange={(e) => setInputValue(e.target.value)}></input>
<button onClick={send}>send</button>
</div>
)

}
export default index;