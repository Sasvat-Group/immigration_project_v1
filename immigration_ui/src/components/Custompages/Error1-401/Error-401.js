import React, { Fragment } from "react";
import { Col, Container } from "react-bootstrap";
import { Link } from "react-router-dom";
const Error401 = () => {
    document.querySelector("body").classList.add("error-1");
    return (
        <Fragment>
            {/* <!-- Page --> */}
            <div className="ltr main-body leftmenu">
                <div className="page main-signin-wrapper bg-primary construction">
                    <Container>
                        <div className="construction1 text-center details text-white">
                            <div>
                                <Col lg={12}>
                                    <h1 className="tx-140 mb-0">401</h1>
                                </Col>
                                <Col lg={12}>
                                    <h1>
                                        You are not authorized person to view
                                        this page
                                    </h1>
                                    <h6 className="tx-15 mt-3 mb-4 text-white-50">
                                        Try to re-login with right person to
                                        view this page
                                    </h6>
                                    <Link
                                        to={`${process.env.PUBLIC_URL}/`}
                                        className="btn ripple btn-success text-center mb-2"
                                    >
                                        Back to Login
                                    </Link>
                                </Col>
                            </div>
                        </div>
                    </Container>
                </div>
            </div>
            {/* <!-- End Page - */}
        </Fragment>
    );
};

Error401.propTypes = {};

Error401.defaultProps = {};

export default Error401;
