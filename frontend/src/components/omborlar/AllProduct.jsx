import { useEffect } from "react";
import Productcart from './ProductCart';
import { useDispatch, useSelector } from "react-redux";
import { getProducts , deleteProduct } from "../../actions/products";

const Allproduct = () => {

    const dispatch = useDispatch()
    const {products} = useSelector((state)=> state.products)
    
    useEffect(()=> {
      dispatch(getProducts())
      console.log(products);
    } , [])
    
    const handleDelete = ( id ) => {
      if(window.confirm("Siz xaqiqatdan ham bu maxsulotni ochirmoqchimisiz")){
        dispatch(deleteProduct(id))
      }
    }
    
    return (
        <Productcart product={products} deleteProduct={handleDelete}/>
    );
}

export default Allproduct;
