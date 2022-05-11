import React, { useEffect, useState } from "react";
import { AiOutlineHome } from "react-icons/ai";
import { HiOutlineShoppingCart } from "react-icons/hi";
import {FaRegHandshake} from "react-icons/fa"
import logo from "./images/massdar.5701287b.png";
import {
  BsFillArrowLeftSquareFill,
  BsArrowRightSquareFill,
  BsBorderAll,
  BsTrash,
} from "react-icons/bs";
import Menuitem from "./MenuItem"
import Navbar from "./Navbar";
import axios from "axios";

function Sidebar(prompt) {

  

  const [inActive, setInActive] = useState(false);

  const menuItems = [
    { name: "Asosiy", to: `/`, icon: <BsBorderAll className="inline-block" /> },
    {
      to: "",
      name: "Omborlar",
      icon: <AiOutlineHome className="inline-block" />,
      subMenus: [
        { name: "Mahsulotlar", to: `/allProducts` },
        { name: "Kirim", to: `/kirim` },
        { name: "Omborlar", to: `/omborlar` },
        { name: "Kategoriya", to: `/category` },
        { name: "Sub-kategoriya", to: `/sub_category` },
      ],
    },
    {
      name: "Mahsulotlarni ko'chirish",
      to: ``,
      icon: <HiOutlineShoppingCart className="inline-block"
      />,
      subMenus: [
        { name: "Qabul qilingan", to: `/kelgan` },
        { name: "Jonatilgan", to: `/jonatilgan` },
      ],
    },
    {
      name: "Qaytarish",
      to: `/qaytarish`,
      icon: <FaRegHandshake className="inline-block" />,
    },
    {
      name: "Chiqit",
      to: `/chiqit`,
      icon: <BsTrash className="inline-block" />,
    },
  ];

  useEffect(() => {
    if (inActive) {
      document.querySelectorAll(".sub-menu").forEach((el) => {
        el.classList.remove("active");
      });
    }

    prompt.onCollapse(inActive)
  }, [inActive]);

  return (
    <>
    <Navbar/>
    <div
      className={`side-menu ${
        inActive ? "inactive" : ""
      } fixed bg-gray-100 w-80 h-full box-border p-5 duration-500`}
    >
      <div className="top-section relative h-10">
        <div
          onClick={() => setInActive(!inActive)}
          className="toggle-menu-btn text-3xl text-gray-500 absolute right-0 cursor-pointer"
        >
          {inActive ? (
            <BsArrowRightSquareFill />
          ) : (
            <BsFillArrowLeftSquareFill />
          )}
        </div>
      </div>
      <div className="divider w-full h-1 rounded bg-gray-500"></div>
      <div className="main-menu">
        <ul>
          {menuItems.map((item, index) => (
            <Menuitem
              key={index}
              name={item.name}
              to={item.to}
              subMenus={item.subMenus || []}
              icon={item.icon}
            />
          ))}
        </ul>
      </div>
      <div className="side-menu-footer w-full absolute bg-gray-800 bottom-0 left-0 py-8 px-5 box-border flex">
        <div className="avatar w-10 h-10 inline-block rounded-full bg-gray-300 p-1 flex justify-center items-center">
          <img src={logo} alt="logo " className="max-w-full " />
        </div>
        <div className="user-info text-gray-500 inline-block ml-5">
          <h5 className="">Amiral Retail ERP</h5>
          <p className="">by qwerty</p>
        </div>
      </div>
    </div>
    </>
  )
}

export default Sidebar;
