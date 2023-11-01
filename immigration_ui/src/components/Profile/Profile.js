import React from 'react'
import { Badge, Button, Card, Col, Nav, Row, Tab, Table, } from 'react-bootstrap'
import randomColor from "randomcolor";
import PageHeader from 'layouts/PageHeader/PageHeader';
import * as petitionerGraph from "./GraphData";
import { Bar, Line } from 'react-chartjs-2';


export default function Profile() {

    const emp_rev = [
        { key: "Number of Employees", us: 45, global: 60 },
        { key: "Gross Revenue", us: 45465, global: 89265 },
        { key: "Net Revenue", us: 9289, global: 9289 }
    ]


    const ContactCard = () => {
        return <Card className="custom-card border rounded-5">
            <Card.Body>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-user fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Last Name</p>
                        <p className="tx-12 text-muted">Test Last Name</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-user fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">First Name</p>
                        <p className="tx-12 text-muted">Test First Name</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-pencil-alt fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Job Title</p>
                        <p className="tx-12 text-muted">CEO</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-mobile fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Phone</p>
                        <p className="tx-12 text-muted">+1 135792468</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-email fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Email</p>
                        <p className="tx-12 text-muted mb-0">harvey@gmail.com.</p>
                    </div>
                </div>
            </Card.Body>
        </Card>
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Profile" BreadcrumbItemList={[{ name: 'Profile' }]} />

            <Row className="row-sm">
                <Col md={12}>
                    <Tab.Container
                        id="center-tabs-example"
                        defaultActiveKey="Overview"
                        className="bg-gray-100"
                    >
                        <Row className="row-sm square">
                            <Card className="custom-card">
                                <Card.Body>
                                    <div className="panel profile-cover">
                                        <div className="profile-cover__img">
                                            <img src={require("../../assets/img/users/1.jpg")} alt="img" />
                                            <h3 className="h3">Google</h3>
                                        </div>
                                        <div className="profile-cover__action bg-img" style={{
                                            background: 'linear-gradient(90deg,' + randomColor() + ' 0%, ' + randomColor() + ' 100%)'
                                        }}></div>
                                        <div className="profile-tab" style={{
                                            marginTop: '6rem'
                                        }}>
                                            <Nav variant="pills" className="p-2 bg-primary-transparent rounded-5">
                                                <Nav.Item>
                                                    <Nav.Link eventKey="Overview" className='mx-3'>Overview</Nav.Link>
                                                </Nav.Item>
                                                <Nav.Item>
                                                    <Nav.Link eventKey="Incorporation" className='mx-3'>Incorporation Data</Nav.Link>
                                                </Nav.Item>
                                                <Nav.Item>
                                                    <Nav.Link eventKey="Employee" className='mx-3'>Employee & Revenue Data</Nav.Link>
                                                </Nav.Item>
                                                <Nav.Item>
                                                    <Nav.Link eventKey="Immigration" className='mx-3'>Immigration Data</Nav.Link>
                                                </Nav.Item>
                                                <Nav.Item>
                                                    <Nav.Link eventKey="Authorized" className='mx-3'>Authorized Signatory Info</Nav.Link>
                                                </Nav.Item>
                                                <Nav.Item>
                                                    <Nav.Link eventKey="Contact" className='mx-3'>Contact Info</Nav.Link>
                                                </Nav.Item>
                                            </Nav>
                                        </div>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Row>
                        <Row className="row-sm">
                            <div className="card custom-card main-content-body-profile">
                                <Tab.Content>
                                    <Tab.Pane eventKey="Overview">
                                        <Card className="custom-card main-content-body-profile mb-0">
                                            <div className="tab-content">
                                                <div className="main-content-body tab-paneactive p-3 active">
                                                    <h4 className="tx-15 d-inline text-uppercase mb-3">
                                                        Overview
                                                    </h4>
                                                    <Button variant="primary" size="sm" className='float-end'>
                                                        Total Active Beneficiaries  <Badge bg="light" className="ms-3">16</Badge>
                                                        <span className="visually-hidden">unread messages</span>
                                                    </Button>
                                                    <Row className='mt-4'>
                                                        <Col xl={6}>
                                                            <div className="d-flex justify-content-between">
                                                                <div>
                                                                    <label className="main-content-label my-auto pt-2">
                                                                        Total Projects
                                                                    </label>
                                                                    <span className="d-block tx-12 mb-0 mt-1 text-muted">
                                                                        Revenue is the total amount of income generated by
                                                                        the sale of goods.
                                                                    </span>
                                                                </div>
                                                            </div>

                                                            <div className="chart-wrapperchart-dropshadow2 ht-300">
                                                                <Line options={petitionerGraph.linechartoptions} data={petitionerGraph.linechart} className="barchart chart-dropshadow2 ht-300 chartjs-render-monitor" height="100" />
                                                            </div>
                                                        </Col>
                                                        <Col xl={6}>
                                                            <div className="d-flex justify-content-between">
                                                                <div>
                                                                    <label className="main-content-label my-auto pt-2">
                                                                        Total Immigration Spend
                                                                    </label>
                                                                    <span className="d-block tx-12 mb-0 mt-1 text-muted">
                                                                        Revenue is the total amount of income generated by
                                                                        the sale of goods.
                                                                    </span>
                                                                </div>
                                                            </div>
                                                            {/* <div className="chart-wrapperchart-dropshadow2 ht-300">
                                                                                                                <Line options={petitionerGraph.linechartoptions1} data={petitionerGraph.linechart1} className="barchart chart-dropshadow2 ht-300 chartjs-render-monitor" height="100" />
                                                                                                            </div> */}
                                                            <div className="chartjs-wrapper-demo ht-300">
                                                                <Bar
                                                                    options={petitionerGraph.Barchart1}
                                                                    data={petitionerGraph.barchart1data}
                                                                    className="barchart"
                                                                    height="300"
                                                                    style={{ paddingTop: "35px" }}
                                                                />
                                                            </div>
                                                        </Col>
                                                    </Row>
                                                </div>
                                            </div>
                                        </Card>
                                    </Tab.Pane>

                                    <Tab.Pane eventKey="Incorporation">
                                        <Card className="custom-card main-content-body-profile mb-0">
                                            <div className="tab-content">
                                                <div className="main-content-body tab-paneactive p-3 active">
                                                    <h4 className="tx-15 text-uppercase">
                                                        Company Incorporation Data
                                                    </h4>
                                                    <div className="main-contact-info-body py-0">
                                                        <div className="media-list">
                                                            <div className="media">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Legal Name:</label>
                                                                        <span className="tx-medium">Test Data</span>
                                                                    </div>
                                                                    <div>
                                                                        <label>D/B/A Name:</label>
                                                                        <span className="tx-medium">Test Data Name</span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="media">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Year Established:</label>
                                                                        <span className="tx-medium">
                                                                            2020
                                                                        </span>
                                                                    </div>
                                                                    <div>
                                                                        <label>Business Type:</label>
                                                                        <span className="tx-medium">Information technology</span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="media mb-0">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>FEIN:</label>
                                                                        <span className="tx-medium">
                                                                            00-0000000
                                                                        </span>
                                                                    </div>
                                                                    <div>
                                                                        <label>NAICS Code:</label>
                                                                        <span className="tx-medium">
                                                                            00-000000
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="media">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Place Established:</label>
                                                                        <span className="tx-medium">
                                                                            012 Dashboard Apartments, San Francisco, California
                                                                            13245
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </Card>
                                    </Tab.Pane>

                                    <Tab.Pane eventKey="Employee">
                                        <Card className="custom-card main-content-body-profile mb-0">
                                            <div className="tab-content">
                                                <div className="main-content-body tab-paneactive p-3 active">
                                                    <h4 className="tx-15 text-uppercase mb-3">
                                                        Company Employee & Revenue Data
                                                    </h4>
                                                    <Row>
                                                        <Col lg={12}>
                                                            <Table className="table text-nowrap text-md-nowrap table-striped mg-b-0 border">
                                                                <thead>
                                                                    <tr>
                                                                        <th></th>
                                                                        <th><b>U.S.</b></th>
                                                                        <th><b>Global</b></th>
                                                                        <th><b>Combined</b></th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    {emp_rev.map((list, index) => (
                                                                        <tr key={index} data-index={index}>
                                                                            <th scope="row">{list.key}</th>
                                                                            <td>{list.us}</td>
                                                                            <td>{list.global} </td>
                                                                            <td>{list.us + list.global}</td>
                                                                        </tr>
                                                                    ))}
                                                                </tbody>
                                                            </Table>
                                                        </Col>
                                                    </Row>
                                                </div>
                                            </div>
                                        </Card>
                                    </Tab.Pane>

                                    <Tab.Pane eventKey="Immigration">
                                        <Card className="custom-card main-content-body-profile mb-0">
                                            <div className="tab-content">
                                                <div className="main-content-body tab-paneactive p-3 active">
                                                    <h4 className="tx-15 text-uppercase mb-3">
                                                        Company Immigration Data
                                                    </h4>
                                                    <div className="main-contact-info-body py-0">
                                                        <div className="media-list">
                                                            <div className="media">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Blanket L Approval Number:</label>
                                                                        <span className="tx-medium">34563242</span>
                                                                    </div>
                                                                    <div>
                                                                        <label>Blanket L Expiration Date:</label>
                                                                        <span className="tx-medium">25 Oct 2020</span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="media">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Is Petitioner on Blanket L?:</label>
                                                                        <span className="tx-medium">
                                                                            No
                                                                        </span>
                                                                    </div>
                                                                    <div>
                                                                        <label>Is Petitioner H-1B Dependent Employer?</label>
                                                                        <span className="tx-medium">Yes</span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="media mb-0">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Is Petitioner Willful Violator?</label>
                                                                        <span className="tx-medium">
                                                                            No
                                                                        </span>
                                                                    </div>
                                                                    <div>
                                                                        <label>H/L Employee %:</label>
                                                                        <span className="tx-medium">
                                                                            50%
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="media">
                                                                <div className="media-body">
                                                                    <div>
                                                                        <label>Place Established:</label>
                                                                        <span className="tx-medium">
                                                                            012 Dashboard Apartments, San Francisco, California
                                                                            13245
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </Card>
                                    </Tab.Pane>

                                    <Tab.Pane eventKey="Authorized">
                                        <Card className="custom-card main-content-body-profile mb-0">
                                            <div className="tab-content">
                                                <div className="main-content-body tab-paneactive p-3 active">
                                                    <h4 className="tx-15 text-uppercase mb-3">
                                                        Company Authorized Signatory Info
                                                    </h4>
                                                    <Row className="row-sm">
                                                        <Col sm={12} md={4}><ContactCard /></Col>
                                                        <Col sm={12} md={4}><ContactCard /></Col>
                                                    </Row>
                                                </div>
                                            </div>
                                        </Card>
                                    </Tab.Pane>

                                    <Tab.Pane eventKey="Contact">
                                        <Card className="custom-card main-content-body-profile mb-0">
                                            <div className="tab-content">
                                                <div className="main-content-body tab-paneactive p-3 active">
                                                    <h4 className="tx-15 text-uppercase mb-3">
                                                        Company Contact Info
                                                    </h4>
                                                    <Row className="row-sm">
                                                        <Col sm={12} md={4}><ContactCard /></Col>
                                                    </Row>
                                                </div>
                                            </div>
                                        </Card>
                                    </Tab.Pane>
                                </Tab.Content>
                            </div>
                        </Row>
                    </Tab.Container>
                </Col>
            </Row>
        </React.Fragment>
    )
}
