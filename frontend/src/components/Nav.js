import React from "react";
import { FaHome } from "react-icons/fa";
import { FaList } from "react-icons/fa";
import { Link } from "react-router-dom";

export const Nav = () => {
  const iconStyle = { color: 'black' };
  
  return (
    <nav className="nav">
      <Link to="/">
        <FaHome style={iconStyle}/>
      </Link>
      <Link to="/plan">
        <FaList style={iconStyle}/>
      </Link>
      <Link to="/music">
        <FaList style={iconStyle}/>
      </Link>
    </nav>
  );
};
