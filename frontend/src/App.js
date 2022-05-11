import { useState } from "react";
import { Route, Routes } from "react-router-dom";
import "./App.css";
import { ToastContainer } from "react-toastify";
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Addproduct from "./components/omborlar/AddProduct";
import Allproduct from "./components/omborlar/AllProduct";
import Omborlar from "./components/omborlar/Omborlar";
import Sidebar from "./components/Sidebar";
import Login from "./components/user/LogIn";
import Users from "./components/user/users";
import Category from "./components/omborlar/Category";

function App() {
  const [inActive, setInActive] = useState(false);

  return (
    <>
      <Sidebar
        onCollapse={(inactive) => {
          setInActive(inactive);
        }}
      />

      <div className={`section ${inActive ? "inactive" : ""}`}>
        <Routes>
          <Route path="/*" element={<Home />} />
          <Route path="/kirim" element={<Addproduct />} />
          <Route path="/allProducts" element={<Allproduct />} />
          <Route path="/omborlar" element={<Omborlar />} />
          <Route path="/login" element={<Login />} />
          <Route path="/users" element={<Users />} />
          <Route path="/category" element={<Category />} />
        </Routes>
      </div>
      <ToastContainer />
      {/* <Demo/> */}

      {/* <Footer/> */}
    </>
  );
}

export default App;
