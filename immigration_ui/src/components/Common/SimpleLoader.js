import { Alert, Spinner } from "react-bootstrap"

export const SimpleLoader = () => {

    return <Alert className="login-alert alert alert-transparent text-start" role="alert" >
        <Spinner animation="border" role="status">
            <span className="visually-hidden"></span>
        </Spinner>
        <strong>Loading...</strong>
    </Alert >
} 