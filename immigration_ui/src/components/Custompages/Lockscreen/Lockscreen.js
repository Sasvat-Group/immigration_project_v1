import React, { Fragment } from "react";
import * as Customswitcherdata from "data/Switcherdata/Customswitcherdata";
import { Card, Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";

const Lockscreen = () => (
  <Fragment>
    <div className="page main-signin-wrapper">
      <div className="d-flex header-setting-icon demo-icon fa-spin" 
      onClick={() => Customswitcherdata.Swicherbutton()}
      >
        <Link className="nav-link icon" to="#" >
          <i className="fe fe-settings settings-icon "></i>
        </Link>
      </div>
      <Row className="signpages text-center"
       onClick={() => Customswitcherdata.remove()}
       >
        <Col md={12}>
          <Card>
            <Row className="row-sm">
              <Col lg={6} xl={5} className=" d-none d-lg-block bg-primary details">
                <div className="mt-4 pt-4 ps-5 ms-3 pe-5 pos-absolute">
                  <img
                    src={require("../../../assets/img/brand/logo-light.png")}
                    className="header-brand-img mb-4"
                    alt="logo"
                  />
                  <div className="clearfix"></div>
                  <img
                    src={require("../../../assets/img/svgs/user.svg").default}
                    className="ht-100 mb-0"
                    alt="user"
                  />
                  <h5 className="mt-4 text-white">Unlock</h5>
                  <span className="tx-white-6 tx-13 mb-5 mt-xl-0">
                    Enter your password to access the admin.
                  </span>
                </div>
              </Col>
              <Col lg={6} xl={7} xs={12} sm={12} className=" login_form ">
                <div className="main-container container-fluid">
                  <div className="row row-sm">
                    <div className="card-body main-profile-overview mt-3 mb-3">
                      <img
                        src={require("../../../assets/img/brand/logo.png")}
                        className=" d-lg-none header-brand-img text-start float-start mb-4 auth-light-logo"
                        alt="logo"
                      />
                      <img
                        src={require("../../../assets/img/brand/logo-light.png")}
                        className=" d-lg-none header-brand-img text-start float-start mb-4 auth-dark-logo"
                        alt="logo"
                      />
                      <div className="clearfix"></div>
                      <h5 className="text-start mb-2">Lockscreen</h5>
                      <p className="mb-4 text-muted tx-13 ms-0 text-start">
                        Unlock your screen by entering password
                      </p>
                      <form>
                        <div className="text-start d-flex float-start mb-4 user-lock">
                          <img
                            alt="avatar avatar-sm"
                            className="rounded-circle mb-0"
                            src={require("../../../assets/img/users/1.jpg")}
                          />
                          <div className="my-auto">
                            <p className="font-weight-semibold my-auto ms-2 text-uppercase ">
                              Sonia Taylor
                            </p>
                          </div>
                        </div>
                        <div className="form-group">
                          <input
                            className="form-control"
                            placeholder="Enter your password"
                            type="password"
                          />
                        </div>
                        <div className="text-start">
                          <label className="form-switch ps-0">
                            <input
                              type="checkbox"
                              name="form-switch-checkbox"
                              className="form-switch-input me-2"
                            />
                            <span className="form-switch-indicator"></span>
                            <span className="form-switch-description">
                              show password
                            </span>
                          </label>
                        </div>
                        <button className="btn ripple btn-main-primary btn-block mt-4">
                          Unlock
                        </button>
                      </form>
                    </div>
                  </div>
                </div>
              </Col>
            </Row>
          </Card>
        </Col>
      </Row>
    </div>

  </Fragment>
);
Lockscreen.propTypes = {};

Lockscreen.defaultProps = {};

export default Lockscreen;
