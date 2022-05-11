import React, { useEffect, useState } from "react";
import { connect } from "react-redux";
import { NavLink } from "react-router-dom";
import { addProducts } from "../../actions/products";
import Input from "../ui/Input";
import { useDispatch  } from "react-redux";

const Addproduct = () => {
  
  let dispatch = useDispatch()

  const [data, setData] = useState({
    supplier: 1,
    category: 1,
    sub_category: 1,
    name: "lays",
    price: "2000",
    bar_code: "1258963",
  });

  const submit = (e) => {
    e.preventDefault();
    dispatch(addProducts({
      bar_code: data.bar_code,
      category : parseInt(data.category),
      name: data.name,
      price: parseInt(data.price),
      sub_category: parseInt(data.sub_category),
      supplier:parseInt(data.supplier),
    }))
  };

  const handle = (e) => {
    // const newData = { ...data  };
    // newData[e.target.id] = e.target.value;
    // setData(newData);
    // console.log(newData[e.target.id]);
  };
  
  return (
    <>
      <form
        method="POST"
        onSubmit={(e) => submit(e)}
        className="border p-5 rounded bg-gray-100"
      >
        <div className="grid xl:grid-cols-3 xl:gap-6">
          {Object.keys(data).map((val , index) => (
            <Input key={index} val={val} data={data} handle={handle} />
          ))}
          
        </div>
        <button
          onClick={(e) => submit(e)}
          type="submit"
          className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Qoshish
        </button>
        <NavLink
          to="/allProducts"
          className="text-black bg-yellow-400 ml-3 hover:bg-yellow-500 focus:ring-4 focus:outline-none focus:ring-yellow-500 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-yellow-400 dark:hover:bg-yellow-600 dark:focus:ring-yellow-500"
        >
          Jami mahsulotlarni ko'rish
        </NavLink>
      </form>
    </>
  );
};

export default connect( null ,  { addProducts } ) (Addproduct);
