import React, { Fragment } from "react"
import { Dropdown, Container, Form, Nav, Navbar, InputGroup, } from "react-bootstrap"
import { useDispatch, useSelector } from "react-redux"
import { Link, useNavigate } from "react-router-dom"
import { setAppUser } from "store/slices/userSlice"

// FullScreen-end
function Header() {

  const navigate = useNavigate()
  const dispatch = useDispatch()

  const initialState = useSelector((state) => {
    return state['app-user']
  })

  //  headerToggleButton
  const headerToggleButton = () => {
    let body = document.querySelector("body")
    let innerWidth = window.innerWidth
    if (body !== !body) {
      if (innerWidth >= 992) {
        document.querySelector("body")?.classList.toggle("main-sidebar-hide")
        document.querySelector("body")?.classList.remove("main-sidebar-show")
      } else if (document.body.classList.contains("horizontalmenu")) {
        document.querySelector("body")?.classList.toggle("main-navbar-show")
        document.querySelector("body")?.classList.remove("main-sidebar-show")
        document.querySelector("body")?.classList.remove("main-sidebar-hide")
      } else {
        document.querySelector("body")?.classList.toggle("main-sidebar-show")
        document.querySelector("body")?.classList.remove("main-sidebar-hide")
      }
    }
  }

  const logout = () => {
    window.localStorage.clear()
    dispatch(setAppUser(null))
    // navigate("/authentication/login", { state: { logout: true } })
    window.location.href = `${process.env.PUBLIC_URL}/`
  }

  const Darkmode = () => {
    document.querySelector("body").classList.toggle("dark-theme")
  }
  return (
    <Fragment>
      <Navbar
        expand="lg"
        className="main-header side-header sticky"
      // style={{ marginBottom: "-64px" }}
      >
        <Container fluid className="main-container container-fluid">
          <div className="main-header-left">
            <Link
              to="#"
              className="main-header-menu-icon"
              id="mainSidebarToggle"
              onClick={() => headerToggleButton()}
            >
              <span></span>
            </Link>
            <div className="hor-logo">
              <Link
                to={`${process.env.PUBLIC_URL}/dashboard/`}
                className="main-logo"
              >
                <span>ImmiLytics</span>
                {/* <img
                  src={require("../../assets/img/logo.jpg")}
                  className="header-brand-img desktop-logo"
                  alt="logo"
                />
                <img
                  src={require("../../assets/img/logo.jpg")}
                  className="header-brand-img desktop-logo-dark"
                  alt="logo"
                /> */}
              </Link>
            </div>
          </div>
          <div className="main-header-center">
            <div className="responsive-logo">
              <Link to={`${process.env.PUBLIC_URL}/dashboard/`}>
                <h3>ImmiLytics</h3>
                {/* <img
                  src={require("../../assets/img/logo.jpg")}
                  className="mobile-logo"
                  alt="logo"
                /> */}
              </Link>
            </div>
            <InputGroup>
              <Form.Control
                type="search"
                className="rounded-0"
                placeholder="Search for anything..."
              />
              <InputGroup.Text className="btn search-btn">
                <i className="fe fe-search"></i>
              </InputGroup.Text>
            </InputGroup>
          </div>
          <div className="main-header-right">
            <Navbar.Toggle
              aria-controls="navbarSupportedContent-4"
              className="navresponsive-toggler"
            >
              <i className="fe fe-more-vertical header-icons navbar-toggler-icon"></i>
            </Navbar.Toggle>
            <div className="navbar navbar-expand-lg nav nav-item navbar-nav-right responsive-navbar navbar-dark">
              <Navbar.Collapse
                className="collapse navbar-collapse"
                id="navbarSupportedContent-4"
              >
                <div className="d-flex order-lg-2 align-items-center ms-auto">
                  <Dropdown className="header-search">
                    <Dropdown.Toggle variant="default" className="px-0">
                      <i className="fe fe-search header-icons fs-18 px-2 lh-5"></i>
                    </Dropdown.Toggle>
                  </Dropdown>
                  <Dropdown className="dropdown d-flex main-header-theme">
                    <Nav.Link
                      className="nav-link icon layout-setting"
                      onClick={() => Darkmode()}
                    >
                      <span className="dark-layout">
                        <i className="fe fe-sun header-icons"></i>
                      </span>
                      <span className="light-layout">
                        <i className="fe fe-moon header-icons"></i>
                      </span>
                    </Nav.Link>
                  </Dropdown>
                  <Dropdown className="main-profile-menu">
                    <Dropdown.Toggle className="d-flex p-0" variant="default">
                      <span className="main-img-user mx-1">
                        <img
                          alt="avatar"
                          src={require("../../assets/img/users/1.jpg")}
                        />
                      </span>
                    </Dropdown.Toggle>
                    <Dropdown.Menu style={{ margin: "0px" }}>
                      <div className="header-navheading">
                        <h6 className="main-notification-title">
                          {`${initialState.firstname} ${initialState.lastname}`}
                        </h6>
                        <p className="main-notification-text">{initialState.usertype}</p>
                      </div>
                      <Dropdown.Item
                        className="border-top"
                        href={`${process.env.PUBLIC_URL}/profile/`}
                      >
                        <i className="fe fe-user"></i> My Profile
                      </Dropdown.Item>
                      <Dropdown.Item
                        href={`${process.env.PUBLIC_URL}/pages/profile`}
                      >
                        <i className="fe fe-edit"></i> Edit Profile
                      </Dropdown.Item>
                      <Dropdown.Item
                        href={`${process.env.PUBLIC_URL}/pages/profile`}
                      >
                        <i className="fe fe-settings"></i> Account Settings
                      </Dropdown.Item>
                      <Dropdown.Item
                        href={`${process.env.PUBLIC_URL}/pages/profile`}
                      >
                        <i className="fe fe-settings"></i> Support
                      </Dropdown.Item>
                      <Dropdown.Item
                        onClick={logout}
                      >
                        <i className="fe fe-compass"></i> Sign Out
                      </Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                </div>
              </Navbar.Collapse>
            </div>
          </div>
        </Container>
      </Navbar>
    </Fragment>
  )
}

Header.propTypes = {}

Header.defaultProps = {}

export default Header
