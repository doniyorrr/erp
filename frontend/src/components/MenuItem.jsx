import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const Menuitem = (props) => {
  const { name, subMenus, icon, to } = props;
  const [active, setActive] = useState(false);

  return (
    <li className="" onClick={props.onClick}>
      <NavLink
        onClick={() => setActive(!active)}
        to={to}
        className="menu-item block text-gray-500 text-base font-semibold active:bg-gray-500 active:text-gray-900"
      >
        <div className="menu-icon inline-block w-10 h-10 text-xl text-center leading-10">
          {icon}
        </div>
        <span className="absolute inline-block leading-10 transition ease-in duration-200 ">
          {name}
        </span>
      </NavLink>
      {subMenus && subMenus.length > 0 ? (
        <ul
          className={`sub-menu ${
            active ? "active" : ""
          } hidden text-gray-500 ml-5 pl-8 border-solid border-gray-500 border-l`}
        >
          {subMenus.map((menu, index) => (
            <li key={index}>
              <NavLink to={menu.to}>{menu.name}</NavLink>
            </li>
          ))}
        </ul>
      ) : null}
    </li>
  );
};

export default Menuitem;
