import React from "react";
import "components/Common/FullScreenLoader/index.style.scss";
import { Alert, Spinner } from "react-bootstrap";

export default function FullScreenLoader() {
    return (
        <div className="full-page">
            <Alert className={`login-alert alert alert-primary text-start`} role="alert">
                <Spinner animation="border" role="status">
                    <span className="visually-hidden"></span>
                </Spinner>
                <strong>Loading...</strong>
            </Alert>
        </div>
    );
}
