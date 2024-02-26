import { useState,useEffect } from "react";
import axios from "axios";
export default function Product(){
    const [product,setProduct]=useState([])
    useEffect(()=>{
        console.log("request to api")
        axios.get("http://127.0.0.1:3000/products")
        .then(response=>setProduct(response.data))
        .catch(error => {
            console.error('Error fetching data:', error);
        })
    },[])
    const productList=product.map(p=><li key={p.id}>{p.id} {p.name} <img src={p.img}/> {p.price}</li>)
    return (
        <div style={{display : "flex",justifyContent : "center", alignContent : "center"}}>
            <div style={{display : "grid",justifyItems : "center", alignContent : "center", width : 500, height : 500}}>
                <form action="/url" method="GET" style={{paddingBottom : 10}} >
                    <p style={{display: "flex", justifyContent : "center", alignContent : "center" }}>Enter ID</p>
                    <input style={{display: "flex", justifyContent : "center", alignContent : "center" ,width : 250, height : 30, borderRadius : 50}} type="text"/>
                </form>
                <form action="/url" method="GET" style={{paddingBottom : 10}} >
                    <p style={{display: "flex", justifyContent : "center", alignContent : "center" }}>Enter Name</p>
                    <input style={{display: "flex", justifyContent : "center", alignContent : "center" ,width : 250, height : 30, borderRadius : 50}} type="text"/>
                </form>
                <form action="/url" method="GET" style={{paddingBottom : 10}} >
                    <p style={{display: "flex", justifyContent : "center", alignContent : "center" }}>Enter img (URL)</p>
                    <input style={{display: "flex", justifyContent : "center", alignContent : "center" ,width : 250, height : 30, borderRadius : 50}} type="text"/>
                </form>
                <button style={{width : 300, height : 100, fontSize : 30, borderRadius : 50}}>ADD</button>
            </div>
            <ul>
                {productList}
            </ul>
        </div>
    )
}