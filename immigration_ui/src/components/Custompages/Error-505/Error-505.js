import React, { Fragment } from "react";
import { Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";
const Error505 = () => (
  <Fragment >
    <div className="page">
      {/* <!-- Row --> */}
      <Row className="error-bg signpages text-center row">
        <Col md={12}>
          <div className="text-center">
            <div className="">
              <Col lg={12}>
                <h1 className="tx-140 mb-0">500</h1>
              </Col>
              <Col lg={12} >
                <h1>Oops.The Page you are looking for doesn't exit..</h1>
                <h6 className="tx-15 mt-3 mb-4 text-muted">
                  You may have mistyped the address or the page may have moved.
                  Try searching below.
                </h6>
                <Link
                    to={`${process.env.PUBLIC_URL}/dashboard/`}
                    className="btn ripple btn-success text-center mb-2"
                  >
                    Back to Home
                  </Link>
              </Col>
            </div>
          </div>
        </Col>
      </Row>
      {/* <!-- End Row --> */}
    </div>
    
  </Fragment>
);

Error505.propTypes = {};

Error505.defaultProps = {};

export default Error505;
