import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getCategory, getSubCategory } from '../../actions/category';

const Category = () => {

    const dispatch = useDispatch()
    const {category} = useSelector((state) => state.category)
    console.log(category);

    useEffect(()=>{
        dispatch(getCategory())
        dispatch(getSubCategory)
    } , [] )

    return (
        <div>
            Category
        </div>
    );
}

export default Category;
