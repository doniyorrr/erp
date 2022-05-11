import Axios from "../components/axios/axios"
import { GET_PRODUCT , DELETE_PRODUCT, ADD_PRODUCT } from "./types"




export const getProducts = () => dispatch =>{
    Axios.get("/product/")
    .then(res =>{ dispatch({
        type: GET_PRODUCT,
        payload: res.data
    })})
    .catch(err => console.log(err))
}

export const addProducts = (data) => dispatch =>{
    console.log(data);
     Axios.post("/product/create/" , data)
    .then(res => {
        console.log(res.data);
        dispatch({
        type: ADD_PRODUCT,
        payload: res.data
    })})
    // .catch(err => console.log(err))
}

export const deleteProduct = (id) => dispatch =>{
    Axios.delete(`/product/detail/${id}/`)
    .then(res => {dispatch({
        type: DELETE_PRODUCT,
        payload: id
    })})
    .catch(err => console.log(err))
}