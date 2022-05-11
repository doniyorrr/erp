import axios from "axios";
import React, { useState, useEffect } from "react";
import { ToastContainer, toast } from "react-toastify";

const Login = () => {
  let url = "http://127.0.0.1:8000/api/users/login/";

  const [data, setData] = useState({
    username: "",
    password: "",
  });

  const body = JSON.stringify(data);

  const config = {
    headers: {
      Authorization: localStorage.getItem("access"),
      "Content-Type": "application/json",
      accept: "application/json",
    },
  };

  const handle = (e) => {
    const newData = { ...data };
    newData[e.target.id] = e.target.value;
    setData(newData);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    axios
      .get(url, body)
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err));
    toast("salom");
  };

  // };
  return (
    <div className=" flex">
      <div className="w-full max-w-md m-auto bg-gray-100 rounded-lg border border-primaryBorder shadow-default py-10 px-16">
        <h1 className="text-2xl font-medium text-primary mt-4 mb-12 text-center">
          Log in to your account 🔐
        </h1>

        <form onSubmit={handleFormSubmit}>
          <div>
            <label htmlFor="username">Username</label>
            <input
              type="text"
              className={`w-full p-2 text-primary border rounded-md outline-none text-sm transition duration-150 ease-in-out mb-4`}
              id="username"
              placeholder="Username"
              value={data.username}
              onChange={(e) => handle(e)}
            />
          </div>
          <div>
            <label htmlFor="password">Password</label>
            <input
              type="password"
              className={`w-full p-2 text-primary border rounded-md outline-none text-sm transition duration-150 ease-in-out mb-4`}
              id="password"
              placeholder="Your Password"
              value={data.password}
              onChange={(e) => handle(e)}
            />
          </div>

          <div className="flex justify-center items-center mt-6">
            <button
              onClick={(e) => handle(e)}
              className={`bg-green-500 py-2 px-4 text-sm text-white rounded border border-green focus:outline-none focus:border-green-dark`}
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
