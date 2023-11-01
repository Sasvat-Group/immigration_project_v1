import React, { Fragment } from "react";
import Landingpage from "./LandingPage/Landingpage";
const Landingpageapp = () => {
  document.querySelector("body").classList.add("app", "sidebar-mini", "ltr", "landing-page", "horizontalmenu");
  document.querySelector("body").classList.remove("main-body", "leftmenu");
  return (
    <Fragment>
      <Landingpage />
    </Fragment>
  );
};
export default Landingpageapp;
