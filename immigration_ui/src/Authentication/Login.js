import jwt from 'jwt-decode'
import { Fragment, useEffect, useState } from "react"
import { Alert, Button, Card, Col, Container, Form, Row, Spinner } from "react-bootstrap"
import { useDispatch, useSelector } from "react-redux"
import { Link, useNavigate } from "react-router-dom"
import { loginService } from "services/login.service"
import { setAppUser } from "store/slices/userSlice"
import validator from "hooks/tokenValidation"

/* --------------------------------- Login Component --------------------------------- */

const SignIn = () => {

    /* ------------------------------ Hooks ----------------------------- */

    const dispatch = useDispatch()
    const navigate = useNavigate()

    const SuccessCheck = () => <i className="fa fa-check"></i>
    const FailedCheck = () => <i className="fa fa-times"></i>

    const appUser = useSelector((state) => {
        return state["app-user"]
    })

    const [err, setError] = useState("")
    const [data, setData] = useState({
        email: "tony@immilytics.com",
        password: "password",
        alert: {
            status: "loading",
            class: "",
            message: "",
        },
    })

    const tokenRevalidate = () => {

        if (appUser && appUser.token && validator(appUser.token))
            return true

        return false
    }

    /* ------------------------- onInit ------------------------ */

    useEffect(() => {

        if (tokenRevalidate()) {

            if (appUser && appUser.usertype === 'Beneficiary')
                navigate("/beneficiary/")
            else
                navigate("/dashboard/")
        }

    }, [])

    /* ---------------------------------- Methods ---------------------------------- */

    const routeChange = (token) => {

        const user = jwt(token)

        let path

        if (user && user.usertype === 'Beneficiary')
            path = `${process.env.PUBLIC_URL}/beneficiary/`
        else
            path = `${process.env.PUBLIC_URL}/dashboard/`

        setTimeout(() => navigate(path), 600)
    }

    const handleLogin = () => {
        setData((prev) => ({
            ...prev,
            alert: {
                status: "loading",
                class: "primary",
                message: "Signing in...",
            },
        }))

        loginService
            .signIn({
                username: data.email,
                password: data.password,
            })
            .then((res) => {

                if (res.data.token && validator(res.data.token)) {

                    dispatch(setAppUser(res.data.token))

                    setData((prev) => ({
                        ...prev,
                        alert: {
                            status: "success",
                            class: "success",
                            message: "Login Success",
                        },
                    }))
                    routeChange(res.data.token)
                }
            })
            .catch((err) => {
                // console.log(err)
                setData((prev) => ({
                    ...prev,
                    alert: {
                        status: "failed",
                        class: "danger",
                        message: "Login Failed - " + err.response?.data?.Error,
                    },
                }))

            })
    }

    const changeHandler = (e) => {
        setData({ ...data, [e.target.name]: e.target.value })
        setError("")
    }

    const LoginAlert = () => {

        const StatusIcon = () => {
            switch (data.alert.status) {
                case "loading":
                    return (
                        <Spinner animation="border" role="status">
                            <span className="visually-hidden"></span>
                        </Spinner>
                    )
                case "success":
                    return <SuccessCheck />
                case "failed":
                    return <FailedCheck />
                default:
                    return <FailedCheck />
            }
        }

        if (data.alert.message)
            return (
                <Alert className={`login-alert alert alert-${data.alert.class} text-start`} role="alert">
                    <StatusIcon />
                    {data.alert.message}
                </Alert>
            )
    }

    /* ---------------------------- Render ---------------------------- */

    return (
        <>
            <Fragment>
                {/* <!-- Row --> */}
                <div className="page main-signin-wrapper">
                    <Row className="signpages text-center">
                        <Col md={12}>
                            <Card>
                                <Row className="row-sm">
                                    <Col lg={6} xl={5} className="d-none d-lg-block text-center bg-primary">
                                        <div className="mt-5 pt-5">
                                            <img src={require("assets/img/logo.jpg")} className="header-brand-img mb-4 p-4 bg-white rounded" alt="logo-light" />
                                            <h5 className="mt-4 text-white">Create Your Account</h5>
                                            <span className="tx-white-6 tx-13 mb-5 mt-xl-0">Signup to create, discover and connect with the global community</span>
                                        </div>
                                    </Col>
                                    <Col lg={6} xl={7} xs={12} sm={12} className="login_form ">
                                        <Container fluid>
                                            <Row className="row-sm">
                                                <Card.Body className="mt-2 mb-2">
                                                    <div className="clearfix"></div>
                                                    {err && <Alert variant="danger">{err}</Alert>}
                                                    <Form onSubmit={(e) => e.preventDefault()}>
                                                        <h5 className="text-start mb-2">Signin to Your Account</h5>
                                                        <p className="mb-4 text-muted tx-13 ms-0 text-start">Signin to create, discover and connect with the global community</p>
                                                        <LoginAlert />
                                                        <Form.Group className="text-start form-group" controlId="formEmail">
                                                            <Form.Label>Email</Form.Label>
                                                            <Form.Control className="form-control" placeholder="Enter your email" name="email" type="text" value={data.email} onChange={changeHandler} required />
                                                        </Form.Group>
                                                        <Form.Group className="text-start form-group" controlId="formpassword">
                                                            <Form.Label>Password</Form.Label>
                                                            <Form.Control className="form-control" placeholder="Enter your password" name="password" type="password" value={data.password} onChange={changeHandler} required />
                                                        </Form.Group>
                                                        <Button type="submit" onClick={() => handleLogin()} className="btn ripple btn-main-primary btn-block mt-2">
                                                            Sign In
                                                        </Button>
                                                    </Form>
                                                    <div className="text-start mt-5 ms-0">
                                                        <div className="mb-1">
                                                            <Link to="#"> Forgot password ?</Link>
                                                        </div>
                                                        <div>
                                                            Don't have an account?
                                                            <Link to={`${process.env.PUBLIC_URL}/authentication/signup`}> Resgister Here</Link>
                                                        </div>
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
        </>
    )
}

SignIn.propTypes = {}

SignIn.defaultProps = {}

export default SignIn
