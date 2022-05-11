import React from "react";
import Home from "./Home";
import {Routes , Route} from "react-router-dom"
import Addproduct from "./omborlar/AddProduct";

const Sectionpage = () => {
  return (
    <div className="container mx-auto py-10 h-64 md:w-4/5 w-11/12 px-6 ">
      <div className="w-full h-full rounded border-solid border-2 border-gray-300 p-3 drop-shadow-lg">
          <Routes>
              <Route path="/" element={<Home/>}/>
              <Route path="/addProduct" element={<Addproduct/>}/>
          </Routes>
      </div>
    </div>
  );
};

export default Sectionpage;
