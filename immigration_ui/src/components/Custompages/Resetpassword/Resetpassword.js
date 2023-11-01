import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import { Row, Col, Card, Container, Form } from "react-bootstrap";
import * as Customswitcherdata from "data/Switcherdata/Customswitcherdata";

const Resetpassword = () => (
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
              <Col
                lg={6}
                xl={5}
                className="d-none d-lg-block text-center bg-primary details"
              >
                <div className="mt-5 pt-5 p-2 pos-absolute">
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
                  <h5 className="mt-4 text-white">Reset Your Password</h5>
                  <span className="tx-white-6 tx-13 mb-5 mt-xl-0">
                    Signup to create, discover and connect with the global
                    community
                  </span>
                </div>
              </Col>
              <Col lg={6} xl={7} xs={12} sm={12} className=" login_form ">
                <Container fluid>
                  <Row className=" row-sm">
                    <Card.Body className="mt-2 mb-2">
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
                      <h5 className="text-start mb-2">Reset Your Password</h5>
                      <p className="mb-4 text-muted tx-13 ms-0 text-start">
                        It's free to signup and only takes a minute.
                      </p>
                      <Form>
                        <Form.Group className="text-start form-group" controlId="fromEmail">
                          <Form.Label>Email</Form.Label>
                          <Form.Control
                            placeholder="Enter your mail"
                            type="text"
                          />
                        </Form.Group>
                        <Form.Group
                          className="text-start form-group"
                          controlId="formNewPassword"
                        >
                          <Form.Label>New Password</Form.Label>
                          <Form.Control
                            placeholder="Enter your password"
                            type="email"
                          />
                        </Form.Group>
                        <Form.Group
                          className="text-start form-group"
                          controlId="formpassword"
                        >
                          <Form.Label>Password</Form.Label>
                          <Form.Control
                            placeholder="Enter your password"
                            type="password"
                          />
                        </Form.Group>

                        <button className="btn ripple btn-main-primary btn-block mt-2">
                          Create Account
                        </button>
                      </Form>
                      <div className="text-start mt-5 ms-0">
                        <p className="mb-0">
                          Already have an account?
                          <Link
                            to={`${process.env.PUBLIC_URL}/CustomPages/signin/`}>
                            Sign In
                          </Link>
                        </p>
                      </div>
                    </Card.Body>
                  </Row>
                </Container>
              </Col>
            </Row>
          </Card>
        </Col>
      </Row>
    </div>

    {/* <!-- End Row --> */}
  </Fragment>
);

Resetpassword.propTypes = {};

Resetpassword.defaultProps = {};

export default Resetpassword;
