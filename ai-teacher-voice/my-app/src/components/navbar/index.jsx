// Filename - "./components/Navbar.js
 
import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";
 
const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                <a href="http://localhost:5173/" target="_blank" rel="noopener noreferrer">
    Flight AI
</a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://localhost:3002/" target="_blank" rel="noopener noreferrer">
    Voice AI
</a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://localhost:5174/" target="_blank" rel="noopener noreferrer">
    Teacher AI
</a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://localhost:3001/" target="_blank" rel="noopener noreferrer">
    File Upload 
</a>

                </NavMenu>
            </Nav>
        </>
    );
};
 
export default Navbar;