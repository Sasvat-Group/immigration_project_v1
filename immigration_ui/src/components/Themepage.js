import React, { Fragment } from "react";
import Sidebar from "../layouts/SideBar/SideBar";
import Footer from "../layouts/Footer/Footer";
import Switcher from "../layouts/Switcher/Switcher";
import Rightside from "../layouts/Rightside/Rightside";
import { Backtotop1 } from "../layouts/Backtotop/Backtotop";
import Switcherpage from "./Pages/Switcherpage/Switcherpages";
export default function Themepage() {
  const remove = () => {
    document.querySelector(".sidebar-right").classList.remove("sidebar-open");
    document.querySelector(".demo_changer").classList.remove("active");
    document.querySelector(".demo_changer").style.right = "-270px";
  };
  return (
    <Fragment>
      <div className="horizontalMenucontainer">
        <div className="page">
          <Sidebar />
          <div className="main-content side-content">
            <div className="main-container container-fluid" onClick={() => remove()}>
              <div className="inner-body" >
                <Switcherpage />
              </div>
            </div>
          </div>
          <Rightside />
        </div>
        <Backtotop1 />
        <Switcher />
        <Footer />
      </div>
    </Fragment>
  );
};

