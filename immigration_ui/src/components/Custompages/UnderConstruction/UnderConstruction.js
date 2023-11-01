import React, { Fragment } from "react";
import * as Customswitcherdata from "data/Switcherdata/Customswitcherdata";
import { Link } from "react-router-dom";

const UnderConstruction = () => (
  <Fragment>
    {/* <!-- Page --> */}
    <div className="page main-signin-wrapper bg-primary construction"  >
      <div className="d-flex header-setting-icon demo-icon fa-spin">
        <Link className="nav-link icon" to="#"
          onClick={() => Customswitcherdata.Swicherbutton()}
        >
          <i className="fe fe-settings settings-icon "></i>
        </Link>
      </div>
      <div className="construction1 text-center details text-white"
        onClick={() => Customswitcherdata.remove()}
      >
        <div>
          <img
            src={require("../../../assets/img/brand/logo-light.png")}
            className="mb-5"
            alt="logo"
          />
          <h4 className="text-center text-white tx-30 font-weight-bold ">
            We are Comming soon
          </h4>
          <p className="text-white-50 tx-15">
            We're making the system more awesome.we'll be back shortly.
          </p>
          <div id="launch_date">
            {/* <DayCounter /> */}
          </div>
        </div>
        <div className="text-center">
          © 2022
          <a href="https://www.spruko.com/" className="text-white-50 mx-2">
            Spruko
          </a>
          All rights reserved.
        </div>
      </div>

    </div>
    {/* <!-- End Page --> */}
  </Fragment>
);

UnderConstruction.propTypes = {};

UnderConstruction.defaultProps = {};

export default UnderConstruction;
